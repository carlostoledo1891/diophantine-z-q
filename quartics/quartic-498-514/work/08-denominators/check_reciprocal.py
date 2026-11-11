"""Exact checks for the fixed-target reciprocal difference chart.

Uses only Python's standard library. Polynomial reduction is modulo
j^2=h^4-D over Q(sqrt(2)); no numerical approximations are used.
"""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[1] / 'quartic-version6-release' / 'repository'

def k(a=0,b=0): return (F(a),F(b))
def ka(x,y): return (x[0]+y[0],x[1]+y[1])
def kn(x): return (-x[0],-x[1])
def ks(x,y): return ka(x,kn(y))
def km(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def ki(x):
    n=x[0]**2-2*x[1]**2
    assert n
    return (x[0]/n,-x[1]/n)
def kd(x,y): return km(x,ki(y))
def kp(x,n):
    r=k(1)
    for _ in range(n): r=km(r,x)
    return r
def fmt(x): return [str(v) for v in x]

D=k(11,-6); a=k(-1,F(7,4)); b=k(F(39,8),F(-9,2)); c=kp(a,2)
assert ks(kp(a,4),kp(b,2))==D

def pc(v): return {} if v==k() else {(0,0):v}
def pa(*ps):
    out={}
    for p in ps:
        for m,v in p.items():
            out[m]=ka(out.get(m,k()),v)
            if out[m]==k(): del out[m]
    return out
def pn(p): return {m:kn(v) for m,v in p.items()}
def ps(p,q): return pa(p,pn(q))
def pm(p,q):
    out={}
    for (h1,j1),v1 in p.items():
        for (h2,j2),v2 in q.items():
            hh,jj=h1+h2,j1+j2; vv=km(v1,v2)
            if jj<2:
                out=pa(out,{(hh,jj):vv})
            else:
                assert jj==2
                out=pa(out,{(hh+4,0):vv},{(hh,0):kn(km(D,vv))})
    return out
def pp(p,n):
    r=pc(k(1))
    for _ in range(n): r=pm(r,p)
    return r
def scale(p,v): return pm(p,pc(v))

h={(1,0):k(1)}; j={(0,1):k(1)}; x=pp(h,2)
d=pa(scale(x,c),pc(D)); dx=ps(x,pc(c))
N=ps(scale(j,a),scale(h,b))
M=pn(pa(scale(pm(h,pa(x,pc(c))),km(k(2),km(a,D))),
        scale(pm(j,ps(scale(x,c),pc(D))),b)))
slopeN=pa(pm(h,j),pc(km(a,b)))
Xnum=ps(pp(slopeN,2),pm(pa(x,pc(c)),pp(dx,2)))
Ynum=ps(pm(slopeN,ps(pm(x,pp(dx,2)),Xnum)),pm(pm(h,j),pp(dx,3)))
identities={
    'reciprocal_quartic': pa(pp(M,2),scale(pp(N,4),D),pn(pp(d,4))),
    'reciprocal_x': ps(pm(Xnum,pp(N,2)),pm(pp(dx,2),pp(d,2))),
    'reciprocal_y': ps(pm(Ynum,pp(N,3)),pm(pm(M,d),pp(dx,3))),
    'zero_numerator_factorization': ps(pm(N,pa(scale(j,a),scale(h,b))),pm(dx,d)),
}
for name,p in identities.items(): assert not p, (name,p)

def double(P):
    xx,yy=P
    m=kd(ks(km(k(3),kp(xx,2)),D),km(k(2),yy))
    xx2=ks(kp(m,2),km(k(2),xx))
    return xx2,ks(km(m,ks(xx,xx2)),yy)
def reciprocal(hh,jj):
    xx=kp(hh,2); dd=ka(km(c,xx),D)
    nn=ks(km(a,jj),km(b,hh))
    mm=kn(ka(km(km(k(2),km(a,D)),km(hh,ka(xx,c))),
             km(b,km(jj,ks(km(c,xx),D)))))
    gg=kd(nn,dd); kk=kd(mm,kp(dd,2))
    assert ka(kp(kk,2),km(D,kp(gg,4)))==k(1)
    return gg,kk

P=(c,km(a,b)); minus_two_P=double((P[0],kn(P[1])))
g0,k0=reciprocal(a,b)
assert g0==k() and k0==k(-1)
gm,kkm=reciprocal(a,kn(b))
assert (ki(kp(gm,2)),kd(kkm,kp(gm,3)))==minus_two_P
# A local counterexample to deleting dx guards from the old formula.
fake_x=km(k(-2),c); fake_y=P[1]
fake_curve_defect=ks(kp(fake_y,2),ks(kp(fake_x,3),km(D,fake_x)))
assert fake_curve_defect!=k()

ir_path=REPO/'quartics/quartic-523-540/final523_540/symbolic523/integer-candidate-ir.json'
ir=json.loads(ir_path.read_text())
inventory=[]
for guard in ir['guards']:
    ids=sorted({i for comp in guard.get('fieldInverse',[guard.get('inverse',[])])
                for term in comp for i in term['monomial']})
    rows=[r['name'] for r in ir['residuals'] if any(set(t['monomial'])&set(ids) for t in r['terms'])]
    inventory.append({'name':guard['name'],'coordinateIds':ids,'rowsUsingInverse':rows})

report={
    'sourceSha256':hashlib.sha256(ir_path.read_bytes()).hexdigest(),
    'sourceCoordinates':len(ir['coordinates']), 'sourceResiduals':len(ir['residuals']),
    'polynomialIdentities':{name:'zero remainder' for name in identities},
    'Q_equals_P':{'g':fmt(g0),'k':fmt(k0),'guard':'excluded'},
    'Q_equals_minus_P':{'g':fmt(gm),'k':fmt(kkm),'matches_minus_two_P':True},
    'unguarded_old_slope_zero_curve_defect':fmt(fake_curve_defect),
    'fixedTargetCoordinates':{'old':12,'new':11,'savingEach':1,'occurrences':2,'candidateTotal':521},
    'inventory':inventory,
}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({key:value for key,value in report.items() if key!='inventory'},indent=2))
