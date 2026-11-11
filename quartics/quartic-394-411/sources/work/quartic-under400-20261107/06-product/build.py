"""Exact scalar norm denominator consolidation, from frozen 498 to 496."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
HERE=Path(__file__).resolve().parent
REPO=HERE.parent.parent/'quartic-version6-release/repository'
SOURCE=REPO/'quartics/quartic-498-514/candidate498-ir.json'
def poly(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
 d={}
 for (s,m),a in p.items():
  for (t,n),b in q.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,F(0))+a*b
 return {k:v for k,v in d.items() if v}
def var(i):return {(0,(i,)):F(1)}
def norm(p):
 l=math.lcm(*(v.denominator for v in p.values()));g=math.gcd(*(int(v*l) for v in p.values()))
 return scale(p,F(l,abs(g)))
def main():
 d=json.loads(SOURCE.read_text());by={r['id']:r for r in d['residuals']}
 inverse=poly(by[456]['terms']);assert inverse[(0,())]==1
 r={}
 for (s,m),v in inverse.items():
  if not m:continue
  assert m.count(490)==1;r[s,tuple(x for x in m if x!=490)]=-v
 removed_coords=set(range(490,496))|{537,538};removed_rows=set(range(456,462))|{507,508}
 d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed_coords]
 for c in d['coordinates']:
  if c['id']==539:c['name']='scalar.ratio1_unscaled_square'
 d['residuals']=[row for row in d['residuals'] if row['id'] not in removed_rows]
 previous=r
 for j in range(6):
  i=600+j;d['coordinates'].append({'id':i,'name':f'scalar.r_power_{2**(j+1)}','kind':'base','block':'scalar_forward_powers','protected':False})
  d['residuals'].append({'id':600+j,'name':f'scalar.r_power_{2**(j+1)}.definition','terms':terms(norm(add(var(i),scale(mul(previous,previous),-1))))})
  previous=var(i)
 for row in d['residuals']:
  if row['id']==509:row['terms']=terms(add(var(539),scale(mul(var(509),var(509)),-1)));row['name']='scalar.ratio1_unscaled_square.definition'
  if row['id']==510:row['terms']=terms(norm(add(mul(var(605),var(540)),scale(mul(var(508),var(508)),-1),scale(mul(r,var(539)),-1))));row['name']='scalar.ratio_node.consolidated_denominator'
 ids={c['id'] for c in d['coordinates']};active={x for row in d['residuals'] for t in row['terms'] for x in t['monomial']}
 assert len(ids)==496 and ids==active and len(d['residuals'])==465
 assert all(len(t['monomial'])<=2 for row in d['residuals'] for t in row['terms'])
 d['status']={'name':'scalar_forward_denominator_consolidation','sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'scope':'Exact rational equivalence on existing input domain r!=0, proved from beta=2X^2+3; no new arithmetic condition.','removedCoordinates':sorted(removed_coords),'repurposedCoordinate':539}
 (HERE/'candidate496-ir.json').write_text(json.dumps(d,indent=2)+'\n')
 sos={}
 for row in d['residuals']:
  rp=norm(poly(row['terms']));sos=add(sos,mul(rp,rp))
 (HERE/'polynomial496.json').write_text(json.dumps({'schema':'formal-C-sparse-sos-v1','fixedParameter':d['fixedParameter'],'coordinates':d['coordinates'],'terms':terms(sos)},indent=2)+'\n')
 print(json.dumps({'coordinates':len(ids),'residuals':len(d['residuals']),'monomials':len({m for s,m in sos}),'degree':max(len(m) for s,m in sos)},indent=2))
if __name__=='__main__':main()

