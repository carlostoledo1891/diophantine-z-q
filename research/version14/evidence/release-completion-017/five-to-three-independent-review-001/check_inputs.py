from pathlib import Path
import hashlib,json
R=Path.cwd();B=R/'work/source-risk-review-20261107';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def ck(ok,s):
 if not ok:raise AssertionError(s)
 checks.append(s)
def pin(p,h,n=None):
 ck(sha(p)==h,'hash '+str(p.relative_to(R)))
 if n is not None:ck(p.stat().st_size==n,'size '+str(p.relative_to(R)))
def manifest(name,h):
 d=B/name;pin(d/'MANIFEST.json',h)
 for x in load(d/'MANIFEST.json')['files']:pin(R/x['path'] if x['path'].startswith('work/') else d/x['path'],x['sha256'],x.get('bytes'))
 return d
def loc(x):
 p=x.get('pin',x);f=R/p['path'];pin(f,p['sha256']);a=x['start_line'];b=x['end_line'];ll=f.read_bytes().splitlines(keepends=True)
 ck(1<=a<=b<=len(ll),'range '+str(a));ck(hashlib.sha256(b''.join(ll[a-1:b])).hexdigest()==x['excerpt_sha256'],'excerpt '+p['path']+':'+str(a)+'-'+str(b))
d1=manifest('five-to-three-author-sol-001','4acb2711635186ff2c702bac4f1e13221bc6593f4ad1e384a7a339cc761da481')
d2=manifest('five-to-three-author-sol-002','a3f48e27c8df1e1999bc07abc06b1cfa3a2d32636cb37346b356535fd69f83b9')
da=manifest('h5-scalar-normalizer-author-arithmetic-001','6e65bc53231605b1019796cbfc38c9dc30a22dbd5076c406eafcef24b38c919a')
x=load(d2/'DELTA.json');old=(d1/'PROOF.md').read_bytes();new=(d2/'PROOF.md').read_bytes();o=x['old_text'].encode();n=x['new_text'].encode()
ck(old.count(o)==1,'unique old paragraph');ck(old.replace(o,n,1)==new,'only literal embedding paragraph changed');ck(x['predecessor_manifest']==sha(d1/'MANIFEST.json'),'delta old manifest');ck(x['predecessor_proof']==sha(d1/'PROOF.md'),'delta old proof')
for f in ['INPUTS.json','CONSUMPTION.json','FRONTIER.json']:ck((d1/f).read_bytes()==(d2/f).read_bytes(),'unchanged '+f)
for x in load(d2/'INPUTS.json').values():
 if isinstance(x,dict) and 'path' in x and 'sha256' in x:pin(R/x['path'],x['sha256'])
for x in load(d2/'CONSUMPTION.json').values():
 if isinstance(x,dict) and 'start_line' in x:loc(x)
s=load(da/'SOURCES.json')
for x in s['pins']:pin(R/x['path'],x['sha256'],x.get('bytes'))
for x in s['locations'].values():loc(x)
for name,h in [('milne-page-21.png','a65a593e404cc7b979f471932fe0919fe6f14a0fd202be9fd4930346c9be043e'),('milne-page-23.png','e847c5abd1bf8effe2f0a67b2494eaa70970e75cc28cedb83a4993b94d61fe2c')]:pin(d1/'local-only'/name,h)
ck(sha(d2/'PROOF.md') in json.dumps(load(d2/'PAYLOAD-MAP.json')),'payload hash')
p=B/'five-to-three-independent-review-001'/'CHECKS.json';p.write_text(json.dumps({'passed':True,'count':len(checks),'checks':checks},indent=2)+'\n',encoding='utf-8',newline='\n');print(len(checks),sha(p))

