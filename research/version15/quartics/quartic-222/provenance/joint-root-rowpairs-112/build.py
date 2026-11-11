import runpy,json,hashlib
from pathlib import Path
O=Path('work/quartic238-optimization-20261110/resume-20261110/joint-root-rowpairs-112')
x=runpy.run_path(str(O/'search_shear_bounded.py'))
s=x['ir'];p=x['poly'];weights=x['weights'];rows=x['rows']
def ser(p):return [dict(parameterPower=a,monomial=list(m),coefficient=str(c)) for (a,m),c in sorted(p.items())]
for r,t,w in zip(s['residuals'],rows,weights):r['terms']=ser(t);r['positive_square_weight']=str(w)
s['polynomial_convention']='sum positive_square_weight*residual^2'
for f,v in [('candidate223-ir.json',s),('polynomial.json',dict(variables=223,terms=ser(p),positiveRowWeights=list(map(str,weights)))),('MAPS.json',dict(operations=x['ops'],inverse='old first = (new first / normalization0 - q*new second / normalization1); second unchanged for this shear',coordinates='unchanged'))]: (O/f).write_text(json.dumps(v,indent=2)+'\n')
assert all(c.denominator==1 for c in p.values())
assert [(m,c) for (a,m),c in p.items() if a==2]==[((108,108),1)]
assert p[0,(108,108)]==1 and max(abs(c) for (a,m),c in p.items() if a==0)<149**214
members=[]
for f in ['build.py','search_shear_bounded.py','SEARCH-SHEAR.json','candidate223-ir.json','polynomial.json','MAPS.json']:
 b=(O/f).read_bytes();members.append(dict(path=f,sha256=hashlib.sha256(b).hexdigest()))
(O/'MANIFEST.json').write_text(json.dumps(dict(status='Author proposal; independent review pending',parent_weight_manifest='90f58f17d69a72d39976fae95da08a7f10bbee2c6dda056d026c4ac0f7d9fd74',statistics=dict(variables=223,residuals=197,coordinate_monomials=2280,parameter_terms=2281,height='A_N^2+1 for N>=53; defining threshold remains ineffective'),members=members),indent=2)+'\n')
print(hashlib.sha256((O/'MANIFEST.json').read_bytes()).hexdigest())
