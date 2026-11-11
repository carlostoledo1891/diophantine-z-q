"""Read-only independent implementation of the primary-fusion finite checks."""
import json,hashlib
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd,lcm
from functools import reduce
P=Path(__file__).resolve().parent
F=Fraction
def read(path):return json.loads(Path(path).read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
cert=read(P/'certificate445.json');old=read(cert['source']);new=read(P/'candidate445-ir.json')
assert sha(cert['source'])=='f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f'
assert sha(P/'candidate445-ir.json')==cert['candidateSha256']
assert sha(P/'polynomial445.json')==cert['polynomialSha256']
def terms(row):return {(x.get('sPower',0),tuple(x['monomial'])):F(x['coefficient']) for x in row['terms']}
def summ(*ps):
 d=defaultdict(F)
 for p in ps:
  for k,c in p.items():d[k]+=c
 return {k:c for k,c in d.items() if c}
def scale(p,n):return {k:c*n for k,c in p.items() if c*n}
def prod(p,q):
 d=defaultdict(F)
 for (s,m),a in p.items():
  for (t,n),b in q.items():d[s+t,tuple(sorted(m+n))]+=a*b
 return {k:c for k,c in d.items() if c}
def atom(n):return {(0,(n,)):F(1)}
def fieldprod(x,y):return summ(prod(x[0],y[0]),scale(prod(x[1],y[1]),2)),summ(prod(x[0],y[1]),prod(x[1],y[0]))
def fieldadd(x,y,sgn=1):return tuple(summ(a,scale(b,sgn)) for a,b in zip(x,y))
def primitive(p):
 den=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*den)) for c in p.values()),0)
 return scale(p,F(den,g)) if g else p
def equivalent(p,q):return primitive(p) in [primitive(q),scale(primitive(q),-1)]
co={x['name']:x['id'] for x in old['coordinates']};oo={x['name']:x for x in old['residuals']};nn={x['name']:x for x in new['residuals']}
hs=[];js=[];zs=[]
for i,c in enumerate(['H','UA','US','UT','UZ']):
 hs.append(tuple(atom(co[f'{c}.chart.h{j}']) for j in range(2)))
 js.append(tuple(atom(co[f'{c}.chart.j{j}']) for j in range(2)))
 zs.append(tuple(atom(co[f'U{i}.z.{j}']) for j in range(2)))
old_expected={};new_expected={}
for i in range(5):
 r=fieldadd(fieldprod(js[i],zs[i]),hs[i])
 for j in range(2):old_expected[f'U{i}.z.definition.{j}']=r[j]
 if i:
  ll=tuple(atom(co[f'L{i}.{j}']) for j in range(2))
  r=fieldadd(fieldprod(zs[0],ll),zs[i],-1)
  t=fieldadd(fieldprod(js[i],ll),fieldprod(hs[i],zs[0]),-1)
  for j in range(2):old_expected[f'L{i}.definition.{j}']=r[j];new_expected[f'L{i}.definition.{j}']=t[j]
t=fieldadd(fieldprod(hs[0],zs[0]),js[0],-1)
for j in range(2):new_expected[f'U0.z.definition.{j}']=t[j]
for n,p in old_expected.items():assert equivalent(terms(oo[n]),p),n
for n,p in new_expected.items():assert terms(nn[n])==p,n
assert set(oo)-set(nn)==set(old_expected)-set(new_expected)
for n in set(oo)-set(old_expected):assert oo[n]==nn[n],n
oldids={co[f'U{i}.z.{j}'] for i in range(5) for j in range(2)}
for n,r in oo.items():
 if n not in old_expected:assert not any(oldids.intersection(t['monomial']) for t in r['terms'])
removed={co[f'U{i}.z.{j}'] for i in range(1,5) for j in range(2)}
assert {c['id'] for c in old['coordinates']}-{c['id'] for c in new['coordinates']}==removed
newco={c['id']:c for c in new['coordinates']}
for c in old['coordinates']:
 if c['id'] in removed:continue
 expected=c.copy()
 if c['id'] in oldids:expected['name']='primary.negativeReciprocalZ0.'+str(c['id']-co['U0.z.0'])
 assert expected==newco[c['id']]
total={}
for r in new['residuals']:
 p=primitive(terms(r));assert all(len(m)<=2 for s,m in p)
 assert not any(removed.intersection(m) for s,m in p)
 total=summ(total,prod(p,p))
assert total==terms(read(P/'polynomial445.json'))
assert len(new['coordinates'])==445 and len(new['residuals'])==422 and len(total)==6568
# The only exceptional-case numerical invariant used in the chart proof.
assert F(3)**2-2==7
print('PASS: exact old/new field rows, every outside row and coordinate, all deleted-variable incidences, complete primitive SOS, 445 variables / 422 residuals / 6568 monomials.')
