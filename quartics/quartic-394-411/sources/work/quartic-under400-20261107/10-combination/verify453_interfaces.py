"""Check the physical point and logarithm interfaces in the final composition."""
from pathlib import Path
from fractions import Fraction as F
import sys,runpy,json,hashlib
H=Path(__file__).resolve().parent
sys.argv=[str(H/'verify_rational_component.py'),'453']
ns=runpy.run_path(str(H/'verify_rational_component.py'))
p,fc,plus,minus,times,scale,var=[ns[n] for n in ['p','fc','plus','minus','times','scale','var']]
out=ns['out'];rows=ns['new'];val=ns['val'];cn={c['name']:c['id'] for c in out['coordinates']}
def normalized(q):
 a=q[min(q)];return {m:v/a for m,v in q.items()}
def eq(name,q):assert normalized(rows[name])==normalized(q),name
a,b,D=fc(-1,F(7,4)),fc(F(39,8),F(-9,2)),fc(11,-6)
h,j=val('H.h'),val('H.j');g=tuple(var(cn[f'V0.reciprocal.g.{i}']) for i in range(2))
N=minus(times(a,j),times(b,h));T=minus(minus(scale(times(times(D,b),g),2),scale(times(D,h),2)),times(times(a,b),j))
ell=val('logV0');R0=tuple(var(cn[f'logV0.rationalApproximation.{i}']) for i in range(2))
for i,q in enumerate(plus(times(T,ell),times(times(a,N),R0))):eq(f'logV0.definition.{i}',q)
for block in range(1,5):
 R=val('logV1.polynomial') if block==1 else tuple(var(cn[f'logV{block}.rationalApproximation.{i}']) for i in range(2))
 q=minus(times(ell,val(f'LP{block}')),times(val(f'V{block}.z'),R))
 for i,poly in enumerate(q):eq(f'logV{block}.{i}.definition',poly)
# All square relations used by the 470 triple eliminations stay literally equal.
base=json.loads((H/'inputs/accepted470-ir.json').read_text());old={r['id']:r for r in base['residuals']};now={r['name']:r for r in out['residuals']}
for rid in [132,133,144,145,150,151]:
 row=old[rid];assert p(row['terms'])==p(now[row['name']]['terms'])
assert all(f'V{i}.completeTangent.{j}' in rows for i in range(1,5) for j in range(2))
assert not any(n.startswith('V0.completeTangent.') for n in rows)
report={'verified':True,'candidateSha256':hashlib.sha256((H/'rational453-ir.json').read_bytes()).hexdigest(),
 'checked':['Actual reciprocal V0 logarithm consumes R0','Actual LP1 retains G2','Actual LP2..4 consume R2..4','All six square rows required by470 eliminations unchanged','Exactly four tangent chart pairs present'],
 'scope':'Finite physical interfaces. Non-author component reviews establish the real and local domain facts.'}
(H/'interfaces453.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
