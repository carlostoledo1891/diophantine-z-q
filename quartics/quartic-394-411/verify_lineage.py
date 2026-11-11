"""Replay the complete packaged source chain without using the old workspace.

Absolute source paths frozen inside historical certificates are redirected only
under their exact original root. All redirected files must be in this package.
Verification report writes are captured rather than changing frozen artifacts.
"""
from pathlib import Path
import builtins,io,runpy,sys,json,hashlib,contextlib
H=Path(__file__).resolve().parent;ROOT=H/'sources'
plan=json.loads((H/'VERIFICATION-PLAN.json').read_text())
manifest=json.loads((H/'SOURCE-MANIFEST.json').read_text())
for name,item in manifest.items():
    p=ROOT/name
    assert p.stat().st_size==item['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],name
original=Path(plan['originalRoot'])
real_open=builtins.open;real_io_open=io.open;real_write=Path.write_text;real_writebytes=Path.write_bytes
def remap(file):
    if not isinstance(file,(str,bytes,Path)):return file
    p=Path(file)
    try:p.relative_to(H);return file
    except ValueError:pass
    try:rel=p.relative_to(original)
    except ValueError:return file
    target=ROOT/rel
    assert target.is_file(),f'Missing packaged historical input: {rel}'
    return target
def scoped_open(file,*a,**kw):return real_open(remap(file),*a,**kw)
def scoped_io_open(file,*a,**kw):return real_io_open(remap(file),*a,**kw)
def capture(self,data,*a,**kw):return len(data)
builtins.open=scoped_open;io.open=scoped_io_open;Path.write_text=capture;Path.write_bytes=capture;sys.dont_write_bytecode=True
try:
    for step in plan['steps']:
        script=ROOT/step['script'];sys.argv=[str(script)]+step['args']
        with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(script),run_name='__main__')
        print('PASS '+step['script']+' '+' '.join(step['args']),flush=True)
finally:
    builtins.open=real_open;io.open=real_io_open;Path.write_text=real_write;Path.write_bytes=real_writebytes
# Bind the public-facing copies to the exact copies used by the replay.
mirror=ROOT/'work/quartic-under400-20261107/10-combination/release394'
artifacts=json.loads((H/'ARTIFACTS.json').read_text())
for name,digest in artifacts['files'].items():
    assert hashlib.sha256((H/name).read_bytes()).hexdigest()==digest
    assert hashlib.sha256((mirror/name).read_bytes()).hexdigest()==digest
print('PASS all packaged source stages, final symbolic394 and ordinary411 tables')
