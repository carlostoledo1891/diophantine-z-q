"""Apply pinned, independently reviewed relative changes with conflict checks."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,copy,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def norm(a):
 d=reduce(lcm,(v.denominator for v in a.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in a.values()),0)
 return {m:v*F(d,g)*(1 if a[min(a)]>0 else -1) for m,v in a.items()}
steps=[
 ('scalar_f1_guard','scalar443-ir.json','inputs/scalar-guard442-ir.json','inputs/scalar-guard-review.md'),
 ('positive_scalar_correction','rational453-ir.json','inputs/scalar-shift450-ir.json','inputs/scalar-shift-review.md'),
]

def main():
 d=copy.deepcopy(read('combined439-ir.json'));records=[]
 for label,src,tgt,review in steps:
  b=read(src);n=read(tgt);br={r['name']:r for r in b['residuals']};nr={r['name']:r for r in n['residuals']};dr={r['name']:r for r in d['residuals']}
  bc={c['id']:c for c in b['coordinates']};nc={c['id']:c for c in n['coordinates']};dc={c['id']:c for c in d['coordinates']}
  removed=set(bc)-set(nc);newcoords=set(nc)-set(bc)
  rename={i for i in set(nc)&set(bc) if nc[i]['name']!=bc[i]['name']}
  deleted=set(br)-set(nr);added=set(nr)-set(br);changed={name for name in set(br)&set(nr) if norm(p(br[name]['terms']))!=norm(p(nr[name]['terms']))}
  touched=set().union(*({i for s,m in p(br[name]['terms']) for i in m} for name in deleted|changed))|removed|rename
  for i in touched:assert dc[i]['name']==bc[i]['name'],(label,'coordinate semantics conflict',i,dc[i]['name'],bc[i]['name'])
  for name in deleted|changed:assert norm(p(dr[name]['terms']))==norm(p(br[name]['terms'])),(label,name)
  coordmap={}
  for i in sorted(newcoords):
   newid=i if i not in dc else max(dc)+1
   coordmap[i]=newid;dc[newid]=dict(nc[i],id=newid);d['coordinates'].append(dc[newid])
  def remap(ts):return terms({(s,tuple(sorted(coordmap.get(i,i) for i in m))):v for (s,m),v in p(ts).items()})
  for name in changed:dr[name]['terms']=remap(nr[name]['terms'])
  d['residuals']=[r for r in d['residuals'] if r['name'] not in deleted]
  rowmap={}
  for name in sorted(added):
   assert name not in dr
   newid=max(r['id'] for r in d['residuals'])+1;r=dict(nr[name],id=newid,terms=remap(nr[name]['terms']));d['residuals'].append(r);rowmap[name]=newid
  d['coordinates']=[dict(c,name=nc[c['id']]['name']) if c['id'] in rename else c for c in d['coordinates'] if c['id'] not in removed]
  records.append({'step':label,'source':src,'sourceSha256':sha(src),'target':tgt,'targetSha256':sha(tgt),'review':review,'reviewSha256':sha(review) if review else None,
   'removedCoordinates':sorted(removed),'renamedCoordinates':sorted(rename),'addedCoordinates':coordmap,'deletedRows':sorted(deleted),'changedRows':sorted(changed),'addedRows':rowmap,
   'variablesAfter':len(d['coordinates']),'residualsAfter':len(d['residuals'])})
 d['status']='Under400 research combination. No publication milestone reached.'
 total={}
 for r in d['residuals']:
  pp=norm(p(r['terms']))
  for (s,m),a in pp.items():
   for (t,n),b in pp.items():
    key=s+t,tuple(sorted(m+n));total[key]=total.get(key,0)+a*b
 total={m:v for m,v in total.items() if v}
 count=len(d['coordinates']);assert count==435 and len(d['residuals'])==412
 assert {i for s,m in total for i in m}=={c['id'] for c in d['coordinates']}
 assert max(len(m) for s,m in total)==4
 assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
 assert not any(s!=2 and m==(57,57) for s,m in total)
 assert any(s==0 and abs(v)==1 for (s,m),v in total.items())
 assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
 def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
 write(f'combined{count}-ir.json',d);write(f'combined{count}-polynomial.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
 stats={'variables':count,'witnesses':count-1,'residuals':len(d['residuals']),'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
  'candidateSha256':sha(f'combined{count}-ir.json'),'polynomialSha256':sha(f'combined{count}-polynomial.json')}
 write(f'combined{count}-certificate.json',{'source':'combined439-ir.json','sourceSha256':sha('combined439-ir.json'),'steps':records,'statistics':stats});print(json.dumps(stats,indent=2))
if __name__=='__main__':main()
