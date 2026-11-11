"""Producer-free row, valuation-residue, witness-inventory and complete SOS check."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent
src=H.parent/'chain327/candidate327-ir.json'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665'
old=json.loads(src.read_bytes());new=json.loads((H/'candidate326-ir.json').read_bytes())
F=Fraction
def plus(*ps):
 d=defaultdict(F)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def times(p,q):
 d=defaultdict(F)
 for a,b in p.items():
  for c,e in q.items():d[tuple(sorted(a+c))]+=b*e
 return {m:c for m,c in d.items() if c}
def scalar(p,c):return {m:v*F(c) for m,v in p.items() if v*c}
def affine(d):return {(i,) if i is not None else ():F(v) for i,v in d.items() if v}
def x(i):return affine({i:1})
def kp(i,f=1):return (x(i),affine({i+1:f}))
def prod(a,b):return (plus(times(a[0],b[0]),scalar(times(a[1],b[1]),2)),plus(times(a[0],b[1]),times(a[1],b[0])))
def read(r):
 assert all(t['sPower']==0 for t in r['terms'])
 return {tuple(t['monomial']):F(t['coefficient']) for t in r['terms']}
nr={r['name']:r for r in new['residuals']};expected={}
def equal(name,i,value):
 for j in range(2):expected[name+'.'+str(j)]=plus(x(i+j),scalar(value[j],-1))
def cached(a):return (affine({a:F(72097,5764801),a+1:F(101904,5764801)}),affine({a:F(-50952,5764801),a+1:F(-72097,5764801)}))
roots={'H1':kp(313,2),'H2':kp(315,2),'H3':kp(317,2),
       'H4':(affine({None:1,253:-2,319:1}),affine({320:4,254:-4})),
       'M0':kp(305,2),'M1':(affine({307:1,232:-6,0:1224,248:1224,None:15321}),affine({308:2,233:-6})),
       'P2':kp(257,2),'P3':kp(259,2),'P4':kp(261,2)}
positions={'H1':826,'H2':820,'H3':822,'H4':835,'M0':837,'M1':839,'P2':828,'P3':830,'P4':841}
for name,root in roots.items():equal('three.shared.'+name,positions[name],prod(root,root))
values={name:kp(i) for name,i in positions.items()}
values.update({'H0':kp(311,2),'P1':kp(255,2),'T0':cached(182),'T2':cached(200),'T3':cached(212),'T4':cached(224),
 'Z1':(affine({192:F(37249,2401),193:F(-34848,2401)}),affine({192:F(-25476,2401),193:F(25476,2401)}))})
# Each tuple is leaf, exponent, power of the underlying f/test, valuation step,
# required depth and depth supplied by the ORIGINAL Pi^19 completeness.
groups=[ [('H1',158,4,1,40,40),('H4',157,4,1,40,40),('M0',39,4,1,10,12),('T0',8,8,2,2,2),('T4',4,8,2,2,2)],
 [('H2',158,4,1,40,40),('H0',79,2,2,40,40),('T2',8,8,2,2,2),('Z1',4,4,2,2,2),('P1',1,2,2,2,40)],
 [('H3',158,4,1,40,40),('M1',39,4,1,10,80),('T3',8,8,2,2,2),('P2',157,4,2,2,40),('P3',4,4,2,2,40),('P4',1,4,2,2,40)] ]
assert {t[0] for g in groups for t in g}==set(values)
valuation=[]
for g in groups:
 occupied={0}
 for name,w,power,step,required,complete in g:
  residues={v for v in range(16) if (v+w)%(power*step)==0}
  assert residues and not residues.intersection(occupied)
  occupied|=residues
  inferred=step*((w+power*step-1)//(power*step))
  assert inferred>=required and power*complete-w>0
  valuation.append({'leaf':name,'residues':sorted(residues),'inferredDepth':inferred,'completenessMargin':power*complete-w})
for det,b,E,e4,e8,e39,e79,e158,W in ((0,634,350,832,356,369,360,374,380),(1,654,398,833,404,417,408,422,428),(2,674,446,834,452,465,456,470,476)):
 name=f'three.det{det}';weights={1:E,4:e4,8:e8,39:e39,79:e79,157:843+det,158:e158}
 er=read(next(r for r in old['residuals'] if r['name']==f'detector{det}.eWeight.definition'))
 assert er.pop(())==-1
 R={}
 for m,c in er.items():
  a=list(m);assert E in a;a.remove(E);R[tuple(a)]=c
 expected[name+'.E157']=plus(x(843+det),scalar(times(R,x(e158)),-1))
 for k,g in enumerate(groups):
  value=tuple(plus(affine({None:1}) if j==0 else {},*(times(values[t[0]][j],x(weights[t[1]])) for t in g)) for j in range(2))
  equal(name+f'.group{k}',b+2*k,value)
 equal(name+'.product01',b+6,prod(kp(b),kp(b+2)))
 equal(name+'.W',W,prod(kp(b+6),kp(b+4)))
assert len(expected)==51
for name,p in expected.items():assert read(nr[name])==p,name
gone={r['id'] for r in old['residuals'] if r['name'].startswith(('four.high','four.primary')) or (r['name'].startswith('four.det') and not r['name'].endswith('.E4'))}
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
assert set(o)-set(n)==gone
assert {r['name'] for i,r in n.items() if i not in o}==set(expected)
assert all(n[i]==r for i,r in o.items() if i not in gone)
drop={b+j for b in (634,654,674) for j in range(8,12)}
repurpose={826,827}|{b+j for b in (634,654,674) for j in (6,7)}
assert all(r['id'] in gone for r in old['residuals'] if any((drop|repurpose).intersection(t['monomial']) for t in r['terms']))
assert all(r['name'] in expected for r in new['residuals'] if any(repurpose.intersection(t['monomial']) for t in r['terms']))
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert set(oc)-set(nc)==drop and set(nc)-set(oc)==set(range(835,846))
renamed={820,821,822,823,826,827,828,829,830,831}|repurpose
for i in set(oc)&set(nc):
 c=dict(oc[i])
 if i in renamed:c['name']=nc[i]['name']
 assert c==nc[i]
assert len(nc)==326 and len(n)==296
assert {i for r in n.values() for t in r['terms'] for i in t['monomial']}==set(nc)
total=defaultdict(int)
for r in n.values():
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']};den=1;div=0
 for c in p.values():den=lcm(den,c.denominator)
 for c in p.values():div=gcd(div,abs(int(c*den)))
 entries=sorted((m,int(c*den)//div) for m,c in p.items())
 for i,(m,c) in enumerate(entries):
  for j in range(i,len(entries)):
   k,d=entries[j];total[tuple(sorted(m+k))]+=c*d*(1 if i==j else 2)
actual={tuple([-1]*t['sPower']+t['monomial']):int(t['coefficient']) for t in json.loads((H/'polynomial326.json').read_bytes())['terms']}
assert {m:c for m,c in total.items() if c}==actual
content=0
for c in actual.values():content=gcd(content,abs(c))
assert content==1 and max(len(m) for m in actual if -1 not in m)==4
result={'candidateSha256':hashlib.sha256((H/'candidate326-ir.json').read_bytes()).hexdigest(),'variables':326,'witnesses':325,'rows':296,'monomials':len(actual),'fullSOS':True,'allRowsAndConsumers':True,'valuationChecks':valuation,'arithmeticAcceptance':False}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='valuationChecks'},indent=2))
