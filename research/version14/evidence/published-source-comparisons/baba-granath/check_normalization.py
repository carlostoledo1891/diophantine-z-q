"""Exact check of the two displayed forms; no third-party source text."""
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

def mul(x,y):
    z=[F(0)]*4
    for u in range(4):
        for v in range(4):
            sign=(-1)**((u>>1)*(v&1))
            z[u^v]+=x[u]*y[v]*sign*(2**((u&1)*(v&1)))*((-3)**((u>>1)*(v>>1)))
    return z
def bar(x): return [x[0],-x[1],-x[2],-x[3]]
def det(a):
    return sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*
               a[0][p[0]]*a[1][p[1]]*a[2][p[2]]*a[3][p[3]] for p in permutations(range(4)))
basis=[[F(1),0,0,0],[0,F(1),0,0],[F(1,2),0,F(1,2),0],[0,F(1,2),0,F(1,2)]]
mu=[0,0,F(2),F(1)]
mi=[-F(x)/6 for x in mu]
assert mul(mu,mu)==[-6,0,0,0]
current=[[2*mul(mul(mi,x),bar(y))[0] for y in basis] for x in basis]
published=[[2*mul(mul(bar(x),mu),y)[0] for y in basis] for x in basis]
assert current==[[0,0,-1,1],[0,0,1,-2],[1,-1,0,0],[-1,2,0,0]]
assert published==[[6*x for x in row] for row in current]
assert det(current)==1 and det(published)==1296
result={'status':'pass','arithmetic':'exact rational','basis':['1','i','(1+j)/2','(i+ij)/2'],'relations':['i^2=2','j^2=-3','ij=-ji'],'mu':'2j+ij','current_form':'Trd(mu^-1 x conjugate(y))','published_displayed_form':'Trd(conjugate(x) mu y)','current_matrix':[[int(x) for x in row] for row in current],'published_matrix':[[int(x) for x in row] for row in published],'current_determinant':int(det(current)),'published_determinant':int(det(published)),'published_to_current_scalar':6,'scope':'Checks displayed algebraic forms and matrix only; does not independently prove moduli theorem, positivity, or analytic identification.'}
Path(__file__).with_name('NORMALIZATION-CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
