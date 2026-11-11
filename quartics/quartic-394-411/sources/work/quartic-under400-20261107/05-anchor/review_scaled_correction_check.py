"""Independent exact maps and SOS check for the frozen scaled-correction446."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
BASE=H.parent/'06-product'/'scalar-redesign'
EXT=BASE/'scaled-correction446'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def v(i):return {(i,):F(1)}
def c(q):return {():F(q)} if q else {}
def add(a,b,k=1):
    d=a.copy()
    for m,q in b.items():d[m]=d.get(m,0)+k*q
    return {m:q for m,q in d.items() if q}
def scale(a,q):return {m:x*q for m,x in a.items() if x*q}
def mul(a,b):
    d={}
    for m,q in a.items():
        for n,r in b.items():
            k=tuple(sorted(m+n));d[k]=d.get(k,0)+q*r
    return {m:q for m,q in d.items() if q}
def sub(a,mp):
    d={}
    for m,q in a.items():
        t=c(q)
        for i in m:t=mul(t,mp.get(i,v(i)))
        d=add(d,t)
    return d
def norm(a):
    den=reduce(lcm,(q.denominator for q in a.values()),1)
    g=reduce(gcd,(abs(int(q*den)) for q in a.values()),0)
    return scale(a,F(den,g)*(1 if a[min(a)]>0 else -1))
S=BASE/'odd-input447'/'candidate447-ir.json'
assert sha(S)=='20e9732f0ce5b493190d4c876fdc1a5c6838627145a72f7ee2bec7e548810189'
assert sha(EXT/'candidate446-ir.json')=='20699504b0998782752f49e5b2c5ddcadea2f88b073db49418c38f0b55317f8b'
assert sha(EXT/'REPORT.md')=='cb6196998bd96d901ff4b75d9e1d8e3d78c4e6bf8c045e85d8fcbc3898090dff'
old=read(S);new=read(EXT/'candidate446-ir.json')
o={r['name']:parse(r['terms']) for r in old['residuals']};n={r['name']:parse(r['terms']) for r in new['residuals']}
prod=o['scalar.correctedR.definition']
assert prod[(524,)]==-20619812
s0={tuple(i for i in m if i!=65):q for m,q in prod.items() if 65 in m}
assert prod==add(mul(v(65),s0),v(524),-20619812)
r=scale(add(s0,c(7895415)),-4)
# Raw contact identity, independently recovering the intermediate coordinates.
mp={}
for name,i in [('scalar.rPair1.definition',487),('scalar.rFour.definition',488),('scalar.r.definition',489)]:
    p=sub(o[name],mp);q=p.pop((i,));assert all(i not in m for m in p)
    mp[i]=scale(p,-1/q)
beta=add(add(scale(v(248),4),scale(v(0),4)),c(2403))
expected=c(1)
for factor in [beta,add(beta,c(-1)),add(beta,c(-2401)),add(scale(beta,32),c(343)),add(scale(beta,2),c(-1))]:expected=mul(expected,factor)
assert sub(r,mp)==expected
assert norm(o['inputSquare.definition'])==norm(add(mul(v(0),v(0)),v(248),-1))
# beta=(2X+1)^2+2402 after using the literal input-square equation.
assert sub(beta,{248:mul(v(0),v(0))})==add(mul(add(scale(v(0),2),c(1)),add(scale(v(0),2),c(1))),c(2402))
first=mul(add(v(62),r,-1),add(v(62),r,-33))
out=add(mul(v(65),v(525)),v(526),82479248)
assert set(n)==set(o)-{'scalar.correctedR.definition'}
for name,row in n.items():
    want=first if name=='correction.oddInputProduct1' else out if name=='scalar.b.definition' else o[name]
    assert norm(row)==norm(want),name
forward={i:mul(r,v(i)) for i in [62,63,64,65]}
for i,g in enumerate([33,17,105,273],1):
    name=f'correction.oddInputProduct{i}'
    prev=c(1) if i==1 else v(60+i)
    assert o[name]==mul(add(v(61+i),prev,-1),add(v(61+i),prev,-g))
    assert sub(n[name],forward)==mul(mul(r,r),o[name])
assert sub(out,forward)==scale(add(o['scalar.b.definition'],mul(v(525),prod)),-4)
# Clear r from the reverse c=C/r,F=-(C+31581660*c)/82479248 map.
reverse_scaled_F=scale(mul(v(65),add(r,c(31581660))),F(-1,82479248))
assert add(mul(v(65),s0),reverse_scaled_F,-20619812)=={}
reverse_old_b=add(add(scale(mul(v(65),v(525)),7895415),scale(mul(reverse_scaled_F,v(525)),20619812)),scale(mul(r,v(526)),-20619812))
assert reverse_old_b==scale(mul(r,out),F(-1,4))
assert {name for name,row in o.items() if any(524 in m for m in row)}=={'scalar.correctedR.definition','scalar.b.definition'}
assert {name for name,row in o.items() if any(set(m)&{62,63,64,65} for m in row)}=={'scalar.correctedR.definition','scalar.b.definition'}|{f'correction.oddInputProduct{i}' for i in range(1,5)}
oc={x['id']:x for x in old['coordinates']};nc={x['id']:x for x in new['coordinates']}
assert set(nc)==set(oc)-{524}
for i,x in nc.items():
    y=oc[i].copy()
    if i in forward:y['name']=f'correction.scaledProduct{i-61}'
    assert x==y
for k in old:
    if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
sos={}
for row in n.values():
    assert max(sum(i!=-1 for i in m) for m in row)<=2
    p=norm(row);sos=add(sos,mul(p,p))
assert sos==parse(read(EXT/'polynomial446.json')['terms'])
assert (len(nc),len(n),len(sos))==(446,423,6730)
assert max(sum(i!=-1 for i in m) for m in sos)==4
assert any(-1 not in m and abs(q)==1 for m,q in sos.items())
assert {m:q for m,q in sos.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
assert max(abs(q.numerator).bit_length() for m,q in sos.items() if m.count(-1)<2)<2048
assert {i for m in sos for i in m if i!=-1}==set(nc)
paths=[S,EXT/'REPORT.md',EXT/'candidate446-ir.json',EXT/'polynomial446.json']
result={'passed':True,'variables':446,'rows':423,'monomials':6730,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)',
        'scope':'Raw positive contact polynomial, exact forward and reverse maps, full incidence and all outside rows/coordinates, full primitive SOS. No approval of an unseen single-correction packet.',
        'sourceSha256':{str(p):sha(p) for p in paths}}
(H/'review-scaled-correction-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
