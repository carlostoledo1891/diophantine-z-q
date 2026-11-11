"""Replace the scalar preparation parametrization by an equivalent guarded conic."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib,copy,math,functools
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parents[2]/'work/quartic-optimization-20261107/02-squares'))
from search import read,encode,add,mul,degree,vs
S=H/'candidate494-ir.json';d=json.loads(S.read_text());cn={c['name']:c['id'] for c in d['coordinates']};rn={r['name']:r['id'] for r in d['residuals']};rows={r['id']:read(r['terms']) for r in d['residuals']}
b,t,t2,T,V,u2=[cn[n] for n in ['scalar.b.quadratic','scalar.preparation','scalar.t2.quadratic','scalar.preparationT','scalar.UplusB','scalar.U2.quadratic']]
a,c,e,g=[rn[n] for n in ['scalar.t2.definition','scalar.preparationT.definition','scalar.UplusB.definition','scalar.U2.definition']]
K=rows[g][(0,tuple(sorted((b,V))))]/2;assert K>0
rows[a]={(0,(t,t)):Q(1),(0,(u2,)):-K*K}
rows[c]={(0,()):Q(1),(0,tuple(sorted((b,t2)))):K}
rows[e]={(0,tuple(sorted((t2,u2)))):K*K,(0,(T,T)):Q(1),(0,(b,)):K}
del rows[g]
coords=[]
for x in d['coordinates']:
 if x['id']==V:continue
 x=copy.deepcopy(x)
 if x['id']==t:x['name']='scalar.conic.U'
 if x['id']==t2:x['name']='scalar.conic.inverseB'
 if x['id']==T:x['name']='scalar.conic.V'
 coords.append(x)
out=dict(d,coordinates=coords,residuals=[dict(r,terms=encode(rows[r['id']])) for r in d['residuals'] if r['id'] in rows],status='Future candidate: scalar preparation represented by guarded conic.')
(H/'candidate493-ir.json').write_text(json.dumps(out,indent=2)+'\n')
pol={}
for p in rows.values():
 den=functools.reduce(math.lcm,(v.denominator for v in p.values()),1);gg=functools.reduce(math.gcd,(abs(v.numerator*(den//v.denominator)) for v in p.values()),0);p={m:v*Q(den,gg) for m,v in p.items()};pol=add(pol,mul(p,p))
(H/'polynomial493.json').write_text(json.dumps({'fixedParameter':out['fixedParameter'],'terms':encode(pol)},indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cert={'source':str(S),'sourceSha256':sha(S),'candidateSha256':sha(H/'candidate493-ir.json'),'polynomialSha256':sha(H/'polynomial493.json'),'ids':{'b':b,'t':t,'t2':t2,'T':T,'V':V,'u2':u2},'rows':{'square':a,'inverse':c,'Vplus':e,'U2':g},'K':str(K),'counts':{'variables':len(coords),'witnesses':len(coords)-1,'residuals':len(rows),'degree':degree(pol),'monomials':len({m for s,m in pol})}}
(H/'certificate493.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps(cert['counts'],indent=2))
