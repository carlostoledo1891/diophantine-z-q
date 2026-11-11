"""Independent source-interface, identity and full-SOS verification."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[1]));import verify494 as P
cert=P.read(H/'certificate411.json');S=Path(cert['source']);M=Path(cert['semanticSource'])
assert P.sha(S)==cert['sourceSha256']=='6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4'
assert P.sha(M)==cert['semanticSourceSha256']=='4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c'
assert P.sha(H/'candidate411-ir.json')==cert['candidateSha256'];assert P.sha(H/'polynomial411.json')==cert['polynomialSha256']
old=P.read(S);new=P.read(H/'candidate411-ir.json');sem=P.read(M);cn={c['name']:c['id'] for c in old['coordinates']};nc={c['name']:c['id'] for c in new['coordinates']};mp={c['id']:cn[c['name']] for c in sem['coordinates'] if c['name'] in cn}
before={r['name']:r for r in old['residuals']};after={r['name']:r for r in new['residuals']}
def scale(a,k):return {m:v*k for m,v in a.items() if v*k}
def sub(a,b):return P.add(a,b,-1)
def C(k):return {():F(k)} if k else {}
def fa(a,b):return tuple(P.add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def fm(a,b):return P.add(P.mul(a[0],b[0]),P.mul(a[1],b[1]),2),P.add(P.mul(a[0],b[1]),P.mul(a[1],b[0]))
def fc(a,k):return tuple(scale(x,k) for x in a)
def val(n):return tuple({tuple(sorted(-1 if v==-1 else mp[v] for v in m)):a for m,a in P.poly(sem['values'][n+'.'+str(k)]['terms']).items()} for k in range(2))
def cv(n):return tuple(P.mon(cn[n+str(k)]) for k in range(2))
def nv(n):return tuple(P.mon(nc[n+str(k)]) for k in range(2))
def canon(p):return scale(p,1/p[min(p)])
def match(rs,pre,expr,post=''):
 for j in range(2):assert canon(P.poly(rs[pre+str(j)+post]['terms']))==canon(expr[j]),pre+str(j)+post
D=(C(11),C(-6));one=(C(1),{});s=cv('primary.negativeReciprocalZ0.')
affected=set();removed=set();repurposed=set();incidences={};expectednew=set()
for op in cert['operations']:
 root,primary,vi,ui=[op[n] for n in ['root','primary','V','U']];ix=int(vi[1:]);ll=val('L'+str(ix));z=val(vi+'.z')
 a,b,c=[val(root+'.'+n) for n in ['h','j','x']];r,J=cv(primary+'.reciprocal.r'),cv(primary+'.reciprocal.J');f,Fv=val(ui+'.f'),val(vi+'.f');g,u,k=[cv(vi+'.reciprocal.'+n+'.') for n in ['g','u','k']];YU,YV=val('testSquare.1.'+str(ix-1)),val('log'+vi+'.fSquare');d=fa(c,fm(D,f))
 match(before,root+'.chart.x.',fs(c,fm(a,a)),'.definition');match(before,root+'.chart.equation.',fa(fs(fm(b,b),fm(c,c)),D))
 checks=[(primary+'.reciprocal.f.',fs(f,fm(r,r)),''),(primary+'.reciprocal.curve.',fs(fa(fm(J,J),fm(D,fm(f,f))),one),''),(vi+'.reciprocal.g.',fs(fa(fm(d,g),fm(b,r)),fm(a,J)),''),(vi+'.reciprocal.u.',fs(fs(u,fm(c,r)),fm(b,g)),''),(vi+'.reciprocal.k.',fa(fs(fm(d,k),fm(b,J)),fc(fm(a,u),2)),''),(vi+'.f.definition.',fs(Fv,fm(g,g)),''),(vi+'.z.definition.',fa(fm(k,z),g),''),('L'+str(ix)+'.definition.',fs(fm(J,ll),fm(r,s)),''),('testSquare.1.'+str(ix-1)+'.',fs(YU,fm(f,f)),'.definition'),('log'+vi+'.fSquare.',fs(YV,fm(Fv,Fv)),'.definition')]
 for pre,expr,post in checks:
  match(before,pre,expr,post);affected.update(pre+str(j)+post for j in range(2))
 pre=vi+'.biquadratic.';V,Q,I,K,W=[nv(pre+n+'.') for n in ['V','Q','I','K','W']]
 newchecks=[(pre+'cross.',fs(fm(V,Q),fm(c,W)),''),(pre+'curve.',fs(fa(fa(fa(fm(V,V),fm(Q,Q)),fm(D,fm(W,W))),fc(fm(b,W),2)),one),''),(pre+'I.',fs(fs(fs(fm(a,I),fm(b,V)),fm(c,Q)),fm(D,fm(V,W))),''),(pre+'K.',fa(fa(fa(fm(a,K),fm(b,Q)),fm(c,V)),fm(D,fm(Q,W))),''),('L'+str(ix)+'.definition.',fs(fm(I,ll),fm(V,s)),''),(vi+'.z.definition.',fa(fm(K,z),Q),''),('testSquare.1.'+str(ix-1)+'.',fs(fa(fm(D,fm(c,YU)),fm(I,I)),c),'.definition'),('log'+vi+'.fSquare.',fs(fa(fm(D,fm(c,YV)),fm(K,K)),c),'.definition')]
 for pre,expr,post in newchecks:
  match(after,pre,expr,post);expectednew.update(pre+str(j)+post for j in range(2))
 drop={cn[n+'.f.'+str(j)] for n in [ui,vi] for j in range(2)};assert drop==set(op['removedCoordinates']);removed.update(drop)
 oldvars={v for pair in [r,J,g,u,k,f,Fv] for p in pair for m in p for v in m if v!=-1};repurposed.update(oldvars-drop)
 incidences[vi]={cn_name:sorted(n for n,row in before.items() if any(cn[cn_name] in t['monomial'] for t in row['terms'])) for cn_name in [ui+'.f.0',ui+'.f.1',vi+'.f.0',vi+'.f.1']}
assert set(after)==set(before)-affected|expectednew
for n in set(before)-affected:
 assert before[n]==after[n]
 assert not any((removed|repurposed).intersection(t['monomial']) for t in before[n]['terms']),n
oc={c['id']:c for c in old['coordinates']};out={c['id']:c for c in new['coordinates']};assert set(out)==set(oc)-removed
for i in set(out)-repurposed:assert out[i]==oc[i]
for key in old:
 if key not in {'coordinates','residuals','status'}:assert old[key]==new[key]
# Two unconditional scalar polynomial identities used in reverse recovery.
a,b,c,r,J,g,k,Dd=[P.mon(i) for i in range(8)];mul=P.mul;add=P.add;a2=mul(a,a);r2=mul(r,r);g2=mul(g,g);d=add(c,mul(Dd,r2));e=add(c,mul(Dd,g2))
C0=sub(c,a2);B0=add(sub(mul(b,b),mul(c,c)),Dd)
G0=add(sub(mul(d,g),mul(a,J)),mul(b,r));E0=add(add(mul(a,k),mul(b,g)),mul(e,r))
Q0=sub(add(add(mul(c,add(r2,g2)),mul(Dd,mul(r2,g2))),scale(mul(b,mul(r,g)),2)),C(1))
P0=sub(add(mul(J,J),mul(Dd,mul(r2,r2))),C(1));K0=sub(add(mul(k,k),mul(Dd,mul(g2,g2))),C(1))
rhs=add(add(mul(d,Q0),mul(B0,r2)),scale(mul(C0,sub(mul(Dd,mul(r2,r2)),C(1))),-1));rhs=sub(rhs,mul(G0,add(add(mul(d,g),mul(b,r)),mul(a,J))))
assert mul(a2,P0)==rhs
rhs=add(add(mul(e,Q0),mul(B0,g2)),scale(mul(C0,sub(mul(Dd,mul(g2,g2)),C(1))),-1));rhs=add(rhs,mul(E0,sub(mul(a,k),add(mul(b,g),mul(e,r)))))
assert mul(a2,K0)==rhs
oldK=add(sub(mul(d,k),mul(b,J)),scale(mul(a,add(mul(c,r),mul(b,g))),2))
rhs=add(mul(a,oldK),mul(Dd,mul(r,Q0)));rhs=sub(rhs,mul(b,G0));rhs=add(rhs,scale(mul(C0,add(mul(b,g),mul(c,r))),2));rhs=add(rhs,mul(r,B0))
assert mul(d,E0)==rhs
total={}
for row in new['residuals']:
 p=P.normalized(P.poly(row['terms']));assert max(sum(x!=-1 for x in m) for m in p)<=2
 tt=list(p.items())
 for i,(m,a) in enumerate(tt):
  for j in range(i,len(tt)):
   n,b=tt[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={m:v for m,v in total.items() if v};assert total==P.poly(P.read(H/'polynomial411.json')['terms'])
assert {v for m in total for v in m if v!=-1}==set(out)
assert len(out)==411 and len(new['residuals'])==380
assert functools.reduce(math.gcd,(abs(v.numerator) for v in total.values()),0)==1
result={'passed':True,'candidateSha256':cert['candidateSha256'],'counts':cert['counts'],'unconditionalCurveRecoveryIdentities':3,'allOldNewRowsChecked':True,'removedFConsumers':incidences,'allOutsideObjectsUnchanged':True,'fullPrimitiveSOS':True}
(H/'verification411.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='removedFConsumers'},indent=2))
