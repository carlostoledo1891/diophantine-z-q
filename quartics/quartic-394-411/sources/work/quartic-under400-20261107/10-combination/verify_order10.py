"""Independent source, guard, Laurent-circuit, and full-SOS check of495."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def add(a,b,k=1):
 d=a.copy()
 for m,v in b.items():d[m]=d.get(m,0)+k*v
 return {m:v for m,v in d.items() if v}
def mul(a,b):
 d={}
 for m,v in a.items():
  for n,w in b.items():
   key=tuple(sorted(m+n));d[key]=d.get(key,0)+v*w
 return {m:v for m,v in d.items() if v}
def mon(*m):return {tuple(sorted(m)):F(1)}
def norm(a):
 d=reduce(lcm,(v.denominator for v in a.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in a.values()),0)
 scale=F(d,g)*(1 if a[min(a)]>0 else -1)
 return {m:v*scale for m,v in a.items()}
def zero(a,ids):return {m:v for m,v in a.items() if not set(m)&set(ids)}
def eq(x,y):return add(x,y,-1)
d=read('inputs/released498.json');new=read('order10-495-ir.json');cert=read('order10-495-certificate.json');depth=read('inputs/depth519.json')
assert sha('inputs/released498.json')==cert['released498Sha256']=='7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a'
assert sha('order10-495-ir.json')==cert['statistics']['candidateSha256']
rows={r['name']:p(r['terms']) for r in d['residuals']};out={r['name']:p(r['terms']) for r in new['residuals']}
cn={c['name']:c['id'] for c in d['coordinates']};nn={c['name']:c['id'] for c in new['coordinates']};deleted=set();expected={};removed=[]
for k in range(3):
 pre=f'detector{k}.'
 def v(s):return cn[pre+s]
 E,q,q12,q40,q2,q3,q5,R=[v(s) for s in ['eWeight','q1','q12','q40','E1.power2.quadratic','E1.power3.quadratic','E1.power5.quadratic','E12.power2.quadratic']]
 a,b,c,dd,t=[v('toric.'+s) for s in ['a','b','u','v','t']]
 oldeq=[('a',eq(mon(E,a),mon())),('b',eq(mon(E,b),mon(a,a))),('u',eq(mon(b,c),mon(E,q))),('v',eq(mon(b,dd),mon(c,c))),('q12',eq(mon(q3,q12),mon(dd,dd))),('t',eq(mon(q,t),mon(E,R))),('q40',eq(mon(dd,q40),mon(R,t)))]
 for name,r in oldeq:
  key=pre+'toric.'+name+'.definition';assert norm(rows[key])==norm(r);deleted.add(key)
 assert all(not set(m)&{a,b,c,dd,t} for key,r in rows.items() if key not in deleted for m in r)
 for name,r in [('E1.power2',eq(mon(q,q),mon(q2))),('E1.power3',eq(mon(q,q2),mon(q3))),('E1.power5',eq(mon(q2,q3),mon(q5))),('E12.power2',eq(mon(q12,q12),mon(R)))]:
  assert norm(rows[pre+name+'.definition'])==norm(r)
 w0=p(depth['values'][pre+'W.0']['terms']);w1=p(depth['values'][pre+'W.1']['terms']);n=v('normOver2w0');inv=v('w0Inverse');D=v('eDelta.quadratic');B=v('B')
 assert rows[pre+'w0Inverse.definition']==eq(mon(),mul(w0,mon(inv)))
 assert rows[pre+'normOver2w0.definition']==add(add(mul(w0,w0),mul(w1,w1),-2),mul(w0,mon(n)),-2)
 assert zero(rows[pre+'eDelta.definition'],[E])==eq({},mon(D))
 assert zero(rows[pre+'B.definition'],[E,D])==mon(n,n)
 assert zero(rows[pre+'q1.definition'],[q])==eq({},mon(E))
 ne=[('a',eq(mon(E,a),mon(q))),('b',eq(mon(E,b),mon(a,a))),('c',eq(mon(q,c),mon(b,b))),('d',eq(mon(c,dd),mon(q5))),('q10',eq(mon(c,q12),mon(dd,dd))),('q40',eq(mon(c,q40),mon(R,R)))]
 ex={E:(1,0),q:(0,1),q5:(0,5),R:(36,2),a:(-1,1),b:(-3,2),c:(-6,3),dd:(6,2),q12:(18,1),q40:(78,1)}
 for name,r in ne:
  expected[pre+'toric.'+name+'.definition']=r
  accum={}
  for m,vv in r.items():
   e=tuple(sum(ex[i][j] for i in m) for j in [0,1]);accum[e]=accum.get(e,0)+vv
  assert not any(accum.values())
 removed.append(t)
 assert nn[pre+'q10']==q12
 for label,i in [('a',a),('b',b),('c',c),('d',dd)]:assert nn[pre+'order10.'+label]==i
expected.update({name.replace('.E12.','.E10.'):r for name,r in rows.items() if name not in deleted})
assert set(out)==set(expected)
for name,r in out.items():assert norm(r)==norm(expected[name]),name
assert {c['id'] for c in new['coordinates']}=={c['id'] for c in d['coordinates']}-set(removed)
total={}
for r in out.values():
 assert max(sum(i!=-1 for i in m) for m in r)<=2
 items=list(norm(r).items())
 for i,(m,a) in enumerate(items):
  for j in range(i,len(items)):
   n,b=items[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read('order10-495-polynomial.json')['terms'])
assert len(new['coordinates'])==495 and len(out)==464 and len(total)==24657
assert max(sum(i!=-1 for i in m) for m in total)==4
assert {i for m in total for i in m if i!=-1}=={c['id'] for c in new['coordinates']}
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
result={'verified':True,'variables':495,'witnesses':494,'residuals':464,'degree':4,'monomials':24657,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'source':'released498, not the unrelated old proposal498','candidateSha256':sha('order10-495-ir.json'),
 'scope':'All circuit, guard, retained-row, and SOS coefficients checked. The order change uses the separately reviewed arithmetic proof.'}
(H/'order10-495-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
