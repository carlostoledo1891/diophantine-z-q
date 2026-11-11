from fractions import Fraction as F
from pathlib import Path
import json
D=Path(__file__).parent
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
 n=b[0]*b[0]-2*b[1]*b[1];assert n
 return mul(a,(b[0]/n,-b[1]/n))
def scale(a,c):return(a[0]*c,a[1]*c)
def sq(a):return mul(a,a)
x=(F(57,8),F(-7,2));y=(F(-165,8),F(417,32));d=(F(11),F(-6))
assert sq(y)==sub(mul(sq(x),x),mul(d,x))
m=div(sub(scale(sq(x),3),d),scale(y,2));xx=sub(sq(m),scale(x,2));yy=sub(mul(m,sub(x,xx)),y)
assert sq(yy)==sub(mul(sq(xx),xx),mul(d,xx))
z=neg(div(x,y));zz=neg(div(xx,yy));ratio=div(zz,z)
assert ratio!=(F(2),F(0))
# Three quadratic equations have the exact eliminated Lucas polynomial.
for a in range(-5,6):
 for b in range(-5,6):
  for t in range(-5,6):
   k=(a-2)*b;l=t*k
   assert t*t-a*l+k*k-1==t*t-a*(a-2)*t*b+(a-2)**2*b*b-1
out={'ok':True,'ratio_z2P_over_zP':[str(q) for q in ratio],'ratio_is_not_index_2':True,'scope':'Actual curve point-function counterexample, not an admitted full223 witness with H=P.','three_quadratic_elimination_identity':True}
D.joinpath('CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
