"""Remove the scalar anchor coefficient by scaling its private witnesses."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,copy
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent));import verify494 as P
S=H.parents[1]/'10-combination/combined399-ir.json'
assert P.sha(S)=='eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b'
old=P.read(S);new=copy.deepcopy(old);rn={r['name']:r for r in new['residuals']}
def encode(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(c)} for m,c in sorted(p.items())]
anchor=P.add(P.add(P.add(P.mon(55,55),P.mon(56,56),6),P.mon(57,57),-2),P.mon(544,544),-12)
anchor=P.add(anchor,P.mon(-1,57,549),-4)
rn['anchor.translatedEquation']['terms']=encode(anchor)
rn['scalar.shiftedS.reciprocal.f1Inverse.definition']['name']='scalar.shiftedS.reciprocal.g0Inverse.definition'
rn['scalar.shiftedS.reciprocal.f1Inverse.definition']['terms']=encode(P.add(P.mon(543,549),P.mon(),-1))
new['residuals']=[r for r in new['residuals'] if r['name']!='Sscalar.f.definition.1']
new['coordinates']=[c for c in new['coordinates'] if c['id']!=505]
for c in new['coordinates']:
 if c['id'] in [55,56,57]:c['name']+='ScaledByG0'
 if c['id']==549:c['name']='scalar.shiftedS.reciprocal.g0Inverse'
new['status']='Candidate pending independent review: scaled scalar anchor.'
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
write('candidate398-ir.json',new);total={}
for row in new['residuals']:
 p=P.normalized(P.poly(row['terms']));total=P.add(total,P.mul(p,p))
write('polynomial398.json',{'fixedParameter':new['fixedParameter'],'terms':encode(total)})
cert={'source':str(S),'sourceSha256':P.sha(S),'candidateSha256':P.sha(H/'candidate398-ir.json'),'polynomialSha256':P.sha(H/'polynomial398.json'),'removedCoordinate':505,'repurposedCoordinates':[55,56,57,549],'counts':{'variables':len(new['coordinates']),'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),'degree':max(sum(x!=-1 for x in m) for m in total),'monomials':len({tuple(x for x in m if x!=-1) for m in total})}}
write('certificate398.json',cert);print(json.dumps(cert,indent=2))
