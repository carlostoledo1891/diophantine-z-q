from package_paths import reference_repo
"""Compose the mixed-depth seven-equation toric circuit with frozen504."""
from pathlib import Path
import json,hashlib
from build import pol,terms,norm,remap
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=H/'candidate504-ir.json';patchpath=H.parent/'07-toric/mixed/candidate516.json';depthpath=H.parent/'03-depth/beta12/final/candidate-ir.json'
d=read(src);p=read(patchpath);old=read(depthpath)
assert sha(src)=='7c17debaff9a726562be6b7ef843dbc6ca6a0a9d17556158c54ffe5c49ddb0cd'
assert p['source_sha256']==sha(depthpath)
mp={c['id']:c['sourceId'] for c in p['coordinates']};cn={c['name']:c['id'] for c in old['coordinates']};dr={r['name']:r for r in d['residuals']};br={r['name']:r for r in old['residuals']}
deleted=[];removed=[]
for k in range(3):
 pre=f'detector{k}.'
 for suffix in ['eMinus1','eMinus3','eMinus7','eMinus14','eMinus29','eMinus55','q12','q40']:
  name=pre+suffix+'.definition';assert pol(dr[name]['terms'])==pol(br[name]['terms']);deleted.append(name)
 removed.append(cn[pre+'eMinus55'])
names={c['sourceId']:c['name'] for c in p['coordinates']}
d['coordinates']=[dict(c,name=names.get(c['id'],c['name'])) if c['name'].startswith('detector') and '.eMinus' in c['name'] else c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[r for r in d['residuals'] if r['name'] not in deleted]
for r in p['residuals']:
 if '.toric.' in r['name']:
  new=max(rr['id'] for rr in d['residuals'])+1;d['residuals'].append(dict(r,id=new,terms=terms(remap(pol(r['terms']),mp))))
total={}
for r in d['residuals']:
 pp=norm(pol(r['terms']))
 for (s,m),a in pp.items():
  for (t,n),b in pp.items():
   key=(s+t,tuple(sorted(m+n)));total[key]=total.get(key,0)+a*b
total={m:c for m,c in total.items() if c}
assert len(d['coordinates'])==501 and len(d['residuals'])==470
assert max(len(m) for s,m in total)==4 and len(total)==24724
assert {i for s,m in total for i in m}=={c['id'] for c in d['coordinates']}
assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
assert any(s==0 and v==1 for (s,m),v in total.items())
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n', encoding='utf-8', newline='\r\n')
write('candidate501-ir.json',d);write('polynomial501.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':501,'witnesses':500,'residuals':470,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'candidate501-ir.json'),'polynomialSha256':sha(H/'polynomial501.json')}
write('certificate501.json',{'source504Sha256':sha(src),'toricSourceSha256':sha(patchpath),'depthSourceSha256':sha(depthpath),'removedCoordinates':removed,'deletedRows':deleted,'statistics':stats})
print(json.dumps(stats,indent=2))
