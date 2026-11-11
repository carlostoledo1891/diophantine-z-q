"""Standalone exact replay and SOS expansion; imports no producer/search."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
from functools import reduce
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
def pol(ts):
 d={}
 for t in ts:
  s=t.get('sPower',0);m=tuple(t['monomial']);assert tuple(sorted(m))==m
  k=s,m;d[k]=d.get(k,Q(0))+Q(t['coefficient'])
 return {k:v for k,v in d.items() if v}
def add(a,b):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,Q(0))+v
 return {k:v for k,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,Q(0))+v*w
 return {k:v for k,v in d.items() if v}
def substitute(p,x,q):
 d={}
 for (s,m),v in p.items():
  z={(s,tuple(i for i in m if i!=x)):v}
  for j in range(m.count(x)):z=mul(z,q)
  d=add(d,z)
 return d
def variables(p):return {v for s,m in p for v in m}
def degree(p):return max((len(m) for s,m in p),default=0)
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items())]
def normalize(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1)
 g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 return {k:v*Q(d,g) for k,v in p.items()}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')

src=read('baseline498.json');cert=read('macaulay-certificate.json');out=read('macaulay-candidate-ir.json')
assert sha('baseline498.json')==cert['baselineSha256']=='e8aea4b56037c0be0a8e9906e377bceea8c7bebd8fc3bf3314366032cfeae1f7'
rows={r['id']:pol(r['terms']) for r in src['residuals']};coords={c['id']:c for c in src['coordinates']}
for op in cert['operations']:
 x=op['coordinate'];pivot=op['pivot'];q=pol(op['replacement']);p=rows[pivot]
 assert x!=0 and not coords[x].get('protected') and x not in variables(q)
 assert p.get((0,(x,))) and all(x not in m or (s,m)==(0,(x,)) for s,m in p)
 assert substitute(p,x,q)=={}
 affected={r for r,p in rows.items() if x in variables(p)}
 assert {z['row'] for z in op['changes']}==affected-{pivot}
 assert len(op['changes'])==len(affected)-1
 changes={}
 for z in op['changes']:
  expect=substitute(rows[z['row']],x,q)
  for multiple in z['multiples']:
   r=multiple['row'];factor=pol(multiple['factor'])
   assert r not in affected and x not in variables(factor)
   expect=add(expect,mul(factor,rows[r]))
  actual=pol(z['result'])
  assert actual==expect and degree(actual)<=2 and x not in variables(actual)
  changes[z['row']]=actual
 rows.update(changes);del rows[pivot];del coords[x]
assert rows=={r['id']:pol(r['terms']) for r in out['residuals']}
assert coords=={c['id']:c for c in out['coordinates']}
assert set(coords)==set().union(*(variables(p) for p in rows.values()))
assert src['fixedParameter']==out['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}
assert coords[0]==src['coordinates'][0]
total={}
for p in rows.values():
 p=normalize(p);items=list(p.items())
 for i,((s,m),a) in enumerate(items):
  for j in range(i,len(items)):
   (t,n),b=items[j];k=s+t,tuple(sorted(m+n))
   total[k]=total.get(k,Q(0))+a*b*(1 if i==j else 2)
total={k:v for k,v in total.items() if v}
assert degree(total)==4 and all(v.denominator==1 for v in total.values())
assert any(s==0 and v==1 for (s,m),v in total.items())
assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
assert (0,(57,57)) not in total and (1,(57,57)) not in total
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
write('candidate470-ir.json',out)
write('polynomial470.json',{'fixedParameter':out['fixedParameter'],'terms':terms(total)})
write('elimination470-certificate.json',cert)
summary={'verified':True,'sourceSha256':sha('baseline498.json'),'candidateSha256':sha('candidate470-ir.json'),
 'certificateSha256':sha('elimination470-certificate.json'),'polynomialSha256':sha('polynomial470.json'),
 'coordinates':len(coords),'witnesses':len(coords)-1,'residuals':len(rows),'degree':4,
 'monomials':len({m for s,m in total}),'formalTerms':len(total),'content':1,
 'largestCoefficient':'16*3^(2^26)','operationCount':len(cert['operations']),
 'proof':'Exact constant pivot with complete affected-row coverage and multiples of unaffected retained rows; reverse reinserts the pivot replacement.'}
assert len(coords)==470 and len(rows)==439
write('VERIFIED470.json',summary);print(json.dumps(summary,indent=2))

