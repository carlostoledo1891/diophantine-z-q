from package_paths import reference_repo
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
src=read('candidate499-ir.json');cert=read('certificate498.json');out=read('candidate498-ir.json')
assert sha('candidate499-ir.json')==cert['source499Sha256']
assert sha('candidate498-ir.json')==cert['statistics']['candidateSha256']
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
 items=list(normalize(p).items())
 for i,((s,m),a) in enumerate(items):
  for j in range(i,len(items)):
   (t,n),b=items[j];k=s+t,tuple(sorted(m+n));total[k]=total.get(k,Q(0))+a*b*(1 if i==j else 2)
total={k:v for k,v in total.items() if v}
assert total==pol(read('polynomial498.json')['terms'])
assert degree(total)==4 and all(v.denominator==1 for v in total.values())
assert any(s==0 and v==1 for (s,m),v in total.items())
assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
assert (0,(57,57)) not in total and (1,(57,57)) not in total
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
assert len(coords)==498 and len(rows)==467 and len(total)==24669
result={'verified':True,'variables':498,'witnesses':497,'residuals':467,'degree':4,'monomials':24669,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha('candidate498-ir.json'),'polynomialSha256':sha('polynomial498.json'),'certificateOperations':len(cert['operations']),
 'scope':'Complete constant-pivot replay, unaffected-row multiples, coordinate coverage, and full SOS; inherited arithmetic not revalidated.'}
write('VERIFICATION498.json',result);print(json.dumps(result,indent=2))
ordinary=read('candidate514-ir.json');oc={c['name']:c['id'] for c in ordinary['coordinates']}
ors={r['name']:pol(r['terms']) for r in ordinary['residuals']};source_rows={r['name']:pol(r['terms']) for r in out['residuals']}
assert set(ors)==set(source_rows)|{f'constant.definition{j}' for j in range(16)}
for name,p in source_rows.items():
 expected={(0,tuple(sorted(m+(oc['constant.c15'],)*s))):v for (s,m),v in p.items()}
 assert ors[name]==expected
for j in range(16):
 rhs={(0,()):Q(-(3**1024))} if not j else {(0,(oc[f'constant.c{j-1}'],)*2):Q(-1)}
 assert ors[f'constant.definition{j}']==add({(0,(oc[f'constant.c{j}'],)):Q(1)},rhs)
assert 1024*2**15==2**25
ototal={}
for p in ors.values():ototal=add(ototal,mul(normalize(p),normalize(p)))
assert ototal==pol(read('polynomial514.json')['terms'])
assert len(ordinary['coordinates'])==514 and len(ors)==483 and len(ototal)==24716
assert variables(ototal)=={c['id'] for c in ordinary['coordinates']}
assert degree(ototal)==4 and reduce(gcd,(abs(v.numerator) for v in ototal.values()),0)==1
assert max(abs(v) for v in ototal.values())==3**2048+1005072314676622
assert (3**2048+1005072314676622).bit_length()==3247
ordinary_result={'verified':True,'variables':514,'witnesses':513,'residuals':483,'degree':4,'monomials':24716,'content':1,
 'maximumCoefficient':'3^2048+1005072314676622','maximumCoefficientBits':3247,
 'source498Sha256':sha('candidate498-ir.json'),'candidate514Sha256':sha('candidate514-ir.json'),'polynomial514Sha256':sha('polynomial514.json'),
 'scope':'Independent exact constant lift and all ordinary coefficient checks.'}
write('INDEPENDENT514.json',ordinary_result);print(json.dumps(ordinary_result,indent=2))

