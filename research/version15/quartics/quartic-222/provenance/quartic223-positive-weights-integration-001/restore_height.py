import json,sys
from pathlib import Path
from fractions import Fraction as F
O=Path(__file__).resolve().parent;B=O.parents[1]
sys.path.insert(0,str(B/'work/quartic224-validation-integration-001'))
from verify import terms,add,mul,scale,check
ir=json.loads((B/'work/quartic238-optimization-20261110/resume-20261110/joint-root-sparse-111/candidate223-ir.json').read_bytes());q=json.loads((O/'polynomial.json').read_bytes());w=list(map(F,q['positiveRowWeights']))
C=next(F(t['coefficient'])for t in q['terms']if t['parameterPower']==2)
for i,r in enumerate(ir['residuals']):
 if r['id'] in [57,71]:w[i]/=C
p=add(*(scale(mul(terms(r['terms']),terms(r['terms'])),z)for r,z in zip(ir['residuals'],w)))
assert all(v.denominator==1 for v in p.values())
(O/'WEIGHTS.json').write_text(json.dumps(list(map(str,w)),indent=2)+'\n')
q['positiveRowWeights']=list(map(str,w));q['terms']=[dict(parameterPower=a,monomial=list(m),coefficient=str(v))for(a,m),v in sorted(p.items())]
r=check(ir,ir,q);r['anchor_weight_divisor']=str(C)
(O/'polynomial.json').write_text(json.dumps(q,indent=2)+'\n');(O/'HEIGHT-RESTORE.json').write_text(json.dumps(r,indent=2)+'\n');print(r['coordinate_monomials'])
