from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd
import json, pathlib
ROOT=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/')
C=ROOT/'global/resume-20261110/shared-alternate-226-001'
P=ROOT/'resume-20261110/scalar-contact-quartic-001/candidate232-ir.json'
old=json.loads(P.read_text()); new=json.loads((C/'candidate226-ir.json').read_text()); pub=json.loads((C/'candidate226-polynomial.json').read_text())
def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for k,v in p.items(): d[k]+=v
 return clean(d)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
 d=defaultdict(F)
 for (a,m),v in p.items():
  for (b,n),w in q.items(): d[a+b,tuple(sorted(m+n))]+=v*w
 return clean(d)
def atom(i):return {(0,(i,)):F(1)}
def const(c):return {(0,()):F(c)} if c else {}
def terms(ts):
 d=defaultdict(F)
 for t in ts:d[t['parameterPower'],tuple(t['monomial'])]+=F(t['coefficient'])
 return clean(d)
def fa(x,y):return (add(x[0],y[0]),add(x[1],y[1]))
def fm(x,y):return (add(mul(x[0],y[0]),scale(mul(x[1],y[1]),2)),add(mul(x[0],y[1]),mul(x[1],y[0])))
def fc(a,b=0):return (const(a),const(b))
def fp(a,b):return (atom(a),atom(b))
def neg(x):return tuple(scale(z,-1) for z in x)
def remap(p):return {(a,tuple(sorted(i if i<21 else i-8 for i in m))):v for (a,m),v in p.items()}

C=ROOT/'global/resume-20261110/shared-T-elimination224-004'
par=json.loads((C.parent/'shared-alternate-226-001/candidate226-ir.json').read_text()); cand=json.loads((C/'candidate224-ir.json').read_text()); rr={r['id']:terms(r['terms']) for r in par['residuals']}
rels=next(r for r in json.loads((C/'FIELD-RELATIONS.json').read_text()) if r['dropped']=='g')['relations']
fields=[fp(17,18),fp(19,20),fp(126,127),(atom(74),scale(atom(75),2)),(atom(21),scale(atom(22),2)),(add(scale(atom(23),F(37249,2401)),scale(atom(24),F(-34848,2401))),scale(add(atom(23),scale(atom(24),-1)),F(25476,2401))),fp(225,226)]
def expand(rel):
 r=fc(0)
 for t in rel:
  z=fc(*map(F,t['coefficient']))
  for i in t['monomial']:z=fm(z,fields[i])
  r=fa(r,z)
 return r
bd=expand(rels[0]);wd=expand(rels[4]);assert bd==(rr[26],scale(rr[27],2))
assert wd==(add(scale(rr[7],F(193,2401)),scale(rr[8],F(-1056,2401))),add(scale(rr[7],F(132,2401)),scale(rr[8],F(-772,2401))))
assert 193*(-772)-(-1056)*132 !=0
Ff,S,G,B,w,W,T=fields
a,b,c,d=fc(57,-28),fc(8,-14),fc(88,-48),fc(39,-36)
oldF=fa(fa(fm(fa(a,fm(c,Ff)),G),fm(b,fm(Ff,S))),fm(d,Ff))
oldE=fa(fa(fa(fm(b,fm(S,G)),neg(fm(d,G))),neg(fm(a,Ff))),fc(8))
NN=fa(fa(fc(8),neg(fm(a,Ff))),neg(fm(fc(2),fm(d,G))))
AA=fa(fa(fm(a,a),fm(fc(2),fm(fm(a,c),Ff))),fm(fm(c,c),B))
oldW=fa(fm(AA,w),neg(fm(NN,NN)))
assert oldF==(rr[3],rr[4]) and oldE==(rr[5],rr[6]) and oldW==(rr[1],scale(rr[2],2))
removed={1,2,3,4,5,6,199,200}; deleted={126,127}
assert {r['id'] for r in par['residuals'] if any(deleted.intersection(t['monomial']) for t in r['terms'])}==removed
def compact(p):return {(a,tuple(i-2 if i>127 else i for i in m)):v for (a,m),v in p.items()}
expected=[compact(rr[i]) for i in sorted(rr) if i not in removed]
from math import lcm
for ix in [1,2,3,5]:
 for p in expand(rels[ix]):
  den=lcm(*(v.denominator for v in p.values())); gg=reduce(gcd,(abs(int(v*den)) for v in p.values()));expected.append(compact(scale(p,F(den,gg))))
assert expected==[terms(r['terms']) for r in cand['residuals']]
poly=add(*(mul(p,p) for p in expected)); assert poly==terms(json.loads((C/'candidate224-polynomial.json').read_text())['terms'])
assert set(i for p in expected for a,m in p for i in m)==set(range(1,225))
assert cand['inputCoordinate']==par['inputCoordinate']==1 and cand['fixedParameter']==par['fixedParameter']
assert max(len(m) for a,m in poly)==4 and reduce(gcd,(abs(v.numerator) for v in poly.values()))==1
assert max(abs(v) for (a,m),v in poly.items() if a==0)<149**214
assert max(abs(v) for (a,m),v in poly.items() if a==1)==44402
assert {(a,m):v for (a,m),v in poly.items() if a==2}=={(2,(114,114)):1} and poly[0,(114,114)]==1
print(json.dumps({'status':'pass','rows':200,'unchanged_rows':192,'new_field_relations':4,'variables':224,'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':4,'content':1,'height':'A_N^2+1 for N>=53; defining threshold remains ineffective','deleted_coordinate_consumers':sorted(removed)},indent=2))
