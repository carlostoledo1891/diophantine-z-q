from package_paths import reference_repo
"""Reconstruct scalar reciprocal equations and check every504 SOS coefficient."""
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce
from math import gcd,lcm
import json,hashlib,importlib.util
H=Path(__file__).resolve().parent;R=reference_repo()
spec=importlib.util.spec_from_file_location('exact',R/'quartics/quartic-523-540/final523_540/verify_elimination.py');V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def c(x):return {(0,()):Q(x)} if x else {}
def scale(p,x):return {k:v*x for k,v in p.items() if v*x}
def sub(p,q):return V.add(p,scale(q,-1))
def var(i):return {(0,(i,)):Q(1)}
def fa(p,q):return tuple(V.add(a,b) for a,b in zip(p,q))
def fs(p,q):return tuple(sub(a,b) for a,b in zip(p,q))
def fc(a,b=0):return c(a),c(b)
def fm(p,q):return V.add(V.mul(p[0],q[0]),scale(V.mul(p[1],q[1]),2)),V.add(V.mul(p[0],q[1]),V.mul(p[1],q[0]))
def fscale(p,q):return scale(p[0],q),scale(p[1],q)
def norm(p):
 d=reduce(lcm,(x.denominator for x in p.values()),1);g=reduce(gcd,(abs(int(x*d)) for x in p.values()),0)
 return scale(p,Q(d,g))
d=read(H/'candidate501-ir.json');out=read(H/'candidate499-ir.json');cert=read(H/'certificate499.json')
assert sha(H/'candidate501-ir.json')==cert['source501Sha256']
assert sha(H/'candidate499-ir.json')==cert['statistics']['candidateSha256']
dr={r['name']:V.readpoly(r['terms']) for r in d['residuals']};rows={r['name']:V.readpoly(r['terms']) for r in out['residuals']}
depth=read(H.parent/'03-depth/beta12/final/candidate-ir.json');cn={c['name']:c['id'] for c in d['coordinates']}
def val(s):return tuple(V.readpoly(depth['values'][s+'.'+str(j)]['terms']) for j in range(2))
def cv(s):return tuple(var(cn['scalar.shiftedS.reciprocal.'+s+'.'+str(j)]) for j in range(2))
h,j,x=map(val,['S.h','S.j','S.x']);g,k,d2=map(cv,['g','k','d2'])
a,b,D=fc(-1,Q(7,4)),fc(Q(39,8),Q(-9,2)),fc(11,-6);cc=fm(a,a)
assert fs(fm(b,b),fs(fm(cc,cc),D))==fc(0)
dd=fa(fm(cc,x),D);N=fs(fm(a,j),fm(b,h));M=fs(fscale(fm(fm(a,D),fm(h,fa(x,cc))),-2),fm(b,fm(j,fs(fm(cc,x),D))))
newk=fs(fa(fa(fm(fm(a,dd),k),fscale(fm(D,h),2)),fm(fm(a,b),j)),fscale(fm(fm(D,b),g),2))
fullold=fs(fm(fm(dd,dd),k),M);oldg=fs(fm(dd,g),N)
assert fm(dd,newk)==fs(fm(a,fullold),fscale(fm(fm(D,b),oldg),2))
deleted={f'scalar.shiftedS.reciprocal.d2.definition.{t}' for t in range(2)}
changed={f'scalar.shiftedS.reciprocal.k.definition.{t}':newk[t] for t in range(2)}
assert set(rows)==set(dr)-deleted
for name,p in rows.items():assert norm(p)==norm(changed[name] if name in changed else dr[name]),name
for t in range(2):assert norm(dr[f'scalar.shiftedS.reciprocal.g.definition.{t}'])==norm(oldg[t])
for t in range(2):assert norm(dr[f'scalar.shiftedS.reciprocal.d2.definition.{t}'])==norm(fs(d2,fm(dd,dd))[t])
oldstored=fs(fm(d2,k),M)
for t in range(2):assert norm(dr[f'scalar.shiftedS.reciprocal.k.definition.{t}'])==norm(oldstored[t])
total={}
for rr in rows.values():
 ts=list(norm(rr).items())
 for i,((s,m),v) in enumerate(ts):
  for jj in range(i,len(ts)):
   (t,n),w=ts[jj];kk=(s+t,tuple(sorted(m+n)));total[kk]=total.get(kk,0)+v*w*(1 if i==jj else 2)
total={k:v for k,v in total.items() if v}
assert total==V.readpoly(read(H/'polynomial499.json')['terms'])
assert len(total)==24661 and len(out['coordinates'])==499 and len(rows)==468
assert max(len(m) for s,m in total)==4
assert V.variables(total)=={c['id'] for c in out['coordinates']}
assert any(s==0 and v==1 for (s,m),v in total.items())
assert [(m,c) for (s,m),c in total.items() if s==2]==[((57,57),16)]
assert not any(s!=2 and m==(57,57) for s,m in total)
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
result={'verified':True,'variables':499,'witnesses':498,'residuals':468,'degree':4,'monomials':24661,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'candidate499-ir.json'),'polynomialSha256':sha(H/'polynomial499.json'),'polynomialCancellationIdentity':True}
(H/'VERIFICATION499.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
