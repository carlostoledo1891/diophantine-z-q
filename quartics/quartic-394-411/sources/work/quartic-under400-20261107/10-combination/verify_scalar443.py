"""Independent identity and full-coefficient check; imports no producer."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def add(a,b,k=1):
 c=a.copy()
 for m,v in b.items():c[m]=c.get(m,0)+k*v
 return {m:v for m,v in c.items() if v}
def mul(a,b):
 c={}
 for m,v in a.items():
  for n,w in b.items():
   key=tuple(sorted(m+n));c[key]=c.get(key,0)+v*w
 return {m:v for m,v in c.items() if v}
def con(v):return {():F(v)} if v else {}
def var(v):return {(v,):F(1)}
def fc(a,b=0):return con(a),con(b)
def plus(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def minus(a,b):return tuple(add(x,y,-1) for x,y in zip(a,b))
def times(a,b):return add(mul(a[0],b[0]),mul(a[1],b[1]),2),add(mul(a[0],b[1]),mul(a[1],b[0]))
def scale(a,c):return tuple({m:v*c for m,v in x.items() if v*c} for x in a)
def norm(a):
 d=reduce(lcm,(v.denominator for v in a.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in a.values()),0)
 s=F(d,g)*(1 if a[min(a)]>0 else -1)
 return {m:v*s for m,v in a.items()}

source=read('inputs/accepted445-ir.json');out=read('scalar443-ir.json');depth=read('inputs/depth519.json');cert=read('scalar443-certificate.json')
assert hashlib.sha256((H/cert['source']).read_bytes()).hexdigest()==cert['sourceSha256']
old={r['name']:p(r['terms']) for r in source['residuals']};new={r['name']:p(r['terms']) for r in out['residuals']};cn={c['name']:c['id'] for c in source['coordinates']}
def val(n):return tuple(p(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
def named(n):return tuple(var(cn[n+'.'+str(i)]) for i in range(2))
h,j=val('S.h'),val('S.j');g=named('scalar.shiftedS.reciprocal.g');z=val('Sscalar.z');rho=val('scalar.zRatio');s=named('primary.negativeReciprocalZ0')
h0,j0=val('H.h'),val('H.j')
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6)
N=minus(times(a,j),times(b,h));T=minus(minus(scale(times(times(D,b),g),2),scale(times(D,h),2)),times(times(a,b),j))
Z=plus(times(T,z),times(a,N));B=plus(times(h0,rho),times(j0,z));P=minus(times(h0,s),j0);E=minus(times(T,rho),times(times(a,N),s))
assert times(h0,E)==plus(minus(times(T,B),times(times(h0,s),Z)),times(times(T,z),P))
for i in range(2):
 assert norm(old[f'U0.z.definition.{i}'])==norm(P[i])
 assert norm(old[f'Sscalar.z.definition.{i}'])==norm(Z[i])
 assert norm(old[f'scalar.zRatio.definition.{i}'])==norm(B[i])
 assert new[f'scalar.zRatio.definition.{i}']==E[i]
ids={cn[f'Sscalar.z.{i}'] for i in range(2)};deleted={f'Sscalar.z.definition.{i}' for i in range(2)};changed={f'scalar.zRatio.definition.{i}' for i in range(2)}
assert {name for name,q in old.items() if any(ids.intersection(m) for m in q)}==deleted|changed
assert set(new)==set(old)-deleted
for name,q in new.items():
 if name not in changed:assert q==old[name]
assert {c['id']:c for c in out['coordinates']}=={c['id']:c for c in source['coordinates'] if c['id'] not in ids}
assert source['fixedParameter']==out['fixedParameter']
total={}
for q in new.values():
 assert max(sum(i!=-1 for i in m) for m in q)<=2
 total=add(total,mul(norm(q),norm(q)))
assert total==p(read('scalar443-polynomial.json')['terms'])
assert len(out['coordinates'])==443 and len(new)==420 and len(total)==6616
assert max(sum(i!=-1 for i in m) for m in total)==4
assert {i for m in total for i in m if i!=-1}=={c['id'] for c in out['coordinates']}
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
result={**cert['statistics'],'verified':True,'content':1,'maximumCoefficient':'16*3^(2^26)','scope':'Exact polynomial identity, complete consumer check and full SOS. Non-author acceptance pending.'}
(H/'scalar443-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
