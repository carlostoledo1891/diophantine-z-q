"""All App operations are fake and in-memory. No token, network or remote writes."""
from dataclasses import replace,asdict
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import copy
import json
import unittest
import app_publisher as p
from generation_state import SQLiteGenerationState,LocalSQLiteAuthority,StaleGeneration

def oid(n):return f'{n:040x}'
def context(**kw):
    return replace(p.PullContext(11,'owner/math',7,'main',oid(1),oid(2),oid(3),oid(4),oid(5),oid(6)),**kw)
def observation(c):
    binding={'record_schema':2,'repository_id':c.repository_id,'pull_request':c.number,'git_hash':'sha1','policy_sha256':'1'*64,
             'base_commit':c.base_sha,'base_tree':c.base_tree,'head_commit':c.head_sha,'head_tree':c.head_tree,
             'base_manifest_sha256':'2'*64,'head_manifest_sha256':'3'*64}
    return {'binding':binding,'state':{'repository_id':c.repository_id,'pr':{'number':c.number,'state':'open','draft':False,'merged':False,'base':{'ref':c.base_ref},'title':'Exact π audit'},
            'commits':{s:{'commit':getattr(c,s+'_sha'),'tree':getattr(c,s+'_tree')} for s in ('base','head','merge')}},'intake':[],'ci':['strict fake CI']}

class FakeSession:
    def __init__(self,owner,c):
        self.owner=owner;self.obs=observation(c);self.calls=0;self.failed=False
        self.res={'records_consistent':True,'live_context_verified':True,'packet_sha256':'4'*64,'observation_sha256':p.sha(self.obs),
                  'intake_checkpoint':{'sequence':1,'sha256':'5'*64},'operator_checkpoint':{'sequence':2,'sha256':'6'*64}}
    @property
    def binding(self):return copy.deepcopy(self.obs['binding'])
    @property
    def result(self):return copy.deepcopy(self.res)
    @property
    def observation(self):return copy.deepcopy(self.obs)
    def recheck(self):
        if self.failed:raise ValueError('latched stale session')
        self.calls+=1
        try:
            if self.owner.on_recheck:self.owner.on_recheck(self)
        except Exception:self.failed=True;raise
        return {k:copy.deepcopy(self.res[k]) for k in ('observation_sha256','intake_checkpoint','operator_checkpoint')}

class FakeRunner:
    def __init__(self):self.error=None;self.after=None;self.on_recheck=None;self.sessions=[];self.return_dict=False
    def evaluate(self,c):
        if self.error:raise self.error
        s=FakeSession(self,c);self.sessions.append(s)
        if self.after:self.after(s)
        return s.result if self.return_dict else s
    def validate(self,s):
        p.need(type(s) is FakeSession and s.owner is self,'fake trusted session provenance missing')

class FakeTransport:
    def __init__(self,c):
        self.auth=p.AppIdentity(42,43,11);self.contexts=(c,);self.checks={};self.writes=[];self.next_id=100
        self.on_write=None;self.fail=False
    def identity(self):
        if self.fail:raise OSError('offline')
        return self.auth
    def open_contexts(self,repo,head):
        if self.fail:raise OSError('offline')
        assert repo==11;return tuple(c for c in self.contexts if c.head_sha==head)
    def list_checks(self,repo,head):
        if self.fail:raise OSError('offline')
        assert repo==11;return tuple(c for c in self.checks.values() if c.head_sha==head)
    def get_check(self,repo,cid):
        if self.fail:raise OSError('offline')
        assert repo==11;return self.checks[cid]
    def add(self,head,app=42,name=p.CHECK_NAME,status='completed',conclusion='success'):
        self.next_id+=1;self.checks[self.next_id]=p.CheckRun(self.next_id,app,head,name,status,conclusion)
        return self.next_id
    def create_check(self,repo,payload):
        assert repo==11;self.next_id+=1
        return self._write(self.next_id,payload['head_sha'],payload)
    def update_check(self,repo,cid,payload):
        assert repo==11;return self._write(cid,self.checks[cid].head_sha,payload)
    def _write(self,cid,head,payload):
        if self.fail:raise OSError('offline')
        assert payload['name']==p.CHECK_NAME
        self.writes.append((cid,copy.deepcopy(payload)))
        value=p.CheckRun(cid,self.auth.app_id,head,payload['name'],payload['status'],payload.get('conclusion'),payload['external_id'])
        self.checks[cid]=value
        if self.on_write:self.on_write(value)
        return value

class FakeAuthority(LocalSQLiteAuthority):
    def __init__(self,state):super().__init__(state);self.barriers=[];self.error=None;self.boolean=False
    def before_success(self,lease,snapshot,identity):
        super().before_success(lease,snapshot,identity)
        if self.error:raise self.error
        if self.boolean:return False
        self.barriers.append((asdict(lease),copy.deepcopy(snapshot),copy.deepcopy(identity)))

class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.addCleanup(self.temp.cleanup);root=Path(self.temp.name).resolve()
        self.candidate=root/'candidate';self.candidate.mkdir();self.c=context()
        self.state=SQLiteGenerationState(root/'state.sqlite',(self.candidate,));self.state.initialize()
        self.transport=FakeTransport(self.c);self.runner=FakeRunner();self.authority=FakeAuthority(self.state)
        self.config=p.Config('owner/math',11,42,43,'main','head')
        self.publisher=p.Publisher(self.config,self.state,self.transport,self.runner,self.authority)
    def run_pub(self,g=0):return self.publisher.run(self.c.head_sha,g)
    def own(self,target=None):return [x for x in self.transport.checks.values() if x.app_id==42 and x.name==p.CHECK_NAME and (target is None or x.head_sha==target)]
    def no_green(self):self.assertFalse(any(x.conclusion=='success' for x in self.own()))
    def test_success_exact_name_identity_and_barrier(self):
        r=self.run_pub();self.assertTrue(r['published_success']);self.assertEqual(len(self.authority.barriers),1)
        self.assertGreaterEqual(self.runner.sessions[0].calls,2);self.assertEqual(self.own()[0].name,p.CHECK_NAME)
        identity=self.authority.barriers[0][2];self.assertEqual(identity['context'],asdict(self.c))
        self.assertEqual(identity['validated_identity_sha256'],r['context_sha256'])
    def test_candidate_result_booleans_rejected(self):
        self.runner.return_dict=True;r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_failure_invalidates_own_previous_success(self):
        self.assertTrue(self.run_pub()['published_success']);self.runner.error=ValueError('rejected records')
        r=self.run_pub(1);self.assertFalse(r['published_success']);self.no_green();self.assertEqual(len(self.own()),1)
    def test_private_diagnostics_exclude_exception_values_and_absolute_paths(self):
        secret='secret-test-sentinel-DO-NOT-LOG'
        self.runner.error=ValueError(secret)
        r=self.run_pub();self.assertFalse(r['published_success']);self.no_green()
        self.assertEqual(r['diagnostic']['exception_type'],'ValueError')
        self.assertTrue(any(f['function']=='evaluate' for f in r['diagnostic']['frames']))
        self.assertNotIn(secret,json.dumps(r));self.assertNotIn(secret,json.dumps(self.transport.writes))
        self.assertLessEqual(len(r['diagnostic']['frames']),12)
        for frame in r['diagnostic']['frames']:
            self.assertNotIn('/',frame['file']);self.assertNotIn('\\',frame['file'])
            self.assertEqual(set(frame),{'file','function','line'})
    def test_pending_invalidates_previous_success(self):
        self.run_pub();self.runner.error=p.PendingEvaluation('CI not ready');r=self.run_pub(1)
        self.assertEqual(r['status'],'pending');self.no_green();self.assertEqual(self.own()[0].status,'completed')
        self.assertEqual(self.own()[0].conclusion,'failure')
    def test_completed_checks_are_not_reopened_during_successful_revalidation(self):
        self.assertTrue(self.run_pub()['published_success'])
        original=self.transport.update_check
        def sticky(repo,cid,payload):
            old=self.transport.checks[cid]
            if old.conclusion is not None and payload['status']=='in_progress':
                raise AssertionError('do not rely on clearing a completed GitHub conclusion')
            return original(repo,cid,payload)
        self.transport.update_check=sticky
        self.assertTrue(self.run_pub(1)['published_success'])
        self.assertEqual(len(self.own()),1)
    def test_wrong_app_does_not_mutate(self):
        self.transport.auth=p.AppIdentity(99,43,11);r=self.run_pub();self.assertFalse(r['published_success']);self.assertEqual(self.transport.writes,[])
    def test_bool_app_identity_rejected(self):
        self.transport.auth=p.AppIdentity(True,43,11);self.run_pub();self.assertEqual(self.transport.writes,[])
    def test_foreign_same_name_check_not_changed(self):
        cid=self.transport.add(self.c.head_sha,app=99);original=self.transport.checks[cid]
        self.assertTrue(self.run_pub()['published_success']);self.assertEqual(original,self.transport.checks[cid])
    def test_duplicate_own_runs_all_invalidated_and_block(self):
        self.transport.add(self.c.head_sha);self.transport.add(self.c.head_sha)
        r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green();self.assertFalse(self.runner.sessions)
    def test_same_head_different_pr_blocks(self):
        self.transport.add(self.c.head_sha);self.transport.contexts+=(replace(self.c,number=8,base_ref='other',base_sha=oid(12)),)
        r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_closed_pr_revokes(self):
        self.run_pub();self.transport.contexts=();r=self.run_pub(1);self.assertEqual(r['status'],'blocked');self.no_green()
    def test_draft_pr_blocks(self):
        self.transport.contexts=(replace(self.c,ready=False),);r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_base_changes_during_evaluation(self):
        self.runner.after=lambda s:setattr(self.transport,'contexts',(replace(self.c,base_sha=oid(12),merge_sha=oid(15)),))
        r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_base_changes_after_success_write_revoked(self):
        def hook(c):
            if c.conclusion=='success':self.transport.contexts=(replace(self.c,base_sha=oid(12),merge_sha=oid(15)),)
        self.transport.on_write=hook;r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_new_same_head_pr_after_write_revoked(self):
        def hook(c):
            if c.conclusion=='success':self.transport.contexts+=(replace(self.c,number=8),)
        self.transport.on_write=hook;r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_intake_or_ledger_recheck_failure(self):
        def changed(s):raise ValueError('checkpoint changed')
        self.runner.on_recheck=changed;r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_recheck_boolean_rejected(self):
        self.runner.after=lambda s:setattr(s,'recheck',lambda:True)
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_session_binding_tree_tamper(self):
        self.runner.after=lambda s:s.obs['binding'].update(head_tree=oid(900))
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_missing_checkpoint_rejected(self):
        self.runner.after=lambda s:s.res.pop('intake_checkpoint')
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_old_job_completion_cannot_publish(self):
        def newer(s):self.state.begin(self.publisher.key(self.c.head_sha),1)
        self.runner.after=newer;r=self.run_pub();self.assertEqual(r['status'],'superseded');self.no_green()
        self.assertFalse(any(pay.get('conclusion')=='success' for _,pay in self.transport.writes))
    def test_start_generation_cas(self):
        self.run_pub();n=len(self.transport.writes);self.assertEqual(self.run_pub(0)['status'],'superseded');self.assertEqual(len(self.transport.writes),n)
    def test_durable_barrier_failure_blocks(self):
        self.authority.error=ValueError('remote CAS failed');r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_durable_barrier_boolean_not_accepted(self):
        self.authority.boolean=True;r=self.run_pub();self.assertEqual(r['status'],'blocked');self.no_green()
    def test_transport_ambiguous_write_is_honestly_uncertain(self):
        def hook(c):
            if c.conclusion=='success':self.transport.fail=True;raise OSError('response lost')
        self.transport.on_write=hook;r=self.run_pub();self.assertEqual(r['status'],'uncertain');self.assertFalse(r['revocation_confirmed'])
        self.assertFalse(r['published_success']);self.assertEqual(self.state.read(self.publisher.key(self.c.head_sha))['phase'],'uncertain')
    def setup_merge(self):
        self.config=replace(self.config,target_mode='merge',required_merge_ci=(p.RequiredCheck('CI / test',1),))
        self.publisher=p.Publisher(self.config,self.state,self.transport,self.runner,self.authority)
        self.transport.add(self.c.merge_sha,app=1,name='CI / test')
    def test_merge_target_exact_and_legacy_head_revoked(self):
        self.setup_merge();old=self.transport.add(self.c.head_sha)
        r=self.run_pub();self.assertTrue(r['published_success']);self.assertEqual(r['target_sha'],self.c.merge_sha)
        self.assertEqual(self.transport.checks[old].conclusion,'failure')
    def test_merge_ci_on_head_only_blocks(self):
        self.setup_merge();self.transport.checks.clear();self.transport.add(self.c.head_sha,app=1,name='CI / test')
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_newer_failed_merge_ci_not_hidden_by_old_success(self):
        self.setup_merge();self.transport.add(self.c.merge_sha,app=1,name='CI / test',conclusion='failure')
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_merge_ci_wrong_app_blocks(self):
        self.setup_merge();self.transport.checks.clear();self.transport.add(self.c.merge_sha,app=2,name='CI / test')
        self.assertEqual(self.run_pub()['status'],'blocked');self.no_green()
    def test_old_merge_success_revoked_after_base_change(self):
        self.setup_merge();self.assertTrue(self.run_pub()['published_success'])
        self.transport.contexts=(replace(self.c,base_sha=oid(20),merge_sha=oid(21)),)
        self.runner.error=ValueError('new base not accepted');self.run_pub(1);self.no_green()
    def test_restored_state_retains_old_merge_revocation_targets(self):
        self.setup_merge();self.run_pub();snap=self.state.snapshot();root=Path(self.temp.name)
        restored=SQLiteGenerationState(root/'restored.sqlite',(self.candidate,));restored.initialize();restored.restore_trusted(snap)
        auth=FakeAuthority(restored);pub=p.Publisher(self.config,restored,self.transport,self.runner,auth)
        self.transport.contexts=();r=pub.run(self.c.head_sha,1);self.assertEqual(r['status'],'blocked');self.no_green()
    def test_restore_cannot_overwrite_existing_generation(self):
        self.run_pub()
        with self.assertRaises(ValueError):self.state.restore_trusted(self.state.snapshot())
    def test_state_cannot_live_in_candidate_root(self):
        with self.assertRaises(ValueError):SQLiteGenerationState(self.candidate/'state.sqlite',(self.candidate,))
    def test_second_state_instance_observes_cas(self):
        other=SQLiteGenerationState(self.state.path,(self.candidate,));key=self.publisher.key(self.c.head_sha)
        lease=self.state.begin(key,0);other.begin(key,1)
        with self.assertRaises(StaleGeneration):self.state.intent(lease)
    def test_candidate_not_executed_and_no_http(self):
        file=self.candidate/'candidate.py';file.write_text("raise RuntimeError('candidate must never execute')\n")
        before=file.read_bytes()
        with patch('subprocess.run',side_effect=AssertionError('candidate execution')),patch('http.client.HTTPSConnection',side_effect=AssertionError('network forbidden')):
            self.assertTrue(self.run_pub()['published_success'])
        self.assertEqual(file.read_bytes(),before)
    def test_generation_authority_required(self):
        with self.assertRaises(p.Blocked):p.Publisher(self.config,self.state,self.transport,self.runner,None)

if __name__=='__main__':unittest.main(verbosity=2)
