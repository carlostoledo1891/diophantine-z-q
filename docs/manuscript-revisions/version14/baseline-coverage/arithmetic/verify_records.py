from pathlib import Path
import json, hashlib, sys
O=Path(__file__).parent
R=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-version6-release/repository')
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
freeze=read(O/'INITIAL-FREEZE.json')
for f,h in freeze['files'].items(): assert sha((O/f).read_bytes())==h,f
raw=(R/'manuscripts/quartic_v13.tex').read_bytes(); lines=raw.splitlines(keepends=True)
assert sha(raw)==freeze['source_sha256']
cov=read(O/'COVERAGE-INDEX.json')['passages']; uses=read(O/'INITIAL-SOURCE-USES.json')['uses']
nextline=1
for p in cov:
    assert p['start_line']==nextline
    assert p['sha256_raw_byte_lines']==sha(b''.join(lines[p['start_line']-1:p['end_line']]))
    nextline=p['end_line']+1
assert nextline==5931
ids={u['source_use_id'] for u in uses}
assert ids=={i for p in cov for i in p['source_use_ids']}
rec=read(O/'RECONCILIATION.json')
assert ids=={u['source_use_id'] for u in rec['reconciled_uses']}
for f,h in rec['inventory_and_history_pins'].items(): assert sha((R/f).read_bytes())==h,f
original=read(R/'docs/theorem-application-audit/computations/generator-arithmetic.json')
replay=read(O/'generator-arithmetic.json')
assert original==replay
result={'status':'PASS','scope':'Structural integrity of recorded coverage, original-byte passage hashes, frozen initial reconstruction, reconciliation ID completeness, source-record hashes, and exact decoded generator replay equality. Does not certify semantic exhaustiveness or mathematics.','python_executable':sys.executable,'python_version':sys.version,'covered_lines':[1,5930],'passages':len(cov),'source_use_groups':len(uses),'initial_unchanged':True,'generator_replay_matches_original_json':True,'cross_slice_supplier_review':'Requires parent integration of current separate reviews.'}
(O/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
manifest={'schema':'arithmetic-coverage-artifact-manifest-v1','source_sha256':sha(raw),'files':{p.name:sha(p.read_bytes()) for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}}
(O/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result,indent=2))
