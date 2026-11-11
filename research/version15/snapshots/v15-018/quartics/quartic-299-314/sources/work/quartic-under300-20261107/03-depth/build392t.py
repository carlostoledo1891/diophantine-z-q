"""Candidate: Kummer H/V0 with an affine slope change and algebraic f!=0."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib,copy
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'quartic-under400-20261107/10-combination/combined394-ir.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5'
def add(*ps):
    out={}
    for p in ps:
        for m,a in p.items():out[m]=out.get(m,F(0))+a
    return {m:a for m,a in out.items() if a}
def sc(p,k):return {m:a*k for m,a in p.items() if a*k}
def mul(p,q):
    out={}
    for m,a in p.items():
        for n,b in q.items():
            k=tuple(sorted(m+n));out[k]=out.get(k,F(0))+a*b
    return {m:a for m,a in out.items() if a}
def v(i):return {(i,):F(1)}
def c(a):return {():F(a)} if a else {}
def fc(a,b=0):return c(a),c(b)
def pair(i):return v(i),v(i+1)
def fa(p,q,k=1):return tuple(add(a,sc(b,k)) for a,b in zip(p,q))
def fm(p,q):return add(mul(p[0],q[0]),sc(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0]))
def pol(r):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in r['terms']}
def terms(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(a)} for m,a in sorted(p.items())]
def primitive(p):
    den=reduce(lcm,(a.denominator for a in p.values()),1);g=reduce(gcd,(abs(int(a*den)) for a in p.values()),0)
    return sc(p,F(den,g)*(1 if p[min(p)]>0 else -1))
def substitute(p,mapping):
    out={}
    for mon,coef in p.items():
        term={():coef}
        for i in mon:term=mul(term,mapping.get(i,v(i)))
        out=add(out,term)
    return out
old=json.loads(SOURCE.read_text());new=copy.deepcopy(old)
oldrows={r['name']:r for r in old['residuals']}
uses={r['name'] for r in old['residuals'] if any(set(t['monomial'])&{90,91} for t in r['terms'])}
assert uses=={n+str(j) for n in ['H.chart.equation.','U0.f.definition.','V0.reciprocal.g.definition.'] for j in [0,1]}
a=fc(-1,F(7,4));b=fc(F(39,8),F(-9,2));cc=fm(a,a);D=fc(11,-6)
f=pair(140);FF=pair(160);s=pair(142);vv=pair(700)
K=fa(fa(fa(fm(cc,fa(f,FF)),fm(D,fm(vv,vv))),fm(fc(2),fm(b,vv))),fc(1),-1)
A=fa(vv,fm(f,s),-1)
E=fa(FF,fm(vv,s),-1)
ainv=fc(F(8,41),F(14,41));Sback=fm(ainv,fa(fa(b,fm(cc,s)),fm(D,vv)))
mapping={142:Sback[0],143:Sback[1]}
new['residuals']=[r for r in new['residuals'] if not r['name'].startswith('U0.f.definition.')]
for row in new['residuals']:
    row['terms']=terms(substitute(pol(row),mapping))
    for j in [0,1]:
        if row['name']=='H.chart.equation.'+str(j):row['name']='H.kummer.curve.'+str(j);row['terms']=terms(K[j])
        if row['name']=='V0.reciprocal.g.definition.'+str(j):row['terms']=terms(A[j])
        if row['name']=='V0.f.definition.'+str(j):row['terms']=terms(E[j])
new['coordinates']=[co for co in new['coordinates'] if co['id'] not in {90,91}]
for co in new['coordinates']:
    if co['id'] in {142,143}:co['name']='H.kummer.slopeRatio.'+str(co['id']-142)
new['status']='Research candidate: Kummer H/V0 with affine slope change. Nonzero fH follows algebraically. Independent review pending.'
total={}
for row in new['residuals']:
    p=primitive(pol(row));assert max(sum(i>=0 for i in m) for m in p)<=2
    total=add(total,mul(p,p))
assert {i for m in total for i in m if i>=0}=={co['id'] for co in new['coordinates']}
assert len(new['coordinates'])==392 and len(new['residuals'])==362
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert [(m,z) for m,z in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),F(16))]
assert max(abs(z.numerator).bit_length() for m,z in total.items() if -1 not in m)<2048
assert max(abs(z) for m,z in total.items() if m.count(-1)==1)<=96
def write(name,obj):
    raw=(json.dumps(obj,indent=2)+'\n').encode();(HERE/name).write_bytes(raw);return hashlib.sha256(raw).hexdigest()
ch=write('candidate392t-ir.json',new);ph=write('polynomial392t.json',{'terms':terms(total)})
result={'sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'candidateSha256':ch,'polynomialSha256':ph,'variables':392,'witnesses':391,'residuals':362,'monomials':len(total),'degree':4,'maximumCoefficient':'16*3^(2^26)','removedCoordinates':[90,91],'sourceIncidence':sorted(uses),'arithmeticReview':'pending'}
write('CERTIFICATE392t.json',result);print(json.dumps(result,indent=2))
