import json,hashlib,math
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
P=Path(__file__).resolve().parent;S=P.parent/'shared-T-elimination224-004/candidate224-ir.json'
raw=S.read_bytes();assert hashlib.sha256(raw).hexdigest()=='abd51c098e6f8de7207977beafb4319fc334e3c5c3e621cfa1f48fd3c9f9c3af'
ir=json.loads(raw);assert [r['name']for r in ir['residuals'][-2:]]==['sharedT.reference.relation5.0','sharedT.reference.relation5.1']
ir['residuals']=ir['residuals'][:-2];ir['source']={'parent_sha256':hashlib.sha256(raw).hexdigest(),'construction':'Drop two implied Q5 components using Q2 coefficient149-unit domain; identity on coordinates'}
acc=defaultdict(int)
for row in ir['residuals']:
 ts=row['terms']
 for i,t in enumerate(ts):
  for j in range(i,len(ts)):
   u=ts[j];acc[t['parameterPower']+u['parameterPower'],tuple(sorted(t['monomial']+u['monomial']))]+=int(t['coefficient'])*int(u['coefficient'])*(1 if i==j else 2)
acc={k:v for k,v in acc.items()if v};assert max(len(m)for a,m in acc)==4 and math.gcd(*acc.values())==1
assert {i for a,m in acc for i in m}==set(range(1,225))
assert max(abs(c)for(a,m),c in acc.items()if a==0)<149**214
assert [(m,c)for(a,m),c in acc.items()if a==2]==[((114,114),1)] and acc[0,(114,114)]==1
assert max(abs(c)for(a,m),c in acc.items()if a==1)==44402
rels=json.loads((S.parent/'FIELD-RELATIONS.json').read_text())[0]['relations']
coefs=[]
for t in rels[2]:
 if 4 in t['monomial']:
  a,b=map(F,t['coefficient']);norm=a*a-2*b*b
  assert a.denominator%149 and b.denominator%149 and norm.numerator%149
  coefs.append(dict(t,norm=str(norm),norm_mod149=(norm.numerator*pow(norm.denominator,-1,149))%149))
stats={'variables':224,'residuals':198,'coordinate_monomials':len({m for a,m in acc}),'parameter_terms':len(acc),'degree':4,'content':1,'coefficient_height':'A_N^2+1 for N>=53; ineffective defining threshold unchanged'}
terms=[{'parameterPower':a,'monomial':list(m),'coefficient':str(c)}for(a,m),c in sorted(acc.items())]
for name,obj in [('candidate224-ir.json',ir),('candidate224-polynomial.json',{'variables':224,'degree':4,'inputCoordinate':ir['inputCoordinate'],'fixedParameter':ir['fixedParameter'],'terms':terms}),('COEFFICIENT-DOMAIN.json',coefs),('STATISTICS.json',stats)]:
 (P/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
