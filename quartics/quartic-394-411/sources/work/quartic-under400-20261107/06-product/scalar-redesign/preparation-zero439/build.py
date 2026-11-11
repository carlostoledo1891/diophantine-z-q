from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'deterministic442/candidate442-ir.json'
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def enc(q):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(q.items()) if v]
def add(a,b):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   k=tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {m:v for m,v in d.items() if v}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 return {m:v*F(d,g) for m,v in q.items()}
d=json.loads(S.read_text());removed={50,528,529};changed={'scalar.t2.definition','scalar.preparationT.definition','scalar.UplusB.definition'}
assert {r['name'] for r in d['residuals'] if any(set(t['monomial'])&removed for t in r['terms'])}==changed
d['residuals']=[r for r in d['residuals'] if r['name'] not in {'scalar.preparationT.definition','scalar.UplusB.definition'}]
for r in d['residuals']:
 if r['name']=='scalar.t2.definition':r['terms']=enc({(531,):F(1),(526,526):F(-1)})
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
d['status']='Research439: scalar preparation zero after simultaneous real and finite-place preparation; independent arithmetic review required.'
total={}
for r in d['residuals']:
 q=norm(p(r['terms']));total=add(total,mul(q,q))
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
write('candidate439-ir.json',d);write('polynomial439.json',{'fixedParameter':d['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate439-ir.json'),'polynomialSha256':sha(H/'polynomial439.json'),'variables':len(d['coordinates']),'residuals':len(d['residuals']),'monomials':len(total),'removedCoordinates':sorted(removed)})
print((H/'CERTIFICATE.json').read_text())
