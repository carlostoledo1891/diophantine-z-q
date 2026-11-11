"""Replace the two-level scalar root by a single reversed norm node."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parent/'candidate450-ir.json'
def parse(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(p.items()) if v]
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def times(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   key=tuple(sorted(m+n));d[key]=d.get(key,0)+v*w
 return {m:v for m,v in d.items() if v}
def prim(p):
 d=reduce(lcm,(x.denominator for x in p.values()),1);g=reduce(gcd,(abs(int(x*d)) for x in p.values()),0)
 return {m:x*F(d,g) for m,x in p.items()}
data=json.loads(S.read_text());rows={r['name']:r for r in data['residuals']}
p=parse(rows['reduced_scalar.constant_node']['terms'])
r={tuple(i for i in m if i!=536):v for m,v in p.items() if 536 in m}
q2={(311,311):F(1),(312,312):F(-8)}
assert p==add(add(times(r,{(536,):F(1)}),r,-1),q2,-1)
assert {x['name'] for x in data['residuals'] if any(536 in t['monomial'] for t in x['terms'])}=={'reduced_scalar.constant_node','reduced_scalar.root'}
newroot=add(add(times(r,{(542,):F(1)}),q2,-1),times(r,{(541,):F(1)}),-1)
data['residuals']=[x for x in data['residuals'] if x['name']!='reduced_scalar.constant_node']
for row in data['residuals']:
 if row['name']=='reduced_scalar.root':row['terms']=enc(newroot)
data['coordinates']=[c for c in data['coordinates'] if c['id']!=536]
data['status']='Research root449: positive contact parameter and single reversed scalar norm node; independent review required.'
total={}
for row in data['residuals']:
 p=prim(parse(row['terms']));total=add(total,times(p,p))
def write(n,d):(H/n).write_text(json.dumps(d,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
write('candidate449-ir.json',data);write('polynomial449.json',{'fixedParameter':data['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate449-ir.json'),'polynomialSha256':sha(H/'polynomial449.json'),'variables':len(data['coordinates']),'residuals':len(data['residuals']),'monomials':len(total),'rTerms':enc(r),'rootTerms':enc(newroot),'removedCoordinate':536})
print((H/'CERTIFICATE.json').read_text())
