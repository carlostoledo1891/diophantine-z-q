"""Exact finite checks; does not certify the ineffective defining threshold."""
import json, math, hashlib
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parent

def terms(rows):
    out={}
    for t in rows:
        k=(t['parameterPower'],tuple(t['monomial']))
        assert k not in out, 'duplicate term'
        assert list(k[1])==sorted(k[1])
        out[k]=Fraction(t['coefficient'])
        assert out[k]
    return out

def check(kind):
    ir=json.loads((ROOT/'tables'/f'{kind}222-ir.json').read_bytes())
    p=json.loads((ROOT/'tables'/f'{kind}222-polynomial.json').read_bytes())
    assert ir['variables']==p['variables']==222
    assert ir['inputCoordinate']==p['inputCoordinate']==1
    assert ir['fixedParameter']==p['fixedParameter']
    assert p['fixedParameter']['base']==149 and p['fixedParameter']['exponent']=='2*N+1'
    assert p['fixedParameter']['coordinate'] is False
    assert len(ir['residuals'])==196
    expected=terms(p['terms']); actual={}; weights=[]
    for row in ir['residuals']:
        r=terms(row['terms']); w=Fraction(row.get('positive_square_weight','1'))
        assert w>0; weights.append(w)
        assert max(len(m) for a,m in r)<=2
        for (a,m),c in r.items():
            for (b,n),d in r.items():
                k=(a+b,tuple(sorted(m+n)))
                actual[k]=actual.get(k,Fraction(0))+w*c*d
    actual={k:v for k,v in actual.items() if v}
    assert actual==expected, 'weighted SOS differs from coefficient table'
    if 'positiveRowWeights' in p: assert weights==list(map(Fraction,p['positiveRowWeights']))
    assert all(c.denominator==1 for c in actual.values())
    assert {i for a,m in actual for i in m}==set(range(1,223))
    assert max(len(m) for a,m in actual)==4
    assert math.gcd(*(abs(int(c)) for c in actual.values()))==1
    grouped={}
    for (a,m),c in actual.items(): grouped.setdefault(m,{})[a]=int(c)
    expected_count=2277 if kind=='sparse' else 2961
    assert len(grouped)==expected_count and len(actual)==expected_count+1
    A0=149**107
    maxima=[]
    for m,c in grouped.items():
        if 2 in c:
            assert c=={0:1,2:1}; maxima.append(m)
        else:
            assert set(c)<= {0,1}
            c0,c1=abs(c.get(0,0)),abs(c.get(1,0))
            assert c0+c1*A0<A0*A0+1
            assert 2*A0>=c1
    assert len(maxima)==1
    return dict(kind=kind,variables=222,residuals=196,coordinate_monomials=len(grouped),parameter_terms=len(actual),degree=4,content=1,height='A_N^2+1 for N>=53',height_attaining_monomial=list(maxima[0]),defining_threshold='ineffective, not certified by this check')

def verify_sources():
    manifest=json.loads((ROOT/'SOURCE-COPIES.json').read_bytes())
    for row in manifest['files']:
        data=(ROOT/row['path']).read_bytes()
        assert len(data)==row['bytes']
        assert hashlib.sha256(data).hexdigest()==row['sha256'], row['path']
    return len(manifest['files'])

if __name__=='__main__':
    print(json.dumps({'ok':True,'source_files':verify_sources(),'results':[check('raw'),check('sparse')]},indent=2))
