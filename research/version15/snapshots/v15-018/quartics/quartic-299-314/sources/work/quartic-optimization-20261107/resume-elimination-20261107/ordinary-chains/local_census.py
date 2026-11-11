"""Bounded exact census on frozen319. No ideal closure or branch assumptions."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
H=Path(__file__).resolve().parent
path=H.parent/'exact319/candidate319-ir.json'
assert hashlib.sha256(path.read_bytes()).hexdigest()=='847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676'
p=json.loads(path.read_bytes());rows=p['residuals']
quadratic={i for r in rows for t in r['terms'] if len(t['monomial'])==2 for i in t['monomial']}
assert quadratic=={c['id'] for c in p['coordinates']}
for monomial,rid in [([543,544],903),([903,903],504)]:
    assert {r['id'] for r in rows if any(t['monomial']==monomial for t in r['terms'])}=={rid}
base=[r for r in rows if r['id'] not in {903,504}]
assert all(t['sPower']==0 for r in base for t in r['terms'])
basis={}
for r in base:
    q={tuple(t['monomial']):F(t['coefficient']) for t in r['terms'] if len(t['monomial'])==2}
    while q:
        k=max(q)
        if k not in basis:
            a=q[k];basis[k]={m:c/a for m,c in q.items()};break
        a=q[k]
        for m,c in basis[k].items():
            q[m]=q.get(m,F(0))-a*c
            if not q[m]:del q[m]
assert len(basis)==len(base)==287
out={'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'variables_occurring_quadratically':len(quadratic),'variables_only_linear':0,'C_free_quadratic_part_rank':287,'independent_unique_anchor_pivots':{'903':[543,544],'504':[903,903]},'full_quadratic_part_rank_for_every_C':289,'affine_relations_from_scalar_linear_combinations':0,'scope':'No multiplied equations, nonlinear ideal closure, rational substitutions or arithmetic conclusions are tested.'}
(H/'LOCAL-CENSUS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
