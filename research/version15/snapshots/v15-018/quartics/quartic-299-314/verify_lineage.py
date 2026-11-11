"""Replay the packaged finite source chain without the original workspace."""
from pathlib import Path
import builtins,io,runpy,sys,os,json,hashlib,contextlib
H=Path(__file__).resolve().parent;S=H/'sources'
def read(p):return json.loads(p.read_bytes())
def check_package():
    pins=read(H/'PACKAGE-MANIFEST.json')
    actual={p.relative_to(H).as_posix() for p in H.rglob('*') if p.is_file() and p!=H/'PACKAGE-MANIFEST.json'}
    assert actual==set(pins),'Package file inventory differs'
    for name,item in pins.items():
        b=(H/name).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256'],name
check_package()
manifest=read(H/'SOURCE-MANIFEST.json');plan=read(H/'VERIFICATION-PLAN.json')
def check_manifest():
    actual={p.relative_to(S).as_posix() for p in S.rglob('*') if p.is_file()}
    assert actual==set(manifest),'Source manifest file set differs'
    for name,item in manifest.items():
        b=(S/name).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256'],name
check_manifest()
# Baseline is an exact independently accepted published artifact, not a new theorem.
baseline=S/'work/quartic-version6-release/repository/quartics/quartic-394-411/candidate394-ir.json'
legacy=S/'work/quartic-under400-20261107/10-combination/combined394-ir.json'
assert baseline.read_bytes()==legacy.read_bytes()
original=plan['originalRoot'].replace('\\','/').rstrip('/')
packagePrefix=H.as_posix().rstrip('/')+'/'
allowed=set(manifest)
for name in manifest:
    allowed.update(p.as_posix() for p in Path(name).parents)
real_open=builtins.open;real_io=io.open;real_stat=Path.stat
real_wt=Path.write_text;real_wb=Path.write_bytes
def remap(file):
    if not isinstance(file,(str,bytes,os.PathLike)):return file
    text=os.fsdecode(file).replace('\\','/')
    if text.casefold().startswith(packagePrefix.casefold()):return file
    if text.casefold().startswith(original.casefold()+'/'):
        rel=text[len(original)+1:];assert rel in allowed,'Unpackaged historical path: '+rel
        return S/rel
    return file
def readmode(args,kwargs):
    mode=args[0] if args else kwargs.get('mode','r')
    assert not any(c in mode for c in 'wax+'),'Replay attempted a direct file write'
def op(file,*args,**kwargs):
    readmode(args,kwargs);return real_open(remap(file),*args,**kwargs)
def iop(file,*args,**kwargs):
    readmode(args,kwargs);return real_io(remap(file),*args,**kwargs)
def st(self,*args,**kwargs):return real_stat(Path(remap(self)),*args,**kwargs)
def capture(self,data,*args,**kwargs):return len(data)
sys.dont_write_bytecode=True
oldpath=sys.path[:];oldcwd=Path.cwd();oldargv=sys.argv[:]
builtins.open=op;io.open=iop;Path.stat=st;Path.write_text=capture;Path.write_bytes=capture
try:
    for step in plan['steps']:
        script=S/step['script'];sys.argv=[str(script)]+step['args'];sys.path.insert(0,str(script.parent));os.chdir(script.parent)
        with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(script),run_name='__main__')
        sys.path[:]=oldpath
        print('PASS '+step['script'],flush=True)
finally:
    builtins.open=real_open;io.open=real_io;Path.stat=real_stat;Path.write_text=real_wt;Path.write_bytes=real_wb
    os.chdir(oldcwd);sys.path[:]=oldpath;sys.argv[:]=oldargv
# Public source-ID copies are precisely those consumed by the finite replay.
copies={'candidate299-ir.json':'work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json',
 'polynomial299.json':'work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/polynomial299.json',
 'candidate314-ir.json':'work/quartic-under300-20261107/10-combination/ordinary-reciprocal299/314/candidate-ir.json',
 'polynomial314.json':'work/quartic-under300-20261107/10-combination/ordinary-reciprocal299/314/polynomial.json',
 'quartic-314-source-id-coefficients.txt':'work/quartic-under300-20261107/10-combination/ordinary-reciprocal299/314/polynomial.txt'}
for public,source in copies.items():assert (H/public).read_bytes()==(S/source).read_bytes(),public
runpy.run_path(str(H/'verify_artifacts.py'),run_name='__main__')
check_manifest()
check_package()
print('PASS portable published394-to299 lineage and selected ordinary314; frozen sources unchanged')
