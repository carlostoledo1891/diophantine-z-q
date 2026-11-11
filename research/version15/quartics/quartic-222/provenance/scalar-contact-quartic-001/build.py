import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
O=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[4]
P=ROOT/'work/quartic238-optimization-20261110/linear-lucas/reference233-014/candidate233-ir.json'
b=P.read_bytes();assert hashlib.sha256(b).hexdigest()=='26d9a2aef8b92fb7fa7d42a24c185ac71d889c0952a0e0bf4b44d09ea9e67691'
x=json.loads(b)
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 return c
# s=beta-3 and u=s^2/4.  Four contact factors in s.
c=[1]
for f in [[3,1],[2,1],[-2398,1],[439,32]]:c=pmul(c,f)
a0,a1,a2,a3,a4=c
terms={():-(a0+2501*a1),(63,):-51*a1,(121,):-(4*a2+4*2501*a3),(63,121):-4*51*a3,(121,121):-16*a4,(123,):1}
# Residual is contactProduct minus r4, same sign immaterial.
def compact(i):
 assert i!=122
 return i-(i>122)
new=[]
for r in x['residuals']:
 if r['id']==71:continue
 if r['id']==72:r={'name':'scalar.four_contact_product.definition','terms':[{'parameterPower':0,'monomial':list(m),'coefficient':str(v)} for m,v in sorted(terms.items()) if v]}
 else:r=json.loads(json.dumps(r))
 for t in r['terms']:t['monomial']=[compact(i) for i in t['monomial']]
 r['id']=len(new)+1;new.append(r)
x['residuals']=new;x['variables']=232;x['coordinates']=[dict(q,id=compact(q['id'])) for q in x['coordinates'] if q['id']!=122]
x['source']={'parent_sha256':hashlib.sha256(b).hexdigest(),'change':'Four-factor scalar contact; arithmetic equivalence of integer projection requires separate proof, not a coordinate equivalence of all old/new witnesses.'}
poly={}
for r in new:
 for a in r['terms']:
  for b in r['terms']:
   k=(a['parameterPower']+b['parameterPower'],tuple(sorted(a['monomial']+b['monomial'])))
   poly[k]=poly.get(k,0)+int(a['coefficient'])*int(b['coefficient'])
poly={k:v for k,v in poly.items() if v}
assert max(len(m) for a,m in poly)==4
stats={'variables':232,'residuals':len(new),'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':4,'content':math.gcd(*poly.values()),'all_coordinates_present':set(i for a,m in poly for i in m)==set(range(1,233))}
for name,obj in [('candidate232-ir.json',x),('candidate232-polynomial.json',{'variables':232,'degree':4,'terms':[{'parameterPower':a,'monomial':list(m),'coefficient':str(v)} for (a,m),v in sorted(poly.items())]}),('MAP.json',{'deleted_old_coordinate':122,'deleted_old_row':71,'replaced_old_row':72,'old_to_new':{str(i):compact(i) for i in range(1,234) if i!=122},'s_polynomial_coefficients':c,'new_contact_row_before_compaction':[{'monomial':list(m),'coefficient':str(v)} for m,v in sorted(terms.items())],'warning':'This is an arithmetic redesign, not identical witness sets under compaction.'}),('STATISTICS.json',stats)]:
 (O/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
