from pathlib import Path
import hashlib, json, subprocess, sys
here=Path(__file__).resolve().parent
repo=here.parent/'protocol-ruleset-20261107/deployment-repository'
manifest=json.loads((here/'activation-author/ACTIVATION.json').read_bytes())
ref=sys.argv[1] if len(sys.argv)>1 else ':'
git=['git','-C',str(repo)]
for path,row in manifest['files'].items():
    spec=':'+path if ref==':' else ref+':'+path
    raw=subprocess.check_output(git+['show',spec])
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'],path
if ref==':':
    paths=subprocess.check_output(git+['diff','--cached','--name-only']).decode().splitlines()
else:
    paths=subprocess.check_output(git+['diff','--name-only',manifest['baseline_commit'],ref]).decode().splitlines()
assert set(paths)=={r['path'] for r in manifest['changes_from_bc56dd5']}
print(json.dumps({'ref':ref,'files_verified':len(manifest['files']),'changed_files':len(paths)}))
