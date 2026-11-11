"""Independent exact395 ->394 anchor composition and complete SOS audit."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent;ROOT=H.parents[1];B=ROOT/'10-combination'
def load(p,h):
    raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==h
    return json.loads(raw)
old=load(B/'combined395-ir.json','440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a')
new=load(B/'combined394-ir.json','7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5')
assert hashlib.sha256((ROOT/'01-elimination/review398/REVIEW.md').read_bytes()).hexdigest()=='0e7082164559fa84f38435b188ea3eaa673e7c2ccca5666a21adedcccdf9f1be'
def add(*ps):
    d={}
    for p in ps:
        for m,c in p.items():d[m]=d.get(m,F(0))+c
    return {m:c for m,c in d.items() if c}
def scale(p,c):return {m:a*c for m,a in p.items() if a*c}
def mul(p,q):
    d={}
    for m,c in p.items():
        for n,a in q.items():
            k=tuple(sorted(m+n));d[k]=d.get(k,F(0))+c*a
    return {m:c for m,c in d.items() if c}
def pol(r):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in r['terms']}
def primitive(p):
    d=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*d)) for c in p.values()),0)
    return scale(p,F(d,g)*(1 if p[min(p)]>0 else -1))
def v(i):return {(i,):F(1)}
def c(a):return {():F(a)}
def sub(p,mp):
    out={}
    for m,a in p.items():
        term=c(a)
        for i in m:term=mul(term,mp.get(i,v(i)))
        out=add(out,term)
    return out
def pair(i,j=None):return v(i),v(i+1 if j is None else j)
def fc(a,b=0):return c(a),c(b)
def fa(p,q,k=1):return tuple(add(a,scale(b,k)) for a,b in zip(p,q))
def fm(p,q):return add(mul(p[0],q[0]),scale(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0]))
oo={r['name']:r for r in old['residuals']};nn={r['name']:r for r in new['residuals']}
oc={r['id']:r for r in old['coordinates']};nc={r['id']:r for r in new['coordinates']}
assert len(nn)==len(new['residuals'])==len({r['id'] for r in new['residuals']})==364
assert len(nc)==len(new['coordinates'])==394 and set(nc)==set(oc)-{505}
gone={'Sscalar.f.definition.1','scalar.shiftedS.reciprocal.f1Inverse.definition'}
born='scalar.shiftedS.reciprocal.g0Inverse.definition';anchor='anchor.translatedEquation'
assert set(nn)==set(oo)-gone|{born}
for name in set(oo)-gone-{anchor}:assert nn[name]==oo[name],name
for i in nc:
    wanted=oc[i].copy()
    if i in {55,56,57}:wanted['name']+='ScaledByG0'
    if i==549:wanted['name']='scalar.shiftedS.reciprocal.g0Inverse'
    assert nc[i]==wanted
for k in old.keys()-{'coordinates','residuals','status'}:assert old[k]==new[k]
uses={i:sorted(name for name,row in oo.items() if any(i in t['monomial'] for t in row['terms'])) for i in [55,56,57,505,549]}
assert uses=={55:[anchor],56:[anchor],57:[anchor],505:sorted(gone|{anchor}),549:['scalar.shiftedS.reciprocal.f1Inverse.definition']}
qold={(55,55):F(1),(56,56):F(6),(57,57):F(-2),(505,505):F(-3),(-1,57):F(-4)}
qnew={(55,55):F(1),(56,56):F(6),(57,57):F(-2),(544,544):F(-12),(-1,57,549):F(-4)}
guard={(543,549):F(1),():F(-1)}
assert pol(oo[anchor])==qold and pol(nn[anchor])==qnew and pol(nn[born])==guard
assert pol(oo['Sscalar.f.definition.1'])=={(505,):F(1),(543,544):F(-2)}
assert pol(oo['scalar.shiftedS.reciprocal.f1Inverse.definition'])=={(505,549):F(1),():F(-1)}
mp={55:mul(v(543),v(55)),56:mul(v(543),v(56)),57:mul(v(543),v(57)),505:scale(mul(v(543),v(544)),2)}
assert add(sub(qold,mp),scale(mul(mul(v(543),v(543)),qnew),-1))==mul({(-1,57,543):F(4)},guard)
# Actual unchanged scalar source, including x's physical factor2.
a=fc(-1,F(7,4));b=fc(F(39,8),F(-9,2));cc=fm(a,a);D=fc(11,-6)
h=pair(5);j=pair(7);x=v(84),scale(v(85),2);g=pair(543)
for prefix,expected,suffix in [('S.chart.x.',fa(fm(h,h),x,-1),'.definition'),('S.chart.equation.',fa(fa(fm(j,j),fm(x,x),-1),D),''),('scalar.shiftedS.reciprocal.g.definition.',fa(fm(fa(fm(cc,x),D),g),fa(fm(a,j),fm(b,h),-1),-1),'')]:
    for n in range(2):assert primitive(pol(nn[prefix+str(n)+suffix]))==primitive(expected[n])
# Starting residue in the unconditional nonzero-even coefficient lemma.
mod=lambda z:z.numerator*pow(z.denominator,-1,3)%3
assert [mod(F(3396356159088,3287811625151)/3),mod(F(-4135204317756,3287811625151)/3)]==[2,1]
assert (2*2+2)%3==0 and (2*2)%3==1
total={}
for row in nn.values():
    p=primitive(pol(row));assert max(sum(i>=0 for i in m) for m in p)<=2
    total=add(total,mul(p,p))
assert total==pol(load(B/'combined394-polynomial.json','39e1f5c05a1a26be26b006703bccc2e1c23b8a15876fbd6d43749d5d464d3193'))
assert len(total)==6338 and len({tuple(i for i in m if i>=0) for m in total})==6338
assert {i for m in total for i in m if i>=0}==set(nc)
assert max(sum(i>=0 for i in m) for m in total)==4
assert all(z.denominator==1 for z in total.values()) and reduce(gcd,(abs(z.numerator) for z in total.values()))==1
assert [(m,z) for m,z in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),F(16))]
assert (57,57,549,549) not in total and (-1,57,57,549,549) not in total
bits=max(abs(z.numerator).bit_length() for m,z in total.items() if -1 not in m)
linear=max(abs(z) for m,z in total.items() if m.count(-1)==1)
assert bits<2048 and linear<=96
result={'passed':True,'candidateSha256':'7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5','variables':394,'residuals':364,'monomials':6338,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','largestCLinearMultiplier':str(linear),'constantBitBound':bits,'privateIncidence':uses,'allOutsideObjectsPreserved':True,'scalarSourceEquationsChecked':True,'fullSOS':True}
(H/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
