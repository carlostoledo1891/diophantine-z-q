import json,sys
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'work/jose248-audit-20261109/repository/computation/quartic/family248_v17/quadratic-family248-v17.json'
raw=SRC.read_bytes(); assert sha256(raw).hexdigest()=='b1bf58c470365a7b330af4a33a17a1f7e9aa10c997853c9078a9b8593f43a7ff'
ir=json.loads(raw)
def add(*ps):
 d={}
 for p in ps:
  for m,c in p.items(): d[m]=d.get(m,F(0))+c
 return {m:c for m,c in d.items() if c}
def sc(p,c):return {m:v*F(c) for m,v in p.items() if v*c}
def mul(p,q):
 d={}
 for m,c in p.items():
  for n,e in q.items():
   k=tuple(sorted(m+n));d[k]=d.get(k,F(0))+c*e
 return {m:c for m,c in d.items() if c}
def v(i):return {(i,):F(1)}
def con(x):return {():F(x)} if x else {}
def fa(*xs):return (add(*(x[0] for x in xs)),add(*(x[1] for x in xs)))
def fs(x,c):return sc(x[0],c),sc(x[1],c)
def fm(x,y):return add(mul(x[0],y[0]),sc(mul(x[1],y[1]),2)),add(mul(x[0],y[1]),mul(x[1],y[0]))
def fc(a,b=0):return con(a),con(b)
def pair(i,k=1):return v(i),sc(v(i+1),k)
def conj(x):return x[0],sc(x[1],-1)
checks=[]
def ck(rid,p,label):
 r=ir['residuals'][rid-1];assert r['id']==rid
 q={tuple(t['monomial']):F(t['coefficient']) for t in r['terms']};assert all(t['parameterPower']==0 for t in r['terms'])
 assert set(p)==set(q),(rid,label,'support',set(p)^set(q))
 c=q[next(iter(q))]/p[next(iter(q))];assert c and all(q[m]==c*p[m] for m in q),(rid,label,'coefficient')
 checks.append({'row':rid,'source_id':r['sourceId'],'meaning':label,'literal_row_multiplier':str(c)})
def ckpair(rid,p,label):
 ck(rid,p[0],label+' real');ck(rid+1,p[1],label+' rho')

D=fc(11,-6)
for i,a_id,b_id,c_id,V_id,I_id,Q_id,W_id,K_id,L_id,z_id in [(1,2,4,47,18,20,57,59,61,113,87),(2,6,8,49,22,24,63,65,67,117,89),(3,10,12,51,26,28,69,71,73,121,91),(4,14,16,53,30,32,75,77,79,125,93)]:
 a,b,c=pair(a_id),pair(b_id),pair(c_id,2)
 if i==3:c=(sc(c[0],2),c[1])
 V,I,Q,W,K,L,z=map(pair,[V_id,I_id,Q_id,W_id,K_id,L_id,z_id])
 ckpair(1+4*(i-1),fa(fm(a,a),fs(c,-1)),f'root{i} c=a^2')
 ckpair(3+4*(i-1),fa(fm(b,b),fs(fm(c,c),-1),D),f'root{i} b^2=c^2-D')
 first=145+8*(i-1)
 ckpair(first,fa(fm(a,I),fs(fm(b,V),-1),fs(fm(c,Q),-1),fs(fm(D,fm(V,W)),-1)),f'root{i} I equation')
 ckpair(first+2,fa(fm(a,K),fm(b,Q),fm(c,V),fm(D,fm(Q,W))),f'root{i} K equation')
 ckpair(first+4,fa(fm(V,Q),fs(fm(c,W),-1)),f'root{i} cross equation')
 ckpair(first+6,fa(fm(V,V),fm(Q,Q),fm(D,fm(W,W)),fs(fm(b,W),2),fc(-1)),f'root{i} biquadratic equation')
 ckpair(57+2*(i-1),fa(fm(V,pair(83)),fs(fm(I,L),-1)),f'root{i} primary ratio')
 ckpair(23+2*(i-1),fa(Q,fm(K,z)),f'root{i} alternate point parameter')
chi=pair(55,2);f=pair(81);S=pair(83)
ckpair(17,fa(chi,fs(fm(D,f),-1),fs(fm(S,S),-1)),'H finite chart')
ckpair(19,fa(fm(chi,f),fc(-1)),'H reciprocal')

gH=pair(206)
N=fa(fc(-312,-69),fm(fc(-236,-120),S))
Den=fa(fc(-576,-256),fm(fc(312,69),S),fm(fc(504,-1344),gH))
for rid,lp,z in [(37,115,87),(43,119,89),(49,123,91),(55,127,93)]:
 ckpair(rid,fa(fm(pair(lp),N),fs(fm(pair(z),Den),-1)),'plain alternate ratio with N_H,D_H')
ckpair(143,fa(fm(fa(fm(fc(57,-28),chi),fc(88,-48)),gH),fc(39,-36),fm(fc(8,-14),S)),'fixed subtraction gH')

a,b,r,g,J,k=map(v,range(1001,1007))
c=mul(a,a);dd=add(mul(c,c),sc(mul(b,b),-1))
d=add(c,mul(dd,mul(r,r)));e=add(c,mul(dd,mul(g,g)))
T=add(mul(c,add(mul(r,r),mul(g,g))),mul(dd,mul(mul(r,r),mul(g,g))),sc(mul(b,mul(r,g)),2),con(-1))
G=add(mul(d,g),sc(mul(a,J),-1),mul(b,r))
Ep=add(mul(a,k),mul(b,g),mul(e,r))
Hp=add(mul(d,k),sc(mul(b,J),-1),sc(mul(a,add(mul(c,r),mul(b,g))),2))
identities=[
 add(mul(c,add(mul(J,J),mul(dd,mul(mul(r,r),mul(r,r))),con(-1))),sc(mul(d,T),-1),mul(G,add(mul(d,g),mul(b,r),mul(a,J)))),
 add(mul(c,add(mul(k,k),mul(dd,mul(mul(g,g),mul(g,g))),con(-1))),sc(mul(e,T),-1),sc(mul(Ep,add(mul(a,k),sc(mul(b,g),-1),sc(mul(e,r),-1))),-1)),
 add(mul(d,Ep),sc(mul(a,Hp),-1),sc(mul(dd,mul(r,T)),-1),mul(b,G))]
assert all(not x for x in identities)
out={'status':'passed','row_checks':len(checks),'checks':checks,'generic_printed_polynomial_identities':3,'scope':'Exact row components and generic saturation identities. Arithmetic point-group premises are identified separately.'}
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','row_checks':len(checks),'generic_identities':3}))
