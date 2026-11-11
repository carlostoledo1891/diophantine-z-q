"""Eliminate the scalar reciprocal k pair by exact quadratic row identities."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def pol(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def add(a,b,c=1):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,0)+c*v
 return {k:v for k,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {k:v for k,v in d.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def con(a):return {(0,()):F(a)} if a else {}
def var(i):return {(0,(i,)):F(1)}
def fc(a,b=0):return con(a),con(b)
def fa(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(add(x,y,-1) for x,y in zip(a,b))
def fm(a,b):return add(mul(a[0],b[0]),mul(a[1],b[1]),2),add(mul(a[0],b[1]),mul(a[1],b[0]))
def fsc(a,c):return tuple(scale(x,c) for x in a)
def norm(a):
 d=reduce(lcm,(v.denominator for v in a.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in a.values()),0)
 return scale(a,F(d,g))
data=read('inputs/released498.json');depth=read('inputs/depth519.json');cn={c['name']:c['id'] for c in data['coordinates']}
def val(n):return tuple(pol(depth['values'][n+'.'+str(j)]['terms']) for j in range(2))
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6)
h,j,x=map(val,['H.h','H.j','H.x']);g=(var(700),var(701));f=val('V0.f');ell=val('logV0');G=val('logV0.polynomial')
c=fm(a,a);dd=fa(fm(c,x),D);N=fs(fm(a,j),fm(b,h));T=fs(fs(fsc(fm(fm(D,b),g),2),fsc(fm(D,h),2)),fm(fm(a,b),j))
newg=fs(fm(dd,g),N);newf=fs(f,fm(g,g));newell=fa(fm(T,ell),fm(fm(a,N),G))
prefix=('V0.dxInverse','V0.slope','V0.slopeSquare','V0.yProduct')
removed={c['id'] for c in data['coordinates'] if c['name'].startswith(prefix) or c['name']=='V0.dxRationalCoefficientInverse'}
deleted={r['name'] for r in data['residuals'] if r['name'].startswith(prefix)}
assert len(removed)==7 and len(deleted)==7
changed=[f'{n}.definition.{i}' for n in ['V0.f','logV0'] for i in range(2)]
assert {r['name'] for r in data['residuals'] if any(set(t['monomial'])&removed for t in r['terms'])}==deleted|set(changed)
for r in data['residuals']:
 for i in range(2):
  if r['name']==f'V0.f.definition.{i}':r['terms']=terms(newf[i])
  if r['name']==f'logV0.definition.{i}':r['terms']=terms(newell[i])
data['coordinates']=[c for c in data['coordinates'] if c['id'] not in removed]
data['residuals']=[r for r in data['residuals'] if r['name'] not in deleted]
for i in range(2):
 data['coordinates'].append({'id':700+i,'name':f'V0.reciprocal.g.{i}','kind':'gate','block':'reciprocal_fixed_difference'})
 data['residuals'].append({'id':700+i,'name':f'V0.reciprocal.g.definition.{i}','terms':terms(newg[i]),'kind':'structural','block':'reciprocal_fixed_difference'})
data['status']='Under400 candidate: V0 reciprocal chart; domain supplied by retained nonzero V1 logarithm numerator.'
total={}
for r in data['residuals']:
 pp=norm(pol(r['terms']));assert max(len(m) for s,m in pp)<=2;total=add(total,mul(pp,pp))
assert len(data['coordinates'])==493 and len(data['residuals'])==462
assert max(len(m) for s,m in total)==4
assert {v for s,m in total for v in m}=={c['id'] for c in data['coordinates']}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
write('v0-493-ir.json',data);write('v0-493-polynomial.json',{'fixedParameter':data['fixedParameter'],'terms':terms(total)})
stats={'variables':493,'witnesses':492,'residuals':462,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha('v0-493-ir.json'),'polynomialSha256':sha('v0-493-polynomial.json')}
write('v0-493-certificate.json',{'sourceSha256':sha('inputs/released498.json'),'removedCoordinates':sorted(removed),'deletedRows':sorted(deleted),'changedRows':changed,'statistics':stats});print(json.dumps(stats,indent=2))
