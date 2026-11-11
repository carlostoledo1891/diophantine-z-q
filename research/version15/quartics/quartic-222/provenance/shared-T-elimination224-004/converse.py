from fractions import Fraction as F
from itertools import combinations_with_replacement
import json
from pathlib import Path
Z=(F(0),F(0));O=(F(1),F(0))
def ka(a,b):return(a[0]+b[0],a[1]+b[1])
def kn(a):return(-a[0],-a[1])
def km(a,b):return(a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ki(a):
 d=a[0]*a[0]-2*a[1]*a[1];return(a[0]/d,-a[1]/d)
def C(a):return{():tuple(map(F,a))} if a!=Z else{}
def X(i):return{(i,):O}
def add(*ps):
 r={}
 for p in ps:
  for m,a in p.items():r[m]=ka(r.get(m,Z),a)
 return{m:a for m,a in r.items() if a!=Z}
def sc(p,a):return{m:km(v,a) for m,v in p.items() if km(v,a)!=Z}
def neg(p):return sc(p,(-1,0))
def mul(p,q):
 r={}
 for m,a in p.items():
  for n,b in q.items():
   k=tuple(sorted(m+n));r[k]=ka(r.get(k,Z),km(a,b))
 return{m:a for m,a in r.items() if a!=Z}
def lead(p):return max(p,key=lambda m:(len(m),m))
def reduce(p,basis):
 p=dict(p)
 for m,(r,_) in sorted(basis.items(),key=lambda kv:(len(kv[0]),kv[0]),reverse=True):
  if m in p:p=add(p,sc(r,kn(p[m])))
 return p
def insert(p,basis):
 p=reduce(p,basis)
 if p:
  m=lead(p);p=sc(p,ki(p[m]));basis[m]=(p,None)
 return p


P=Path(__file__).resolve().parent
rels=json.loads((P/'FIELD-RELATIONS.json').read_text())[0]['relations']
def parse(r):return {tuple(t['monomial']):tuple(map(F,t['coefficient']))for t in r}
qs=[parse(r)for r in rels]
f,S,g,B,w,W,T=[X(i)for i in range(7)]
a=(F(57),F(-28));b=(F(8),F(-14));c=(F(88),F(-48));d=(F(39),F(-36))
alpha=(F(156),F(69,2));beta=(F(118),F(60));gamma=(F(-288),F(-128));delta=(F(252),F(-672))
gexp=sc(add(mul(add(sc(S,beta),C(alpha)),T),neg(sc(S,alpha)),neg(C(gamma))),ki(delta))
oldF=add(mul(add(C(a),sc(f,c)),gexp),sc(mul(f,S),b),sc(f,d))
oldE=add(sc(mul(S,gexp),b),neg(sc(gexp,d)),neg(sc(f,a)),C((8,0)))
oldW=add(mul(add(C(km(a,a)),sc(f,tuple(2*x for x in km(a,c))),sc(B,km(c,c))),w),neg(mul(add(C((8,0)),neg(sc(f,a)),neg(sc(gexp,tuple(2*x for x in d)))),add(C((8,0)),neg(sc(f,a)),neg(sc(gexp,tuple(2*x for x in d)))))))
def span_reduce(target,generators):
 basis={}
 for ix,r in enumerate(generators):
  rr=r.copy();cert={ix:O}
  for m,(row,cc)in sorted(basis.items(),key=lambda kv:(len(kv[0]),kv[0]),reverse=True):
   if m in rr:
    z=kn(rr[m]);rr=add(rr,sc(row,z))
    for i,v in cc.items():cert[i]=ka(cert.get(i,Z),km(z,v))
  if rr:
   m=lead(rr);z=ki(rr[m]);basis[m]=(sc(rr,z),{i:km(z,v)for i,v in cert.items()if v!=Z})
 rr=target.copy();cert={}
 for m,(row,cc)in sorted(basis.items(),key=lambda kv:(len(kv[0]),kv[0]),reverse=True):
  if m in rr:
   z=rr[m];rr=add(rr,sc(row,kn(z)))
   for i,v in cc.items():cert[i]=ka(cert.get(i,Z),km(z,v))
 assert add(rr,*[sc(generators[i],v)for i,v in cert.items()])==target
 return rr,cert
outputs=[]
for name,target in [('F',oldF),('E',oldE),('W',oldW)]:
 maxdeg=1 if name!='W' else 2
 mm=[()]+[(i,)for i in [0,1,3,4,5,6]]
 if maxdeg==2:mm+=list(combinations_with_replacement([0,1,3,4,5,6],2))
 gens=[mul(q,{m:O})for q in qs for m in mm]
 rem,cert=span_reduce(target,gens)
 outputs.append({'name':name,'remainder':[{'monomial':m,'coefficient':list(map(str,a))}for m,a in rem.items()],'certificate':[{'relation':i//len(mm),'multiplier':mm[i%len(mm)],'coefficient':list(map(str,a))}for i,a in cert.items()if a!=Z]})
 print(name,'remainder',len(rem),'certificate',len(cert),flush=True)
# The f=0 branch from the first core relation and B*T relation.
r1=qs[1];r3=qs[3];T0=km(kn(r3[()]),ki(r3[(6,)]))
coefS=ka(r1[(1,)],T0);constant=ka(r1[()],km(r1[(6,)],T0))
print('f0',T0,coefS,constant,flush=True)
(P/'CONVERSE-RESULT.json').write_text(json.dumps({'checks':outputs,'f_zero':{'T':list(map(str,T0)),'S_coefficient':list(map(str,coefS)),'constant':list(map(str,constant))}},indent=2)+'\n')
