"""Discover and check every physical input-square consumer after scalar fusion."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def canon(q):
 a=q[min(q)];return {m:v/a for m,v in q.items()}
def shift(q):
 out={}
 for (power,mon),v in q.items():
  n=mon.count(248);rest=tuple(i for i in mon if i!=248)
  for k in range(n+1):
   key=power,tuple(sorted(rest+(248,)*k));out[key]=out.get(key,0)+v*comb(n,k)*1200**(n-k)
 return {m:v for m,v in out.items() if v}
before=read('combined438-ir.json');after=read('combined435-ir.json')
b={r['name']:p(r['terms']) for r in before['residuals']};a={r['name']:p(r['terms']) for r in after['residuals']}
bc={n for n in b if n.startswith('correction.')};ac={n for n in a if n.startswith('correction.')}
assert len(bc)==8 and len(ac)==5 and set(b)-bc==set(a)-ac
affected=[]
for n,q in b.items():
 if n in bc:continue
 expected=q if n=='inputSquare.definition' else shift(q)
 assert canon(expected)==canon(a[n]),n
 if expected!=q:affected.append(n)
assert b['inputSquare.definition']==a['inputSquare.definition']
for j,(i,g) in enumerate(zip(range(61,66),[3,11,17,35,91])):
 q={(0,(i,i)):F(1)}
 if j:q.update({(0,(i-1,i)):F(-1-g),(0,(i-1,i-1)):F(g)})
 else:q.update({(0,(i,)):F(-1-g),(0,()):F(g)})
 assert canon(q)==canon(a[f'correction.restrictedProduct{j+1}'])
removed={58,59,60}
assert not any(removed.intersection(mon) for q in a.values() for power,mon in q)
report={'verified':True,'sourceSha256':hashlib.sha256((H/'combined438-ir.json').read_bytes()).hexdigest(),'candidateSha256':hashlib.sha256((H/'combined435-ir.json').read_bytes()).hexdigest(),'allRediscoveredShiftedRows':affected,'shiftedRowCount':len(affected),'inputSquareEquationUnchanged':True,'fiveCorrectionEquationsVerified':True}
(H/'consumers435.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
