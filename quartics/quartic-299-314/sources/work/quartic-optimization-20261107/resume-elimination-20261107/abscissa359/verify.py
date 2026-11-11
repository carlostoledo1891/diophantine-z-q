"""Producer-free finite identities, complete consumers/signs and full SOS for359."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;ROOT=H.parents[3]
def load(path,pin):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==pin,str(path)
    return json.loads(path.read_text())
old=load(ROOT/'work/quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json','0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56')
new=load(H/'candidate359-ir.json','282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1')
table=load(H/'polynomial359.json','a48baf563cfb8b490fdab230dd60079067d7f19f0185ef13bfca22548882af3d')
drop={66,67,68,74,75,76,78,79,80};gone={687,688,689,693,694,695,696,697,698}
rr={r['id']:r for r in new['residuals']};oo={r['id']:r for r in old['residuals']}
assert set(rr)==set(oo)-gone|{903,904}
assert all(rr[i]==oo[i] for i in set(oo)-gone-{504})
assert [c for c in new['coordinates'] if c['id']<900]==[c for c in old['coordinates'] if c['id'] not in drop]
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-drop|{903,904}
assert {r['id'] for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms'])}==gone
for key in old:
    if key not in ('coordinates','residuals','status'):assert new[key]==old[key]
assert new['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}

def clean(p):return {m:c for m,c in p.items() if c}
def add(*ps):
    out=defaultdict(F)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return clean(out)
def sc(p,c):return clean({m:c*v for m,v in p.items()})
def sub(p,q):return add(p,sc(q,-1))
def mul(*ps):
    out={():F(1)}
    for p in ps:
        temp=defaultdict(F)
        for m,c in out.items():
            for n,d in p.items():temp[tuple(sorted(m+n))]+=c*d
        out=clean(temp)
    return out
def sq(p):return mul(p,p)
def v(i):return {(i,):F(1)}
def const(c):return {():F(c)} if c else {}
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}

# Actual retained x=h^2 rows fix every physical rho normalization.
for rowid,h0,h1,x0,x1,scale in [(0,1,2,82,83,1),(16,9,10,86,87,2),(24,13,14,88,89,1)]:
    assert dec(rr[rowid])==add(sq(v(h0)),sc(sq(v(h1)),2),sc(v(x0),-scale))
    assert dec(rr[rowid+1])==sub(mul(v(h0),v(h1)),v(x1))
# The physical rho coefficients are twice slots83,87,89.
assert dec(rr[903])==add(v(903),sc(sq(v(83)),-48),sc(sq(v(87)),-48),sc(sq(v(89)),-432))
assert dec(rr[904])==add(v(904),sc(v(544),-2),sc(mul(v(-1),v(903),v(549)),-1))
assert dec(rr[504])==add(dec(oo[504]),sc(sq(v(544)),12),sc(sq(v(904)),-3))
U,V,W,g0,g1,tau,C,Q,B=map(v,[55,56,57,543,544,549,-1,903,904])
guard=sub(mul(g0,tau),const(1));assert guard==dec(rr[732])
qform=add(sq(mul(g0,U)),sc(sq(mul(g0,V)),6),sc(sq(mul(g0,W)),-2),
          sc(mul(C,g0,W),-4),sc(sq(mul(g0,B)),-3))
assert sub(qform,mul(sq(g0),dec(rr[504])))==sc(mul(C,g0,W,guard),4)
assert sub(mul(g0,B),add(sc(mul(g0,g1),2),mul(C,Q)))==add(mul(g0,dec(rr[904])),mul(C,Q,guard))

# Verify every source half-abscissa row in the actual physical normalization.
for h0,h1,j0,j1,x0,x1,scale,a0,a1,norm,row0 in (
    (1,2,3,4,82,83,1,66,67,68,687),(9,10,11,12,86,87,2,74,75,76,693),
    (13,14,15,16,88,89,1,78,79,80,696)):
    real=add(sq(v(a0)),sc(sq(v(a1)),2),sc(mul(v(x0),v(a0)),-2*scale),
             sc(mul(v(x1),v(a1)),-8),sc(mul(v(j0),v(a0)),-2),sc(mul(v(j1),v(a1)),-4),const(-11))
    imag=add(sc(mul(v(a0),v(a1)),2),sc(mul(v(x0),v(a1)),-2*scale),
             sc(mul(v(x1),v(a0)),-4),sc(mul(v(j0),v(a1)),-2),sc(mul(v(j1),v(a0)),-2),const(6))
    assert dec(oo[row0])==real and dec(oo[row0+1])==imag
    assert dec(oo[row0+2])==add(sq(v(a0)),sc(sq(v(a1)),-2),sq(v(norm)))

flips={'A':{1,2,3,4,21,22,23,24,112,113},
       'T':{9,10,11,12,29,30,31,32,128,129},
       'Z':{13,14,15,16,33,34,35,36,136,137}}
sign_cert={}
for name,indices in flips.items():
    sign_cert[name]=[]
    for row in new['residuals']:
        parity={sum(i in indices for i in t['monomial'])%2 for t in row['terms']}
        assert len(parity)==1,(name,row['id'])
        if any(indices.intersection(t['monomial']) for t in row['terms']):
            sign_cert[name].append({'row':row['id'],'multiplier':(-1)**next(iter(parity))})

# Exact arithmetic for the cited2-adic starting point and its square coefficient.
def km(a,b):return a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def ki(a):
    norm=a[0]**2-2*a[1]**2
    return a[0]/norm,-a[1]/norm
def val(q,p):
    assert q
    a,b=abs(q.numerator),q.denominator;n=0
    while a%p==0:a//=p;n+=1
    while b%p==0:b//=p;n-=1
    return n
a=(F(-1),F(7,4));b=(F(39,8),F(-9,2));x=km(a,a);y=km(a,b)
z=km((-x[0],-x[1]),ki(y))
assert z==(F(232,357),F(86,357))
assert (val(z[0],2),val(z[1],2))==(3,1)
assert val(km(z,z)[1],2)==5
assert val(km(ki(z),ki(z))[1],2)==-1
assert val(x[1],2)==-1
assert km(ki((F(2),F(1))),ki((F(2),F(1)))) == (F(3,2),F(-1))
assert int(F(-1))%3==2
assert (x[0].numerator*pow(x[0].denominator,-1,3))%3==0
assert (x[1].numerator*pow(x[1].denominator,-1,3))%3==1
assert (val(F(12),2),val(F(108),2))==(2,2)
assert (val(F(12),3),val(F(108),3))==(1,3)
assert all((u*u+w*w)%3 for u in range(3) for w in range(3) if (u,w)!=(0,0))

# Full primitive-integer residual SOS, including coefficient and support checks.
total={};used=set()
for row in new['residuals']:
    p=dec(row);used|={i for m in p for i in m if i>=0}
    assert max(sum(i>=0 for i in m) for m in p)<=2
    denominator=reduce(lcm,(c.denominator for c in p.values()),1)
    integers={m:int(c*denominator) for m,c in p.items()}
    content=reduce(gcd,(abs(c) for c in integers.values()))
    total=add(total,sq({m:F(c,content) for m,c in integers.items()}))
assert total==dec(table)
assert used=={c['id'] for c in new['coordinates']}
assert (len(used),len(rr),len(total))==(359,329,6416)
assert max(sum(i>=0 for i in m) for m in total)==4
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert reduce(gcd,(abs(c.numerator) for c in total.values()))==1
assert {m:c for m,c in total.items() if m.count(-1)==2}=={
    (-1,-1,57,57,549,549):F(16),(-1,-1,549,549,903,903):F(1)}
assert max(abs(c) for m,c in total.items() if m.count(-1)==1)<=96
assert max(abs(c.numerator).bit_length() for m,c in total.items() if -1 not in m)<2048
result={'variables':359,'witnesses':358,'residuals':329,'monomials':6416,'degree':4,'content':1,
    'maximum_coefficient':'16*3^(2^26)','all_retained_consumers_checked':True,'full_SOS':True,
    'sign_involutions':{k:sorted(v) for k,v in flips.items()},'affected_sign_rows':sign_cert,
    'new_math_pending_independent_review':True}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='affected_sign_rows'},indent=2))
