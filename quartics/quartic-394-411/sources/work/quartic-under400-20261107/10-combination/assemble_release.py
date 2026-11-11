"""Collect exactly the source files read by the complete verification chain."""
from pathlib import Path
import builtins,io,runpy,sys,json,hashlib,contextlib,shutil
H=Path(__file__).resolve().parent;ROOT=H.parents[2];O=H/'release394'
P='work/quartic-under400-20261107/'
plan=[]
def own(name,*args):plan.append({'script':P+'10-combination/'+name,'args':list(args)})
own('verify_order10.py');own('verify_combination.py','486')
plan += [{'script':P+'01-elimination/triple-cubic/check_hybrid_semantics.py','args':[]},{'script':P+'01-elimination/triple-cubic/elimination/verify_result.py','args':[]}]
own('verify_v0.py');own('verify_tangent_subset.py');own('verify_combination.py','461')
own('verify_rational_component.py','453');own('verify453_interfaces.py')
plan.append({'script':P+'03-depth/further/verify_primary.py','args':[]})
own('verify_scalar443.py')
for count in [439,435,433,431,423,417,401,399,396,395]:own('verify_combination.py',str(count))
own('verify417_interfaces.py');own('verify399_interfaces.py');own('verify395_interfaces.py')
own('verify_anchor_combination.py','394');own('verify394_interfaces.py');own('verify_release394.py','394')
seen=set();real_open=builtins.open;real_io_open=io.open;real_write=Path.write_text;real_writebytes=Path.write_bytes
def note(file):
    if isinstance(file,(str,bytes,Path)):
        try:
            p=Path(file).resolve();p.relative_to(ROOT)
            if p.is_file():seen.add(p)
        except (ValueError,OSError):pass
def logged_open(file,*args,**kw):note(file);return real_open(file,*args,**kw)
def logged_io_open(file,*args,**kw):note(file);return real_io_open(file,*args,**kw)
def discard(self,data,*args,**kw):return len(data)
builtins.open=logged_open;io.open=logged_io_open;Path.write_text=discard;Path.write_bytes=discard
try:
    for step in plan:
        path=ROOT/step['script'];seen.add(path);sys.argv=[str(path)]+step['args']
        with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(path),run_name='__main__')
        print('Verified '+step['script'].split('/')[-1]+' '+' '.join(step['args']),flush=True)
finally:
    builtins.open=real_open;io.open=real_io_open;Path.write_text=real_write;Path.write_bytes=real_writebytes
# Add complete frozen reports, bindings, producers and local mathematical checks.
for folder in [H,H/'inputs']:
    for p in folder.iterdir():
        if p.is_file() and (p.suffix in {'.py','.md'} or p.name.endswith('-certificate.json')):seen.add(p)
for rel in ['03-depth/integrated394','03-depth/integrated395','02-squares/point-charts/biquadratic','02-squares/beyond399','05-anchor']:
    folder=ROOT/P/rel
    for p in folder.iterdir():
        if p.is_file() and p.suffix in {'.md','.py'}:seen.add(p)
manifest={}
for p in sorted(seen):
    rel=p.relative_to(ROOT);target=O/'sources'/rel;target.parent.mkdir(parents=True,exist_ok=True)
    if target.resolve()!=p.resolve():shutil.copyfile(p,target)
    manifest[rel.as_posix()]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
(O/'VERIFICATION-PLAN.json').write_text(json.dumps({'originalRoot':str(ROOT),'steps':plan},indent=2)+'\n')
(O/'SOURCE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'files':len(manifest),'bytes':sum(v['bytes'] for v in manifest.values()),'verificationSteps':len(plan)},indent=2))
