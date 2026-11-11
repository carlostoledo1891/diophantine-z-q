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
src=H/'inputs/released498.json';data=read('inputs/released498.json');depth=read('inputs/depth519.json');cn={c['name']:c['id'] for c in data['coordinates']}
def val(n):return tuple(pol(depth['values'][n+'.'+str(j)]['terms']) for j in range(2))
def new(n):return tuple(var(cn['scalar.shiftedS.reciprocal.'+n+'.'+str(j)]) for j in range(2))
h,j,x=map(val,['S.h','S.j','S.x']);z=val('Sscalar.z');g,k=map(new,['g','k'])
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6)
c=fm(a,a);d=fa(fm(c,x),D);N=fs(fm(a,j),fm(b,h));T=fs(fs(fsc(fm(fm(D,b),g),2),fsc(fm(D,h),2)),fm(fm(a,b),j))
oldg=fs(fm(d,g),N);oldk=fs(fm(fm(a,d),k),T);oldz=fa(fm(k,z),g);newz=fa(fm(T,z),fm(a,N))
assert newz==fs(fs(fm(fm(a,d),oldz),fm(z,oldk)),fm(a,oldg))
rows={r['name']:r for r in data['residuals']}
deleted=[f'scalar.shiftedS.reciprocal.k.definition.{i}' for i in range(2)]
changed=[f'Sscalar.z.definition.{i}' for i in range(2)]
removed=[cn['scalar.shiftedS.reciprocal.k.'+str(i)] for i in range(2)]
for i in range(2):
 assert norm(pol(rows[deleted[i]]['terms']))==norm(oldk[i])
 assert norm(pol(rows[changed[i]]['terms']))==norm(oldz[i])
 assert norm(pol(rows[f'scalar.shiftedS.reciprocal.g.definition.{i}']['terms']))==norm(oldg[i])
 rows[changed[i]]['terms']=terms(newz[i])
data['residuals']=[r for r in data['residuals'] if r['name'] not in deleted];data['coordinates']=[c for c in data['coordinates'] if c['id'] not in removed]
data['status']='Under400 candidate: eliminate scalar reciprocal k by quadratic identities.'
total={}
for r in data['residuals']:
 pp=norm(pol(r['terms']));total=add(total,mul(pp,pp))
assert len(data['coordinates'])==496 and len(data['residuals'])==465
assert max(len(m) for s,m in total)==4
assert {i for s,m in total for i in m}=={c['id'] for c in data['coordinates']}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
write('scalar496-ir.json',data);write('scalar496-polynomial.json',{'fixedParameter':data['fixedParameter'],'terms':terms(total)})
stats={'variables':496,'witnesses':495,'residuals':465,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha('scalar496-ir.json'),'polynomialSha256':sha('scalar496-polynomial.json')}
write('scalar496-certificate.json',{'sourceSha256':sha('inputs/released498.json'),'removedCoordinates':removed,'deletedRows':deleted,'changedRows':changed,'statistics':stats});print(json.dumps(stats,indent=2))
