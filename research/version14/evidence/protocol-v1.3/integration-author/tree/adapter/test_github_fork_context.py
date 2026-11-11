"""Fork profile regressions, including inherited strict reader behavior."""
import copy,unittest
import test_github_read_context as original
import github_fork_context as fork
g=original.g

def forkify(packet,transport,repository_id=42):
    pr=transport.routes[original.ROOT+'/pulls/7'][0]
    pr['head']['repo']={'id':repository_id,'full_name':'contributor/repo'}
    run=transport.routes[original.ROOT+'/actions/runs/20'][0]
    run['head_repository']={'id':repository_id}
    run['pull_requests'][0]['head']['repo']=copy.deepcopy(pr['head']['repo'])
    for label,sha in (('head',packet['head']['commit']),('merge','3'*40)):
        transport.routes[original.ROOT+'/git/ref/pull/7/'+label]=({'ref':'refs/pull/7/'+label,'object':{'type':'commit','sha':sha}},{})

class ForkTests(original.ContextTests):
    def setUp(self):
        self.p,self.policy,self.transport=original.fixture();forkify(self.p,self.transport)
        self.reader=fork.ForkReadContext(self.policy,self.transport)
    def test_fork_rejected(self):
        # Replace inherited same-repository-only assertion with missing identity.
        self.object('/pulls/7')['head']['repo']=None;self.rejects('fork repository identity')
    def test_authenticated_fork_supported(self):
        result=self.observe();self.assertEqual(result['state']['head_repository']['id'],42)
        self.assertTrue(all(p.startswith(original.ROOT) for p in self.transport.calls))
    def test_head_pull_ref_must_match(self):
        self.object('/git/ref/pull/7/head')['object']['sha']='4'*40;self.rejects('pull ref mismatch')
    def test_merge_pull_ref_must_match(self):
        self.object('/git/ref/pull/7/merge')['object']['sha']='4'*40;self.rejects('pull ref mismatch')
    def test_mismatched_ref_name_rejected(self):
        self.object('/git/ref/pull/7/head')['ref']='refs/pull/8/head';self.rejects('pull ref mismatch')
    def test_base_identity_cannot_move(self):
        self.object('/pulls/7')['base']['repo']['id']=42;self.rejects('base repository mismatch')
    def test_run_must_bind_fork_identity(self):
        self.runobj()['head_repository']['id']=1;self.rejects('run repository mismatch')
    def test_run_association_must_bind_fork_identity(self):
        self.runobj()['pull_requests'][0]['head']['repo']['id']=1;self.rejects('CI not bound')
    def test_fork_id_bool_rejected(self):
        self.object('/pulls/7')['head']['repo']['id']=True;self.rejects('fork repository identity')
    def test_fork_id_float_rejected(self):
        self.object('/pulls/7')['head']['repo']['id']=42.0;self.rejects('fork repository identity')
    def test_same_repository_supported_with_pull_refs(self):
        forkify(self.p,self.transport,1);self.observe()

if __name__=='__main__':unittest.main()
