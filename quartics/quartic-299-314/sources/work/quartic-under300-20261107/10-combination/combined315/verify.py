"""Independent literal chain transport and full primitive sum of squares."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
pins={
 'base':('quartic-under300-20261107/10-combination/combined318/candidate318-ir.json','e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1'),
 'old':('quartic-optimization-20261107/resume-depth-20261107/three326/candidate326-ir.json','48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'),
 'component':('quartic-optimization-20261107/resume-depth-20261107/chain323/candidate323-ir.json','dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd')}
def load(p,h):
 b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==h
 return json.loads(b)
d={k:load(WORK/p,h) for k,(p,h) in pins.items()}
new=load(H/'candidate315-ir.json','d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8')
table=load(H/'polynomial315.json','2e8879814484a8c838c700215d21c7c625f9b0569a5fa4d2e5e23d5c05055fd1')
changes={}
for section in ['coordinates','residuals']:
 maps={k:{r['id']:r for r in doc[section]} for k,doc in d.items()};actual={r['id']:r for r in new[section]}
 assert len(actual)==len(new[section])
 changed={i for i in maps['old'].keys()|maps['component'].keys() if maps['old'].get(i)!=maps['component'].get(i)}
 changes[section]=sorted(changed)
 for i in actual.keys()|maps['base'].keys()|changed:
  if i in changed:
   assert maps['base'].get(i)==maps['old'].get(i)
   assert actual.get(i)==maps['component'].get(i)
  else:assert actual.get(i)==maps['base'].get(i)
for k,v in d['base'].items():
 if k not in {'coordinates','residuals','status'}:assert new[k]==v
assert changes['coordinates']==[355,361,403,409,451,457]
assert changes['residuals']==[313,363,413,544,546,550,552,556,558,745,760,775]
def dec(r):
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 assert len(p)==len(r['terms']) and all(p.values())
 return p
def mul(p,q):
 z=defaultdict(F)
 for m,c in p.items():
  for n,e in q.items():z[tuple(sorted(m+n))]+=c*e
 return {m:c for m,c in z.items() if c}
def var(i):return {(i,):F(1)}
def sub(p,q):
 z=defaultdict(F,p)
 for m,c in q.items():z[m]-=c
 return {m:c for m,c in z.items() if c}
rows={r['id']:r for r in new['residuals']}
def named(s):return next(r for r in rows.values() if r['name']==s)
consumer_checks={}
for det,E,A,B,J,Q,L,M in [(0,350,832,356,355,359,369,360),(1,398,833,404,403,407,417,408),(2,446,834,452,451,455,465,456)]:
 p=dec(named(f'detector{det}.eWeight.definition'));assert p.pop(())==-1
 R={}
 for m,c in p.items():
  assert E in m
  n=list(m);n.remove(E);R[tuple(n)]=c
 assert all(len(m)<=1 for m in R)
 assert dec(named(f'detector{det}.toric.c.definition'))==sub(mul(var(E),var(J)),mul(R,R))
 assert dec(named(f'four.det{det}.E4'))==sub(mul(var(A),var(J)),var(E))
 assert dec(named(f'detector{det}.toric.q10.definition'))==sub(mul(var(Q),var(J)),mul(var(B),var(B)))
 consumer_checks[J]=[r['id'] for r in rows.values() if any(J in t['monomial'] for t in r['terms'])]
 assert set(consumer_checks[J])=={[544,550,556][det],[745,760,775][det],[546,552,558][det]}
 for oldhelper in [361,409,457]:assert not any(oldhelper in t['monomial'] for r in rows.values() for t in r['terms'])
# All eight outputs follow by divisions by known nonzero monomials in R and E.
known={-1,0,1}
for target,left,right,divisor in [(-3,-1,-1,1),(4,1,0,-3),(8,4,4,0),(19,8,8,-3),(39,19,19,-1),(79,39,39,-1),(158,79,79,0),(157,158,-1,0)]:
 assert {left,right,divisor}<=known and target==left+right-divisor;known.add(target)
oldrows={r['id']:r for r in d['base']['residuals']}
for i in [504,732,903,904,1903]:assert rows[i]==oldrows[i]
assert 1904 not in rows
for flip in [{1,2,3,4,21,22,23,24,112,113},{9,10,11,12,29,30,31,32,128,129},{13,14,15,16,33,34,35,36,136,137}]:
 for r in rows.values():assert len({sum(i in flip for i in m)%2 for m in dec(r)})==1
total=defaultdict(int);used=set()
for r in rows.values():
 p=dec(r);assert all(sum(i>=0 for i in m)<=2 for m in p)
 used.update(i for m in p for i in m if i>=0)
 den=lcm(*(c.denominator for c in p.values()));div=gcd(*(int(c*den) for c in p.values()))
 terms=list((m,int(c*den)//div) for m,c in p.items())
 for j,(m,c) in enumerate(terms):
  for k in range(j,len(terms)):
   n,e=terms[k];total[tuple(sorted(m+n))]+=c*e*(1 if j==k else 2)
total={m:c for m,c in total.items() if c};assert total==dec(table)
assert used=={c['id'] for c in new['coordinates']}
groups=defaultdict(dict)
for m,c in total.items():groups[tuple(i for i in m if i>=0)][m.count(-1)]=c
assert (len(used),len(rows),len(total),len(groups))==(315,285,5732,5729)
assert groups[(89,89,89,89)]=={2:186624,0:64}
assert all(abs(p.get(2,0))<186624 for m,p in groups.items() if m!=(89,89,89,89))
assert all(abs(p.get(1,0))<=1728 and abs(p.get(0,0)).bit_length()<2048 and max(p)<=2 for p in groups.values())
assert any(p=={0:1} for p in groups.values()) and max(map(len,groups))==4
result={'status':'PASS','variables':315,'witnesses':314,'residuals':285,'coefficientPowerEntries':5732,'monomials':5729,'degree':4,'content':1,'maximumCoefficient':'186624*3^(2^26)+64','sourcePins':pins,'changedObjects':changes,'repurposedHelperConsumers':consumer_checks,'successiveNonzeroExponentRecovery':True,'anchorAndCollisionRowsPreserved':True,'fullSOS':True,'acceptance':'provisional; component and composition reviews required'}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','variables','residuals','monomials','maximumCoefficient']},indent=2))
