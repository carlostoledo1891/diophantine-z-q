"""Exact primary-ratio fusion. Outputs are confined to this proposal folder."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import sys,json,hashlib
H=Path(__file__).resolve().parent
ROOT=H.parents[2]
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def ts(a):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(a.items()) if c]
def add(a,b):
 d=a.copy()
 for k,c in b.items():d[k]=d.get(k,0)+c
 return {k:c for k,c in d.items() if c}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 d={}
 for (s,m),c in a.items():
  for (t,n),e in b.items():
   k=(s+t,tuple(sorted(m+n)));d[k]=d.get(k,0)+c*e
 return {k:c for k,c in d.items() if c}
def v(i):return {(0,(i,)):F(1)}
def fa(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def fm(a,b):return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def norm(a):
 den=reduce(lcm,(x.denominator for x in a.values()),1)
 g=reduce(gcd,(abs(int(x*den)) for x in a.values()),0)
 return scale(a,F(den,g)) if g else {}
def eq(a,b):return a==b or norm(a)==norm(b) or norm(a)==scale(norm(b),-1)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def build(source_path):
 source_path=Path(source_path).resolve();source=json.loads(source_path.read_text());out=json.loads(source_path.read_text())
 cn={c['name']:c['id'] for c in source['coordinates']};rows={r['name']:r for r in source['residuals']}
 def field(prefix):return tuple(v(cn[prefix+'.'+str(j)]) for j in range(2))
 def chart(prefix,kind):return tuple(v(cn[prefix+'.chart.'+kind+str(j)]) for j in range(2))
 charts=['H','UA','US','UT','UZ'];hs=[chart(c,'h') for c in charts];js=[chart(c,'j') for c in charts]
 zs=[field(f'U{i}.z') for i in range(5)];ls=[None]+[field(f'L{i}') for i in range(1,5)]
 touched=set();removed={cn[f'U{i}.z.{j}'] for i in range(1,5) for j in range(2)}
 changed={};deleted=[]
 for i in range(5):
  old=fa(fm(js[i],zs[i]),hs[i])
  for j in range(2):
   name=f'U{i}.z.definition.{j}';assert eq(p(rows[name]['terms']),old[j]),name;touched.add(name)
   if i:deleted.append(name)
 for i in range(1,5):
  old=fs(fm(zs[0],ls[i]),zs[i]);new=fs(fm(js[i],ls[i]),fm(hs[i],zs[0]))
  for j in range(2):
   name=f'L{i}.definition.{j}';assert eq(p(rows[name]['terms']),old[j]),name;touched.add(name)
   changed[name]=new[j]
 new0=fs(fm(hs[0],zs[0]),js[0])
 for j in range(2):changed[f'U0.z.definition.{j}']=new0[j]
 allz=removed|{cn[f'U0.z.{j}'] for j in range(2)}
 incidence=[r['name'] for r in source['residuals'] if any(allz.intersection(t['monomial']) for t in r['terms'])]
 assert set(incidence)==touched,(set(incidence)-touched,touched-set(incidence))
 out['coordinates']=[c for c in out['coordinates'] if c['id'] not in removed]
 for c in out['coordinates']:
  if c['id'] in allz:c['name']='primary.negativeReciprocalZ0.'+str(c['id']-cn['U0.z.0'])
 out['residuals']=[r for r in out['residuals'] if r['name'] not in deleted]
 for r in out['residuals']:
  if r['name'] in changed:r['terms']=ts(changed[r['name']])
  assert not any(removed.intersection(t['monomial']) for t in r['terms'])
 count=len(out['coordinates']);assert count==len(source['coordinates'])-8
 out['status']='Primary reciprocal-ratio fusion; author checked, pending independent review.'
 total={}
 for r in out['residuals']:
  a=norm(p(r['terms']));assert all(len(m)<=2 for s,m in a)
  total=add(total,mul(a,a))
 dest=H/f'candidate{count}-ir.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 poly=H/f'polynomial{count}.json';poly.write_text(json.dumps({'fixedParameter':out['fixedParameter'],'terms':ts(total)},indent=2)+'\n')
 cert={'source':str(source_path),'sourceSha256':sha(source_path),'candidateSha256':sha(dest),'polynomialSha256':sha(poly),'removedCoordinates':sorted(removed),'changedRows':list(changed),'deletedRows':deleted,'completeOldZIncidence':incidence,'statistics':{'variables':count,'residuals':len(out['residuals']),'monomials':len(total),'degree':max(len(m) for s,m in total)},'substitution':'new s=-1/old z0=j0/h0; old zi=-hi/ji; retained Li unchanged'}
 (H/f'certificate{count}.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps(cert,indent=2))
 return source,out,cert
if __name__=='__main__':build(sys.argv[1] if len(sys.argv)>1 else ROOT/'quartic-under400-20261107/01-elimination/triple-cubic/elimination/candidate470-ir.json')
