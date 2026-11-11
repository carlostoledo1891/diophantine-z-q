"""Independent literal-row, scaling-identity, incidence and full-SOS check."""
from pathlib import Path
import json,sys,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent));import verify494 as P
c=P.read(H/'certificate398.json');S=Path(c['source'])
assert P.sha(S)==c['sourceSha256']=='eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b'
assert P.sha(H/'candidate398-ir.json')==c['candidateSha256'];assert P.sha(H/'polynomial398.json')==c['polynomialSha256']
old=P.read(S);new=P.read(H/'candidate398-ir.json');before={r['id']:r for r in old['residuals']};after={r['id']:r for r in new['residuals']}
assert P.poly(before[471]['terms'])==P.add(P.mon(505),P.mon(543,544),-2)
q=P.add(P.add(P.add(P.add(P.mon(55,55),P.mon(56,56),6),P.mon(57,57),-2),P.mon(505,505),-3),P.mon(-1,57),-4)
assert P.poly(before[504]['terms'])==q
assert P.poly(before[699]['terms'])==P.add(P.mon(505,549),P.mon(),-1)
anchor=P.add(P.add(P.add(P.add(P.mon(55,55),P.mon(56,56),6),P.mon(57,57),-2),P.mon(544,544),-12),P.mon(-1,57,549),-4)
guard=P.add(P.mon(543,549),P.mon(),-1)
assert P.poly(after[504]['terms'])==anchor;assert P.poly(after[699]['terms'])==guard
# Complete polynomial recovery identity, including the fixed coefficient C.
mapping={55:P.mon(55,543),56:P.mon(56,543),57:P.mon(57,543),505:{(543,544):2}}
lhs=P.add(P.sub(q,mapping),P.mul(P.mon(543,543),anchor),-1)
assert lhs==P.mul({(-1,57,543):4},guard)
uses={i:sorted(ri for ri,r in before.items() if any(i in t['monomial'] for t in r['terms'])) for i in [55,56,57,505,549]}
assert uses=={55:[504],56:[504],57:[504],505:[471,504,699],549:[699]}
assert set(after)==set(before)-{471}
for i in set(before)-{471,504,699}:assert before[i]==after[i]
oc={x['id']:x for x in old['coordinates']};nc={x['id']:x for x in new['coordinates']}
assert set(nc)==set(oc)-{505}
for i in nc:
 expected=oc[i].copy()
 if i in [55,56,57]:expected['name']+='ScaledByG0'
 if i==549:expected['name']='scalar.shiftedS.reciprocal.g0Inverse'
 assert nc[i]==expected
for key in old:
 if key not in {'coordinates','residuals','status'}:assert old[key]==new[key]
total={}
for row in new['residuals']:
 p=P.normalized(P.poly(row['terms']));assert max(sum(x!=-1 for x in m) for m in p)<=2
 tt=list(p.items())
 for i,(m,a) in enumerate(tt):
  for j in range(i,len(tt)):
   n,b=tt[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={m:a for m,a in total.items() if a}
assert total==P.poly(P.read(H/'polynomial398.json')['terms'])
assert {v for m in total for v in m if v!=-1}==set(nc)
assert len(nc)==398 and len(new['residuals'])==367
assert functools.reduce(math.gcd,(abs(v.numerator) for v in total.values()),0)==1
result={'passed':True,'candidateSha256':c['candidateSha256'],'counts':c['counts'],'exactScalingIdentity':True,'completePrivateIncidence':uses,'allOutsideObjectsUnchanged':True,'fullPrimitiveSOS':True,'arithmeticDependency':'nonzero even scalar orbit implies f1!=0; independent review required'}
(H/'verification398.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
