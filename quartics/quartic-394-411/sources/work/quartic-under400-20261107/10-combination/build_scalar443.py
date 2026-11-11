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

src='inputs/accepted445-ir.json';data=read(src);depth=read('inputs/depth519.json');cn={c['name']:c['id'] for c in data['coordinates']}
def val(n):return tuple(pol(depth['values'][n+'.'+str(j)]['terms']) for j in range(2))
def named(n):return tuple(var(cn[n+'.'+str(i)]) for i in range(2))
h,j=val('S.h'),val('S.j');g=named('scalar.shiftedS.reciprocal.g');rho=val('scalar.zRatio');z=val('Sscalar.z');s=named('primary.negativeReciprocalZ0')
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6)
N=fs(fm(a,j),fm(b,h));T=fs(fs(fsc(fm(fm(D,b),g),2),fsc(fm(D,h),2)),fm(fm(a,b),j))
newrow=fs(fm(T,rho),fm(fm(a,N),s));oldz=fa(fm(T,z),fm(a,N))
Hh,Hj=val('H.h'),val('H.j');ratio=fa(fm(Hh,rho),fm(Hj,z))
rows={r['name']:r for r in data['residuals']};deleted=[f'Sscalar.z.definition.{i}' for i in range(2)];changed=[f'scalar.zRatio.definition.{i}' for i in range(2)]
ids={cn[f'Sscalar.z.{i}'] for i in range(2)}
assert {n for n,r in rows.items() if any(ids.intersection(t['monomial']) for t in r['terms'])}==set(deleted+changed)
for i in range(2):
 assert norm(pol(rows[deleted[i]]['terms']))==norm(oldz[i])
 assert norm(pol(rows[changed[i]]['terms']))==norm(ratio[i])
 rows[changed[i]]['terms']=terms(newrow[i])
data['coordinates']=[c for c in data['coordinates'] if c['id'] not in ids]
data['residuals']=[r for r in data['residuals'] if r['name'] not in deleted]
data['status']='Research candidate: shared primary reciprocal removes scalar z pair; pending non-author review.'
total={}
for row in data['residuals']:
 p=norm(pol(row['terms']));assert max(len(m) for power,m in p)<=2;total=add(total,mul(p,p))
assert len(data['coordinates'])==443 and len(data['residuals'])==420
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
write('scalar443-ir.json',data);write('scalar443-polynomial.json',{'fixedParameter':data['fixedParameter'],'terms':terms(total)})
stats={'variables':443,'witnesses':442,'residuals':420,'degree':4,'monomials':len(total),'candidateSha256':sha('scalar443-ir.json'),'polynomialSha256':sha('scalar443-polynomial.json')}
write('scalar443-certificate.json',{'source':src,'sourceSha256':sha(src),'removedCoordinates':sorted(ids),'deletedRows':deleted,'changedRows':changed,'statistics':stats});print(json.dumps(stats,indent=2))
