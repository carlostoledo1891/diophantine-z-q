"""Verify and restore the layered Version14 supplement safely."""
from pathlib import Path, PurePosixPath
import hashlib, io, json, stat, sys, zipfile

ROOT = Path(__file__).resolve().parent
def digest(raw): return hashlib.sha256(raw).hexdigest()
def safe(name):
    p=PurePosixPath(name)
    if (not name or p.is_absolute() or ':' in name or '\\' in name or '\x00' in name
            or any(x in ('','.','..') for x in name.split('/'))):
        raise ValueError('Unsafe member path: '+repr(name))
    reserved={'con','prn','aux','nul'}|{'com'+str(i) for i in range(1,10)}|{'lpt'+str(i) for i in range(1,10)}
    if any(x.endswith((' ','.')) or x.split('.')[0].lower() in reserved for x in p.parts):
        raise ValueError('Ambiguous Windows member path')
    return p
def checked_zip(raw):
    z=zipfile.ZipFile(io.BytesIO(raw));seen=set()
    for i in z.infolist():
        safe(i.filename)
        if i.filename.casefold() in seen: raise ValueError('Duplicate/case-colliding ZIP member')
        seen.add(i.filename.casefold())
        if i.is_dir() or stat.S_ISLNK(i.external_attr >> 16): raise ValueError('Nonregular ZIP member')
    m=json.loads(z.read('MANIFEST.json'))
    if set(z.namelist()) != set(m['files'])|{'MANIFEST.json'}:
        raise ValueError('Unmanifested or missing member')
    for name,h in m['files'].items():
        safe(name)
        if digest(z.read(name))!=h: raise ValueError('Layer hash mismatch: '+name)
    return z,m
def main():
    if len(sys.argv)!=2: raise SystemExit('Usage: python -B restore.py NEW_DIRECTORY')
    dest=Path(sys.argv[1]).resolve()
    if dest.exists(): raise SystemExit('Choose a new output directory; existing paths are never merged')
    m=json.loads((ROOT/'MANIFEST.json').read_bytes())
    for name,h in m['files'].items():
        safe(name);p=ROOT/name
        if p.resolve()!=p or not p.is_file():
            raise ValueError('Unsafe or missing extracted input: '+name)
        if digest(p.read_bytes())!=h: raise ValueError('Supplement hash mismatch: '+name)
    names={}
    def save(name,raw):
        safe(name);old=names.get(name.casefold())
        if old is not None and old!=name: raise ValueError('Cross-layer case collision')
        names[name.casefold()]=name;p=(dest/name).resolve()
        if not p.is_relative_to(dest): raise ValueError('Restore target escaped')
        p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    def layer(raw,depth=0):
        if depth>16: raise ValueError('Historical layer depth limit exceeded')
        z,lm=checked_zip(raw)
        with z:
            for name in sorted(lm['files']):
                if name.endswith('-base.zip'): layer(z.read(name),depth+1)
            has_current=any(n.startswith('current/') for n in lm['files'])
            for name in sorted(lm['files']):
                if name.endswith('-base.zip') or name in ('restore.py','README.txt'): continue
                if has_current and not name.startswith('current/'): continue
                save(name[8:] if name.startswith('current/') else name,z.read(name))
    historical=(ROOT/'version13-base.zip').read_bytes()
    layer(historical)
    save('research/version13/z-in-q-version13-supplement.zip',historical)
    for name in sorted(m['files']):
        if name.startswith('current/'): save(name[8:],(ROOT/name).read_bytes())
    print('Restored Version14 with verified historical bases; research notes stay beside this script.')
if __name__=='__main__': main()
