"""Producer-free rational-log presentation and complete SOS check."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm,comb
from functools import reduce
import json,hashlib,sys
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def add(a,b,k=1):
 c=a.copy()
 for m,v in b.items():c[m]=c.get(m,0)+k*v
 return {m:v for m,v in c.items() if v}
def mul(a,b):
 c={}
 for m,v in a.items():
  for n,w in b.items():
   key=tuple(sorted(m+n));c[key]=c.get(key,0)+v*w
 return {m:v for m,v in c.items() if v}
def con(v):return {():F(v)} if v else {}
def var(v):return {(v,):F(1)}
def fc(a,b=0):return con(a),con(b)
def plus(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def minus(a,b):return tuple(add(x,y,-1) for x,y in zip(a,b))
def times(a,b):return add(mul(a[0],b[0]),mul(a[1],b[1]),2),add(mul(a[0],b[1]),mul(a[1],b[0]))
def scale(a,c):return tuple({m:v*c for m,v in x.items() if v*c} for x in a)
def norm(a):
 d=reduce(lcm,(v.denominator for v in a.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in a.values()),0)
 return {m:v*F(d,g) for m,v in a.items()}
def ev(a,env):
 out={}
 for mon,v in a.items():
  term=con(v)
  for x in mon:term=mul(term,env.get(x,var(x)))
  out=add(out,term)
 return out
count=int(sys.argv[1]) if len(sys.argv)>1 else 490
prefix=f'rational{count}';cert=read(prefix+'-certificate.json');source=read(cert['source']);out=read(prefix+'-ir.json');depth=read('inputs/depth519.json')
assert hashlib.sha256((H/cert['source']).read_bytes()).hexdigest()==cert['sourceSha256']
assert hashlib.sha256((H/(prefix+'-ir.json')).read_bytes()).hexdigest()==cert['statistics']['candidateSha256']
old={r['name']:p(r['terms']) for r in source['residuals']};new={r['name']:p(r['terms']) for r in out['residuals']}
cn={c['name']:c['id'] for c in source['coordinates']};nc={c['name']:c['id'] for c in out['coordinates']}
def val(n):return tuple(p(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
a=[F(1),F(-2,5)]
for j in range(2,10):a.append(a[-1]*F(4*j-5,4*j+1))
q=[F(1),F(-1526,1073),F(513,1073)]
product=[sum(q[k]*a[j-k] for k in range(3) if 0<=j-k<10) for j in range(12)]
assert product[7]==product[9]==0
assert product[10:]==[F(2970726,254443709),F(-41697666,6361092725)]
assert sum(q)==F(60,1073)>0 and q[1]+2*q[2]<0
bern=[sum(product[i]*F(comb(k,i),comb(8,i)) for i in range(k+1)) for k in range(9)]
assert min(bern)==F(83904,10113025)>0
for coef in product+q+a:
 d=coef.denominator
 for prime in [2,3,5,7,11,13,17,19,23,29,31,37]:
  while d%prime==0:d//=prime
 assert d==1
expected={};env={};deleted=set();removed=set();renamed={}
for i in [0,2,3,4]:
 pre=f'logV{i}';w=val(pre+'.w');s=val(pre+'.wPower2');G=val(pre+'.polynomial')
 t=tuple(var(nc[f'{pre}.wPower4.{j}']) for j in range(2));R=tuple(var(nc[f'{pre}.rationalApproximation.{j}']) for j in range(2))
 # Check retained w-square outputs against the actual source equations.
 for j,poly in enumerate(minus(s,times(w,w))):
  oldrow=old[f'{pre}.wPower2.{j}.definition'];factor=next(iter(poly.values()))/oldrow[next(iter(poly))]
  assert poly=={m:v*factor for m,v in oldrow.items()}
 # Evaluate N from independent convolution-derived coefficients.
 powers=[fc(1),w,s,times(w,s),t,times(w,t),times(s,t),fc(0),times(t,t)]
 N=fc(0)
 for coef,power in zip(product,powers):N=plus(N,scale(power,coef))
 Q=plus(plus(fc(1),scale(w,q[1])),scale(s,q[2]))
 for block,polys in [('wPower4',minus(t,times(s,s))),('rationalApproximation',minus(times(Q,R),N))]:
  for j,poly in enumerate(polys):expected[f'{pre}.{block}.{j}.definition']=poly
 for j in range(2):
  x=cn[f'{pre}.polynomial.{j}.quadratic'];coef=G[j][(x,)];rest=add(G[j],{(x,):coef},-1)
  env[x]={m:v/coef for m,v in add(var(x),rest,-1).items()}
  assert ev(G[j],{x:env[x]})==R[j]
  renamed[x]=f'{pre}.rationalApproximation.{j}'
  y=cn[f'{pre}.wPower3.{j}.quadratic'];assert nc[f'{pre}.wPower4.{j}']==y;renamed[y]=f'{pre}.wPower4.{j}'
  removed.add(cn[f'{pre}.middle.{j}.quadratic'])
  for block in ['wPower3','middle','polynomial']:deleted.add(f'{pre}.{block}.{j}.definition')
assert set(new)==(set(old)-deleted)|set(expected)
for name,poly in new.items():assert poly==(expected[name] if name in expected else ev(old[name],env)),name
assert removed==set(cert['removedCoordinates']) and deleted==set(cert['deletedRows'])
assert {c['id']:c['name'] for c in out['coordinates']}=={c['id']:renamed.get(c['id'],c['name']) for c in source['coordinates'] if c['id'] not in removed}
assert set(nc.values())=={i for poly in new.values() for mon in poly for i in mon if i!=-1}
assert out['fixedParameter']==source['fixedParameter']
total={}
for poly in new.values():
 assert max(sum(i!=-1 for i in mon) for mon in poly)<=2
 total=add(total,mul(norm(poly),norm(poly)))
assert total==p(read(prefix+'-polynomial.json')['terms'])
assert len(total)==cert['statistics']['monomials'] and len(nc)==count
assert max(sum(i!=-1 for i in mon) for mon in total)==4
assert any(-1 not in mon and abs(v)==1 for mon,v in total.items())
assert [(mon,v) for mon,v in total.items() if mon.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v.numerator).bit_length() for mon,v in total.items() if -1 not in mon)<2048
assert max(abs(v) for mon,v in total.items() if mon.count(-1)==1)<=48
result={**cert['statistics'],'finiteVerified':True,'maximumCoefficient':'16*3^(2^26)','content':1,'status':'Arithmetic acceptance requires separate non-author review.'}
(H/(prefix+'-verification.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
