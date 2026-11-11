from fractions import Fraction as F
import json
from pathlib import Path

def q(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def div(x,y):
 n=y[0]*y[0]-2*y[1]*y[1]
 assert n
 return mul(x,(y[0]/n,-y[1]/n))
def square(x):return mul(x,x)
lam=q(3,2); l2=square(lam); l3=mul(l2,lam)
d0=q(75,-53); d=q(3,-1); D=q(11,-6)
p0=(q(F(1641,8),-145),q(F(-123720,32),F(87483,32)))
p=(q(F(57,8),F(-28,8)),q(F(-660,32),F(417,32)))
r=(q(1,1),q(0,2))
a=q(-1,F(7,4)); b=q(F(39,8),F(-9,2))
slope=div(sub(mul(q(3),square(r[0])),D),mul(q(2),r[1]))
x2=sub(square(slope),mul(q(2),r[0])); y2=sub(mul(slope,sub(r[0],x2)),r[1])
checks={
 'unit_norm':lam[0]**2-2*lam[1]**2==1,
 'lambda_square':l2==q(17,12),
 'lambda_cube':l3==q(99,70),
 'normalized_d':mul(l2,d0)==d,
 'normalized_D':square(d)==D,
 'P_x_transport':mul(l2,p0[0])==p[0],
 'P_y_transport':mul(l3,p0[1])==p[1],
 'R0_on_curve':square(r[1])==sub(mul(square(r[0]),r[0]),mul(D,r[0])),
 'tangent_slope':slope==q(3,F(-1,4)),
 'double_R0':(x2,y2)==p,
 'current_c_star':square(a)==p[0],
 'current_y_star':mul(a,b)==p[1],
 'current_b_relation':square(b)==sub(square(square(a)),D)
}
assert all(checks.values()),checks
out={'arithmetic':'exact Fraction arithmetic in Q[rho]/(rho^2-2)','checks':checks}
Path(__file__).with_name('ARITHMETIC.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
