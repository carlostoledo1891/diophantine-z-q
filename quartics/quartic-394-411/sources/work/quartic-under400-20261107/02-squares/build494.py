from pathlib import Path
import json,hashlib,sys,copy,math,functools
from fractions import Fraction as Q
H=Path(__file__).resolve().parent
ROOT=H.parents[2]
OLD=ROOT/'work/quartic-optimization-20261107'
R=ROOT/'work/quartic-version6-release/repository'
S=R/'quartics/quartic-498-514/candidate498-ir.json'
# Earlier helper code is arithmetic only; the independent verifier imports none of it.
sys.path.insert(0,str(OLD/'02-squares'));from search import read,encode,add,mul,degree,vs
old=json.loads((OLD/'10-combination/candidate501-ir.json').read_text())
patch=json.loads((OLD/'02-squares/factored/candidate497-ir.json').read_text())
base=json.loads(S.read_text());bn={c['name']:c['id'] for c in base['coordinates']};on={c['id']:c['name'] for c in old['coordinates']};mp={i:bn[n] for i,n in on.items() if n in bn}
def remap(p):return {(s,tuple(sorted(mp[i] for i in m))):v for (s,m),v in p.items()}
orows={r['id']:r for r in old['residuals']};prows={r['id']:r for r in patch['residuals']};rows={r['name']:copy.deepcopy(r) for r in base['residuals']};changed=[];deleted=[]
for i,r in orows.items():
 if i in prows and read(r['terms'])==read(prows[i]['terms']):continue
 assert r['name'] in rows
 assert read(rows[r['name']]['terms'])==remap(read(r['terms'])),r['name']
 if i not in prows:deleted.append(rows[r['name']]['id']);del rows[r['name']]
 else:
  rows[r['name']]['terms']=encode(remap(read(prows[i]['terms'])));changed.append(rows[r['name']]['id'])
pcs={c['id']:c for c in patch['coordinates']};removed=[mp[i] for i in on if i not in pcs];coords=[]
for c in base['coordinates']:
 if c['id'] in removed:continue
 c=copy.deepcopy(c)
 for i,p in pcs.items():
  if i in mp and c['id']==mp[i] and p['name']!=on[i]:c['name']=p['name']
 coords.append(c)
out=dict(base,coordinates=coords,residuals=list(rows.values()),status='Future candidate: four factored second conics transported to frozen v12 498.')
(H/'candidate494-ir.json').write_text(json.dumps(out,indent=2)+'\n')
pol={}
for r in rows.values():
 p=read(r['terms']);den=functools.reduce(math.lcm,(v.denominator for v in p.values()),1);g=functools.reduce(math.gcd,(abs(v.numerator*(den//v.denominator)) for v in p.values()),0);p={m:v*Q(den,g) for m,v in p.items()};pol=add(pol,mul(p,p))
assert {x for s,m in pol for x in m}=={c['id'] for c in coords}
(H/'polynomial494.json').write_text(json.dumps({'fixedParameter':base['fixedParameter'],'terms':encode(pol)},indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cert={'source':str(S),'sourceSha256':sha(S),'earlier501Sha256':sha(OLD/'10-combination/candidate501-ir.json'),'earlier497Sha256':sha(OLD/'02-squares/factored/candidate497-ir.json'),'candidateSha256':sha(H/'candidate494-ir.json'),'polynomialSha256':sha(H/'polynomial494.json'),'coordinateMap':mp,'removedCoordinates':removed,'changedRows':changed,'deletedRows':deleted,'counts':{'variables':len(coords),'witnesses':len(coords)-1,'residuals':len(rows),'degree':degree(pol),'monomials':len({m for s,m in pol})}}
(H/'certificate494.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps(cert['counts'],indent=2))
