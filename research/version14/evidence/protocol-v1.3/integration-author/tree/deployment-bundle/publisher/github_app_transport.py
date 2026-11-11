"""Trusted-controller-only GitHub App transport. Never executes candidate code.

No environment/file key lookup, redirects, proxy discovery, or secret logging.
The injected signer and exchange are trusted test/controller dependencies.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import wraps
import base64
import http.client
import json
import re
import ssl
import time
from urllib.parse import quote, urlencode, urlsplit, unquote
from app_publisher import AppIdentity, PullContext, CheckRun, CHECK_NAME

APP_ID = 5663093
APP_SLUG = 'elliot-research-review-gate'
REPOSITORIES = {1446122118: 'elliotglazer/diophantine-z-q',
                1447509909: 'elliotglazer/private-diophantine'}
PERMISSIONS = {'checks': 'write', 'contents': 'read', 'pull_requests': 'read',
               'actions': 'read', 'metadata': 'read'}
HOST = 'api.github.com'
MAX_RESPONSE = 16 * 1024 * 1024
MAX_REQUESTS = 5000
MAX_PAGES = 100

class TransportError(Exception):
    """Fixed, non-secret diagnostic. No response body is retained."""

def need(ok, message):
    if not ok: raise TransportError(message)

def positive(n): return type(n) is int and n > 0
def oid(s): return type(s) is str and re.fullmatch('[0-9a-f]{40}', s) is not None
def text(s, limit=1000): return type(s) is str and 0 < len(s) <= limit

def safe(method):
    @wraps(method)
    def call(*args, **kwargs):
        try: return method(*args, **kwargs)
        except TransportError: raise
        except Exception: raise TransportError('invalid API response or transport failure') from None
    return call

def strict_json(raw):
    def pairs(items):
        d = {}
        for k,v in items:
            need(k not in d, 'duplicate JSON key'); d[k] = v
        return d
    try:
        return json.loads(raw, object_pairs_hook=pairs,
                          parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
    except TransportError: raise
    except Exception: raise TransportError('invalid JSON response') from None

def b64(data): return base64.urlsafe_b64encode(data).rstrip(b'=')

class RS256Signer:
    def __init__(self, key): self._key = key

    @classmethod
    @safe
    def from_pem(cls, pem):
        """Only the isolated controller supplies these bytes; no path is accepted."""
        need(type(pem) is bytes and 0 < len(pem) <= 32768, 'invalid private key input')
        from cryptography.hazmat.primitives.serialization import load_pem_private_key
        from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
        key = load_pem_private_key(pem, password=None)
        need(isinstance(key, RSAPrivateKey) and 2048 <= key.key_size <= 8192, 'RSA private key required')
        return cls(key)

    @safe
    def __call__(self, payload):
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        return self._key.sign(payload, padding.PKCS1v15(), hashes.SHA256())

@dataclass(frozen=True)
class TransportConfig:
    installation_id: int
    repository_id: int

    def validate(self):
        need(positive(self.installation_id), 'exact installation ID required')
        need(positive(self.repository_id) and self.repository_id in REPOSITORIES,
             'repository is not approved')

@safe
def https_exchange(method, path, headers, body):
    """Direct TLS connection. http.client does not consult proxy variables."""
    connection = http.client.HTTPSConnection(HOST, timeout=30, context=ssl.create_default_context())
    try:
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        need(response.status in (200,201), 'GitHub request rejected')
        need(response.getheader('Content-Encoding','identity') == 'identity', 'encoded response rejected')
        need(response.getheader('Content-Type','').split(';')[0].strip() == 'application/json', 'JSON response required')
        length = response.getheader('Content-Length')
        need(length is None or (length.isdigit() and int(length) <= MAX_RESPONSE), 'response size limit')
        raw = response.read(MAX_RESPONSE + 1)
        need(len(raw) <= MAX_RESPONSE, 'response size limit')
        return response.status, strict_json(raw), {'link':response.getheader('Link','')}
    finally: connection.close()

class GitHubAppTransport:
    def __init__(self, config, signer, *, exchange=https_exchange, clock=time.time):
        need(type(config) is TransportConfig, 'trusted transport configuration required')
        config.validate()
        self.config=config; self._signer=signer; self._exchange=exchange; self._clock=clock
        self._token=None; self._expires=0; self._requests=0
        self.root='/repos/'+REPOSITORIES[config.repository_id]

    def _jwt(self):
        now=int(self._clock())
        header=b64(b'{"alg":"RS256","typ":"JWT"}')
        claims=b64(json.dumps({'iat':now-60,'exp':now+480,'iss':str(APP_ID)},separators=(',',':')).encode())
        message=header+b'.'+claims
        signature=self._signer(message)
        need(type(signature) is bytes and 256 <= len(signature) <= 1024, 'invalid RSA signature')
        return (message+b'.'+b64(signature)).decode('ascii')

    def _call(self, method, path, credential, payload=None):
        self._requests+=1
        need(self._requests<=MAX_REQUESTS, 'request budget exceeded')
        need(type(path) is str and path.startswith('/') and not path.startswith('//') and
             not any(ord(c)<33 or ord(c)>126 for c in path), 'invalid API path')
        app_root=f'/app/installations/{self.config.installation_id}'
        if method=='GET':
            if path not in ('/app',app_root):self._read_path(path)
            need(payload is None,'GET body rejected')
        elif method=='POST':
            need(path in (app_root+'/access_tokens',self.root+'/check-runs'),'unapproved POST route')
            if path==app_root+'/access_tokens':
                need(payload=={'repository_ids':sorted(REPOSITORIES),'permissions':PERMISSIONS},'unapproved token scope')
            else:self._payload(payload,True)
        elif method=='PATCH':
            need(re.fullmatch(re.escape(self.root)+r'/check-runs/[1-9][0-9]*',path) is not None,'unapproved PATCH route')
            self._payload(payload,False)
        else:raise TransportError('unapproved HTTP method')
        need(type(credential) is str and 0<len(credential)<=16384 and
             all(32<ord(c)<127 for c in credential), 'invalid credential')
        body=None if payload is None else json.dumps(payload,separators=(',',':'),allow_nan=False).encode()
        need(body is None or len(body)<=65536, 'request size limit')
        headers={'Authorization':'Bearer '+credential,'Accept':'application/vnd.github+json',
                 'X-GitHub-Api-Version':'2022-11-28','User-Agent':'elliot-independent-gate/1'}
        if body is not None: headers['Content-Type']='application/json'
        status,value,response_headers=self._exchange(method,path,headers,body)
        need(type(status) is int and status==(201 if method=='POST' else 200), 'GitHub request rejected')
        need(type(response_headers) is dict and type(response_headers.get('link','')) is str, 'invalid response headers')
        return value,response_headers

    def _app(self):
        jwt=self._jwt()
        app,_=self._call('GET','/app',jwt)
        need(type(app) is dict and type(app.get('id')) is int and app['id']==APP_ID and app.get('slug')==APP_SLUG,
             'unexpected authenticated App')
        install,_=self._call('GET',f'/app/installations/{self.config.installation_id}',jwt)
        need(type(install) is dict and type(install.get('id')) is int and install['id']==self.config.installation_id
             and type(install.get('app_id')) is int and install['app_id']==APP_ID
             and install.get('suspended_at') is None, 'unexpected or suspended installation')
        return jwt

    def _access(self):
        now=self._clock()
        if self._token is not None and now+60<self._expires:return self._token
        self._token=None; self._expires=0
        jwt=self._app()
        value,_=self._call('POST',f'/app/installations/{self.config.installation_id}/access_tokens',jwt,
                            {'repository_ids':sorted(REPOSITORIES),'permissions':dict(PERMISSIONS)})
        need(type(value) is dict and value.get('permissions')==PERMISSIONS, 'unexpected token permissions')
        repos=value.get('repositories')
        need(type(repos) is list and len(repos)==2 and
             all(type(r) is dict and positive(r.get('id')) for r in repos) and
             {r['id']:r.get('full_name') for r in repos}==REPOSITORIES, 'unexpected token repository scope')
        expiry=datetime.fromisoformat(value['expires_at'].replace('Z','+00:00'))
        need(expiry.tzinfo is not None, 'token expiry timezone required')
        expires=expiry.timestamp()
        need(now+60<expires<=now+3660, 'unexpected token expiry')
        token=value.get('token')
        need(text(token,16384) and all(32<ord(c)<127 for c in token), 'invalid installation token')
        self._token=token; self._expires=min(expires,now+300)
        return token

    def _repo(self, repository_id):
        need(type(repository_id) is int and repository_id==self.config.repository_id, 'repository scope mismatch')

    def _read_path(self,path):
        need(type(path) is str and len(path)<=8192, 'invalid API path')
        parts=urlsplit(path)
        need(not parts.scheme and not parts.netloc and not parts.fragment, 'external API URL rejected')
        decoded=parts.path
        for _ in range(5):
            newer=unquote(decoded)
            if newer==decoded:break
            decoded=newer
        need('%' not in decoded and not any(c in decoded for c in ('\\','?','#')) and
             not any(ord(c)<33 or ord(c)>126 for c in decoded) and
             not any(s in ('.','..','') for s in decoded.split('/')[1:]), 'unsafe API path')
        need(decoded==self.root or decoded.startswith(self.root+'/'), 'read outside selected repository')

    @safe
    def get(self,path):
        """ReadContext adapter. The bearer token never leaves this object."""
        self._read_path(path)
        return self._call('GET',path,self._access())

    def _one(self,path):
        value,headers=self.get(path)
        need(type(value) is dict and not headers.get('link'), 'single API object required')
        return value

    def _pages(self,path,key=None,query=None):
        out=[];ids=set();expected=None
        for page in range(1,MAX_PAGES+1):
            value,headers=self.get(path+'?'+urlencode(dict(query or {},per_page=100,page=page)))
            if key is None: rows=value
            else:
                need(type(value) is dict and type(value.get('total_count')) is int and value['total_count']>=0,'missing page total')
                need(expected is None or expected==value['total_count'],'page total changed')
                expected=value['total_count'];rows=value.get(key)
            need(type(rows) is list and len(rows)<=100, 'invalid API page')
            for row in rows:
                need(type(row) is dict and positive(row.get('id')) and row['id'] not in ids,'duplicate or invalid API ID')
                ids.add(row['id']);out.append(row)
            # Construct pages ourselves; never follow a response URL.
            if len(rows)<100:
                need('rel="next"' not in headers.get('link',''), 'inconsistent pagination')
                need(expected is None or len(out)==expected, 'incomplete page inventory')
                return out
        raise TransportError('pagination limit exceeded')

    @safe
    def identity(self):
        self._app()
        repo=self._one(self.root)
        need(type(repo.get('id')) is int and repo['id']==self.config.repository_id and
             repo.get('full_name')==REPOSITORIES[self.config.repository_id], 'repository identity changed')
        return AppIdentity(APP_ID,self.config.installation_id,self.config.repository_id)

    def _check(self,value):
        need(type(value) is dict and positive(value.get('id')) and oid(value.get('head_sha')) and
             type(value.get('app')) is dict and positive(value['app'].get('id')) and text(value.get('name')),
             'invalid check response')
        need(value.get('status') in ('queued','in_progress','completed','waiting','pending','requested'), 'invalid check status')
        need(value.get('conclusion') is None or text(value['conclusion'],100), 'invalid check conclusion')
        need(value.get('external_id') is None or text(value['external_id'],1024), 'invalid check external ID')
        return CheckRun(value['id'],value['app']['id'],value['head_sha'],value['name'],value['status'],value.get('conclusion'),value.get('external_id'))

    @safe
    def list_checks(self,repository_id,commit_sha):
        self._repo(repository_id);need(oid(commit_sha),'exact commit SHA required')
        checks=tuple(self._check(v) for v in self._pages(self.root+'/commits/'+commit_sha+'/check-runs','check_runs',{'filter':'all'}))
        need(all(c.head_sha==commit_sha for c in checks),'check commit mismatch')
        return checks

    @safe
    def get_check(self,repository_id,check_id):
        self._repo(repository_id);need(positive(check_id),'exact check ID required')
        c=self._check(self._one(self.root+'/check-runs/'+str(check_id)))
        need(c.id==check_id,'check ID mismatch');return c

    def _payload(self,payload,create):
        need(type(payload) is dict, 'check payload required')
        required={'name','status','external_id','output'}|({'head_sha'} if create else set())
        need(required<=set(payload)<=required|{'conclusion','completed_at'}, 'unapproved check payload field')
        need(payload['name']==CHECK_NAME and payload['status'] in ('in_progress','completed'),'unapproved check identity/status')
        need(text(payload['external_id'],1024) and re.fullmatch(r'protocol:[1-9][0-9]*:[A-Za-z0-9_-]+',payload['external_id']), 'invalid generation identity')
        output=payload['output'];need(type(output) is dict and set(output)=={'title','summary'} and
             text(output['title'],255) and text(output['summary'],60000),'invalid check output')
        if create:need(oid(payload['head_sha']),'exact check commit required')
        if payload['status']=='completed':
            need(payload.get('conclusion') in ('success','failure') and text(payload.get('completed_at'),64),'invalid completed check')
            dt=datetime.fromisoformat(payload['completed_at'].replace('Z','+00:00'));need(dt.tzinfo is not None,'completion timezone required')
        else:need('conclusion' not in payload and 'completed_at' not in payload,'pending check has conclusion')

    @safe
    def create_check(self,repository_id,payload):
        self._repo(repository_id);self._payload(payload,True)
        self.identity()
        result,_=self._call('POST',self.root+'/check-runs',self._access(),payload)
        c=self._check(result)
        need(c.app_id==APP_ID and c.name==CHECK_NAME and c.head_sha==payload['head_sha'],'created check ownership mismatch')
        return c

    @safe
    def update_check(self,repository_id,check_id,payload):
        self._repo(repository_id);self._payload(payload,False)
        self.identity();old=self.get_check(repository_id,check_id)
        need(old.app_id==APP_ID and old.name==CHECK_NAME,'refusing foreign check mutation')
        result,_=self._call('PATCH',self.root+'/check-runs/'+str(check_id),self._access(),payload)
        c=self._check(result)
        need(c.id==check_id and c.app_id==APP_ID and c.name==CHECK_NAME and c.head_sha==old.head_sha,'updated check ownership mismatch')
        return c

    def _pull_inventory(self):
        rows=self._pages(self.root+'/pulls',query={'state':'open','sort':'created','direction':'asc'})
        result={}
        for p in rows:
            need(positive(p.get('number')) and p['number'] not in result and p.get('state')=='open' and
                 type(p.get('head')) is dict and oid(p['head'].get('sha')), 'invalid open PR inventory')
            result[p['number']]=p['head']['sha']
        return result

    @safe
    def open_contexts(self,repository_id,head_sha):
        self._repo(repository_id);need(oid(head_sha),'exact head SHA required')
        inventory=self._pull_inventory();out=[]
        for number,head in sorted(inventory.items()):
            if head!=head_sha:continue
            p=self._one(self.root+'/pulls/'+str(number));base=p.get('base',{});h=p.get('head',{})
            need(p.get('number')==number and type(p.get('number')) is int and p.get('state')=='open' and p.get('merged') is False
                 and type(p.get('draft')) is bool and h.get('sha')==head_sha,'PR changed during read')
            need(type(base.get('repo')) is dict and type(base['repo'].get('id')) is int and
                 base['repo']['id']==repository_id and base['repo'].get('full_name')==REPOSITORIES[repository_id], 'PR base repository mismatch')
            ref=base.get('ref');bs=base.get('sha');ms=p.get('merge_commit_sha')
            need(text(ref,255) and oid(bs) and oid(ms),'PR merge context unavailable')
            def check_ref(name,sha):
                obj=self._one(self.root+'/git/ref/'+quote(name,safe='/'))
                need(obj.get('ref')=='refs/'+name and obj.get('object',{}).get('type')=='commit' and obj['object'].get('sha')==sha,'current ref mismatch')
            check_ref('heads/'+ref,bs);check_ref('pull/'+str(number)+'/head',head_sha);check_ref('pull/'+str(number)+'/merge',ms)
            trees=[]
            for sha in (bs,head_sha,ms):
                obj=self._one(self.root+'/git/commits/'+sha)
                need(obj.get('sha')==sha and oid(obj.get('tree',{}).get('sha')), 'commit identity mismatch')
                if sha==ms:need([v.get('sha') for v in obj.get('parents',[])]==[bs,head_sha], 'merge parents mismatch')
                trees.append(obj['tree']['sha'])
            out.append(PullContext(repository_id,REPOSITORIES[repository_id],number,ref,bs,trees[0],head_sha,trees[1],ms,trees[2],not p['draft'] and p.get('mergeable') is True))
        need(inventory==self._pull_inventory(),'open PR inventory changed')
        return tuple(out)
