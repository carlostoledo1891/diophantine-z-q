"""Operator-authenticated audit intake with persistent revisions and classifications.

Trust the isolated recorder and configured keys; no provider attestation or merge
authority. The current checkpoint must survive independently of log restoration.
"""
import base64
import hashlib
import hmac
import operator_ledger as operators

Invalid=operators.Invalid
IntegrationMissing=operators.IntegrationMissing
need=operators.need
fields=operators.fields
text=operators.text
canonical=operators.canonical
digest=operators.digest
check_checkpoint=operators.check_checkpoint
trusted_key=operators.trusted_key
DOMAIN=b'research-audit-intake/v1\0'
MAX_EVENT=32*1024*1024
MAX_LOG=256*1024*1024
MAX_ENTRIES=10000

def genesis(ledger_id):
    need(text(ledger_id),'empty intake ledger identity')
    return {'schema':1,'ledger_id':ledger_id,'sequence':0,
            'entry_sha256':hashlib.sha256(DOMAIN+ledger_id.encode()).hexdigest()}

def scope(binding):
    operators.binding(binding)
    return str(binding['repository_id'])+'/'+str(binding['pull_request'])

def validate_scope(value):
    import re
    need(type(value) is str and re.fullmatch('[1-9][0-9]*/[1-9][0-9]*',value) is not None,'invalid intake scope')

def empty_state():
    return {'captures':{},'latest':{},'materials':{},'findings':{},'classifications':{}}

def materials_from(observation,reports):
    out={}
    fields(observation['intake'],'issue_comments reviews review_comments')
    for kind,rows in observation['intake'].items():
        need(type(rows) is list,'intake list required')
        ids=set()
        for row in rows:
            need(type(row) is dict and type(row.get('id')) is int and row['id']>0 and row['id'] not in ids,'invalid intake record identity')
            ids.add(row['id'])
            value={'source':'github','kind':kind,'record':row}
            out['github/'+kind+'/'+str(row['id'])+'/'+digest(row)]=value
    need(type(reports) is dict,'report inventory required')
    for rid,row in reports.items():
        need(text(rid) and type(row) is dict,'invalid report inventory')
        value={'source':'operator_ledger','report_id':rid,'record':row}
        out['report/'+digest(value)]=value
    return out

def context_digest(state, which):
    need(which in state['latest'],'no capture for scope')
    event=state['captures'][state['latest'][which]]
    return digest({'binding':event['binding'],'packet_sha256':event['packet_sha256'],
        'operator_checkpoint':event['operator_checkpoint'],'report_inventory_sha256':digest(event['reports']),
        'materials':state['materials'].get(which,{}),'findings':state['findings'].get(which,{})})

def apply_event(state,event,operator_id,sequence):
    need(type(event) is dict,'event required')
    kind=event.get('kind')
    if kind=='capture':
        fields(event,'kind capture_id binding packet_sha256 manifests observation operator_checkpoint reports')
        which=scope(event['binding'])
        need(text(event['capture_id']) and event['capture_id'] not in state['captures'],'repeated or empty capture ID')
        need(operators.hexhash(event['packet_sha256']),'invalid packet digest')
        operators.check_checkpoint(event['operator_checkpoint'])
        need(type(event['observation']) is dict and canonical(event['observation'].get('binding'))==canonical(event['binding']),'capture binding mismatch')
        fields(event['manifests'],'base head')
        for side,value in event['manifests'].items():
            fields(value,'manifest_sha256 transport_envelope')
            need(operators.hexhash(value['manifest_sha256']) and type(value['transport_envelope']) is dict,'missing collector provenance')
        materials=materials_from(event['observation'],event['reports'])
        archive=state['materials'].setdefault(which,{})
        for mid,value in materials.items():
            need(mid not in archive or canonical(archive[mid])==canonical(value),'material ID collision')
            archive[mid]=value
        state['captures'][event['capture_id']]=event
        state['latest'][which]=event['capture_id']
    elif kind=='external_registered':
        fields(event,'kind scope source_id body_base64 observation_base64')
        which=event['scope'];validate_scope(which)
        need(text(event['source_id']),'missing external source identity')
        operators.raw64(event['body_base64'],operators.MAX_REPORT)
        operators.raw64(event['observation_base64'],operators.MAX_OBSERVATION)
        value={'source':'external','source_id':event['source_id'],'body_base64':event['body_base64'],
               'observation_base64':event['observation_base64']}
        state['materials'].setdefault(which,{})['external/'+digest(value)]=value
    elif kind=='finding_registered':
        fields(event,'kind scope finding_id body_base64 material_ids observation_base64')
        which=event['scope'];validate_scope(which)
        need(text(event['finding_id']),'empty finding identity')
        operators.raw64(event['body_base64'],operators.MAX_REPORT)
        operators.raw64(event['observation_base64'],operators.MAX_OBSERVATION)
        ids=event['material_ids'];archive=state['materials'].get(which,{})
        need(type(ids) is list and ids and len(set(ids))==len(ids) and all(mid in archive for mid in ids),'unknown finding source material')
        findings=state['findings'].setdefault(which,{})
        need(event['finding_id'] not in findings,'finding IDs cannot be replaced or deleted')
        findings[event['finding_id']]={'body_base64':event['body_base64'],'material_ids':ids,
                                      'operator_id':operator_id,'sequence':sequence}
    elif kind=='classified':
        fields(event,'kind scope context_sha256 material_id finding_ids reason observation_base64')
        which=event['scope'];validate_scope(which)
        need(event['context_sha256']==context_digest(state,which),'classification has stale context')
        need(event['material_id'] in state['materials'].get(which,{}),'classification source missing')
        ids=event['finding_ids']
        need(type(ids) is list and len(set(ids))==len(ids) and all(fid in state['findings'].get(which,{}) for fid in ids),'classification finding missing')
        need(all(event['material_id'] in state['findings'][which][fid]['material_ids'] for fid in ids),'classification not linked to registered source')
        need(text(event['reason']),'classification requires reason, including no-finding decisions')
        operators.raw64(event['observation_base64'],operators.MAX_OBSERVATION)
        # Empty IDs explicitly attest no finding. That is an operator semantic
        # judgement, not an inference from a green check or accepted report.
        state['classifications'][(which,event['context_sha256'],event['material_id'])]=event
    else:
        raise Invalid('unknown intake event')

def verify(entries,trusted_keys=None,expected_checkpoint=None):
    if trusted_keys is None or expected_checkpoint is None:
        raise IntegrationMissing('trusted intake keys and external current checkpoint required')
    check_checkpoint(expected_checkpoint)
    need(type(entries) is list and len(entries)==expected_checkpoint['sequence'] and len(entries)<=MAX_ENTRIES,'intake log length mismatch or limit')
    state=empty_state();previous=genesis(expected_checkpoint['ledger_id'])['entry_sha256'];total=0
    for n,entry in enumerate(entries,1):
        raw=canonical(entry);total+=len(raw)
        need(len(raw)<=MAX_EVENT and total<=MAX_LOG,'intake byte limit')
        fields(entry,'schema ledger_id sequence previous_sha256 key_id operator_id event mac')
        need(type(entry['schema']) is int and entry['schema']==1 and entry['ledger_id']==expected_checkpoint['ledger_id'],'wrong intake schema or ledger')
        need(type(entry['sequence']) is int and entry['sequence']==n and entry['previous_sha256']==previous,'broken intake chain')
        key=trusted_key(trusted_keys,entry['key_id'])
        need(entry['operator_id']==key['operator_id'],'wrong intake operator')
        unsigned={k:v for k,v in entry.items() if k!='mac'}
        mac=hmac.new(key['secret'],DOMAIN+canonical(unsigned),hashlib.sha256).hexdigest()
        need(operators.hexhash(entry['mac']) and hmac.compare_digest(entry['mac'],mac),'invalid intake authentication')
        apply_event(state,entry['event'],entry['operator_id'],n);previous=digest(entry)
    need(previous==expected_checkpoint['entry_sha256'],'intake checkpoint mismatch')
    return state

def append(entries,event,key_id,trusted_keys=None,expected_checkpoint=None):
    state=verify(entries,trusted_keys,expected_checkpoint)
    need(len(entries)<MAX_ENTRIES,'intake entry limit')
    key=trusted_key(trusted_keys,key_id);n=len(entries)+1
    apply_event(state,event,key['operator_id'],n)
    entry={'schema':1,'ledger_id':expected_checkpoint['ledger_id'],'sequence':n,
           'previous_sha256':expected_checkpoint['entry_sha256'],'key_id':key_id,
           'operator_id':key['operator_id'],'event':event}
    entry['mac']=hmac.new(key['secret'],DOMAIN+canonical(entry),hashlib.sha256).hexdigest()
    result=entries+[entry]
    checkpoint={'schema':1,'ledger_id':entry['ledger_id'],'sequence':n,'entry_sha256':digest(entry)}
    verify(result,trusted_keys,checkpoint)
    return result,checkpoint

def reconcile(state,packet,operator_checkpoint,reports):
    """Return intake consistency only. Caller must authenticate state via store.

    This is not a VerifiedContext, and does not select/authorize review receipts.
    """
    import offline_manifest_gate as core
    bm,_=core.snapshot(packet['base'],packet['git_hash']);hm,_=core.snapshot(packet['head'],packet['git_hash'])
    binding=core.binding(packet,bm,hm);which=scope(binding)
    need(which in state['latest'],'missing captured context')
    current=state['captures'][state['latest'][which]]
    need(canonical(binding)==canonical(current['binding']) and digest(packet)==current['packet_sha256'],'captured candidate changed')
    need(canonical(operator_checkpoint)==canonical(current['operator_checkpoint']) and digest(reports)==digest(current['reports']),'operator ledger changed since capture')
    context=context_digest(state,which);archive=state['materials'].get(which,{})
    registered=state['findings'].get(which,{})
    mapped=set()
    for mid in archive:
        key=(which,context,mid)
        need(key in state['classifications'],'unclassified historical audit material')
        mapped.update(state['classifications'][key]['finding_ids'])
    need(mapped==set(registered),'registered finding omitted from material classification')
    findings=core.unique(packet['findings'],'id','findings')
    need(set(findings)==set(registered),'missing or extra registered finding')
    inventory=[]
    for fid,row in registered.items():
        need(all(fid in state['classifications'][(which,context,mid)]['finding_ids'] for mid in row['material_ids']),
             'registered finding source classified without that finding')
        body=operators.raw64(row['body_base64'],operators.MAX_REPORT)
        sha=hashlib.sha256(body).hexdigest();finding=findings[fid]
        need(finding['body_sha256']==sha,'registered finding body changed')
        need(finding['status'] in ('repaired','rebutted','duplicate','out_of_scope') and text(finding['reason']),'registered finding lacks disposition')
        inventory.append({'id':fid,'body_sha256':sha})
    return {'binding':binding,'findings':sorted(inventory,key=lambda v:v['id']),
            'context_sha256':context,'material_count':len(archive),
            'intake_consistent':True,'merge_authorized':False,'deployment_eligible':False}
