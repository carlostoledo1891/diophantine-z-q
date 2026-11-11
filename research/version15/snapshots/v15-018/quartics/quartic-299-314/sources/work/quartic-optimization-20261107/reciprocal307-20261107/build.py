"""Build the A/T/Z reciprocal-slope candidate from frozen anchor-gamma313."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
from functools import reduce
import json,hashlib,copy
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
SOURCE=ROOT/'work/quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json'
PIN='6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
old=json.loads(SOURCE.read_bytes());new=copy.deepcopy(old)
def add(*ps):
 o=defaultdict(F)
 for p in ps:
  for m,c in p.items():o[m]+=c
 return {m:c for m,c in o.items() if c}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
 o=defaultdict(F)
 for (a,m),c in p.items():
  for (b,n),d in q.items():o[(a+b,tuple(sorted(m+n)))]+=c*d
 return {m:c for m,c in o.items() if c}
def v(i,c=1):return {(0,(i,)):F(c)}
def const(c):return {(0,()):F(c)} if c else {}
def pair(i,k=1):return v(i),v(i+1,k)
def fa(*xs):return add(*(x[0] for x in xs)),add(*(x[1] for x in xs))
def fs(x,c):return scale(x[0],c),scale(x[1],c)
def fm(x,y):return add(mul(x[0],y[0]),scale(mul(x[1],y[1]),2)),add(mul(x[0],y[1]),mul(x[1],y[0]))
def sq(x):return fm(x,x)
def encode(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items())]
D=(const(11),const(-6));one=(const(1),{})
H=(add(const(F(-87,41)),v(142,-1),v(143,F(7,2)),v(700,F(-80,41)),v(701,F(212,41))),
 add(const(F(129,164)),v(142,F(7,4)),v(143,-1),v(700,F(106,41)),v(701,F(-80,41))))
specs=[('A',1,82,21,110,112,114,255,190,232,164,2,700,116,142,207,184),
       ('T',9,86,29,126,128,130,259,208,240,172,18,716,124,160,211,192),
       ('Z',13,88,33,134,136,138,261,220,244,176,26,724,128,172,213,196)]
replacement={};renames={};added=[];deleted=set();maps=[]
def put(rid,name,eq,extra=False):
 for h in range(2):
  record={'id':rid+h,'name':name+f'.{h}','kind':'structural','block':'reciprocal_slope_points','sourceLines':[], 'terms':encode(eq[h])}
  assert rid+h not in replacement
  replacement[rid+h]=record
  if extra:added.append(rid+h)
for j,spec in enumerate(specs):
 name,a0,c0,f0,F0,s0,k0,Y0,B0,L0,z0,rootrow,chartrow,zrow,Brow,Yrow,Lrow=spec
 f,h,Fv,sv,kv,L,z=map(pair,[f0,f0+2,F0,s0,k0,L0,z0])
 Y,B=pair(Y0,2),pair(B0,2)
 c=pair(c0,2)
 if name=='T':c=(v(c0,2),v(c0+1,2))
 put(rootrow,name+'.reciprocal.primaryCurve',fa(sq(h),fs(f,-1),fm(D,fm(f,Y))))
 put(chartrow,name+'.reciprocal.alternateCurve',fa(sq(kv),fs(Fv,-1),fm(D,fm(Fv,B))))
 put(chartrow+2,name+'.slope.secant',fa(fm(sv,fa(f,fs(Fv,-1))),fs(h,-1),fs(kv,-1)))
 put(chartrow+4,name+'.slope.dividedDifference',fa(fm(sv,fa(h,fs(kv,-1))),fs(one,-1),fm(D,fa(Y,fm(f,Fv),B))))
 put(chartrow+6,name+'.slope.rootAbscissa',fa(sq(sv),fs(c,-1),fm(D,fa(f,Fv))))
 put(Yrow,name+'.reciprocal.primarySquare',fa(sq(f),fs(Y,-1)))
 put(Brow,name+'.reciprocal.alternateSquare',fa(sq(Fv),fs(B,-1)))
 put(Lrow,name+'.ratio.primaryRaw',fa(fm(h,L),fm(f,H)))
 put(zrow,name+'.ratio.alternateRaw',fa(fm(kv,z),fs(Fv,-1)))
 put(2200+4*j,name+'.ratio.primaryRegular',fa(fm(fa(one,fs(fm(D,Y),-1)),L),fm(h,H)),True)
 put(2202+4*j,name+'.ratio.alternateRegular',fa(fm(fa(one,fs(fm(D,B),-1)),z),fs(kv,-1)),True)
 for base,meaning in [(f0,'primary.f'),(f0+2,'primary.h'),(F0,'alternate.f'),(s0,'slope'),(k0,'alternate.h')]:
  for hcomp in range(2):renames[base+hcomp]=name+'.reciprocal.'+meaning+f'.{hcomp}'
 deleted.update([a0+2,a0+3]);maps.append({'root':name,'a':a0,'c':c0,'f':f0,'h':f0+2,'F':F0,'s':s0,'k':k0,'Y':Y0,'Yalt':B0,'L':L0,'z':z0})
oldids={r['id'] for r in old['residuals']}
assert set(added).isdisjoint(oldids)
new['residuals']=[replacement.get(r['id'],r) for r in old['residuals']]+[replacement[i] for i in added]
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in deleted]
for c in new['coordinates']:
 if c['id'] in renames:c['name']=renames[c['id']]
new['status']='Proposed reciprocal-slope307; new auxiliary E(K) domain argument and independent review required.'
assert len(new['coordinates'])==307 and len(new['residuals'])==295
assert all(not deleted.intersection(t['monomial']) for r in new['residuals'] for t in r['terms'])
def decode(r):return {(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
total={};active=set()
for r in new['residuals']:
 p=decode(r);assert max(len(m) for s,m in p)<=2
 active.update(i for s,m in p for i in m)
 den=reduce(lcm,(c.denominator for c in p.values()),1)
 ints={m:int(c*den) for m,c in p.items()};g=reduce(gcd,map(abs,ints.values()))
 primitive={m:F(c,g) for m,c in ints.items()}
 total=add(total,mul(primitive,primitive))
assert active=={c['id'] for c in new['coordinates']}
def write(name,value):
 p=HERE/name;p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ir=write('candidate307-ir.json',new);poly=write('polynomial307.json',{'terms':encode(total)})
certificate={'source':str(SOURCE.relative_to(ROOT)),'source_sha256':PIN,'candidate_sha256':ir,'polynomial_sha256':poly,
 'deleted_coordinates':sorted(deleted),'repurposed_coordinates':sorted(renames),'changed_old_rows':sorted(set(replacement)&oldids),
 'added_rows':added,'coordinate_maps':maps,'variables':307,'witnesses':306,'residuals':295,
 'coefficient_power_entries':len(total),'specialized_monomials':len({m for s,m in total}),
 'status':'Proposed; producer output is not independent acceptance.'}
write('CERTIFICATE.json',certificate)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
print(json.dumps(certificate,indent=2))
