from pathlib import Path
import json,hashlib
ROOT=Path.cwd();H=ROOT/'work/quartic-v14-prep/quartic-299-314';O=ROOT/'work/quartic-v14-release-review-sol/package';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_bytes())
assert sha(H/'PACKAGE-MANIFEST.json')=='5369f80f69742958ea31f3a32b62b43e6b23b284063e6870af2dc2f0073977fb'
pins=load(H/'PACKAGE-MANIFEST.json');actual={p.relative_to(H).as_posix() for p in H.rglob('*') if p.is_file() and p.name!='PACKAGE-MANIFEST.json'};assert actual==set(pins)
for n,x in pins.items():assert sha(H/n)==x['sha256'] and (H/n).stat().st_size==x['bytes'],n
source=load(H/'SOURCE-MANIFEST.json');matched=0
for n,x in source.items():
 p=H/'sources'/n;assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if (ROOT/n).exists():assert p.read_bytes()==(ROOT/n).read_bytes();matched+=1
accept=load(H/'ACCEPTANCE.json')
for n,x in accept['reviews'].items():assert sha(H/'reviews'/n)==x['sha256'] and (H/'reviews'/n).read_bytes()==(ROOT/x['originalPath']).read_bytes()
result={'package_files':len(pins),'source_files':len(source),'original_source_files_matched':matched,'review_copies_matched':len(accept['reviews']),'passed':True};(O/'BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
