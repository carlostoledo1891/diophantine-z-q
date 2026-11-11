"""Restricted obstruction: two explicit rational quadratic gates from one w."""
from fractions import Fraction as F
from pathlib import Path
import json
a=[F(1),F(-2,5)]
for j in range(2,10):a.append(a[-1]*F(4*j-5,4*j+1))
def solve(mat,b):
    rows=[list(row)+[x] for row,x in zip(mat,b)]
    for k in range(len(rows)):
        r=next(i for i in range(k,len(rows)) if rows[i][k]);rows[k],rows[r]=rows[r],rows[k]
        t=rows[k][k];rows[k]=[z/t for z in rows[k]]
        for i in range(len(rows)):
            if i!=k:
                t=rows[i][k];rows[i]=[x-t*y for x,y in zip(rows[i],rows[k])]
    return [r[-1] for r in rows]
out={}
for d in [2,3]:
    q=[F(1)]+solve([[a[n-j] for j in range(1,d+1)] for n in range(5,5+d)],[-a[n] for n in range(5,5+d)])
    defect={n:sum(q[j]*a[n-j] for j in range(d+1)) for n in range(5+d,10)}
    assert any(defect.values())
    out[f'numerator4_denominator{d}']={'normalizedDenominator':[str(x) for x in q],'remainingCoefficients':{str(n):str(v) for n,v in defect.items()}}
(Path(__file__).resolve().parent/'two-gate-obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
