"""Isolated, injected-transport GitHub App publisher. No HTTP/key loading here.

Candidate input can enter only through the trusted live runner's full validation.
There is deliberately no publish_success(result_json) or saved-result import API.
"""
from dataclasses import dataclass,asdict
from datetime import datetime,timezone
from typing import Protocol
import copy
import hashlib
import json
import re
from generation_state import StaleGeneration

CHECK_NAME='Protocol / independent agent audit'
class Blocked(Exception):pass
class PendingEvaluation(Exception):pass
def need(ok,message):
    if not ok:raise Blocked(message)
def positive(n):return type(n) is int and n>0
def oid(s):return type(s) is str and re.fullmatch('[0-9a-f]{40}',s) is not None
def digest(s):return type(s) is str and re.fullmatch('[0-9a-f]{64}',s) is not None
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
def sha(x):return hashlib.sha256(canonical(x).encode()).hexdigest()

def failure_location(error):
    """Private controller diagnostics: code locations only, never error values."""
    frames=[]
    cursor=error.__traceback__
    while cursor is not None:
        code=cursor.tb_frame.f_code
        frames.append({'file':code.co_filename.replace('\\','/').rsplit('/',1)[-1],
                       'function':code.co_name,'line':cursor.tb_lineno})
        cursor=cursor.tb_next
    return {'exception_type':type(error).__name__,'frames':frames[-12:]}

@dataclass(frozen=True)
class AppIdentity:
    app_id:int
    installation_id:int
    repository_id:int

@dataclass(frozen=True)
class PullContext:
    repository_id:int
    repository:str
    number:int
    base_ref:str
    base_sha:str
    base_tree:str
    head_sha:str
    head_tree:str
    merge_sha:str
    merge_tree:str
    ready:bool=True

@dataclass(frozen=True)
class CheckRun:
    id:int
    app_id:int
    head_sha:str
    name:str
    status:str
    conclusion:str|None
    external_id:str|None=None

@dataclass(frozen=True)
class RequiredCheck:
    name:str
    app_id:int

@dataclass(frozen=True)
class Config:
    repository:str
    repository_id:int
    app_id:int
    installation_id:int
    base_ref:str
    target_mode:str
    required_merge_ci:tuple=()
    def validate(self):
        need(type(self.repository) is str and re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',self.repository),'invalid repository')
        need(all(positive(x) for x in (self.repository_id,self.app_id,self.installation_id)),'exact App/installation/repository IDs required')
        need(type(self.base_ref) is str and self.base_ref and self.target_mode in ('head','merge'),'explicit base and target mode required')
        need(type(self.required_merge_ci) is tuple,'immutable CI policy required')
        for c in self.required_merge_ci:
            need(type(c) is RequiredCheck and type(c.name) is str and c.name and c.name!=CHECK_NAME and positive(c.app_id),'invalid required CI identity')
        need(len(set(self.required_merge_ci))==len(self.required_merge_ci),'duplicate CI policy')
        if self.target_mode=='merge':need(bool(self.required_merge_ci),'test-merge CI compatibility policy required')

class TrustedAppTransport(Protocol):
    """Implement outside candidate access. All lists must be complete/paginated.

    identity authenticates this actual credential, installation and repository.
    open_contexts includes ALL open PRs on head, even drafts/other bases. Context
    acquisition verifies current base refs, commits/trees and merge parents.
    Mutation methods may use only the authenticated App installation credential.
    """
    def identity(self)->AppIdentity:...
    def open_contexts(self,repository_id,head_sha)->tuple[PullContext,...]:...
    def list_checks(self,repository_id,commit_sha)->tuple[CheckRun,...]:...
    def get_check(self,repository_id,check_id)->CheckRun:...
    def create_check(self,repository_id,payload)->CheckRun:...
    def update_check(self,repository_id,check_id,payload)->CheckRun:...

class GenerationAuthority(Protocol):
    """Protected durable CAS, supplied by the deployment controller.

    begin commits a new generation against its authenticated prior checkpoint.
    assert_current rejects superseded remote generations/controller revisions.
    before_success durably commits the complete pending state and exact identity.
    All methods raise on failure; candidate booleans are not an authorization.
    """
    def begin(self,lease,snapshot):...
    def assert_current(self,lease):...
    def before_success(self,lease,snapshot,identity):...

@dataclass(frozen=True)
class EvaluationInputs:
    packet:dict
    recorder:object
    live_reader:object
    selected_reports:dict
    blob_reader:object

class LiveProtocolRunner:
    """Protected input provider; direct call to the full live evaluator only."""
    def __init__(self,input_provider):self.input_provider=input_provider
    def evaluate(self,context):
        import live_protocol_context as live
        inputs=self.input_provider(context)
        need(type(inputs) is EvaluationInputs,'trusted evaluation inputs required')
        return live.evaluate_session(copy.deepcopy(inputs.packet),inputs.recorder,inputs.live_reader,
                                     copy.deepcopy(inputs.selected_reports),inputs.blob_reader)
    def validate(self,session):
        import live_protocol_context as live
        need(type(session) is live.LiveEvaluation,'fresh live session required, not result JSON')

class Publisher:
    def __init__(self,config,state,transport,live_runner,authority):
        need(type(config) is Config,'trusted publisher configuration required');config.validate()
        need(authority is not None,'explicit durable generation authority required')
        self.config=config;self.state=state;self.transport=transport;self.runner=live_runner;self.authority=authority
    def key(self,head):
        need(oid(head),'exact head SHA required')
        c=self.config;return f'{c.app_id}:{c.installation_id}:{c.repository_id}:{head}'
    def _identity(self):
        c=self.config;i=self.transport.identity()
        need(type(i) is AppIdentity and all(positive(v) for v in (i.app_id,i.installation_id,i.repository_id)),'unverified App identity')
        need(i==AppIdentity(c.app_id,c.installation_id,c.repository_id),'wrong App installation or repository')
    def _checks(self,target):
        checks=self.transport.list_checks(self.config.repository_id,target)
        need(type(checks) is tuple,'complete check tuple required')
        ids=set()
        for c in checks:
            need(type(c) is CheckRun and positive(c.id) and positive(c.app_id) and c.head_sha==target and type(c.name) is str,'malformed check inventory')
            need(c.id not in ids,'duplicate check ID in inventory');ids.add(c.id)
        return checks
    def _own(self,target):return tuple(c for c in self._checks(target) if c.app_id==self.config.app_id and c.name==CHECK_NAME)
    def _contexts(self,head):
        out=self.transport.open_contexts(self.config.repository_id,head)
        need(type(out) is tuple,'complete open PR tuple required')
        seen=set()
        for p in out:
            need(type(p) is PullContext and positive(p.number) and p.number not in seen,'malformed or duplicate PR context');seen.add(p.number)
            need(p.repository_id==self.config.repository_id and type(p.repository_id) is int and p.repository==self.config.repository and p.head_sha==head,'wrong context repository/head')
            need(type(p.ready) is bool and all(oid(x) for x in (p.base_sha,p.base_tree,p.head_sha,p.head_tree,p.merge_sha,p.merge_tree)),'missing current commit/tree identity')
        return tuple(sorted(out,key=lambda p:p.number))
    def _only_context(self,head):
        contexts=self._contexts(head)
        need(len(contexts)==1,'same-head PR context absent or ambiguous')
        p=contexts[0];need(p.ready and p.base_ref==self.config.base_ref,'PR not ready on configured base')
        return p
    def _payload(self,lease,conclusion,summary):
        completed=conclusion is not None
        p={'name':CHECK_NAME,'status':'completed' if completed else 'in_progress',
           'external_id':f'protocol:{lease.generation}:{lease.token}',
           'output':{'title':'Protocol audit '+('accepted' if conclusion=='success' else 'blocked' if completed else 'pending'),'summary':summary}}
        if completed:p.update(conclusion=conclusion,completed_at=datetime.now(timezone.utc).isoformat())
        return p
    def _matches(self,c,target,check_id=None):
        need(type(c) is CheckRun and positive(c.id) and type(c.app_id) is int and c.app_id==self.config.app_id and c.name==CHECK_NAME and c.head_sha==target,'check ownership changed')
        if check_id is not None:need(c.id==check_id,'check ID changed')
    def _write(self,lease,target,check_id,conclusion,summary,fresh=None,publication_identity=None):
        payload=self._payload(lease,conclusion,summary)
        self.state.intent(lease)
        def operation():
            need(self.authority.assert_current(lease) is None,'authority must raise on rejection')
            self._identity()
            if check_id is None:need(not self._own(target),'check appeared before create')
            else:self._matches(self.transport.get_check(self.config.repository_id,check_id),target,check_id)
            if conclusion=='success':
                need(publication_identity is not None,'missing durable publication identity')
                need(self.authority.before_success(lease,self.state.snapshot(),publication_identity) is None,'durable barrier returned an untrusted flag')
                need(self.authority.assert_current(lease) is None,'authority must raise on rejection')
            if fresh is not None:fresh()
            need(self.authority.assert_current(lease) is None,'authority must raise on rejection')
            # No candidate execution or untrusted callback occurs here.
            if check_id is None:
                got=self.transport.create_check(self.config.repository_id,dict(payload,head_sha=target))
            else:got=self.transport.update_check(self.config.repository_id,check_id,payload)
            self._matches(got,target,check_id)
            need(got.status==payload['status'] and got.conclusion==conclusion and got.external_id==payload['external_id'],'write response not confirmed')
            return got
        return self.state.perform(lease,operation,'success' if conclusion=='success' else 'blocked' if conclusion else 'pending',{'target':target,'conclusion':conclusion})
    def _invalidate(self,lease,targets,summary,allow_pending=False):
        ids=[]
        for target in sorted(targets):
            self._identity();own=self._own(target)
            for c in own:
                # GitHub may retain an old conclusion when status is reopened.
                # A completed check stays failed until full fresh acceptance.
                can_pending=allow_pending and len(own)==1 and c.status!='completed' and c.conclusion is None
                got=self._write(lease,target,c.id,None if can_pending else 'failure',summary)
                ids.append(got.id)
        return ids
    def _validate_session(self,session,p):
        self.runner.validate(session)
        binding=session.binding;result=session.result;observation=session.observation
        need(type(binding) is dict and type(result) is dict and type(observation) is dict,'malformed live session')
        expected={'repository_id':p.repository_id,'pull_request':p.number,'base_commit':p.base_sha,'base_tree':p.base_tree,'head_commit':p.head_sha,'head_tree':p.head_tree}
        for k,v in expected.items():need(type(binding.get(k)) is type(v) and binding.get(k)==v,'live binding differs from current context')
        need(binding.get('record_schema')==2 and type(binding.get('record_schema')) is int and binding.get('git_hash')=='sha1','unsupported live record')
        for k in ('policy_sha256','base_manifest_sha256','head_manifest_sha256'):need(digest(binding.get(k)),'missing full manifest or policy binding')
        need(result.get('records_consistent') is True and result.get('live_context_verified') is True,'full live evaluation did not succeed')
        for k in ('packet_sha256','observation_sha256'):need(digest(result.get(k)),'missing evaluated digest')
        need(result['observation_sha256']==sha(observation),'observation digest mismatch')
        for k in ('intake_checkpoint','operator_checkpoint'):need(type(result.get(k)) is dict and result[k],'missing protected checkpoint')
        need(canonical(observation.get('binding'))==canonical(binding),'observation binding mismatch')
        st=observation.get('state',{});pr=st.get('pr',{})
        need(st.get('repository_id')==p.repository_id and type(st.get('repository_id')) is int and pr.get('number')==p.number and type(pr.get('number')) is int,'live PR identity mismatch')
        need(pr.get('state')=='open' and pr.get('draft') is False and pr.get('merged') is False and pr.get('base',{}).get('ref')==p.base_ref,'live readiness/base mismatch')
        for side,commit,tree in (('base',p.base_sha,p.base_tree),('head',p.head_sha,p.head_tree),('merge',p.merge_sha,p.merge_tree)):
            need(st.get('commits',{}).get(side)=={'commit':commit,'tree':tree},'live commit/tree mismatch')
        return sha({'binding':binding,'packet_sha256':result['packet_sha256'],'observation_sha256':result['observation_sha256'],
                    'intake_checkpoint':result['intake_checkpoint'],'operator_checkpoint':result['operator_checkpoint']})
    def _fresh(self,session,p,target,check_id,fingerprint):
        need(self._only_context(p.head_sha)==p,'current base/head/PR context changed')
        own=self._own(target);need(len(own)==1 and own[0].id==check_id,'duplicate or changed own check run')
        if self.config.target_mode=='merge':
            checks=self._checks(target)
            for required in self.config.required_merge_ci:
                matches=[c for c in checks if c.name==required.name and c.app_id==required.app_id]
                need(bool(matches),'required CI absent on test-merge SHA')
                newest=max(matches,key=lambda c:c.id)
                need(newest.status=='completed' and newest.conclusion=='success','required test-merge CI not successful')
        # This final read rechecks full GitHub observation and both protected logs.
        refreshed=session.recheck()
        need(type(refreshed) is dict,'fresh checkpoint identities required')
        result=session.result
        need(set(refreshed)=={'observation_sha256','intake_checkpoint','operator_checkpoint'} and
             all(canonical(refreshed[k])==canonical(result[k]) for k in refreshed),'fresh intake or ledger identity changed')
        need(self._validate_session(session,p)==fingerprint,'live session identity changed')
    def run(self,head_sha,expected_generation):
        """All results are freshly evaluated internally; supplied result JSON is unsupported."""
        key=self.key(head_sha)
        try:lease=self.state.begin(key,expected_generation)
        except StaleGeneration:return {'status':'superseded','published_success':False}
        targets={head_sha,*self.state.known_targets(key)};check=None
        try:
            need(self.authority.begin(lease,self.state.snapshot()) is None,'durable generation CAS returned an untrusted flag')
            self._identity()
            # Revoke legacy/head successes as well when migrating to test-merge.
            self._invalidate(lease,targets,'A new generation requires fresh independent audit.')
            need(all(len(self._own(t))<=1 for t in targets),'duplicate own named check runs require operator reconciliation')
            p=self._only_context(head_sha);target=p.head_sha if self.config.target_mode=='head' else p.merge_sha
            targets.add(target)
            self.state.remember_target(lease,target)
            if target!=head_sha:self._invalidate(lease,{target},'A new generation requires fresh independent audit.')
            own=self._own(target)
            need(len(own)<=1,'duplicate own named check runs require operator reconciliation')
            check=self._write(lease,target,own[0].id if own else None,'failure' if own else None,'Full live validation is pending.')
            session=self.runner.evaluate(p)
            fingerprint=self._validate_session(session,p)
            self.state.assert_current(lease)
            fresh=lambda:self._fresh(session,p,target,check.id,fingerprint)
            identity={'context':asdict(p),'target_sha':target,'target_mode':self.config.target_mode,'validated_identity_sha256':fingerprint}
            check=self._write(lease,target,check.id,'success',f'Exact live audit identity {fingerprint}; generation {lease.generation}.',fresh,identity)
            # Detect races observable immediately after the remote write and revoke.
            fresh();self.state.assert_current(lease);need(self.authority.assert_current(lease) is None,'authority must raise on rejection')
            return {'status':'success','published_success':True,'generation':lease.generation,'check_id':check.id,'target_sha':target,'context_sha256':fingerprint,'target_mode':self.config.target_mode}
        except StaleGeneration:
            return {'status':'superseded','published_success':False,'generation':lease.generation}
        except Exception as ex:
            pending=isinstance(ex,PendingEvaluation)
            try:
                self.state.assert_current(lease)
                self._invalidate(lease,targets,'Validation is pending.' if pending else 'Fresh protocol validation did not complete.',allow_pending=pending)
                revoked=True
            except StaleGeneration:
                return {'status':'superseded','published_success':False,'generation':lease.generation}
            except Exception:revoked=False
            return {'status':'pending' if pending and revoked else 'blocked' if revoked else 'uncertain',
                    'published_success':False,'generation':lease.generation,'revocation_confirmed':revoked,
                    'diagnostic':failure_location(ex),
                    'reason':str(ex) if type(ex) is Blocked else 'Trusted evaluation or transport did not complete.'}
