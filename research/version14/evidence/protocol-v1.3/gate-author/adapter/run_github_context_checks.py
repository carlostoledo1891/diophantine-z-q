"""Run read-only component tests and pin their inputs. No network or credentials."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
files=['github_read_context.py','test_github_read_context.py','GITHUB-READ-CONTEXT.md',
       'run_github_context_checks.py','protected_ledger_store.py','ledger_evidence_bridge.py',
       'offline_manifest_gate.py','git_manifest.py']
results={}
for test in ('test_github_read_context.py','test_store_bridge.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/test)],cwd=HERE,capture_output=True,text=True)
    log=test.removesuffix('.py')+'.log'
    (HERE/log).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[test]={'returncode':run.returncode,'log':log}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        'tests':results,'network_used':False,'credentials_used':False,'merge_authorized':False}
(HERE/'GITHUB-CONTEXT-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
sys.exit(any(row['returncode'] for row in results.values()))
