"""Collect exact source closure by read-only finite replay and explicit review pins."""
from pathlib import Path
import sys,os,json,hashlib,runpy,io,contextlib,shutil
H=Path(__file__).resolve().parent;ROOT=H.parents[1];O=H/'quartic-299-314';S=O/'sources'
U='work/quartic-under300-20261107/';OPT='work/quartic-optimization-20261107/';C=U+'10-combination/'
steps=[U+'03-depth/verify392t.py',U+'01-elimination/squared-h/verify.py',C+'unweighted372/verify.py',C+'verify369.py',U+'01-elimination/s-odd366/verify.py',
 OPT+'resume-depth-20261107/strong-h330/verify330.py',OPT+'resume-depth-20261107/chain327/verify327.py',OPT+'resume-depth-20261107/three326/verify326.py',
 OPT+'resume-depth-20261107/chain323/verify323.py',OPT+'resume-elimination-20261107/abscissa359/verify.py',C+'three-anchor319/verify.py',
 OPT+'resume-elimination-20261107/exact319/verify.py',C+'combined318/verify.py',C+'combined315/verify.py',
 OPT+'resume-elimination-20261107/shared-scale314/verify.py',C+'sparse-shared314/verify.py',OPT+'resume-anchor-shared314-20261107/anchor-gamma313/verify.py',
 OPT+'reciprocal307-20261107/verify.py',OPT+'resume-elimination-20261107/reciprocal301/verify.py',OPT+'resume-elimination-20261107/reciprocal299-r2/verify.py',
 C+'ordinary-reciprocal299/check_source.py',C+'ordinary-reciprocal299/verify.py',C+'review-reciprocal301/check_identities.py',C+'review-reciprocal301/check_finite.py',
 C+'review-reciprocal299/check.py',OPT+'resume-depth-20261107/review-ordinary299/check.py']
seen=set();capturing=False
def audit(event,args):
    if event!='open' or not capturing or not isinstance(args[0],(str,bytes,os.PathLike)):return
    p=Path(os.fsdecode(args[0])).resolve()
    try:p.relative_to(ROOT)
    except ValueError:return
    if p.is_file() and '__pycache__' not in p.parts:seen.add(p)
sys.addaudithook(audit);sys.dont_write_bytecode=True
real_wt=Path.write_text;real_wb=Path.write_bytes
def discard(self,data,*a,**kw):return len(data)
Path.write_text=discard;Path.write_bytes=discard
oldcwd=Path.cwd();oldargv=sys.argv[:];oldpath=sys.path[:]
try:
    for name in steps:
        script=ROOT/name;assert script.is_file(),script
        seen.add(script);sys.argv=[str(script)];sys.path.insert(0,str(script.parent));os.chdir(script.parent)
        capturing=True
        with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(script),run_name='__main__')
        capturing=False;sys.path[:]=oldpath
        print('PASS '+name,flush=True)
finally:
    capturing=False;Path.write_text=real_wt;Path.write_bytes=real_wb;os.chdir(oldcwd);sys.argv[:]=oldargv;sys.path[:]=oldpath
# The accepted source/argument archive is explicit, not inferred from checker imports.
inv=ROOT/(OPT+'resume-release-inventory-20261107-r6')
inventory=json.loads((inv/'SOURCE-PINS.json').read_bytes())
for name,pin in inventory.items():
    p=ROOT/name;raw=p.read_bytes()
    assert len(raw)==pin['bytes'] and hashlib.sha256(raw).hexdigest()==pin['sha256'],name
    seen.add(p)
seen.update(p for p in inv.iterdir() if p.is_file())
# Preserve producers, frozen reports, manifests, certificates and full candidate tables
# beside every actually executed source checker. Mutable status/search logs are excluded.
for name in steps:
    for p in (ROOT/name).parent.iterdir():
        if p.is_file() and p.suffix in {'.py','.md','.json','.txt'} and not any(x in p.name.lower() for x in ['status','search-notes','local-scan']):seen.add(p)
# Preserve the explicitly rejected cache draft as history, never as a replay target.
rejected=ROOT/(OPT+'resume-elimination-20261107/reciprocal299')
seen.update(p for p in rejected.iterdir() if p.is_file() and p.suffix in {'.py','.md','.json'})
# Baseline acceptance and exact public artifacts; the new replay starts from this baseline.
baseline=ROOT/'work/quartic-version6-release/repository/quartics/quartic-394-411'
for name in ['candidate394-ir.json','polynomial394.json','ARTIFACTS.json','ACCEPTANCE.json']:
    seen.add(baseline/name)
seen.update(p for p in (baseline/'reviews').rglob('*') if p.is_file())
seen.add(H/'package_v14.py')
manifest={}
for p in sorted(seen):
    rel=p.relative_to(ROOT);dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    raw=p.read_bytes()
    if dest.exists():assert dest.read_bytes()==raw,dest
    else:dest.write_bytes(raw)
    manifest[rel.as_posix()]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
(O/'SOURCE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
plan={'originalRoot':str(ROOT),'baseline':'published394; inherited mathematics remains separately reviewed',
      'steps':[{'script':n,'args':[]} for n in steps],
      'rejectedNotExecuted':[p.relative_to(ROOT).as_posix() for p in rejected.iterdir() if p.is_file() and p.name.startswith('candidate')]}
(O/'VERIFICATION-PLAN.json').write_text(json.dumps(plan,indent=2)+'\n',encoding='utf-8')
(H/'COLLECTION.json').write_text(json.dumps({'files':len(manifest),'bytes':sum(p['bytes'] for p in manifest.values()),'steps':len(steps),'inventorySources':len(inventory)},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(manifest),'bytes':sum(p['bytes'] for p in manifest.values()),'steps':len(steps)}))
