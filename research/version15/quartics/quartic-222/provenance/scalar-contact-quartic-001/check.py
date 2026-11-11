import json,math,hashlib
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent;ROOT=O.parents[3]
old=json.loads((ROOT/'work/quartic238-optimization-20261110/linear-lucas/reference233-014/candidate233-ir.json').read_bytes());new=json.loads((O/'candidate232-ir.json').read_bytes())
def compact(i):return i-(i>122)
oldkept=[r for r in old['residuals'] if r['id'] not in (71,72)]
newkept=[r for r in new['residuals'] if r['name']!='scalar.four_contact_product.definition']
assert len(oldkept)==len(newkept)==205
for a,b in zip(oldkept,newkept):assert [dict(t,monomial=[compact(i) for i in t['monomial']]) for t in a['terms']]==b['terms']
assert old['inputCoordinate']==new['inputCoordinate']==1 and old['fixedParameter']==new['fixedParameter']
def val(x,p):
 x=F(x);assert x
 n,d=x.numerator,x.denominator;v=0
 while n%p==0:n//=p;v+=1
 while d%p==0:d//=p;v-=1
 return v
def r4(x):
 beta=2504+51*x*x
 return beta*(beta-1)*(beta-2401)*(32*beta+343)
def R(x,N):
 r=r4(x);return F(149**(2*N+1)*r,1+149**2*r)
# Polynomial identity: both sides have degree<=4 in t, so 5 exact t values establish equality.
for t in range(5):
 beta=2504+51*t;u=F((51*t+2501)**2,4)
 represented=512*u*u-767410608*u-15531948*t*u-291790992*t-14315517724
 assert represented==beta*(beta-1)*(beta-2401)*(32*beta+343)
for x in range(-256,257):
 q=R(x,1)
 assert val(q,2) in (2,3) and val(q,3)==0 and val(q,17)==0
 assert val(F(9792,q),2)>=3 and val(F(9792,q),3)==2 and val(F(9792,q),17)==1
 d=(q*(q+9792)).denominator;assert math.isqrt(d)**2==d
for x in range(149):assert val(r4(x),149)==0
for N in (1,2,3):
 for e in range(1,5):
  for k in (1,2,7,148):assert val(R(F(k,149**e),N),149)==2*N-1
 for k in range(149):assert val(R(k,N),149)==2*N+1
poly={}
for r in new['residuals']:
 ts=r['terms']
 for i,a in enumerate(ts):
  for j in range(i,len(ts)):
   b=ts[j];key=(a['parameterPower']+b['parameterPower'],tuple(sorted(a['monomial']+b['monomial'])))
   poly[key]=poly.get(key,0)+int(a['coefficient'])*int(b['coefficient'])*(1 if i==j else 2)
poly={k:v for k,v in poly.items() if v}
saved=json.loads((O/'candidate232-polynomial.json').read_bytes());assert poly=={(t['parameterPower'],tuple(t['monomial'])):int(t['coefficient']) for t in saved['terms']}
assert len({i for a,m in poly for i in m})==232 and max(len(m) for a,m in poly)==4 and math.gcd(*poly.values())==1
report={'status':'PASS','unchanged_rows':205,'polynomial_identity':'degree<=4 checked at5 exact distinct values','integer_preparation_samples':513,'all149_residue_classes_checked':True,'nonintegral149_cases':48,'full_unordered_sos_matches':True,'variables':232,'rows':206,'coordinate_monomials':len({m for a,m in poly}),'finite_tests_do_not_replace_arithmetic_proof':True}
(O/'CHECKS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
