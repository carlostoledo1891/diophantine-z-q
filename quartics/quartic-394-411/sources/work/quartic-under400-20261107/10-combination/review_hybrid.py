"""Non-author replay with all producer-file writes suppressed."""
from pathlib import Path
import runpy,json,hashlib
H=Path(__file__).resolve().parent
P=H.parent/'01-elimination'
dest=H/'reviews/hybrid'
dest.mkdir(parents=True,exist_ok=True)
original=Path.write_text
writes={}
def capture(self,data,*args,**kwargs):
 writes[str(self.resolve())]=data
 return len(data)
Path.write_text=capture
try:
 first=runpy.run_path(str(P/'adapt486/check_hybrid_semantics.py'))
 second=runpy.run_path(str(P/'post478/verify_result.py'))
finally:
 Path.write_text=original
for path,data in writes.items():
 p=Path(path)
 if p.name not in {'HYBRID-VERIFICATION.json','VERIFIED476.json'}:
  assert json.loads(data)==json.loads(p.read_text()),p
for tag,result in [('hybrid',first['report']),('elimination',second['summary'])]:
 (dest/(tag+'-replay.json')).write_text(json.dumps(result,indent=2)+'\n')
# The deletion replay must actually end at the published candidate bytes.
assert json.loads((P/'post478/candidate476-ir.json').read_text())==second['out']
assert hashlib.sha256((P/'post478/candidate476-ir.json').read_bytes()).hexdigest()=='a519286d9241db26cbb6dee196a5cd5825f992d5b3fc439013e3a702f93a738c'
assert hashlib.sha256((P/'adapt486/candidate478-ir.json').read_bytes()).hexdigest()=='74758dee6369b80daa2e902228f7d2bf7c76fdc3fcbb461c5e92bd7666f28695'
manifest={}
for folder,names in [('adapt486',['baseline486.json','candidate478-ir.json','polynomial478.json','check_hybrid_semantics.py','hybrid-certificate.json','REPORT.md']),('post478',['candidate476-ir.json','polynomial476.json','elimination476-certificate.json','verify_result.py'])]:
 for name in names:
  p=P/folder/name;manifest[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
(dest/'source-hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Independent hybrid and elimination replay passed; no source files written.')
