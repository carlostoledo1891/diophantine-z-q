from package_paths import reference_repo
"""Independent complete check of mixed toric transport504->501 and its SOS."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def poly(*ts):return {(0,tuple(sorted(m))):F(c) for c,m in ts}
def normal(q):
 d=reduce(lcm,(v.denominator for v in q.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in q.values()),0)
 k=F(d,g)*(1 if q[min(q)]>0 else -1)
 return {m:v*k for m,v in q.items()}
d=read(H/'candidate504-ir.json');n=read(H/'candidate501-ir.json');cert=read(H/'certificate501.json')
assert sha(H/'candidate504-ir.json')==cert['source504Sha256']=='7c17debaff9a726562be6b7ef843dbc6ca6a0a9d17556158c54ffe5c49ddb0cd'
assert sha(H/'candidate501-ir.json')==cert['statistics']['candidateSha256']
old={r['name']:p(r['terms']) for r in d['residuals']};new={r['name']:p(r['terms']) for r in n['residuals']}
cn={c['name']:c['id'] for c in d['coordinates']};nn={c['name']:c['id'] for c in n['coordinates']}
deleted=set();removed=set();expected={};witness_maps=[]
for k in range(3):
 pre=f'detector{k}.'
 def v(s):return cn[pre+s]
 E,q,q12,q40,Q,R,q2=[v(s) for s in ['eWeight','q1','q12','q40','E1.power3.quadratic','E12.power2.quadratic','E1.power2.quadratic']]
 a,b,u,vv,t,z=[v(s) for s in ['eMinus1','eMinus3','eMinus7','eMinus14.quadratic','eMinus29','eMinus55']]
 names=['eMinus1','eMinus3','eMinus7','eMinus14','eMinus29','eMinus55','q12','q40']
 oldeq=[poly((1,()),(-1,(E,a))),poly((1,(E,b)),(-1,(a,a))),poly((1,(E,u)),(-1,(b,b))),
        poly((1,(u,u)),(-1,(vv,))),poly((1,(E,t)),(-1,(vv,vv))),poly((1,(b,z)),(-1,(t,t))),
        poly((1,(q,u)),(-1,(t,q12))),poly((1,(E,q12)),(-1,(z,q40)))]
 for name,eq in zip(names,oldeq):
  key=pre+name+'.definition';assert normal(old[key])==normal(eq);deleted.add(key)
 for name,eq in [('E1.power2',poly((1,(q,q)),(-1,(q2,)))),('E1.power3',poly((1,(q,q2)),(-1,(Q,)))),('E12.power2',poly((1,(q12,q12)),(-1,(R,))))]:
  assert normal(old[pre+name+'.definition'])==normal(eq)
 internal={a,b,u,vv,t,z}
 assert all(not(set(m)&internal) for name,r in old.items() if name not in deleted for s,m in r)
 # Both versions have E*a=1, hence E nonzero. q=0 in the unchanged
 # q-definition leaves -E. No additional arithmetic nonzero guard is used.
 assert {(s,m):c for (s,m),c in old[pre+'q1.definition'].items() if q not in m}==poly((-1,(E,)))
 eqs=[('a',poly((1,(E,a)),(-1,()))),('b',poly((1,(E,b)),(-1,(a,a)))),
      ('u',poly((1,(b,u)),(-1,(E,q)))),('v',poly((1,(b,vv)),(-1,(u,u)))),
      ('q12',poly((1,(Q,q12)),(-1,(vv,vv)))),('t',poly((1,(q,t)),(-1,(E,R)))),
      ('q40',poly((1,(vv,q40)),(-1,(R,t))))]
 for name,eq in eqs:expected[pre+'toric.'+name+'.definition']=eq
 for name,co in [('a',a),('b',b),('u',u),('v',vv),('t',t)]:assert nn[pre+'toric.'+name]==co
 exponents={E:(1,0),q:(0,1),Q:(0,3),R:(44,2),a:(-1,0),b:(-3,0),u:(4,1),vv:(11,2),t:(45,1),q12:(22,1),q40:(78,1)}
 for name,eq in eqs:
  laurent={}
  for (s,m),c in eq.items():
   assert not s
   ee=tuple(sum(exponents[i][j] for i in m) for j in [0,1]);laurent[ee]=laurent.get(ee,0)+c
  assert not any(laurent.values())
 removed.add(z);witness_maps.append({'detector':k,'newExponents':exponents,'oldPowerExponents':[-1,-3,-7,-14,-29,-55]})
assert set(new)==(set(old)-deleted)|set(expected)
for name,r in new.items():assert normal(r)==normal(expected[name] if name in expected else old[name]),name
assert {c['id'] for c in n['coordinates']}=={c['id'] for c in d['coordinates']}-removed
assert len(n['coordinates'])==501 and len(new)==470
total={}
for r in new.values():
 items=list(normal(r).items())
 assert max(len(m) for s,m in r)<=2
 for i,((s,m),a) in enumerate(items):
  for j in range(i,len(items)):
   (t,nnn),b=items[j];key=(s+t,tuple(sorted(m+nnn)));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read(H/'polynomial501.json')['terms'])
assert len(total)==24724 and max(len(m) for s,m in total)==4
assert {v for s,m in total for v in m}=={c['id'] for c in n['coordinates']}
assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
assert [(m,c) for (s,m),c in total.items() if s==2]==[((57,57),16)]
assert (0,(57,57)) not in total and (1,(57,57)) not in total
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
result={'verified':True,'variables':501,'witnesses':500,'residuals':470,'degree':4,'monomials':24724,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'candidate501-ir.json'),'polynomialSha256':sha(H/'polynomial501.json'),'witnessMaps':witness_maps}
(H/'VERIFICATION501.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='witnessMaps'},indent=2))

