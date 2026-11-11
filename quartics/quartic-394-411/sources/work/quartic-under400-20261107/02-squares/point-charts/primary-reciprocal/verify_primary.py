"""Read-only exact algebra/SOS check; identity-domain arithmetic is separate."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[1]));import verify494 as P
cert=P.read(H/'certificate428.json');S=Path(cert['source']);M=Path(cert['semanticSource'])
assert P.sha(S)==cert['sourceSha256']=='c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859'
assert P.sha(M)==cert['semanticSourceSha256']=='4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c'
assert P.sha(H/'candidate428-ir.json')==cert['candidateSha256'];assert P.sha(H/'polynomial428.json')==cert['polynomialSha256']
old=P.read(S);new=P.read(H/'candidate428-ir.json');sem=P.read(M)
cn={c['name']:c['id'] for c in old['coordinates']};nc={c['name']:c['id'] for c in new['coordinates']};mp={c['id']:cn[c['name']] for c in sem['coordinates'] if c['name'] in cn}
before={r['name']:r for r in old['residuals']};after={r['name']:r for r in new['residuals']}
def sc(a,k):return {m:x*k for m,x in a.items() if x*k}
def C(k):return {():F(k)} if k else {}
def fa(a,b):return tuple(P.add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(P.add(x,y,-1) for x,y in zip(a,b))
def fc(a,k):return tuple(sc(x,k) for x in a)
def fm(a,b):return P.add(P.mul(a[0],b[0]),P.mul(a[1],b[1]),2),P.add(P.mul(a[0],b[1]),P.mul(a[1],b[0]))
def val(n):return tuple({tuple(sorted(-1 if v==-1 else mp[v] for v in m)):a for m,a in P.poly(sem['values'][n+'.'+str(k)]['terms']).items()} for k in range(2))
def nv(n):return tuple(P.mon(nc[n+str(k)]) for k in range(2))
def canon(p):return sc(p,1/p[min(p)])
def match(rows,pre,expr,post=''):
 for j in range(2):assert canon(P.poly(rows[pre+str(j)+post]['terms']))==canon(expr[j]),pre+str(j)+post
D=(C(11),C(-6));one=(C(1),{});s=nv('primary.negativeReciprocalZ0.')
affected=set();removed=set();repurposed=set();expectednew=set()
for op in cert['operations']:
 primary,root,U,V,L=[op[n] for n in ['primary','root','U','V','L']]
 a,b,c=[val(root+'.'+n) for n in ['h','j','x']];h,j,x=[val(primary+'.'+n) for n in ['h','j','x']]
 m,q,yp=[val(V+'.'+n) for n in ['slope','slopeSquare','yProduct']];fv,z,ll,f=[val(n) for n in [V+'.f',V+'.z',L,U+'.f']]
 match(before,primary+'.chart.x.',fs(fm(h,h),x),'.definition')
 match(before,primary+'.chart.equation.',fa(fs(fm(j,j),fm(x,x)),D))
 match(before,U+'.f.definition.',fs(fm(x,f),one))
 match(before,L+'.definition.',fs(fm(j,ll),fm(h,s)))
 match(before,V+'.slope.definition.',fa(fa(fm(h,j),fm(a,b)),fm(fs(c,x),m)))
 match(before,V+'.slopeSquare.',fs(fm(m,m),q),'.definition')
 match(before,V+'.yProduct.',fa(fa(fm(h,j),fm(m,fs(fs(q,c),fc(x,2)))),yp),'.definition')
 xr=fs(fs(q,c),x);yr=yp
 match(before,V+'.f.definition.',fs(fm(xr,fv),one))
 match(before,V+'.z.definition.',fa(xr,fm(yr,z)))
 tangent=fs(fs(fm(q,fs(fa(x,c),fc(xr,2))),fc(fm(m,yr),2)),fs(fa(fa(fm(x,x),fm(x,c)),fm(c,c)),D))
 match(before,V+'.completeTangent.',tangent)
 r,J,g,u,k=[nv(n) for n in [primary+'.reciprocal.r',primary+'.reciprocal.J',V+'.reciprocal.g.',V+'.reciprocal.u.',V+'.reciprocal.k.']]
 d=fa(c,fm(D,f))
 for pre,expr in [(primary+'.reciprocal.f.',fs(f,fm(r,r))),(primary+'.reciprocal.curve.',fs(fa(fm(J,J),fm(D,fm(f,f))),one)),(V+'.reciprocal.g.',fs(fa(fm(d,g),fm(b,r)),fm(a,J))),(V+'.reciprocal.u.',fs(fs(u,fm(c,r)),fm(b,g))),(V+'.reciprocal.k.',fa(fs(fm(d,k),fm(b,J)),fc(fm(a,u),2))),(V+'.f.definition.',fs(fv,fm(g,g))),(V+'.z.definition.',fa(fm(k,z),g)),(L+'.definition.',fs(fm(J,ll),fm(r,s)))]:
  match(after,pre,expr);expectednew.update(pre+str(j) for j in range(2))
 ids=set(op['changedRows'])|set(op['deletedRows']);affected.update(ids);removed.update(op['removedCoordinates'])
 repurposed.update(v for vv in [h,j,m,q,yp] for p in vv for mm in p for v in mm if v!=-1)
assert set(r['id'] for r in new['residuals'])==(set(r['id'] for r in old['residuals'])-set(x for op in cert['operations'] for x in op['deletedRows']))|{cert['guardRow']}
for r in old['residuals']:
 if r['id'] not in affected:
  assert not any((removed|repurposed).intersection(t['monomial']) for t in r['terms']),r['name']
  assert after[r['name']]==r
assert P.poly(after['V0.reciprocal.f0Inverse.definition']['terms'])==P.add(P.mon(160,cert['guardCoordinate']),P.mon(),-1)
assert P.poly(before['V0.f.definition.0']['terms'])==P.add(P.add(P.mon(160),P.mon(700,700),-1),P.mon(701,701),-2)
oc={c['id']:c for c in old['coordinates']};newc={c['id']:c for c in new['coordinates']}
assert set(newc)==set(oc)-removed|{cert['guardCoordinate']}
for i in set(oc)-removed-repurposed:assert oc[i]==newc[i]
for key in old:
 if key not in {'coordinates','residuals','status'}:assert old[key]==new[key]
total={}
for r in new['residuals']:
 p=P.normalized(P.poly(r['terms']));assert max(sum(v!=-1 for v in mm) for mm in p)<=2
 tt=list(p.items())
 for i,(mm,a) in enumerate(tt):
  for j in range(i,len(tt)):
   nn,b=tt[j];key=tuple(sorted(mm+nn));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={k:v for k,v in total.items() if v}
assert total==P.poly(P.read(H/'polynomial428.json')['terms'])
assert {i for m in total for i in m if i!=-1}==set(newc)
assert len(newc)==428 and len(new['residuals'])==397
assert functools.reduce(math.gcd,(abs(v.numerator) for v in total.values()),0)==1
# Generic identities, independent of the actual coefficient expansion above.
import sympy as sp
a,b,r,J,dD=sp.symbols('a b r J D');cc=a*a;ff=r*r;dd=cc+dD*ff;N=a*J-b*r;K=b*J*dd-2*a*(cc*r*dd+b*N)
def red(poly):
 poly=sp.rem(sp.Poly(sp.expand(poly),J),sp.Poly(J*J-1+dD*r**4,J)).as_expr()
 return sp.expand(sp.rem(sp.Poly(poly,b),sp.Poly(b*b-a**4+dD,b)).as_expr())
assert red(K*K+dD*N**4-dd**4)==0
assert red(K-(-b*J*(cc-dD*ff)-2*dD*a*r*(cc*ff+1)))==0
# At r=0 these give the negative root. At N=0, the norm identity gives k²=1.
assert sp.expand(N.subs(r,0))==a*J
assert red(K.subs(r,0)+a*a*b*J)==0
result={'passed':True,'sourceSha256':P.sha(S),'candidateSha256':P.sha(H/'candidate428-ir.json'),'counts':cert['counts'],'literalOldAndNewRows':True,'allOutsideObjectsUnchanged':True,'fullPrimitiveSOS':True,'genericNormAndOrientationIdentity':True,'arithmeticIdentityExtension':'separate independent review required'}
(H/'verification428.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
