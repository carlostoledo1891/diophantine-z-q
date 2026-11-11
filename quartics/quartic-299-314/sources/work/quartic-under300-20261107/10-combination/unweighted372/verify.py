"""Producer-free source transport, contact identities, Laurent circuit and SOS."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parents[1]/'01-elimination/squared-h/candidate390-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced'
old=json.loads(S.read_text(encoding='utf-8'));new=json.loads((H/'candidate372-ir.json').read_text(encoding='utf-8'))
sr={r['id']:r for r in old['residuals']};nr={r['id']:r for r in new['residuals']}
def add(*ps):
 d=defaultdict(Q)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def mul(p,q):
 d=defaultdict(Q)
 for m,c in p.items():
  for n,a in q.items():d[tuple(sorted(m+n))]+=c*a
 return {m:c for m,c in d.items() if c}
def sc(p,a):return {m:c*a for m,c in p.items() if c*a}
def v(i):return {(i,):Q(1)}
def const(c):return {():Q(c)} if c else {}
def power(p,n):
 out=const(1)
 for _ in range(n):out=mul(out,p)
 return out
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):Q(t['coefficient']) for t in r['terms']}
def sub(p,mapping):
 out={}
 for mon,c in p.items():
  term=const(c)
  for i in mon:term=mul(term,mapping.get(i,v(i)))
  out=add(out,term)
 return out
def solve(mp,row,target):
 p=dec(nr[row]);c=p.pop((target,));assert all(target not in m for m in p)
 mp[target]=sc(sub(p,mp),-1/c)
def contact(t):
 out=const(1)
 for c in [0,Q(-1,2),-1,Q(1,2399),Q(-32,407)]:out=mul(out,add(t,const(-c)))
 return out
drop={395,396,397,443,444,445};gone={349,350,351,399,400,401}
mapping={};special={};interfaces=[];Rs={}
for det,E,q,a,b,ed,er,qr,ar,br,dr,Brow,B,z,Fgate,t2,tlin,fc,tc,K in [
 (0,350,352,353,354,384,302,304,520,521,336,337,385,383,348,346,v(37),Q(3081901),Q(76265),Q(1952786)),
 (1,398,400,401,402,432,352,354,527,528,386,387,433,431,394,392,v(391),Q(77146368),Q(1220240),Q(1952786)),
 (2,446,448,449,450,480,402,404,534,535,436,437,481,479,442,440,add(v(37),sc(v(439),32)),Q(1205412),Q(76265),Q(1952786))]:
 # R is declared independently of the producer's coefficient extraction.
 R=sc(add(sc(v(Fgate),fc),sc(v(t2),tc),sc(tlin,-128 if det==1 else -32)),1/K)
 Rs[det]=R; mapping[q]=v(E);mapping[a]=const(1);mapping[b]=R
 drop|={q,a,b,ed};gone|={qr,ar,br,dr}
 special[er]=add(mul(v(E),R),const(-1))
 special[Brow]=add(mul(v(B),add(R,v(E),const(2))),sc(power(v(z),2),-1))
 mp={}
 seq=[[(298,346),(299,347),(300,348)],[(345,391),(346,392),(347,393),(348,394)],[(395,439),(396,440),(397,441),(398,442)]][det]
 for row,target in seq:solve(mp,row,target)
 A=[const(1),sc(v(343),4),add(const(1),sc(v(344),32),sc(v(345),256))][det]
 t=mul(A,v(37))
 assert sub(R,mp)==contact(t)
 interfaces.append({'detector':det,'R':'F5(A*lambda)','Erow':er,'Brow':Brow,'RplusInverse':'R+E+2'})
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-drop
assert new['coordinates']==[c for c in old['coordinates'] if c['id'] not in drop]
assert set(nr)==set(sr)-gone
changed=[]
for i,r in nr.items():
 expected=special.get(i,sub(dec(sr[i]),mapping))
 assert dec(r)==expected,(i,r['name'])
 a=dict(r);b=dict(sr[i]);a.pop('terms');b.pop('terms');assert a==b
 if r!=sr[i]:changed.append(i)
 assert not any(drop.intersection(t['monomial']) for t in r['terms'])
for k in old:
 if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
# All removed-only incidence is covered by the exact row reconstruction above.
incidence={str(i):sorted(r['id'] for r in old['residuals'] if any(i in t['monomial'] for t in r['terms'])) for i in sorted(drop)}
# Independent Laurent verification of the retained univariate weight circuits.
# Exponent -1 denotes E=R^-1, never an actual coordinate ID here.
for det,offset in enumerate([0,48,96]):
 E=350+offset;mp={E:-1,355+offset:3,356+offset:-8,359+offset:-19,360+offset:-79,361+offset:-2,362+offset:-3,369+offset:-38,374+offset:-158,375+offset:-237}
 rownames=[f'detector{det}.'+s for s in ['E1.power2.definition','E1.power3.definition','E10.power2.definition','E40.power2.definition','E40.power3.definition','toric.c.definition','toric.d.definition','toric.q10.definition','toric.q40.definition']]
 for name in rownames:
  row=next(r for r in nr.values() if r['name']==name)
  # Replace the affine R expression introduced into the c row by a formal R.
  if name.endswith('toric.c.definition'):
   assert dec(row)==add(mul(v(E),v(355+offset)),sc(power(Rs[det],2),-1))
   assert mp[E]+mp[355+offset]==2
  else:
   out=defaultdict(Q)
   for mon,c in dec(row).items():out[sum(mp[i] for i in mon)]+=c
   assert not any(out.values()),name
# Rational identity used to keep the bounded pole equation quadratic.
# (R+1)^2/R = R+2+1/R. At a required contact prime R has positive valuation.
assert add(power(add(v(9000),const(1)),2),sc(mul(v(9000),add(v(9000),const(2))),-1),const(-1))=={}
total={};used=set()
for row in new['residuals']:
 p=dec(row);assert max(sum(i>=0 for i in m) for m in p)<=2
 used|={i for m in p for i in m if i>=0}
 den=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p=sc(p,Q(den,g));total=add(total,mul(p,p))
assert total==dec(json.loads((H/'polynomial372.json').read_text(encoding='utf-8')))
assert used=={c['id'] for c in new['coordinates']}
assert (len(used),len(nr),len(total))==(372,342,6574)
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert [(m,c) for m,c in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),Q(16))]
assert max(abs(c) for m,c in total.items() if m.count(-1)==1)<=96
assert max(abs(c.numerator).bit_length() for m,c in total.items() if -1 not in m)<2048
assert reduce(gcd,(abs(c.numerator) for c in total.values()))==1
out={'candidateSha256':hashlib.sha256((H/'candidate372-ir.json').read_bytes()).hexdigest(),'variables':372,'residuals':342,'monomials':6574,'degree':4,'maximumCoefficient':'16*3^(2^26)','removedCoordinateConsumers':incidence,'changedRows':changed,'interfaces':interfaces,'allOtherObjectsExact':True,'LaurentExponentsVerified':[1,19,79],'fullSOS':True,'arithmeticStatus':'pending independent review'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='removedCoordinateConsumers'},indent=2))
