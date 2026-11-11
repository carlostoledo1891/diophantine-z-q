from fractions import Fraction as F
import json,pathlib
P=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-elimination224-004/FIELD-RELATIONS.json')
rels=next(x for x in json.loads(P.read_text()) if x['dropped']=='g')['relations']
def k(a=0,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def mul(x,y):return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def inv(x):
 n=x[0]**2-2*x[1]**2
 assert n
 return x[0]/n,-x[1]/n

# Independent polynomial arithmetic, keys are sorted variable-index tuples.
def pa(*ps):
 out={}
 for p in ps:
  for m,c in p.items():out[m]=add(out.get(m,k()),c)
 return {m:c for m,c in out.items() if c!=k()}
def pm(p,q):
 out={}
 for m,c in p.items():
  for n,d in q.items():
   z=tuple(sorted(m+n));out[z]=add(out.get(z,k()),mul(c,d))
 return {m:c for m,c in out.items() if c!=k()}
def ps(p,c):return {m:mul(v,c) for m,v in p.items() if mul(v,c)!=k()}
def pc(c):return {():c}
def px(i):return {(i,):k(1)}
qs=[{tuple(t['monomial']):k(*t['coefficient']) for t in r} for r in rels]
f,S,g,B,w,W,T=[px(i) for i in range(7)]
a,b,c,d=k(57,-28),k(8,-14),k(88,-48),k(39,-36)
alpha,beta,gamma,delta=k(156,F(69,2)),k(118,60),k(-288,-128),k(252,-672)
ge=ps(pa(pm(pa(ps(S,beta),pc(alpha)),T),ps(S,neg(alpha)),pc(neg(gamma))),inv(delta))
targetF=pa(pm(pa(pc(a),ps(f,c)),ge),ps(pm(f,S),b),ps(f,d))
targetE=pa(ps(pm(S,ge),b),ps(ge,neg(d)),ps(f,neg(a)),pc(k(8)))
Anorm=pa(pc(mul(a,a)),ps(f,mul(k(2),mul(a,c))),ps(B,mul(c,c)))
N=pa(pc(k(8)),ps(f,neg(a)),ps(ge,mul(k(-2),d)))
targetW=pa(pm(Anorm,w),ps(pm(N,N),k(-1)))

from math import comb
Dc=k(11,-6)
def pp(p,n):
 out=pc(k(1))
 for _ in range(n):out=pm(out,p)
 return out
A=pa(pc(a),ps(f,c)); C=pa(ps(S,beta),pc(alpha)); bs=pa(ps(S,b),pc(d))
Tnum=pa(pm(pa(ps(S,alpha),pc(gamma)),A),ps(pm(f,bs),neg(delta)))
subs={0:(f,0,0),1:(S,0,0),3:(pp(f,2),0,0),4:(pm(pp(f,2),pp(bs,4)),4,0),5:(pm(pp(f,4),pp(bs,8)),8,0),6:(Tnum,1,1)}
Ap=[pp(A,n) for n in range(17)]; Cp=[pp(C,n) for n in range(3)]
results=[]
for ix,q in enumerate(qs):
 out={}
 for m,coef in q.items():
  z=pc(coef); da=dc=0
  for i in m:
   num,aa,cc=subs[i];z=pm(z,num);da+=aa;dc+=cc
  assert da<=16 and dc<=2
  out=pa(out,pm(pm(z,Ap[16-da]),Cp[2-dc]))
 rem={}
 for mon,coef in out.items():
  assert all(i in [0,1] for i in mon)
  af=mon.count(0); ss=mon.count(1); power=ss//2; odd=ss%2
  dcPower=k(1)
  for j in range(power+1):
   key=(af-power+2*j,odd);v=mul(coef,mul(k(comb(power,j)),dcPower));rem[key]=add(rem.get(key,k()),v);dcPower=mul(dcPower,neg(Dc))
 rem={m:v for m,v in rem.items() if v!=k()}
 assert not rem,(ix,rem)
 results.append({'relation':ix,'cleared_terms':len(out),'remainder_terms':len(rem)})
print(json.dumps({'status':'pass','method':'independent substitution and reduction by f*S^2+Dc*f^2=1','clearing':'(a+c*f)^16*(beta*S+alpha)^2','relations':results},indent=2))
