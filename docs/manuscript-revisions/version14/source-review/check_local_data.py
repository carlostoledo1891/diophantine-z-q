"""Check finite data actually consumed by the new source-level argument."""
from fractions import Fraction as F
from pathlib import Path
import json

numerator=list(map(F,['1','-9776/5365','2941/3219','-1024/13949','-1920/237133','-1024/711399','-1408/5928325','0','2432/103152855']))
denominator=list(map(F,['1','-1526/1073','513/1073']))
def roots(coeffs,p):
    cs=[(c.numerator*pow(c.denominator,-1,p))%p for c in coeffs]
    assert cs[-1]
    return [x for x in range(p) if sum(c*pow(x,i,p) for i,c in enumerate(cs))%p==0]
assert roots(numerator,71)==[] and roots(denominator,7)==[]
assert {x for x in range(71) if x*x%71==2}=={12,59}
assert {x for x in range(7) if x*x%7==2}=={3,4}
groups=[[(4,1),(4,2),(4,-1),(8,-4),(16,-8)],[(4,1),(4,2),(8,3),(8,-4),(8,-1),(16,-8)],[(4,1),(4,2),(8,3),(16,-8),(16,-4),(16,-1)]]
for alpha in range(1,16,2):
    for group in groups:
        used={0}
        for period,shift in group:
            cls={(period*n+shift*alpha)%16 for n in range(16)}
            assert not used.intersection(cls)
            used.update(cls)
assert F(5,24)*F('25165823.5')>2093966+7
assert 3+3+27==33 and 33%8==1
report={'status':'PASS finite local source data only',
        'N_mod71_roots':[],'Q_mod7_roots':[],
        'split_roots':{'71':[12,59],'7':[3,4]},
        'all_three_group_classes_disjoint_for_all_odd_classes_mod16':True,
        'scalar_height_margin':str(F(5,24)*F('25165823.5')-(2093966+7)),
        'proof_limit':'Residue enumeration supports the explicit unbounded valuation arguments; it does not prove those arguments or the arithmetic theorem.'}
(Path(__file__).parent/'LOCAL-DATA-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
