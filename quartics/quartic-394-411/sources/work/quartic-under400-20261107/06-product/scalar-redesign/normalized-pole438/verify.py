from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parent/'preparation-zero439/candidate439-ir.json'
def read(f):return json.loads(f.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 factor=F(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*factor for m,v in q.items()}
def add(a,b):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {m:v for m,v in d.items() if v}
old=read(S);new=read(H/'candidate438-ir.json')
assert sha(S)=='135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3'
a={r['name']:p(r['terms']) for r in old['residuals']};b={r['name']:p(r['terms']) for r in new['residuals']}
first=a['scalar.firstConic'];bh=a['scalar.Bh.definition']
expectedFirst={(0,(51,51)):F(1),(0,(51,)):first[(0,(51,526))],(0,()):first[(0,(526,526))],(0,(526,527)):first[(0,(526,527))]}
expectedBh={(0,(51,)):F(17),(0,(51,526)):bh[(0,(51,531))],(0,(52,532)):F(-17)}
assert set(b)==set(a)-{'scalar.t2.definition'}
for name,q in b.items():assert norm(q)==norm(expectedFirst if name=='scalar.firstConic' else expectedBh if name=='scalar.Bh.definition' else a[name]),name
weights={51:1,52:1,53:1,54:1,532:1,527:2,534:2}
targets={'scalar.p2.definition','scalar.firstConic','scalar.Bh.definition','scalar.q2.definition','scalar.secondConic'}
assert {name for name,q in a.items() if any(set(m)&(set(weights)|{531}) for s,m in q)}==targets|{'scalar.t2.definition'}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{531}
for name in targets:
 transformed={}
 for (s,m),v in a[name].items():
  e=2*m.count(531)+sum(weights.get(i,0) for i in m)
  key=s,tuple(sorted(tuple(i for i in m if i!=531)+(526,)*e))
  transformed[key]=transformed.get(key,0)+v
 assert transformed==mul({(0,(526,526)):F(1)},b[name]),name
assert old['fixedParameter']==new['fixedParameter']
total={}
for q in b.values():
 q=norm(q);assert max(len(m) for s,m in q)<=2
 total=add(total,mul(q,q))
assert total==p(read(H/'polynomial438.json')['terms'])
assert len(new['coordinates'])==438 and len(b)==416
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
out={'passed':True,'variables':438,'residuals':416,'monomials':len(total),'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate438-ir.json'),'review':'pending exact-equivalence review and source439 arithmetic review'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
