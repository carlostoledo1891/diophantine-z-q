"""Three-coordinate scalar correction saving; no imported producer helpers."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
SOURCE=H.parent.parent/'10-combination/rational453-ir.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def add(a,b):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,0)+v
 return {k:v for k,v in d.items() if v}
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {k:v for k,v in d.items() if v}
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1)
 g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 return {k:v*F(d,g) for k,v in p.items()}
def shift(p):
 q={}
 for (s,m),v in p.items():
  t={(s,()):v}
  for i in m:t=mul(t,{(0,(i,)):F(1),(0,()):F(1200)} if i==248 else {(0,(i,)):F(1)})
  q=add(q,t)
 return q
d=json.loads(SOURCE.read_text());source_sha=sha(SOURCE)
assert len(d['coordinates'])==453
old_corr=[r for r in d['residuals'] if r['name'].startswith('correction.')]
assert len(old_corr)==8
removed={58,59,60}
assert all(not any(set(t['monomial'])&removed for t in r['terms']) for r in d['residuals'] if r not in old_corr)
shifted=[]
for r in d['residuals']:
 if r['name']!='inputSquare.definition' and any(248 in t['monomial'] for t in r['terms']):
  r['terms']=terms(shift(parse(r['terms'])));shifted.append(r['name'])
d['residuals']=[r for r in d['residuals'] if r not in old_corr]
prev=None
for n,(i,m) in enumerate(zip([61,62,63,64,65],[3,11,17,35,91])):
 p={(0,(i,i)):F(1)}
 if prev is None:p.update({(0,(i,)):F(-(m+1)),(0,()):F(m)})
 else:p.update({(0,tuple(sorted([i,prev]))):F(-(m+1)),(0,(prev,prev)):F(m)})
 d['residuals'].append({'id':445+n,'name':f'correction.restrictedProduct{n+1}','terms':terms(p),'kind':'structural','block':'scalar_correction_redesign'})
 prev=i
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
for c in d['coordinates']:
 if c['id'] in [61,62,63,64]:c['name']=f'correction.restrictedProduct{c["id"]-60}'
d['status']='Research candidate: beta=2X^2+2403 and five-generator positive scalar correction; non-author arithmetic review required.'
total={}
for r in d['residuals']:
 p=norm(parse(r['terms']));assert max(len(m) for s,m in p)<=2
 total=add(total,mul(p,p))
assert len(d['coordinates'])==450
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
write('candidate450-ir.json',d)
write('polynomial450.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
write('CERTIFICATE.json',{'sourcePath':str(SOURCE),'sourceSha256':source_sha,'candidateSha256':sha(H/'candidate450-ir.json'),'polynomialSha256':sha(H/'polynomial450.json'),'removedCoordinates':sorted(removed),'shiftedRows':shifted,'generators':[3,11,17,35,91],'totalVariables':len(d['coordinates']),'residuals':len(d['residuals']),'monomials':len(total)})
print((H/'CERTIFICATE.json').read_text())
