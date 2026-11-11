"""Producer-free finite, sign-symmetry and local identity checks for366."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parents[1]/'10-combination/candidate369-ir.json'
def read(p,pin):
 assert hashlib.sha256(p.read_bytes()).hexdigest()==pin,str(p)
 return json.loads(p.read_text())
old=read(S,'b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095')
new=read(H/'candidate366-ir.json','0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56')
table=read(H/'polynomial366.json','f9219fb79cc687a5af567e6e8cc7b7591ccb1ea4d8f803b7d7189122412e5e64')
assert new['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}
drop={70,71,72};gone={690,691,692}
assert new['coordinates']==[c for c in old['coordinates'] if c['id'] not in drop]
assert new['residuals']==[r for r in old['residuals'] if r['id'] not in gone]
assert {r['id'] for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms'])}==gone
for k in old:
 if k not in ('coordinates','residuals','status'):assert old[k]==new[k]
rr={r['id']:r for r in old['residuals']}
def clean(p):return {m:c for m,c in p.items() if c}
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return clean(d)
def sc(p,c):return clean({m:c*v for m,v in p.items()})
def sub(p,q):return add(p,sc(q,-1))
def mul(*ps):
 out={():F(1)}
 for p in ps:
  d=defaultdict(F)
  for m,c in out.items():
   for n,vv in p.items():d[tuple(sorted(m+n))]+=c*vv
  out=clean(d)
 return out
def sq(p):return mul(p,p)
def v(i):return {(i,):F(1)}
def const(q):return {():F(q)} if q else {}
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
def ka(a,b):return add(a[0],b[0]),add(a[1],b[1])
def ks(a,b):return sub(a[0],b[0]),sub(a[1],b[1])
def km(a,b):return add(mul(a[0],b[0]),sc(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def kc(a,b=0):return const(a),const(b)
def kscale(a,q):return sc(a[0],q),sc(a[1],q)

# Exact involution of the entire remaining system, not just the S block.
flips={5,6,7,8,25,26,27,28,55,56,57,120,121,543,544,549}
assert flips<={c['id'] for c in new['coordinates']}
signrows=[]
for r in new['residuals']:
 parity={sum(i in flips for i in t['monomial'])%2 for t in r['terms']}
 assert len(parity)==1,('not homogeneous under involution',r['id'])
 if any(flips.intersection(t['monomial']) for t in r['terms']):
  signrows.append({'id':r['id'],'name':r['name'],'multiplier':-1 if next(iter(parity)) else 1})

# Exact retained scalar point and anchor interfaces.
h=(v(5),v(6));j=(v(7),v(8));x=(v(84),sc(v(85),2));g=(v(543),v(544))
a=kc(-1,F(7,4));b=kc(F(39,8),F(-9,2));c=km(a,a);D=kc(11,-6)
G=ka(ks(km(ka(km(c,x),D),g),km(a,j)),km(b,h))
assert dec(rr[513])==sc(G[0],8) and dec(rr[514])==sc(G[1],8)
assert dec(rr[8])==sub(km(h,h)[0],x[0])
assert dec(rr[9])==sc(sub(km(h,h)[1],x[1]),F(1,2))
assert dec(rr[732])==sub(mul(v(543),v(549)),const(1))
U,V,W,g0,g1,tau,C=map(v,[55,56,57,543,544,549,-1])
assert dec(rr[504])==add(sq(U),sc(sq(V),6),sc(sq(W),-2),sc(sq(g1),-12),sc(mul(C,tau,W),-4))
qold=add(sq(mul(g0,U)),sc(sq(mul(g0,V)),6),sc(sq(mul(g0,W)),-2),
         sc(sq(sc(mul(g0,g1),2)),-3),sc(mul(C,g0,W),-4))
assert sub(qold,mul(sq(g0),dec(rr[504])))==sc(mul(C,g0,W,dec(rr[732])),4)

# The removed block is exactly the half-abscissa norm chart.
half=(v(70),v(71));q=ks(ks(km(half,half),kscale(km(ka(x,j),half),2)),D)
assert dec(rr[690])==q[0] and dec(rr[691])==q[1]
assert dec(rr[692])==add(sq(v(70)),sc(sq(v(71)),-2),sq(v(72)))

# Generic reciprocal subtraction identity, without an odd-index premise.
# Set x=h²,c=a² and reduce j²=h⁴-D, b²=a⁴-D.
aa,hh,jj,bb,DD=map(v,range(9000,9005))
xx,cc=sq(hh),sq(aa);NN=sub(mul(aa,jj),mul(bb,hh));MM=add(mul(hh,jj),mul(aa,bb));dd=add(mul(cc,xx),DD)
identity=sub(mul(sq(NN),sub(sq(MM),mul(add(xx,cc),sq(sub(xx,cc))))),mul(sq(dd),sq(sub(xx,cc))))
def reduce_squares(p,index,replacement):
 out={}
 for mon,coeff in p.items():
  n=mon.count(index);remain=tuple(i for i in mon if i!=index)+(index,)*(n%2)
  term={tuple(sorted(remain)):coeff}
  for _ in range(n//2):term=mul(term,replacement)
  out=add(out,term)
 return out
assert reduce_squares(reduce_squares(identity,9002,sub(sq(xx),DD)),9003,sub(sq(cc),DD))=={}

# Good reduction and the odd-multiple residue at 3.
def mod3(q):return q.numerator*pow(q.denominator,-1,3)%3
def kval(k):return tuple(p.get((),F(0)) for p in k)
ar,br,cr,Dr=[tuple(map(mod3,kval(k))) for k in (a,b,c,D)]
assert ar==(2,1) and br==(0,0) and cr==(0,1) and Dr==(2,0)
assert 64*pow(Dr[0],3,3)%3!=0
assert tuple(map(mod3,kval(km(c,kc(0,2)))))==(1,0)
assert {(u,w) for u in range(3) for w in range(3) if (u*u-2*w*w)%3==0}=={(0,0)}
assert {2*t*t%3 for t in (1,2)}=={2}

total={};used=set()
for r in new['residuals']:
 p=dec(r);used|={i for mon in p for i in mon if i>=0}
 assert max(sum(i>=0 for i in mon) for mon in p)<=2
 den=reduce(lcm,(q.denominator for q in p.values()),1);nn={m:int(q*den) for m,q in p.items()};gg=reduce(gcd,(abs(x) for x in nn.values()))
 pp={m:F(q,gg) for m,q in nn.items()};total=add(total,sq(pp))
assert total==dec(table) and used=={c['id'] for c in new['coordinates']}
assert (len(used),len(new['residuals']),len(total))==(366,336,6527)
assert max(sum(i>=0 for i in mon) for mon in total)==4
assert len({tuple(i for i in mon if i>=0) for mon in total})==len(total)
assert reduce(gcd,(abs(q.numerator) for q in total.values()))==1
assert {m:q for m,q in total.items() if m.count(-1)==2}=={(-1,-1,57,57,549,549):F(16)}
assert max(abs(q) for m,q in total.items() if m.count(-1)==1)<=96
assert max(abs(q.numerator).bit_length() for m,q in total.items() if -1 not in m)<2048
out={'candidateSha256':hashlib.sha256((H/'candidate366-ir.json').read_bytes()).hexdigest(),
 'variables':366,'witnesses':365,'residuals':336,'monomials':6527,'degree':4,'content':1,
 'maximumCoefficient':'16*3^(2^26)','allOutsideObjectsIdentical':True,'signInvolution':sorted(flips),
 'allAffectedSignRows':signrows,'local3Residues':{'xP':[0,1],'yP':[0,0],'fP':[0,2]},
 'fullSOS':True,'status':'finite pass; parity and sign-restoration proof require independent review'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='allAffectedSignRows'},indent=2))
