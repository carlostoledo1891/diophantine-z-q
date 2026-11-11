"""No-producer verification of the Lucas affine change and complete SOS."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent
def load(p,h):
 assert hashlib.sha256(p.read_bytes()).hexdigest()==h
 return json.loads(p.read_bytes())
old=load(H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json','7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5')
new=load(H/'candidate314-ir.json','aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382')
table=load(H/'polynomial314.json','1fc9ba1e03e5134bd3173f22d80ecc5c29838996c1cb58839264844f6358d77e')
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
def add(*ps):
 out=defaultdict(F)
 for p in ps:
  for m,c in p.items():out[m]+=c
 return {m:c for m,c in out.items() if c}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
 out=defaultdict(F)
 for m,c in p.items():
  for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
 return {m:c for m,c in out.items() if c}
def v(i):return {(i,):F(1)}
def fm(p,q):return add(mul(p[0],q[0]),scale(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0]))
def fa(*ps):return add(*(p[0] for p in ps)),add(*(p[1] for p in ps))
def fs(p,c):return scale(p[0],c),scale(p[1],c)
def pair(i):return v(i),v(i+1)
rr={r['id']:r for r in new['residuals']};oo={r['id']:r for r in old['residuals']}
assert set(rr)==set(oo)
assert {i for i in rr if rr[i]!=oo[i]}=={201,202,205,206}
assert {r['id'] for r in old['residuals'] if any({249,250}.intersection(t['monomial']) for t in r['terms'])}=={201,202,205,206}
A,T,Z,S,V=map(pair,[236,240,244,249,251])
Sdef=fa(fm(A,Z),fs(Z,-2),fs(S,-1))
Fdef=fa(fm(T,T),fm(S,S),fs(fm(S,V),-1),fs((v(253),scale(v(254),2)),-1))
for j in range(2):assert dec(rr[201+j])==Sdef[j] and dec(rr[205+j])==Fdef[j]
for a,b in zip(old['coordinates'],new['coordinates']):
 if a['id'] in [249,250]:assert {k:v for k,v in a.items() if k!='name'}=={k:v for k,v in b.items() if k!='name'}
 else:assert a==b
for k in old:
 if k not in ['coordinates','residuals','status']:assert old[k]==new[k]
def substitute(p,sign):
 out={}
 for m,c in p.items():
  z={():c}
  for i in m:z=mul(z,add(v(i),scale(v(i-5),2*sign)) if i in [249,250] else v(i))
  out=add(out,z)
 return out
for i in [201,202,205,206]:
 assert substitute(dec(oo[i]),1)==dec(rr[i])
 assert substitute(dec(rr[i]),-1)==dec(oo[i])
total=defaultdict(int);used=set()
for r in rr.values():
 p=dec(r);assert max(sum(i>=0 for i in m) for m in p)<=2
 used.update(i for m in p for i in m if i>=0)
 den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
 terms=[(m,int(c*den)//g) for m,c in p.items()]
 for j,(m,c) in enumerate(terms):
  for k in range(j,len(terms)):
   n,d=terms[k];total[tuple(sorted(m+n))]+=c*d*(1 if j==k else 2)
total={m:c for m,c in total.items() if c}
assert total==dec(table) and len(total)==6077 and len(used)==314 and len(rr)==283
assert used=={c['id'] for c in new['coordinates']}
assert gcd(*total.values())==1 and max(sum(i>=0 for i in m) for m in total)==4
group=defaultdict(dict)
for m,c in total.items():group[tuple(i for i in m if i>=0)][m.count(-1)]=c
assert len(group)==6074
assert group[(89,89,89,89)]=={2:186624,0:64}
assert all(abs(p.get(2,0))<186624 for m,p in group.items() if m!=(89,89,89,89))
assert all(abs(p.get(1,0))<=1728 and max(p)<=2 for p in group.values())
assert all(abs(c).bit_length()<2048 for m,c in total.items() if -1 not in m)
result={'status':'PASS','variables':314,'residuals':283,'monomials':6074,'coefficientPowerEntries':6077,'monomialsSaved':61,'degree':4,'content':1,'maximumCoefficient':'186624*3^(2^26)+64','scope':'Exact affine equivalence checked both ways; author finite certificate, no independent acceptance asserted.'}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
