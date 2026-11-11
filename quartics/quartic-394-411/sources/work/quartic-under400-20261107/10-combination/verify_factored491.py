"""Independent checker for transport onto the frozen 498-variable source."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,functools
H=Path(__file__).resolve().parent

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def poly(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts if F(t['coefficient'])}
def add(a,b,k=F(1)):
 r=a.copy()
 for m,c in b.items():r[m]=r.get(m,F(0))+k*c
 return {m:c for m,c in r.items() if c}
def mul(a,b):
 r={}
 for m,c in a.items():
  for n,d in b.items():
   k=tuple(sorted(m+n));r[k]=r.get(k,F(0))+c*d
 return {m:c for m,c in r.items() if c}
def mon(*vs):return {tuple(sorted(vs)):F(1)}
def sub(a,mp):
 r={}
 for m,c in a.items():
  p={():c}
  for v in m:p=mul(p,mp.get(v,mon(v)))
  r=add(r,p)
 return r
def normalized(a):
 d=functools.reduce(math.lcm,(v.denominator for v in a.values()),1);g=functools.reduce(math.gcd,(abs(v.numerator*(d//v.denominator)) for v in a.values()),0)
 return {m:v*F(d,g) for m,v in a.items()}
def main():
 cert=read(H/'combined491-certificate.json');p=H/'order10-495-ir.json';assert sha(p)==cert['source495Sha256']
 assert sha(H/'combined491-ir.json')==cert['statistics']['candidateSha256'];assert sha(H/'combined491-polynomial.json')==cert['statistics']['polynomialSha256']
 old=read(p);new=read(H/'combined491-ir.json');before={r['id']:poly(r['terms']) for r in old['residuals']};after={r['id']:poly(r['terms']) for r in new['residuals']};cn={c['name']:c['id'] for c in old['coordinates']};rn={r['name']:r['id'] for r in old['residuals']}
 maps={};deleted=set();removed=set();scalings={}
 for prefix in ['detector0','detector1','detector2','scalar']:
  normalized_name=prefix+'.normalized.' if prefix!='scalar' else prefix+'.'
  t,t2,q,q2,f=[cn[normalized_name+x] for x in ['s','s2.quadratic','q','q2.quadratic','Bh.quadratic']]
  b=cn[prefix+'.B' if prefix!='scalar' else 'scalar.b.quadratic']
  rb,rq,rt,rc=[rn[prefix+'.'+n] for n in ['Bh.definition','q2.definition','s2.definition','secondConic']]
  maps[f]=mon(t,f);maps[q]=mon(t,q);maps[q2]=mon(t,t,q2);maps[t2]=mon(t,t)
  deleted.add(rt);removed.add(t2);scalings[rq]=mon(t,t);scalings[rc]=mon(t,t)
  assert before[rq]==add(mon(q,q),mon(q2),-1) and before[rt]==add(mon(t,t),mon(t2),-1)
  branch=sub(before[rc],{t:{},t2:{},q2:mon(q,q)})
  if prefix!='scalar':assert branch==add({tuple(sorted((b,q,q))):F(17)},mon(f,f),867)
  else:
   A=branch[tuple(sorted((b,q,q)))];K=A/17
   assert K>0 and branch==add({tuple(sorted((b,q,q))):A},mon(f,f),-3*A*A)
   # The stored b satisfies semantic B=-K*b>0 in completeness.
  lift={t:{},q:{},q2:{},f:{}}
  assert sub(after[rq],lift)=={} and sub(after[rc],lift)=={}
  assert sub(after[rb],lift)==sub(before[rb],{f:{}})
 assert deleted=={rn[n] for n in cert['deletedRows']} and removed==set(cert['removedCoordinates'])
 assert set(after)==set(before)-deleted
 for ri,p in before.items():assert sub(p,maps)==({} if ri in deleted else mul(scalings.get(ri,mon()),after[ri])),ri
 oldids={c['id'] for c in old['coordinates']};newids={c['id'] for c in new['coordinates']}
 assert newids==oldids-removed and len(newids)==491 and len(after)==460
 assert old['coordinates'][0]==new['coordinates'][0] and old['fixedParameter']==new['fixedParameter']
 assert {v for p in after.values() for m in p for v in m if v!=-1}==newids
 assert all(sum(v!=-1 for v in m)<=2 for p in after.values() for m in p)
 total={}
 for p in after.values():
  terms=list(normalized(p).items())
  for i,(m,c) in enumerate(terms):
   for j in range(i,len(terms)):
    n,d=terms[j];z=tuple(sorted(m+n));total[z]=total.get(z,F(0))+c*d*(1 if i==j else 2)
 total={m:c for m,c in total.items() if c}
 assert total==poly(read(H/'combined491-polynomial.json')['terms'])
 assert max(sum(v!=-1 for v in m) for m in total)==4
 assert functools.reduce(math.gcd,(abs(v.numerator) for m,v in total.items() if -1 not in m),0)==1
 assert len({tuple(v for v in m if v!=-1) for m in total})==24641
 assert {m:v for m,v in total.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
 assert (57,57) not in total and (-1,57,57) not in total
 assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
 assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
 print(json.dumps({'verified':True,'variables':491,'witnesses':490,'residuals':460,'degree':4,'monomials':24641,'content':1,'maxCoefficient':'16*3^(2^26)','sourceSha256':cert['source495Sha256'],'candidateSha256':cert['statistics']['candidateSha256'],'polynomialSha256':cert['statistics']['polynomialSha256'],'scope':'algebraic soundness and explicit positive-pole completeness transport; independent arithmetic acceptance pending'},indent=2))
if __name__=='__main__':main()
