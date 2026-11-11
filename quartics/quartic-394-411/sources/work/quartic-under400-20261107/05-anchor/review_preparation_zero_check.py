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
S=BASE/'deterministic442'/'candidate442-ir.json'
assert sha(S)=='e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86'
assert sha(E/'REPORT.md')=='918d33e53edbd7d481ad5fe97a7d369eb6f1e3cec01c36a4dca0a043bb83363a'
assert sha(E/'candidate439-ir.json')=='135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3'
old=read(S);new=read(E/'candidate439-ir.json')
o={r['name']:parse(r['terms']) for r in old['residuals']};n={r['name']:parse(r['terms']) for r in new['residuals']}
K=o['scalar.preparationT.definition'][(526,528)]
assert K>0
assert o['scalar.preparationT.definition']==add(c(1),mul(v(526),v(528)),K)
assert o['scalar.t2.definition']==add(mul(v(50),v(50)),v(531),-K*K)
assert o['scalar.UplusB.definition']==add(add(sc(v(526),K),mul(v(528),v(531)),K*K),mul(v(529),v(529)))
newrow=add(v(531),mul(v(526),v(526)),-1)
assert set(n)==set(o)-{'scalar.preparationT.definition','scalar.UplusB.definition'}
for name,row in n.items():assert norm(row)==norm(newrow if name=='scalar.t2.definition' else o[name])
assert {name for name,row in o.items() if any(set(m)&{50,528,529} for m in row)}=={'scalar.t2.definition','scalar.preparationT.definition','scalar.UplusB.definition'}
mp={50:sc(v(526),-K),531:mul(v(526),v(526)),529:{}}
assert sub(o['scalar.t2.definition'],mp)=={}
assert sub(o['scalar.UplusB.definition'],mp)==mul(sc(v(526),K),o['scalar.preparationT.definition'])
# Actual b=-K*v526 remains c*r*W² and is strictly positive globally.
r=parse(read(BASE/'deterministic442'/'CERTIFICATE.json')['rTerms'])
vals={}
for name,i in [('scalar.rPair1.definition',487),('scalar.rFour.definition',488),('scalar.r.definition',489)]:
 row=sub(n[name],vals);q=row.pop((i,));assert all(i not in m for m in row);vals[i]=sc(row,-1/q)
beta=add(add(sc(v(248),204),sc(v(0),204)),c(2555));want=c(1)
for f in [beta,add(beta,c(-1)),add(beta,c(-2401)),add(sc(beta,32),c(343)),add(sc(beta,2),c(-1))]:want=mul(want,f)
assert sub(r,vals)==want
assert norm(n['inputSquare.definition'])==norm(add(mul(v(0),v(0)),v(248),-1))
assert sub(beta,{248:mul(v(0),v(0))})==add(sc(mul(add(sc(v(0),2),c(1)),add(sc(v(0),2),c(1))),51),c(2504))
assert norm(n['scalar.r_power_2.definition'])==norm(add(v(600),mul(r,r),-1))
assert norm(n['scalar.b.definition'])==norm(add(mul(add(v(600),r,4896),v(525)),v(526),82479248))
L=n['scalar.W2.definition'][(525,)]
assert n['scalar.W2.definition']==add(sc(v(525),L),mul(v(542),v(542)),-1)
assert K==82479248*L
assert norm(n['reduced_scalar.root'])==norm(add(add(mul(v(604),v(542)),mul(v(540),v(540)),-1),mul(r,v(541)),-1))
assert norm(n['reduced_scalar.ratio_node_squared'])==norm(add(add(v(541),mul(v(311),v(311)),-1),mul(v(312),v(312)),8))
# Finite congruence exhaustions over complete residue sets, not input sampling.
def contact(t,mod):
 b=(51*t*t+2504)%mod
 return b*(b-1)*(b-2401)*(32*b+343)*(2*b-1)%mod
assert {contact(t,32) for t in range(1,32,2)}=={4}
assert {contact(t,9) for t in range(9)}<={3,6}
assert {contact(t,17) for t in range(17)}=={15}
assert 4896%32==0 and 4896%9==0 and 4896%17==0
# Source records and the whole polynomial.
oc={x['id']:x for x in old['coordinates']};nc={x['id']:x for x in new['coordinates']}
assert nc=={i:x for i,x in oc.items() if i not in {50,528,529}}
for k in old:
 if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
sos={}
for row in n.values():
 q=norm(row);assert max(sum(i!=-1 for i in m) for m in q)<=2;sos=add(sos,mul(q,q))
assert sos==parse(read(E/'polynomial439.json')['terms'])
assert (len(nc),len(n),len(sos))==(439,417,6658)
assert {i for m in sos for i in m if i!=-1}==set(nc)
assert any(-1 not in m and abs(q)==1 for m,q in sos.items())
assert {m:q for m,q in sos.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
assert max(abs(q.numerator).bit_length() for m,q in sos.items() if m.count(-1)<2)<2048
pins=read(E/'SOURCE-PINS.json');assert sha(REPO/pins['repoRelativePath'])==pins['sha256']
paths=[S,E/'REPORT.md',E/'candidate439-ir.json',E/'polynomial439.json',E/'SOURCE-PINS.json',REPO/pins['repoRelativePath']]
result={'passed':True,'variables':439,'rows':417,'monomials':6658,'K':str(K),'reverse':'U=-K*v526=b; J=1/b; V=0',
 'scope':'Independent exact pole normalization and reverse lift, global positive b formula, raw input/contact polynomial, complete local residue classes, full outside-coordinate/incidence/SOS checks. Simultaneous real/local proof reviewed in separate report.',
 'sourceSha256':{str(p):sha(p) for p in paths}}
(H/'review-preparation-zero-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
