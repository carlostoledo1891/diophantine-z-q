import json,hashlib
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent;P=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-redundancy224-006/candidate224-ir.json');j=json.loads(P.read_bytes());rows={r['id']:r for r in j['residuals']}
# Divide row45 by its x101 coefficient and by T^2; x99/T=r,x100/T=r²,x128/T=r³.
L=next(int(t['coefficient']) for t in rows[45]['terms'] if t['monomial']==[101])
powers={99:1,100:2,128:3,125:0};poly={}
for t in rows[45]['terms']:
 if t['monomial']==[101]:continue
 e=sum(powers[v] for v in t['monomial']);poly[e]=poly.get(e,F(0))-F(int(t['coefficient']),L)
assert poly[5]==1
mod=lambda q:(q.numerator*pow(q.denominator,-1,5))%5
mods={e:mod(v) for e,v in poly.items()};assert mods=={0:1,1:1,2:3,3:3,4:1,5:1}
# product (r-1)^2(r-4)^3 over F5
prod=[1]
for root in [1,1,4,4,4]:
 new=[0]*(len(prod)+1)
 for i,a in enumerate(prod):new[i]=(new[i]-root*a)%5;new[i+1]=(new[i+1]+a)%5
 prod=new
assert prod==[mods[i] for i in range(6)]
residues=[]
for t in range(5):
 r=(t-1)**2%5;v=sum(mods[e]*pow(r,e,5) for e in mods)%5;rhs=pow(r,5,5)
 assert v!=rhs;residues.append({'t_mod5':t,'r_mod5':r,'P_mod5':v,'r5_mod5':rhs})
# R nonzero uses only inputSquare and scalar56/57/71. The exact positive polynomial was independently expanded in104.
pj=json.loads(Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/scalar-normalizer-degree-104/CHECKS.json').read_bytes());coeffs={int(k):F(v) for k,v in pj['contact_coefficients_degree_to_value'].items()};assert all(v>0 for v in coeffs.values())
assert all(t['parameterPower']==0 for rid in [43,44,45,46,73] for t in rows[rid]['terms'])
result={'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'required_rows':[9,43,44,45,46,56,57,68,71,73],'q_coordinate':102,'q_name':next(x['name'] for x in j['coordinates'] if x['id']==102),'T_coordinate':125,'R_coordinate':126,'contact_polynomial':{str(e):str(poly[e]) for e in sorted(poly)},'mod5_coefficients':mods,'integral_residue_checks':residues,'negative_valuation_leading_coefficient':str(poly[4]),'negative_valuation_leading_coefficient_mod5':mods[4],'scalar_contact_positive_coefficients':pj['contact_coefficients_degree_to_value'],'q_minus1_branch':{'t':'1','r':'0','q':'-1','P0':str(poly[0]),'equation_holds':True},'scope':'q!=0 on every rational tuple satisfying the listed unchanged rows with nonzero A; no trace/root/ratio/comparison or inverseguard equation used.'}
(O/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');(O/'REQUIRED-ROWS.json').write_text(json.dumps([rows[r] for r in result['required_rows']],indent=2)+'\n');print(json.dumps(result))
