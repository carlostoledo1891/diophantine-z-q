"""Exact universal identities for BIQUADRATIC_PROPOSAL.md; no file writes."""
from collections import defaultdict
class P(dict):
    def __add__(self,other):
        other=poly(other);out=defaultdict(int,self)
        for m,v in other.items():out[m]+=v
        return P({m:v for m,v in out.items() if v})
    __radd__=__add__
    def __neg__(self):return P({m:-v for m,v in self.items()})
    def __sub__(self,other):return self+-poly(other)
    def __rsub__(self,other):return poly(other)+-self
    def __mul__(self,other):
        out=defaultdict(int)
        for m,v in self.items():
            for n,w in poly(other).items():out[tuple(sorted(m+n))]+=v*w
        return P({m:v for m,v in out.items() if v})
    __rmul__=__mul__
    def __pow__(self,n):
        out=poly(1)
        for _ in range(n):out=out*self
        return out
def poly(x):return x if isinstance(x,P) else P({():x}) if x else P()
def reduce_roots(p):
    out=poly(0)
    for m,v in p.items():
        na=m.count('a');nb=m.count('b')
        rest=tuple(x for x in m if x not in ('a','b'))
        out+=P({tuple(sorted(rest+('a',)*(na%2)+('b',)*(nb%2))):v})*c**(na//2)*(c*c-D)**(nb//2)
    return out
a,b,c,D,r,g,J,k=[P({(s,):1}) for s in ('a','b','c','D','r','g','J','k')]
d=c+D*r*r
e=c+D*g*g
F=c*(r*r+g*g)+D*r*r*g*g+2*b*r*g-1
G=a*J-b*r-d*g
A=a*k+b*g+e*r
H=d*k-b*J+2*a*(c*r+b*g)
tests={
 'first discriminant':(b*r+d*g)**2+c*D*r**4-c-d*F,
 'second discriminant':(b*g+e*r)**2+c*D*g**4-c-e*F,
 'inverse addition orientation':a*H-d*A+b*G+D*r*F,
}
for label,p in tests.items():
    assert not reduce_roots(p),label
    print(label+': exact identity verified')
print('All universal polynomial identities passed. Domain and consumer obligations remain as stated in the proof.')
