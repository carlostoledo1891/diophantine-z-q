"""Exact alternate-ordinate elimination from independently accepted reciprocal307."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import copy,hashlib,json
HERE=Path(__file__).resolve().parent
OPT=HERE.parent.parent
SRC=OPT/'reciprocal307-20261107/candidate307-ir.json'
PIN='0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==PIN
old=json.loads(SRC.read_bytes());new=copy.deepcopy(old)
def add(*ps):
 d=defaultdict(Q)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def mul(p,q):
 d=defaultdict(Q)
 for (a,m),c in p.items():
  for (b,n),e in q.items():d[a+b,tuple(sorted(m+n))]+=c*e
 return {m:c for m,c in d.items() if c}
def sc(p,c):return {m:c*a for m,a in p.items() if c*a}
def v(i):return {(0,(i,)):Q(1)}
def c(x):return {(0,()):Q(x)} if x else {}
def pair(i,im=1,re=1):return sc(v(i),re),sc(v(i+1),im)
def plus(*xs):return add(*(x[0] for x in xs)),add(*(x[1] for x in xs))
def times(x,y):return add(mul(x[0],y[0]),sc(mul(x[1],y[1]),2)),add(mul(x[0],y[1]),mul(x[1],y[0]))
def scale(x,a):return sc(x[0],a),sc(x[1],a)
def enc(p):return [{'sPower':a,'monomial':list(m),'coefficient':str(c)} for (a,m),c in sorted(p.items())]
D=(c(11),c(-6));one=(c(1),{})
specs=[('A',82,1,21,110,112,114,255,190,164,700,116,2202),
       ('T',86,2,29,126,128,130,259,208,172,716,124,2206),
       ('Z',88,1,33,134,136,138,261,220,176,724,128,2210)]
removed_rows=set();removed_vars=set();replacement={};maps=[]
for name,ci,cr,fi,Fi,si,ki,Yi,Bi,zi,chart,zraw,zreg in specs:
 f,h,F,s,Y,B,z=map(pair,(fi,fi+2,Fi,si,Yi,Bi,zi))
 Y=pair(Yi,2);B=pair(Bi,2);root=pair(ci,2,cr)
 diff=plus(f,scale(F,-1))
 krec=plus(times(s,diff),scale(h,-1))
 q=plus(scale(times(s,h),2),scale(times(root,diff),-1),scale(one,-1),times(D,plus(scale(Y,2),times(f,F))))
 reg=plus(times(plus(one,scale(times(D,B),-1)),z),scale(krec,-1))
 for rid,title,expr in ((chart+4,'eliminatedOrdinate.dividedDifference',q),(zreg,'eliminatedOrdinate.alternateRegular',reg)):
  for j in (0,1):replacement[rid+j]={'id':rid+j,'name':name+'.'+title+f'.{j}','kind':'structural','block':'reciprocal_ordinate_elimination','sourceLines':[],'terms':enc(expr[j])}
 removed_rows.update((chart,chart+1,chart+2,chart+3,zraw,zraw+1))
 removed_vars.update((ki,ki+1))
 maps.append({'root':name,'deleted_k':ki,'f':fi,'F':Fi,'h':fi+2,'s':si,'reconstruction':'k=s*(f-F)-h','raw_restoration':'(1-D*B)!=0 from inherited low tests; regular and curve give k*z=F'})
new['coordinates']=[x for x in new['coordinates'] if x['id'] not in removed_vars]
new['residuals']=[replacement.get(r['id'],r) for r in new['residuals'] if r['id'] not in removed_rows]
new['status']='Proposed reciprocal301; inherited low-test exclusion restores removed raw ratios. Independent review required.'
assert len(new['coordinates'])==301 and len(new['residuals'])==277
assert not any(removed_vars.intersection(t['monomial']) for r in new['residuals'] for t in r['terms'])
total={}
for r in new['residuals']:
 p={(t['sPower'],tuple(t['monomial'])):Q(t['coefficient']) for t in r['terms']}
 assert max(len(m) for a,m in p)<=2
 den=lcm(*(a.denominator for a in p.values()));nums={m:int(a*den) for m,a in p.items()};g=gcd(*nums.values())
 primitive={m:Q(a,g) for m,a in nums.items()}
 total=add(total,mul(primitive,primitive))
def write(name,value):
 p=HERE/name;p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ir=write('candidate301-ir.json',new);pol=write('polynomial301.json',{'terms':enc(total)})
cert={'source_sha256':PIN,'candidate_sha256':ir,'polynomial_sha256':pol,'variables':301,'witnesses':300,'residuals':277,
      'power_entries':len(total),'monomials':len({m for a,m in total}),'deleted_coordinates':sorted(removed_vars),
      'deleted_rows':sorted(removed_rows),'changed_rows':sorted(replacement),'maps':maps,'independently_accepted':False}
write('CERTIFICATE.json',cert)
print(json.dumps(cert,indent=2))
