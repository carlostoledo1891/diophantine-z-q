import json,hashlib
from pathlib import Path
from fractions import Fraction as F
O=Path(__file__).resolve().parent;P=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/joint-root-factor-110')
assert hashlib.sha256((P/'MANIFEST.json').read_bytes()).hexdigest()=='f673e732217d82bca9c6d10a4a6114155b7af75c3be92790daabc7b876eeab4f'
m=json.loads((P/'MANIFEST.json').read_bytes())
for item in m['members']:
 b=(P/item['path']).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
par=json.loads(Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-redundancy224-006/candidate224-ir.json').read_bytes());new=json.loads((P/'candidate223-ir.json').read_bytes());maps=json.loads((P/'MAPS.json').read_bytes())
cm={int(k):v for k,v in maps['old_to_new'].items()};inv={v:k for k,v in cm.items()}
assert len(cm)==len(inv)==223 and maps['deleted']==[62,63,66,67,68,69]
assert set(maps['scaled'])==set(range(167,181))|set(range(195,209))|set(range(209,223))
assert set(maps['first_R_scaled'])==set(range(167,179))|set(range(195,203))|set(range(209,217))
assert set(maps['ratio_R_scaled'])==set(range(47,55))|set(range(56,60))
assert new['inputCoordinate']==par['inputCoordinate']==1 and new['fixedParameter']==par['fixedParameter']
assert len(new['coordinates'])==223 and len(new['residuals'])==197
assert maps['removed_rows']==[124,125,160,161,178,179]
byold={r['parentRowId']:r for r in new['residuals']if 'parentRowId'in r}
def poly(row,back=False):return {(t['parameterPower'],tuple(inv[i]for i in t['monomial'])if back else tuple(t['monomial'])):F(t['coefficient'])for t in row['terms']}
for rid in [9,43,44,45,46,56,57,68,71,73]:
 old=poly(par['residuals'][rid-1]);cur=poly(byold[rid],True);assert set(old)==set(cur)
 ratio=next(iter(cur.values()))/old[next(iter(cur))];assert ratio and all(cur[k]==ratio*v for k,v in old.items())
 assert not any(set(t['monomial'])&set(maps['scaled']+maps['ratio_R_scaled']+maps['deleted'])for t in par['residuals'][rid-1]['terms'])
helpers=[r for r in new['residuals']if 'parentRowId'not in r];assert len(helpers)==5
for r,oldid in zip(helpers,range(225,230)):
 pp=poly(r,True);key=(0,(oldid,));assert key in pp and pp[key]!=0
 assert all(not set(mon)&set(range(225,230))for a,mon in pp if(a,mon)!=key)
res={'all_frozen_pins':True,'coordinate_budget':[224,-6,5,223],'residual_budget':[198,-6,5,197],'guard_rows_unchanged_and_unscaled':True,'five_acyclic_unique_helpers':True,'input_parameter_preserved':True,'scope':'Budget, mapping domains and required-row invariance only; full Laurent and SOS replay assigned independent integration reviewer.'}
(O/'CHECKS.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
