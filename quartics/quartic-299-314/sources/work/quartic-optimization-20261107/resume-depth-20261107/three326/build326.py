"""Three-group mixed-residue packing. Independent review pending."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent
source=H.parent/'chain327/candidate327-ir.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665'
old=json.loads(source.read_bytes());new=copy.deepcopy(old)
def add(*args):
 out=defaultdict(F)
 for p in args:
  for m,c in p.items():out[m]+=c
 return {m:c for m,c in out.items() if c}
def scale(p,k):return {m:c*F(k) for m,c in p.items() if c*k}
def mul(p,q):
 out=defaultdict(F)
 for m,c in p.items():
  for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
 return {m:c for m,c in out.items() if c}
def var(i):return {(i,):F(1)}
def con(c):return {():F(c)} if c else {}
def pair(i,s=1):return (var(i),scale(var(i+1),s))
def ka(*args):return tuple(add(*(p[j] for p in args)) for j in range(2))
def km(p,q):return (add(mul(p[0],q[0]),scale(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0])))
def ks(p,q):return tuple(mul(v,q) for v in p)
def terms(p):return [{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in sorted(p.items())]
gone={r['id'] for r in old['residuals'] if r['name'].startswith(('four.high','four.primary')) or (r['name'].startswith('four.det') and not r['name'].endswith('.E4'))}
drop={b+j for b in (634,654,674) for j in range(8,12)}
repurpose={826,827}|{b+j for b in (634,654,674) for j in (6,7)}
assert all(r['id'] in gone for r in old['residuals'] if any((drop|repurpose).intersection(t['monomial']) for t in r['terms']))
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in drop]
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
nextrow=900
def row(name,p):
 global nextrow
 assert all(len(m)<=2 for m in p)
 new['residuals'].append({'id':nextrow,'name':name,'kind':'structural','block':'three_group_packing','terms':terms(p)});nextrow+=1
def coord(i,name):
 existing=next((c for c in new['coordinates'] if c['id']==i),None)
 if existing is not None:existing['name']=name
 else:new['coordinates'].append({'id':i,'name':name,'kind':'gate','block':'three_group_packing','protected':False})
def eqpair(i,name,p):
 for j in range(2):row(name+'.'+str(j),add(var(i+j),scale(p[j],-1)))
def sqpair(i,name,p):
 for j in range(2):coord(i+j,name+'.'+str(j))
 eqpair(i,name,km(p,p));return pair(i)
high=[pair(i,2) for i in (311,313,315,317)]
high.append((add(con(1),scale(var(253),-2),var(319)),add(scale(var(320),4),scale(var(254),-4))))
middle=[pair(305,2),(add(var(307),scale(var(232),-6),scale(var(0),1224),scale(var(248),1224),con(15321)),add(scale(var(308),2),scale(var(233),-6)))]
primary=[pair(i,2) for i in (255,257,259,261)]
leaves={'H0':high[0],'P1':primary[0]}
for name,i,value in [('H1',826,high[1]),('H2',820,high[2]),('H3',822,high[3]),('H4',835,high[4]),('M0',837,middle[0]),('M1',839,middle[1]),('P2',828,primary[1]),('P3',830,primary[2]),('P4',841,primary[3])]:
 leaves[name]=sqpair(i,'three.shared.'+name,value)
for name,i in zip(('T0','T2','T3','T4'),(182,200,212,224)):
 leaves[name]=(scale(add(scale(var(i),72097),scale(var(i+1),101904)),F(1,5764801)),scale(add(scale(var(i),-50952),scale(var(i+1),-72097)),F(1,5764801)))
leaves['Z1']=(add(scale(var(192),F(37249,2401)),scale(var(193),F(-34848,2401))),scale(add(var(193),scale(var(192),-1)),F(25476,2401)))
groups=((('H1',158),('H4',157),('M0',39),('T0',8),('T4',4)),(('H2',158),('H0',79),('T2',8),('Z1',4),('P1',1)),(('H3',158),('M1',39),('T3',8),('P2',157),('P3',4),('P4',1)))
for det,b,E,e4,e8,e39,e79,e158,W in ((0,634,350,832,356,369,360,374,380),(1,654,398,833,404,417,408,422,428),(2,674,446,834,452,465,456,470,476)):
 e157=843+det;coord(e157,f'three.det{det}.E157')
 r=next(r for r in old['residuals'] if r['name']==f'detector{det}.eWeight.definition');R={}
 for t in r['terms']:
  if E in t['monomial']:
   m=list(t['monomial']);m.remove(E);R[tuple(m)]=F(t['coefficient'])
  else:assert t['monomial']==[] and F(t['coefficient'])==-1
 row(f'three.det{det}.E157',add(var(e157),scale(mul(R,var(e158)),-1)))
 weights={1:E,4:e4,8:e8,39:e39,79:e79,157:e157,158:e158}
 for j,items in enumerate(groups):eqpair(b+2*j,f'three.det{det}.group{j}',ka((con(1),{}),*(ks(leaves[name],var(weights[w])) for name,w in items)))
 for j in (6,7):coord(b+j,f'three.det{det}.product01.{j-6}')
 eqpair(b+6,f'three.det{det}.product01',km(pair(b),pair(b+2)))
 eqpair(W,f'three.det{det}.W',km(pair(b+6),pair(b+4)))
new['status']='Research326: three-group detector; independent arithmetic review pending.'
new['coordinates'].sort(key=lambda c:c['id']);new['residuals'].sort(key=lambda r:r['id'])
ids={c['id'] for c in new['coordinates']};used={i for r in new['residuals'] for t in r['terms'] for i in t['monomial']}
assert ids==used and len(ids)==326 and len(new['residuals'])==296
total=defaultdict(F)
for r in new['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 den=reduce(lcm,(c.denominator for c in p.values()),1);div=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p={m:c*den/div for m,c in p.items()}
 for m,c in p.items():
  for n,d in p.items():total[tuple(sorted(m+n))]+=c*d
poly={'terms':[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]}
def write(name,data):
 p=H/name;p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ch=write('candidate326-ir.json',new);ph=write('polynomial326.json',poly)
cert={'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'candidateSha256':ch,'polynomialSha256':ph,'removedCoordinates':sorted(drop),'removedRows':sorted(gone),'repurposedCoordinates':sorted(repurpose),'newCoordinates':list(range(835,846)),'variables':326,'witnesses':325,'residuals':296,'monomials':len(poly['terms']),'arithmeticAcceptance':False}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
