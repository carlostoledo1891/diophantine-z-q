from pathlib import Path
from datetime import date
import hashlib,json,sys,time
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];TOOLS=ROOT/'work/quartic-v14-release-r5';OLD=OUT.parent/'handoff-annex-author'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,o):(OUT/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
pins=json.loads((OUT/'INPUT-PINS.json').read_bytes())
assert sha(TOOLS/'MANIFEST.json')==pins['r5_manifest_sha256']
tm=json.loads((TOOLS/'MANIFEST.json').read_bytes())
for name in ['research_annex.py','release_common.py']:assert sha(TOOLS/name)==tm['files'][name]['sha256']
assert sha(OUT/'SELECTION.json')==pins['selection_sha256']
assert sha(OUT/'CONTENT-SOURCES.json')==pins['content_sources_sha256']
old=json.loads((OLD/'SELECTION.json').read_bytes());new=json.loads((OUT/'SELECTION.json').read_bytes())
before={r['path']:r for r in old['files']};after={r['path']:r for r in new['files']}
assert set(after)<set(before) and all(before[k]==v for k,v in after.items())
assert new['unavailable'][:len(old['unavailable'])]==old['unavailable']
sys.path.insert(0,str(TOOLS));import research_annex
target=OUT/'z-in-q-version14-research-annex.zip';start=time.monotonic()
result=research_annex.build(new,json.loads((OUT/'CONTENT-SOURCES.json').read_bytes()),ROOT,target,date(2026,11,7))
receipt={'archive':target.as_posix(),'archive_sha256':sha(target),'archive_bytes':target.stat().st_size,'selection_sha256':pins['selection_sha256'],'content_sources_sha256':pins['content_sources_sha256'],'elapsed_seconds':round(time.monotonic()-start,3),'validation':{k:v for k,v in result.items() if k!='unavailable'},'unavailable_count':len(result['unavailable']),'removed_paths':sorted(set(before)-set(after)),'retained_rows_unchanged':True,'predecessor_unavailable_rows_unchanged':True,'predecessor_archive_sha256':sha(OLD/'z-in-q-version14-research-annex.zip'),'status':'R2 author candidate built and R5-validated; independent successor review pending. No install or push.'}
dump('BUILD-RECEIPT.json',receipt);print(json.dumps(receipt))
