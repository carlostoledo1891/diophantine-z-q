"""Standalone exact verifier for modulo-certificate.json.

No candidate-producing code is imported. All arithmetic is rational. A recorded
row replacement is checked as a polynomial identity after a constant pivot.
Only unaffected rows may be used as identities. They remain present, so both
directions of the rational-zero correspondence follow without any division
other than the pivot's nonzero rational constant.
"""
import hashlib,json
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
from functools import reduce

HERE=Path(__file__).resolve().parent
BASE=HERE
SOURCE=HERE/'source532.json'

def readpoly(terms):
    p={}
    for t in terms:
        m=tuple(t['monomial']);assert m==tuple(sorted(m))
        k=(t.get('sPower',0),m);p[k]=p.get(k,Q(0))+Q(t['coefficient'])
    return {k:v for k,v in p.items() if v}

def terms(p):
    return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]

def add(p,q):
    p=p.copy()
    for k,v in q.items():
        p[k]=p.get(k,Q(0))+v
        if not p[k]:del p[k]
    return p

def mul(p,q):
    r={}
    for (s,m),v in p.items():
        for (t,n),w in q.items():
            k=(s+t,tuple(sorted(m+n)));r[k]=r.get(k,Q(0))+v*w
    return {k:v for k,v in r.items() if v}

def subst(p,x,q):
    r={}
    for (s,m),v in p.items():
        t={(s,tuple(i for i in m if i!=x)):v}
        for i in range(m.count(x)):t=mul(t,q)
        r=add(r,t)
    return r

def degree(p):return max((len(m) for s,m in p),default=0)
def variables(p):return {v for s,m in p for v in m}

def verify():
    src=SOURCE
    cert=json.loads((HERE/'modulo-certificate.json').read_text())
    assert hashlib.sha256(src.read_bytes()).hexdigest()==cert['baselineSha256']
    data=json.loads(src.read_text());rows={r['id']:readpoly(r['terms']) for r in data['residuals']}
    coords={x['id']:x for x in data['coordinates']};original=len(coords)
    for step in cert['operations']:
        if step.get('kind')=='shear':
            free=step['free'];assert free in coords
            for s in step['shears']:
                v=s['coordinate'];a=Q(s['factor'])
                assert v in coords and v!=free and v!=0 and not coords[v].get('protected')
                q={(0,(v,)):Q(1),(0,(free,)):a}
                rows={r:subst(p,v,q) for r,p in rows.items()}
                assert all(degree(p)<=2 for p in rows.values())
            continue
        x=step['coordinate'];pivot=step['pivot'];p=rows[pivot];q=readpoly(step['replacement'])
        assert x!=0 and not coords[x].get('protected')
        assert x not in variables(q)
        a=p.get((0,(x,)));assert a
        assert subst(p,x,q)=={}
        assert all(x not in m or (s,m)==(0,(x,)) for s,m in p)
        affected={r for r,p in rows.items() if x in variables(p)}
        assert {z['row'] for z in step['changes']}==affected-{pivot}
        assert len(step['changes'])==len(affected)-1
        changes={}
        for z in step['changes']:
            r=z['row'];expected=subst(rows[r],x,q)
            for multiple in z['multiples']:
                s=multiple['row'];factor=readpoly(multiple['factor'])
                assert s not in affected and x not in variables(factor)
                expected=add(expected,mul(factor,rows[s]))
            actual=readpoly(z['result'])
            assert expected==actual and degree(actual)<=2 and x not in variables(actual)
            changes[r]=actual
        rows.update(changes);del rows[pivot];del coords[x]
    candidate=json.loads((HERE/'candidate-ir.json').read_text())
    assert {r['id']:readpoly(r['terms']) for r in candidate['residuals']}==rows
    assert {x['id']:x for x in candidate['coordinates']}==coords
    assert set(coords)==set.union(*(variables(p) for p in rows.values()))
    multipliers={}
    for r,p in rows.items():
        denominator=reduce(lcm,(v.denominator for v in p.values()),1)
        numerator=reduce(gcd,(abs(v.numerator*(denominator//v.denominator)) for v in p.values()),0)
        factor=Q(denominator,numerator);multipliers[r]=str(factor)
        rows[r]={k:v*factor for k,v in p.items()}
        assert all(v.denominator==1 for v in rows[r].values())
    # Sum of rational squares vanishes exactly when all rows vanish.
    result={'verified':True,'baselineCoordinates':original,'coordinates':len(coords),'residuals':len(rows),
      'eliminated':original-len(coords),'maxResidualDegree':max(map(degree,rows.values())),
      'sumOfSquaresDegree':2*max(map(degree,rows.values())),
      'certificateSha256':hashlib.sha256((HERE/'modulo-certificate.json').read_bytes()).hexdigest(),
      'proof':'Exact polynomial identities. Forward: invert each shear, then delete each pivot coordinate. Reverse: reinsert each pivot replacement, then apply each shear, processing operations in reverse order.'}
    for r in candidate['residuals']:r['terms']=terms(rows[r['id']])
    assert json.loads((HERE/'integer-candidate-ir.json').read_text(encoding='utf-8')) == candidate
    assert json.loads((HERE/'verification.json').read_text(encoding='utf-8')) == result
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=SOURCE)
    parser.add_argument('--directory',type=Path,default=HERE)
    args=parser.parse_args();SOURCE=args.source;HERE=args.directory
    verify()
