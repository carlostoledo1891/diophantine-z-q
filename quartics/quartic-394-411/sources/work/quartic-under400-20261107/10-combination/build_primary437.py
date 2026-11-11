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

src='combined439-ir.json';data=read(src);depth=read('inputs/depth519.json');cn={c['name']:c['id'] for c in data['coordinates']}
def val(n):return tuple(pol(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
def named(n):return tuple(var(cn[n+'.'+str(i)]) for i in range(2))
h,j,x,f0,fV,ell=[val(n) for n in ['H.h','H.j','H.x','U0.f','V0.f','logV0']]
s=named('primary.negativeReciprocalZ0');g=named('V0.reciprocal.g');R=named('logV0.rationalApproximation')
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6);d=fa(fm(fm(a,a),x),D)
N=fs(fm(a,j),fm(b,h));T=fs(fs(fsc(fm(fm(D,b),g),2),fsc(fm(D,h),2)),fm(fm(a,b),j))
Np=fs(fm(a,s),b);Tp=fs(fs(fsc(fm(fm(D,b),g),2),fsc(D,2)),fm(fm(a,b),s))
oldfamilies={'H.chart.equation':fa(fs(fm(j,j),fm(x,x)),D),'U0.z.definition':fs(fm(h,s),j),'V0.f.definition':fs(fV,fm(g,g)),'logV0.definition':fa(fm(T,ell),fm(fm(a,N),R)),'V0.reciprocal.g.definition':fs(fm(d,g),N)}
newfamilies={'H.chart.equation':fa(fs(fm(s,s),x),fm(D,f0)),'V0.f.definition':fs(fm(g,g),fm(fV,f0)),'logV0.definition':fa(fm(Tp,ell),fm(fm(a,Np),R)),'V0.reciprocal.g.definition':fs(fm(d,g),Np)}
rows={r['name']:r for r in data['residuals']}
def canonical(p):return scale(p,1/p[min(p)])
for pre,qs in oldfamilies.items():
 for i,q in enumerate(qs):assert canonical(pol(rows[pre+'.'+str(i)]['terms']))==canonical(q),(pre,i)
for pre,qs in newfamilies.items():
 for i,q in enumerate(qs):rows[pre+'.'+str(i)]['terms']=terms(q)
removed={cn['H.chart.j0'],cn['H.chart.j1']};changed=set(pre+'.'+str(i) for pre in oldfamilies for i in range(2));touched=removed|{cn['V0.reciprocal.g.'+str(i)] for i in range(2)}
original=read(src)
assert {r['name'] for r in original['residuals'] if any(touched.intersection(t['monomial']) for t in r['terms'])}==changed
for row in data['coordinates']:
 if row['name'].startswith('V0.reciprocal.g.'):row['name']=row['name'].replace('V0.reciprocal.g.','V0.reciprocal.gOverH.')
data['coordinates']=[c for c in data['coordinates'] if c['id'] not in removed]
data['residuals']=[r for r in data['residuals'] if r['name'] not in {'U0.z.definition.0','U0.z.definition.1'}]
data['status']='Research candidate: shared reciprocal removes H.j through V0 rescaling; pending independent review.'
total={}
for row in data['residuals']:
 q=norm(pol(row['terms']));assert max(len(m) for power,m in q)<=2;total=add(total,mul(q,q))
assert len(data['coordinates'])==437 and len(data['residuals'])==414
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
write('primary437-ir.json',data);write('primary437-polynomial.json',{'fixedParameter':data['fixedParameter'],'terms':terms(total)})
stats={'variables':437,'witnesses':436,'residuals':414,'degree':4,'monomials':len(total),'candidateSha256':sha('primary437-ir.json'),'polynomialSha256':sha('primary437-polynomial.json')}
write('primary437-certificate.json',{'source':src,'sourceSha256':sha(src),'removedCoordinates':sorted(removed),'renamedCoordinates':sorted(touched-removed),'oldFamilies':list(oldfamilies),'newFamilies':list(newfamilies),'statistics':stats});print(json.dumps(stats,indent=2))
