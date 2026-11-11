"""Independent row, incidence, metadata and full sum-of-squares check."""
from pathlib import Path
import sys,json,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[1]))
import verify494 as P
c=P.read(H/'certificate442.json');S=Path(c['source'])
assert P.sha(S)==c['sourceSha256']=='9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1'
assert P.sha(H/'candidate442-ir.json')==c['candidateSha256']
assert P.sha(H/'polynomial442.json')==c['polynomialSha256']
old=P.read(S);new=P.read(H/'candidate442-ir.json')
bn={r['name']:r for r in old['residuals']};nn={r['name']:r for r in new['residuals']}
assert P.poly(bn['Sscalar.f.definition.0']['terms'])==P.add(P.add(P.mon(504),P.mon(543,543),-1),P.mon(544,544),-2)
assert P.poly(bn['Sscalar.f.definition.1']['terms'])==P.add(P.mon(505),P.mon(543,544),-2)
assert P.poly(bn['scalar.shiftedS.reciprocal.f0Inverse.definition']['terms'])==P.add(P.mon(504,549),P.mon(),-1)
assert P.poly(nn['scalar.shiftedS.reciprocal.f1Inverse.definition']['terms'])==P.add(P.mon(505,549),P.mon(),-1)
affected={n for n,r in bn.items() if any(504 in t['monomial'] or 549 in t['monomial'] for t in r['terms'])}
assert affected=={'Sscalar.f.definition.0','scalar.shiftedS.reciprocal.f0Inverse.definition'}
assert set(nn)==(set(bn)-affected)|{'scalar.shiftedS.reciprocal.f1Inverse.definition'}
for n in set(bn)-affected:assert bn[n]==nn[n]
oc={x['id']:x for x in old['coordinates']};nc={x['id']:x for x in new['coordinates']}
assert set(nc)==set(oc)-{504}
for i in nc:
 if i!=549:assert oc[i]==nc[i]
assert dict(oc[549],name='scalar.shiftedS.reciprocal.f1Inverse')==nc[549]
for key in old:
 if key not in {'coordinates','residuals','status'}:assert old[key]==new[key]
polys=[P.poly(r['terms']) for r in new['residuals']]
assert {v for p in polys for m in p for v in m if v!=-1}==set(nc)
assert max(sum(v!=-1 for v in m) for p in polys for m in p)<=2
total={}
for p in polys:
 terms=list(P.normalized(p).items())
 for i,(m,a) in enumerate(terms):
  for j in range(i,len(terms)):
   n,b=terms[j];k=tuple(sorted(m+n));total[k]=total.get(k,0)+a*b*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==P.poly(P.read(H/'polynomial442.json')['terms'])
assert len(nc)==442 and len(polys)==419
assert functools.reduce(math.gcd,(abs(v.numerator) for v in total.values()),0)==1
result={'passed':True,'variables':442,'residuals':419,'degree':max(sum(v!=-1 for v in m) for m in total),'monomials':len(set(tuple(v for v in m if v!=-1) for m in total)),'checks':['literal scalar definitions','complete private incidence','all outside rows and metadata unchanged','full primitive SOS','retained coordinate coverage']}
(H/'verification442.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

