import json,sys,hashlib,math
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
D=B/'work/quartic238-optimization-20261110/resume-20261110/joint-root-sparse-111';P=D.parent/'joint-root-factor-110/candidate223-ir.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'MANIFEST.json')=='9dd61dce4126ea8fb85e5b7992346e40ce9d96cc56c4f46c3f0e8ee1f4ee3bc0'
for x in json.loads((D/'MANIFEST.json').read_bytes())['members']:assert sha(D/x['path'])==x['sha256']and(D/x['path']).stat().st_size==x['bytes']
sys.path.insert(0,str(B/'work/quartic224-validation-integration-001'))
import verify as v
p=json.loads(P.read_bytes());c=json.loads((D/'candidate223-ir.json').read_bytes());q=json.loads((D/'candidate223-polynomial.json').read_bytes());m=json.loads((D/'MAPS.json').read_bytes())
assert sha(P)=='0839eb623c76ba462eec8842dc5b8c85fef85cc924c9daa98f35a83ae61948e0'
assert c['coordinates']==p['coordinates'] and c['fixedParameter']==p['fixedParameter']
rows=[v.terms(r['terms'])for r in p['residuals']];original=list(rows)
def maps(stage,key):
 out={i:v.variable(i)for i in range(1,224)}
 for k,ts in stage[key].items():
  assert 1<=int(k)<=223;out[int(k)]=v.terms(ts)
 assert out[1]==v.variable(1)
 assert all(a==0 and len(mon)<=1 and all(1<=i<=223 for i in mon)for x in out.values()for a,mon in x)
 return out
for stage in m['stages']:
 kind=stage['kind']
 if kind=='coordinates':
  f=maps(stage,'old_in_new');g=maps(stage,'new_in_old')
  for i in range(1,224):assert v.subst(f[i],g)==v.variable(i)and v.subst(g[i],f)==v.variable(i)
  rows=[v.subst(r,f)for r in rows]
 elif kind=='row_add':
  i,j=stage['target'],stage['source'];assert 0<=i<197 and 0<=j<197 and i!=j
  rows[i]=v.add(rows[i],v.scale(rows[j],F(stage['factor'])))
 elif kind=='row_sum_difference':
  i,j=stage['first'],stage['second'];assert 0<=i<197 and 0<=j<197 and i!=j
  a,b=rows[i],rows[j];rows[i]=v.add(a,b);rows[j]=v.add(a,v.scale(b,-1))
 else:raise AssertionError(kind)
assert len(m['normalization_factors'])==197
for i,f in enumerate(m['normalization_factors']):
 assert F(f)!=0;rows[i]=v.scale(rows[i],F(f));assert rows[i]==v.terms(c['residuals'][i]['terms'])
rev=[v.scale(r,1/F(f))for r,f in zip(rows,m['normalization_factors'])]
for stage in reversed(m['stages']):
 if stage['kind']=='coordinates':rev=[v.subst(r,maps(stage,'new_in_old'))for r in rev]
 elif stage['kind']=='row_add':
  i,j=stage['target'],stage['source'];rev[i]=v.add(rev[i],v.scale(rev[j],-F(stage['factor'])))
 else:
  i,j=stage['first'],stage['second'];a,b=rev[i],rev[j];rev[i]=v.scale(v.add(a,b),F(1,2));rev[j]=v.scale(v.add(a,v.scale(b,-1)),F(1,2))
assert rev==original
result=v.check(p,c,q);poly=v.terms(q['terms']);aa=[(mon,z)for(a,mon),z in poly.items()if a==2];assert len(aa)==1 and aa[0][1]==1 and poly[0,aa[0][0]]==1
M0=max(abs(z)for(a,mon),z in poly.items()if a==0);M1=max(abs(z)for(a,mon),z in poly.items()if a==1);assert M1*149**107+M0<149**214
assert all(z.denominator==1 for z in poly.values())and math.gcd(*(int(z)for z in poly.values()))==1
result.update(forward_all_rows=True,reverse_all_rows=True,affine_stages=sum(t['kind']=='coordinates'for t in m['stages']),input_fixed_each_stage=True,height='A_N²+1 for coefficientN>=53; ineffective defining threshold retained')
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print({k:z for k,z in result.items()if k!='consumers'})
