import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
O=Path(__file__).resolve().parent; P=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/joint-root-rowpairs-112'); W=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic223-positive-weights-integration-001'); I=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/joint-root-sparse-111/candidate223-ir.json')
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sh(P/'MANIFEST.json')=='369f42d05523ab2176527cb2b72a48de5bcaff907ac38825636e030beb0b57a0'
m=json.loads((P/'MANIFEST.json').read_bytes())
for t in m['members']:assert sh(P/t['path'])==t['sha256']
assert sh(I)=='eef4351cd9cd714ee93b6851fcfbfe62c5351be4b1d7000f5b90afd56d26da7c'
assert sh(W/'MANIFEST.json')==m['parent_weight_manifest']=='90f58f17d69a72d39976fae95da08a7f10bbee2c6dda056d026c4ac0f7d9fd74'
a=json.loads(I.read_bytes()); b=json.loads((P/'candidate223-ir.json').read_bytes()); p=json.loads((P/'polynomial.json').read_bytes()); wp=json.loads((W/'polynomial.json').read_bytes())
def terms(r):return {(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
def add(x,y,k):
 z=dict(x)
 for m,c in y.items():z[m]=z.get(m,F(0))+k*c
 return {m:c for m,c in z.items() if c}
for k in ['variables','inputCoordinate','fixedParameter','coordinates']:assert a[k]==b[k]
assert len(a['residuals'])==len(b['residuals'])==197
for n,(x,y) in enumerate(zip(a['residuals'],b['residuals'])):
 target=terms(x) if n!=123 else add({m:3*c for m,c in terms(x).items()},terms(a['residuals'][124]),11)
 assert terms(y)==target,n
assert add({m:c/3 for m,c in terms(b['residuals'][123]).items()},terms(b['residuals'][124]),F(-11,3))==terms(a['residuals'][123])
weights=p['positiveRowWeights'];assert weights==wp['positiveRowWeights'] and all(F(w)>0 for w in weights)
assert all(F(r['positive_square_weight'])==F(w) for r,w in zip(b['residuals'],weights))
acc=defaultdict(F)
for r,w in zip(b['residuals'],weights):
 for (i,m),v in terms(r).items():
  for (j,n),z in terms(r).items():acc[i+j,tuple(sorted(m+n))]+=F(w)*v*z
acc={k:v for k,v in acc.items() if v}; actual=terms(p)
assert acc==actual and len(acc)==len(p['terms'])==2281
assert len({m for i,m in acc})==2280 and max(map(lambda k:len(k[1]),acc))==4
assert all(c.denominator==1 for c in acc.values()) and math.gcd(*(int(c) for c in acc.values()))==1
assert {i for a,m in acc for i in m}==set(range(1,224))
quad=[(m,c)for(a,m),c in acc.items()if a==2];assert len(quad)==1 and quad[0][1]==1 and acc[0,quad[0][0]]==1
M0=max(abs(c)for(a,m),c in acc.items()if a==0);M1=max(abs(c)for(a,m),c in acc.items()if a==1);A=149**107
assert M1*A+M0<A*A and 2*A>M1
out={'member_pins':True,'exact_changed_row':123,'unchanged_rows':196,'inverse_row_check':True,'coordinates_input_parameter_unchanged':True,'weights_unchanged_positive':True,'full_weighted_expansion':True,'variables':223,'residuals':197,'monomials':2280,'parameter_terms':2281,'degree':4,'content':1,'height':'A_N^2+1 for N>=53','defining_threshold':'inherited ineffective'}
(O/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
