from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'deterministic442/candidate442-ir.json'
def read(f):return json.loads(f.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   key=s+t,tuple(sorted(m+n));d[key]=d.get(key,0)+v*w
 return {m:v for m,v in d.items() if v}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 z=F(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*z for m,v in q.items()}
old=read(S);new=read(H/'candidate439-ir.json')
assert sha(S)=='e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86'
a={r['name']:p(r['terms']) for r in old['residuals']};b={r['name']:p(r['terms']) for r in new['residuals']}
N={(0,(531,)):F(1),(0,(526,526)):F(-1)}
K=a['scalar.preparationT.definition'][(0,(526,528))]
assert K>0
assert a['scalar.preparationT.definition']=={(0,()):F(1),(0,(526,528)):K}
assert a['scalar.t2.definition']=={(0,(50,50)):F(1),(0,(531,)):-K*K}
assert a['scalar.UplusB.definition']=={(0,(526,)):K,(0,(528,531)):K*K,(0,(529,529)):F(1)}
assert set(b)==set(a)-{'scalar.preparationT.definition','scalar.UplusB.definition'}
for name,row in b.items():assert norm(row)==norm(N if name=='scalar.t2.definition' else a[name]),name
assert {name for name,row in a.items() if any(set(m)&{50,528,529} for s,m in row)}=={'scalar.t2.definition','scalar.preparationT.definition','scalar.UplusB.definition'}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{50,528,529}
assert old['fixedParameter']==new['fixedParameter']
total={}
for row in b.values():
 row=norm(row);assert max(len(m) for s,m in row)<=2
 total=add(total,mul(row,row))
assert total==p(read(H/'polynomial439.json')['terms'])
assert len(new['coordinates'])==439 and len(b)==417 and len(total)==6658
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
out={'passed':True,'variables':439,'residuals':417,'monomials':6658,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate439-ir.json'),'semanticInput':'b=-K*v526; preparationSquare=K^2*v531','K':str(K),'inverseMap':'U=b, J=1/b, V=0','arithmeticReview':'pending05'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
