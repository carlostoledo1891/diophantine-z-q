import json,hashlib
from pathlib import Path
from fractions import Fraction as F
B=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo')
O=B/'work/quartic238-optimization-20261110'
D=O/'global/resume-20261110/trace-quotient-review-019'
C=O/'resume-20261110/trace-quotient222-116'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pol(row):return {(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient']) for t in row['terms']}
def sub(p):
 out={}
 for (a,m),v in p.items():
  n=[]
  for x in m:n.extend([119,222] if x==222 else [98,222] if x==223 else [x])
  k=(a,tuple(sorted(n)));out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
results=[]
for kind,parent in [('raw','joint-root-factor-110/candidate223-ir.json'),('sparse','joint-root-rowpairs-112/candidate223-ir.json')]:
 pp=O/'resume-20261110'/parent; np=C/(kind+'222-ir.json')
 old=json.loads(pp.read_bytes());new=json.loads(np.read_bytes())
 assert old['inputCoordinate']==new['inputCoordinate'] and old['fixedParameter']==new['fixedParameter']
 assert new['variables']==222 and len(new['residuals'])==196
 assert old['coordinates'][:221]==new['coordinates'][:221]
 census=[r['id'] for r in old['residuals'] if any(222 in t['monomial'] or 223 in t['monomial'] for t in r['terms'])]
 assert census==[186,196,197]
 target={r['parent223RowId']:r for r in new['residuals']}
 assert set(target)==set(range(1,198))-{186}
 for r in old['residuals']:
  p=sub(pol(r))
  if r['id']==186:assert not p
  else:
   assert p==pol(target[r['id']]),(kind,r['id'])
   assert r.get('positive_square_weight',1)==target[r['id']].get('positive_square_weight',1)
 for i in [9,43,44,45,46,56,57,68,71,73,47]:
  assert pol(old['residuals'][i-1])==pol(target[i])
 assert pol(target[47])=={(0,(96,96)):F(1),(0,(98,)):F(-1)}
 results.append(dict(kind=kind,parent_sha256=sha(pp),candidate_sha256=sha(np),census=census,exact_parent_rows=197,retained_rows=196,unchanged_domain_rows=11,input_and_parameter_fixed=True,weights_unchanged=True))
(D/'CHECKS.json').write_text(json.dumps(results,indent=2)+chr(10))
print(json.dumps(results))
