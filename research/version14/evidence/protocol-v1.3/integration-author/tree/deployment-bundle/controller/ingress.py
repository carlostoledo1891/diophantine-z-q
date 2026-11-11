"""Protected-owner ingress. Signs observations, never manufactures approvals.

Candidate Git objects are data. One remote CAS commits complete signed append
tails and checkpoints; no App check or repository-policy mutation occurs here.
"""
from __future__ import annotations
import base64
import copy
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import sys

import runtime
from runtime import require,exact,canonical,decode_json,digest,Invalid
import audit_intake
import operator_ledger
import git_manifest
import manifest_transport
import github_fork_context
import ledger_evidence_bridge
from durable_intake import IntakeRecorder,AuditObservationSource

MAX_BATCH=2000
COLLECTOR_SHA='8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef'

class StagedStore:
    """Verified transaction-local log. Nothing becomes durable before one CAS."""
    def __init__(self,codec,entries,checkpoint,keys):
        self.codec=codec;self.keys=copy.deepcopy(keys)
        self.entries=copy.deepcopy(entries);self.checkpoint=copy.deepcopy(checkpoint)
        codec.verify(self.entries,self.keys,self.checkpoint)
    def read_verified(self):
        state=self.codec.verify(self.entries,self.keys,self.checkpoint)
        return copy.deepcopy(self.entries),copy.deepcopy(self.checkpoint),state
    def assert_current(self,expected):
        require(canonical(self.checkpoint)==canonical(expected),'staged checkpoint changed')
        self.codec.verify(self.entries,self.keys,self.checkpoint)
    def append(self,event,key_id,expected_checkpoint):
        self.assert_current(expected_checkpoint)
        self.entries,self.checkpoint=self.codec.append(self.entries,copy.deepcopy(event),key_id,self.keys,self.checkpoint)
        return copy.deepcopy(self.checkpoint)

class BareGitCollector:
    """Fetch approved base refs into a fresh bare store; never check out code."""
    def __init__(self,policy,transport,workdir,git_executable=None):
        self.policy=policy;self.transport=transport;self.workdir=Path(workdir).resolve()
        require(self.workdir.is_dir(),'collector work directory missing')
        self.git=git_executable or shutil.which('git')
        require(self.git and Path(self.git).is_absolute(),'trusted absolute Git executable required')
        self.repository=None

    def _run(self,args,environment):
        return self._run_argv([self.git,*args],environment)

    def _run_argv(self,argv,environment):
        try:
            result=subprocess.run(argv,env=environment,stdin=subprocess.DEVNULL,
                                  stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=1800,check=False)
        except Exception:
            raise Invalid('bare Git collection failed') from None
        require(result.returncode==0,'bare Git collection failed')
        require(len(result.stdout)<=1024*1024,'unexpected Git output size')
        return result.stdout

    def collect_pair(self,packet):
        require(digest(Path(git_manifest.__file__).read_bytes())==COLLECTOR_SHA,'approved collector code changed')
        require(type(packet.get('pull_request')) is int and packet['pull_request']>0,'invalid pull request')
        for side in ('base','head'):git_manifest.verify_manifest(packet[side])
        require(packet['git_hash']=='sha1','GitHub collector requires SHA1 Git objects')
        environment=git_manifest.git_environment()
        for key in list(environment):
            if key.startswith('PROTOCOL_') or key in ('GITHUB_TOKEN','GH_TOKEN'):
                environment.pop(key)
        self.repository=Path(tempfile.mkdtemp(prefix='objects-',dir=self.workdir))
        hooks=Path(tempfile.mkdtemp(prefix='empty-hooks-',dir=self.workdir))
        # The narrow token accessor authenticates App ID, installation and scope.
        # Keep credentials in child environment only, never argv or Git config.
        token=self.transport._access()
        require(type(token) is str and token and all(32<ord(c)<127 for c in token),'invalid installation token')
        header='AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+token).encode()).decode()
        settings=[('http.https://github.com/.extraheader',header),('credential.helper',''),
                  ('core.hooksPath',str(hooks)),('protocol.file.allow','never'),
                  ('fetch.recurseSubmodules','false'),('http.followRedirects','false')]
        environment['GIT_CONFIG_COUNT']=str(len(settings))
        for n,(key,value) in enumerate(settings):
            environment['GIT_CONFIG_KEY_'+str(n)]=key;environment['GIT_CONFIG_VALUE_'+str(n)]=value
        try:
            self._run(['init','--bare','--quiet',str(self.repository)],environment)
            self._run(['--no-replace-objects','-C',str(self.repository),'fetch','--quiet','--no-tags',
                '--depth=1','--no-recurse-submodules','--no-write-fetch-head',
                'https://github.com/'+self.policy.repository+'.git',
                '+refs/heads/'+self.policy.base_ref+':refs/heads/approved-base',
                '+refs/pull/'+str(packet['pull_request'])+'/head:refs/heads/approved-head'],environment)
            for side in ('base','head'):
                actual=self._run(['--no-replace-objects','-C',str(self.repository),'rev-parse',
                                  '--verify','refs/heads/approved-'+side],environment).decode().strip()
                require(actual==packet[side]['commit'],'remote Git ref differs from protected packet')
        finally:
            environment.clear();token=None;header=None
        # ObjectReader disables lazy fetch. Every tree and blob must be local and
        # is independently hashed by the pinned full collector, in bounded chunks.
        # Run the unchanged collector in a separately sanitized Python process.
        # Its nested Git processes inherit this environment, not controller keys.
        child_environment=git_manifest.git_environment()
        for key in list(child_environment):
            if key.startswith('PROTOCOL_') or key in ('GITHUB_TOKEN','GH_TOKEN','PYTHONPATH','PYTHONHOME','PYTHONSTARTUP'):
                child_environment.pop(key)
        result={}
        try:
            for side in ('base','head'):
                output=self.workdir/('verified-'+side+'-manifest.json')
                require(not output.exists(),'collector output already exists')
                self._run_argv([sys.executable,'-I','-B',str(Path(git_manifest.__file__).resolve()),
                    str(self.repository),packet[side]['commit'],'--output',str(output)],child_environment)
                require(output.is_file() and output.stat().st_size<=runtime.MAX_INPUT,'collector manifest output missing or oversized')
                result[side]=git_manifest.load_json(output)
        finally:
            child_environment.clear()
        return result

def selector_ids(state,scope,selector):
    """Exact owner-authored selectors; no wildcard/latest/body-free matching."""
    require(type(selector) is dict,'classification selector required')
    material=state['materials'].get(scope,{})
    if set(selector)=={'material_id'}:
        require(selector['material_id'] in material,'unknown exact material ID')
        return [selector['material_id']]
    exact(selector,'report_id report_sha256','invalid report material selector')
    require(operator_ledger.text(selector['report_id']) and operator_ledger.hexhash(selector['report_sha256']),
            'invalid exact report selector')
    matches=[]
    for mid,value in material.items():
        if value['source']=='operator_ledger' and value['report_id']==selector['report_id']:
            raw=operator_ledger.raw64(value['record']['report']['body_base64'],operator_ledger.MAX_REPORT)
            if digest(raw)==selector['report_sha256']:matches.append(mid)
    require(len(matches)==1,'report selector does not identify one exact archived report')
    return matches

def apply_batch(remote,keys,policy,packet,selected_reports,batch,collector,reader):
    """Inputs come from approved owner-only controller checkout, not the PR."""
    packet=copy.deepcopy(packet);batch=copy.deepcopy(batch);selected_reports=copy.deepcopy(selected_reports)
    exact(batch,'schema id job_id mode key_ids operator_events external_materials findings classifications', 'invalid ingress batch')
    require(batch['schema']=='protocol-owner-ingress/v1' and batch['mode'] in ('capture','finalize'), 'unsupported ingress mode')
    require(operator_ledger.text(batch['id']) and operator_ledger.text(batch['job_id']),'missing batch identity')
    exact(batch['key_ids'],'operator intake collector','invalid ingress signing keys')
    for name in ('operator_events','external_materials','findings','classifications'):
        require(type(batch[name]) is list and len(batch[name])<=MAX_BATCH,'invalid or oversized ingress event list')
    require(type(selected_reports) is dict,'explicit protected report selection required')
    batch_digest=digest(canonical({'batch':batch,'packet':packet,'selected_reports':selected_reports}))
    remote.check()
    for path,raw in remote.current.entries.items():
        if not path.startswith('state/snapshots/'):continue
        saved=decode_json(raw)
        if saved.get('schema')=='protocol-ingress-receipt/v1' and saved.get('batch_id')==batch['id']:
            require(saved.get('batch_sha256')==batch_digest,'batch ID reused for different protected input')
            return {'already_committed':True,'receipt_sha256':digest(raw),'mode':saved['mode'],'merge_authorized':False}
    op_entries,op_cp=remote.entries('operator',operator_ledger,keys['operator'])
    in_entries,in_cp=remote.entries('intake',audit_intake,keys['intake'])
    operator=StagedStore(operator_ledger,op_entries,op_cp,keys['operator'])
    intake=StagedStore(audit_intake,in_entries,in_cp,keys['intake'])
    for event in batch['operator_events']:
        operator.append(event,batch['key_ids']['operator'],operator.checkpoint)
    # Sign only after full real object collection and exact metadata comparison.
    actual=collector.collect_pair(packet)
    exact(actual,'base head','collector did not return complete pair')
    envelopes={}
    for side in ('base','head'):
        require(canonical(actual[side])==canonical(packet[side]),'full verified collection differs from protected manifest')
        envelopes[side]=manifest_transport.seal(actual[side],{
            'repository_id':policy.repository_id,'commit':actual[side]['commit'],
            'tree':actual[side]['tree'],'collector_sha256':COLLECTOR_SHA},
            batch['key_ids']['collector'],keys['collector'][batch['key_ids']['collector']])
    recorder=IntakeRecorder(intake,operator,AuditObservationSource(reader),COLLECTOR_SHA,keys['collector'])
    recorder.capture(packet,envelopes,'owner-batch:'+batch['id'],batch['key_ids']['intake'],intake.checkpoint)
    scope=str(packet['repository_id'])+'/'+str(packet['pull_request'])
    for item in batch['external_materials']:
        exact(item,'source_id body_base64 observation_base64','invalid external material')
        intake.append(dict(item,kind='external_registered',scope=scope),batch['key_ids']['intake'],intake.checkpoint)
    for item in batch['findings']:
        exact(item,'finding_id body_base64 sources observation_base64','invalid owner finding')
        require(type(item['sources']) is list and item['sources'],'finding exact sources required')
        state=intake.read_verified()[2];mids=[]
        for selector in item['sources']:mids.extend(selector_ids(state,scope,selector))
        event={'kind':'finding_registered','scope':scope,'finding_id':item['finding_id'],
               'body_base64':item['body_base64'],'material_ids':mids,'observation_base64':item['observation_base64']}
        intake.append(event,batch['key_ids']['intake'],intake.checkpoint)
    state=intake.read_verified()[2];context=audit_intake.context_digest(state,scope)
    for item in batch['classifications']:
        exact(item,'source finding_ids reason observation_base64','invalid owner classification')
        mid=selector_ids(state,scope,item['source'])[0]
        event={'kind':'classified','scope':scope,'context_sha256':context,'material_id':mid,
               'finding_ids':item['finding_ids'],'reason':item['reason'],'observation_base64':item['observation_base64']}
        intake.append(event,batch['key_ids']['intake'],intake.checkpoint)
    if batch['mode']=='finalize':
        recorder.reconcile(packet)
        expected=ledger_evidence_bridge.targets(packet)
        require(set(selected_reports)==set(expected),'incomplete protected receipt selections')
        for key,(kind,target,sha,deps) in expected.items():
            operator_ledger.export_receipt(operator.entries,selected_reports[key],{
                'target_kind':kind,'target_id':target,'target_sha256':sha,'dependency_sha256':deps,
                'binding':intake.read_verified()[2]['captures']['owner-batch:'+batch['id']]['binding']},
                keys['operator'],operator.checkpoint)
    final_state=intake.read_verified()[2]
    unclassified=[mid for mid in final_state['materials'][scope]
                  if (scope,context,mid) not in final_state['classifications']]
    receipt={'schema':'protocol-ingress-receipt/v1','batch_id':batch['id'],'batch_sha256':batch_digest,
        'job_id':batch['job_id'],'mode':batch['mode'],'packet_sha256':digest(canonical(packet)),
        'selected_reports':selected_reports,'operator_checkpoint':operator.checkpoint,
        'intake_checkpoint':intake.checkpoint,'material_ids':sorted(final_state['materials'][scope]),
        'unclassified_material_ids':sorted(unclassified),'merge_authorized':False}
    additions={}
    for kind,store,old in (('operator',operator,op_entries),('intake',intake,in_entries)):
        for entry in store.entries[len(old):]:
            additions[f"state/entries/{kind}/{entry['sequence']:010d}.json"]=canonical(entry)
    raw=canonical(receipt);receipt_sha=digest(raw);additions['state/snapshots/'+receipt_sha+'.json']=raw
    checkpoints=copy.deepcopy(remote.current.index['checkpoints'])
    checkpoints.update(operator=operator.checkpoint,intake=intake.checkpoint)
    # One authoritative commit: the signed append tails and both checkpoints
    # advance together. Existing reports and unrelated publisher state remain.
    remote.advance(additions,checkpoints)
    return {'already_committed':False,'receipt_sha256':receipt_sha,'mode':batch['mode'],
            'unclassified_material_ids':sorted(unclassified),'merge_authorized':False}

def main(environment=None):
    env=os.environ if environment is None else environment
    checkout=runtime.ROOT.resolve()
    config=runtime.read_protected_json(checkout,'controller/config.json')
    api=runtime.ControllerHTTPS(config['controller_repository'],env['GITHUB_TOKEN'])
    guard=runtime.RevisionGuard(api,config['controller_repository'],config['controller_repository_id'],env['PROTOCOL_APPROVED_SHA'],env)
    guard.check();keys=runtime.load_keys(env)
    batch_path=env['PROTOCOL_INGRESS_BATCH']
    require(batch_path.startswith('controller/ingress-batches/'),'ingress batch must be in protected checkout directory')
    batch=runtime.read_protected_json(checkout,batch_path)
    jobs=[j for j in config['jobs'] if j['id']==batch['job_id']]
    require(len(jobs)==1,'ingress job not uniquely configured')
    publisher_config,policy,packet,selected=runtime.load_job(checkout,jobs[0])
    require(jobs[0]['collector_sha256']==COLLECTOR_SHA,'job selects a different collector implementation')
    from github_app_transport import GitHubAppTransport,TransportConfig,RS256Signer
    signer=RS256Signer.from_pem(env['PROTOCOL_APP_PRIVATE_KEY'].encode())
    app=GitHubAppTransport(TransportConfig(publisher_config.installation_id,publisher_config.repository_id),signer)
    reader=github_fork_context.ForkReadContext(policy,app)
    reader.api=runtime.CachingAPI(app)
    remote=runtime.RemoteState(runtime.GitState(api,config['controller_repository'],config['controller_repository_id']),guard)
    with tempfile.TemporaryDirectory(prefix='protocol-ingress-') as workdir:
        result=apply_batch(remote,keys,policy,packet,selected,batch,BareGitCollector(policy,app,workdir),reader)
    print(runtime.json.dumps(result,sort_keys=True));return 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception:
        print('Ingress stopped: protected input, observation, collection or state validation failed.',file=sys.stderr)
        sys.exit(2)
