from package_paths import reference_repo
"""Unique 16-coordinate constant lift of candidate498; independent SOS collection."""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent
src=json.loads((H/'candidate498-ir.json').read_text());out=json.loads(json.dumps(src))
out.pop('fixedParameter');out['status']='Candidate ordinary-coefficient lift; same inherited arithmetic scope'
start=max(c['id'] for c in out['coordinates'])+1
rs=max(r['id'] for r in out['residuals'])+1
for j in range(16):
 out['coordinates'].append({'id':start+j,'name':f'constant.c{j}'})
 ts=[{'monomial':[start+j],'sPower':0,'coefficient':'1'},
     {'monomial':[] if j==0 else [start+j-1]*2,'sPower':0,'coefficient':str(-(3**1024) if j==0 else -1)}]
 out['residuals'].append({'id':rs+j,'name':f'constant.definition{j}','terms':ts})
changed=[]
for r in out['residuals']:
 for t in r['terms']:
  if t['sPower']:
   assert t['sPower']==1
   changed.append(r['name']);t['sPower']=0;t['monomial']=sorted(t['monomial']+[start+15])
assert changed==['anchor.translatedEquation']
assert 1024*2**15==2**25
poly={}
for r in out['residuals']:
 items=[(tuple(t['monomial']),Fraction(t['coefficient'])) for t in r['terms']]
 den=reduce(lcm,(c.denominator for m,c in items),1);g=reduce(gcd,(abs(int(c*den)) for m,c in items),0)
 items=[(m,int(c*den/g)) for m,c in items]
 for i,(m,a) in enumerate(items):
  assert len(m)<=2
  for j in range(i,len(items)):
   n,b=items[j];z=tuple(sorted(m+n));poly[z]=poly.get(z,0)+a*b*(1 if i==j else 2)
poly={m:c for m,c in poly.items() if c}
assert len(out['coordinates'])==514 and len(out['residuals'])==483
assert set(x for m in poly for x in m)==set(c['id'] for c in out['coordinates'])
assert poly[()]==3**2048+1005072314676622
assert max(abs(c) for c in poly.values())==poly[()] and poly[()].bit_length()==3247
assert max(map(len,poly))==4 and reduce(gcd,map(abs,poly.values()))==1
def write(n,d):(H/n).write_text(json.dumps(d,indent=2)+'\n', encoding='utf-8', newline='\r\n')
write('candidate514-ir.json',out)
write('polynomial514.json',{'terms':[{'monomial':list(m),'coefficient':str(c)} for m,c in sorted(poly.items())]})
stats={'variables':514,'witnesses':513,'residuals':483,'degree':4,'monomials':len(poly),'content':1,
       'maximumCoefficient':'3^2048+1005072314676622','maximumCoefficientBits':3247,
       'uniqueLift':'c0=3^1024; c(j+1)=cj^2 for j=0,...,14; c15=3^(2^25)',
       'polynomialSha256':hashlib.sha256((H/'polynomial514.json').read_bytes()).hexdigest()}
write('VERIFICATION514.json',stats);print(json.dumps(stats,indent=2))


