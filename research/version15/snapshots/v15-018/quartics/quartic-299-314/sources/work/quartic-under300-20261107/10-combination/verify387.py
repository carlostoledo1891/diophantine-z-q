"""Producer-free finite checks, including physical contact/trace interfaces."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
S=H.parent/'01-elimination/squared-h/candidate390-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced'
source=json.loads(S.read_text(encoding='utf-8')); result=json.loads((H/'candidate387-ir.json').read_text(encoding='utf-8'))
sr={r['id']:r for r in source['residuals']}; rr={r['id']:r for r in result['residuals']}
def tidy(p):return {m:c for m,c in p.items() if c}
def add(*ps):
 d=defaultdict(Q)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return tidy(d)
def scale(p,c):return tidy({m:v*c for m,v in p.items()})
def mul(p,q):
 d=defaultdict(Q)
 for m,c in p.items():
  for n,v in q.items():d[tuple(sorted(m+n))]+=c*v
 return tidy(d)
def power(p,n):
 z={():Q(1)}
 for _ in range(n):z=mul(z,p)
 return z
def v(i):return {(i,):Q(1)}
def const(x):return {():Q(x)} if x else {}
def decode(r):return {tuple([-1]*t['sPower']+t['monomial']):Q(t['coefficient']) for t in r['terms']}
def substitute(p,mapping):
 out={}
 for mon,c in p.items():
  t=const(c)
  for i in mon:t=mul(t,mapping.get(i,v(i)))
  out=add(out,t)
 return out
deleted={382,430,478}; deletedrows={334,384,434}
assert [c for c in source['coordinates'] if c['id'] not in deleted]==result['coordinates']
assert set(rr)==set(sr)-deletedrows
assert all(rr[i]==sr[i] for i in rr)
assert {r['id'] for r in source['residuals'] if any(deleted.intersection(t['monomial']) for t in r['terms'])}==deletedrows
for k in source:
 if k not in {'coordinates','residuals','status'}:assert source[k]==result[k]
for w,inv,row,z,normrow,e,ed,B,brow in [(380,382,334,383,335,350,384,385,337),(428,430,384,431,385,398,432,433,387),(476,478,434,479,435,446,480,481,437)]:
 assert decode(sr[row])==add(const(1),scale(mul(v(w),v(inv)),-1))
 assert decode(rr[normrow])==add(power(v(w),2),scale(power(v(w+1),2),-2),scale(mul(v(w),v(z)),-2))
 assert decode(rr[brow])==add(power(v(z),2),mul(v(e),v(B)),scale(mul(v(ed),v(B)),-4 if brow==387 else -1))
# Solve only the retained, named polynomial gates. No candidate producer is used.
def gate(mapping,row,target):
 p=decode(rr[row]); a=p.pop((target,)); assert all(target not in m for m in p)
 mapping[target]=scale(substitute(p,mapping),-1/a)
 return mapping[target]
theta=[Q(0),Q(-1,2),Q(-1),Q(1,2399),Q(-32,407)]
def contact(t):
 z=const(1)
 for a in theta:z=mul(z,add(t,const(-a)))
 return z
maps=[]; interfaces=[]
for det in range(3):
 m={}; lam=v(37)
 if det==0:
  a=const(1); t=lam
  seq=[(298,346),(299,347),(300,348)]; erow=302; E=350; qrow=304; q=352; econst=Q(1952786)
 elif det==1:
  a=scale(v(343),4)
  seq=[(345,391),(346,392),(347,393),(348,394),(349,395),(350,396),(351,397)]
  erow=352; E=398; qrow=354; q=400; econst=Q(1952786,16)
  t=mul(a,lam)
 else:
  a=add(const(1),scale(v(344),32),scale(v(345),256))
  seq=[(395,439),(396,440),(397,441),(398,442),(399,443),(400,444),(401,445)]
  erow=402; E=446; qrow=404; q=448; econst=Q(1952786)
  t=mul(a,lam)
 for row,target in seq:gate(m,row,target)
 delta=add(t,const(-1))
 expected=scale(add(mul(contact(t),v(E)),scale(mul(power(a,5),power(delta,5)),-1)),econst)
 actual=substitute(decode(rr[erow]),m)
 assert actual==expected,('weight',det,len(actual),len(expected))
 assert substitute(decode(rr[qrow]),m)==add(mul(power(delta,3),v(q)),scale(v(E),-1))
 ed=[384,432,480][det]; B=[385,433,481][det]; z=[383,431,479][det]
 gate(m,[336,386,436][det],ed)
 assert substitute(decode(rr[[337,387,437][det]]),m)==add(power(v(z),2),scale(mul(mul(v(E),delta),v(B)),-1))
 maps.append(m)
 interfaces.append({'detector':det,'Erow':erow,'qrow':qrow,'weightEquation':'F5(t)*E=A^5*(t-1)^5','physicalScale':{'0':'1','1':'4*v343','2':'1+32*v344+256*v345'}[str(det)]})
# The scale is nonzero: scale0=(2*productReal)^2, productReal>0;
# scale1=(1+16*productImaginarySquare)^2>0, checked from physical square gates.
assert decode(rr[296])==add(power(v(342),2),scale(v(344),-1))
assert decode(rr[297])==add(power(v(344),2),scale(v(345),-1))
assert substitute(add(const(1),scale(v(344),32),scale(v(345),256)),{345:power(v(344),2)})==power(add(const(1),scale(v(344),16)),2)
f1=Q(1)
for a in theta:f1*=1-a
assert f1==Q(3*2398*439,2399*407)
def factors(n):
 out=[]; p=2
 while p*p<=n:
  if n%p==0:
   out.append(p)
   while n%p==0:n//=p
  p+=1
 if n>1:out.append(n)
 return out
assert max(factors(f1.numerator)+factors(f1.denominator))<76176
# Full primitive SOS, including the symbolic coefficient parameter.
total={}; used=set()
for row in result['residuals']:
 p=decode(row); used|={i for m in p for i in m if i>=0}
 assert max(sum(i>=0 for i in m) for m in p)<=2
 den=reduce(lcm,(c.denominator for c in p.values()),1)
 numer={m:int(c*den) for m,c in p.items()}; g=reduce(gcd,(abs(c) for c in numer.values()))
 p={m:Q(c,g) for m,c in numer.items()}
 total=add(total,mul(p,p))
table=decode(json.loads((H/'polynomial387.json').read_text(encoding='utf-8')))
assert total==table
assert used=={c['id'] for c in result['coordinates']}
assert len(result['coordinates'])==387 and len(rr)==357
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert [(m,c) for m,c in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),Q(16))]
assert max(abs(c) for m,c in total.items() if m.count(-1)==1)<=96
assert max(abs(c.numerator).bit_length() for m,c in total.items() if -1 not in m)<2048
assert reduce(gcd,(abs(c.numerator) for c in total.values()))==1
evidence={'candidateSha256':hashlib.sha256((H/'candidate387-ir.json').read_bytes()).hexdigest(),'variables':387,'residuals':357,'monomials':len(total),'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','deletedRows':sorted(deletedrows),'completeIncidenceChecked':True,'allOutsideObjectsUnchanged':True,'contactInterfaces':interfaces,'F5at1':str(f1),'F5at1PrimeSupport':sorted(set(factors(f1.numerator)+factors(f1.denominator))),'fullSOS':True,'arithmeticStatus':'requires independent review of conditional detector use'}
(H/'VERIFICATION387.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
print(json.dumps(evidence,indent=2))
