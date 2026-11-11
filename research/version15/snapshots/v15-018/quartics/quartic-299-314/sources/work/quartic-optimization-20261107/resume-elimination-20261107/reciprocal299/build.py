"""Extend reciprocal301 to S auxiliary points, retaining its oriented root chart."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import copy,hashlib,json
HERE=Path(__file__).resolve().parent
SRC=HERE.with_name('reciprocal301')/'candidate301-ir.json'
PIN='ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6'
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
def sq(x):return times(x,x)
def enc(p):return [{'sPower':a,'monomial':list(m),'coefficient':str(c)} for (a,m),c in sorted(p.items())]
D=(c(11),c(-6));one=(c(1),{})
N=(add(c(Q(-87,41)),sc(v(142),-1),sc(v(143),Q(7,2)),sc(v(700),Q(-80,41)),sc(v(701),Q(212,41))),
   add(c(Q(129,164)),sc(v(142),Q(7,4)),sc(v(143),-1),sc(v(700),Q(106,41)),sc(v(701),Q(-80,41))))
a,b,root,f,h,F,s,Y,B,L,z=map(pair,(5,7,84,25,27,118,120,257,202,236,168))
root=pair(84,2);Y=pair(257,2);B=pair(202,2)
diff=plus(f,scale(F,-1));k=plus(times(s,diff),scale(h,-1))
equations={
 708:('S.primaryCurve',plus(sq(h),scale(f,-1),times(D,times(f,Y)))),
 710:('S.dividedDifference',plus(scale(times(s,h),2),scale(times(root,diff),-1),scale(one,-1),times(D,plus(scale(Y,2),times(f,F))))),
 712:('S.rootAbscissa',plus(sq(s),scale(root,-1),times(D,plus(f,F)))),
 714:('S.rootOrientation',plus(times(a,b),scale(times(D,h),-1),times(s,plus(times(D,f),root)))),
 209:('S.primarySquare',plus(sq(f),scale(Y,-1))),
 148:('S.alternateSquare',plus(sq(F),scale(B,-1))),
 188:('S.primaryRaw',plus(times(h,L),times(f,N))),
 120:('S.alternateRegular',plus(times(plus(one,scale(times(D,B),-1)),z),scale(k,-1))),
 2220:('S.primaryRegular',plus(times(plus(one,scale(times(D,Y),-1)),L),times(h,N))),
}
replacement={}
for rid,(name,eq) in equations.items():
 for j in (0,1):replacement[rid+j]={'id':rid+j,'name':name+f'.{j}','kind':'structural','block':'S_reciprocal_oriented','sourceLines':[],'terms':enc(eq[j])}
oldids={r['id'] for r in old['residuals']};added=set(replacement)-oldids
assert added=={2220,2221}
new['residuals']=[replacement.get(r['id'],r) for r in old['residuals']]+[replacement[i] for i in sorted(added)]
new['coordinates']=[c for c in old['coordinates'] if c['id'] not in {122,123}]
renames={i+j:f'S.reciprocal.{name}.{j}' for i,name in [(25,'f'),(27,'h'),(118,'F'),(120,'s')] for j in (0,1)}
for coord in new['coordinates']:
 if coord['id'] in renames:coord['name']=renames[coord['id']]
new['status']='Proposed reciprocal299; S root a,b and all scalar consumers retained with explicit orientation. Independent review required.'
assert len(new['coordinates'])==299 and len(new['residuals'])==279
assert not any({122,123}.intersection(t['monomial']) for r in new['residuals'] for t in r['terms'])
total={}
for r in new['residuals']:
 p={(t['sPower'],tuple(t['monomial'])):Q(t['coefficient']) for t in r['terms']}
 assert max(len(m) for a,m in p)<=2
 den=lcm(*(a.denominator for a in p.values()));nums={m:int(a*den) for m,a in p.items()};g=gcd(*nums.values())
 pp={m:Q(a,g) for m,a in nums.items()};total=add(total,mul(pp,pp))
def write(name,value):
 p=HERE/name;p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ir=write('candidate299-ir.json',new);pol=write('polynomial299.json',{'terms':enc(total)})
cert={'source_sha256':PIN,'candidate_sha256':ir,'polynomial_sha256':pol,'variables':299,'witnesses':298,'residuals':279,'power_entries':len(total),'monomials':len({m for a,m in total}),'deleted_coordinates':[122,123],'repurposed_coordinates':sorted(renames),'changed_rows':sorted(set(replacement)&oldids),'added_rows':sorted(added),'root_orientation':'a*b=D*h-s*(D*f+c)','independently_accepted':False}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
