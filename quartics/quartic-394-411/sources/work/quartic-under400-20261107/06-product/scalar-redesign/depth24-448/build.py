from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'root449/candidate449-ir.json'
def parse(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(p.items()) if v]
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def times(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   z=tuple(sorted(m+n));d[z]=d.get(z,0)+v*w
 return {m:v for m,v in d.items() if v}
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 return {m:v*F(d,g) for m,v in p.items()}
data=json.loads(S.read_text());old={r['name']:r for r in data['residuals']}
r={():F(-99006679260),(248,):F(-82479248),(487,):F(-21050600),(488,):F(-7629700),(489,):F(-45771136)}
q2={(311,311):F(1),(312,312):F(-8)}
changed={
 'reduced_scalar.ratio_node_squared':add({(541,):F(1)},q2,-1),
 'reduced_scalar.root':add({(542,604):F(1),(540,540):F(-1)},times(r,{(541,):F(1)}),-1),
 'scalar.ratio_node.consolidated_denominator':add({(540,604):F(1),(508,508):F(-1)},times(r,{(539,):F(1)}),-1)}
assert {x['name'] for x in data['residuals'] if any(605 in t['monomial'] for t in x['terms'])}=={'scalar.r_power_64.definition','scalar.ratio_node.consolidated_denominator'}
assert {x['name'] for x in data['residuals'] if any(541 in t['monomial'] for t in x['terms'])}=={'reduced_scalar.ratio_node_squared','reduced_scalar.root'}
data['residuals']=[x for x in data['residuals'] if x['name']!='scalar.r_power_64.definition']
for row in data['residuals']:
 if row['name'] in changed:row['terms']=enc(changed[row['name']])
data['coordinates']=[c for c in data['coordinates'] if c['id']!=605]
for c in data['coordinates']:
 if c['id']==541:c['name']='reduced_scalar.H_norm_squared'
data['status']='Research448: scalar depth24 with repurposed norm-square slot and five forward contact powers; non-author review required.'
total={}
for row in data['residuals']:
 p=norm(parse(row['terms']));total=add(total,times(p,p))
def write(n,d):(H/n).write_text(json.dumps(d,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
write('candidate448-ir.json',data);write('polynomial448.json',{'fixedParameter':data['fixedParameter'],'terms':enc(total)})
write('CERTIFICATE.json',{'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate448-ir.json'),'polynomialSha256':sha(H/'polynomial448.json'),'variables':len(data['coordinates']),'residuals':len(data['residuals']),'monomials':len(total),'removedCoordinate':605,'repurposedCoordinate':541,'changedRows':list(changed)})
print((H/'CERTIFICATE.json').read_text())
