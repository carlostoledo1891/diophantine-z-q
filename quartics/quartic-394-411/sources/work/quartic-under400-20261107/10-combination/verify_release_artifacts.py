"""Independently check all physical tables and the ordinary coefficient lift."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
from functools import reduce
import json,hashlib,sys
H=Path(__file__).resolve().parent;n=int(sys.argv[1]);D=H/f'release{n}'
def read(name):return json.loads((D/name).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):
    out={}
    for t in ts:
        m=tuple([-1]*t.get('sPower',0)+t['monomial']);assert m==tuple(sorted(m))
        out[m]=out.get(m,0)+Q(t['coefficient'])
    return {m:v for m,v in out.items() if v}
def normalize(q):
    den=reduce(lcm,(v.denominator for v in q.values()),1)
    div=reduce(gcd,(abs(int(v*den)) for v in q.values()),0)
    return {m:v*Q(den,div) for m,v in q.items()}
def expand(rows):
    out={}
    for row in rows:
        q=normalize(p(row['terms']))
        assert max(sum(i!=-1 for i in m) for m in q)<=2
        for m,v in q.items():
            for k,w in q.items():
                t=tuple(sorted(m+k));out[t]=out.get(t,0)+v*w
    return {m:v for m,v in out.items() if v}
meta=read('ARTIFACTS.json')
for name,digest in meta['files'].items():assert sha(D/name)==digest,name
assert sha(H/f'combined{n}-ir.json')==meta['sourceSha256']==sha(D/f'candidate{n}-ir.json')
assert sha(H/f'combined{n}-polynomial.json')==meta['sourcePolynomialSha256']==sha(D/f'polynomial{n}.json')
base=read(f'candidate{n}-ir.json');ordinary=read(f'candidate{n+16}-ir.json')
br={r['name']:r for r in base['residuals']};orr={r['name']:r for r in ordinary['residuals']}
oc={c['name']:c['id'] for c in ordinary['coordinates']}
assert set(orr)==set(br)|{f'constant.definition{i}' for i in range(16)}
for name,row in br.items():
    expected={tuple(sorted(tuple(i for i in mon if i!=-1)+(oc['constant.c15'],)*mon.count(-1))):v for mon,v in p(row['terms']).items()}
    assert p(orr[name]['terms'])==expected,name
for j in range(16):
    expected={(oc[f'constant.c{j}'],):Q(1)}
    expected[() if j==0 else (oc[f'constant.c{j-1}'],)*2]=Q(-3**1024 if j==0 else -1)
    assert p(orr[f'constant.definition{j}']['terms'])==expected
assert 1024*2**15==2**25
for count,ir in [(n,base),(n+16,ordinary)]:
    q=expand(ir['residuals']);assert q==p(read(f'polynomial{count}.json')['terms'])
    assert len(ir['coordinates'])==count
    assert {i for mon in q for i in mon if i!=-1}=={c['id'] for c in ir['coordinates']}
    assert max(sum(i!=-1 for i in mon) for mon in q)==4
    assert all(v.denominator==1 for v in q.values())
    assert reduce(gcd,(abs(v.numerator) for v in q.values()),0)==1
    stem=f'quartic-{count}-'+('symbolic-coefficients' if count==n else 'ordinary-coefficients')
    table=read(stem+'.json');compact=read(f'compact{count}-ir.json')
    assert table['inputCoordinate']==compact['inputCoordinate']==1
    assert [c['id'] for c in table['coordinates']]==list(range(1,count+1))
    mapping={c['sourceId']:c['id'] for c in table['coordinates']};assert mapping[0]==1
    mapped={tuple(mapping[i] if i!=-1 else -1 for i in mon):v for mon,v in q.items()}
    assert mapped==p(table['terms'])==expand(compact['residuals'])
    text=[line for line in (D/(stem+'.txt')).read_text().splitlines() if line and not line.startswith('#')]
    expected=[t['coefficient']+' | '+str(t['sPower'])+' | '+','.join(map(str,t['monomial'])) for t in table['terms']]
    assert text==expected
    if count==n:
        assert [(m,v) for m,v in q.items() if m.count(-1)==2]==[((-1,-1,57,57),Q(16))]
        assert max(abs(v.numerator).bit_length() for m,v in q.items() if -1 not in m)<2048
        assert max(abs(v) for m,v in q.items() if m.count(-1)==1)<=48
        assert (57,57) not in q and (-1,57,57) not in q
    else:
        maximum=max(abs(v) for v in q.values());delta=maximum-3**2048
        assert meta['statistics'][str(count)]['maximumCoefficient']==f'3^2048+{delta}'
        assert maximum.numerator.bit_length()==3247
    assert len(q)==meta['statistics'][str(count)]['monomials']
print(json.dumps({'verified':True,'symbolicVariables':n,'ordinaryVariables':n+16,'symbolicMonomials':meta['statistics'][str(n)]['monomials'],'ordinaryMonomials':meta['statistics'][str(n+16)]['monomials'],'coordinateRange':'1..totalVariables','inputCoordinate':1,'ordinaryMaximumCoefficientBits':3247,'fullTablesAndConstantLift':True},indent=2))
