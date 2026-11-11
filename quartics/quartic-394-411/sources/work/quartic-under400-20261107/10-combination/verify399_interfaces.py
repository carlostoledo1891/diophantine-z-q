"""Read-only physical interface checks for the frozen 399-variable batch."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def rows(d):return {r['name']:r for r in d['residuals']}
def coords(d):return {c['id']:c for c in d['coordinates']}
def pol(row):
    p={(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in row['terms']}
    v=p[min(p)];return {m:a/v for m,a in p.items()}
source=read('combined417-ir.json');scaled=read('combined401-ir.json');final=read('combined399-ir.json')
component=read('inputs/biquadratic411-ir.json');component_base=read('inputs/identity-chart427-ir.json')
s,m,f=map(rows,[source,scaled,final]);cr,cb=map(rows,[component,component_base])
deleted={'H.chart.x.0.definition','H.chart.x.1.definition'}
assert set(f)==set(m)-deleted
assert coords(final)=={i:c for i,c in coords(scaled).items() if i not in {17,18}}
assert {n for n,r in m.items() if any({17,18}.intersection(t['monomial']) for t in r['terms'])}==deleted
assert all(f[n]==r for n,r in m.items() if n not in deleted)
assert final['fixedParameter']==source['fixedParameter']
# Every changed or added biquadratic row has precisely the reviewed polynomial.
changed={n for n in cr if n not in cb or pol(cr[n])!=pol(cb[n])}
for n in changed:assert pol(f[n])==pol(cr[n]),n
removed=set(coords(component_base))-set(coords(component))
assert not any(removed.intersection(t['monomial']) for r in f.values() for t in r['terms'])
# The H/V0 equations in the independently reviewed H-domain source survive
# literally, apart from row IDs assigned during earlier disjoint compositions.
hd=rows(read('primary437-ir.json'))
protected={n for n in hd if n.startswith(('H.','V0.','logV0.'))}-deleted
for n in protected:assert pol(hd[n])==pol(f[n]),n
# All scalar, input and anchor equations are untouched by the final two steps.
scalar={n for n in s if n.startswith(('scalar.','reduced_scalar.','inputSquare.','anchor.'))}
for n in scalar:assert s[n]==f[n],n
# Root charts and odd-root choices are unchanged, so every a,c divisor used in
# the exact scaled map has exactly its previously reviewed source equations.
root={n for n in s if n.startswith(('A.','S.','T.','Z.'))}
for n in root:assert s[n]==f[n],n
assert len(f)==368 and len(coords(final))==399
print(json.dumps({'passed':True,'candidateSha256':hashlib.sha256((H/'combined399-ir.json').read_bytes()).hexdigest(),'biquadraticChangedRows':sorted(changed),'protectedHAndV0Rows':sorted(protected),'unchangedScalarInputAnchorRows':len(scalar),'unchangedRootRows':len(root),'deletedHCoordinates':[17,18],'completeHIncidence':sorted(deleted)},indent=2))
