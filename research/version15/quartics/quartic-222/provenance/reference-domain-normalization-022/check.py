from fractions import Fraction as Q
import json
import sys
K=lambda a,b=0:(Q(a),Q(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
 n=x[0]*x[0]-2*x[1]*x[1]
 assert n
 return (x[0]/n,-x[1]/n)
def div(x,y): return mul(x,inv(y))
a,b,c,d=K(57,-28),K(8,-14),K(88,-48),K(39,-36)
assert mul(b,b)==mul(K(8),a)
v=div(K(8),a)
assert mul(v,v)[0]==Q(308288,2825761)
assert pow(2,74,149)==148
count=0
for n in range(-20,21):
 f,S,g=K(n+1,n-2),K(2*n-1,n+3),K(n,n+1)
 h,t=inv(g),div(f,g)
 A=add(a,mul(c,f))
 F=add(add(mul(A,g),mul(b,mul(f,S))),mul(d,f))
 E=sub(sub(mul(sub(mul(b,S),d),g),mul(a,f)),K(-8))
 Fn=add(add(A,mul(b,mul(t,S))),mul(d,t))
 En=add(sub(sub(mul(b,S),d),mul(a,t)),mul(K(8),h))
 assert div(F,g)==Fn
 assert div(E,g)==En
 assert mul(f,h)==t
 count+=1
print(json.dumps({'exact_field_identity_samples':count,'constant_checks':'pass','claim':'algebra support, not full-system solutions or independent acceptance'},indent=2))
