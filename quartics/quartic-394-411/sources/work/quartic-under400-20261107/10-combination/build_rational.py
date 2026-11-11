"""Four rational log blocks with explicit affine-output recentering."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib,sys
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def p(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def ts(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def plus(a,b):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,0)+v
 return {k:v for k,v in d.items() if v}
def sc(a,c):return {k:v*c for k,v in a.items() if v*c}
def sub(a,b):return plus(a,sc(b,-1))
def mul(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,0)+v*w
 return {k:v for k,v in d.items() if v}
def v(i):return {(0,(i,)):F(1)}
def c(a):return {(0,()):F(a)} if a else {}
def fc(a):return c(a),{}
def fa(a,b):return tuple(plus(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def fsc(a,c):return tuple(sc(x,c) for x in a)
def fm(a,b):return plus(mul(a[0],b[0]),sc(mul(a[1],b[1]),2)),plus(mul(a[0],b[1]),mul(a[1],b[0]))
def subst(a,x,b):
 d={}
 for (s,m),co in a.items():
  t={(s,tuple(i for i in m if i!=x)):co}
  for _ in range(m.count(x)):t=mul(t,b)
  d=plus(d,t)
 return d
def norm(a):
 den=reduce(lcm,(x.denominator for x in a.values()),1);g=reduce(gcd,(abs(int(x*den)) for x in a.values()),0)
 return sc(a,F(den,g))
src=sys.argv[1] if len(sys.argv)>1 else 'inputs/released498.json'
source=read(src);out=read(src);depth=read('inputs/depth519.json')
cn={c['name']:c['id'] for c in source['coordinates']};rows={r['name']:r for r in out['residuals']};maps=[];removed=set();deleted=set();renamed={};newrows=[]
def val(n):return tuple(p(depth['values'][n+'.'+str(i)]['terms']) for i in range(2))
q1,q2=F(-1526,1073),F(513,1073)
co=[F(1),F(-9776,5365),F(2941,3219),F(-1024,13949),F(-1920,237133),F(-1024,711399),F(-1408,5928325),F(0),F(2432,103152855)]
for i in [0,2,3,4]:
 pre=f'logV{i}';w=val(pre+'.w');s=val(pre+'.wPower2');oldG=val(pre+'.polynomial')
 fourth=tuple(v(cn[f'{pre}.wPower3.{j}.quadratic']) for j in range(2));R=tuple(v(cn[f'{pre}.polynomial.{j}.quadratic']) for j in range(2))
 for j in range(2):
  x=cn[f'{pre}.polynomial.{j}.quadratic'];a=oldG[j][(0,(x,))];rest=sub(oldG[j],sc(v(x),a));replacement=sc(sub(v(x),rest),1/a)
  maps.append({'coordinate':x,'oldSemantic':ts(oldG[j]),'replacement':ts(replacement)})
  renamed[x]=f'{pre}.rationalApproximation.{j}'
  renamed[cn[f'{pre}.wPower3.{j}.quadratic']]=f'{pre}.wPower4.{j}'
  removed.add(cn[f'{pre}.middle.{j}.quadratic'])
  for block in ['wPower3','middle','polynomial']:deleted.add(f'{pre}.{block}.{j}.definition')
 N=fc(1)
 for coeff,term in [(co[1],w),(co[2],s),(co[3],fm(w,s)),(co[4],fourth),(co[5],fm(w,fourth)),(co[6],fm(s,fourth)),(co[8],fm(fourth,fourth))]:N=fa(N,fsc(term,coeff))
 Q=fa(fa(fc(1),fsc(w,q1)),fsc(s,q2))
 for block,polys in [('wPower4',fs(fourth,fm(s,s))),('rationalApproximation',fs(fm(Q,R),N))]:
  for j,poly in enumerate(polys):newrows.append({'name':f'{pre}.{block}.{j}.definition','terms':ts(poly),'kind':'structural','block':'rational_log'})
assert deleted<=set(rows)
recentered=[]
for name,row in rows.items():
 if name in deleted:continue
 a=p(row['terms']);old=a
 for m in maps:a=subst(a,m['coordinate'],p(m['replacement']))
 if a!=old:recentered.append(name)
 row['terms']=ts(a)
 assert not any(set(mon)&(removed|{x for x,n in renamed.items() if '.wPower4.' in n}) for power,mon in a),name
out['coordinates']=[dict(c,name=renamed.get(c['id'],c['name'])) for c in out['coordinates'] if c['id'] not in removed]
out['residuals']=[r for r in out['residuals'] if r['name'] not in deleted]
for row in newrows:row['id']=max(r['id'] for r in out['residuals'])+1;out['residuals'].append(row)
out['status']='Rational logarithm research component; pending non-author arithmetic acceptance.'
total={}
for row in out['residuals']:
 a=norm(p(row['terms']));assert max(len(m) for s,m in a)<=2;total=plus(total,mul(a,a))
count=len(out['coordinates'])
assert count==len(source['coordinates'])-8 and len(out['residuals'])==len(source['residuals'])-8
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n')
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
prefix=f'rational{count}'
write(prefix+'-ir.json',out);write(prefix+'-polynomial.json',{'fixedParameter':out['fixedParameter'],'terms':ts(total)})
stats={'variables':count,'witnesses':count-1,'residuals':len(out['residuals']),'degree':4,'monomials':len(total),'candidateSha256':sha(prefix+'-ir.json'),'polynomialSha256':sha(prefix+'-polynomial.json')}
write(prefix+'-certificate.json',{'source':src,'sourceSha256':sha(src),'maps':maps,'removedCoordinates':sorted(removed),'deletedRows':sorted(deleted),'recenteredRows':recentered,'statistics':stats})
print(json.dumps(stats,indent=2))
