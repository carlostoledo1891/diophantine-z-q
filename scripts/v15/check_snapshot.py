"""Read-only byte/inventory check; no mathematical or publication approval."""
import argparse, hashlib, json
from pathlib import Path, PurePosixPath

def digest(data): return hashlib.sha256(data).hexdigest()
def safe(root, name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name or str(p)!=name:
        raise ValueError('unsafe path: '+name)
    cur=root
    for part in p.parts:
        cur=cur/part
        if cur.is_symlink(): raise ValueError('symlink: '+name)
    return cur

def check(root, expected):
    root=Path(root).resolve()
    selector=json.loads((root/'CURRENT-MANIFEST.json').read_bytes())
    mp=safe(root,selector['path']); data=mp.read_bytes()
    if digest(data)!=expected or selector['sha256']!=expected: raise ValueError('manifest identity')
    manifest=json.loads(data); seen=set()
    for item in manifest['files']:
        name=item['path']
        if name in seen: raise ValueError('duplicate member')
        seen.add(name); raw=safe(root,name).read_bytes()
        if len(raw)!=item['bytes'] or digest(raw)!=item['sha256']: raise ValueError('member mismatch: '+name)
    exclusions={selector['path'],'CURRENT-MANIFEST.json'}
    if set(selector['exclusions']) != exclusions|{'.git/'}: raise ValueError('unexpected exclusions')
    actual=set()
    def walk(d,prefix=''):
        for f in d.iterdir():
            name=prefix+f.name
            if name=='.git': continue
            if f.is_symlink(): raise ValueError('symlink: '+name)
            if f.is_dir(): walk(f,name+'/')
            else: actual.add(name)
    walk(root)
    if actual-exclusions!=seen: raise ValueError('inventory mismatch')
    origins=json.loads((root/'COPY-ORIGINS.json').read_bytes())
    origin_paths=set()
    for item in origins:
        name=item['path']
        if name in origin_paths or name not in seen: raise ValueError('origin destination')
        origin_paths.add(name);raw=safe(root,name).read_bytes()
        if digest(raw)!=item['sha256'] or len(raw)!=item['bytes']: raise ValueError('origin mismatch')
    return {'manifest_sha256':expected,'members':len(seen),'copy_origins':len(origins),'scope':'bytes and inventory only'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repository',required=True);ap.add_argument('--manifest-sha256',required=True)
    a=ap.parse_args();print(json.dumps(check(a.repository,a.manifest_sha256),indent=2))
