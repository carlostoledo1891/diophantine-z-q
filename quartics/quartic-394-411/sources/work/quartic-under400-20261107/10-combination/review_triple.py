"""Non-author replay with all producer-file writes suppressed."""
from pathlib import Path
import runpy,json,hashlib
H=Path(__file__).resolve().parent
P=H.parent/'01-elimination'
dest=H/'reviews/triple'
dest.mkdir(parents=True,exist_ok=True)
original=Path.write_text
writes={}
def capture(self,data,*args,**kwargs):
 writes[str(self.resolve())]=data
 return len(data)
Path.write_text=capture
try:
 first=runpy.run_path(str(P/'triple-cubic/check_hybrid_semantics.py'))
 second=runpy.run_path(str(P/'triple-cubic/elimination/verify_result.py'))
finally:
 Path.write_text=original
for path,data in writes.items():
 p=Path(path)
 if p.name not in {'HYBRID-VERIFICATION.json','VERIFIED470.json'}:
  assert json.loads(data)==json.loads(p.read_text()),p
for tag,result in [('hybrid',first['report']),('elimination',second['summary'])]:
 (dest/(tag+'-replay.json')).write_text(json.dumps(result,indent=2)+'\n')
# The deletion replay must actually end at the published candidate bytes.
assert json.loads((P/'triple-cubic/elimination/candidate470-ir.json').read_text())==second['out']
assert hashlib.sha256((P/'triple-cubic/elimination/candidate470-ir.json').read_bytes()).hexdigest()=='eff9369864da6bd2ed46fa300f51f5a0cc9217d3b790380713644ee31f512b72'
assert hashlib.sha256((P/'triple-cubic/candidate479-ir.json').read_bytes()).hexdigest()=='e8aea4b56037c0be0a8e9906e377bceea8c7bebd8fc3bf3314366032cfeae1f7'
manifest={}
for folder,names in [('triple-cubic',['baseline486.json','candidate479-ir.json','polynomial479.json','check_hybrid_semantics.py','hybrid-certificate.json','REPORT.md']),('triple-cubic/elimination',['candidate470-ir.json','polynomial470.json','elimination470-certificate.json','verify_result.py'])]:
 for name in names:
  p=P/folder/name;manifest[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
(dest/'source-hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Independent hybrid and elimination replay passed; no source files written.')
