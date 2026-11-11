"""Independent finite/normalization checks for preparation-zero439."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent;BASE=H.parent/'06-product'/'scalar-redesign';E=BASE/'preparation-zero439'
REPO=H.parents[1]/'quartic-version6-release'/'repository'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def v(i):return {(i,):F(1)}
def c(q):return {():F(q)} if q else {}
def add(a,b,k=1):
 d=a.copy()
 for m,q in b.items():d[m]=d.get(m,0)+k*q
 return {m:q for m,q in d.items() if q}
def sc(a,k):return {m:q*k for m,q in a.items() if q*k}
def mul(a,b):
 d={}
 for m,q in a.items():
  for n,r in b.items():
   t=tuple(sorted(m+n));d[t]=d.get(t,0)+q*r
 return {m:q for m,q in d.items() if q}
def sub(a,mp):
 d={}
 for m,q in a.items():
  t=c(q)
  for i in m:t=mul(t,mp.get(i,v(i)))
  d=add(d,t)
 return d
def norm(a):
 den=reduce(lcm,(q.denominator for q in a.values()),1);g=reduce(gcd,(abs(int(q*den)) for q in a.values()),0)
 return sc(a,F(den,g)*(1 if a[min(a)]>0 else -1))

E=BASE/'normalized-pole438';S=BASE/'preparation-zero439'/'candidate439-ir.json'
pins={S:'135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3', E/'REPORT.md':'726ba8026c7afaf133594fdd6e5392f3dfe882826d99ac4071678c40b063809c',E/'candidate438-ir.json':'6867a2365bf3bc33225aba4d055d4e698f2fbcd67b958d6f528e477b0e697ea9',E/'polynomial438.json':'e0684677d00d82b700d8442aa71d2c9226b6e000e46bfbfb2ad59bd55e6e253a'}
for p,h in pins.items():assert sha(p)==h,str(p)
a=read(S);b=read(E/'candidate438-ir.json')
o={r['name']:parse(r['terms']) for r in a['residuals']};n={r['name']:parse(r['terms']) for r in b['residuals']}
weights={51:1,52:1,53:1,54:1,532:1,527:2,534:2}
names={'scalar.p2.definition','scalar.firstConic','scalar.Bh.definition','scalar.q2.definition','scalar.secondConic'}
x=v(526);x2=mul(x,x)
mp={i:mul(v(i),x if w==1 else x2) for i,w in weights.items()};mp[531]=x2
assert set(n)==set(o)-{'scalar.t2.definition'}
assert sub(o['scalar.t2.definition'],mp)=={}
for name in names:assert sub(o[name],mp)==mul(x2,n[name]),name
assert {name for name,q in o.items() if any(set(m)&(set(weights)|{531}) for m in q)}==names|{'scalar.t2.definition'}
assert {name for name,q in n.items() if any(set(m)&set(weights) for m in q)}==names
for name in set(n)-names:assert n[name]==o[name]
assert {name for name in n if n[name]!=o[name]}=={'scalar.firstConic','scalar.Bh.definition'}
# The reverse substitution is checked as a Laurent-polynomial identity, with
# the exponent of x recorded separately. Replace new u by old u/x^weight.
def reverse(q):
 d={}
 for m,t in q.items():
  e=m.count(526)-sum(weights.get(i,0) for i in m)
  mm=tuple(i for i in m if i!=526)
  key=(e,mm);d[key]=d.get(key,F(0))+t
 return {k:t for k,t in d.items() if t}
def source_laurent(q):
 d={}
 for m,t in q.items():
  e=m.count(526)+2*m.count(531)-2
  mm=tuple(i for i in m if i not in {526,531})
  key=(e,mm);d[key]=d.get(key,F(0))+t
 return {k:t for k,t in d.items() if t}
for name in names:assert reverse(n[name])==source_laurent(o[name])
# Squared slots must carry weight two while their square roots carry one.
assert n['scalar.p2.definition']==add(mul(v(53),v(53)),v(527),-1)
assert n['scalar.q2.definition']==add(mul(v(54),v(54)),v(534),-1)
K=o['scalar.Bh.definition'][(51,531)];assert K>0
assert n['scalar.Bh.definition']==add(add(sc(v(51),17),mul(v(51),x),K),mul(v(52),v(532)),-17)
# Full coordinate, residual metadata and all non-change top-level fields.
oc={q['id']:q for q in a['coordinates']};nc={q['id']:q for q in b['coordinates']}
assert set(nc)==set(oc)-{531}
for i,q in nc.items():
 expected=dict(oc[i])
 if i in weights:expected['name']='normalized_'+expected['name']
 assert q==expected
oldrecords={q['name']:q for q in a['residuals']}
for q in b['residuals']:
 assert {k:t for k,t in q.items() if k!='terms'}=={k:t for k,t in oldrecords[q['name']].items() if k!='terms'}
for k in a:
 if k not in {'coordinates','residuals','status'}:assert a[k]==b[k]
# Independent full sparse expansion after primitive normalization.
total={}
for q in n.values():
 assert max(sum(i!=-1 for i in m) for m in q)<=2
 z=norm(q);total=add(total,mul(z,z))
assert total==parse(read(E/'polynomial438.json')['terms'])
assert (len(nc),len(n),len(total))==(438,416,6655)
assert max(sum(i!=-1 for i in m) for m in total)==4
assert {i for m in total for i in m if i!=-1}==set(nc)
assert any(-1 not in m and abs(q)==1 for m,q in total.items())
assert {m:q for m,q in total.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
assert max(abs(q.numerator).bit_length() for m,q in total.items() if m.count(-1)<2)<2048
assert a['fixedParameter']==b['fixedParameter']
out={'passed':True,'variables':438,'witnesses':437,'rows':416,'monomials':6655,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','scope':'Both weighted polynomial and inverse Laurent identities; complete incidence and coordinate/row metadata; outside rows; primitive full SOS. Positivity inherited from separately accepted, exactly pinned preparation-zero439.','pins':{str(p):h for p,h in pins.items()}}
(H/'review-normalized-pole-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
