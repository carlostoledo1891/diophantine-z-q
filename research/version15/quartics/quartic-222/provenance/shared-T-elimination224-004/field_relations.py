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

D=(F(11),F(-6));aa=(F(57),F(-28));bb=(F(8),F(-14));cc=(F(88),F(-48));dd=(F(39),F(-36))
def pm(p,q):
 out={}
 for (e,j),a in p.items():
  for (h,k),b in q.items():
   c=km(a,b);z=e+h
   for key,val in ([((z,j+k),c)]if j+k<2 else[((z-1,0),c),((z+1,0),kn(km(D,c)))]):out[key]=ka(out.get(key,Z),val)
 return{k:v for k,v in out.items()if v!=Z}
def shift(p,n):return{(e+n,j):a for(e,j),a in p.items()}
def power(p,n):
 out={(0,0):O}
 for _ in range(n):out=pm(out,p)
 return out

def pa(*ps):
 out={}
 for p in ps:
  for m,a in p.items():out[m]=ka(out.get(m,Z),a)
 return {m:a for m,a in out.items()if a!=Z}
def ps(p,a):return {m:km(c,a)for m,c in p.items()if km(c,a)!=Z}
ap={(0,0):aa,(1,0):cc};gn={(1,0):kn(dd),(1,1):kn(bb)}
alpha=(F(156),F(69,2));beta=(F(118),F(60));gamma=(F(-288),F(-128));delta=(F(252),F(-672))
hp={(0,0):km(alpha,alpha),(-1,0):kn(km(beta,beta)),(1,0):km(km(beta,beta),D)}
tn=pm(pa(pm({(0,1):alpha,(0,0):gamma},ap),ps(gn,delta)),{(0,0):alpha,(0,1):kn(beta)})
funcs=[({(1,0):O},0,0),({(0,1):O},0,0),(gn,1,0),({(2,0):O},0,0),(shift(power(gn,4),-2),4,0),(shift(power(gn,8),-4),8,0),(tn,1,1)]
names=['f','S','g','B','w','W','T']
apows=[power(ap,i)for i in range(17)];hpows=[power(hp,i)for i in range(3)]
def vec(m):
 p={(0,0):O};a=0;h=0
 for i in m:p=pm(p,funcs[i][0]);a+=funcs[i][1];h+=funcs[i][2]
 return pm(pm(p,apows[16-a]),hpows[2-h])
def kernel(ms):
 piv={};rels=[]
 for m in ms:
  p=vec(m);q={m:O}
  for k,(r,rq)in sorted(piv.items(),reverse=True):
   if k in p:
    z=kn(p[k]);q=add(q,sc(rq,z))
    p=pa(p,ps(r,z))
  if p:
   k=max(p);z=ki(p[k]);piv[k]=(ps(p,z),sc(q,z))
  else:rels.append(q)
 return rels
def dump(p):return[{'monomial':list(m),'coefficient':[str(a[0]),str(a[1])]}for m,a in sorted(p.items(),key=lambda kv:(len(kv[0]),kv[0]))]
out=[]
for drop in [2,1,4]:
 inds=[i for i in range(7)if i!=drop];mons=[()]+[(i,)for i in inds]+list(combinations_with_replacement(inds,2))
 rels=kernel(mons);out.append({'dropped':names[drop],'variables':names,'relations':[dump(q)for q in rels]});print(names[drop],len(rels),flush=True)
Path(__file__).with_name('FIELD-RELATIONS.json').write_text(json.dumps(out,indent=2)+'\n')
