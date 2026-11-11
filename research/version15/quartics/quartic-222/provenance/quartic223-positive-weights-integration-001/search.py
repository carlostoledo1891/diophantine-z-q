import json,sys,hashlib,math,time
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'quartic224-validation-integration-001'))
from verify import terms,mul,add,scale
B=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
P=B/'work/quartic238-optimization-20261110/resume-20261110/joint-root-sparse-111/candidate223-ir.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='eef4351cd9cd714ee93b6851fcfbfe62c5351be4b1d7000f5b90afd56d26da7c'
ir=json.loads(P.read_bytes());squares=[mul(terms(r['terms']),terms(r['terms']))for r in ir['residuals']]
poly=add(*squares);weights=[F(1)]*len(squares);history=[];started=time.monotonic();tried=0
# Every one-weight change reducing support must cancel at least one existing coefficient.
for iteration in range(32):
 groups={}
 for (a,m),v in poly.items():groups.setdefault(m,{})[a]=v
 count=len(groups);best=None
 for i,sq in enumerate(squares):
  sg={}
  for (a,m),v in sq.items():sg.setdefault(m,{})[a]=v
  candidates={-poly.get(k,F(0))/v for k,v in sq.items()}
  for delta in candidates:
   if not delta or weights[i]+delta not in {F(1,4),F(1,2),F(1),F(2),F(3),F(4),F(8)}:continue
   tried+=1;gain=0
   for m,aps in sg.items():
    old=groups.get(m,{})
    remains=any(old.get(a,F(0))+delta*aps.get(a,F(0)) for a in set(old)|set(aps))
    gain+=bool(old)-remains
   if gain>0 and (best is None or gain>best[0]):best=(gain,i,delta)
 if best is None:break
 gain,i,delta=best;weights[i]+=delta;poly=add(poly,scale(squares[i],delta));history.append({'iteration':iteration,'row_index':i,'row_id':ir['residuals'][i]['id'],'row_name':ir['residuals'][i]['name'],'weight':str(weights[i]),'monomials_before':count,'monomials_after':len({m for a,m in poly})})
# Global positive integer normalization preserves the zero locus.
lcm=math.lcm(*(v.denominator for v in poly.values()));content=math.gcd(*(int(v*lcm) for v in poly.values()));factor=F(lcm,content)
poly=scale(poly,factor);weights=[w*factor for w in weights]
assert poly==add(*(scale(s,w)for s,w in zip(squares,weights))) and all(w>0 for w in weights)
result={'status':'author candidate; independent review required','parent_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'variables':ir['variables'],'residuals':len(squares),'coordinate_monomials':len({m for a,m in poly}),'formal_terms':len(poly),'iterations':history,'candidate_weights_tested':tried,'seconds':time.monotonic()-started,'limits':'Exact single-positive-row-weight support search, weights in {1/4,1/2,1,2,3,4,8}; at most32 accepted steps. No joint-weight or global optimality claim. Defining threshold remains ineffective; coefficient-height formula must be rechecked.'}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(O/'WEIGHTS.json').write_text(json.dumps([str(w)for w in weights],indent=2)+'\n')
out={'variables':ir['variables'],'inputCoordinate':ir['inputCoordinate'],'fixedParameter':ir['fixedParameter'],'degree':4,'positiveRowWeights':[str(w)for w in weights],'terms':[{'parameterPower':a,'monomial':list(m),'coefficient':str(v)}for(a,m),v in sorted(poly.items())]}
(O/'polynomial.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(result))
