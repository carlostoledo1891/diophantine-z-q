"""Non-author checks for the frozen 06 scalar-root extension. No producer import."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm
import hashlib, json
H=Path(__file__).resolve().parent
PACK=H.parent/'06-product'/'scalar-redesign'
EXT=PACK/'root449'
DEPTH=H.parent/'10-combination'/'inputs'/'depth519.json'
REPO=H.parents[1]/'quartic-version6-release'/'repository'
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(ts): return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def v(i): return {(i,):F(1)}
def const(c): return {():F(c)} if c else {}
def add(a,b,k=1):
    d=a.copy()
    for m,q in b.items(): d[m]=d.get(m,0)+k*q
    return {m:q for m,q in d.items() if q}
def mul(a,b):
    d={}
    for m,q in a.items():
        for n,r in b.items():
            key=tuple(sorted(m+n)); d[key]=d.get(key,0)+q*r
    return {m:q for m,q in d.items() if q}
def sub(a,mp):
    d={}
    for m,q in a.items():
        term=const(q)
        for i in m: term=mul(term,mp.get(i,v(i)))
        d=add(d,term)
    return d
def norm(a):
    den=reduce(lcm,(q.denominator for q in a.values()),1)
    g=reduce(gcd,(abs(int(q*den)) for q in a.values()),0)
    return {m:q*F(den,g)*(1 if a[min(a)]>0 else -1) for m,q in a.items()}
def eq(a,b): assert norm(a)==norm(b)
old=read(PACK/'candidate450-ir.json'); new=read(EXT/'candidate449-ir.json')
assert sha(PACK/'candidate450-ir.json')=='31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6'
assert sha(EXT/'candidate449-ir.json')=='02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549'
assert sha(EXT/'REPORT.md')=='1bcd3140a837f2b7a17e28887f591fc1cbf2fe25df95bc1cb9314934265e2e9e'
o={r['name']:parse(r['terms']) for r in old['residuals']}
n={r['name']:parse(r['terms']) for r in new['residuals']}
depth=read(DEPTH); sem={k:parse(x['terms']) for k,x in depth['values'].items()}
r=sub(sem['scalar.r'],{248:add(v(248),const(1200))})
# Independently solve the physical intermediate definitions as polynomials in X^2.
mp={}
for name,i in [('scalar.rPair1.definition',487),('scalar.rFour.definition',488),('scalar.r.definition',489)]:
    row=sub(n[name],mp); coefficient=row.pop((i,))
    assert all(i not in m for m in row)
    mp[i]={m:-q/coefficient for m,q in row.items()}
beta=add({(248,):F(2)},const(2403))
want=const(1)
for factor in [beta,add(beta,const(-1)),add(beta,const(-2401)),add({m:32*q for m,q in beta.items()},const(343)),add({m:2*q for m,q in beta.items()},const(-1))]:
    want=mul(want,factor)
assert sub(r,mp)==want
# The shared quadratic slots really encode Norm(f(H))^2, without a sign change.
q=add(mul(v(140),v(140)),mul(v(141),v(141)),-2)
q2=add(mul(v(311),v(311)),mul(v(312),v(312)),-8)
eq(n['testSquare.40.0.0.definition'],add(add(mul(v(140),v(140)),mul(v(141),v(141)),2),v(311),-1))
eq(n['testSquare.40.0.1.definition'],add(mul(v(140),v(141)),v(312),-1))
assert sub(q2,{311:add(mul(v(140),v(140)),mul(v(141),v(141)),2),312:mul(v(140),v(141))})==mul(q,q)
# B=(z0^2+r*z1^2)/r^64 and the new root, exactly in physical coordinates.
eq(n['scalar.ratio1_unscaled_square.definition'],add(v(539),mul(v(509),v(509)),-1))
eq(n['scalar.ratio_node.consolidated_denominator'],add(add(mul(v(540),v(605)),mul(v(508),v(508)),-1),mul(r,v(539)),-1))
prev=r
for j,i in enumerate(range(600,606)):
    eq(n[f'scalar.r_power_{2**(j+1)}.definition'],add(v(i),mul(prev,prev),-1));prev=v(i)
eq(n['reduced_scalar.ratio_node_squared'],add(v(541),mul(v(540),v(540)),-1))
newroot=add(add(mul(r,v(542)),q2,-1),mul(r,v(541)),-1)
eq(n['reduced_scalar.root'],newroot)
eq(o['reduced_scalar.constant_node'],add(add(mul(r,v(536)),r,-1),q2,-1))
eq(o['reduced_scalar.root'],add(add(v(542),mul(v(536),v(536)),-1),mul(r,v(541)),-1))
assert set(n)==set(o)-{'reduced_scalar.constant_node'}
for name,row in n.items(): eq(row,newroot if name=='reduced_scalar.root' else o[name])
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{536}
assert {name for name,row in o.items() if any(536 in m for m in row)}=={'reduced_scalar.root','reduced_scalar.constant_node'}
assert {name for name,row in n.items() if any(542 in m for m in row)}=={'reduced_scalar.root','scalar.W2.definition'}
# Transport to the actual pole input, including its negative stored normalization.
eq(n['scalar.correctedR.definition'],add(sem['scalar.correctedR'],mul(r,v(65)),-1))
eq(n['scalar.W2.definition'],add(sem['scalar.W2'],mul(v(542),v(542)),-1))
eq(n['scalar.b.definition'],add(sem['scalar.b'],mul(sem['scalar.correctedR'],sem['scalar.W2']),-1))
K=-sem['scalar.b'][(526,)]
assert K>0
eq(n['scalar.preparationT.definition'],add(const(1),mul(v(526),v(528)),K))
# Full independent primitive residual sum of squares.
sos={}
for row in n.values():
    assert max(sum(i!=-1 for i in m) for m in row)<=2
    sos=add(sos,mul(norm(row),norm(row)))
assert sos==parse(read(EXT/'polynomial449.json')['terms'])
assert (len(new['coordinates']),len(n),len(sos))==(449,426,6582)
assert new['fixedParameter']==old['fixedParameter']
assert {i for m in sos for i in m if i!=-1}=={c['id'] for c in new['coordinates']}
paths=[PACK/'candidate450-ir.json',EXT/'candidate449-ir.json',EXT/'polynomial449.json',EXT/'REPORT.md',EXT/'verify.py',DEPTH,REPO/'manuscripts'/'quartic_v12.tex']
out={'passed':True,'scope':'Independent r polynomial, norm-square, B denominator, changed and unchanged rows, root incidence, semantic pole input and guard, full primitive SOS. Arithmetic acceptance is in review-scalar-root.md.',
     'variables':449,'residuals':426,'monomials':6582,'semanticPoleInput':'c*r*W^2 = -K*v526','K':str(K),
     'sourceSha256':{str(p):sha(p) for p in paths}}
(H/'review-scalar-root-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
