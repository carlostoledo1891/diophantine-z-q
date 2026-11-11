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
source=read('inputs/released498.json');out=read('v0-493-ir.json');depth=read('inputs/depth519.json');cert=read('v0-493-certificate.json')
old={r['name']:p(r['terms']) for r in source['residuals']};new={r['name']:p(r['terms']) for r in out['residuals']}
cn={c['name']:c['id'] for c in out['coordinates']}
def val(n):return tuple(p(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6);c=times(a,a)
h,j,x=map(val,['H.h','H.j','H.x']);g=tuple(var(cn[f'V0.reciprocal.g.{i}']) for i in range(2));f=val('V0.f');ell=val('logV0');G=val('logV0.polynomial')
d=plus(times(c,x),D);N=minus(times(a,j),times(b,h));T=minus(minus(scale(times(times(D,b),g),2),scale(times(D,h),2)),times(times(a,b),j))
expected={}
for i,q in enumerate(minus(times(d,g),N)):expected[f'V0.reciprocal.g.definition.{i}']=q
for i,q in enumerate(minus(f,times(g,g))):expected[f'V0.f.definition.{i}']=q
for i,q in enumerate(plus(times(T,ell),times(times(a,N),G))):expected[f'logV0.definition.{i}']=q
deleted=set(cert['deletedRows'])
assert set(new)==(set(old)-deleted)|set(expected)
for name,q in new.items():assert norm(q)==norm(expected[name] if name in expected else old[name]),name
removed=set(cert['removedCoordinates']);assert len(removed)==7
assert {name for name,q in old.items() if any(set(m)&removed for m in q)}==deleted|set(cert['changedRows'])
assert {c['id'] for c in out['coordinates']}==({c['id'] for c in source['coordinates']}-removed)|{700,701}
# The retained V1 ratio supplies nonvanishing of ell0. Its numerator is
# exactly z(V1)*(1-2w/5-2w^2/15), nonzero for a genuine doubled point.
z1=val('V1.z');G1=val('logV1.polynomial');w1=val('logV1.w');f1=val('V1.f');f1sq=val('logV1.fSquare');LP=val('LP1')
ratio=minus(times(z1,G1),times(ell,LP))
for i in range(2):
 assert norm(old[f'logV1.{i}.definition'])==norm(ratio[i])
 assert norm(old[f'logV1.fSquare.{i}.definition'])==norm(minus(times(f1,f1),f1sq)[i])
assert w1==times(D,f1sq)
def in_span(q,basis):
 reduced=[]
 for r in basis:
  r=dict(r)
  for pivot,br in reduced:
   if pivot in r:r=add(r,br,-r[pivot])
  if r:
   pivot=min(r);r={m:v/r[pivot] for m,v in r.items()};reduced.append((pivot,r))
 for pivot,r in reduced:
  if pivot in q:q=add(q,r,-q[pivot])
 return not q
err=plus(plus(minus(G1,fc(1)),scale(w1,F(2,5))),scale(times(w1,w1),F(2,15)))
assert all(in_span(q,[old[f'logV1.polynomial.{i}.definition'] for i in range(2)]) for q in err)
assert 1-F(2,5)-F(2,15)==F(7,15)>0
# Generic reciprocal identities in Q(sqrt2)[h,j]/(j^2-h^4+D).
HH,JJ=10000,10001
def rf(q):
 ans=fc(0)
 for side,r in enumerate(q):
  for m,v in r.items():
   n=m.count(JJ);rest=tuple(i for i in m if i!=JJ);rest=tuple(sorted(rest+((JJ,) if n%2 else ())))
   atom=({rest:v},{}) if side==0 else ({},{rest:v})
   for _ in range(n//2):atom=times(atom,minus(( {(HH,HH,HH,HH):F(1)},{}),D))
   ans=plus(ans,atom)
 return ans
def rm(a,b):return rf(times(a,b))
def power(q,n):
 ans=fc(1)
 for _ in range(n):ans=rm(ans,q)
 return ans
hh=(var(HH),{});jj=(var(JJ),{});xx=power(hh,2);dd=plus(rm(c,xx),D);dx=minus(xx,c)
nn=minus(rm(a,jj),rm(b,hh));mm=minus(scale(rm(rm(a,D),rm(hh,plus(xx,c))),-2),rm(b,rm(jj,minus(rm(c,xx),D))))
sn=plus(rm(hh,jj),rm(a,b));xn=minus(power(sn,2),rm(plus(xx,c),power(dx,2)))
yn=minus(rm(sn,minus(rm(xx,power(dx,2)),xn)),rm(rm(hh,jj),power(dx,3)))
identities=[minus(plus(power(mm,2),rm(D,power(nn,4))),power(dd,4)),minus(rm(xn,power(nn,2)),rm(power(dx,2),power(dd,2))),minus(rm(yn,power(nn,3)),rm(rm(mm,dd),power(dx,3))),minus(rm(nn,plus(rm(a,jj),rm(b,hh))),rm(dx,dd))]
assert all(q==fc(0) for q in identities)
tn=plus(rm(dd,minus(scale(rm(D,hh),-2),rm(rm(a,b),jj))),scale(rm(rm(D,b),nn),2))
assert tn==rm(a,mm)
total={}
for q in new.values():
 assert max(sum(i!=-1 for i in m) for m in q)<=2
 ts=list(norm(q).items())
 for i,(m,v) in enumerate(ts):
  for j in range(i,len(ts)):
   n,w=ts[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+v*w*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read('v0-493-polynomial.json')['terms'])
assert len(out['coordinates'])==493 and len(new)==462 and len(total)==24567
assert max(sum(i!=-1 for i in m) for m in total)==4
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
result={'verified':True,'variables':493,'residuals':462,'monomials':24567,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':hashlib.sha256((H/'v0-493-ir.json').read_bytes()).hexdigest(),'status':'New V0 chart; requires non-author mathematical review.'}
(H/'v0-493-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
