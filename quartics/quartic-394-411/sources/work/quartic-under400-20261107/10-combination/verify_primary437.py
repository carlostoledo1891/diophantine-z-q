"""Independent identity and full-coefficient check; imports no producer."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
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
 s=F(d,g)*(1 if a[min(a)]>0 else -1)
 return {m:v*s for m,v in a.items()}

source=read('combined439-ir.json');out=read('primary437-ir.json');depth=read('inputs/depth519.json');cert=read('primary437-certificate.json')
assert hashlib.sha256((H/cert['source']).read_bytes()).hexdigest()==cert['sourceSha256']
old={r['name']:p(r['terms']) for r in source['residuals']};new={r['name']:p(r['terms']) for r in out['residuals']};cn={c['name']:c['id'] for c in source['coordinates']}
def val(n):return tuple(p(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
def named(n):return tuple(var(cn[n+'.'+str(i)]) for i in range(2))
h,j,x,f,fv,ell=[val(n) for n in ['H.h','H.j','H.x','U0.f','V0.f','logV0']]
s=named('primary.negativeReciprocalZ0');v=named('V0.reciprocal.g');R=named('logV0.rationalApproximation')
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6);d=plus(times(times(a,a),x),D)
N=minus(times(a,j),times(b,h));T=minus(minus(scale(times(times(D,b),v),2),scale(times(D,h),2)),times(times(a,b),j))
Np=minus(times(a,s),b);Tp=minus(minus(scale(times(times(D,b),v),2),scale(D,2)),times(times(a,b),s))
oldq={'H.chart.equation':plus(minus(times(j,j),times(x,x)),D),'U0.z.definition':minus(times(h,s),j),'V0.f.definition':minus(fv,times(v,v)),'logV0.definition':plus(times(T,ell),times(times(a,N),R)),'V0.reciprocal.g.definition':minus(times(d,v),N)}
newq={'H.chart.equation':plus(minus(times(s,s),x),times(D,f)),'V0.f.definition':minus(times(fv,f),times(v,v)),'logV0.definition':plus(times(Tp,ell),times(times(a,Np),R)),'V0.reciprocal.g.definition':minus(times(d,v),Np)}
changed=set(pre+'.'+str(i) for pre in oldq for i in range(2));removed={cn['H.chart.j0'],cn['H.chart.j1']};touch=removed|{cn[f'V0.reciprocal.g.{i}'] for i in range(2)}
for pre,qs in oldq.items():
 for i,q in enumerate(qs):assert norm(q)==norm(old[pre+'.'+str(i)])
for pre,qs in newq.items():
 for i,q in enumerate(qs):assert norm(q)==norm(new[pre+'.'+str(i)]),(pre,i)
assert set(new)==set(old)-{'U0.z.definition.0','U0.z.definition.1'}
assert {n for n,q in old.items() if any(touch.intersection(m) for m in q)}==changed
for n,q in new.items():
 if n not in changed:assert q==old[n]
# Reconstruct old j=h*s and oldg=h*v. The source x and reciprocal rows
# make every old row an explicit multiple of new or retained rows.
EX=minus(times(h,h),x);EF=minus(times(x,f),fc(1))
for i in range(2):
 assert norm(EX[i])==norm(old[f'H.chart.x.{i}.definition'])
 assert norm(EF[i])==norm(old[f'U0.f.definition.{i}'])
jback=times(h,s);gback=times(h,v)
oldcurveback=plus(minus(times(jback,jback),times(x,x)),D)
assert oldcurveback==minus(plus(times(x,newq['H.chart.equation']),times(EX,times(s,s))),times(D,EF))
oldfback=minus(fv,times(gback,gback))
assert oldfback==minus(minus(times(x,newq['V0.f.definition']),times(fv,EF)),times(EX,times(v,v)))
Nback=minus(times(a,jback),times(b,h));Tback=minus(minus(scale(times(times(D,b),gback),2),scale(times(D,h),2)),times(times(a,b),jback))
assert minus(times(d,gback),Nback)==times(h,newq['V0.reciprocal.g.definition'])
assert plus(times(Tback,ell),times(times(a,Nback),R))==times(h,newq['logV0.definition'])
expected={c['id']:dict(c) for c in source['coordinates'] if c['id'] not in removed}
for i in touch-removed:expected[i]['name']=expected[i]['name'].replace('V0.reciprocal.g.','V0.reciprocal.gOverH.')
assert expected=={c['id']:c for c in out['coordinates']}
assert source['fixedParameter']==out['fixedParameter']
total={}
for q in new.values():
 assert max(sum(i!=-1 for i in m) for m in q)<=2
 total=add(total,mul(norm(q),norm(q)))
assert total==p(read('primary437-polynomial.json')['terms'])
assert len(expected)==437 and len(new)==414 and len(total)==6503
assert max(sum(i!=-1 for i in m) for m in total)==4
assert {i for m in total for i in m if i!=-1}==set(expected)
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
result={**cert['statistics'],'verified':True,'content':1,'maximumCoefficient':'16*3^(2^26)','scope':'Exact polynomial witness identities, full incidence and SOS. Non-author review pending.'}
(H/'primary437-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
