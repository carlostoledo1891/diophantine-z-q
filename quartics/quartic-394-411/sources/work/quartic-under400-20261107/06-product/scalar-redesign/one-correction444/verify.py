from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm,comb
import json,hashlib
H=Path(__file__).resolve().parent;S=H.parent/'depth24-448/candidate448-ir.json'
PROOF=H.parent.parent.parent/'00-root/one-correction/PROPOSAL.md'
def read(f):return json.loads(f.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def norm(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 s=F(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*s for m,v in q.items()}
def translated(q):
 z={}
 for (s,m),v in q.items():
  n=m.count(248);rest=tuple(i for i in m if i!=248)
  for nx in range(n+1):
   for ny in range(n-nx+1):
    nc=n-nx-ny;key=s,tuple(sorted(rest+(0,)*nx+(248,)*ny))
    value=v*comb(n,nx)*comb(n-nx,ny)*102**(nx+ny)*76**nc
    z[key]=z.get(key,0)+value
 return {m:v for m,v in z.items() if v}
old=read(S);new=read(H/'candidate444-ir.json')
assert sha(S)=='e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609'
assert sha(PROOF)=='495ffb791c149bb6b2ee6fa1f4988aa8583fea383efd0e4197436fe6bab2b9a6'
a={r['name']:p(r['terms']) for r in old['residuals']};b={r['name']:p(r['terms']) for r in new['residuals']}
expected={name:q if name=='inputSquare.definition' else translated(q) for name,q in a.items() if not name.startswith('correction.')}
expected['correction.singleChoice']={(0,(65,65)):F(1),(0,(65,)):F(-33-33033),(0,()):F(33*33033)}
assert set(b)==set(expected)
for name,q in b.items():assert norm(q)==norm(expected[name]),name
assert b['inputSquare.definition']==a['inputSquare.definition']
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{61,62,63,64}
assert not any(set(m)&{61,62,63,64} for name,q in a.items() if not name.startswith('correction.') for s,m in q)
assert old['fixedParameter']==new['fixedParameter']
odd_rows=[name for name in a if name.startswith('A.odd.')];assert len(odd_rows)==4
assert all(a[name]==b[name] for name in odd_rows)
def val(n,q):
 v=0
 while n%q==0:n//=q;v+=1
 return v,n
def square(n,q):
 v,u=val(n,q)
 return v%2==0 and (u%8==1 if q==2 else pow(u%q,(q-1)//2,q)==1)
for x in range(306):
 t=2*x+1;beta=51*t*t+2504
 assert beta==204*x*x+204*x+2555
 r=beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1)
 c=33033 if t%3==0 else 33
 assert all(square(c*r,q) for q in [2,3,17])
 v2,u2=val(r,2);v3,u3=val(r,3)
 assert v2==2 and u2%8==1 and v3==1 and u3%3==(1+t*t)%3 and r%17==15
assert 51==3*17 and (51%2)==1 and 2504%2==0
total={}
for q in b.values():
 q=norm(q);assert max(len(m) for s,m in q)<=2;items=list(q.items())
 for i,((s,m),v) in enumerate(items):
  for j in range(i,len(items)):
   (t,n),w=items[j];key=s+t,tuple(sorted(m+n));total[key]=total.get(key,0)+v*w*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read(H/'polynomial444.json')['terms'])
assert len(new['coordinates'])==444 and len(b)==421
assert max(len(m) for s,m in total)==4
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(s,m,v) for (s,m),v in total.items() if s==2]==[(2,(57,57),16)]
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s<2)<2048
out={'passed':True,'variables':444,'residuals':421,'monomials':len(total),'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate444-ir.json'),'sourceProofSha256':sha(PROOF),'oddRootRowsPreserved':odd_rows,'arithmeticReview':'pending03'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
