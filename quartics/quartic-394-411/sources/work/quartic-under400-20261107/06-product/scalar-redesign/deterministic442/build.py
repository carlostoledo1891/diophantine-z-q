from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parent/'one-correction444/candidate444-ir.json'
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(p.items()) if v]
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   k=tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {m:v for m,v in d.items() if v}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 return {m:v*F(d,g) for m,v in q.items()}
d=json.loads(S.read_text());rows={r['name']:r for r in d['residuals']}
root=p(rows['reduced_scalar.root']['terms'])
r={tuple(i for i in m if i!=541):-v for m,v in root.items() if 541 in m}
assert len(r)==6
newb=add(mul(add({(600,):F(1)},r,4896),{(525,):F(1)}),{(526,):F(82479248)})
deleted={'correction.singleChoice','scalar.correctedR.definition'}
assert {x['name'] for x in d['residuals'] if any(set(t['monomial'])&{65,524} for t in x['terms'])}==deleted|{'scalar.b.definition'}
d['residuals']=[row for row in d['residuals'] if row['name'] not in deleted]
for row in d['residuals']:
 if row['name']=='scalar.b.definition':row['terms']=enc(newb)
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in {65,524}]
d['status']='Research442: deterministic correction c=r+4896 using fixed2/3/17valuations; arithmetic review required.'
total={}
for row in d['residuals']:
 q=norm(p(row['terms']));total=add(total,mul(q,q))
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
write('candidate442-ir.json',d);write('polynomial442.json',{'fixedParameter':d['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate442-ir.json'),'polynomialSha256':sha(H/'polynomial442.json'),'variables':len(d['coordinates']),'residuals':len(d['residuals']),'monomials':len(total),'removedCoordinates':[65,524],'rTerms':enc(r),'newBTerms':enc(newb)})
print((H/'CERTIFICATE.json').read_text())
