"""Exact composition and interface check, importing neither component producer."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
pins={
 'base':('quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json','0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56'),
 'detector':('quartic-optimization-20261107/resume-depth-20261107/three326/candidate326-ir.json','48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'),
 'anchor':('quartic-optimization-20261107/resume-elimination-20261107/abscissa359/candidate359-ir.json','282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1')}
def read(p,h):
 assert hashlib.sha256(p.read_bytes()).hexdigest()==h,p
 return json.loads(p.read_bytes())
d={name:read(WORK/p,h) for name,(p,h) in pins.items()}
# Check the only relabeling separately; no variable in any monomial is renamed.
original_anchor_rows={r['id']:r for r in d['anchor']['residuals']}
assert not {1903,1904}&set(original_anchor_rows)
d['anchor']['residuals']=[dict(r,id={903:1903,904:1904}.get(r['id'],r['id'])) for r in d['anchor']['residuals']]
assert len(d['anchor']['residuals'])==len(original_anchor_rows)
for r in d['anchor']['residuals']:
 old=original_anchor_rows[{1903:903,1904:904}.get(r['id'],r['id'])]
 assert {k:v for k,v in r.items() if k!='id'}=={k:v for k,v in old.items() if k!='id'}
new=read(H/'candidate319-ir.json','61898500a23024afbf21aed5a35ee0b573beef0dcaa598caba07de884c4281f4')
table=read(H/'polynomial319.json','2ea15f952e6e38d2aa49aa1ef849b854696dc99f8af8dcfa23d686b4ebd3af37')
delta={}
for section in ['coordinates','residuals']:
 maps={k:{x['id']:x for x in v[section]} for k,v in d.items()};actual={x['id']:x for x in new[section]}
 assert len(actual)==len(new[section])
 touched={k:{i for i in maps['base'].keys()|maps[k].keys() if maps['base'].get(i)!=maps[k].get(i)} for k in ['detector','anchor']}
 assert not touched['detector']&touched['anchor']
 for i in maps['base'].keys()|maps['detector'].keys()|maps['anchor'].keys()|actual.keys():
  supplier='detector' if i in touched['detector'] else 'anchor' if i in touched['anchor'] else 'base'
  assert actual.get(i)==maps[supplier].get(i),(section,i,supplier)
 delta[section]={k:sorted(v) for k,v in touched.items()}
for k,v in d['base'].items():
 if k not in ['coordinates','residuals','status']:assert new[k]==v
removed={c['id'] for c in d['base']['coordinates']}-{c['id'] for c in new['coordinates']}
for r in new['residuals']:assert not removed.intersection(i for t in r['terms'] for i in t['monomial'])
def dec(r):
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 assert len(p)==len(r['terms']) and all(p.values())
 return p
# These actions restore the removed A/T/Z half-chart normalizations.
actions={'A':{1,2,3,4,21,22,23,24,112,113},'T':{9,10,11,12,29,30,31,32,128,129},'Z':{13,14,15,16,33,34,35,36,136,137}}
sign_rows={}
for name,flip in actions.items():
 sign_rows[name]=[]
 for row in new['residuals']:
  parity={sum(i in flip for i in m)%2 for m in dec(row)}
  assert len(parity)==1,(name,row['id'])
  if parity=={1}:sign_rows[name].append(row['id'])
 # Outputs of all newly defined cached powers and detector products are fixed.
 assert not flip&set(range(820,846)) and not flip&set(range(903,905))
rr={r['id']:r for r in new['residuals']};aa={r['id']:r for r in d['anchor']['residuals']}
assert {i for i in delta['residuals']['anchor'] if i in rr}=={504,1903,1904}
for i in [504,1903,1904]:assert rr[i]==aa[i]
# Complete current uses of the new anchor and shared cached powers.
consumers={i:[r['id'] for r in new['residuals'] if any(i in t['monomial'] for t in r['terms'])] for i in list(range(820,846))+list(range(903,905))+[55,56,57,543,544,549]}
total=defaultdict(int);used=set()
for r in rr.values():
 p=dec(r);assert max(sum(i>=0 for i in m) for m in p)<=2
 used.update(i for m in p for i in m if i>=0)
 den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
 terms=[(m,int(c*den)//g) for m,c in p.items()]
 for i,(m,c) in enumerate(terms):
  for j in range(i,len(terms)):
   n,e=terms[j];total[tuple(sorted(m+n))]+=c*e*(1 if i==j else 2)
total={m:c for m,c in total.items() if c}
assert total==dec(table)
assert used=={c['id'] for c in new['coordinates']}
assert len(used)==319 and len(rr)==289 and len(total)==5676
assert gcd(*total.values())==1 and max(sum(i>=0 for i in m) for m in total)==4
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert {m:c for m,c in total.items() if m.count(-1)==2}=={(-1,-1,57,57,549,549):16,(-1,-1,549,549,903,903):1}
assert all(abs(c)<=96 for m,c in total.items() if m.count(-1)==1)
assert all(abs(c).bit_length()<2048 for m,c in total.items() if -1 not in m)
out={'status':'PASS','sourcePins':pins,'exactChanges':delta,'anchorResidualIdMap':{'903':1903,'904':1904},'restorationSignOddRows':sign_rows,'currentConsumers':consumers,
 'variables':len(used),'residuals':len(rr),'monomials':len(total),'degree':4,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'acceptance':'provisional; finite composition only; components accepted; independent composition review required'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','variables','residuals','monomials','degree','content','maximumCoefficient','acceptance']},indent=2))
