from pathlib import Path
from fractions import Fraction as F
import json,hashlib

home=Path(__file__).resolve().parent
root=home.parents[3]
source=root/'work/quartic-under400-20261107/10-combination/primary437-ir.json'
data=json.loads(source.read_text())
assert hashlib.sha256(source.read_bytes()).hexdigest()=='e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e'
ids={c['id'] for c in data['coordinates'] if c['name'] in ['H.chart.h0','H.chart.h1']}
assert ids=={17,18}
inc=[r['name'] for r in data['residuals'] if any(ids.intersection(t['monomial']) for t in r['terms'])]
assert inc==['H.chart.x.0.definition','H.chart.x.1.definition']
N=[F(1),-F(9776,5365),F(2941,3219),-F(1024,13949),-F(1920,237133),-F(1024,711399),-F(1408,5928325),F(0),F(2432,103152855)]
Q=[F(1),-F(1526,1073),F(513,1073)]
modular=[]
for poly,p in [(N,71),(Q,7)]:
    assert all(v.denominator%p for v in poly) and poly[-1].numerator%p
    roots=[x for x in range(p) if sum(v.numerator*pow(v.denominator,-1,p)*pow(x,i,p) for i,v in enumerate(poly))%p==0]
    sqrt2=[x for x in range(p) if x*x%p==2]
    assert not roots and len(sqrt2)==2
    modular.append({'prime':p,'sqrt2':sqrt2,'roots':roots})

# Laurent polynomial identities in a,b,x,S, modulo S^2=x-D/x.
def add(a,b):
    out=a.copy()
    for m,v in b.items():out[m]=out.get(m,F(0))+v
    return {m:v for m,v in out.items() if v}
def scale(a,k):return {m:v*k for m,v in a.items() if v*k}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    out={}
    for m,v in a.items():
        for n,w in b.items():
            key=tuple(i+j for i,j in zip(m,n));out[key]=out.get(key,F(0))+v*w
    return {m:v for m,v in out.items() if v}
one={(0,0,0,0):F(1)}
def power(a,n):
    out=one
    for _ in range(n):out=mul(out,a)
    return out
a,b,x,S=[{tuple(int(i==j) for i in range(4)):F(1)} for j in range(4)]
invx={(0,0,-1,0):F(1)}
c=power(a,2);D=sub(power(a,4),power(b,2));S2=sub(x,mul(D,invx))
def reduce(a):
    out={}
    for m,v in a.items():out=add(out,mul({m[:3]+(m[3]%2,):v},power(S2,m[3]//2)))
    return out
d=add(mul(c,x),D);N=sub(mul(a,S),b)
T=add(mul(sub(scale(D,-2),mul(mul(a,b),S)),d),scale(mul(mul(D,b),N),2))
e=sub(x,c);M=add(mul(x,S),mul(a,b))
X=sub(power(M,2),mul(add(x,c),power(e,2)))
Y=sub(mul(M,sub(mul(x,power(e,2)),X)),mul(mul(x,S),power(e,3)))
assert not reduce(sub(mul(mul(X,x),power(N,2)),mul(power(d,2),power(e,2))))
assert not reduce(sub(mul(mul(mul(Y,a),x),power(N,3)),mul(mul(T,d),power(e,3))))
assert not reduce(sub(add(mul(mul(x,power(T,2)),one),mul(mul(mul(c,D),power(x,2)),power(N,4))),mul(c,power(d,4))))
out={'passed':True,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'H_h_ids':sorted(ids),'full_incidence':inc,'modular_nonvanishing':modular,'difference_abscissa_and_ordinate':True,'reciprocal_curve_identity':True}
(home/'checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
