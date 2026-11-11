from fractions import Fraction as F
from pathlib import Path
import json
D=Path(__file__).parent
rows=[]
for a in [4,5,10,100,1000]:
 t=F(a);b=F(1,a-2)
 assert t*t-a*(a-2)*t*b+(a-2)**2*b*b-1==0
 assert b.denominator>1
 rows.append({'a':a,'t':str(t),'b':str(b),'B':a})
D.joinpath('CHECKS.json').write_text(json.dumps({'ok':True,'counterexamples':rows,'general_proof':'See PROPOSAL.md; finite examples are corroboration only.'},indent=2)+'\n')
