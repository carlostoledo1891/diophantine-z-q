import json,math,hashlib
from pathlib import Path
from fractions import Fraction as F
O=Path('work/quartic238-optimization-20261110/resume-20261110/trace-quotient222-116');O.mkdir(exist_ok=True)
BASE=O.parent
G,Z,Q,R2=222,223,98,119

def read(ts):return {(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def add(p,k,c):
 p[k]=p.get(k,F(0))+c
 if not p[k]:del p[k]
def mul(p,q):
 r={}
 for (a,m),c in p.items():
  for (b,n),d in q.items():add(r,(a+b,tuple(sorted(m+n))),c*d)
 return r
def ser(p):return [dict(parameterPower=a,monomial=list(m),coefficient=str(c)) for (a,m),c in sorted(p.items())]
def sub(p):
 r={}
 for (a,m),c in p.items():
  n=[]
  for i in m:n.extend([R2,Z] if i==G else [Q,Z] if i==Z else [i])
  add(r,(a,tuple(sorted(n))),c)
 return r
allstats={};pins=[];censuses={}
for kind,src in [('raw',BASE/'joint-root-factor-110/candidate223-ir.json'),('sparse',BASE/'joint-root-rowpairs-112/candidate223-ir.json')]:
 b=src.read_bytes();s=json.loads(b);pins.append(dict(kind=kind,path=str(src),sha256=hashlib.sha256(b).hexdigest()))
 out=[];removed=[];poly={};changed=[];census=[]
 for row in s['residuals']:
  p=read(row['terms']);t=sub(p)
  if any(G in m or Z in m for a,m in p):census.append(dict(id=row['id'],name=row['name']))
  if not t:removed.append(row['id']);continue
  assert max(map(lambda k:len(k[1]),t))<=2,(kind,row['id'])
  if t!=p:changed.append(row['id'])
  t={(a,tuple(222 if i==223 else i for i in m)):c for (a,m),c in t.items()}
  rr=dict(row,id=len(out)+1,parent223RowId=row['id'],terms=ser(t));out.append(rr)
  w=F(row.get('positive_square_weight',1));assert w>0
  for k,c in mul(t,t).items():add(poly,k,w*c)
 assert len(out)==196 and len(removed)==1 and len(changed)==2 and len(census)==3
 assert set(i for a,m in poly for i in m)==set(range(1,223))
 assert all(c.denominator==1 for c in poly.values())
 coords=[dict(c,id=222 if c['id']==223 else c['id']) for c in s['coordinates'] if c['id']!=222]
 coords[-1]['name']='trace.quotient.Z_over_q1_squared'
 s.update(variables=222,coordinates=coords,residuals=out,source=dict(parent_sha256=hashlib.sha256(b).hexdigest(),change='G=R2*T, Z=Q1*T; remove tautological trace row'))
 a2=[(m,c) for (a,m),c in poly.items() if a==2];assert a2==[((108,108),F(1))]
 assert poly[0,(108,108)]==1
 assert max(abs(c) for (a,m),c in poly.items() if a==0)<149**214
 assert max(abs(c) for (a,m),c in poly.items() if a==1)==44402
 stats=dict(variables=222,residuals=196,coordinate_monomials=len({m for a,m in poly}),parameter_terms=len(poly),degree=max(len(m) for a,m in poly),content=math.gcd(*(int(c) for c in poly.values())),height='A_N^2+1 for N>=53; defining threshold remains ineffective',changed_parent_rows=changed,deleted_parent_rows=removed)
 for name,obj in [(kind+'222-ir.json',s),(kind+'222-polynomial.json',dict(variables=222,inputCoordinate=s['inputCoordinate'],fixedParameter=s['fixedParameter'],positiveRowWeights=[str(r.get('positive_square_weight',1)) for r in out],terms=ser(poly)))]: (O/name).write_text(json.dumps(obj,indent=2)+'\n')
 allstats[kind]=stats;censuses[kind]=census
(O/'STATISTICS.json').write_text(json.dumps(allstats,indent=2)+'\n')
(O/'MAPS.json').write_text(json.dumps(dict(parent_pins=pins,census=censuses,old_G=222,old_Z=223,new_T=222,Q1=98,R_squared=119,forward='T=oldZ/Q1; discardoldG; coordinates1..221fixed',inverse='oldG=R_squared*T; oldZ=Q1*T; coordinates1..221fixed',required_domain='Q1=q1^2!=0 from unchanged accepted ten-row contact proof107'),indent=2)+'\n')
print(json.dumps(allstats))

