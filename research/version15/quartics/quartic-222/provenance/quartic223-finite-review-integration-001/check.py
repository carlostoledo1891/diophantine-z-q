import json,hashlib,sys,math
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
B=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
A=B/'work/quartic238-optimization-20261110/resume-20261110/joint-root-factor-110'
P=B/'work/quartic238-optimization-20261110/global/resume-20261110/shared-T-redundancy224-006/candidate224-ir.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(A/'MANIFEST.json')=='f673e732217d82bca9c6d10a4a6114155b7af75c3be92790daabc7b876eeab4f'
manifest=json.loads((A/'MANIFEST.json').read_bytes())
for x in manifest['members']:assert sha(A/x['path'])==x['sha256'] and (A/x['path']).stat().st_size==x['bytes']
assert sha(P)=='6b961988414509ff6619fb674b696c745b098d00ad2af326df43e4db5aa5d39f'
old=json.loads(P.read_bytes());new=json.loads((A/'candidate223-ir.json').read_bytes());maps=json.loads((A/'MAPS.json').read_bytes());poly=json.loads((A/'candidate223-polynomial.json').read_bytes())
sys.path.insert(0,str(B/'work/quartic224-validation-integration-001'))
import verify as V
sos=V.check(old,new,poly)
cm={int(k):v for k,v in maps['old_to_new'].items()};rev={v:k for k,v in cm.items()}
assert set(rev)==set(range(1,224)) and cm[1]==1
removed={62,63,66,67,68,69};assert set(maps['deleted'])==removed
assert set(cm)==(set(range(1,225))-removed)|set(range(225,230))
for c in old['coordinates']:
 if c['id'] not in removed:
  actual=new['coordinates'][cm[c['id']]-1]
  assert actual==dict(c,id=cm[c['id']])
# Laurent ring Q[A,q,q^-1,R,R^-1,other current coordinates], using old labels.
def plus(*ps):
 d=defaultdict(F)
 for p in ps:
  for k,v in p.items():d[k]+=v
 return {k:v for k,v in d.items()if v}
def times(p,q):
 d=defaultdict(F)
 for(a,b,c,m),v in p.items():
  for(e,f,g,n),w in q.items():d[a+e,b+f,c+g,tuple(sorted(m+n))]+=v*w
 return {k:v for k,v in d.items()if v}
def scale(p,z):return {k:v*z for k,v in p.items()if v*z}
def unit(a=0,b=0,c=0,m=(),v=1):return {(a,b,c,m):F(v)}
def atom(i):
 if i==102:return unit(b=1)
 if i==104:return unit(b=2)
 if i==126:return unit(c=1)
 if i==125:return unit(c=2)
 return unit(m=(i,))
def square(p):return times(p,p)
first=set(range(167,179))|set(range(195,203))|set(range(209,217))
scaled=first|set(range(203,207))|set(range(217,221))|{179,180,207,208,221,222}
ratio=set(range(47,55))|set(range(56,60))
assert first==set(maps['first_R_scaled']) and scaled==set(maps['scaled']) and ratio==set(maps['ratio_R_scaled'])
fu={62:(179,180,0),63:(179,180,1),66:(207,208,0),67:(207,208,1),68:(221,222,0),69:(221,222,1)}
def parent_var(i):
 if i in fu:
  u,v,im=fu[i];p=times(atom(u),atom(v))if im else plus(square(atom(u)),scale(square(atom(v)),2))
  return times(unit(b=-2),p)
 if i in scaled:return times(atom(i),unit(b=-1,c=int(i in first)))
 if i in ratio:return times(atom(i),unit(c=1))
 return atom(i)
def loadrow(row,parent=False):
 out={}
 for t in row['terms']:
  z=unit(a=t['parameterPower'],v=F(t['coefficient']))
  for i in t['monomial']:z=times(z,parent_var(i)if parent else atom(rev[i]))
  out=plus(out,z)
 return out
# Independent helper definitions from stated maps.
helpers={225:plus(times(atom(104),atom(88)),scale(times(atom(89),atom(103)),-1)),226:plus(times(atom(104),atom(90)),scale(times(atom(89),atom(105)),-1)),227:plus(times(atom(104),atom(87)),scale(times(atom(89),atom(102)),-1))}
qform=lambda a,b,c,d:plus(square(plus(atom(a),scale(atom(b),-1))),scale(square(plus(atom(c),scale(atom(d),-1))),2))
helpers[228]=plus(scale(times(atom(4),atom(98)),8),scale(qform(185,187,186,188),-1))
helpers[229]=plus(qform(171,173,172,174),qform(199,201,200,202),qform(213,215,214,216))
def expand(p):
 out={}
 for(a,b,c,m),v in p.items():
  z=unit(a,b,c,v=v)
  for i in m:z=times(z,helpers.get(i,atom(i)))
  out=plus(out,z)
 return out
def proportional(p,q):
 assert p and q
 # Laurent-unit proportionality is enough for zero-locus equivalence on qR!=0.
 bp=min(k[1]for k in p);cp=min(k[2]for k in p);bq=min(k[1]for k in q);cq=min(k[2]for k in q)
 pn={(a,b-bp,c-cp,m):v for(a,b,c,m),v in p.items()};qn={(a,b-bq,c-cq,m):v for(a,b,c,m),v in q.items()}
 assert set(pn)==set(qn)
 k=next(iter(pn));s=pn[k]/qn[k];assert pn==scale(qn,s)
 return {'q_power':bp-bq,'R_power':cp-cq,'constant':str(s)}
byname={r['name']:r for r in old['residuals']};byparent={r['parentRowId']:r for r in new['residuals']if 'parentRowId'in r}
assert len(byparent)==192 and len(new['residuals'])==197
pair={}
for fi in [1,2,4]:
 for part in [0,1]:
  r0=byname[f'residue.det0.factor{fi}.{part}.definition'];r1=byname[f'residue.det1.factor{fi}.{part}.definition']
  def outputcoef(r,idx):return next(F(t['coefficient'])for t in r['terms']if t['parameterPower']==0 and t['monomial']==[idx])
  p0=scale(loadrow(r0,True),1/outputcoef(r0,135+2*fi+part));p1=scale(loadrow(r1,True),1/outputcoef(r1,151+2*fi+part))
  pair[r0['id']]=plus(times(atom(104),p0),scale(times(atom(89),p1),-1))
checks=[];deleted_rows=[]
for row in old['residuals']:
 p=loadrow(row,True)
 if row['id']not in byparent:
  assert not p;deleted_rows.append(row['id']);continue
 actual=expand(loadrow(byparent[row['id']]))
 expected=pair.get(row['id'],p)
 if 'aggregate.rootTrace'in row['name']:expected=times(atom(104),p)
 if not actual and not expected:factor={'alias_identity':True}
 else:factor=proportional(actual,expected)
 checks.append(dict(row=row['id'],**factor))
assert set(deleted_rows)==set(maps['removed_rows']) and len(deleted_rows)==6
for i,row in zip(range(225,230),new['residuals'][-5:]):
 assert expand(loadrow(row))=={}
 proportional(loadrow(row),plus(atom(i),scale(helpers[i],-1)))
# Explicit domain/alias equations remain unchanged under index renumbering, up to nonzero constants.
required=[9,43,44,45,46,47,56,57,68,71,73]
for i in required:
 r=next(r for r in old['residuals']if r['id']==i)
 expected={}
 for t in r['terms']:
  z=unit(a=t['parameterPower'],v=F(t['coefficient']))
  for k in t['monomial']:z=times(z,unit(m=(k,)))
  expected=plus(expected,z)
 actual={}
 for t in byparent[i]['terms']:
  actual=plus(actual,unit(a=t['parameterPower'],m=tuple(sorted(rev[k]for k in t['monomial'])),v=F(t['coefficient'])))
 assert proportional(actual,expected)['q_power']==0
# Strong coefficient bound including mixed A terms.
p=V.terms(poly['terms']);a2=[(m,v)for(a,m),v in p.items()if a==2];assert len(a2)==1 and a2[0][1]==1 and p[0,a2[0][0]]==1
M0=max(abs(v)for(a,m),v in p.items()if a==0);M1=max(abs(v)for(a,m),v in p.items()if a==1);assert M1*149**107+M0<149**214
assert all(v.denominator==1 for v in p.values())and math.gcd(*(int(v)for v in p.values()))==1
result=dict(sos,all_parent_rows_checked=198,deleted_identity_rows=deleted_rows,paired_rows_checked=6,helper_definitions_checked=5,required_alias_domain_rows=required,coordinate_map_checked=True,full_height_bound='A_N²+1 for N>=53; ineffective defining threshold unchanged',row_relations=checks,source_ir_sha256=sha(P),candidate_ir_sha256=sha(A/'candidate223-ir.json'))
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k not in ['consumers','row_relations']})
