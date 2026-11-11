"""Bounded modular search for constant-pivot quadratic eliminants in new H block."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json
H=Path(__file__).resolve().parent;d=json.loads((H/'candidate390-ir.json').read_text());P=1000003
rows=[r for r in d['residuals'] if r.get('block')=='squared_H_Kummer']
variables=sorted({i for r in rows for t in r['terms'] for i in t['monomial']})
def scalar(s):a=Fraction(s);return a.numerator*pow(a.denominator,-1,P)%P
raw=[{tuple(t['monomial']):scalar(t['coefficient']) for t in r['terms']} for r in rows]
lifted=[]
for r in raw:
 for factor in [()]+[(i,) for i in variables]:lifted.append({tuple(sorted(m+factor)):c for m,c in r.items()})
results=[]
for target in variables:
 def forbidden(m):return (target in m and m!=(target,)) or len(m)>2
 basis={};candidates=[]
 for ri,row in enumerate(lifted):
  q=row.copy()
  while True:
   bad=[m for m in q if forbidden(m)]
   if not bad:break
   pivot=max(bad)
   if pivot not in basis:
    inv=pow(q[pivot],-1,P);basis[pivot]={m:c*inv%P for m,c in q.items()};q={};break
   c=q[pivot]
   for m,e in basis[pivot].items():
    q[m]=(q.get(m,0)-c*e)%P
    if not q[m]:del q[m]
  if q.get((target,),0):candidates.append({'generator':ri,'support':len(q),'quadratics':sum(len(m)==2 for m in q)})
 results.append({'target':target,'constantPivotRelations':candidates,'forbiddenRank':len(basis)})
out={'prime':P,'scope':'8 local H rows times all monomials of degree at most1; no global impossibility claim','variables':variables,'inputRows':len(lifted),'results':results}
(H/'LOCAL-SCAN.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
