from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'root449/candidate449-ir.json'
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):Q(t['coefficient']) for t in ts}
def read(f):return json.loads(f.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 z=Q(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*z for m,v in q.items()}
assert sha(S)=='02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549'
old=read(S);new=read(H/'candidate448-ir.json')
a={r['name']:p(r['terms']) for r in old['residuals']};b={r['name']:p(r['terms']) for r in new['residuals']}
r={None:-99006679260,248:-82479248,487:-21050600,488:-7629700,489:-45771136}
root={(0,(542,604)):Q(1),(0,(540,540)):Q(-1)}
node={(0,(540,604)):Q(1),(0,(508,508)):Q(-1)}
for i,v in r.items():
 root[(0,(541,) if i is None else (i,541))]=Q(-v)
 node[(0,(539,) if i is None else (i,539))]=Q(-v)
expected={'reduced_scalar.ratio_node_squared':{(0,(541,)):Q(1),(0,(311,311)):Q(-1),(0,(312,312)):Q(8)},'reduced_scalar.root':root,'scalar.ratio_node.consolidated_denominator':node}
assert set(b)==set(a)-{'scalar.r_power_64.definition'}
for name,row in b.items():assert norm(row)==norm(expected.get(name,a[name])),name
assert {name for name,row in a.items() if any(605 in m for s,m in row)}=={'scalar.r_power_64.definition','scalar.ratio_node.consolidated_denominator'}
assert {name for name,row in a.items() if any(541 in m for s,m in row)}=={'reduced_scalar.ratio_node_squared','reduced_scalar.root'}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{605}
assert old['fixedParameter']==new['fixedParameter']
total={}
for row in b.values():
 row=norm(row);assert max(len(m) for s,m in row)<=2
 items=list(row.items())
 for i,((s,m),v) in enumerate(items):
  for j in range(i,len(items)):
   (t,n),w=items[j];key=s+t,tuple(sorted(m+n));total[key]=total.get(key,0)+v*w*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read(H/'polynomial448.json')['terms'])
assert len(new['coordinates'])==448 and len(b)==425
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
# Exact rational check of the unchanged anchor margin, using log2(80)<7.
assert Q(5,24)*Q(50331647,2)>2093966+7
assert Q(191,8)>23 and Q(187,8)>23
out={'passed':True,'variables':448,'residuals':425,'monomials':len(total),'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate448-ir.json'),'arithmeticReview':'pending'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
