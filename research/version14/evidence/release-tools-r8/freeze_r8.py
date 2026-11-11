"""Freeze the tested R8 successor without modifying R7."""
from pathlib import Path
import hashlib,json

root=Path(__file__).resolve().parent
parent=root.with_name('quartic-v14-release-r7')
sha=lambda raw:hashlib.sha256(raw).hexdigest()
delta=json.loads((root/'R8-DELTA.json').read_bytes())
tests=json.loads((root/'TEST-RESULT.json').read_bytes())
assert tests['count']==37 and tests['result']=='PASS'
assert sha((parent/'MANIFEST.json').read_bytes())==delta['parent_manifest_sha256']
changed=[]
for old in parent.rglob('*'):
    if old.is_file():
        name=old.relative_to(parent).as_posix()
        if name=='MANIFEST.json':continue
        if old.read_bytes()!=(root/name).read_bytes():changed.append(name)
assert sorted(changed)==['research_annex.py','test_research_annex.py']
for name in ('package_v14.py','reviewed-literal-files.json'):
    assert (root/name).read_bytes()==(parent/name).read_bytes()
import package_v14
for name in ('research_annex.py','test_research_annex.py'):
    package_v14.check_private_key_markers('research/version14/evidence/release-tools-r8/'+name,(root/name).read_bytes())
files={}
for path in sorted(root.rglob('*')):
    if not path.is_file():continue
    name=path.relative_to(root).as_posix()
    if name=='MANIFEST.json':continue
    assert '__pycache__' not in path.parts
    raw=path.read_bytes();files[name]={'bytes':len(raw),'sha256':sha(raw)}
for name in ('research_annex.py','test_research_annex.py','package_v14.py','release_common.py','reviewed-literal-files.json'):
    assert name in files
manifest={'author':'/root/astra_v14_assertions_arithmetic','status':'awaiting independent Sol review',
          'change':'Constant-folded fragment spelling for three scanner/test byte literals in two files; scanner behavior and historical five-file allowlist unchanged.',
          'prior_manifest_sha256':delta['parent_manifest_sha256'],'inherited_source_delta':changed,
          'tests':tests,'files':files}
raw=(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode('utf8')
(root/'MANIFEST.json').write_bytes(raw)
print(json.dumps({'manifest_sha256':sha(raw),'files':len(files),'changed_inherited_source_files':changed}))
