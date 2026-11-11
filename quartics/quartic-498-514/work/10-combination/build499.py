from package_paths import reference_repo
"""Apply exact scalar denominator-square cancellation to frozen501."""
from pathlib import Path
import json,hashlib
from build import pol,terms,norm
H=Path(__file__).resolve().parent;P=H.parent/'04-charts/further-scalar-cancel'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=H/'candidate501-ir.json';d=read(src);before=read(H/'candidate504-ir.json');patch=read(P/'candidate502-ir.json');pc=read(P/'certificate502.json')
assert sha(src)=='6a31040f85e30cc6f9d076bf6c92218be110e0829e93333d7e99f93a6b2f0d9a'
assert sha(H/'candidate504-ir.json')==pc['sourceSha256'] and sha(P/'candidate502-ir.json')==pc['candidateSha256']
dr={r['name']:r for r in d['residuals']};br={r['name']:r for r in before['residuals']};pr={r['name']:r for r in patch['residuals']}
for name in pc['changedRows']+pc['deletedRows']:assert pol(dr[name]['terms'])==pol(br[name]['terms'])
for name in pc['changedRows']:dr[name]['terms']=pr[name]['terms']
d['residuals']=[r for r in d['residuals'] if r['name'] not in pc['deletedRows']]
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in pc['removedCoordinates']]
total={}
for r in d['residuals']:
 p=norm(pol(r['terms']))
 for (s,m),a in p.items():
  for (t,n),b in p.items():
   key=(s+t,tuple(sorted(m+n)));total[key]=total.get(key,0)+a*b
total={m:c for m,c in total.items() if c}
assert len(d['coordinates'])==499 and len(d['residuals'])==468 and len(total)==24661
assert max(len(m) for s,m in total)==4
assert {i for s,m in total for i in m}=={c['id'] for c in d['coordinates']}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n', encoding='utf-8', newline='\r\n')
write('candidate499-ir.json',d);write('polynomial499.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':499,'witnesses':498,'residuals':468,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'candidate499-ir.json'),'polynomialSha256':sha(H/'polynomial499.json')}
write('certificate499.json',{'source501Sha256':sha(src),'source502Sha256':sha(P/'candidate502-ir.json'),'removedCoordinates':pc['removedCoordinates'],'deletedRows':pc['deletedRows'],'changedRows':pc['changedRows'],'statistics':stats})
print(json.dumps(stats,indent=2))
