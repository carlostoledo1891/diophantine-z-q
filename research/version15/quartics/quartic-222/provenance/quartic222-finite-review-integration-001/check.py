import json,hashlib,sys,math
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
A=B/'work/quartic238-optimization-20261110/resume-20261110/trace-quotient222-116'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(A/'MANIFEST.json')=='6bec2e3182a34bf009f6582c43593faeea8960d541674d7dade109dca7463211'
manifest=json.loads((A/'MANIFEST.json').read_bytes())
for member in manifest['members']:
 p=A/member['path'];assert sha(p)==member['sha256'] and p.stat().st_size==member['bytes']
sys.path.insert(0,str(B/'work/quartic224-validation-integration-001'))
import verify as V
maps=json.loads((A/'MAPS.json').read_bytes());stats=json.loads((A/'STATISTICS.json').read_bytes())
results={}
for kind in ['raw','sparse']:
 pin=next(x for x in maps['parent_pins']if x['kind']==kind);p=B/Path(pin['path']);assert sha(p)==pin['sha256']
 assert sha(p.parent/'MANIFEST.json')==manifest['parent_'+kind+'_manifest']
 pm=json.loads((p.parent/'MANIFEST.json').read_bytes())
 for member in pm['members']:
  member_path=p.parent/member['path'];assert sha(member_path)==member['sha256'] and ('bytes' not in member or member_path.stat().st_size==member['bytes'])
 old=json.loads(p.read_bytes());new=json.loads((A/(kind+'222-ir.json')).read_bytes());poly=json.loads((A/(kind+'222-polynomial.json')).read_bytes())
 oldpoly=json.loads((p.parent/('candidate223-polynomial.json' if kind=='raw' else 'polynomial.json')).read_bytes())
 result=V.check(old,new,poly)
 assert old['variables']==223 and new['variables']==222 and len(old['residuals'])==197 and len(new['residuals'])==196
 assert new['coordinates'][:221]==old['coordinates'][:221]
 assert new['coordinates'][221]['id']==222 and new['coordinates'][221]['kind']==old['coordinates'][222]['kind']
 op={r['id']:V.terms(r['terms'])for r in old['residuals']};nr={r['parent223RowId']:r for r in new['residuals']}
 assert set(nr)==set(op)-{186} and [r['id']for r in new['residuals']]==list(range(1,197))
 census=[i for i,p in op.items()if any(222 in m or 223 in m for a,m in p)]
 assert census==[186,196,197]
 assert census==[x['id']for x in maps['census'][kind]]
 inv={i:V.variable(i)for i in range(1,222)}
 inv[222]=V.mul(V.variable(119),V.variable(222));inv[223]=V.mul(V.variable(98),V.variable(222))
 assert V.subst(op[186],inv)=={}
 for i,r in nr.items():
  actual=V.terms(r['terms']);assert V.subst(op[i],inv)==actual
  assert r['name']==old['residuals'][i-1]['name']
  if i not in [196,197]:assert actual==op[i]
 # Q times the forward-substituted residual, without dividing by a trace weight.
 def cleared(p):
  out={}
  for(a,m),v in p.items():
   k=m.count(222);assert k<=1
   mm=tuple(sorted(tuple(223 if x==222 else x for x in m)+(98,)*(1-k)))
   out=V.add(out,{(a,mm):v})
  return out
 assert cleared(V.terms(nr[196]['terms']))==V.add(V.mul(V.variable(98),op[196]),V.scale(op[186],-1))
 assert cleared(V.terms(nr[197]['terms']))==V.mul(V.variable(98),op[197])
 # All other rows are literally unchanged: the accepted q!=0 proof inputs remain exact.
 assert all(op[i]==V.terms(nr[i]['terms'])for i in op if i not in census)
 ow=list(map(F,oldpoly.get('positiveRowWeights',['1']*197)));nw=list(map(F,poly.get('positiveRowWeights',['1']*196)))
 assert nw==[w for i,w in enumerate(ow,1)if i!=186] and all(w>0 for w in nw)
 pp=V.terms(poly['terms']);assert all(v.denominator==1 for v in pp.values())
 assert math.gcd(*(int(v)for v in pp.values()))==1
 a2=[(m,v)for(a,m),v in pp.items()if a==2];assert len(a2)==1 and a2[0][1]==1 and pp[0,a2[0][0]]==1
 assert all(a<=2 for a,m in pp)
 m0=max(abs(v)for(a,m),v in pp.items()if a==0);m1=max(abs(v)for(a,m),v in pp.items()if a==1)
 assert m1*149**107+m0<149**214
 assert result['coordinate_monomials']==stats[kind]['coordinate_monomials'] and result['formal_terms']==stats[kind]['parameter_terms']
 # Algebraic zero-case map checks, not claimed full-system witnesses.
 zero_cases=0
 for q in [F(1),F(4),F(9)]:
  for r2 in [F(0),F(1),F(4)]:
   for t in [F(0),F(1),F(-1),F(2,3)]:
    g=r2*t;z=q*t;assert q*g-r2*z==0 and z/q==t
    if t==0:assert g==z==0
    zero_cases+=1
 results[kind]={k:v for k,v in result.items()if k!='consumers'}
 results[kind].update(candidate_ir_sha256=sha(A/(kind+'222-ir.json')),parent_ir_sha256=sha(p),all_parent_rows_substituted=197,unchanged_rows=194,consumer_census=census,forward_cleared_identities=True,positive_weights_preserved=True,zero_map_cases=zero_cases,content=1,height='A_N^2+1 for N>=53; defining threshold unchanged')
(O/'RESULT.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
