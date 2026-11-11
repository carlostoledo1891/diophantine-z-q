"""Independent finite checks for the shifted-label five-generator correction."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,gcd,lcm
from functools import reduce
import hashlib,json
H=Path(__file__).resolve().parent
S=H.parent.parent/'10-combination/rational453-ir.json'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(S)=='f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f'
assert sha(H/'candidate450-ir.json')=='31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6'
def poly(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):Q(t['coefficient']) for t in ts}
def normalize(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1)
 g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 s=Q(d,g)*(1 if p[min(p)]>0 else -1)
 return {m:v*s for m,v in p.items()}
def shifted(p):
 out={}
 for m,v in p.items():
  n=m.count(248);rest=tuple(i for i in m if i!=248)
  for k in range(n+1):
   new=tuple(sorted(rest+(248,)*k));out[new]=out.get(new,0)+v*comb(n,k)*1200**(n-k)
 return {m:v for m,v in out.items() if v}
old=read(S);new=read(H/'candidate450-ir.json')
o={r['name']:poly(r['terms']) for r in old['residuals']}
n={r['name']:poly(r['terms']) for r in new['residuals']}
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in old['coordinates']}-{58,59,60}
expected={name:p if name=='inputSquare.definition' else shifted(p) for name,p in o.items() if not name.startswith('correction.')}
previous=None
for k,(i,g) in enumerate(zip([61,62,63,64,65],[3,11,17,35,91]),1):
 p={(i,i):Q(1)}
 if previous is None:p.update({(i,):Q(-g-1),():Q(g)})
 else:p.update({(previous,i):Q(-g-1),(previous,previous):Q(g)})
 expected[f'correction.restrictedProduct{k}']=p
 previous=i
assert set(n)==set(expected)
for name,p in n.items():assert normalize(p)==normalize(expected[name]),name
for name,p in o.items():
 if not name.startswith('correction.'):assert not any(set(m)&set(range(58,65)) for m in p),name
assert n['inputSquare.definition']==o['inputSquare.definition']
assert old['fixedParameter']==new['fixedParameter']
def val(a,p):
 v=0
 while a%p==0:a//=p;v+=1
 return v,a
def squareclass(a):
 v,u=val(a,2);bits=[v%2,int(u%8 in (3,7)),int(u%8 in (3,5))]
 for p in [3,17]:
  v,u=val(a,p);bits +=[v%2,int(pow(u%p,(p-1)//2,p)!=1)]
 return tuple(bits)
def xor(a,b):return tuple(x^y for x,y in zip(a,b))
gens=[3,11,17,35,91];vectors=[squareclass(g) for g in gens]
span={tuple([0]*7):1}
for g,v in zip(gens,vectors):
 for oldv,product in list(span.items()):
  nv=xor(oldv,v);assert nv not in span
  span[nv]=product*g
assert len(span)==32
assert set(span)=={tuple([0,a,a,b,c,d,e]) for a in [0,1] for b in [0,1] for c in [0,1] for d in [0,1] for e in [0,1]}
def r(beta):return beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1)
q2=[]
# beta modulo128 depends only on X modulo64; v2(r) is exactly2 or4.
for x in range(64):
 a=r(2*x*x+2403);v,u=val(a,2)
 assert (v,u%8)==((2,1) if x%2==0 else (4,3))
 q2.append([x,v,u%8])
# Exhaustive 32 classes, independent of any integer-X samples at3 or17.
for bits,c in span.items():assert xor(bits,squareclass(c))==tuple([0]*7)
total={}
for p in n.values():
 p=normalize(p);items=list(p.items())
 assert max(sum(i!=-1 for i in m) for m in p)<=2
 for k,(m,v) in enumerate(items):
  for j in range(k,len(items)):
   z,w=items[j];key=tuple(sorted(m+z))
   total[key]=total.get(key,0)+v*w*(1 if j==k else 2)
total={m:v for m,v in total.items() if v}
assert total==poly(read(H/'polynomial450.json')['terms'])
assert len(new['coordinates'])==450 and len(n)==427 and len(total)==6593
assert max(sum(i!=-1 for i in m) for m in total)==4
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v.numerator).bit_length() for m,v in total.items() if m.count(-1)<2)<2048
assert {i for m in total for i in m if i!=-1}=={c['id'] for c in new['coordinates']}
out={'passed':True,'variables':450,'residuals':427,'monomials':6593,'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate450-ir.json'),'squareclassGenerators':dict(zip(map(str,gens),vectors)),'all32ClassesCovered':True,'Q2period64Table':q2,'sourceSha256':sha(S),'arithmeticReviewStatus':'Author proof requires non-author review.'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='Q2period64Table'},indent=2))
