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
 q={tuple(sorted(t['monomial']+[999]*t['parameterPower'])):F(t['coefficient']) for t in r['terms']}
 assert set(p)==set(q),(rid,label,'support',set(p)^set(q))
 c=q[next(iter(q))]/p[next(iter(q))];assert c and all(q[m]==c*p[m] for m in q),(rid,label,'coefficient')
 checks.append({'row':rid,'source_id':r['sourceId'],'meaning':label,'literal_row_multiplier':str(c)})
def ckpair(rid,p,label):
 ck(rid,p[0],label+' real');ck(rid+1,p[1],label+' rho')

def powp(p,n):
 r=con(1)
 for _ in range(n):r=mul(r,p)
 return r
def coeff(row,mon):
 return F(next(t['coefficient'] for t in ir['residuals'][row-1]['terms'] if t['monomial']==mon))
D=fc(11,-6)
ckpair(21,fa(fm(pair(81),pair(85)),fs(fm(pair(206),pair(206)),-1)),'f(H)*f(V0)=gH^2')
# Scalar normalizer: solve only constant-linear output gates, compare the independent five-factor formula.
x=v(129);beta=add(sc(x,51),con(2504))
p187=sc(powp(add(beta,con(-3)),2),F(1,4))
ck(121,add(powp(add(beta,con(-3)),2),sc(v(187),-4)),'scalar first intermediate')
r122=ir['residuals'][121]
def subst_row(row,env):
 out={}
 for t in row['terms']:
  term=con(t['coefficient'])
  for i in t['monomial']:term=mul(term,env.get(i,v(i)))
  out=add(out,term)
 return out
p188=sc(subst_row(r122,{187:p187,188:{}}),F(1,1525940))
p189=sc(subst_row(ir['residuals'][122],{187:p187,188:p188,189:{}}),-1)
rs=con(1)
for f in [beta,add(beta,con(-1)),add(beta,con(-2401)),add(sc(beta,32),con(343)),add(sc(beta,2),con(-1))]:rs=mul(rs,f)
assert p189==rs
checks.append({'rows':[121,122,123],'meaning':'successive unique intermediates give exact five-factor scalar r_s','status':'passed'})
ck(178,add(mul(add(con(1),sc(v(189),149**2)),v(208)),sc(mul(v(999),v(189)),-1)),'R_s*(1+149^2*r_s)=A_N*r_s')
ck(139,add(v(204),sc(powp(v(208),2),-1)),'R_s squared')
ck(140,add(powp(v(204),2),sc(v(205),-1)),'R_s fourth')
ck(141,add(powp(v(191),2),sc(v(197),-1)),'Z1 squared')
ck(142,add(powp(v(190),2),mul(v(197),v(208)),sc(mul(v(198),v(205)),-1)),'R_s^4*A=Z0^2+R_s*Z1^2')
ck(133,add(powp(v(148),2),sc(powp(v(149),2),-8),sc(v(199),-1)),'Norm(f)^2 from stored f^2')
ck(134,add(powp(v(198),2),mul(v(199),v(208)),sc(mul(v(200),v(205)),-1)),'R_s^4*W_s=A^2+R_s*Norm(f)^2')
M=coeff(126,[192]);K=coeff(130,[43,193]);L=coeff(129,[193,194]);assert K==82479248*M and 3*L==17*K
ck(126,add(sc(v(192),M),sc(powp(v(200),2),-1)),'scaled W_s square')
ck(127,add(mul(v(192),v(204)),sc(mul(v(192),v(208)),9792),sc(v(193),82479248)),'b_s=-K*barb=R_s*(R_s+9792)*W_s^2')
# Actual fixed-subtraction component equations, retaining their geometric prerequisites.
h,j,c,gs=pair(6),pair(8),pair(49,2),pair(201)
ckpair(135,fa(fm(fa(fm(fc(57,-28),c),fc(88,-48)),gs),fm(fc(39,-36),h),fm(fc(8,-14),j)),'S-P fixed subtraction')
NS=fa(fm(fc(-660,417),h),fm(fc(-228,112),j))
DS=fa(fm(fc(-704,384),h),fm(fc(660,-417),j),fm(fc(6888,-5040),gs))
ckpair(124,fa(fm(pair(190),DS),fm(NS,pair(83))),'Z*D_S=-N_S*S_H')
ck(177,add(con(1),sc(mul(v(201),v(203)),-1)),'gS real component inverse')
# Pole systems. This checks the complete signed scalar rescaling, not only the two constant ratios.
for base,ee,uu,pp,qq,bp,p2,vv,q2,scaleK in [(102,35,36,37,38,168,169,170,171,F(1)),(116,39,40,41,42,183,184,185,186,F(1)),(128,43,44,45,46,193,194,195,196,K)]:
 ck(base,add(powp(v(pp),2),sc(v(p2),-1)),'pole p-square')
 if scaleK==1:E,U,V,B,P2,Q2=v(ee),v(uu),v(vv),v(bp),v(p2),v(q2)
 else:E,U,V,B,P2,Q2=sc(v(ee),-1/K),sc(v(uu),1/K),sc(v(vv),-1),sc(v(bp),-K),sc(v(p2),1/(K*K)),sc(v(q2),1/(K*K))
 ck(base+1,add(con(289),sc(E,34),sc(mul(E,E),-3),sc(mul(B,P2),-17)),'ordinary first pole conic after exact scale')
 ck(base+2,add(sc(E,17),sc(mul(E,B),-1),sc(mul(U,V),-17)),'ordinary pole product after exact scale')
 ck(base+3,add(powp(v(qq),2),sc(v(q2),-1)),'pole q-square')
 ck(base+4,add(mul(U,U),sc(mul(U,V),34),sc(mul(V,V),-867),sc(mul(B,Q2),-17)),'ordinary second pole conic after exact scale')
# Reflected contact circuit. Direct substitution into independent ten-factor polynomial.
theta=[F(0),F(-1,2),F(-1),F(1,2399),F(-32,407)];theta=theta+[2-x for x in theta]
for tid,d2,d4,d6,out,q,q2,q4,q7,row,wr,pr,w0,tau,bpole in [(34,158,159,209,160,161,163,164,162,94,97,98,165,167,168),(172,173,174,210,175,176,178,179,177,108,111,112,180,182,183)]:
 delta=add(v(tid),con(-1));dd2=powp(delta,2);dd4=powp(delta,4);dd6=powp(delta,6)
 ck(row,add(powp(delta,2),sc(v(d2),-1)),'delta squared')
 ck(row+1,add(powp(v(d2),2),sc(v(d4),-1)),'delta fourth')
 ck(179 if tid==34 else 180,add(mul(v(d2),v(d4)),sc(v(d6),-1)),'delta sixth')
 poly=con(1)
 for th in theta:poly=mul(poly,add(v(tid),con(-th)))
 contactrow=ir['residuals'][row+1]
 substituted=subst_row(contactrow,{d2:dd2,d4:dd4,d6:dd6,out:poly})
 assert not substituted
 checks.append({'row':row+2,'meaning':'F2(t) exact ten-factor contact polynomial','status':'passed'})
 ck(wr,add(mul(v(d4),v(d6)),sc(v(out),-1),sc(mul(v(out),v(q)),-1)),'delta^10=F2(t)*(1+q)')
 ck(pr,add(powp(v(q),2),sc(v(q2),-1)),'weight square')
 ck(pr+1,add(powp(v(q2),2),sc(v(q4),-1)),'weight fourth')
 ck(137 if tid==34 else 138,add(mul(v(q),v(q7)),sc(powp(v(q4),2),-1)),'q*h=q^8; h free at q=0')
 ck(pr+2,add(powp(v(w0),2),sc(mul(v(w0),v(tau)),-2),sc(powp(v(w0+1),2),-2)),'cleared reciprocal trace')
 ck(pr+3,add(mul(add(con(1),v(q)),v(bpole)),sc(powp(v(tau),2),-F(408**2,409**2))),'balanced physical pole input')
ck(107,add(mul(v(34),add(v(47),v(49),sc(v(51),2),v(53))),sc(v(172),-2)),'t1=lambda*(1/4)*Trace(sum root x)')
out={'status':'passed','checks':checks,'checked_entries':len(checks),'M':str(M),'K':str(K),'L':str(L),'scope':'Exact remaining scalar/contact/pole coefficient typing, with arithmetic prerequisites external'}
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','checked_entries':len(checks)}))
