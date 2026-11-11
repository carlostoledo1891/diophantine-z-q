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
source=read('inputs/released498.json');out=read('scalar496-ir.json');depth=read('inputs/depth519.json');cert=read('scalar496-certificate.json')
assert hashlib.sha256((H/'inputs/released498.json').read_bytes()).hexdigest()==cert['sourceSha256']
old={r['name']:p(r['terms']) for r in source['residuals']};new={r['name']:p(r['terms']) for r in out['residuals']};cn={c['name']:c['id'] for c in source['coordinates']}
def val(n):return tuple(p(depth['values'][n+'.'+str(j)]['terms']) for j in range(2))
def pv(n):return tuple(var(cn['scalar.shiftedS.reciprocal.'+n+'.'+str(j)]) for j in range(2))
h,j,x=map(val,['S.h','S.j','S.x']);g,k=map(pv,['g','k']);z=val('Sscalar.z')
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6);delta=fc(3,-1)
assert times(delta,delta)==D
for i in range(2):assert norm(old[f'S.chart.x.{i}.definition'])==norm(minus(times(h,h),x)[i])
d=plus(times(times(a,a),x),D);N=minus(times(a,j),times(b,h));T=minus(minus(scale(times(times(D,b),g),2),scale(times(D,h),2)),times(times(a,b),j))
G=minus(times(d,g),N);K=minus(times(times(a,d),k),T);Z=plus(times(k,z),g);L=plus(times(T,z),times(a,N))
assert L==minus(minus(times(times(a,d),Z),times(z,K)),times(a,G))
deleted={f'scalar.shiftedS.reciprocal.k.definition.{i}' for i in range(2)};changed={f'Sscalar.z.definition.{i}':L[i] for i in range(2)}
ids={cn[f'scalar.shiftedS.reciprocal.k.{i}'] for i in range(2)}
assert {name for name,r in old.items() if any(set(m)&ids for m in r)}==deleted|set(changed)
for i in range(2):
 assert norm(old[f'scalar.shiftedS.reciprocal.g.definition.{i}'])==norm(G[i])
 assert norm(old[f'scalar.shiftedS.reciprocal.k.definition.{i}'])==norm(K[i])
 assert norm(old[f'Sscalar.z.definition.{i}'])==norm(Z[i])
assert set(new)==set(old)-deleted
for name,r in new.items():assert norm(r)==norm(changed[name] if name in changed else old[name]),name
assert {c['id'] for c in out['coordinates']}=={c['id'] for c in source['coordinates']}-ids
total={}
for r in new.values():
 assert max(sum(x!=-1 for x in m) for m in r)<=2
 ts=list(norm(r).items())
 for i,(m,v) in enumerate(ts):
  for jj in range(i,len(ts)):
   n,w=ts[jj];key=tuple(sorted(m+n));total[key]=total.get(key,0)+v*w*(1 if i==jj else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read('scalar496-polynomial.json')['terms'])
assert len(out['coordinates'])==496 and len(new)==465 and len(total)==24705
assert max(sum(x!=-1 for x in m) for m in total)==4
assert {v for m in total for v in m if v!=-1}=={c['id'] for c in out['coordinates']}
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
result={'verified':True,'variables':496,'witnesses':495,'residuals':465,'degree':4,'monomials':24705,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':hashlib.sha256((H/'scalar496-ir.json').read_bytes()).hexdigest(),'arithmeticStatus':'New algebraic equivalence, awaiting non-author review.'}
(H/'scalar496-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
