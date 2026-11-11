"""Freeze this isolated proposal. Does not install or alter controller state."""
from pathlib import Path
import hashlib,json,subprocess

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'protocol-ruleset-20261107'/'deployment-repository'
OVER=HERE/'overlay'
EXPECTED='ce9c4cf5f08eb5a56eabec041fddd81f2dddcc5f'
assert subprocess.check_output(['git','-C',str(BASE),'rev-parse','HEAD'],text=True).strip()==EXPECTED
def sha(b): return hashlib.sha256(b).hexdigest()
def write(p,value):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')

history=OVER/'deployment-history'/'2026-11-07-before-v1.4'
history.mkdir(parents=True,exist_ok=True)
for name in ('DEPLOYMENT-STATUS.md','DEPLOYMENT-DECISION.md'):
    (history/name).write_bytes((BASE/name).read_bytes())
notice=(b'> Historical proposal, preserved November 7, 2026. This document is not a current deployment receipt. '
        b'The exact original bytes are retained in `deployment-history/2026-11-07-before-v1.4/DEPLOYMENT-DECISION.md`. '
        b'See `DEPLOYMENT-STATUS.md` for the current bounded readback.\n\n')
(OVER/'DEPLOYMENT-DECISION.md').write_bytes(notice+(BASE/'DEPLOYMENT-DECISION.md').read_bytes())
(OVER/'DEPLOYMENT-STATUS.md').write_text('''# Deployment status

As reported by the release integrator on November 7, 2026, the controller remote main and protected `PROTOCOL_APPROVED_SHA` both identify `ce9c4cf5f08eb5a56eabec041fddd81f2dddcc5f`. Controller run `42452003901` succeeded with the empty active-job configuration `jobs: []`. This is the deployed v1.3 runtime. The present v1.4 extension is an isolated proposal pending independent review, installation, deployment and new remote readback. It is not live v1.4 acceptance.

This status records the integrator's reported readback, not a second remote observation by the implementation author. The deployment integrator must bind the actual readback evidence and update this status after any later deployment. An idle successful run does not accept a mathematical PR.

The previous status and deployment-decision bytes are preserved in `deployment-history/2026-11-07-before-v1.4/`. They describe earlier pending/failed v1.2 activity and the original deployment proposal. They must not be read as the current deployment state.

Branch protection continues to require the eleven Actions checks and the dedicated independent-review App check. No second human approval is introduced by this proposal. The extension does not change active jobs, signed observations, receipts, ledger keys or branch protection. It checks recorded evidence, not mathematical truth or honest review.
''',encoding='utf-8',newline='\n')

bundle=json.loads((BASE/'BUNDLE-MANIFEST.json').read_text())
baseline=[];drift=[]
for path,row in bundle['files'].items():
    p=BASE/path
    if not p.exists():
        drift.append({'path':path,'reason':'missing'})
        continue
    raw=p.read_bytes()
    baseline.append({'path':path,'bytes':len(raw),'sha256':sha(raw)})
    if len(raw)!=row['bytes'] or sha(raw)!=row['sha256']:
        drift.append({'path':path,'reason':'baseline-manifest-mismatch','actual_sha256':sha(raw),'declared_sha256':row['sha256']})
write(HERE/'BASELINE-PINS.json',{'commit':EXPECTED,'files':baseline,'existing_manifest_discrepancies':drift})
assert not drift, drift
for p in sorted(OVER.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.name=='BUNDLE-MANIFEST.json':continue
    rel=p.relative_to(OVER).as_posix();raw=p.read_bytes()
    bundle['files'][rel]={'bytes':len(raw),'sha256':sha(raw),'role':'v1.4-proposal-or-preserved-history','source':None}
bundle['production_edges']['adapter/coverage_gate.py']=['adapter/connections_gate.py','adapter/offline_manifest_gate.py']
bundle['production_edges']['adapter/connections_gate.py']=['adapter/offline_manifest_gate.py']
bundle['test_edges']['adapter/connections_gate.py']=['adapter/offline_manifest_gate.py']
bundle['test_edges']['adapter/coverage_gate.py']=['adapter/connections_gate.py','adapter/offline_manifest_gate.py']
bundle['test_edges']['adapter/test_connections_gate.py']=['adapter/coverage_gate.py','adapter/offline_manifest_gate.py','adapter/test_coverage_gate.py','adapter/test_manifest_gate.py','adapter/ledger_evidence_bridge.py']
bundle['limitation']='Isolated v1.4 overlay on pinned deployed v1.3 controller; pending independent review and deployment. Structural checks do not prove mathematics.'
assert 'BUNDLE-MANIFEST.json' not in bundle['files']
write(OVER/'BUNDLE-MANIFEST.json',bundle)
files=[]
for p in sorted(HERE.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.name=='MANIFEST.json':continue
    raw=p.read_bytes();files.append({'path':p.relative_to(HERE).as_posix(),'bytes':len(raw),'sha256':sha(raw)})
write(HERE/'MANIFEST.json',{'schema':'protocol14-gate-proposal/v1','status':'author_proposal_pending_independent_review',
      'baseline_commit':EXPECTED,'protocol_sha256':'3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9',
      'files':files,'limitations':'No current mathematical acceptance, deployment or remote mutation. Test fixtures are synthetic.'})
print('Manifest SHA256',sha((HERE/'MANIFEST.json').read_bytes()))
print('Files',len(files),'overlay files',len([r for r in files if r['path'].startswith('overlay/')]))
