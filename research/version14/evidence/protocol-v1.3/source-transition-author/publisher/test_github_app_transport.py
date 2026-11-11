"""Offline tests. All credentials are synthetic; no API or real key is used."""
import base64
import copy
from datetime import datetime,timezone
import json
import unittest
from unittest.mock import patch
import github_app_transport as g
from app_publisher import CHECK_NAME

RID=1446122118; ROOT='/repos/'+g.REPOSITORIES[RID]; NOW=1804708800
BASE='1'*40; HEAD='2'*40; MERGE='3'*40

def check(check_id=9,app=g.APP_ID,name=CHECK_NAME):
    return {'id':check_id,'app':{'id':app},'name':name,'head_sha':HEAD,
            'status':'in_progress','conclusion':None,'external_id':'protocol:1:abc'}

def payload():
    return {'name':CHECK_NAME,'status':'in_progress','external_id':'protocol:1:abc',
            'output':{'title':'Pending','summary':'Synthetic test'},'head_sha':HEAD}

class Fake:
    def __init__(self):
        self.calls=[];self.override={};self.pull_rows=[];self.checks=[]
        self.token={'token':'synthetic-installation-token','expires_at':datetime.fromtimestamp(NOW+3600,timezone.utc).isoformat(),
                    'permissions':dict(g.PERMISSIONS),'repositories':[{'id':i,'full_name':n} for i,n in g.REPOSITORIES.items()]}
    def __call__(self,method,path,headers,body):
        data=json.loads(body) if body else None;self.calls.append((method,path,copy.deepcopy(data)))
        if (method,path) in self.override:
            value=self.override[method,path]
            if isinstance(value,Exception):raise value
            return copy.deepcopy(value)
        if path=='/app':return 200,{'id':g.APP_ID,'slug':g.APP_SLUG},{}
        if path=='/app/installations/77':return 200,{'id':77,'app_id':g.APP_ID,'suspended_at':None},{}
        if path=='/app/installations/77/access_tokens':return 201,copy.deepcopy(self.token),{}
        if path==ROOT:return 200,{'id':RID,'full_name':g.REPOSITORIES[RID]},{}
        if path.startswith(ROOT+'/pulls?'):return 200,copy.deepcopy(self.pull_rows),{}
        if '/check-runs?' in path:return 200,{'total_count':len(self.checks),'check_runs':copy.deepcopy(self.checks)},{}
        if path==ROOT+'/check-runs/9' and method=='GET':return 200,check(),{}
        if path in (ROOT+'/check-runs',ROOT+'/check-runs/9') and method in ('POST','PATCH'):
            out=check();out.update(data);return 201 if method=='POST' else 200,out,{}
        raise AssertionError('unconfigured fake route')

class Tests(unittest.TestCase):
    def setUp(self):
        self.fake=Fake();self.t=g.GitHubAppTransport(g.TransportConfig(77,RID),lambda b:b'x'*256,exchange=self.fake,clock=lambda:NOW)
    def rejects(self,fn):
        with self.assertRaises(g.TransportError):fn()
    def test_exact_identity(self):
        i=self.t.identity();self.assertEqual((i.app_id,i.installation_id,i.repository_id),(g.APP_ID,77,RID))
        post=[x for x in self.fake.calls if x[0]=='POST'][0]
        self.assertEqual(post[2],{'repository_ids':sorted(g.REPOSITORIES),'permissions':g.PERMISSIONS})
    def test_config_denies_controller_and_boolean(self):
        for i in (True,1449903511,1):self.rejects(lambda:g.TransportConfig(77,i).validate())
        self.rejects(lambda:g.TransportConfig(True,RID).validate())
    def test_wrong_app(self):
        self.fake.override['GET','/app']=(200,{'id':1,'slug':g.APP_SLUG},{})
        self.rejects(self.t.identity);self.assertFalse(any(x[0]=='POST' for x in self.fake.calls))
    def test_wrong_slug(self):
        self.fake.override['GET','/app']=(200,{'id':g.APP_ID,'slug':'another-app'},{})
        self.rejects(self.t.identity)
    def test_wrong_installation(self):
        self.fake.override['GET','/app/installations/77']=(200,{'id':77,'app_id':True,'suspended_at':None},{})
        self.rejects(self.t.identity)
    def test_suspended(self):
        self.fake.override['GET','/app/installations/77']=(200,{'id':77,'app_id':g.APP_ID,'suspended_at':'now'},{})
        self.rejects(self.t.identity)
    def test_token_extra_permission(self):
        self.fake.token['permissions']['contents']='write';self.rejects(self.t.identity)
    def test_token_extra_repo(self):
        self.fake.token['repositories'].append({'id':1449903511,'full_name':'elliotglazer/research-review-controller'})
        self.rejects(self.t.identity)
    def test_token_missing_repo(self):
        self.fake.token['repositories'].pop();self.rejects(self.t.identity)
    def test_token_expiry_bound(self):
        for seconds in (0,10,7200):
            self.fake.token['expires_at']=datetime.fromtimestamp(NOW+seconds,timezone.utc).isoformat()
            self.rejects(self.t.identity)
    def test_repository_rename_or_transfer(self):
        self.fake.override['GET',ROOT]=(200,{'id':RID,'full_name':'foreign/name'},{})
        self.rejects(self.t.identity)
    def test_token_cached_only_short_period(self):
        self.t.identity();self.t.identity()
        self.assertEqual(sum(x[0]=='POST' for x in self.fake.calls),1)
        self.t._clock=lambda:NOW+241;self.t.identity()
        self.assertEqual(sum(x[0]=='POST' for x in self.fake.calls),2)
    def test_path_escape_before_auth(self):
        for path in ('https://evil.invalid/x','//evil.invalid/x',ROOT+'/../private-diophantine',ROOT+'/%2e%2e/private-diophantine',
                     ROOT+'/%252e%252e/x',ROOT+'/x\\y',ROOT+'/x#fragment','/repos/foreign/name',ROOT+'suffix',ROOT+'/%0aX'):
            self.rejects(lambda:self.t.get(path))
        self.assertEqual(self.fake.calls,[])
    def test_fixed_http_route_allowlist(self):
        for method,path in [('DELETE',ROOT+'/check-runs/9'),('POST',ROOT+'/issues'),('PATCH',ROOT+'/pulls/1')]:
            self.rejects(lambda:self.t._call(method,path,'synthetic',{}))
        self.assertEqual(self.fake.calls,[])
    def test_get_adapter(self):
        self.assertEqual(self.t.get(ROOT)[0]['id'],RID)
    def test_create_and_update_own_check(self):
        c=self.t.create_check(RID,payload());self.assertEqual(c.app_id,g.APP_ID)
        p=payload();p.pop('head_sha');self.assertEqual(self.t.update_check(RID,9,p).id,9)
    def test_wrong_repo_mutation(self):
        self.rejects(lambda:self.t.create_check(1447509909,payload()));self.assertFalse(self.fake.calls)
    def test_foreign_check_app_or_name(self):
        for c in (check(app=1),check(name='another-check')):
            self.fake.override['GET',ROOT+'/check-runs/9']=(200,c,{})
            p=payload();p.pop('head_sha');self.rejects(lambda:self.t.update_check(RID,9,p))
        self.assertFalse(any(x[0]=='PATCH' for x in self.fake.calls))
    def test_payload_denies_extra_authority(self):
        for key,value in [('actions',[{}]),('details_url','https://evil.invalid'),('head_sha','notsha'),('name','another')]:
            p=payload();p[key]=value;self.rejects(lambda:self.t.create_check(RID,p))
        self.assertFalse(self.fake.calls)
    def test_payload_requires_generation_and_completion(self):
        for patcher in ({'external_id':'unbound'},{'status':'completed'},{'conclusion':'success'}):
            p=payload();p.update(patcher);self.rejects(lambda:self.t.create_check(RID,p))
    def test_completion_accepts_only_success_failure(self):
        p=payload();p.update(status='completed',conclusion='success',completed_at=datetime.fromtimestamp(NOW,timezone.utc).isoformat())
        self.assertEqual(self.t.create_check(RID,p).conclusion,'success')
        p['conclusion']='neutral';self.rejects(lambda:self.t.create_check(RID,p))
    def test_mutation_response_wrong_owner(self):
        self.fake.override['POST',ROOT+'/check-runs']=(201,check(app=5),{})
        self.rejects(lambda:self.t.create_check(RID,payload()))
    def test_list_all_checks(self):
        self.fake.checks=[check(),check(10,app=4)]
        self.assertEqual(len(self.t.list_checks(RID,HEAD)),2)
        self.assertTrue(any('filter=all' in path for _,path,_ in self.fake.calls))
    def test_duplicate_or_wrong_head_check(self):
        self.fake.checks=[check(),check()];self.rejects(lambda:self.t.list_checks(RID,HEAD))
        self.fake.checks=[dict(check(),head_sha=BASE)];self.rejects(lambda:self.t.list_checks(RID,HEAD))
    def test_pages_complete(self):
        prefix=ROOT+'/pulls';rows=[{'id':i+1} for i in range(100)]
        self.fake.override['GET',prefix+'?per_page=100&page=1']=(200,rows,{'link':'<https://evil.invalid>; rel="next"'})
        self.fake.override['GET',prefix+'?per_page=100&page=2']=(200,[{'id':101}],{})
        self.assertEqual(len(self.t._pages(prefix)),101)
        self.assertFalse(any('evil.invalid' in path for _,path,_ in self.fake.calls))
    def test_truncated_total(self):
        self.fake.override['GET',ROOT+'/commits/'+HEAD+'/check-runs?filter=all&per_page=100&page=1']=(200,{'total_count':2,'check_runs':[check()]},{})
        self.rejects(lambda:self.t.list_checks(RID,HEAD))
    def test_page_and_request_caps(self):
        self.t._requests=g.MAX_REQUESTS;self.rejects(self.t.identity)
    def install_pr(self,number=1,draft=False,base_ref='main'):
        row={'id':100+number,'number':number,'state':'open','head':{'sha':HEAD}}
        self.fake.pull_rows.append(row)
        pr=dict(row,merged=False,draft=draft,mergeable=True,merge_commit_sha=MERGE,
                base={'ref':base_ref,'sha':BASE,'repo':{'id':RID,'full_name':g.REPOSITORIES[RID]}})
        self.fake.override['GET',ROOT+'/pulls/'+str(number)]=(200,pr,{})
        for ref,sha in [('heads/'+base_ref,BASE),(f'pull/{number}/head',HEAD),(f'pull/{number}/merge',MERGE)]:
            self.fake.override['GET',ROOT+'/git/ref/'+ref]=(200,{'ref':'refs/'+ref,'object':{'type':'commit','sha':sha}},{})
        for sha in (BASE,HEAD,MERGE):
            self.fake.override['GET',ROOT+'/git/commits/'+sha]=(200,{'sha':sha,'tree':{'sha':'4'*40},'parents':[{'sha':s} for s in ([BASE,HEAD] if sha==MERGE else [])]}, {})
    def test_context_includes_drafts_and_other_bases(self):
        self.install_pr();self.install_pr(2,True,'other')
        contexts=self.t.open_contexts(RID,HEAD)
        self.assertEqual(len(contexts),2);self.assertTrue(contexts[0].ready);self.assertFalse(contexts[1].ready)
    def test_merge_parent_mismatch(self):
        self.install_pr();self.fake.override['GET',ROOT+'/git/commits/'+MERGE][1]['parents'].reverse()
        self.rejects(lambda:self.t.open_contexts(RID,HEAD))
    def test_ref_mismatch(self):
        self.install_pr();self.fake.override['GET',ROOT+'/git/ref/heads/main'][1]['object']['sha']='9'*40
        self.rejects(lambda:self.t.open_contexts(RID,HEAD))
    def test_error_redacts_response_and_exception(self):
        secret='synthetic-token-must-not-escape'
        self.fake.override['GET','/app']=RuntimeError(secret)
        try:self.t.identity()
        except g.TransportError as e:self.assertNotIn(secret,str(e));self.assertTrue(e.__suppress_context__)
        else:self.fail('accepted')
    def test_strict_json(self):
        for raw in (b'{"x":1,"x":2}',b'{"x":NaN}',b'not json'):self.rejects(lambda:g.strict_json(raw))
    def test_real_rs256_with_synthetic_key(self):
        from cryptography.hazmat.primitives.asymmetric import rsa,padding
        from cryptography.hazmat.primitives import serialization,hashes
        key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
        pem=key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
        signer=g.RS256Signer.from_pem(pem)
        t=g.GitHubAppTransport(g.TransportConfig(77,RID),signer,exchange=self.fake,clock=lambda:NOW)
        a,b,c=t._jwt().split('.')
        dec=lambda s:base64.urlsafe_b64decode(s+'='*(-len(s)%4))
        self.assertEqual(json.loads(dec(a)),{'alg':'RS256','typ':'JWT'})
        self.assertEqual(json.loads(dec(b)),{'iat':NOW-60,'exp':NOW+480,'iss':str(g.APP_ID)})
        key.public_key().verify(dec(c),(a+'.'+b).encode(),padding.PKCS1v15(),hashes.SHA256())
        self.rejects(lambda:g.RS256Signer.from_pem(b'synthetic-invalid-key'))
    def test_https_redirect_and_size_rejected(self):
        class Response:
            status=302
            def getheader(self,key,default=None):return {'Content-Type':'application/json','Content-Length':str(g.MAX_RESPONSE+1)}.get(key,default)
            def read(self,n):raise AssertionError('must not read')
        class Connection:
            def __init__(self,*a,**kw):self.response=Response();self.args=a
            def request(self,*a,**kw):pass
            def getresponse(self):return self.response
            def close(self):pass
        with patch.object(g.http.client,'HTTPSConnection',Connection):
            self.rejects(lambda:g.https_exchange('GET','/app',{},None))
            Response.status=200
            self.rejects(lambda:g.https_exchange('GET','/app',{},None))

if __name__=='__main__':unittest.main()
