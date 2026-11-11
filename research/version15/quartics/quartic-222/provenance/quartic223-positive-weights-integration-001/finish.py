import json,sys,hashlib,math
from pathlib import Path
from fractions import Fraction as F
O=Path(__file__).resolve().parent;B=O.parents[1]
sys.path.insert(0,str(B/'work/quartic224-validation-integration-001'))
from verify import check
P=B/'work/quartic238-optimization-20261110/resume-20261110/joint-root-sparse-111/candidate223-ir.json';ir=json.loads(P.read_bytes());q=json.loads((O/'polynomial.json').read_bytes());r=check(ir,ir,q)
ts=q['terms'];a2=[t for t in ts if t['parameterPower']==2];assert len(a2)==1
C=int(a2[0]['coefficient']);m=a2[0]['monomial'];c0=sum(int(t['coefficient'])for t in ts if t['parameterPower']==0 and t['monomial']==m)
M0=max(abs(int(t['coefficient']))for t in ts if t['parameterPower']==0);M1=max(abs(int(t['coefficient']))for t in ts if t['parameterPower']==1)
assert C>0 and c0==C and M1*149**107+M0<C*149**214
r.update(leading_A_squared_coefficient=str(C),matching_constant_coefficient=str(c0),constant_bound_verified=True,linear_bound_verified=True,coefficient_height='C*(A_N^2+1) for N>=53, C='+str(C),degree=4,primitive_content=math.gcd(*(int(t['coefficient'])for t in ts)),map='Identity on all223 coordinates; positive row weights preserve simultaneous zeros exactly over Q or R.',author_claim_only=True)
(O/'VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='consumers'}))
