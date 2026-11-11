import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
O=Path(__file__).resolve().parent;P=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic223-positive-weights-integration-001')
manifest=P/'MANIFEST.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='90f58f17d69a72d39976fae95da08a7f10bbee2c6dda056d026c4ac0f7d9fd74'
m=json.loads(manifest.read_bytes())
for item in m['members']:
 b=(P/item['path']).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
parent=Path(m['parent']['path']);raw=parent.read_bytes();assert hashlib.sha256(raw).hexdigest()==m['parent']['sha256']=='eef4351cd9cd714ee93b6851fcfbfe62c5351be4b1d7000f5b90afd56d26da7c'
ir=json.loads(raw);poly=json.loads((P/'polynomial.json').read_bytes());weights=poly['positiveRowWeights']
assert poly['positiveRowWeights']==weights and len(weights)==len(ir['residuals'])==197
assert all(F(w)>0 for w in weights)
assert (poly['variables'],poly['inputCoordinate'],poly['fixedParameter'])==(ir['variables'],ir['inputCoordinate'],ir['fixedParameter'])
acc=defaultdict(F)
for row,weight in zip(ir['residuals'],weights):
 weight=F(weight)
 for t in row['terms']:
  for u in row['terms']:
   acc[t['parameterPower']+u['parameterPower'],tuple(sorted(t['monomial']+u['monomial']))]+=weight*F(t['coefficient'])*F(u['coefficient'])
acc={k:v for k,v in acc.items()if v};table={(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient'])for t in poly['terms']}
assert len(table)==len(poly['terms']) and acc==table
assert len(acc)==2284 and len({m for a,m in acc})==2283
assert all(v.denominator==1 for v in acc.values()) and math.gcd(*(int(v)for v in acc.values()))==1
assert max(len(m)for a,m in acc)==4 and {i for a,m in acc for i in m}==set(range(1,224))
a2=[(m,v)for(a,m),v in acc.items()if a==2];assert len(a2)==1
mon,C=a2[0];assert C==1 and acc[0,mon]==C
M0=max(abs(v)for(a,m),v in acc.items()if a==0);M1=max(abs(v)for(a,m),v in acc.items()if a==1);A0=149**107
assert M1*A0+M0<C*A0*A0 and 2*C*A0>M1
res={'all_member_pins':True,'exact_full_weighted_expansion':True,'positive_weights':197,'variables':223,'residuals':197,'coordinate_monomials':2283,'parameter_terms':2284,'degree':4,'content':1,'height_multiplier':str(C),'height':'C*(A_N^2+1) for N>=53','height_bound_and_monotonicity':True,'input_parameter_unchanged':True,'identity_witness_map':True}
(O/'CHECKS.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
