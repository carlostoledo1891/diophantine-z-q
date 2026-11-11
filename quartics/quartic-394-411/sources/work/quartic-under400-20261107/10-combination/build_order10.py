"""Transport the reviewed order-ten source change onto released498, giving495."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items()) if c]
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 scale=F(d,g)*(1 if p[min(p)]>0 else -1)
 return {m:v*scale for m,v in p.items()}
def mapped(p,mp):return {(s,tuple(sorted(mp[i] for i in m))):v for (s,m),v in p.items()}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
d=read(H/'inputs/released498.json');old=read(H/'inputs/prior501.json');proposal=read(H/'inputs/proposal-order10.json')
assert sha(H/'inputs/released498.json')=='7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a'
assert proposal['source_sha256']==sha(H/'inputs/prior501.json')
oldrows={r['name']:r for r in old['residuals']};rows={r['name']:r for r in d['residuals']}
mp={c['id']:c['sourceId'] for c in proposal['coordinates']};pn={c['sourceId']:c['name'] for c in proposal['coordinates']}
cn={c['name']:c['id'] for c in d['coordinates']};removed=[];deleted=[]
for k in range(3):
 pre=f'detector{k}.'
 removed.append(cn[pre+'toric.t'])
 for suffix in ['a','b','u','v','q12','t','q40']:
  name=pre+'toric.'+suffix+'.definition';assert norm(p(rows[name]['terms']))==norm(p(oldrows[name]['terms']));deleted.append(name)
d['coordinates']=[dict(c,name=pn[c['id']]) if c['id'] in pn and c['name'].startswith('detector') else c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[dict(r,name=r['name'].replace('.E12.','.E10.')) for r in d['residuals'] if r['name'] not in deleted]
for r in proposal['residuals']:
 if '.toric.' in r['name']:
  i=max(rr['id'] for rr in d['residuals'])+1;d['residuals'].append(dict(r,id=i,terms=terms(mapped(p(r['terms']),mp))))
d['status']='Under400 research candidate. Order10 source change; no new publication.'
total={}
for r in d['residuals']:
 pp=norm(p(r['terms']))
 for (s,m),a in pp.items():
  for (t,n),b in pp.items():
   key=(s+t,tuple(sorted(m+n)));total[key]=total.get(key,0)+a*b
total={k:v for k,v in total.items() if v}
assert len(d['coordinates'])==495 and len(d['residuals'])==464
assert max(len(m) for s,m in total)==4
assert {i for s,m in total for i in m}=={c['id'] for c in d['coordinates']}
assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
write('order10-495-ir.json',d);write('order10-495-polynomial.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':495,'witnesses':494,'residuals':464,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'order10-495-ir.json'),'polynomialSha256':sha(H/'order10-495-polynomial.json')}
write('order10-495-certificate.json',{'released498Sha256':sha(H/'inputs/released498.json'),'prior501Sha256':sha(H/'inputs/prior501.json'),'proposalSha256':sha(H/'inputs/proposal-order10.json'),'removedCoordinates':removed,'deletedRows':deleted,'statistics':stats})
print(json.dumps(stats,indent=2))
