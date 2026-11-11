"""Bind reviewed V14 inputs as unsigned controller data; never submit or sign."""
import argparse, base64, hashlib, json, os, re, sys, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
PROTOCOL='3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9'
REPOS={'public':('elliotglazer/diophantine-z-q',1446122118),'private':('elliotglazer/private-diophantine',1447509909)}
def require(ok, message):
    if not ok: raise ValueError(message)
def sha(raw): return hashlib.sha256(raw).hexdigest()
def canonical(value): return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def pairs(rows):
    result={}
    for k,v in rows:
        require(k not in result,'duplicate JSON key: '+k); result[k]=v
    return result
def decode(raw): return json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))
def resolved(value):
    if isinstance(value,dict):
        require('$required' not in value,'unbound draft field')
        for v in value.values(): resolved(v)
    elif isinstance(value,list):
        for v in value: resolved(v)
    else: require(value!='__UNBOUND__','unbound draft value')
def pin(root, record):
    require(type(record) is dict and set(record)=={'path','sha256','bytes'},'expected exact raw input pin')
    path=Path(record['path']); require(not path.is_absolute() and '..' not in path.parts,'unsafe input path')
    target=(root/path).resolve(); require(target.is_relative_to(root.resolve()),'input escapes input root')
    raw=target.read_bytes(); require(len(raw)==record['bytes'] and sha(raw)==record['sha256'],'input pin mismatch: '+str(path))
    return raw

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bindings',type=Path,required=True); p.add_argument('--bindings-sha256',required=True)
    p.add_argument('--input-root',type=Path,required=True);p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--deployment',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); raw=a.bindings.read_bytes();require(sha(raw)==a.bindings_sha256,'bindings digest mismatch')
    b=decode(raw);resolved(b)
    require(set(b)=={'schema','side','job_id','batch_id','mode','target_mode','inputs'},'bindings schema fields')
    require(b['schema']=='v14-controller-bindings/v1' and b['side'] in REPOS,'bindings schema/side')
    require(b['mode'] in ('capture','finalize') and b['target_mode'] in ('head','merge'),'mode')
    require(re.fullmatch('[a-z0-9-]{1,80}',b['job_id']) and re.fullmatch('[a-z0-9-]{1,100}',b['batch_id']),'job/batch identity')
    required={'pull_request','base_manifest','head_manifest','applications','changes','findings','policy','profile_scope','selected_reports','existing_operator_events','new_operator_events','external_materials','intake_findings','classifications','required_merge_ci','scope_review','policy_review','observation_provenance','finding_inventory'}
    require(set(b['inputs'])==required,'missing or extra input roles')
    source={k:pin(a.input_root,v) for k,v in b['inputs'].items()}
    values={k:decode(v) for k,v in source.items() if k not in {'scope_review','policy_review','observation_provenance'}}
    require(all(source[k].strip() for k in ('scope_review','policy_review','observation_provenance')),'missing actual review or capture provenance')
    deployment=a.deployment.resolve(); pins=decode((HERE/'RUNTIME-PINS.json').read_bytes())
    for row in pins['files']:
        require(sha((deployment/row['path']).read_bytes())==row['sha256'],'deployed implementation changed: '+row['path'])
    sys.path.insert(0,str(deployment/'controller'));sys.path.insert(0,str(deployment/'adapter'))
    import runtime, git_manifest, offline_manifest_gate as g, operator_ledger as ledger, ledger_evidence_bridge as bridge, coverage_gate
    repo_name,repo_id=REPOS[b['side']]; pr=values['pull_request']; base=values['base_manifest']; head=values['head_manifest']
    require(type(pr.get('number')) is int and pr['number']>0 and pr.get('state')=='open','actual open PR observation required')
    require(pr['base']['repo']['id']==repo_id and pr['base']['repo']['full_name']==repo_name and pr['base']['ref']=='main','PR repository/base mismatch')
    require(pr['base']['sha']==base['commit'] and pr['head']['sha']==head['commit'],'PR/manifest commit mismatch')
    require(base['commit']!=head['commit'],'empty source transition')
    for manifest in (base,head):
        git_manifest.verify_manifest(manifest)
        require(canonical(git_manifest.collect(str(a.repo.resolve()),manifest['commit']))==canonical(manifest),'local full Git collection differs from supplied manifest')
    policy=values['policy']; scope=values['profile_scope']
    require(set(scope)=={'claim_ids','proof_paths','connection_record_path'},'profile scope fields')
    require(scope['claim_ids'] and scope['proof_paths'],'empty substantive scope')
    require((policy['repository'],policy['repository_id'],policy['base_ref'])==(repo_name,repo_id,'main'),'policy identity mismatch')
    profile={'schema':'protocol-coverage-policy/v2','protocol_version':'1.4','governing_protocol':{'path':'docs/research-review/PROTOCOL.md','sha256':PROTOCOL},'runtime_policy_sha256':policy['policy_sha256'],'mode':'substantive',**scope,'allowed_nonmath_paths':[]}
    packet={'schema':2,'repository_id':repo_id,'pull_request':pr['number'],'git_hash':'sha1','policy_sha256':policy['policy_sha256'],'base':base,'head':head,'changes':values['changes'],'applications':values['applications'],'findings':values['findings']}
    coverage_gate.select_profile(packet,profile)
    bm,_=g.snapshot(base,'sha1');hm,_=g.snapshot(head,'sha1');binding=g.binding(packet,bm,hm);targets=bridge.targets(packet)
    selected=values['selected_reports']; require(type(selected) is dict and set(selected)==set(targets),'complete explicit current report selection required')
    state=ledger.empty_state();events=values['existing_operator_events']+values['new_operator_events']
    require(events,'missing original operator observations')
    for i,event in enumerate(events,1): ledger.apply_event(state,event,'elliotglazer-research-operator',i)
    # These are unsigned observations. The deployed signed ledger remains authoritative.
    receipts=[];authorship={}
    for key,(kind,target_id,target_sha,dependency_sha) in targets.items():
        require(selected[key] in state['reports'],'selected report lacks original observation: '+key)
        report=state['reports'][selected[key]]['event'];freeze=state['freezes'][report['freeze_id']]['event']
        require(report['decision']=='accepted','selected report is not accepted: '+key)
        require((freeze['target_kind'],freeze['target_id'],freeze['target_sha256'],freeze['dependency_sha256'])==(kind,target_id,target_sha,dependency_sha),'stale observed target: '+key)
        require(g.same_binding(freeze['binding'],binding),'stale observed source binding: '+key)
        reviewer=state['runs'][report['run_id']]['event']['agent_id']
        require(reviewer not in {state['runs'][r]['event']['agent_id'] for r in freeze['author_runs']},'author selected as independent reviewer')
        require(state['latest'][(ledger.digest(binding),kind,target_id)]==report['freeze_id'],'superseded target freeze')
        require(state['latest_reports'][(report['freeze_id'],reviewer)]==selected[key],'superseded reviewer decision')
        body=ledger.raw64(report['body_base64'],ledger.MAX_REPORT)
        paths=sorted(path for path,x in head['files'].items() if x['sha256']==sha(body))
        require(paths,'original selected report body absent from source tree')
        if kind!='assembly': authorship[key]=freeze['author_runs']
        receipts.append({'id':'unsigned-observed:'+selected[key],'kind':kind,'target':target_id,'target_sha256':target_sha,'dependency_sha256':dependency_sha,'run_id':report['run_id'],'decision':report['decision'],'scope':report['scope'],'binding':binding,'report':{'side':'head','path':paths[0],'sha256':sha(body)}})
    evidence={'binding':binding,'policy_paths':policy['policy_paths'],'runs':[{'id':rid,'agent_id':row['event']['agent_id'],'reviewer_type':'model','model':row['event']['model'],'tools':row['event']['tools']} for rid,row in state['runs'].items()],'authorship':authorship,'findings':values['finding_inventory'],'receipts':receipts}
    structural=g.check_records(packet,evidence,g.GitBlobReader({'base':a.repo,'head':a.repo}),profile)
    packet_path=f"packets/{repo_id}/{pr['number']}/{head['commit']}/packet.json"
    reports_path=packet_path.replace('packet.json','selected-reports.json')
    job={'id':b['job_id'],'publisher':{'repository':repo_name,'repository_id':repo_id,'app_id':5663093,'installation_id':179741595,'base_ref':'main','target_mode':b['target_mode'],'required_merge_ci':values['required_merge_ci']},'policy':policy,'packet':packet_path,'selected_reports':reports_path,'collector_sha256':sha((deployment/'adapter/git_manifest.py').read_bytes()),'coverage_profile':profile}
    batch={'schema':'protocol-owner-ingress/v1','id':b['batch_id'],'job_id':b['job_id'],'mode':b['mode'],'key_ids':{'operator':'operator-20261107','intake':'intake-20261107','collector':'collector-20261107'},'operator_events':values['new_operator_events'],'external_materials':values['external_materials'],'findings':values['intake_findings'],'classifications':values['classifications']}
    for role in ('external_materials','findings','classifications'):
        require(type(batch[role]) is list,'ingress array required')
        for item in batch[role]: ledger.raw64(item['observation_base64'],ledger.MAX_OBSERVATION)
    config={'schema':'protocol-controller/v1','controller_repository':'elliotglazer/research-review-controller','controller_repository_id':1449903511,'jobs':[job]}
    require(not a.output.exists(),'output already exists')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='v14-bind-',dir=a.output.parent) as temp:
        stage=Path(temp)
        def write(path,value):
            target=stage/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(canonical(value)+b'\n')
        write(packet_path,packet);write(reports_path,selected)
        runtime.load_job(stage,job) # protected schema/source-transition checks, no network
        write('controller/config.json',config);write('controller/ingress-batches/'+b['batch_id']+'.json',batch)
        write('coverage-profile.json',profile);write('EXPECTED-TARGETS.json',targets)
        write('BINDING-CHECKS.json',{'schema':'v14-controller-preparation-checks/v1','status':'unsigned bound proposal; independent preparation review and real ingress required','source_head':head['commit'],'source_base':base['commit'],'bindings_sha256':a.bindings_sha256,'profile_canonical_sha256':g.digest(profile),'packet_canonical_sha256':g.digest(packet),'targets':len(targets),'observed_events':len(events),'network_used':False,'signed':False,'full_gate_evaluation':False,'limitations':'Original observation presence, IDs and exact bindings checked. Truth, freshness, completeness and signed-history consistency are verified by trusted ingress/evaluator and independent collection review, not this binder.'})
        write('UNVERIFIED-STRUCTURAL-RESULT.json',structural)
        write('INPUT-PINS.json',b['inputs'])
        manifest={p.relative_to(stage).as_posix():{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(stage.rglob('*')) if p.is_file()}
        write('MANIFEST.json',{'schema':'v14-controller-prepared-files/v1','files':manifest})
        os.rename(stage,a.output)
    print(json.dumps({'output':str(a.output),'status':'unsigned bound proposal','head':head['commit']}))
if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,TypeError,OSError) as exc: raise SystemExit('REFUSED: '+str(exc))
