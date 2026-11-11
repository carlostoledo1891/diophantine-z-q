"""Protected operator-attested session ledger, independent of candidate files.

Trust the operator's actual observations, not a model-provider signature. Secrets,
trusted checkpoints and observation capture must be outside candidate control.
This module creates no keys, reads no GitHub credentials and never authorizes merge.
"""
from approval_policy import approval_allowed
import base64
import hashlib
import hmac
import json
import re

DOMAIN=b'research-operator-ledger/v1\0'
MAX_OBSERVATION=1024*1024
MAX_REPORT=16*1024*1024

class Invalid(ValueError):pass
class IntegrationMissing(Invalid):pass

def need(ok,message):
    if not ok:raise Invalid(message)

def fields(value,names):need(type(value) is dict and set(value)==set(names.split()),'schema mismatch')
def text(value):return type(value) is str and bool(value.strip())
def hexhash(value,n=64):return type(value) is str and re.fullmatch('[0-9a-f]{%d}'%n,value) is not None
def canonical(value):return json.dumps(value,sort_keys=True,separators=(',', ':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def digest(value):return hashlib.sha256(canonical(value)).hexdigest()

def raw64(value,maximum):
    need(type(value) is str and len(value)<=4*((maximum+2)//3),'encoded evidence too large')
    try:raw=base64.b64decode(value,validate=True)
    except (ValueError,TypeError):raise Invalid('bad evidence encoding') from None
    need(0<len(raw)<=maximum and base64.b64encode(raw).decode()==value,'empty, oversized or noncanonical evidence')
    return raw

def binding(value):
    fields(value,'record_schema repository_id pull_request git_hash policy_sha256 base_commit base_tree head_commit head_tree base_manifest_sha256 head_manifest_sha256')
    need(type(value['record_schema']) is int and value['record_schema']==2,'unsupported record schema')
    need(all(type(value[k]) is int and value[k]>0 for k in ('repository_id','pull_request')),'invalid repository/PR identity')
    need(value['git_hash'] in ('sha1','sha256'),'invalid Git algorithm')
    width=40 if value['git_hash']=='sha1' else 64
    need(all(hexhash(value[k],width) for k in ('base_commit','base_tree','head_commit','head_tree')),'invalid commit/tree binding')
    need(all(hexhash(value[k]) for k in ('policy_sha256','base_manifest_sha256','head_manifest_sha256')),'invalid manifest/policy binding')

def genesis(ledger_id):
    need(text(ledger_id),'empty ledger identity')
    return {'schema':1,'ledger_id':ledger_id,'sequence':0,'entry_sha256':hashlib.sha256(DOMAIN+ledger_id.encode('utf-8')).hexdigest()}

def check_checkpoint(value):
    fields(value,'schema ledger_id sequence entry_sha256')
    need(type(value['schema']) is int and value['schema']==1 and text(value['ledger_id']),'invalid checkpoint')
    need(type(value['sequence']) is int and value['sequence']>=0 and hexhash(value['entry_sha256']),'invalid checkpoint position')

def trusted_key(registry,key_id):
    if registry is None:raise IntegrationMissing('protected operator key registry not supplied')
    need(type(registry) is dict and type(key_id) is str and key_id in registry,'unknown operator key')
    entry=registry[key_id];fields(entry,'operator_id secret')
    need(text(entry['operator_id']) and type(entry['secret']) is bytes and len(entry['secret'])>=32,'invalid operator key configuration')
    return entry

def empty_state():return {'runs':{},'freezes':{},'reports':{},'latest':{},'latest_reports':{},'observations':set()}

def apply_event(state,event,operator_id,sequence):
    need(type(event) is dict and event.get('kind') in ('run_observed','target_frozen','report_observed'),'unknown event kind')
    observation=event.get('observation');fields(observation,'capture_id tool raw_base64')
    need(text(observation['capture_id']) and observation['capture_id'] not in state['observations'],'duplicate or empty capture identity')
    need(observation['tool'] in ('collaboration','operator_capture'),'unknown observation source')
    raw64(observation['raw_base64'],MAX_OBSERVATION)
    state['observations'].add(observation['capture_id'])
    if event['kind']=='run_observed':
        fields(event,'kind observation run_id agent_id model tools')
        need(text(event['run_id']) and event['run_id'] not in state['runs'],'duplicate or empty run identity')
        need(text(event['agent_id']) and text(event['model']),'missing observed agent/model')
        need(type(event['tools']) is list and all(text(x) for x in event['tools']) and len(set(event['tools']))==len(event['tools']),'invalid tool inventory')
        state['runs'][event['run_id']]={'event':event,'operator_id':operator_id,'sequence':sequence}
    elif event['kind']=='target_frozen':
        fields(event,'kind observation freeze_id target_kind target_id target_sha256 dependency_sha256 binding author_runs')
        need(text(event['freeze_id']) and event['freeze_id'] not in state['freezes'],'duplicate or empty freeze identity')
        need(event['target_kind'] in ('application','finding','assembly') and text(event['target_id']),'invalid review target')
        need(hexhash(event['target_sha256']) and hexhash(event['dependency_sha256']),'invalid target/dependency digest')
        binding(event['binding']);authors=event['author_runs']
        need(type(authors) is list and authors and all(type(x) is str and x in state['runs'] for x in authors) and len(authors)==len(set(authors)),'unknown, duplicate or empty authorship')
        state['freezes'][event['freeze_id']]={'event':event,'operator_id':operator_id,'sequence':sequence}
        key=(digest(event['binding']),event['target_kind'],event['target_id'])
        state['latest'][key]=event['freeze_id']
    else:
        fields(event,'kind observation report_id run_id freeze_id decision scope body_base64')
        need(text(event['report_id']) and event['report_id'] not in state['reports'],'duplicate or empty report identity')
        need(type(event['run_id']) is str and event['run_id'] in state['runs'],'unobserved reviewer run')
        need(type(event['freeze_id']) is str and event['freeze_id'] in state['freezes'],'unfrozen report target')
        need(event['decision'] in ('accepted','changes_required','incomplete','rejected') and text(event['scope']),'invalid decision/scope')
        raw64(event['body_base64'],MAX_REPORT)
        state['reports'][event['report_id']]={'event':event,'operator_id':operator_id,'sequence':sequence}
        agent=state['runs'][event['run_id']]['event']['agent_id']
        state['latest_reports'][(event['freeze_id'],agent)]=event['report_id']

def verify(entries,trusted_keys=None,expected_checkpoint=None):
    if trusted_keys is None:raise IntegrationMissing('protected operator key registry not supplied')
    if expected_checkpoint is None:raise IntegrationMissing('trusted external checkpoint not supplied')
    check_checkpoint(expected_checkpoint)
    need(type(entries) is list and len(entries)==expected_checkpoint['sequence'],'ledger truncation or unexpected extension')
    start=genesis(expected_checkpoint['ledger_id']);previous=start['entry_sha256'];state=empty_state()
    for index,entry in enumerate(entries,1):
        fields(entry,'schema ledger_id sequence previous_sha256 key_id operator_id event mac')
        need(type(entry['schema']) is int and entry['schema']==1 and entry['ledger_id']==expected_checkpoint['ledger_id'],'wrong ledger/schema')
        need(type(entry['sequence']) is int and entry['sequence']==index and entry['previous_sha256']==previous,'broken ledger sequence/hash chain')
        key=trusted_key(trusted_keys,entry['key_id'])
        need(entry['operator_id']==key['operator_id'],'operator/key identity mismatch')
        need(hexhash(entry['mac']),'invalid MAC encoding')
        unsigned={k:v for k,v in entry.items() if k!='mac'}
        mac=hmac.new(key['secret'],DOMAIN+canonical(unsigned),hashlib.sha256).hexdigest()
        need(hmac.compare_digest(entry['mac'],mac),'invalid operator authentication')
        apply_event(state,entry['event'],entry['operator_id'],index)
        previous=digest(entry)
    need(previous==expected_checkpoint['entry_sha256'],'checkpoint does not match ledger head')
    return state

def append(entries,event,key_id,trusted_keys=None,expected_checkpoint=None):
    """Trusted capture process only: append one actual observed event.

    Returns new immutable-by-authentication data; caller atomically persists rows
    and advances a separately trusted checkpoint. No candidate import/auto-approval.
    """
    state=verify(entries,trusted_keys,expected_checkpoint)
    key=trusted_key(trusted_keys,key_id)
    next_sequence=len(entries)+1
    apply_event(state,event,key['operator_id'],next_sequence)
    entry={'schema':1,'ledger_id':expected_checkpoint['ledger_id'],'sequence':next_sequence,
        'previous_sha256':expected_checkpoint['entry_sha256'],'key_id':key_id,'operator_id':key['operator_id'],'event':event}
    entry['mac']=hmac.new(key['secret'],DOMAIN+canonical(entry),hashlib.sha256).hexdigest()
    checkpoint={'schema':1,'ledger_id':entry['ledger_id'],'sequence':next_sequence,'entry_sha256':digest(entry)}
    return entries+[entry],checkpoint

def export_receipt(entries,report_id,expected_target,trusted_keys=None,expected_checkpoint=None):
    """Export operator-attested evidence only, never model-provider attestation."""
    state=verify(entries,trusted_keys,expected_checkpoint)
    fields(expected_target,'target_kind target_id target_sha256 dependency_sha256 binding')
    binding(expected_target['binding'])
    need(report_id in state['reports'],'unknown observed report')
    record=state['reports'][report_id];report=record['event']
    freeze=state['freezes'][report['freeze_id']]['event']
    actual={k:freeze[k] for k in expected_target}
    need(canonical(actual)==canonical(expected_target),'stale or wrong target/binding')
    latest=(digest(freeze['binding']),freeze['target_kind'],freeze['target_id'])
    need(state['latest'][latest]==report['freeze_id'],'report predates refreshed target/authorship freeze')
    need(report['decision']=='accepted','report does not accept target')
    reviewer=state['runs'][report['run_id']]['event']
    need(state['latest_reports'][(report['freeze_id'],reviewer['agent_id'])]==report_id,'superseded reviewer decision')
    author_agents={state['runs'][r]['event']['agent_id'] for r in freeze['author_runs']}
    need(reviewer['agent_id'] not in author_agents,'authoring agent cannot independently accept')
    need(approval_allowed(freeze['binding']['repository_id'], reviewer['model']),
         'public required approval needs trusted exact gpt-6-astra run')
    raw=raw64(report['body_base64'],MAX_REPORT)
    return {'schema':'operator-attested-review-receipt/v1','report_id':report_id,'run_id':report['run_id'],
        'agent_id':reviewer['agent_id'],'model':reviewer['model'],'tools':reviewer['tools'],
        'decision':report['decision'],'scope':report['scope'],'report_sha256':hashlib.sha256(raw).hexdigest(),
        'body_base64':report['body_base64'],'target':actual,'author_runs':list(freeze['author_runs']),
        'operator_id':record['operator_id'],'ledger_checkpoint':dict(expected_checkpoint),
        'report_sequence':record['sequence'],'attestation_basis':'trusted operator observation',
        'provider_cryptographic_attestation':False,'merge_authorized':False}
