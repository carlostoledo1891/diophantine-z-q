"""Independent row and sum-of-squares verification for the scalar-root change."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 factor=F(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*factor for m,v in q.items()}
def add(a,b,k=1):
 out=a.copy()
 for m,v in b.items():out[m]=out.get(m,0)+k*v
 return {m:v for m,v in out.items() if v}
def mul(a,b):
 out={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   key=s+t,tuple(sorted(m+n));out[key]=out.get(key,0)+v*w
 return {m:v for m,v in out.items() if v}
def var(i):return {(0,(i,)):F(1)}
old=read(H.parent/'candidate450-ir.json');new=read(H/'candidate449-ir.json')
assert sha(H.parent/'candidate450-ir.json')=='31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6'
assert sha(H/'candidate449-ir.json')=='02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549'
o={r['name']:p(r['terms']) for r in old['residuals']};n={r['name']:p(r['terms']) for r in new['residuals']}
r={(0,()):F(-99006679260),(0,(248,)):F(-82479248),(0,(487,)):F(-21050600),(0,(488,)):F(-7629700),(0,(489,)):F(-45771136)}
q2={(0,(311,311)):F(1),(0,(312,312)):F(-8)}
assert norm(o['reduced_scalar.constant_node'])==norm(add(add(mul(r,var(536)),r,-1),q2,-1))
assert norm(o['reduced_scalar.root'])==norm(add(add(var(542),mul(var(536),var(536)),-1),mul(r,var(541)),-1))
assert norm(o['reduced_scalar.ratio_node_squared'])==norm(add(var(541),mul(var(540),var(540)),-1))
want=add(add(mul(r,var(542)),q2,-1),mul(r,var(541)),-1)
assert set(n)==set(o)-{'reduced_scalar.constant_node'}
for name,pol in n.items():assert norm(pol)==norm(want if name=='reduced_scalar.root' else o[name]),name
assert {name for name,pol in o.items() if any(536 in m for s,m in pol)}=={'reduced_scalar.constant_node','reduced_scalar.root'}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{536}
assert new['fixedParameter']==old['fixedParameter']
total={}
for pol in n.values():
 q=norm(pol);assert max(len(m) for s,m in q)<=2
 items=list(q.items())
 for i,((s,m),v) in enumerate(items):
  for j in range(i,len(items)):
   (t,z),w=items[j];key=s+t,tuple(sorted(m+z))
   total[key]=total.get(key,0)+v*w*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read(H/'polynomial449.json')['terms'])
assert len(new['coordinates'])==449 and len(n)==426 and len(total)==6582
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
assert {i for s,m in total for i in m}=={c['id'] for c in new['coordinates']}
out={'passed':True,'variables':449,'residuals':426,'monomials':6582,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate449-ir.json'),'arithmeticStatus':'author proof; non-author review pending'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
