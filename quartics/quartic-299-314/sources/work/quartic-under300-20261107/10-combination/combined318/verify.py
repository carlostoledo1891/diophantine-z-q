"""Producer-free transport, private maps, sign actions and full coefficient check."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
pins={
 'base':('quartic-under300-20261107/10-combination/three-anchor319/candidate319-ir.json','61898500a23024afbf21aed5a35ee0b573beef0dcaa598caba07de884c4281f4'),
 'old':('quartic-under300-20261107/10-combination/combined320/candidate320-ir.json','d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f'),
 'component':('quartic-optimization-20261107/resume-elimination-20261107/exact319/candidate319-ir.json','847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676')}
def load(path,pin):
 b=path.read_bytes();assert hashlib.sha256(b).hexdigest()==pin,path
 return json.loads(b)
d={k:load(WORK/p,h) for k,(p,h) in pins.items()}
new=load(H/'candidate318-ir.json','e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1')
table=load(H/'polynomial318.json','664a1c0460a2b01c5b5162f3af3c9dfbd2afc6a90ed3e9d2a88d95eae5561fac')
for section in ['coordinates','residuals']:
 maps={k:{r['id']:r for r in doc[section]} for k,doc in d.items()}
 actual={r['id']:r for r in new[section]};assert len(actual)==len(new[section])
 changed={i for i in maps['old'].keys()|maps['component'].keys() if maps['old'].get(i)!=maps['component'].get(i)}
 assert changed==({55,56,57,903,904} if section=='coordinates' else {504,903,904})
 targets={({903:1903,904:1904}.get(i,i) if section=='residuals' else i):i for i in changed}
 assert len(targets)==len(changed)
 for j in actual.keys()|maps['base'].keys():
  if j not in targets:
   assert actual.get(j)==maps['base'].get(j),(section,j);continue
  i=targets[j]
  for source,match in [('old',maps['base'].get(j)),('component',actual.get(j))]:
   wanted=maps[source].get(i)
   if wanted is None:assert match is None
   else:assert match==dict(wanted,id=j),(section,j,source)
for key,value in d['base'].items():
 if key not in {'coordinates','residuals','status'}:assert new[key]==value
o={r['id']:r for r in d['base']['residuals']};n={r['id']:r for r in new['residuals']}
assert {903,904,1903}<=set(n) and 1904 not in n
assert n[903]==o[903] and n[904]==o[904] # Preserve the colliding detector rows.
def add(*ps):
 z=defaultdict(F)
 for p in ps:
  for m,c in p.items():z[m]+=c
 return {m:c for m,c in z.items() if c}
def scale(p,k):return {m:c*k for m,c in p.items() if c*k}
def mul(*ps):
 z={():F(1)}
 for p in ps:
  w=defaultdict(F)
  for m,c in z.items():
   for k,b in p.items():w[tuple(sorted(m+k))]+=c*b
  z={m:c for m,c in w.items() if c}
 return z
def v(i):return {(i,):F(1)}
def sq(p):return mul(p,p)
def dec(row):
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
 assert len(p)==len(row['terms']) and all(p.values())
 return p
def subst(p,mp):return add(*(scale(mul(*(mp.get(i,v(i)) for i in m)),c) for m,c in p.items()))
C,g,h,t,U,V,W,T,B=[v(i) for i in [-1,543,544,549,55,56,57,903,904]]
q=add(scale(sq(v(83)),48),scale(sq(v(87)),48),scale(sq(v(89)),432))
G=add(mul(g,t),{():F(-1)})
assert dec(n[732])==G
assert dec(o[1903])==add(T,scale(q,-1))
assert dec(o[1904])==add(B,scale(h,-2),scale(mul(C,T,t),-1))
assert dec(n[1903])==add(T,scale(mul(g,h),-2),scale(mul(C,q),-1))
assert dec(n[504])==add(sq(U),scale(sq(V),6),scale(sq(W),-2),scale(mul(C,W),-4),scale(sq(T),-3))
forward={55:mul(g,U),56:mul(g,V),57:mul(g,W),903:mul(g,B)}
reverse={55:mul(t,U),56:mul(t,V),57:mul(t,W),903:q,904:mul(t,T)}
assert subst(dec(n[1903]),forward)==add(mul(g,dec(o[1904])),mul(C,dec(o[1903])),mul(C,T,G))
assert subst(dec(n[504]),forward)==add(mul(sq(g),dec(o[504])),scale(mul(C,g,W,G),4))
assert subst(dec(o[1903]),reverse)=={}
assert subst(dec(o[1904]),reverse)==add(mul(t,dec(n[1903])),scale(mul(h,G),2))
assert subst(dec(o[504]),reverse)==mul(sq(t),dec(n[504]))
for rows,private,expected in [(o,{55,56,57,903,904},{504,1903,1904}),(n,{55,56,57,903},{504,1903})]:
 assert {i for i,row in rows.items() if any(private.intersection(z['monomial']) for z in row['terms'])}==expected
actions={'A':{1,2,3,4,21,22,23,24,112,113},'T':{9,10,11,12,29,30,31,32,128,129},'Z':{13,14,15,16,33,34,35,36,136,137}}
for flip in actions.values():
 for row in n.values():assert len({sum(i in flip for i in m)%2 for m in dec(row)})==1
total=defaultdict(int);used=set()
for row in n.values():
 p=dec(row);assert all(sum(i>=0 for i in m)<=2 for m in p)
 used.update(i for m in p for i in m if i>=0)
 den=lcm(*(c.denominator for c in p.values()));div=gcd(*(int(c*den) for c in p.values()))
 terms=list({m:int(c*den)//div for m,c in p.items()}.items())
 for j,(m,c) in enumerate(terms):
  for k in range(j,len(terms)):
   l,e=terms[k];total[tuple(sorted(m+l))]+=c*e*(1 if j==k else 2)
total={m:c for m,c in total.items() if c};assert total==dec(table)
assert used=={r['id'] for r in new['coordinates']}
groups=defaultdict(dict)
for m,c in total.items():groups[tuple(i for i in m if i>=0)][m.count(-1)]=c
assert (len(used),len(n),len(total),len(groups))==(318,288,5679,5676)
assert groups[(89,89,89,89)]=={2:186624,0:64}
assert all(abs(p.get(2,0))<186624 for m,p in groups.items() if m!=(89,89,89,89))
assert all(abs(p.get(1,0))<=1728 and abs(p.get(0,0)).bit_length()<2048 and max(p)<=2 for p in groups.values())
assert any(p=={0:1} for p in groups.values()) and max(map(len,groups))==4
result={'status':'PASS','variables':318,'witnesses':317,'residuals':288,'coefficientPowerEntries':5679,'monomials':5676,'degree':4,'content':1,'maximumCoefficient':'186624*3^(2^26)+64','sourcePins':pins,'fivePolynomialMapIdentities':True,'completePrivateConsumers':True,'detectorRows903_904Preserved':True,'rootRestorationSignActions':True,'acceptance':'provisional; independent final composition review required'}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
