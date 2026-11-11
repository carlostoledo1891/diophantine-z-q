"""Author's exact algebra/consumer check; not independent mathematical approval."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
def load(p,h=None):
    raw=p.read_bytes()
    if h:assert hashlib.sha256(raw).hexdigest()==h
    return json.loads(raw)
old=load(ROOT/'quartic-under400-20261107/10-combination/combined394-ir.json','7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5')
new=load(H/'candidate392t-ir.json','846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba')
def add(*ps):
    d={}
    for p in ps:
        for m,c in p.items():d[m]=d.get(m,F(0))+c
    return {m:c for m,c in d.items() if c}
def sc(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
    d={}
    for m,a in p.items():
        for n,b in q.items():
            k=tuple(sorted(m+n));d[k]=d.get(k,F(0))+a*b
    return {m:c for m,c in d.items() if c}
def v(i):return {(i,):F(1)}
def c(a):return {():F(a)} if a else {}
def sq(p):return mul(p,p)
def pol(r):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in r['terms']}
def norm(p):
    den=reduce(lcm,(a.denominator for a in p.values()),1);g=reduce(gcd,(abs(int(a*den)) for a in p.values()),0)
    return sc(p,F(den,g)*(1 if p[min(p)]>0 else -1))
def fc(a,b=0):return c(a),c(b)
def pair(i):return v(i),v(i+1)
def fa(p,q,k=1):return tuple(add(a,sc(b,k)) for a,b in zip(p,q))
def fm(p,q):return add(mul(p[0],q[0]),sc(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0]))
def fs(p,k):return tuple(sc(a,k) for a in p)
def substitute(p,mp):
    out={}
    for m,a in p.items():
        t=c(a)
        for i in m:t=mul(t,mp.get(i,v(i)))
        out=add(out,t)
    return out
oo={r['name']:r for r in old['residuals']};nn={r['name']:r for r in new['residuals']}
deleted={f'U0.f.definition.{i}' for i in [0,1]}|{f'H.chart.equation.{i}' for i in [0,1]}
added={f'H.kummer.curve.{i}' for i in [0,1]}
changed={f'{name}.{i}' for name in ['V0.reciprocal.g.definition','V0.f.definition'] for i in [0,1]}
assert set(nn)==set(oo)-deleted|added
for name in changed:assert {k:v for k,v in oo[name].items() if k!='terms'}=={k:v for k,v in nn[name].items() if k!='terms'}
expectedcoords=[dict(q,name='H.kummer.slopeRatio.'+str(q['id']-142)) if q['id'] in {142,143} else q for q in old['coordinates'] if q['id'] not in {90,91}]
assert new['coordinates']==expectedcoords
for key in old.keys()-{'coordinates','residuals','status'}:assert old[key]==new[key]
assert {name for name,row in oo.items() if any(set(t['monomial'])&{90,91} for t in row['terms'])}==deleted|{f'V0.reciprocal.g.definition.{i}' for i in [0,1]}
assert all(not set(t['monomial'])&{90,91} for row in nn.values() for t in row['terms'])
a=fc(-1,F(7,4));b=fc(F(39,8),F(-9,2));cc=fm(a,a);DD=fc(11,-6);ff=pair(140);FF=pair(160);SS=pair(142);vv=pair(700)
K=fa(fa(fa(fm(cc,fa(ff,FF)),fm(DD,fm(vv,vv))),fs(fm(b,vv),2)),fc(1),-1)
A=fa(vv,fm(ff,SS),-1);EE=fa(FF,fm(vv,SS),-1)
ainv=fc(F(8,41),F(14,41));Sback=fm(ainv,fa(fa(b,fm(cc,SS)),fm(DD,vv)))
mpS={142:Sback[0],143:Sback[1]}
affineChanged=[]
for name in set(oo)-deleted-changed:
    assert pol(nn[name])==substitute(pol(oo[name]),mpS),name
    assert {k:v for k,v in oo[name].items() if k!='terms'}=={k:v for k,v in nn[name].items() if k!='terms'}
    if pol(nn[name])!=pol(oo[name]):affineChanged.append(name)
for i in [0,1]:
    assert pol(nn[f'H.kummer.curve.{i}'])==K[i]
    assert pol(nn[f'V0.reciprocal.g.definition.{i}'])==A[i]
    assert pol(nn[f'V0.f.definition.{i}'])==EE[i]
# New equations make the former E and A residuals vanish; Sback is affine.
oldA=fa(fa(fm(a,fm(ff,Sback)),fm(b,ff),-1),fm(fa(cc,fm(DD,ff)),vv),-1)
assert oldA==fs(fm(cc,A),-1)
oldE=fa(fm(vv,vv),fm(ff,FF),-1)
assert oldE==fa(fm(vv,A),fm(ff,EE),-1)
# Unconditional recovery identity in independent scalar indeterminates.
aa,bb,dd,f,Fv,s,t=[v(i) for i in range(1001,1008)]
cc0=sq(aa);d=add(cc0,mul(dd,f));B=add(mul(bb,f),mul(d,t))
E=add(sq(t),sc(mul(f,Fv),-1));KK=add(mul(cc0,add(f,Fv)),mul(dd,sq(t)),sc(mul(bb,t),2),c(-1))
AA=add(mul(aa,mul(f,s)),sc(B,-1));HH=add(mul(f,sq(s)),mul(dd,sq(f)),c(-1));root=add(sq(bb),sc(sq(cc0),-1),dd)
rhs=add(mul(mul(f,d),KK),mul(mul(cc0,d),E),mul(root,sq(f)),mul(AA,add(mul(aa,mul(f,s)),B)))
assert mul(mul(cc0,f),HH)==rhs
# Actual order-one leaf u=conjugate(fV0)^2 belongs to group0 in all3 detectors.
u=(v(178),sc(v(179),-2));p=(v(255),sc(v(256),2));q=(v(257),sc(v(258),2))
C1=fa(fa(u,p),q);C2=fa(fm(u,fa(p,q)),fm(p,q))
co2=[nn['hybrid.1.group0.co2.0.definition'],nn['hybrid.1.group0.right.co2.1.definition']]
for j in [0,1]:assert norm(pol(co2[j]))==norm(add(v(608+j),sc(C2[j],-1)))
# Verify the optimized cubic coefficient from the true F-square and w-square.
fv=pair(160);fsq=fm(fv,fv);w=fm(DD,fsq);w2=fm(w,w)
mp={178:fsq[0],179:sc(fsq[1],F(1,2)),180:sc(w2[0],F(1,193)),181:sc(w2[1],F(-1,132))}
mp[608]=substitute(C2[0],mp);mp[609]=substitute(C2[1],mp)
expected3=fm(fm(u,p),q)
for j in [0,1]:
    row=pol(nn[f'hybrid.1.group0.co3.{j}.definition'])
    assert substitute(row,mp)==add(v(610+j),sc(substitute(expected3[j],mp),-1))
for det,qid,q2,q3,eid in [(0,352,361,362,634),(1,400,409,410,654),(2,448,457,458,674)]:
    for j in [0,1]:
        want=add(v(eid+j),sc(c(1) if j==0 else {},-1),sc(mul(C1[j],v(qid)),-1),sc(mul(v(608+j),v(q2)),-1),sc(mul(v(610+j),v(q3)),-1))
        assert pol(nn[f'hybrid.det{det}.eval1.0.{j}.definition'])==want
total={}
for row in nn.values():
    p0=norm(pol(row));assert max(sum(i>=0 for i in m) for m in p0)<=2
    total=add(total,mul(p0,p0))
assert total==pol(load(H/'polynomial392t.json','46d54b4c183911e195f56dda232a565d88fe5b2a6df56f591efedab56c15f26f'))
assert len(total)==6843 and len(nn)==362 and len(new['coordinates'])==392
assert [(m,z) for m,z in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),F(16))]
result={'passed':True,'genericRecoveryIdentity':True,'allOutsideObjectsPreservedUnderAffineSubstitution':True,'affineChangedRows':sorted(affineChanged),'actualConjugateFV0SquareInAllThreeDetectors':True,'fullSOS':True,'variables':392,'residuals':362,'monomials':6843,'independentAcceptance':False}
(H/'VERIFICATION392t.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
