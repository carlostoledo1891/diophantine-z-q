"""Independent read-only table, constant lift, and compact-coordinate check."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd, lcm
import hashlib,json

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
PKG=OUT.parent/'quartic-299-314'
def load(p): return json.loads(p.read_bytes())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def terms(obj):
    result={}
    for t in obj['terms']:
        key=(t['sPower'],tuple(t['monomial']))
        assert key not in result and tuple(sorted(key[1]))==key[1]
        result[key]=Fraction(t['coefficient'])
        assert result[key]
    return result
def expand(ir):
    result=defaultdict(Fraction)
    active=set()
    assert len({r['id'] for r in ir['residuals']})==len(ir['residuals'])
    assert len({c['id'] for c in ir['coordinates']})==len(ir['coordinates'])
    for r in ir['residuals']:
        p=terms(r)
        assert all(len(m)<=2 for _,m in p)
        denominator=lcm(*(x.denominator for x in p.values()))
        content=gcd(*(int(x*denominator) for x in p.values()))
        p={key:int(value*denominator)//content for key,value in p.items()}
        for (a,m),c in p.items():
            active.update(m)
            for (b,n),d in p.items():
                result[a+b,tuple(sorted(m+n))]+=c*d
    assert active=={c['id'] for c in ir['coordinates']}
    return {key:value for key,value in result.items() if value}

results={}
irs={}
for size,expected in ((299,(279,6630)),(314,(294,6672))):
    source=load(PKG/f'candidate{size}-ir.json');irs[size]=source
    compact=load(PKG/f'compact{size}-ir.json')
    polynomial=terms(load(PKG/f'polynomial{size}.json'))
    assert expand(source)==polynomial
    assert len(source['coordinates'])==size
    assert len(source['residuals'])==expected[0]
    assert len({m for s,m in polynomial})==expected[1]
    assert max(len(m) for s,m in polynomial)==4
    assert gcd(*(int(c) for c in polynomial.values()))==1
    ids=sorted(c['id'] for c in source['coordinates'])
    mapping={i:j+1 for j,i in enumerate(ids)}
    assert mapping[0]==1
    mapped={(s,tuple(mapping[i] for i in m)):c for (s,m),c in polynomial.items()}
    assert expand(compact)==mapped
    typ='symbolic' if size==299 else 'ordinary'
    assert terms(load(PKG/f'quartic-{size}-{typ}-coefficients.json'))==mapped
    rows={}
    for line in (PKG/f'quartic-{size}-{typ}-coefficients.txt').read_text().splitlines():
        if line.startswith('#'):continue
        coeff,power,monomial=(x.strip() for x in line.split('|'))
        key=int(power),tuple(map(int,monomial.split(','))) if monomial else ()
        assert key not in rows
        rows[key]=Fraction(coeff)
    assert rows==mapped
    if size==299:
        assert all(s in (0,1,2) for s,m in polynomial)
        assert len(polynomial)==len({m for s,m in polynomial})
        assert polynomial[(2,(89,89,89,89))]==186624
        assert max(abs(c) for (s,m),c in polynomial.items() if s==2)==186624
        assert max(abs(c) for (s,m),c in polynomial.items() if s==1)<2**2048
        assert max(abs(c) for (s,m),c in polynomial.items() if s==0)<2**2048
        maximum='186624*C^2; C=3^(2^25)'
    else:
        assert all(s==0 for s,m in polynomial)
        maximum=max(abs(c) for c in polynomial.values())
        assert maximum.denominator==1 and int(maximum).bit_length()==6496
        assert 2**6495<=maximum<2**6496
    results[str(size)]={'variables':size,'residuals':expected[0],'monomials':expected[1],
        'degree':4,'content':1,'maximum':str(maximum),
        'candidate_sha256':digest(PKG/f'candidate{size}-ir.json'),
        'polynomial_sha256':digest(PKG/f'polynomial{size}.json'),
        'compact_text_bytes':(PKG/f'quartic-{size}-{typ}-coefficients.txt').stat().st_size}

# The ordinary change must preserve every outside object and exactly replace C consumers.
a={r['id']:r for r in irs[299]['residuals']};b={r['id']:r for r in irs[314]['residuals']}
assert {rid for rid in a if any(t['sPower'] for t in a[rid]['terms'])}=={504,1903}
assert {rid for rid in a if a[rid]!=b[rid]}=={504,1903}
oldcoords={c['id']:c for c in irs[299]['coordinates']}
newcoords={c['id']:c for c in irs[314]['coordinates']}
assert all(newcoords[i]==c for i,c in oldcoords.items())
assert set(newcoords)-set(oldcoords)==set(range(1000,1015))
exponents=[2049]+[2048]*11+[0,0]
e=0
for j,addition in enumerate(exponents):
    e=2*e+addition
    prior=() if j==0 else (1000+j,1000+j)
    assert terms(b[1001+j])=={(0,(1001+j,)):1,(0,prior):-3**addition}
assert e==2**25
qpoly={(0,(83,83)):48,(0,(87,87)):48,(0,(89,89)):432}
assert terms(b[1000])=={(0,(1000,)):1,**{k:-v for k,v in qpoly.items()}}
for rid in (504,1903):
    restored=defaultdict(Fraction)
    for (power,m),coeff in terms(b[rid]).items():
        power+=m.count(1014)
        m=tuple(i for i in m if i!=1014)
        if 1000 in m:
            assert m.count(1000)==1
            m=tuple(i for i in m if i!=1000)
            for (qpower,qm),qc in qpoly.items():restored[power+qpower,tuple(sorted(m+qm))]+=coeff*qc
        else:restored[power,m]+=coeff
    assert {k:v for k,v in restored.items() if v}==terms(a[rid])
report={'status':'PASS independent finite table/remapping checks; not arithmetic proof acceptance',
        'results':results,'ordinary_C_consumers':[504,1903],
        'ordinary_added_coordinates':list(range(1000,1015)),
        'constant_exponent_recurrence':exponents,'constant_final_exponent':e}
(OUT/'FINITE-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:{i:j for i,j in v.items() if i!='maximum'} for k,v in results.items()},indent=2))
