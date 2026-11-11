"""Independent identities for the new alternate-ordinate elimination."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json
def add(*ps):
    o=defaultdict(Q)
    for p in ps:
        for m,c in p.items():o[m]+=c
    return {m:c for m,c in o.items() if c}
def scale(p,a):return {m:c*a for m,c in p.items() if c*a}
def mul(*ps):
    o={():Q(1)}
    for p in ps:
        n=defaultdict(Q)
        for m,c in o.items():
            for j,d in p.items():n[tuple(sorted(m+j))]+=c*d
        o={m:c for m,c in n.items() if c}
    return o
def v(x):return {(x,):Q(1)}
def const(x):return {():Q(x)} if x else {}
f,F,h,s,D,c,z=map(v,['f','F','h','s','D','c','z'])
delta=add(f,scale(F,-1));k=add(mul(s,delta),scale(h,-1))
P=add(mul(h,h),scale(f,-1),mul(D,f,f,f))
A=add(mul(k,k),scale(F,-1),mul(D,F,F,F))
T=add(scale(mul(s,h),2),scale(mul(c,delta),-1),const(-1),mul(D,add(scale(mul(f,f),2),mul(f,F))))
R=add(mul(s,s),scale(c,-1),mul(D,add(f,F)))
oldDD=add(mul(s,add(h,scale(k,-1))),const(-1),mul(D,add(mul(f,f),mul(f,F),mul(F,F))))
assert A==add(P,scale(mul(delta,T),-1),mul(delta,delta,R))
assert oldDD==add(T,scale(mul(delta,R),-1))
coef=add(const(1),scale(mul(D,F,F),-1))
regular=add(mul(coef,z),scale(k,-1));raw=add(mul(k,z),scale(F,-1))
assert mul(coef,raw)==add(mul(k,regular),A)
# Retained caches only replace literal squares; no division is used above.
out={'status':'PASS','alternateCurveIdentity':'A=P-(f-F)*T+(f-F)^2*R',
     'dividedDifferenceIdentity':'oldDD=T-(f-F)*R',
     'rawRatioIdentity':'(1-D*F^2)*(k*z-F)=k*((1-D*F^2)*z-k)+A',
     'reconstruction':'k=s*(f-F)-h',
     'divisionRequiredOnlyFor':'Recover raw ratio after proving 1-D*F^2 nonzero',
     'scope':'Universal algebra only; candidate binding and arithmetic order are separate.'}
home=Path(__file__).resolve().parent
(home/'IDENTITIES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
