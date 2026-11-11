from package_paths import reference_repo
"""Add only the scalar fixed-difference reciprocal chart to frozen505."""
from pathlib import Path
import json,hashlib
from build import pol,terms,norm,remap
H=Path(__file__).resolve().parent;W=H.parent;R=reference_repo()
src=H/'candidate505-ir.json';proposal=W/'08-denominators/candidate-521-ir.json'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966'
d=json.loads(src.read_text());patch=json.loads(proposal.read_text())
b=json.loads((R/'quartics/quartic-523-540/final523_540/symbolic523/integer-candidate-ir.json').read_text())
cn={c['name']:c['id'] for c in d['coordinates']};mp={c['id']:cn[c['name']] for c in b['coordinates'] if c['name'] in cn}
oldprefix=tuple('scalar.shiftedS.'+s for s in ['dxInverse','slope','slopeSquare','yProduct'])
removed=[c['id'] for c in d['coordinates'] if c['name'].startswith(oldprefix)]
deleted=[r['name'] for r in d['residuals'] if r['name'].startswith(oldprefix)]
changed=[f'Sscalar.{s}.definition.{j}' for s in ['f','z'] for j in range(2)]
br={r['name']:r for r in b['residuals']};dr={r['name']:r for r in d['residuals']};pr={r['name']:r for r in patch['residuals']}
for name in changed+deleted:
 oldp=remap(pol(br[name]['terms']),mp)
 # The mixed-depth compiler scales this private ordinate-product coordinate
 # by two. It is among the eight coordinates deleted by the new chart.
 private=cn['scalar.shiftedS.yProduct.1.quadratic']
 oldp={key:c*2**key[1].count(private) for key,c in oldp.items()}
 assert norm(pol(dr[name]['terms']))==norm(oldp),name
for c in patch['coordinates']:
 if c['name'].startswith('scalar.shiftedS.reciprocal.'):
  i=max(cc['id'] for cc in d['coordinates'])+1;mp[c['id']]=i;d['coordinates'].append(dict(c,id=i))
for name in changed:dr[name]['terms']=terms(remap(pol(pr[name]['terms']),mp))
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[r for r in d['residuals'] if r['name'] not in deleted]
for r in patch['residuals']:
 if r['name'].startswith('scalar.shiftedS.reciprocal.'):
  i=max(rr['id'] for rr in d['residuals'])+1;d['residuals'].append(dict(r,id=i,terms=terms(remap(pol(r['terms']),mp))))
total={}
for r in d['residuals']:
 p=norm(pol(r['terms']))
 for (s,m),a in p.items():
  for (t,n),bb in p.items():
   k=(s+t,tuple(sorted(m+n)));total[k]=total.get(k,0)+a*bb
total={k:v for k,v in total.items() if v}
assert len(d['coordinates'])==504 and len(d['residuals'])==473
assert {i for s,m in total for i in m}=={c['id'] for c in d['coordinates']}
assert max(len(m) for s,m in total)==4
assert [(m,c) for (s,m),c in total.items() if s==2]==[((57,57),16)]
assert any(s==0 and c==1 for (s,m),c in total.items())
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n', encoding='utf-8', newline='\r\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
write('candidate504-ir.json',d);write('polynomial504.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':504,'witnesses':503,'residuals':473,'degree':4,'monomials':len(total),'content':1,
       'largestCoefficient':'16*3^(2^26)','candidateSha256':sha(H/'candidate504-ir.json'),'polynomialSha256':sha(H/'polynomial504.json')}
write('certificate504.json',{'source505Sha256':sha(src),'proposal08Sha256':sha(proposal),'coordinateMap':mp,'privateCoordinateScale':{'source':'scalar.shiftedS.yProduct.1.quadratic','factor':2},'removedCoordinates':removed,'deletedRows':deleted,'changedRows':changed,'statistics':stats})
print(json.dumps(stats,indent=2))
