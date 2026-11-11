import sys,json
from pathlib import Path
sys.path.insert(0,"C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-v14-release-assembled-001/")
import artifact_contracts as a
import package_v14 as p
r=Path("C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-v14-release/preview-repository/")
f=json.loads(Path(__file__).with_name('FINAL-INPUT-ARTIFACT-FRAGMENT.json').read_text())
current={x['path']:(r/x['path']).read_bytes() for x in f.values()}
for x in f.values(): a.check_pin(x,current)
p.admissible(f['pdf']['path'])
for x in f.values():
 bad=dict(current);bad[x['path']]+=b'changed'
 try:a.check_pin(x,bad)
 except ValueError:pass
 else:raise AssertionError('changed bytes accepted')
data,entries=a.project_pdfs()
assert len(entries)==18 and f['pdf']['path'] not in entries
assert a.sha(Path(a.__file__).with_name('project-pdfs.json').read_bytes())==a.PROJECT_PDFS_SHA
try:p.admissible('manuscripts/unapproved.pdf')
except ValueError:pass
else:raise AssertionError('unapproved PDF accepted')
print(json.dumps({'result':'pass','checks':7,'project_pdfs':len(entries),'main_separate':True}))
