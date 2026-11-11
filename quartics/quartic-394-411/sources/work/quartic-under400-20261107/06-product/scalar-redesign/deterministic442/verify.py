from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'one-correction444/candidate444-ir.json'
def read(f):return json.loads(f.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   key=s+t,tuple(sorted(m+n));d[key]=d.get(key,0)+v*w
 return {m:v for m,v in d.items() if v}
def var(i):return {(0,(i,)):F(1)}
def constant(c):return {(0,()):F(c)} if c else {}
def scale(a,k):return {m:v*k for m,v in a.items() if v*k}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 return scale(q,F(d,g)*(1 if q[min(q)]>0 else -1))
old=read(S);new=read(H/'candidate442-ir.json')
assert sha(S)=='c2c60a1bed5c929eb633b654e76d401dc96fc0edd1f09eee44324740c4cde837'
a={r['name']:p(r['terms']) for r in old['residuals']};b={r['name']:p(r['terms']) for r in new['residuals']}
r={(0,()):F(-105275102108),(0,(0,)):F(-8412883296),(0,(248,)):F(-8412883296),(0,(487,)):F(-21050600),(0,(488,)):F(-7629700),(0,(489,)):F(-45771136)}
power_error=add(var(600),mul(r,r),-1)
assert norm(a['scalar.r_power_2.definition'])==norm(power_error)
assert norm(a['reduced_scalar.root'])==norm(add(add(mul(var(604),var(542)),mul(var(540),var(540)),-1),mul(r,var(541)),-1))
cr=add(var(600),r,4896)
expected=add(mul(cr,var(525)),var(526),82479248)
assert set(b)==set(a)-{'correction.singleChoice','scalar.correctedR.definition'}
for name,q in b.items():assert norm(q)==norm(expected if name=='scalar.b.definition' else a[name]),name
assert {name for name,q in a.items() if any(set(m)&{65,524} for s,m in q)}=={'correction.singleChoice','scalar.correctedR.definition','scalar.b.definition'}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{65,524}
assert old['fixedParameter']==new['fixedParameter']
c=add(r,constant(4896));oldF=scale(add(cr,c,31581660),F(-1,82479248))
def substitute(q):
 d={}
 for (s,m),v in q.items():
  t={(s,()):v}
  for i in m:t=mul(t,c if i==65 else oldF if i==524 else var(i))
  d=add(d,t)
 return d
assert substitute(a['scalar.correctedR.definition'])==scale(power_error,F(1,4))
assert substitute(a['scalar.b.definition'])==scale(expected,F(-1,4))
def val(n,q):
 v=0
 while n%q==0:n//=q;v+=1
 return v,n
def square(n,q):
 v,u=val(n,q)
 return v%2==0 and (u%8==1 if q==2 else pow(u%q,(q-1)//2,q)==1)
assert 4896==2**5*3**2*17
for x in range(306):
 beta=51*(2*x+1)**2+2504
 rr=beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1);cc=rr+4896
 assert all(square(rr*cc,q) for q in [2,3,17])
 assert val(rr,2)[0]==2 and val(rr,3)[0]==1 and val(rr,17)[0]==0
total={}
for q in b.values():
 q=norm(q);assert max(len(m) for s,m in q)<=2
 total=add(total,mul(q,q))
assert total==p(read(H/'polynomial442.json')['terms'])
assert len(new['coordinates'])==442 and len(b)==419 and len(total)==6666
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
out={'passed':True,'variables':442,'residuals':419,'monomials':6666,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate442-ir.json'),'arithmeticReview':'pending03'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
