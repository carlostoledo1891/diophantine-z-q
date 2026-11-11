"""Independent exact replay of the bounded arithmetic at manuscript lines 279-325."""
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path
import json, hashlib

def add(z,w): return z[0]+w[0],z[1]+w[1]
def neg(z): return -z[0],-z[1]
def mul(z,w): return z[0]*w[0]+2*z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def inverse(z):
 norm=z[0]*z[0]-2*z[1]*z[1]
 assert norm
 return z[0]/norm,-z[1]/norm
def div(z,w):return mul(z,inverse(w))
def scale(c,z):return c*z[0],c*z[1]
def power(z,n):
 result=(Q(1),Q(0))
 for _ in range(n):result=mul(result,z)
 return result
def rational_sqrt(x):
 if x<0:return None
 a,b=isqrt(x.numerator),isqrt(x.denominator)
 return Q(a,b) if a*a==x.numerator and b*b==x.denominator else None
def square_root(z):
 u,v=z
 if v==0:
  r=rational_sqrt(u)
  if r is not None:return r,Q(0)
  r=rational_sqrt(u/2)
  return (Q(0),r) if r is not None else None
 norm=rational_sqrt(u*u-2*v*v)
 if norm is None:return None
 for t in {norm,-norm}:
  r=rational_sqrt((u+t)/2)
  if r not in (None,0):
   result=r,v/(2*r)
   if mul(result,result)==z:return result
 return None

delta=Q(3),Q(-1)
delta2=mul(delta,delta)
def rhs(x):return add(mul(mul(x,x),x),neg(mul(delta2,x)))
def display(z):return [str(t) for t in z]

counts=[]
for p,s in [(17,6),(23,5)]:
 assert (s*s-2)%p==0
 d=(75-53*s)%p;disc=(64*pow(d,6,p))%p
 assert disc
 points=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x+d*d*x)%p==0]
 character_count=1+sum(1+(0 if (f:=(x*x*x-d*d*x)%p)==0 else (1 if pow(f,(p-1)//2,p)==1 else -1)) for x in range(p))
 assert len(points)+1==character_count
 counts.append(dict(prime=p,s=s,d=d,discriminant_mod_prime=disc,points_including_identity=len(points)+1,affine_points=points))
assert [r['points_including_identity'] for r in counts]==[20,24]

quadratics=[];roots=set()
for a in range(1,82):
 for b in range(-162,163):
  for k in range(1,163):
   num=b*b-2*k*k
   if num%(4*a):continue
   c=num//(4*a)
   if abs(c)>81 or gcd(gcd(a,abs(b)),abs(c))!=1:continue
   quadratics.append((a,b,c,k))
   roots.add((Q(-b,2*a),Q(k,2*a)))
   roots.add((Q(-b,2*a),Q(-k,2*a)))
rationals={(Q(a,b),Q(0)) for a in range(-9,10) for b in range(1,10) if gcd(abs(a),b)==1}
survivors=[]
for x in sorted(roots|rationals):
 y=square_root(rhs(x))
 if y is not None:
  assert mul(y,y)==rhs(x)
  survivors.append(dict(x=display(x),one_y=display(y)))
expected={(Q(0),Q(0)),delta,neg(delta),(Q(1),Q(1)),(Q(23),Q(-17)),(Q(2),Q(4)),(Q(5,2),Q(-2))}
actual={tuple(Q(t) for t in row['x']) for row in survivors}
assert len(quadratics)==7004,(len(quadratics),'quadratics')
assert len(roots)==14008,(len(roots),'roots')
assert len(rationals)==111,(len(rationals),'rationals')
assert actual==expected,dict(extra=list(actual-expected),missing=list(expected-actual))
assert 41**3*676*392**36<9**108
R=(Q(1),Q(1)),(Q(0),Q(2))
slope=div(add(scale(3,power(R[0],2)),neg(delta2)),scale(2,R[1]))
double_x=add(power(slope,2),neg(scale(2,R[0])))
double_y=add(mul(slope,add(R[0],neg(double_x))),neg(R[1]))
assert double_x==(Q(57,8),Q(-7,2))
translations={R[0]}
for e in [(Q(0),Q(0)),delta,neg(delta)]:
 slope=div(R[1],add(R[0],neg(e)))
 translations.add(add(add(power(slope,2),neg(R[0])),neg(e)))
assert translations==expected-{(Q(0),Q(0)),delta,neg(delta)}
epsilon=Q(1),Q(1);d=Q(75),Q(-53)
assert mul(power(epsilon,4),d)==delta
assert div(double_x,power(epsilon,4))==(Q(1641,8),Q(-145,1))
assert div(double_y,power(epsilon,6))==(Q(-15465,4),Q(87483,32))
report=dict(status='PASS',arithmetic='Python integers and Fraction; no floating point',
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 reductions=counts,primitive_quadratics=len(quadratics),quadratic_roots=len(roots),
 rational_candidates=len(rationals),survivors=survivors,
 double_R=dict(x=display(double_x),y=display(double_y)),
 torsion_translate_abscissas_match=True,coordinate_change_to_P0=True,
 height_integer_inequality=True,
 limitation='Verifies finite counts, square tests and one integer inequality; does not prove the duplication height inequalities or two-isogeny descent.')
(Path(__file__).parent/'generator-arithmetic.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='reductions'},indent=2))
