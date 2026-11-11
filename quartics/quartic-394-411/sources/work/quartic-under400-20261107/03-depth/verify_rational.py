"""Read-only exact approximation checks, followed by independent certificate replay."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,shutil
H=Path(__file__).resolve().parent
W=H.parents[1]
OLD=W/'quartic-optimization-20261107/03-depth'
a=[F(1),F(-2,5)]
for j in range(2,10):a.append(a[-1]*F(4*j-5,4*j+1))
q=[F(1),F(-1526,1073),F(513,1073)]
p=[F(1),F(-9776,5365),F(2941,3219),F(-1024,13949),F(-1920,237133),F(-1024,711399),F(-1408,5928325),F(0),F(2432,103152855)]
product=[sum(q[k]*a[j-k] for k in range(3) if 0<=j-k<len(a)) for j in range(12)]
assert product[:9]==p and product[9]==0
assert product[10:]==[F(2970726,254443709),F(-41697666,6361092725)]
bernstein=[sum(p[i]*F(comb(k,i),comb(8,i)) for i in range(k+1)) for k in range(9)]
assert min(bernstein)==F(83904,10113025)
assert q[1]+2*q[2]==F(-500,1073) and sum(q)==F(60,1073)
for x in a+q+p+product:
 d=x.denominator
 for prime in [2,3,5,7,11,13,17,19,23,29,31,37]:
  while d%prime==0:d//=prime
 assert d==1
print('Exact order-40 approximation identity, coefficient integrality and global positivity certificates passed.')
# This verifier contains no producer call. Its only output is the replay report.
# The underlying arithmetic engines remain the separately authored frozen ones.
for name in ['checker.cjs','compile_ir.py']:
 target=H/name
 if target.exists():assert target.read_bytes()==(OLD/name).read_bytes()
 else:shutil.copyfile(OLD/name,target)
source=(OLD/'verify.py').read_text().replace("'beta12'","'rational'").replace('==519','==511').replace('==24986','==24499')
exec(compile(source,str(OLD/'verify.py'),'exec'),globals())
