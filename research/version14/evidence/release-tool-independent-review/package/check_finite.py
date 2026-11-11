from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd,lcm
import json
H=Path('work/quartic-v14-prep/quartic-299-314');O=Path('work/quartic-v14-release-review-sol/package')
def load(n):return json.loads((H/n).read_bytes())
def terms(row):
 out={}
 for t in row['terms']:
  k=(t['sPower'],tuple(t['monomial']));assert k not in out;assert tuple(sorted(k[1]))==k[1];out[k]=Fraction(t['coefficient']);assert out[k]
 return out
def square_sum(ir):
 result=defaultdict(Fraction)
 for row in ir['residuals']:
  p=terms(row);den=lcm(*(v.denominator for v in p.values()));ints={k:int(v*den) for k,v in p.items()};content=gcd(*ints.values());ints={k:v//content for k,v in ints.items()}
  for (s,m),v in ints.items():
   for (t,n),w in ints.items():result[s+t,tuple(sorted(m+n))]+=v*w
 return {k:v for k,v in result.items() if v}
checks=[]
for n in (299,314):
 src=load(f'candidate{n}-ir.json');compact=load(f'compact{n}-ir.json');ids=sorted(c['id'] for c in src['coordinates']);assert len(ids)==len(set(ids))==n
 mp={i:j+1 for j,i in enumerate(ids)};assert mp[0]==1
 supplied=load(f'coordinate-map{n}.json');assert {int(k):v for k,v in supplied['sourceToCompact'].items()}==mp
 assert {int(k):v for k,v in supplied['compactToSource'].items()}=={v:k for k,v in mp.items()}
 assert compact['coordinates']==[dict(c,id=mp[c['id']],sourceId=c['id']) for c in sorted(src['coordinates'],key=lambda c:c['id'])]
 assert len(src['residuals'])==len(compact['residuals'])
 for a,b in zip(src['residuals'],compact['residuals']):
  assert {k:v for k,v in a.items() if k!='terms'}=={k:v for k,v in b.items() if k!='terms'}
  assert {(s,tuple(mp[x] for x in m)):v for (s,m),v in terms(a).items()}==terms(b)
 source_poly=terms(load(f'polynomial{n}.json'));assert square_sum(src)==source_poly
 expected={(s,tuple(mp[x] for x in m)):v for (s,m),v in source_poly.items()};assert square_sum(compact)==expected
 stem=f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients';assert terms(load(stem+'.json'))==expected
 parsed={}
 for row in (H/(stem+'.txt')).read_text().splitlines():
  if row.startswith('#'):continue
  co,power,coords=row.split(' | ');key=(int(power),tuple(map(int,coords.split(','))) if coords else ());assert key not in parsed;parsed[key]=Fraction(co)
 assert parsed==expected
 assert len(expected)==(6630 if n==299 else 6672);assert max(len(m) for s,m in expected)==4;assert gcd(*(v.numerator for v in expected.values()))==1
 if n==314:assert all(s==0 for s,m in expected);maximum=max(abs(v) for v in expected.values());assert maximum.numerator.bit_length()==6496 and len(str(maximum.numerator))==1956
 else:
  groups=defaultdict(dict)
  for (s,m),v in expected.items():groups[m][s]=v
  assert groups[(mp[89],)*4]=={2:Fraction(186624)}
  for poly in groups.values():
   for sign in (-1,1):
    delta={s:Fraction(186624 if s==2 else 0)+sign*poly.get(s,0) for s in set(poly)|{2}};delta={k:v for k,v in delta.items() if v}
    if delta:assert delta[max(delta)]>0 and sum(abs(v) for k,v in delta.items() if k<max(delta))<2**2048
 checks.append({'variables':n,'residuals':len(src['residuals']),'terms':len(expected),'input':1,'result':'passed'})
(O/'FINITE-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
