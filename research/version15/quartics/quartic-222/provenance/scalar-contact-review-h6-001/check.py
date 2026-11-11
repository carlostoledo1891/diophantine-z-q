import json, hashlib, math
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
AUTHOR=HERE.parent/'scalar-contact-quartic-001'
OLD=ROOT/'work/quartic238-optimization-20261110/linear-lucas/reference233-014/candidate233-ir.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(AUTHOR/'MANIFEST.json')=='22eacf67981494ff610bbb4466b518626ca830826c457d08b71b91b8082ee734'
for x in json.loads((AUTHOR/'MANIFEST.json').read_bytes())['members']:
    p=AUTHOR/x['path']; assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
old=json.loads(OLD.read_bytes()); new=json.loads((AUTHOR/'candidate232-ir.json').read_bytes())
assert sha(OLD)=='26d9a2aef8b92fb7fa7d42a24c185ac71d889c0952a0e0bf4b44d09ea9e67691'
assert new['variables']==232 and len(new['residuals'])==206
assert new['fixedParameter']==old['fixedParameter'] and new['inputCoordinate']==old['inputCoordinate']==1
compact=lambda k:k-(k>122)
oldrows={r['name']:r for r in old['residuals']}
newrows={r['name']:r for r in new['residuals']}
assert len(oldrows)==207 and len(newrows)==206
deleted={'scalar.rFour.definition','scalar.contact_product.definition'}
assert set(oldrows)-set(newrows)==deleted
assert set(newrows)-set(oldrows)=={'scalar.four_contact_product.definition'}
for name in set(oldrows)&set(newrows):
    expected=[dict(t,monomial=[compact(i) for i in t['monomial']]) for t in oldrows[name]['terms']]
    assert expected==newrows[name]['terms'],name
for c in old['coordinates']:
    if c['id']==122: continue
    nc=new['coordinates'][compact(c['id'])-1]
    assert nc==dict(c,id=compact(c['id']))

# Independent univariate rational polynomial arithmetic, t=x63, u=(51t+2501)^2/4.
def add(a,b):
    z=dict(a)
    for k,v in b.items():z[k]=z.get(k,F(0))+v
    return {k:v for k,v in z.items() if v}
def mul(a,b):
    z={}
    for i,x in a.items():
        for j,y in b.items(): z[i+j]=z.get(i+j,F(0))+x*y
    return {k:v for k,v in z.items() if v}
beta={0:F(2504),1:F(51)}
u={k:v/4 for k,v in mul({0:F(2501),1:F(51)},{0:F(2501),1:F(51)}).items()}
r={0:F(1)}
for a in [beta,add(beta,{0:F(-1)}),add(beta,{0:F(-2401)}),add({k:32*v for k,v in beta.items()},{0:F(343)})]:r=mul(r,a)
res={}
for term in newrows['scalar.four_contact_product.definition']['terms']:
    assert term['parameterPower']==0
    x={0:F(int(term['coefficient']))}
    for k in term['monomial']:
        x=mul(x,{63:{1:F(1)},121:u,122:r}[k])
    res=add(res,x)
assert not res

# Exact full polynomial, independently convolving all ordered term pairs.
poly=defaultdict(int)
for row in new['residuals']:
    for a in row['terms']:
        assert len(a['monomial'])<=2
        for b in row['terms']:
            k=(a['parameterPower']+b['parameterPower'],tuple(sorted(a['monomial']+b['monomial'])))
            poly[k]+=int(a['coefficient'])*int(b['coefficient'])
poly={k:v for k,v in poly.items() if v}
expected={(t['parameterPower'],tuple(t['monomial'])):int(t['coefficient']) for t in json.loads((AUTHOR/'candidate232-polynomial.json').read_bytes())['terms']}
assert poly==expected
assert len(poly)==3196 and len({k[1] for k in poly})==3195
assert {i for _,m in poly for i in m}==set(range(1,233))
assert max(map(lambda k:len(k[1]),poly))==4
assert math.gcd(*poly.values())==1
# Eventual-family height claim checked at A_min=149^107, not by expanding the family.
Amin=149**107
profiles=defaultdict(dict)
for (p,m),c in poly.items():profiles[m][p]=c
assert profiles[(122,122)]=={0:1,2:1}
for m,prof in profiles.items():
    if m==(122,122):continue
    assert 2 not in prof
    c0=abs(prof.get(0,0));c1=abs(prof.get(1,0))
    assert Amin>c1 and Amin*(Amin-c1)>c0

def vp(x,p):
    x=F(x);assert x
    n,d=x.numerator,x.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v
def product(x):
    b=2504+51*x*x
    return b*(b-1)*(b-2401)*(32*b+343)
def R(x):
    z=product(x);return F(149**3*z,1+149**2*z)
roots=[F(0),F(1),F(2401),F(-343,32)]
residues=[]
for theta in roots:
    q=(theta-2504)/51
    k=(q.numerator*pow(q.denominator,-1,149))%149
    assert pow(k,74,149)==148
    residues.append(k)
for x in range(8*9*17):
    z=product(x);q=R(x)
    assert vp(z,2) in (2,3)
    assert z%3==1 and z%17==13
    assert vp(q,3)==vp(q,17)==0
    assert vp(F(9792)/q,2)>=3 and vp(F(9792)/q,3)==2 and vp(F(9792)/q,17)==1
    den=(q*(q+9792)).denominator
    assert math.isqrt(den)**2==den
for e in range(1,5):
    for k in [1,2,7,148]:assert vp(R(F(k,149**e)),149)==1
# All finite root differences have only small-prime factors.
def primes(n):
    n=abs(n);out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out
bad=set([2,3,17,149])
for i,a in enumerate(roots):
    for b in roots[i+1:]:bad.update(primes((a-b).numerator));bad.update(primes((a-b).denominator))
assert max(bad)<76176
result={'decision':'finite_checks_pass','author_manifest_sha256':sha(AUTHOR/'MANIFEST.json'),'parent_sha256':sha(OLD),'candidate_ir_sha256':sha(AUTHOR/'candidate232-ir.json'),'unchanged_rows':205,'variables':232,'residuals':206,'coordinate_monomials':3195,'parameter_terms':3196,'degree':4,'content':1,'height':'A_N^2+1 for N>=53; not an effective defining threshold','nonsquare_residues_mod149':residues,'finite_contact_bad_primes':sorted(bad),'integer_residue_samples':8*9*17,'arithmetic_scope':'Finite checks support but do not replace the accompanying independent argument.'}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
