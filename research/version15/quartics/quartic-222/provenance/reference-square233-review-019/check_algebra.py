import json
from fractions import Fraction
from pathlib import Path

# Independent exact coefficient algebra over Q(sqrt(2))[f,S,g,v].
def kmul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(*polys):
 out={}
 for p in polys:
  for m,c in p.items():
   z=out.get(m,(0,0));out[m]=(z[0]+c[0],z[1]+c[1])
 return {m:c for m,c in out.items() if c!=(0,0)}
def neg(p): return {m:(-c[0],-c[1]) for m,c in p.items()}
def mul(p,q):
 out={}
 for m,a in p.items():
  for n,b in q.items():
   k=tuple(x+y for x,y in zip(m,n));c=kmul(a,b);z=out.get(k,(0,0));out[k]=(z[0]+c[0],z[1]+c[1])
 return {m:c for m,c in out.items() if c!=(0,0)}
def const(a,b=0):return {(0,0,0,0):(a,b)} if a or b else {}
def var(i):
 m=[0]*4;m[i]=1;return {tuple(m):(1,0)}
f,S,g,v=[var(i) for i in range(4)]
a,b,c,d,D=[const(*z) for z in [(57,-28),(8,-14),(88,-48),(39,-36),(11,-6)]]
one=const(1)
A=add(a,mul(c,f));T=add(mul(A,g),mul(d,f))
F=add(T,mul(mul(b,f),S))
Q=add(mul(A,v),mul(const(2),mul(d,g)),mul(a,f),const(-8))
G=add(mul(g,g),neg(mul(f,v)))
H=add(mul(f,mul(S,S)),const(-1),mul(D,mul(f,f)))
E=add(mul(b,mul(S,g)),neg(mul(d,g)),neg(mul(a,f)),const(8))
R=add(mul(A,v),mul(b,mul(S,g)),mul(d,g))
assert add(mul(F,g),neg(mul(A,G)),neg(mul(f,R)))=={}
assert add(E,neg(R),Q)=={}
assert add(mul(F,add(mul(b,S),neg(d))),neg(mul(A,E)),neg(mul(mul(b,b),H)))=={}
assert {m:c for m,c in E.items() if m[0]==0 and m[2]==0}==const(8)
NN=add(const(8),neg(mul(a,f)),neg(mul(const(2),mul(d,g))))
assert add(mul(A,mul(g,g)),neg(mul(f,NN)),neg(mul(F,g)),mul(f,E))=={}
AA=add(mul(a,a),mul(const(2),mul(mul(a,c),f)),mul(mul(c,c),mul(f,f)))
assert add(AA,neg(mul(A,A)))=={}
identity=add(mul(mul(b,b),mul(f,H)),neg(mul(f,mul(A,Q))),neg(mul(mul(A,A),G)),mul(F,add(T,neg(mul(b,mul(f,S))))))
assert identity=={},identity
assert add(mul(b,b),neg(mul(const(8),a)))=={}
assert add(mul(a,c),neg(mul(mul(b,b),D)))=={}
assert add(mul(d,d),neg(mul(a,a)),mul(const(8),c))=={}
norm=Fraction(57**2-2*28**2,88**2-2*48**2)
assert norm==Fraction(41,56)**2
assert norm.numerator%149 and norm.denominator%149
result={'identity_zero':True,'constant_identities':3,'new_E_identities':2,'reference_square_identities':2,'f_zero_g_zero_contradiction':8,'exception_norm':str(norm),'exception_norm_v149':0,'division_needed_233_to_235':['a+c*f after the scalar149 exclusion'],'division_not_needed_233_to_235':['S','g','w','N','A0','A1'],'curve_recovery_divides_by_no_variable':True,'prime149':all(149%d for d in range(2,13)),'two_is_nonsquare_mod149':all((i*i)%149!=2 for i in range(149)),'status':'exact local algebra only; full candidate remains pending'}
Path(__file__).with_name('ALGEBRA-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
