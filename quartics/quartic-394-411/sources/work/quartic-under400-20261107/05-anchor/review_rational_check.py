"""Rerun producer-free checker read-only, then check physical output consumers."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,sys
HERE=Path(__file__).resolve().parent
OTHER=HERE.parent/'10-combination'
checker=OTHER/'verify_rational_component.py'
text=checker.read_text()
write="(H/(prefix+'-verification.json')).write_text(json.dumps(result,indent=2)+'\\n');"
assert text.count(write)==1
text=text.replace(write,'')
ns={'__file__':str(checker)}
oldargv=sys.argv[:];sys.argv=[str(checker)]
try:exec(compile(text,str(checker),'exec'),ns)
finally:sys.argv=oldargv
times,plus,minus,norm,val,p=map(ns.get,['times','plus','minus','norm','val','p'])
old,new,source,out,nc=map(ns.get,['old','new','source','out','nc'])
deleted=ns['deleted'];var=ns['var'];D=ns['fc'](11,-6)
checked=[]
def same_zero_polynomial(a,b):
    if set(a)!=set(b):return False
    key=min(a);ratio=a[key]/b[key]
    return a=={m:ratio*c for m,c in b.items()}
for i in [0,2,3,4]:
    pre=f'logV{i}';f=val(f'V{i}.f');fsq=val(pre+'.fSquare')
    for j,poly in enumerate(minus(times(f,f),fsq)):
        assert norm(poly)==norm(old[f'{pre}.fSquare.{j}.definition'])
    assert val(pre+'.w')==times(D,fsq)
    R=tuple(var(nc[f'{pre}.rationalApproximation.{j}']) for j in range(2))
    ell=val(pre)
    if i==0:
        physical=plus(times(val('V0.y'),ell),times(val('V0.x'),R))
        rownames=[f'{pre}.definition.{j}' for j in range(2)]
    else:
        # The final compiler eliminated the standalone ell_i output. Its
        # actual consumer is the raw, unconjugated alternate quotient LP_i.
        physical=minus(times(val('logV0'),val(f'LP{i}')),times(val(f'V{i}.z'),R))
        rownames=[f'{pre}.{j}.definition' for j in range(2)]
    for j,row in enumerate(rownames):assert same_zero_polynomial(physical[j],new[row]),row
    # Reused old cubes and deleted middle values must have no surviving
    # incidence once the physical G output is recentered to R.
    ids={c['id'] for c in source['coordinates'] if c['name'].startswith((pre+'.wPower3.',pre+'.middle.'))}
    for name,row in new.items():
        if name in old and name not in deleted:assert not any(set(mon)&ids for mon in row),name
    checked.extend(rownames)

expected_bern=[F(1),F(4143,5365),F(260069,450660),F(27829,67340),F(4636683,16599310),F(82391,474266),F(2245591,23713300),F(955437,23713300),F(83904,10113025)]
assert ns['bern']==expected_bern
summary={'physicalLogOutputRowsChecked':checked,'wEqualsDfsquared':True,
         'noUnmappedCubeOrMiddleConsumers':True,'allBernsteinCoefficientsMatched':True,
         'finiteCheck':ns['result'],
         'bindings':{str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in [checker,OTHER/'rational490-ir.json',HERE.parent/'03-depth/REPORT.md']}}
(HERE/'review-rational-checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='finiteCheck'},indent=2))
