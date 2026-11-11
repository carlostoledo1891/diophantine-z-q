from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
O=Path(__file__).resolve().parent;B=O.parents[3]
P=O.parent/'reference235-011/candidate235-ir.json'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads(P.read_bytes());new=json.loads((O/'candidate233-ir.json').read_bytes());mp=json.loads((O/'MAP.json').read_bytes());cm={int(i):j for i,j in mp['coordinate_map'].items()}
canonical=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
checks=[]
for a,b in mp['unchanged_row_map'].items():
 r=old['residuals'][int(a)-1];s=new['residuals'][b-1]
 expected=[dict(t,monomial=[cm[i] for i in t['monomial']]) for t in r['terms']]
 assert expected==s['terms'] and r['name']==s['name']
 checks.append({'old_row':int(a),'new_row':b,'renumbered_terms_sha256':hashlib.sha256(canonical(expected)).hexdigest()})
assert len(checks)==205
poly={}
for r in new['residuals']:
 ts=r['terms']
 for i,a in enumerate(ts):
  for j in range(i,len(ts)):
   b=ts[j];k=(a['parameterPower']+b['parameterPower'],tuple(sorted(a['monomial']+b['monomial'])))
   poly[k]=poly.get(k,0)+int(a['coefficient'])*int(b['coefficient'])*(1 if i==j else 2)
poly={k:v for k,v in poly.items() if v}
claimed={(t['parameterPower'],tuple(t['monomial'])):int(t['coefficient']) for t in json.loads((O/'candidate233-polynomial.json').read_bytes())['terms']}
assert poly==claimed
profiles={}
for (a,m),v in poly.items():profiles.setdefault(m,{})[a]=v
A=149**107
quadratic=[]
for m,pr in profiles.items():
 assert max(pr)<=2
 if 2 in pr:
  assert pr=={0:1,2:1};quadratic.append(m)
 else:
  c0=abs(pr.get(0,0));c1=abs(pr.get(1,0));assert c0+c1*A<=A*A+1 and c1<=2*A
assert quadratic
def fm(a,b):return a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def fs(a,b):return a[0]-b[0],a[1]-b[1]
def fd(a,b):
 delta=b[0]**2-2*b[1]**2
 return fm(a,(b[0]/delta,-b[1]/delta))
a=(F(57),F(-28));c=(F(88),F(-48));d=(F(39),F(-36));cases=0
for AA in [(F(0),F(1)),(F(1),F(0)),(F(2),F(-3)),(F(-4),F(5))]:
 f=fd(fs(AA,a),c)
 for g in [(F(0),F(0)),(F(1),F(2)),(F(-3),F(1))]:
  N=fs(fs((F(8),F(0)),fm(a,f)),fm((F(2),F(0)),fm(d,g)))
  v=fd(N,AA);w=fm(v,v)
  assert fm(fm(AA,AA),w)==fm(N,N)
  assert fm(AA,v)==N
  cases+=1
report={'input_sha256':h(P),'output_sha256':h(O/'candidate233-ir.json'),'unchanged_rows':205,'all_unchanged_row_hashes':checks,'independent_SOS_convolution_matches':True,'coefficient_envelope':'A_N^2+1 for N>=53; coefficient-size statement only','quadratic_parameter_monomials':[list(m) for m in quadratic],'field_inverse_cases':cases,'variables':233,'residuals':207,'monomials':len(profiles),'parameter_terms':len(poly),'degree':4,'content':math.gcd(*poly.values())}
(O/'VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items() if k!='all_unchanged_row_hashes'})
