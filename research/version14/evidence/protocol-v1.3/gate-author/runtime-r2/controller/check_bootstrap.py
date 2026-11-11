"""Offline sanity check of root's recorded empty genesis. No API calls."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'adapter'))
from git_state import canonical,object_id
import operator_ledger,audit_intake

spec=importlib.util.spec_from_file_location('reviewed_bootstrap',ROOT/'bootstrap_state.py')
module=importlib.util.module_from_spec(spec)
with patch('http.client.HTTPSConnection',side_effect=AssertionError('offline check')):
    spec.loader.exec_module(module)
    files=module.initial_files()
record=json.loads((ROOT/'STATE-BOOTSTRAPPED.json').read_text())
index=json.loads(files['state/index.json'])
assert record['repository']==module.REPO=='elliotglazer/research-review-controller'
assert record['repository_id']==module.REPO_ID==1449903511
assert record['generation']==index['generation']==0 and index['parent'] is None
assert record['checkpoints']==index['checkpoints']
assert record['checkpoints']['operator']==operator_ledger.genesis('elliot-research-operator-20261107')
assert record['checkpoints']['intake']==audit_intake.genesis('elliot-research-intake-20261107')
sha=record['checkpoints']['publisher']['snapshot_sha256'];path='state/snapshots/'+sha+'.json'
raw=files[path]
assert len(files)==2 and set(index['files'])=={path}
assert hashlib.sha256(raw).hexdigest()==sha
assert index['files'][path]=={'blob':object_id('blob',raw),'sha256':sha,'size':len(raw)}
assert raw==canonical({'schema':'protocol-controller-generation/v1','controller_sha':None,
    'state':{'schema':'protocol-publisher-state/v1','generations':[],'targets':[]},'publication':None})
result={'status':'offline empty-genesis sanity checks passed',
    'bootstrap_source_sha256':hashlib.sha256((ROOT/'bootstrap_state.py').read_bytes()).hexdigest(),
    'record_sha256':hashlib.sha256((ROOT/'STATE-BOOTSTRAPPED.json').read_bytes()).hexdigest(),
    'recorded_remote_commit':record['state_commit'],'publisher_snapshot_sha256':sha,
    'limitations':['No live remote state was reread.','Remote commit ID cannot be reconstructed from the abbreviated observation record.'],
    'write_safety_review':'Source main refuses an existing state ref, accepts only absence404, creates an empty-parent initial commit and creates the ref without force. The live bootstrap is recorded as having run; this check did not rerun it.'}
(ROOT/'controller/BOOTSTRAP-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
