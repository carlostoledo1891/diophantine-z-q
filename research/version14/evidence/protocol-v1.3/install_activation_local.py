"""Install the independently accepted idle tree after verified normal merges."""
from pathlib import Path
import hashlib, json, subprocess

here = Path(__file__).resolve().parent
rollout = here.parent / 'protocol-ruleset-20261107'
repo = rollout / 'deployment-repository'
candidate = here / 'activation-author'
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha((candidate/'ACTIVATION.json').read_bytes()) == 'ece0148e3f0c4e378d183c5cfcca4c79f5feecf418caeede6673e9c5dda6dfac'
manifest = json.loads((candidate/'ACTIVATION.json').read_bytes())
git = ['git','-C',str(repo)]
assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip() == manifest['baseline_commit']
assert not subprocess.check_output(git+['status','--porcelain']).strip()
receipts = rollout/'protocol-v1.2/merge-refresh-785efabe/finalizer-live/receipts'
expected = {'diophantine-z-q':(10,'9c0b3aba60d90fdcac82115f0582a6f52f1054f7'),
            'private-diophantine':(2,'225a60c6eb38d3b8aafc792ea8fccd4ecf7a84bd')}
for name,(pr,commit) in expected.items():
    value=json.loads((receipts/f'{name}-pr-{pr}.json').read_bytes())
    assert value['target']['name']==name and value['target']['pr']==pr
    assert value['readback']['merge_commit']==commit
    assert value['evaluation']['id']==42448878205
assert json.loads((candidate/'tree/controller/config.json').read_bytes())['jobs']==[]
for path,row in manifest['files'].items():
    raw=(candidate/'tree'/path).read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes'],path
for path,row in manifest['files'].items():
    target=repo/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes((candidate/'tree'/path).read_bytes())
print(json.dumps({'installed_files':len(manifest['files']),'changed_files':len(manifest['changes_from_bc56dd5']),'jobs':[]}))
