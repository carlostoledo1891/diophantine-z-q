"""Replay author structural negative fixtures without writing into frozen R6."""
from pathlib import Path
import hashlib,json,sys
HERE=Path(__file__).resolve().parent
FOLDER=HERE.with_name('resume-release-inventory-20261107-r6')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(FOLDER/'FROZEN-MANIFEST.json')=='207e7ca6cca93a79fabc19db02ee5c8d2a3d9370d0ec7f19d2847d3bb6e02ae7'
manifest=json.loads((FOLDER/'FROZEN-MANIFEST.json').read_bytes())
for name,rec in manifest.items():assert sha(FOLDER/name)==rec['sha256']
snapshot={p.name:sha(p) for p in FOLDER.iterdir() if p.is_file()}
sys.dont_write_bytecode=True
sys.path.insert(0,str(FOLDER))
original_write=Path.write_text
def redirected(self,data,*args,**kwargs):
 assert self.resolve()==(FOLDER/'CHECKS.json').resolve(),'Unexpected author write'
 return original_write(HERE/'AUTHOR-REPLAY.json',data,*args,**kwargs)
Path.write_text=redirected
try:
 source=FOLDER/'check_revision.py'
 exec(compile(source.read_text(),str(source),'exec'),{'__file__':str(source),'__name__':'__main__'})
finally:Path.write_text=original_write
assert sha(HERE/'AUTHOR-REPLAY.json')==sha(FOLDER/'CHECKS.json')
result=json.loads((HERE/'AUTHOR-REPLAY.json').read_bytes())
assert len(result['negativeFixturesRejected'])==31
assert len(set(result['negativeFixturesRejected']))==31
assert {p.name:sha(p) for p in FOLDER.iterdir() if p.is_file()}==snapshot
(HERE/'AUTHOR-REPLAY-CHECK.json').write_text(json.dumps({'status':'PASS','negative_controls_replayed':31,'frozen_result_reproduced_exactly':True,'frozen_files_unchanged':True},indent=2)+'\n')
