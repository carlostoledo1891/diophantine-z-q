"""Move the scalar reciprocal nonzero guard to the retained anchor coefficient."""
from pathlib import Path
import sys,json,copy,hashlib
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parents[1]))
import verify494 as P
S=H.parents[2]/'10-combination/scalar443-ir.json'
assert P.sha(S)=='9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1'
old=P.read(S);new=copy.deepcopy(old)
cn={c['name']:c['id'] for c in old['coordinates']}
f0,f1,inv=[cn[n] for n in ['Sscalar.f.0','Sscalar.f.1','scalar.shiftedS.reciprocal.f0Inverse']]
new['coordinates']=[c for c in new['coordinates'] if c['id']!=f0]
for c in new['coordinates']:
 if c['id']==inv:c['name']='scalar.shiftedS.reciprocal.f1Inverse'
new['residuals']=[r for r in new['residuals'] if r['name']!='Sscalar.f.definition.0']
for r in new['residuals']:
 if r['name']=='scalar.shiftedS.reciprocal.f0Inverse.definition':
  r['name']='scalar.shiftedS.reciprocal.f1Inverse.definition'
  for term in r['terms']:term['monomial']=[f1 if x==f0 else x for x in term['monomial']]
new['status']='Candidate pending independent review: scalar f1 guard.'
def write(n,x):(H/n).write_text(json.dumps(x,indent=2)+'\n')
def encode(p):return [{'sPower':m.count(-1),'monomial':[v for v in m if v!=-1],'coefficient':str(c)} for m,c in sorted(p.items())]
write('candidate442-ir.json',new);total={}
for r in new['residuals']:
 p=P.normalized(P.poly(r['terms']));total=P.add(total,P.mul(p,p))
write('polynomial442.json',{'fixedParameter':old['fixedParameter'],'terms':encode(total)})
report={'source':str(S),'sourceSha256':P.sha(S),'candidateSha256':P.sha(H/'candidate442-ir.json'),'polynomialSha256':P.sha(H/'polynomial442.json'),'removedCoordinate':f0,'repurposedCoordinate':inv,'anchorCoefficient':f1,'counts':{'variables':len(new['coordinates']),'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),'degree':max(sum(v!=-1 for v in m) for m in total),'monomials':len(set(tuple(v for v in m if v!=-1) for m in total))}}
write('certificate442.json',report);print(json.dumps(report,indent=2))

