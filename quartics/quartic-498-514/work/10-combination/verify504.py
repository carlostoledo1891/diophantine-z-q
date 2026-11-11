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
d=read(H/'candidate505-ir.json');out=read(H/'candidate504-ir.json');cert=read(H/'certificate504.json')
assert sha(H/'candidate505-ir.json')==cert['source505Sha256']=='bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966'
assert sha(H/'candidate504-ir.json')==cert['statistics']['candidateSha256']
dr={r['name']:V.readpoly(r['terms']) for r in d['residuals']};rows={r['name']:V.readpoly(r['terms']) for r in out['residuals']}
cn={x['name']:x['id'] for x in out['coordinates']}
depth=read(H.parent/'03-depth/beta12/final/candidate-ir.json')
def val(s):return tuple(V.readpoly(depth['values'][s+'.'+str(j)]['terms']) for j in range(2))
def newval(s):return tuple(var(cn['scalar.shiftedS.reciprocal.'+s+'.'+str(j)]) for j in range(2))
D=fc(11,-6);a=fc(-1,Q(7,4));b=fc(Q(39,8),Q(-9,2));cc=fm(a,a)
h,j,x=val('S.h'),val('S.j'),val('S.x');g,d2,k=map(newval,['g','d2','k']);f=val('Sscalar.f');z=val('Sscalar.z')
dd=fa(fm(cc,x),D);N=fs(fm(a,j),fm(b,h));M=fs(fscale(fm(fm(a,D),fm(h,fa(x,cc))),-2),fm(b,fm(j,fs(fm(cc,x),D))))
expected={}
for name,ps in [('g',fs(fm(dd,g),N)),('d2',fs(d2,fm(dd,dd))),('k',fs(fm(d2,k),M))]:
 for i,p in enumerate(ps):expected[f'scalar.shiftedS.reciprocal.{name}.definition.{i}']=p
expected['scalar.shiftedS.reciprocal.f0Inverse.definition']=sub(V.mul(f[0],var(cn['scalar.shiftedS.reciprocal.f0Inverse'])),c(1))
for i,p in enumerate(fs(f,fm(g,g))):expected[f'Sscalar.f.definition.{i}']=p
for i,p in enumerate(fa(fm(k,z),g)):expected[f'Sscalar.z.definition.{i}']=p
deleted=set(cert['deletedRows']);changed={f'Sscalar.{s}.definition.{j}' for s in ['f','z'] for j in range(2)}
assert set(rows)==(set(dr)-deleted)|set(expected)
for name,p in rows.items():assert norm(p)==norm(expected[name] if name in expected else dr[name]),name
assert set(dr)-set(rows)==deleted
assert len(out['coordinates'])==504 and len(rows)==473
assert {co['id'] for co in d['coordinates']}-{co['id'] for co in out['coordinates']}==set(cert['removedCoordinates'])
assert all(V.degree(p)<=2 for p in rows.values())
total={}
for p in rows.values():
 items=list(norm(p).items())
 for i,((s,m),aa) in enumerate(items):
  for jj in range(i,len(items)):
   (t,n),bb=items[jj];key=(s+t,tuple(sorted(m+n)));total[key]=total.get(key,0)+aa*bb*(1 if i==jj else 2)
total={k:v for k,v in total.items() if v}
assert total==V.readpoly(read(H/'polynomial504.json')['terms'])
assert len(total)==24733 and V.degree(total)==4
assert V.variables(total)=={co['id'] for co in out['coordinates']}
assert total[(2,(57,57))]==16 and not any(s!=2 and m==(57,57) for s,m in total)
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
assert any(s==0 and v==1 for (s,m),v in total.items())
# Exact symbolic quotient-ring checks. Work over Q(sqrt2)[h,j]/(j^2-h^4+D).
HH,JJ=10000,10001
def reduce_field(q):
 result=fc(0)
 for side,p in enumerate(q):
  for (s,m),coef in p.items():
   assert not s
   count=m.count(JJ);rem=tuple(v for v in m if v!=JJ)
   atom={(0,rem+((JJ,) if count%2 else ())):coef}
   piece=(atom,{}) if side==0 else ({},atom)
   for _ in range(count//2):piece=fm(piece,fs(({(0,(HH,HH,HH,HH)):Q(1)},{}),D))
   result=fa(result,piece)
 return result
def mult(p,q):return reduce_field(fm(p,q))
def power(p,n):
 q=fc(1)
 for _ in range(n):q=mult(q,p)
 return q
hh=(var(HH),{});jj=(var(JJ),{});xx=power(hh,2);dd=fa(mult(cc,xx),D);dx=fs(xx,cc)
nn=fs(mult(a,jj),mult(b,hh));mm=fs(fscale(mult(mult(a,D),mult(hh,fa(xx,cc))),-2),mult(b,mult(jj,fs(mult(cc,xx),D))))
sn=fa(mult(hh,jj),mult(a,b));xn=fs(power(sn,2),mult(fa(xx,cc),power(dx,2)))
yn=fs(mult(sn,fs(mult(xx,power(dx,2)),xn)),mult(mult(hh,jj),power(dx,3)))
identities=[fs(fa(power(mm,2),mult(D,power(nn,4))),power(dd,4)),
 fs(mult(xn,power(nn,2)),mult(power(dx,2),power(dd,2))),
 fs(mult(yn,power(nn,3)),mult(mult(mm,dd),power(dx,3))),
 fs(mult(nn,fa(mult(a,jj),mult(b,hh))),mult(dx,dd))]
assert all(q==fc(0) for q in identities)
result={'verified':True,'variables':504,'residuals':473,'degree':4,'monomials':24733,'content':1,
 'maximumCoefficient':'16*3^(2^26)','quotientRingIdentities':4,'source505Sha256':cert['source505Sha256'],
 'candidate504Sha256':sha(H/'candidate504-ir.json'),'scope':'Full coefficient and row checks; arithmetic branch exclusion recorded in REPORT504.md.'}
(H/'VERIFICATION504.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

