"""Non-author binding and consumer checks for both identity-inclusive packets."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,contextlib,io
H=Path(__file__).resolve().parent
W=H.parent
P=W/'02-squares'/'point-charts'/'primary-reciprocal'
NOTE=W/'00-independent470'/'IDENTITY_EXTENSION.md'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
assert sha(NOTE)=='d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32'
assert sha(P/'candidate427-ir.json')=='6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4'
assert sha(P/'candidate428-ir.json')=='236e837094097aef4596a225f541347f314f7596511b75cbae09b722fa4a184d'
assert sha(P/'REPORT.md')=='47b935a66d73ee6e691b8010488ab41f517dd0d2d6028c703f5db060e9672918'
# Read and replay the inspected algebra checker; prevent its output write to
# the author's frozen directory. Imported verify494 only supplies functions.
code=(P/'verify_primary.py').read_text()
needle="(H/'verification428.json').write_text(json.dumps(result,indent=2)+'\\n');print(json.dumps(result,indent=2))"
assert code.count(needle)==1
code=code.replace(needle,'pass')
# This runtime has no sympy. Replay the complete physical/SOS section and
# use the independently inspected standard-library identity checker below.
marker='# Generic identities, independent of the actual coefficient expansion above.'
assert code.count(marker)==1
code=code.split(marker)[0]
ns={'__file__':str(P/'verify_primary.py'),'__name__':'identity_review_replay'}
exec(compile(code,str(P/'verify_primary.py'),'exec'),ns)
generic=W/'00-independent470'/'identity-extension-check.py'
assert sha(generic)=='b7eabee2c5b801baf6c14e9073f73a98ad48bf6f07b1d9f536b4ad231236de3d'
gcode=generic.read_text().split('home=Path(__file__).resolve().parent')[0]
exec(compile(gcode,str(generic),'exec'),{'__file__':str(generic),'__name__':'identity_generic_replay'})
ops=ns['P']
guarded=read(P/'candidate428-ir.json'); plain=read(P/'candidate427-ir.json')
gc={c['id']:c for c in guarded['coordinates']};pc={c['id']:c for c in plain['coordinates']}
gr={r['id']:r for r in guarded['residuals']};pr={r['id']:r for r in plain['residuals']}
assert set(gc)-set(pc)=={702} and set(gr)-set(pr)=={705}
assert all(gc[i]==c for i,c in pc.items())
assert all(gr[i]==r for i,r in pr.items())
assert all(guarded[k]==plain[k] for k in plain if k not in {'coordinates','residuals','status'})
# Independent guard subtraction and complete 427 SOS check.
total={}
for row in plain['residuals']:
    p=ops.normalized(ops.poly(row['terms']))
    total=ops.add(total,ops.mul(p,p))
assert total==ops.poly(read(P/'polynomial427.json')['terms'])
assert len(pc)==427 and len(pr)==396 and len(total)==6288
guard=ops.normalized(ops.poly(gr[705]['terms']))
assert ops.add(total,ops.mul(guard,guard))==ns['total']
# All height, scalar, correction and detector rows remain literally fixed.
old=read(W/'10-combination'/'combined435-ir.json')
newnames={r['name']:r for r in plain['residuals']}
protected=[]
for row in old['residuals']:
    if row['name'].startswith(('heightProduct.','scalar.','reduced_scalar.','detector','hybrid.','anchor.','correction.','inputSquare.')):
        assert newnames[row['name']]==row,row['name']
        protected.append(row['name'])
# At V_i=O, the actual alternate rows reduce to ell0*LP_i=0.
# This checks the real fused consumers, not stale standalone ell_i metadata.
cn={c['name']:c['id'] for c in plain['coordinates']}
sem=ns['sem']; mp=ns['mp']
def value(name):
    return {tuple(sorted(-1 if j==-1 else mp[j] for j in m)):q for m,q in ops.poly(sem['values'][name]['terms']).items()}
ell=[value('logV0.'+str(j)) for j in range(2)]
def fm(a,b):return [ops.add(ops.mul(a[0],b[0]),ops.mul(a[1],b[1]),2),ops.add(ops.mul(a[0],b[1]),ops.mul(a[1],b[0]))]
def canon(p):return {m:q/p[min(p)] for m,q in p.items()}
zero_consumers=[]
for i in range(1,5):
    z=[value(f'V{i}.z.{j}') for j in range(2)]
    zero={j:{} for comp in z for mon in comp for j in mon if j!=-1}
    lp=[value(f'LP{i}.{j}') for j in range(2)]
    product=fm(ell,lp)
    for j in range(2):
        name=f'logV{i}.{j}.definition'
        assert canon(ops.sub(ops.poly(newnames[name]['terms']),zero))==canon(product[j])
        zero_consumers.append(name)
# f(P) and x(P) are inverses over K and are units outside 2 and 41.
x=(F(57,8),F(-7,2));f=(F(456,1681),F(224,1681))
assert (x[0]*f[0]+2*x[1]*f[1],x[0]*f[1]+x[1]*f[0])==(1,0)
assert f[0]**2-2*f[1]**2==F(64,1681)
assert 10*(7+2093966)<F(50331647,2)
# For Hcal>=1, B>(40Hcal)^10 contradicts B²<7Hcal+6:
# 40^20*Hcal^20 >= 40^20*Hcal > 13Hcal >= 7Hcal+6.
assert 40**20>13
paths=[NOTE,P/'REPORT.md',P/'candidate427-ir.json',P/'candidate428-ir.json',P/'polynomial427.json',P/'polynomial428.json',P/'verify_primary.py',generic,W/'10-combination'/'combined435-ir.json']
out={'passed':True,'scope':'Frozen note and numerical bindings; replayed inspected algebra checker without writes; independent 427/428 delta, full427 SOS, unchanged protected rows, actual zero alternate consumers, exact f(P) and anchor contradiction constants.',
     'guarded':{'variables':428,'rows':397,'monomials':6290},'unguarded':{'variables':427,'rows':396,'monomials':6288},
     'protectedRows':len(protected),'zeroNumeratorConsumers':zero_consumers,
     'sourceSha256':{str(p):sha(p) for p in paths}}
(H/'review-identity-extension-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
