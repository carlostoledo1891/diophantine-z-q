"""Independent literal row/incidence, exponent, and complete SOS check."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;src=H.parent/'three326/candidate326-ir.json'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'
old=json.loads(src.read_bytes());new=json.loads((H/'candidate323-ir.json').read_bytes())
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
def lookup(obj,name):return next(r for r in obj['residuals'] if r['name']==name)
def poly(row):return {tuple(t['monomial']):F(t['coefficient']) for t in row['terms']}
changed=set();gone=set();drop={361,409,457};repurposed=set()
for d,E,e4,e8,e11,e19,e39,e79 in ((0,350,832,356,355,359,369,360),(1,398,833,404,403,407,417,408),(2,446,834,452,451,455,465,456)):
 repurposed|={e11}
 base=poly(lookup(old,f'detector{d}.eWeight.definition'));assert base.pop(())==-1
 R={}
 for m,c in base.items():
  assert E in m;v=list(m);v.remove(E);R[tuple(v)]=c
 square=defaultdict(F);entries=list(R.items())
 for i,(m,c) in enumerate(entries):
  for j in range(i,len(entries)):
   k,v=entries[j];square[tuple(sorted(m+k))]-=c*v*(1 if i==j else 2)
 square[tuple(sorted((e11,E)))]+=1
 expected={f'detector{d}.toric.c.definition':{m:c for m,c in square.items() if c},
           f'four.det{d}.E4':{tuple(sorted((e4,e11))):F(1),(E,):F(-1)},
           f'detector{d}.toric.q10.definition':{tuple(sorted((e19,e11))):F(1),(e8,e8):F(-1)}}
 for name,wanted in expected.items():
  r=lookup(new,name);assert poly(r)==wanted;changed.add(r['id'])
 gone.add(lookup(old,f'detector{d}.E1.power2.definition')['id'])
assert set(o)-set(n)==gone and set(n)-set(o)==set()
assert all(n[i]==r for i,r in o.items() if i not in changed|gone)
for rows in (old['residuals'],new['residuals']):
 assert all(r['id'] in changed|gone for r in rows if any(repurposed.intersection(t['monomial']) for t in r['terms']))
assert all(r['id'] in changed|gone for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms']))
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert set(oc)-set(nc)==drop and set(nc)-set(oc)==set()
for i,c in nc.items():
 expected=dict(oc[i])
 if i in repurposed:expected['name']=c['name']
 assert c==expected
assert len(nc)==323 and len(n)==293
assert {i for r in n.values() for t in r['terms'] for i in t['monomial']}==set(nc)
# Uniquely forced exponents, in solving order; divisor exponent -1 is R.
known={-1,0,1}
for target,left,right,divisor in ((-3,-1,-1,1),(4,1,0,-3),(8,4,4,0),(19,8,8,-3),(39,19,19,-1),(79,39,39,-1),(158,79,79,0),(157,158,-1,0)):
 assert {left,right,divisor}<=known and target==left+right-divisor
 known.add(target)
total=defaultdict(int)
for r in n.values():
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']};den=1;div=0
 for c in p.values():den=lcm(den,c.denominator)
 for c in p.values():div=gcd(div,abs(int(c*den)))
 terms=sorted((m,int(c*den)//div) for m,c in p.items())
 for i,(m,c) in enumerate(terms):
  for j in range(i,len(terms)):
   k,d=terms[j];total[tuple(sorted(m+k))]+=c*d*(1 if i==j else 2)
table=json.loads((H/'polynomial323.json').read_bytes())
actual={tuple([-1]*t['sPower']+t['monomial']):int(t['coefficient']) for t in table['terms']}
assert {m:c for m,c in total.items() if c}==actual
content=0
for c in actual.values():content=gcd(content,abs(c))
assert content==1 and max(len(m) for m in actual if -1 not in m)==4
result={'candidateSha256':hashlib.sha256((H/'candidate323-ir.json').read_bytes()).hexdigest(),'variables':323,'witnesses':322,'rows':293,'monomials':len(actual),'content':1,'literalRowsAndIncidence':True,'exactExponentSolving':True,'fullSOS':True,'arithmeticAcceptance':False}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
