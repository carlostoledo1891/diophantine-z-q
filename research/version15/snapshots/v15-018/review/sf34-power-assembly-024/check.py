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
# New component identities. Accepted022 inputs are used, not reproved here.
for i,l,out,row in [(1,113,144,80),(2,117,150,86),(3,121,152,88),(4,125,154,90)]:
 C=fa(pair(l),fs(conj(pair(l+2)),-1))
 ckpair(row,fa(fm(C,C),fs(pair(out,2),-1)),f'C{i} square')
f=pair(81);ckpair(84,fa(fm(f,f),fs(pair(148,2),-1)),'H reciprocal-abscissa square')
Fshift=pair(134,2)
ckpair(92,fa(fm(Fshift,Fshift),fs(pair(156,4),-1)),'stored (G+1) square')
ckpair(181,fa(fm(pair(144,2),pair(144,2)),fs(pair(211),-1)),'C1 fourth power')
D=fc(11,-6);D2=fm(D,D)
for i,cs,is_,ks,ys,zs in [(1,47,20,61,136,99),(2,49,24,67,138,101),(3,51,28,73,140,105),(4,53,32,79,142,109)]:
 c=pair(cs,2)
 if i==3:c=(sc(c[0],2),c[1])
 ckpair(72+2*(i-1),fa(fm(pair(is_),pair(is_)),fs(c,-1),fm(fm(D,c),pair(ys,2))),f'I{i}^2-c{i}+D*c{i}*A{i}^2')
 vr={1:35,2:39,3:45,4:51}[i]
 ckpair(vr,fa(c,fs(fm(pair(ks),pair(ks)),-1),fs(fm(fm(D,c),pair(zs,2)),-1)),f'c{i}-K{i}^2-D*c{i}*f(V{i})^2')
# D-scaled fourth powers for i=2,3,4 extend accepted022 i=0.
for i,inp,out,row in [(2,101,103,41),(3,105,107,47),(4,109,111,53)]:
 value=fm(D2,fm(pair(inp,2),pair(inp,2)))
 stored=(sc(v(out),193),sc(v(out+1),-132))
 ckpair(row,fa(value,fs(stored,-1)),f'D^2*f(V{i})^4')
# Exact inverse of D^2 followed by conjugation.
def bp(out):return sc(add(sc(v(out),37249),sc(v(out+1),-34848)),F(1,2401)),sc(add(v(out),sc(v(out+1),-1)),F(-25476,2401))
for out in [97,103,107,111]:
 recovered=conj(fm(fc(F(193,2401),F(132,2401)),(sc(v(out),193),sc(v(out+1),-132))))
 assert recovered==bp(out)
G2=fa(pair(156,4),fs(pair(134,2),-2),fc(1))
powers={'C1^4':pair(211),'I^4':pair(213),'B1^4':pair(215),'H^2':pair(148,2),'G^2':G2}
for i,out in enumerate([136,138,140,142],1):powers[f'A{i}^2']=pair(out,2)
for i,out in [(2,150),(3,152),(4,154)]:powers[f'C{i}^2']=pair(out,2)
for i,out in [(0,97),(2,103),(3,107),(4,111)]:powers[f'B{i}^4']=bp(out)
groups=[[(7,'C2^2'),(2,'H^2'),(4,'B1^4')],[(7,'G^2'),(2,'A3^2'),(4,'B0^4')],[(7,'I^4'),(1,'A2^2'),(2,'A4^2'),(4,'B3^4')],[(7,'C3^2'),(2,'C1^4'),(4,'B4^4')],[(7,'C4^2'),(2,'A1^2'),(4,'B2^4')]]
for det,start,row,weights,ws in [(0,217,187,{1:161,2:163,4:164,7:162},165),(1,233,205,{1:176,2:178,4:179,7:177},180)]:
 for j,g in enumerate(groups):
  value=fa(fc(1),*(fm((v(weights[e]),{}),powers[name]) for e,name in g),fs(pair(start+2*j),-1))
  ckpair(row+2*j,value,f'detector{det} T{j+1}')
 left=pair(start)
 for j in range(1,5):
  out=pair(start+8+2*j) if j<4 else pair(ws)
  ckpair(row+10+2*(j-1),fa(fm(left,pair(start+2*j)),fs(out,-1)),f'detector{det} product through T{j+1}')
  left=out
out={'status':'passed','scope':'exact component polynomial identities; conditional semantic typing, no new arithmetic acceptance','source_sha256':sha256(raw).hexdigest(),'row_checks':len(checks),'checks':checks,'D_inverse_conjugation_checks':4}
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','row_checks':len(checks)}))
