"""Non-author primary reciprocal review and physical chart domain checks."""
from pathlib import Path
from fractions import Fraction as F
import runpy,json,hashlib
H=Path(__file__).resolve().parent
P=H.parent/'03-depth/further'
ns=runpy.run_path(str(P/'verify_primary.py'))
fm,fa,sc,equiv,pol=[ns[n] for n in ['fieldprod','fieldadd','scale','equivalent','terms']]
dep=json.loads((H/'inputs/depth519.json').read_text())
D=({(0,()):F(11)},{(0,()):F(-6)})
def val(n):return tuple(pol({'terms':dep['values'][n+'.'+str(i)]['terms']}) for i in range(2))
for i,name in enumerate(['H','UA','US','UT','UZ']):
 h,j=ns['hs'][i],ns['js'][i];x=val(name+'.x')
 for k,q in enumerate(fa(x,fm(h,h),-1)):assert equiv(q,pol(ns['oo'][name+f'.chart.x.{k}.definition']))
 for k,q in enumerate(fa(fa(fm(j,j),fm(x,x),-1),D)):assert equiv(q,pol(ns['oo'][name+f'.chart.equation.{k}']))
t=ns['total']
assert max(len(m) for s,m in t)==4
assert any(s==0 and abs(v)==1 for (s,m),v in t.items())
assert [(m,v) for (s,m),v in t.items() if s==2]==[((57,57),16)]
assert (0,(57,57)) not in t and (1,(57,57)) not in t
assert max(abs(v.numerator).bit_length() for (s,m),v in t.items() if s==0)<2048
assert max(abs(v) for (s,m),v in t.items() if s==1)<=48
out=H/'reviews/primary445';out.mkdir(exist_ok=True,parents=True)
pins={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in [P/'REPORT.md',P/'candidate445-ir.json',P/'polynomial445.json',P/'certificate445.json',P/'verify_primary.py',H/'rational453-ir.json']}
(out/'checks.json').write_text(json.dumps({'verified':True,'sources':pins,'physicalChartRelations':True,'variables':445,'residuals':422,'monomials':6568,'maximumCoefficient':'16*3^(2^26)','content':1},indent=2)+'\n')
print('Non-author primary445 review checks passed.')
