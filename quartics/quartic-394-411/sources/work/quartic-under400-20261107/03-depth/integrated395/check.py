"""Non-author full transport, shared-interface and coefficient audit of frozen395.
No producer/verifier imports. All writes stay beside this file.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
from copy import deepcopy
import json,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
BASE=ROOT/'10-combination'
pins={}
def load(path,expected=None):
    path=Path(path); data=path.read_bytes(); h=hashlib.sha256(data).hexdigest()
    if expected:assert h==expected,(str(path),h)
    pins[str(path.relative_to(ROOT))]=h
    return json.loads(data)
def rows(d):return {r['name']:r for r in d['residuals']}
def coords(d):return {c['id']:c for c in d['coordinates']}
def pol(obj):
    terms=obj['terms'] if isinstance(obj,dict) else obj
    p={}
    for t in terms:
        k=(t.get('sPower',0),tuple(t['monomial']));assert k[1]==tuple(sorted(k[1]))
        p[k]=p.get(k,F(0))+F(t['coefficient'])
    return {m:a for m,a in p.items() if a}
def add(*ps):
    out={}
    for p in ps:
        for m,a in p.items():out[m]=out.get(m,F(0))+a
    return {m:a for m,a in out.items() if a}
def sc(p,a):return {m:b*a for m,b in p.items() if b*a}
def mul(p,q):
    out={}
    for (s,m),a in p.items():
        for (t,n),b in q.items():
            k=s+t,tuple(sorted(m+n));out[k]=out.get(k,F(0))+a*b
    return {m:a for m,a in out.items() if a}
def v(i):return {(0,(i,)):F(1)}
def con(a):return {(0,()):F(a)} if a else {}
def power(p,n):
    out=con(1)
    for _ in range(n):out=mul(out,p)
    return out
def sub(p,mapping):
    out={}
    for (s,m),a in p.items():
        t={(s,()):a}
        for i in m:t=mul(t,mapping.get(i,v(i)))
        out=add(out,t)
    return out
def norm(p):
    den=reduce(lcm,(a.denominator for a in p.values()),1)
    g=reduce(gcd,(abs(int(a*den)) for a in p.values()),0)
    return sc(p,F(den,g)*(1 if p[min(p)]>0 else -1))
def eq(p,q):assert norm(p)==norm(q)
def vars(p):return {i for s,m in p for i in m}
def pair(i,j=None):return v(i),v(i+1 if j is None else j)
def fc(a,b=0):return con(a),con(b)
def fa(a,b,k=1):return tuple(add(x,sc(y,k)) for x,y in zip(a,b))
def fs(a,k):return tuple(sc(x,k) for x in a)
def fm(a,b):return add(mul(a[0],b[0]),sc(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def fp(a,n):
    out=fc(1)
    for _ in range(n):out=fm(out,a)
    return out
def feq(name,p,suffix=''):
    for j in range(2):eq(pol(rr[name+str(j)+suffix]),p[j])

final=load(BASE/'combined395-ir.json','440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a')
rr=rows(final);cc=coords(final)
assert len(rr)==len(final['residuals'])==len({r['id'] for r in final['residuals']})
assert len(cc)==len(final['coordinates'])
assert final['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}
assert [c['id'] for c in final['coordinates'] if c['kind']=='input']==[0]
# Derive deltas from whole component files, rather than accepting declared lists.
transport=[]
for count in [417,401,399,396,395]:
    cert=load(BASE/f'combined{count}-certificate.json')
    source=load(BASE/cert['source'],cert['sourceSha256'])
    dest=load(BASE/f'combined{count}-ir.json',cert['statistics']['candidateSha256'])
    current=deepcopy(rows(source)); currentc=deepcopy(coords(source))
    for step in cert['steps']:
        old=load(BASE/step['source'],step['sourceSha256']);new=load(BASE/step['target'],step['targetSha256'])
        review=BASE/step['review'];assert hashlib.sha256(review.read_bytes()).hexdigest()==step['reviewSha256']
        pins[str(review.relative_to(ROOT))]=step['reviewSha256']
        a,b=rows(old),rows(new);ac,bc=coords(old),coords(new)
        gone=a.keys()-b.keys();born=b.keys()-a.keys()
        changed={n for n in a.keys()&b.keys() if norm(pol(a[n]))!=norm(pol(b[n]))}
        assert not (bc.keys()-ac.keys()),'this chain requires no new coordinates'
        removed=ac.keys()-bc.keys();renamed={i for i in ac.keys()&bc.keys() if ac[i]!=bc[i]}
        for n in gone|changed:eq(pol(current[n]),pol(a[n]))
        touched=set().union(*(vars(pol(a[n])) for n in gone|changed))|set(removed)|renamed
        for i in touched:assert currentc[i]['name']==ac[i]['name']
        for n in gone:del current[n]
        for n in changed:current[n]['terms']=b[n]['terms']
        for n in born:current[n]=dict(b[n],id=step['addedRows'][n])
        for i in removed:del currentc[i]
        for i in renamed:currentc[i]=bc[i]
        assert set(currentc)==set().union(*(vars(pol(r)) for r in current.values()))
        transport.append({'step':step['step'],'removedCoordinates':sorted(removed),'changed':sorted(changed),'deleted':sorted(gone),'added':sorted(born)})
    assert currentc==coords(dest)
    assert set(current)==set(rows(dest))
    for n,r in current.items():
        assert pol(r)==pol(rows(dest)[n]),n
        assert {k:v for k,v in r.items() if k!='terms'}=={k:v for k,v in rows(dest)[n].items() if k!='terms'},n
    for key in source.keys()-{'coordinates','residuals','status'}:assert source[key]==dest[key],key

# All changed scalar definitions are bound to actual beta, not semantic names.
assert pol(rr['inputSquare.definition'])==add(power(v(0),2),sc(v(248),-1))
root=pol(rr['reduced_scalar.root'])
r={(s,tuple(i for i in m if i!=541)):-a for (s,m),a in root.items() if 541 in m}
mapping={248:power(v(0),2)}
for idx,name in [(487,'scalar.rPair1.definition'),(488,'scalar.rFour.definition'),(489,'scalar.r.definition')]:
    p=pol(rr[name]);coef=p[(0,(idx,))]
    mapping[idx]=sub(sc(add(p,sc(v(idx),-coef)),-1/coef),mapping)
beta=add(sc(power(add(sc(v(0),2),con(1)),2),51),con(2504))
raw=con(1)
for factor in [beta,add(beta,con(-1)),add(beta,con(-2401)),add(sc(beta,32),con(343)),add(sc(beta,2),con(-1))]:raw=mul(raw,factor)
assert sub(r,mapping)==raw
eq(pol(rr['scalar.r_power_2.definition']),add(v(600),sc(mul(r,r),-1)))
for n,a,b in [(4,600,601),(8,601,602),(16,602,603),(32,603,604)]:eq(pol(rr[f'scalar.r_power_{n}.definition']),add(v(b),sc(power(v(a),2),-1)))
eq(pol(rr['scalar.ratio1_unscaled_square.definition']),add(v(539),sc(power(v(509),2),-1)))
eq(pol(rr['scalar.ratio_node.consolidated_denominator']),add(mul(v(604),v(540)),sc(power(v(508),2),-1),sc(mul(r,v(539)),-1)))
eq(root,add(mul(v(604),v(542)),sc(power(v(540),2),-1),sc(mul(r,v(541)),-1)))
eq(pol(rr['testSquare.40.0.0.definition']),add(power(v(140),2),sc(power(v(141),2),2),sc(v(311),-1)))
eq(pol(rr['testSquare.40.0.1.definition']),add(mul(v(140),v(141)),sc(v(312),-1)))
eq(pol(rr['reduced_scalar.ratio_node_squared']),add(v(541),sc(power(v(311),2),-1),sc(power(v(312),2),8)))
eq(pol(rr['scalar.b.definition']),add(mul(add(v(600),sc(r,4896)),v(525)),sc(v(526),82479248)))
Wscale=pol(rr['scalar.W2.definition'])[(0,(525,))]
eq(pol(rr['scalar.W2.definition']),add(sc(v(525),Wscale),sc(power(v(542),2),-1)))
prep=rows(load(BASE/'combined396-ir.json'))
K=pol(prep['scalar.Bh.definition'])[(0,(51,531))]
assert K==82479248*Wscale and K>0

# Reconstruct the actual enlarged H and V0 field equations, including scale2.
D=fc(11,-6);a=fc(-1,F(7,4));b=fc(F(39,8),F(-9,2));c=fm(a,a)
x=(v(90),sc(v(91),2));f=pair(140);S=pair(142);vv=pair(700);fv=pair(160);R=pair(186);ell=pair(188)
feq('H.chart.equation.',fa(fa(fp(S,2),x,-1),fm(D,f)))
for j in range(2):
    expected=fa(fm(x,f),fc(1),-1)[j]
    assert any(norm(pol(row))==norm(expected) for row in rr.values())
feq('V0.f.definition.',fa(fp(vv,2),fm(fv,f),-1))
d=fa(fm(c,x),D);N=fa(fm(a,S),b,-1)
feq('V0.reciprocal.g.definition.',fa(fm(d,vv),N,-1))
T=fa(fa(fs(D,-2),fm(fm(a,b),S),-1),fs(fm(fm(D,b),vv),2))
feq('logV0.definition.',fa(fm(T,ell),fm(fm(a,N),R)))
assert not ({17,18}&set(cc))

# Derive squared-test meanings from the old literal rows, then check all
# scaled field equations directly in final395. This is in addition to transport.
oldchart=load(BASE/'inputs/identity-chart427-ir.json','6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4')
orows=rows(oldchart);oc={q['name']:q['id'] for q in oldchart['coordinates']}
def oldfield(name):return tuple(v(oc[name+str(j)]) for j in range(2))
def square_output(value,prefix):
    sq=fp(value,2);out=[]
    for j in range(2):
        p=pol(orows[prefix+str(j)+'.definition']);pivot=next(iter(sq[j]));factor=p[pivot]/sq[j][pivot]
        linear=add(sq[j],sc(p,-1/factor));assert all(len(m)<=1 for s,m in linear)
        out.append(linear)
    return tuple(out)
for idx,label in enumerate(['A','S','T','Z'],1):
    ar=oldfield(label+'.chart.h');br=oldfield(label+'.chart.j');cr=square_output(ar,label+'.chart.x.')
    V=oldfield('U'+label+'.reciprocal.r');I=oldfield('U'+label+'.reciprocal.J')
    Q=oldfield(f'V{idx}.reciprocal.g.');W=oldfield(f'V{idx}.reciprocal.u.');KK=oldfield(f'V{idx}.reciprocal.k.')
    YU=square_output(oldfield(f'U{idx}.f.'),f'testSquare.1.{idx-1}.')
    YV=square_output(oldfield(f'V{idx}.f.'),f'logV{idx}.fSquare.')
    feq(label+'.chart.equation.',fa(fa(fp(br,2),fp(cr,2),-1),D))
    feq(f'V{idx}.biquadratic.cross.',fa(fm(V,Q),fm(cr,W),-1))
    feq(f'V{idx}.biquadratic.curve.',fa(fa(fa(fa(fp(V,2),fp(Q,2)),fm(D,fp(W,2))),fs(fm(br,W),2)),fc(1),-1))
    feq(f'V{idx}.biquadratic.I.',fa(fa(fa(fm(ar,I),fm(br,V),-1),fm(cr,Q),-1),fm(D,fm(V,W)),-1))
    feq(f'V{idx}.biquadratic.K.',fa(fa(fa(fm(ar,KK),fm(br,Q)),fm(cr,V)),fm(D,fm(Q,W))))
    feq(f'L{idx}.definition.',fa(fm(I,oldfield(f'L{idx}.')),fm(V,S),-1))
    feq(f'V{idx}.z.definition.',fa(fm(KK,oldfield(f'V{idx}.z.')),Q))
    feq(f'testSquare.1.{idx-1}.',fa(fa(fm(D,fm(cr,YU)),fp(I,2)),cr,-1),'.definition')
    feq(f'logV{idx}.fSquare.',fa(fa(fm(D,fm(cr,YV)),fp(KK,2)),cr,-1),'.definition')

# Bind rational approximation to the literal final field equations.
approx=load(ROOT/'03-depth/approximation.json');num=list(map(F,approx['p']));den=list(map(F,approx['q']))
y=(v(178),sc(v(179),2));w=fm(D,y);w2=(sc(v(180),193),sc(v(181),-132));w4=pair(182)
feq('logV0.fSquare.',fa(fp(fv,2),y,-1),'.definition')
feq('logV0.wPower2.',fa(fp(w,2),w2,-1),'.definition')
feq('logV0.wPower4.',fa(fp(w2,2),w4,-1),'.definition')
powers={0:fc(1),1:w,2:w2,3:fm(w,w2),4:w4,5:fm(w,w4),6:fm(w2,w4),8:fp(w4,2)}
nn=fc(0);qq=fc(0)
for k,t in enumerate(num):
    if t:nn=fa(nn,fs(powers[k],t))
for k,t in enumerate(den):qq=fa(qq,fs(powers[k],t))
feq('logV0.rationalApproximation.',fa(fm(qq,R),nn,-1),'.definition')
for coefficients,p,roots in [(num,71,[12,59]),(den,7,[3,4])]:
    assert all(z*z%p==2 for z in roots)
    assert all(t.denominator%p for t in coefficients) and coefficients[-1].numerator%p
    residues=[sum(t.numerator*pow(t.denominator,-1,p)*pow(z,k,p) for k,t in enumerate(coefficients))%p for z in range(p)]
    assert all(residues)

# Normalization is an exact equivalence for x526 !=0, including zero privates.
weights={51:1,52:1,53:1,54:1,532:1,527:2,534:2}
pm={i:mul(v(i),power(v(526),n)) for i,n in weights.items()};pm[531]=power(v(526),2)
pole={'scalar.p2.definition','scalar.firstConic','scalar.Bh.definition','scalar.q2.definition','scalar.secondConic'}
for name in pole:assert sub(pol(prep[name]),pm)==mul(power(v(526),2),pol(rr[name])),name
assert sub(pol(prep['scalar.t2.definition']),pm)=={}
for name,row in prep.items():
    if name not in pole|{'scalar.t2.definition'}:assert not (vars(pol(row))&(set(weights)|{531}))

# Complete final primitive sum of squares, without materializing the fixed C.
total={}
for row in rr.values():
    p=norm(pol(row));assert max(len(m) for s,m in p)<=2
    total=add(total,mul(p,p))
assert total==pol(load(BASE/'combined395-polynomial.json','3d7c165ffb4171fe3dc11559b1a2bb29ff24dcb02289303d4544e8c5a5667d85'))
assert (len(cc),len(rr),len(total))==(395,365,6341)
assert vars(total)==set(cc) and max(len(m) for s,m in total)==4
assert {(s,m):a for (s,m),a in total.items() if s==2}=={(2,(57,57)):F(16)}
assert (0,(57,57)) not in total and (1,(57,57)) not in total
assert max(abs(a.numerator).bit_length() for (s,m),a in total.items() if s==0)<2048
assert max(abs(a) for (s,m),a in total.items() if s==1)<=48
assert any(s==0 and a==1 for (s,m),a in total.items())
assert F(5,24)*F(50331647,2)>2093966+7
result={'passed':True,'variables':395,'residuals':365,'monomials':6341,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','pins':pins,'transport':transport,'interfaces':['actual beta and scalar r','five scalar powers and two root equations','actual norm square','b sign and exact scale','enlarged H / V0 / ell0','four scaled charts with derived actual squared outputs','actual rational numerator and denominator, no K-roots','normalized pole all five identities and full incidence','every final SOS coefficient']}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'pins','transport'}},indent=2))
