from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'depth24-448/candidate448-ir.json'
def parse(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(p.items()) if v]
def add(a,b):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   z=tuple(sorted(m+n));d[z]=d.get(z,0)+v*w
 return {m:v for m,v in d.items() if v}
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 return {m:v*F(d,g) for m,v in p.items()}
def translate(p):
 d={}
 for m,v in p.items():
  t={():v}
  for i in m:t=mul(t,{(248,):F(102),(0,):F(102),():F(76)} if i==248 else {(i,):F(1)})
  d=add(d,t)
 return d
d=json.loads(S.read_text());corr=[r for r in d['residuals'] if r['name'].startswith('correction.')]
removed={61,62,63,64};assert len(corr)==5
assert not any(set(t['monomial'])&removed for r in d['residuals'] if r not in corr for t in r['terms'])
changed=[]
for row in d['residuals']:
 if row['name']!='inputSquare.definition' and any(248 in t['monomial'] for t in row['terms']):
  row['terms']=enc(translate(parse(row['terms'])));changed.append(row['name'])
d['residuals']=[r for r in d['residuals'] if r not in corr]
d['residuals'].append({'id':445,'name':'correction.singleChoice','terms':enc({(65,65):F(1),(65,):F(-33066),():F(1090089)}),'kind':'structural','block':'one_correction'})
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
for c in d['coordinates']:
 if c['id']==65:c['name']='correction.singleChoice'
d['status']='Research444: beta=51*(2X+1)^2+2504 and correction33or33033; root authored arithmetic; non-author review pending.'
total={}
for row in d['residuals']:
 p=norm(parse(row['terms']));total=add(total,mul(p,p))
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
write('candidate444-ir.json',d);write('polynomial444.json',{'fixedParameter':d['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate444-ir.json'),'polynomialSha256':sha(H/'polynomial444.json'),'variables':len(d['coordinates']),'residuals':len(d['residuals']),'monomials':len(total),'changedInputConsumers':changed,'removedCoordinates':sorted(removed),'correctionChoices':[33,33033]})
print((H/'CERTIFICATE.json').read_text())
