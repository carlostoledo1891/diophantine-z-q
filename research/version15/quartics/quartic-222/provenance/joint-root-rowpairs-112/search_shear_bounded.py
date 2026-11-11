import json,math
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).parent
P=O.parent/'joint-root-sparse-111'
WP=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic223-positive-weights-integration-001/polynomial.json')
weights=[F(w) for w in json.loads(WP.read_bytes())['positiveRowWeights']]
ir=json.loads((P/'candidate223-ir.json').read_bytes())
def read(ts):return {(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def add(d,k,v):
 d[k]=d.get(k,0)+v
 if not d[k]:del d[k]
def square(r):
 d={}
 for (a,m),v in r.items():
  for (b,n),w in r.items():add(d,(a+b,tuple(sorted(m+n))),v*w)
 return d
def normalize(r):
 l=math.lcm(*(v.denominator for v in r.values()));g=math.gcd(*(int(v*l) for v in r.values()))
 return {k:int(v*l/g) for k,v in r.items()},str(F(l,g))
rows=[read(r['terms']) for r in ir['residuals']]
poly=read(json.loads(WP.read_bytes())['terms'])
def score(p):return (len(set(m for a,m in p)),len(p))
pairs=[(i,j) for i in range(len(rows)) for j in range(len(rows)) if i!=j if len(rows[i].keys()&rows[j].keys())>=2]
ops=[];trials=0
for step in range(1):
 best=None
 for i,j in pairs:
  r,s=rows[i],rows[j]
  # Only component pairs sharing at least one monomial.
  common=r.keys()&s.keys()
  if not common:continue
  qs={F(1),F(-1),F(2),F(-2),F(1,2),F(-1,2)}|{-F(r[k],s[k]) for k in common}
  old={k:v*weights[i] for k,v in square(r).items()}
  for k,v in square(s).items():add(old,k,v*weights[j])
  for q in qs:
   trials+=1;nr={k:F(v) for k,v in r.items()};ns={k:F(v) for k,v in s.items()}
   for k,v in s.items():add(nr,k,q*v);pass
   if not nr or not ns:continue
   nr,n1=normalize(nr);ns,n2=normalize(ns);np=poly.copy()
   for k,v in old.items():add(np,k,-v)
   for z,wgt in [(nr,weights[i]),(ns,weights[j])]:
    for k,v in square(z).items():add(np,k,v*wgt)
   sc=score(np)
   if sc<score(poly) and (best is None or sc<best[0]):best=(sc,i,j,q,nr,ns,n1,n2,np)
 if best is None:break
 sc,i,j,q,nr,ns,n1,n2,poly=best;rows[i]=nr;rows[j]=ns
 ops.append({'first':i,'second':j,'q':str(q),'normalizations':[n1,n2],'score':sc});print(ops[-1],flush=True)
result={'initial':score(read(json.loads(WP.read_bytes())['terms'])),'final':score(poly),'trials':trials,'operations':ops,'scope':'Simultaneous all shared-support row r+q*s,s basis changes, primitive normalization, shared-monomial cancellation ratios and1,2,1/2'}
(O/'SEARCH-SHEAR.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

