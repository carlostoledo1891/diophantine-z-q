from fractions import Fraction as F
from collections import defaultdict
def add(*ps):
    q=defaultdict(F)
    for p in ps:
        for m,c in p.items():q[m]+=c
    return {m:c for m,c in q.items() if c}
def scale(p,k):return {m:c*k for m,c in p.items() if c*k}
def mul(a,b):
    q=defaultdict(F)
    for m,c in a.items():
        for n,d in b.items():q[tuple(sorted(m+n))]+=c*d
    return {m:c for m,c in q.items() if c}
def v(i):return {(i,):F(1)}
def constant(x):return {():F(x)} if x else {}
def ka(*xs):return add(*(x[0] for x in xs)),add(*(x[1] for x in xs))
def ks(x,k):return scale(x[0],k),scale(x[1],k)
def km(a,b):return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def pair(i,re=1,im=1):return scale(v(i),re),scale(v(i+1),im)
def kc(x):return constant(x),{}
def dec(r):
    p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
    assert len(p)==len(r['terms']) and all(p.values());return p
