"""Prove the integration input applies precisely four reviewed chart deltas."""
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):
 d={(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
 a=d[min(d)];return {k:v/a for k,v in d.items()}
src=read('inputs/released498.json');full=read('inputs/tangent493-ir.json');sub=read('inputs/tangent494-four-ir.json')
sr={r['name']:r for r in src['residuals']};fr={r['name']:r for r in full['residuals']};tr={r['name']:r for r in sub['residuals']}
assert hashlib.sha256((H/'inputs/tangent493-ir.json').read_bytes()).hexdigest()=='30dae02b01c79ee0f088d55ce45091a8014e376b24562de405fd60a913333a5f'
assert {c['id']:c for c in sub['coordinates']}=={c['id']:c for c in src['coordinates'] if c['id'] not in {108,116,124,132}}
for pre in ['V1.','V2.','V3.','V4.']:
 assert {n:p(r['terms']) for n,r in tr.items() if n.startswith(pre)}=={n:p(r['terms']) for n,r in fr.items() if n.startswith(pre)}
assert {n:p(r['terms']) for n,r in tr.items() if not n.startswith(('V1.','V2.','V3.','V4.'))}=={n:p(r['terms']) for n,r in sr.items() if not n.startswith(('V1.','V2.','V3.','V4.'))}
assert len(sub['coordinates'])==494 and len(sub['residuals'])==471
pins={n:hashlib.sha256((H/n).read_bytes()).hexdigest() for n in ['inputs/released498.json','inputs/tangent493-ir.json','inputs/tangent494-four-ir.json','inputs/tangent-review.md']}
(H/'tangent-subset-verification.json').write_text(json.dumps({'verified':True,'scope':'Exact V1..V4 restriction of reviewed five-chart change','sources':pins},indent=2)+'\n')
print('Exact four-chart restriction verified.')
