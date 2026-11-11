"""Author's exact row/certificate verification; independent review is separate."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parents[1]/'03-depth/candidate392t-ir.json'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(S)=='846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba'
assert sha(H/'candidate390-ir.json')=='c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced'
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def sc(p,c):return {m:x*c for m,x in p.items() if x*c}
def mul(p,q):
 d=defaultdict(F)
 for m,c in p.items():
  for n,e in q.items():d[tuple(sorted(m+n))]+=c*e
 return {m:c for m,c in d.items() if c}
def v(i):return {(i,):F(1)}
def const(c):return {():F(c)} if c else {}
def sq(p):return mul(p,p)
def pol(r):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
def sub(p,mapping):
 out={}
 for m,c in p.items():
  term=const(c)
  for i in m:term=mul(term,mapping.get(i,v(i)))
  out=add(out,term)
 return out
def norm(p):
 d=reduce(lcm,[c.denominator for c in p.values()],1);g=reduce(gcd,[abs(int(c*d)) for c in p.values()]);return sc(p,F(d,g))
def kc(a,b=0):return const(a),const(b)
def ka(a,b):return add(a[0],b[0]),add(a[1],b[1])
def ks(a,b):return add(a[0],sc(b[0],-1)),add(a[1],sc(b[1],-1))
def km(a,b):return add(mul(a[0],b[0]),sc(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
old=read(S);new=read(H/'candidate390-ir.json');br={r['id']:r for r in old['residuals']};ar={r['id']:r for r in new['residuals']}
deleted={34,35,112,113,130,131,263,264,661,662};replaced=deleted-{263,264}
assert set(ar)==set(br)-{263,264}
for i in set(br)-deleted:assert br[i]==ar[i]
assert {i for i,r in br.items() if any(set(t['monomial'])&{140,141,160,161} for t in r['terms'])}==deleted
assert not any(set(t['monomial'])&{160,161} for r in ar.values() for t in r['terms'])
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert set(nc)==set(oc)-{160,161}
for i in nc:
 want=oc[i].copy()
 if i in (140,141):want['name']=f'H.kummer.vSquare.{i-140}'
 assert nc[i]==want
for key in old:
 if key not in ('residuals','coordinates','status'):assert old[key]==new[key]
U=(v(311),sc(v(312),2));V=(v(178),sc(v(179),2));W=(v(140),v(141));vv=(v(700),v(701));tt=(v(142),v(143))
D=kc(11,-6);b=kc(F(39,8),F(-9,2));c=kc(F(57,8),F(-7,2));ci=kc(F(456,1681),F(224,1681))
assert km(c,ci)==kc(1)
Q=km(ci,ks(ks(kc(1),km(D,W)),km(kc(2),km(b,vv))))
wants=[ks(W,km(vv,vv)),ks(km(U,V),km(W,W)),ks(km(Q,Q),ka(ka(U,V),km(kc(2),W))),ks(km(tt,ka(U,W)),km(Q,vv))]
for ids,pp in zip([(34,35),(112,113),(130,131),(661,662)],wants):
 for i,p in zip(ids,pp):assert pol(ar[i])==p
# Abstract quotient numerator identities for f=(U+W)/Q,F=(V+W)/Q.
u,z,w,q=[v(i) for i in (1000,1001,1002,1003)]
e=add(mul(u,z),sc(sq(w),-1));h=add(sq(q),sc(u,-1),sc(z,-1),sc(w,-2))
assert add(sq(add(u,w)),sc(mul(u,sq(q)),-1))==add(sc(mul(u,h),-1),sc(e,-1))
assert add(sq(add(z,w)),sc(mul(z,sq(q)),-1))==add(sc(mul(z,h),-1),sc(e,-1))
assert add(mul(add(u,w),add(z,w)),sc(mul(w,sq(q)),-1))==add(sc(mul(w,h),-1),e)
# Q=0 implies (U+W)^2=0 from the first identity. U=0 implies W^2=0.
# Exact fixed constants and their norms; all possible bad primes are 2,7,41.
def cv(pair):return tuple(p.get((),F(0)) for p in pair)
def kn(pair):a,b=cv(pair);return a*a-2*b*b
assert cv(ka(c,b))==(F(12),F(-8)) and kn(ka(c,b))==16
assert cv(ks(c,b))==(F(9,4),F(1)) and kn(ks(c,b))==F(49,16)
assert kn(c)==F(1681,64)
vplus=kc(F(3,4),F(1,2));vminus=kc(F(-36,49),F(16,49))
for root in (vplus,vminus):assert ka(ka(km(D,km(root,root)),km(kc(2),km(b,root))),kc(-1))==kc(0)
# High-order H signed-square factor is literally retained in each detector.
names={r['name']:r for r in new['residuals']};other=(v(313),sc(v(314),2));co=km(U,other)
for j in (0,1):assert pol(names[f'hybrid.40.group0.co2.{j}.definition'])==add(v(626+j),sc(co[j],-1))
for det,weight,weight2,out in [(0,360,374,646),(1,408,422,666),(2,456,470,686)]:
 for j in (0,1):
  want=add(v(out+j),sc(const(1) if j==0 else {},-1),sc(mul(ka(U,other)[j],v(weight)),-1),sc(mul(v(626+j),v(weight2)),-1))
  assert pol(names[f'hybrid.det{det}.eval40.0.{j}.definition'])==want
# Low-order conjugate V factor: check the optimized triple with V arbitrary.
u=(V[0],sc(V[1],-1));p=(v(255),sc(v(256),2));z=(v(257),sc(v(258),2));c1=ka(ka(u,p),z);c2=ka(km(u,ka(p,z)),km(p,z))
for j,n in enumerate(['hybrid.1.group0.co2.0.definition','hybrid.1.group0.right.co2.1.definition']):assert norm(pol(names[n]))==norm(add(v(608+j),sc(c2[j],-1)))
w2=km(km(D,V),km(D,V));mapping={180:sc(w2[0],F(1,193)),181:sc(w2[1],F(-1,132)),608:c2[0],609:c2[1]}
c3=km(km(u,p),z)
for j in (0,1):assert sub(pol(names[f'hybrid.1.group0.co3.{j}.definition']),mapping)==add(v(610+j),sc(c3[j],-1))
for det,weight,weight2,weight3,out in [(0,352,361,362,634),(1,400,409,410,654),(2,448,457,458,674)]:
 for j in (0,1):
  want=add(v(out+j),sc(const(1) if j==0 else {},-1),sc(mul(c1[j],v(weight)),-1),sc(mul(v(608+j),v(weight2)),-1),sc(mul(v(610+j),v(weight3)),-1))
  assert pol(names[f'hybrid.det{det}.eval1.0.{j}.definition'])==want
total={}
for row in ar.values():
 pp=norm(pol(row));assert max(sum(i>=0 for i in m) for m in pp)<=2
 total=add(total,mul(pp,pp))
assert total==pol(read(H/'polynomial390.json'))
assert len(total)==6989 and len(ar)==360 and len(nc)==390
assert {i for m in total for i in m if i>=0}==set(nc)
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert all(x.denominator==1 for x in total.values()) and reduce(gcd,[abs(x.numerator) for x in total.values()])==1
assert [(m,x) for m,x in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),F(16))]
assert (57,57,549,549) not in total and (-1,57,57,549,549) not in total
assert max(abs(x) for m,x in total.items() if m.count(-1)==1)<=96
assert max(abs(x.numerator).bit_length() for m,x in total.items() if -1 not in m)<2048
out={'passed':True,'candidateSha256':sha(H/'candidate390-ir.json'),'polynomialSha256':sha(H/'polynomial390.json'),'variables':390,'residuals':360,'monomials':6989,'genericReconstructionIdentities':True,'fixedBranchesBadPrimes':[2,7,41],'actualHighAndLowDetectorFactors':True,'allOutsideObjectsUnchanged':True,'fullSOS':True,'independentAcceptance':False}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
