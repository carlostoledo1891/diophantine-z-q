"""Independent finite checks for the four half-abscissa norm charts.
The Mordell-Weil/squareclass argument is reviewed separately in REPORT.md.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent))
import verify494 as P
c=P.read(H/'certificate449.json');S=Path(c['source']);M=Path(c['semanticSource'])
assert P.sha(S)==c['sourceSha256']=='f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f'
assert P.sha(M)==c['semanticSourceSha256']=='4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c'
assert P.sha(Path(c['manuscript']))==c['manuscriptSha256']
assert P.sha(H/'candidate449-ir.json')==c['candidateSha256'];assert P.sha(H/'polynomial449.json')==c['polynomialSha256']
old=P.read(S);new=P.read(H/'candidate449-ir.json');sem=P.read(M)
def sc(a,k):return {m:v*k for m,v in a.items() if v*k}
def sub(a,b):return P.add(a,b,-1)
def C(k):return {():F(k)} if k else {}
def fa(a,b):return tuple(P.add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def fm(a,b):return P.add(P.mul(a[0],b[0]),P.mul(a[1],b[1]),2),P.add(P.mul(a[0],b[1]),P.mul(a[1],b[0]))
def fsc(a,k):return tuple(sc(x,k) for x in a)
def canon(a):return sc(a,1/a[min(a)])
cn={x['name']:x['id'] for x in old['coordinates']};mp={x['id']:cn[x['name']] for x in sem['coordinates'] if x['name'] in cn}
def val(n):return tuple({tuple(-1 if v==-1 else mp[v] for v in m):a for m,a in P.poly(sem['values'][n+'.'+str(k)]['terms']).items()} for k in range(2))
before={r['id']:P.poly(r['terms']) for r in old['residuals']};after={r['id']:P.poly(r['terms']) for r in new['residuals']};bn={r['name']:r for r in old['residuals']};nn={r['name']:r for r in new['residuals']};blockrows=set();removed=set()
for op in c['operations']:
 root=op['root'];prefix=root+'.odd.';t0,t1,r0,r1=op['oldCoordinates'];assert [t0,t1,r0,r1]==[cn[prefix+n] for n in ['t0','t1','r0','r1']]
 h,j,x=[val(root+'.'+n) for n in ['h','j','x']];s=fa(x,j);tt=P.mon(t0),P.mon(t1);rr=P.mon(r0),P.mon(r1)
 # Check actual base chart identities, allowing source normalization.
 for expr in [fs(x,fm(h,h)),fa(fs(fm(j,j),fm(x,x)),(C(11),C(-6)))]:
  for part in expr:
   matches=[r for n,r in bn.items() if n.startswith(root+'.chart.') and canon(P.poly(r['terms']))==canon(part)]
   assert len(matches)==1
 oldC=fs(fm(tt,tt),fsc(s,2));oldK=fs(fa(fm(tt,h),s),fm((C(1),C(1)),fm(rr,rr)))
 for k in range(2):
  assert canon(P.poly(bn[prefix+'halfParameter.'+str(k)]['terms']))==canon(oldC[k])
  assert canon(P.poly(bn[prefix+'halfAbscissaClass.'+str(k)]['terms']))==canon(oldK[k])
 expected=fs(fs(fm(tt,tt),fsc(fm(s,tt),2)),(C(11),C(-6)))
 for k in range(2):assert P.poly(nn[prefix+'halfAbscissaEquation.'+str(k)]['terms'])==expected[k]
 assert P.poly(nn[prefix+'halfAbscissaNorm']['terms'])==P.add(P.add(P.mon(t0,t0),P.mon(t1,t1),-2),P.mon(r0,r0))
 affected={ri for ri,p in before.items() if any({t0,t1,r0,r1}.intersection(m) for m in p)}
 assert affected==set(op['oldRows'])
 blockrows|=affected;removed.add(r1)
 assert op['deletedRow']==bn[prefix+'halfAbscissaClass.1']['id']
assert set(after)==set(before)-{op['deletedRow'] for op in c['operations']}
for ri,p in before.items():
 if ri not in blockrows:assert after[ri]==p
assert {x['id'] for x in new['coordinates']}=={x['id'] for x in old['coordinates']}-removed
assert old['coordinates'][0]==new['coordinates'][0] and old['fixedParameter']==new['fixedParameter']
# Generic identities over any characteristic-zero commutative field.
h,x,j,t,a,D=[P.mon(i) for i in range(1,7)];s=P.add(x,j)
square=lambda p:P.mul(p,p)
A=sub(x,square(h));B=P.add(sub(square(j),square(x)),D);K=sub(P.add(P.mul(t,h),s),a);C0=sub(square(t),sc(s,2));F0=sub(sub(square(a),sc(P.mul(s,a),2)),D)
rhs=P.add(P.add(P.add(P.mul(square(h),C0),P.mul(sc(s,-2),A)),B,-1),P.mul(sc(P.mul(t,h),-2),K));rhs=P.add(rhs,square(K))
assert F0==rhs
assert sub(square(sub(a,s)),sc(P.mul(s,square(h)),2))==P.add(P.add(F0,B),sc(P.mul(s,A),2))
aprime=sub(sc(s,2),a)
assert sub(sub(square(aprime),sc(P.mul(s,aprime),2)),D)==F0
assert P.add(P.mul(a,aprime),D)==sc(F0,-1)
# Halfpoint curve and duplication with a=th+t^2/2, x=h^2, j=t^2/2-h^2.
aa=P.add(P.mul(t,h),sc(square(t),F(1,2)));xx=square(h);jj=sub(sc(square(t),F(1,2)),xx);dd=sub(square(aa),P.mul(aa,square(t)));yy=P.mul(aa,t);slope=P.add(h,t)
assert sub(sc(P.mul(yy,slope),2),sub(sc(square(aa),3),dd))=={}
assert sub(sub(square(slope),sc(aa,2)),xx)=={}
assert sub(sub(P.mul(slope,sub(aa,xx)),yy),P.mul(h,jj))=={}
# Norm(epsilon*r^2)=-Norm(r)^2, with epsilon=1+sqrt(2).
u,v=P.mon(7),P.mon(8);rpair=(u,v);ep=(C(1),C(1));out=fm(ep,fm(rpair,rpair));normout=sub(square(out[0]),sc(square(out[1]),2));normr=sub(square(u),sc(square(v),2));assert P.add(normout,square(normr))=={}
# Full primitive SOS.
total={}
for p in after.values():
 assert max(sum(v!=-1 for v in m) for m in p)<=2
 terms=list(P.normalized(p).items())
 for i,(m,a) in enumerate(terms):
  for k in range(i,len(terms)):
   n,b=terms[k];z=tuple(sorted(m+n));total[z]=total.get(z,F(0))+a*b*(1 if i==k else 2)
total={m:v for m,v in total.items() if v}
assert total==P.poly(P.read(H/'polynomial449.json')['terms'])
assert {v for m in total for v in m if v!=-1}=={x['id'] for x in new['coordinates']}
assert len(new['coordinates'])==449 and len(after)==426 and len({tuple(v for v in m if v!=-1) for m in total})==6536
assert max(sum(v!=-1 for v in m) for m in total)==4
assert functools.reduce(math.gcd,(abs(v.numerator) for m,v in total.items() if -1 not in m),0)==1
assert {m:v for m,v in total.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
result={'verified':True,'variables':449,'witnesses':448,'residuals':426,'degree':4,'monomials':6536,'content':1,'maxCoefficient':'16*3^(2^26)','candidateSha256':c['candidateSha256'],'polynomialSha256':c['polynomialSha256'],'scope':'Exact equations, generic halfpoint and norm identities, private incidence, unchanged consumers, complete SOS; arithmetic squareclass argument separately reviewed.'}
(H/'verification449.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
