"""Read-only semantic transport check; no producer imports."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def add(*qs):
    out={}
    for q in qs:
        for m,v in q.items():out[m]=out.get(m,0)+v
    return {m:v for m,v in out.items() if v}
def scale(q,k):return {m:v*k for m,v in q.items() if v*k}
def mul(q,r):
    out={}
    for m,v in q.items():
        for n,w in r.items():
            key=tuple(sorted(m+n));out[key]=out.get(key,0)+v*w
    return {m:v for m,v in out.items() if v}
def canon(q):return scale(q,1/q[min(q)])
def shift(q):
    out={}
    for mon,v in q.items():
        n=mon.count(248);rest=tuple(i for i in mon if i!=248)
        for y in range(n+1):
            for x in range(n-y+1):
                key=tuple(sorted(rest+(248,)*y+(0,)*x))
                coef=v*comb(n,y)*comb(n-y,x)*102**(x+y)*76**(n-x-y)
                out[key]=out.get(key,0)+coef
    return {m:v for m,v in out.items() if v}
before=read('combined423-ir.json');after=read('combined417-ir.json')
b={r['name']:r for r in before['residuals']};a={r['name']:r for r in after['residuals']}
deleted={n for n in b if n.startswith('correction.')}|{'scalar.correctedR.definition'}
assert len(deleted)==6 and set(a)==set(b)-deleted
removed={61,62,63,64,65,524}
bc={c['id']:c for c in before['coordinates']};ac={c['id']:c for c in after['coordinates']}
assert ac=={i:c for i,c in bc.items() if i not in removed}
affected=[]
for n,row in b.items():
    if n in deleted or n=='scalar.b.definition':continue
    expected=p(row['terms']) if n=='inputSquare.definition' else shift(p(row['terms']))
    assert canon(expected)==canon(p(a[n]['terms'])),n
    assert {k:v for k,v in row.items() if k!='terms'}=={k:v for k,v in a[n].items() if k!='terms'},n
    if expected!=p(row['terms']):affected.append(n)
assert b['inputSquare.definition']==a['inputSquare.definition']
assert not any(removed.intersection(t['monomial']) for row in a.values() for t in row['terms'])
# The current norm root is r32*W-B^2-r*Q=0, with Q in coordinate541.
root=p(a['reduced_scalar.root']['terms'])
r={tuple(i for i in m if i!=541):-v for m,v in root.items() if 541 in m}
assert len(r)==6 and all(len(m)<=1 for m in r)
assert canon(p(a['scalar.r_power_2.definition']['terms']))==canon(add({(600,):F(1)},scale(mul(r,r),-1)))
expected_b=add(mul(add({(600,):F(1)},scale(r,4896)),{(525,):F(1)}),{(526,):F(82479248)})
assert canon(expected_b)==canon(p(a['scalar.b.definition']['terms']))
# Check the reviewed component uses exactly this affine r, not a name alias.
component=read('inputs/deterministic442-ir.json')
cr={q['name']:q for q in component['residuals']}
assert p(cr['reduced_scalar.root']['terms'])==root
assert canon(p(cr['scalar.b.definition']['terms']))==canon(expected_b)
assert before['fixedParameter']==after['fixedParameter']
print(json.dumps({'passed':True,'shiftedRows':affected,'shiftedCount':len(affected),'removedCoordinates':sorted(removed),'candidateSha256':hashlib.sha256((H/'combined417-ir.json').read_bytes()).hexdigest(),'inputLabel':'51*(2X+1)^2+2504','correction':'r+4896','allOtherRowsPreservedUnderInputSubstitution':True},indent=2))
