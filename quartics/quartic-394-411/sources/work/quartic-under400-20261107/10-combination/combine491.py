"""Combine the order10 circuit with four factored poles; preserve all source IDs."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 return {m:v*F(d,g) for m,v in p.items()}
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
d=read('order10-495-ir.json');b=read('inputs/released498.json');patch=read('inputs/factored-candidate494-ir.json')
br={r['name']:r for r in b['residuals']};pr={r['name']:r for r in patch['residuals']};dr={r['name']:r for r in d['residuals']}
deleted=set(br)-set(pr);changed={n for n in set(br)&set(pr) if p(br[n]['terms'])!=p(pr[n]['terms'])}
assert not set(pr)-set(br) and len(deleted)==4 and len(changed)==8
for name in deleted|changed:assert p(dr[name]['terms'])==p(br[name]['terms'])
for name in changed:dr[name]['terms']=pr[name]['terms']
pc={c['id']:c for c in patch['coordinates']};removed={c['id'] for c in b['coordinates']}-set(pc)
bc={c['id']:c for c in b['coordinates']};renamed={i for i in pc if pc[i]['name']!=bc[i]['name']}
d['coordinates']=[dict(c,name=pc[c['id']]['name']) if c['id'] in renamed else c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[r for r in d['residuals'] if r['name'] not in deleted]
d['status']='Under400 research candidate: reviewed order10 and four positive-completeness pole factorizations.'
total={}
for r in d['residuals']:
 pp=norm(p(r['terms']))
 for (s,m),a in pp.items():
  for (t,n),bb in pp.items():
   k=s+t,tuple(sorted(m+n));total[k]=total.get(k,0)+a*bb
total={k:v for k,v in total.items() if v}
assert len(d['coordinates'])==491 and len(d['residuals'])==460
assert max(len(m) for s,m in total)==4
assert {v for s,m in total for v in m}=={c['id'] for c in d['coordinates']}
write('combined491-ir.json',d);write('combined491-polynomial.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':491,'witnesses':490,'residuals':460,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)','candidateSha256':sha('combined491-ir.json'),'polynomialSha256':sha('combined491-polynomial.json')}
write('combined491-certificate.json',{'source495Sha256':sha('order10-495-ir.json'),'factor494Sha256':sha('inputs/factored-candidate494-ir.json'),'deletedRows':sorted(deleted),'changedRows':sorted(changed),'removedCoordinates':sorted(removed),'renamedCoordinates':sorted(renamed),'statistics':stats});print(json.dumps(stats,indent=2))
