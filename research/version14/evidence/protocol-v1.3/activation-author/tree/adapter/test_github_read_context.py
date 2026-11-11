"""Synthetic transport only. No real credentials, capture or GitHub writes."""
import base64
import copy
import hashlib
import json
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit, parse_qs
import github_read_context as g
import test_manifest_gate as fixtures

ROOT = '/repos/fixture/repo'

class Transport:
    def __init__(self, routes):
        self.routes = routes; self.calls = []; self.hook = None
    def get(self, path):
        self.calls.append(path)
        if self.hook:
            self.hook(path)
        if path not in self.routes:
            raise AssertionError('unexpected request: '+path)
        value = self.routes[path]
        return copy.deepcopy(value)

def fixture():
    p, _, _ = fixtures.fixture()
    files = {'policy.md':b'approved policy', '.github/workflows/ci.yml':b'approved workflow',
             'scripts/check.py':b'approved checker', 'paper.md':b'base'}
    p['base'], _ = fixtures.manifest(files,'base')
    headfiles = dict(files, **{'paper.md':b'head'})
    p['head'], _ = fixtures.manifest(headfiles,'head')
    p['repository_id'] = 1; p['pull_request'] = 7
    shas = {path:hashlib.sha256(raw).hexdigest() for path,raw in files.items()}
    p['policy_sha256'] = shas['policy.md']
    policy = g.TrustedPolicy('fixture/repo',1,'main','policy.md',shas['policy.md'],('policy.md','.github/','scripts/'),
        (g.WorkflowPolicy(10,'.github/workflows/ci.yml',('check',),
             {path:shas[path] for path in ('.github/workflows/ci.yml','scripts/check.py')}),))
    base = p['base']['commit']; head = p['head']['commit']; merge = '3'*40
    routes = {}
    def obj(path,value):routes[ROOT+path] = (value,{})
    obj('',{'id':1,'full_name':'fixture/repo'})
    pr = {'number':7,'state':'open','draft':False,'merged':False,'merge_commit_sha':merge,
          'base':{'repo':{'id':1},'sha':base,'ref':'main'},
          'head':{'repo':{'id':1},'sha':head,'ref':'feature'},'updated_at':'2026-11-07T00:00:00Z'}
    obj('/pulls/7',pr)
    obj('/git/ref/heads/main',{'object':{'type':'commit','sha':base}})
    for sha, tree, parents in ((base,p['base']['tree'],[]),(head,p['head']['tree'],[]),(merge,p['head']['tree'],[base,head])):
        obj('/git/commits/'+sha,{'sha':sha,'tree':{'sha':tree},'parents':[{'sha':s} for s in parents]})
    def tree_for(values):
        children = {}
        for path, raw in values.items():
            node = children
            parts = path.split('/')
            for part in parts[:-1]:node=node.setdefault(part,{})
            node[parts[-1]]=raw
        def visit(node):
            rows=[]; body=b''
            for name in sorted(node,key=lambda k:k+('/' if type(node[k]) is dict else '')):
                value=node[name]
                if type(value) is dict:
                    sha=visit(value); kind='tree'; mode='040000'
                else:
                    sha=g.core.git_object('blob',value,'sha1');kind='blob';mode='100644'
                    obj('/git/blobs/'+sha,{'sha':sha,'size':len(value),'encoding':'base64','content':base64.b64encode(value).decode()})
                rows.append({'path':name,'type':kind,'mode':mode,'sha':sha})
                body += (mode.lstrip('0')+' '+name).encode()+b'\0'+bytes.fromhex(sha)
            sha=g.core.git_object('tree',body,'sha1')
            obj('/git/trees/'+sha,{'sha':sha,'truncated':False,'tree':rows})
            return sha
        return visit(children)
    assert tree_for(files)==p['base']['tree']
    assert tree_for(headfiles)==p['head']['tree']
    for suffix in ('/issues/7/comments','/pulls/7/reviews','/pulls/7/comments'):
        obj(suffix+'?per_page=100&page=1',[{'id':100,'body':'Original audit text','user':{'id':9}}])
    obj('/actions/workflows/10',{'id':10,'path':'.github/workflows/ci.yml','state':'active'})
    run = {'id':20,'workflow_id':10,'path':'.github/workflows/ci.yml','head_sha':head,
           'repository':{'id':1},'head_repository':{'id':1},'event':'pull_request',
           'pull_requests':[copy.deepcopy(pr)],'status':'completed','conclusion':'success','run_attempt':2,
           'referenced_workflows':[]}
    obj('/actions/workflows/10/runs?head_sha='+head+'&per_page=100&page=1',{'total_count':1,'workflow_runs':[run]})
    obj('/actions/runs/20',run)
    job = {'id':30,'run_id':20,'run_attempt':2,'head_sha':head,'name':'check','status':'completed',
           'conclusion':'success','steps':[{'number':1,'status':'completed','conclusion':'success'}]}
    obj('/actions/runs/20/attempts/2/jobs?per_page=100&page=1',{'total_count':1,'jobs':[job]})
    transport=Transport(routes)
    return p,policy,transport

class ContextTests(unittest.TestCase):
    def setUp(self):self.p,self.policy,self.transport=fixture();self.reader=g.ReadContext(self.policy,self.transport)
    def object(self,suffix):return self.transport.routes[ROOT+suffix][0]
    def runobj(self):return self.object('/actions/runs/20')
    def jobobj(self):return self.object('/actions/runs/20/attempts/2/jobs?per_page=100&page=1')['jobs'][0]
    def observe(self):return self.reader.observe(self.p)
    def rejects(self,pattern):
        with self.assertRaisesRegex(g.core.Invalid,pattern):self.observe()
    def test_good_capture_is_not_authority(self):
        value=self.observe();self.assertFalse(value['merge_authorized']);self.assertFalse(value['deployment_eligible']);self.assertFalse(value['durable_intake_registered'])
        self.assertEqual(value['intake']['issue_comments'][0]['body'],'Original audit text')
        self.assertTrue(all(p.startswith(ROOT) for p in self.transport.calls))
    def test_no_registered_findings_adapter(self):
        with self.assertRaisesRegex(g.core.IntegrationMissing,'registered findings'):
            self.reader.verify_context(self.p,{}, {})
    def test_float_schema_rejected(self):self.p['schema']=2.0;self.rejects('requires schema2')
    def test_wrong_repository(self):self.object('')['id']=2;self.rejects('origin mismatch')
    def test_bool_repository(self):self.object('')['id']=True;self.rejects('origin mismatch')
    def test_wrong_manifest_commit(self):self.p['head']=copy.deepcopy(self.p['base']);self.rejects('candidate origin mismatch')
    def test_fork_rejected(self):self.object('/pulls/7')['head']['repo']['id']=8;self.rejects('foreign repository')
    def test_closed_pr(self):self.object('/pulls/7')['state']='closed';self.rejects('not open')
    def test_draft_pr(self):self.object('/pulls/7')['draft']=True;self.rejects('not open')
    def test_stale_base_ref(self):self.object('/git/ref/heads/main')['object']['sha']='4'*40;self.rejects('base ref moved')
    def test_stale_merge(self):self.object('/git/commits/'+'3'*40)['parents'][0]['sha']='4'*40;self.rejects('merge commit')
    def test_unregistered_policy(self):self.p['policy_sha256']='f'*64;self.rejects('unregistered policy')
    def test_source_bytes_tampered(self):
        key=next(k for k in self.transport.routes if '/git/blobs/' in k)
        self.transport.routes[key][0]['content']=base64.b64encode(b'fake').decode();self.rejects('source blob')
    def test_truncated_source_tree(self):
        self.object('/git/trees/'+self.p['base']['tree'])['truncated']=True;self.rejects('incomplete Git tree')
    def test_wrong_workflow_path(self):self.runobj()['path']='.github/workflows/fake.yml';self.rejects('run provenance')
    def test_wrong_event(self):self.runobj()['event']='pull_request_target';self.rejects('unsupported CI event')
    def test_stale_run_base(self):self.runobj()['pull_requests'][0]['base']['sha']='4'*40;self.rejects('CI not bound')
    def test_wrong_pr_run(self):self.runobj()['pull_requests'][0]['number']=8;self.rejects('CI not bound')
    def test_float_pr_run(self):self.runobj()['pull_requests'][0]['number']=7.0;self.rejects('CI not bound')
    def test_bool_run_repository(self):self.runobj()['repository']['id']=True;self.rejects('run repository mismatch')
    def test_float_job_attempt(self):self.jobobj()['run_attempt']=2.0;self.rejects('job provenance')
    def test_missing_run_association(self):self.runobj()['pull_requests']=[];self.rejects('CI not bound')
    def test_neutral_run(self):self.runobj()['conclusion']='neutral';self.rejects('run not successful')
    def test_pending_run(self):self.runobj()['status']='in_progress';self.rejects('run not successful')
    def test_unapproved_reusable_workflow(self):self.runobj()['referenced_workflows']=[{'path':'x','sha':'1'*40}];self.rejects('reusable workflow')
    def test_old_job_attempt(self):self.jobobj()['run_attempt']=1;self.rejects('job provenance')
    def test_wrong_job_head(self):self.jobobj()['head_sha']='4'*40;self.rejects('job provenance')
    def test_skipped_job(self):self.jobobj()['conclusion']='skipped';self.rejects('job not successful')
    def test_skipped_step(self):self.jobobj()['steps'][0]['conclusion']='skipped';self.rejects('step not actually')
    def test_missing_steps(self):self.jobobj()['steps']=[];self.rejects('step not actually')
    def test_unknown_job(self):self.jobobj()['name']='fake';self.rejects('unregistered CI job')
    def test_duplicate_job_name(self):
        value=self.object('/actions/runs/20/attempts/2/jobs?per_page=100&page=1');value['jobs'].append(dict(self.jobobj(),id=31));value['total_count']=2;self.rejects('duplicate or unregistered')
    def test_newer_failed_run_cannot_use_old_success(self):
        path='/actions/workflows/10/runs?head_sha='+self.p['head']['commit']+'&per_page=100&page=1'
        value=self.object(path);new=dict(self.runobj(),id=21,conclusion='failure');value['workflow_runs'].append(new);value['total_count']=2
        self.transport.routes[ROOT+'/actions/runs/21']=(new,{})
        self.rejects('run not successful')
    def test_search_cap(self):
        self.object('/actions/workflows/10/runs?head_sha='+self.p['head']['commit']+'&per_page=100&page=1')['total_count']=1000;self.rejects('search cap')
    def test_comment_changes_detected(self):
        path=ROOT+'/issues/7/comments?per_page=100&page=1';count=0
        def hook(p):
            nonlocal count
            if p==path:
                count+=1
                if count==2:self.transport.routes[path][0][0]['body']='edited'
        self.transport.hook=hook;self.rejects('audit intake changed')
    def test_pr_changes_detected(self):
        count=0
        def hook(p):
            nonlocal count
            if p==ROOT+'/pulls/7':
                count+=1
                if count==2:self.object('/pulls/7')['updated_at']='later'
        self.transport.hook=hook;self.rejects('PR or base changed')
    def test_ci_changes_detected(self):
        count=0
        def hook(p):
            nonlocal count
            if p==ROOT+'/actions/runs/20':
                count+=1
                if count==2:self.runobj()['updated_at']='later'
        self.transport.hook=hook;self.rejects('CI changed')

class PaginationTests(unittest.TestCase):
    def api(self,first,second=None):
        routes={'/repos/a/b/items?per_page=100&page=1':first}
        if second:routes['/repos/a/b/items?per_page=100&page=2']=second
        return g.API(Transport(routes))
    def link(self,url):return {'link':'<'+url+'>; rel="next"'}
    def test_two_pages(self):
        api=self.api(([{'id':1}],self.link('https://api.github.com/repos/a/b/items?per_page=100&page=2')),([{'id':2}],{}))
        self.assertEqual(len(api.pages('/repos/a/b/items')),2)
    def test_cross_origin(self):
        api=self.api(([{'id':1}],self.link('https://evil.invalid/repos/a/b/items?per_page=100&page=2')))
        with self.assertRaisesRegex(g.core.Invalid,'origin'):api.pages('/repos/a/b/items')
    def test_changed_query(self):
        api=self.api(([{'id':1}],self.link('https://api.github.com/repos/a/b/items?per_page=100&page=2&token=secret')))
        with self.assertRaisesRegex(g.core.Invalid,'query'):api.pages('/repos/a/b/items')
    def test_skipped_page(self):
        api=self.api(([{'id':1}],self.link('https://api.github.com/repos/a/b/items?per_page=100&page=3')))
        with self.assertRaisesRegex(g.core.Invalid,'nonsequential'):api.pages('/repos/a/b/items')
    def test_duplicate_records(self):
        api=self.api(([{'id':1},{'id':1}],{}))
        with self.assertRaisesRegex(g.core.Invalid,'duplicate'):api.pages('/repos/a/b/items')
    def test_missing_total_rows(self):
        api=self.api(({'total_count':2,'items':[{'id':1}]},{}))
        with self.assertRaisesRegex(g.core.Invalid,'incomplete'):api.pages('/repos/a/b/items','items')
    def test_total_changes(self):
        api=self.api(({'total_count':2,'items':[{'id':1}]},self.link('https://api.github.com/repos/a/b/items?per_page=100&page=2')),({'total_count':3,'items':[{'id':2}]},{}))
        with self.assertRaisesRegex(g.core.Invalid,'total changed'):api.pages('/repos/a/b/items','items')
    def test_page_budget(self):
        api=self.api(([{'id':1}],self.link('https://api.github.com/repos/a/b/items?per_page=100&page=2')))
        with patch.object(g,'MAX_PAGES',1),self.assertRaisesRegex(g.core.Invalid,'page budget'):api.pages('/repos/a/b/items')
    def test_last_without_next(self):
        api=self.api(([{'id':1}],{'link':'<https://api.github.com/repos/a/b/items?per_page=100&page=2>; rel="last"'}))
        with self.assertRaisesRegex(g.core.Invalid,'continuation'):api.pages('/repos/a/b/items')
    def test_earlier_last_page_cannot_be_forgotten(self):
        links={'link':'<https://api.github.com/repos/a/b/items?per_page=100&page=2>; rel="next", <https://api.github.com/repos/a/b/items?per_page=100&page=3>; rel="last"'}
        api=self.api(([{'id':1}],links),([{'id':2}],{}))
        with self.assertRaisesRegex(g.core.Invalid,'before known last'):api.pages('/repos/a/b/items')
    def test_next_beyond_last_rejected(self):
        links={'link':'<https://api.github.com/repos/a/b/items?per_page=100&page=2>; rel="next", <https://api.github.com/repos/a/b/items?per_page=100&page=1>; rel="last"'}
        api=self.api(([{'id':1}],links))
        with self.assertRaisesRegex(g.core.Invalid,'exceeds known last'):api.pages('/repos/a/b/items')
    def test_last_changes_between_pages(self):
        first={'link':'<https://api.github.com/repos/a/b/items?per_page=100&page=2>; rel="next", <https://api.github.com/repos/a/b/items?per_page=100&page=2>; rel="last"'}
        second={'link':'<https://api.github.com/repos/a/b/items?per_page=100&page=3>; rel="next", <https://api.github.com/repos/a/b/items?per_page=100&page=3>; rel="last"'}
        api=self.api(([{'id':1}],first),([{'id':2}],second))
        with self.assertRaisesRegex(g.core.Invalid,'last page changed'):api.pages('/repos/a/b/items')

class TransportTests(unittest.TestCase):
    def test_json_duplicate_keys(self):
        with self.assertRaises(g.core.Invalid):g.strict_json(b'{"x":1,"x":2}')
    def test_json_nan(self):
        with self.assertRaises(g.core.Invalid):g.strict_json(b'{"x":NaN}')
    def test_credential_newline(self):
        with self.assertRaises(g.core.Invalid):g.GitHubHTTPS('token\r\nheader: x')
    def test_fixed_host_get_and_no_redirect(self):
        class Response:
            status=302
        class Connection:
            def __init__(self,host,timeout):self.host=host;self.timeout=timeout;instances.append(self)
            def request(self,method,path,headers):self.method=method;self.path=path;self.headers=headers
            def getresponse(self):return Response()
            def close(self):self.closed=True
        instances=[]
        with patch.object(g.http.client,'HTTPSConnection',Connection),self.assertRaisesRegex(g.core.Invalid,'200'):
            g.GitHubHTTPS('fixture-only-token').get('/repos/a/b')
        self.assertEqual(instances[0].host,'api.github.com');self.assertEqual(instances[0].method,'GET');self.assertTrue(instances[0].closed)

if __name__=='__main__':unittest.main()
