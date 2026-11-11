from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'preparation-zero439/candidate439-ir.json'
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
d=json.loads(S.read_text());weights={51:1,52:1,53:1,54:1,532:1,527:2,534:2}
names={'scalar.p2.definition','scalar.firstConic','scalar.Bh.definition','scalar.q2.definition','scalar.secondConic'}
assert {r['name'] for r in d['residuals'] if any(set(t['monomial'])&(set(weights)|{531}) for t in r['terms'])}==names|{'scalar.t2.definition'}
for row in d['residuals']:
 if row['name'] in names:
  q={}
  for m,v in p(row['terms']).items():
   exponent=m.count(526)+2*m.count(531)+sum(weights.get(i,0) for i in m)-2
   assert exponent>=0
   new=tuple(sorted(tuple(i for i in m if i not in {526,531})+(526,)*exponent))
   q[new]=q.get(new,0)+v
  row['terms']=enc(q)
d['residuals']=[r for r in d['residuals'] if r['name']!='scalar.t2.definition']
d['coordinates']=[c for c in d['coordinates'] if c['id']!=531]
for c in d['coordinates']:
 if c['id'] in weights:c['name']='normalized_'+c['name']
d['status']='Research438: ordinary scalar pole normalized by nonzero stored input after preparation zero; exact equivalence pending review.'
total={}
for row in d['residuals']:
 q=norm(p(row['terms']));total=add(total,mul(q,q))
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
write('candidate438-ir.json',d);write('polynomial438.json',{'fixedParameter':d['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate438-ir.json'),'polynomialSha256':sha(H/'polynomial438.json'),'variables':len(d['coordinates']),'residuals':len(d['residuals']),'monomials':len(total),'weights':weights,'removedCoordinate':531})
print((H/'CERTIFICATE.json').read_text())
