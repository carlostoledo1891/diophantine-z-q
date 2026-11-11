"""Exact quadratic-elimination search. Run with Python's standard library."""
import importlib.util, json, sys
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

OUT=Path(__file__).resolve().parent
BASE=OUT
spec=importlib.util.spec_from_file_location('compiler',BASE/'compile_ir.py')
C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
data=json.loads((BASE/'baseline486.json').read_text())
c=C.Compiler(data)

def main():
    basis={}; dependencies=[]
    for rid,p in c.rows.items():
        q={k:v for k,v in p.items() if len(k[1])==2}
        combo={rid:F(1)}
        while q:
            k=min(q)
            if k not in basis:
                f=q[k]; basis[k]=({a:b/f for a,b in q.items()},{a:b/f for a,b in combo.items()});break
            b,bc=basis[k];f=q[k]
            for target,other in [(q,b),(combo,bc)]:
                for a,v in other.items():
                    target[a]=target.get(a,F(0))-f*v
                    if not target[a]:del target[a]
        if not q:dependencies.append(combo)
    candidates=[(v,r) for v in c.coordinates for r in c.incidence[v] if c.elimination(v,r)]
    result={'coordinates':len(c.coordinates),'rows':len(c.rows),'blocks':dict(Counter(x['block'] for x in c.coordinates.values())),
      'quadratic_part_rank_over_Q':len(basis),'constant_linear_combination_dependencies':[{str(k):str(v) for k,v in p.items()} for p in dependencies],
      'direct_degree_preserving_pivots':candidates}
    (OUT/'initial-census.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()


