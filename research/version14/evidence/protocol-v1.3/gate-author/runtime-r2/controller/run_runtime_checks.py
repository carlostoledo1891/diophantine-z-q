"""Record bounded offline controller tests and frozen source hashes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

H=Path(__file__).resolve().parent
run=subprocess.run([sys.executable,'-B','-m','unittest','test_runtime','test_git_state','-v'],
                   cwd=H,capture_output=True,text=True)
(H/'runtime-tests.log').write_text(run.stdout+run.stderr,encoding='utf-8',newline='\n')
if run.returncode:
    raise SystemExit(run.returncode)
files=['runtime.py','test_runtime.py','workflow.template.yml','requirements.lock',
       'RUNTIME.md','DEPENDENCY-SOURCES.json','run_runtime_checks.py','runtime-tests.log']
pins={name:hashlib.sha256((H/name).read_bytes()).hexdigest() for name in files}
dependencies=['git_state.py','../publisher/app_publisher.py','../publisher/generation_state.py',
              '../publisher/github_app_transport.py','../adapter/restore_verified_stores.py',
              '../adapter/live_protocol_context.py','../adapter/live_protocol_context_forks.py',
              '../adapter/github_fork_context.py','../immutable-cache/immutable_git_cache.py']
result={'status':'26 offline tests passed; independent review and live deployment separate',
        'runtime_files':pins,
        'dependency_pins':{name:hashlib.sha256((H/name).read_bytes()).hexdigest() for name in dependencies},
        'network':'No GitHub API calls; tests replace HTTP only, using real signed stores, evaluator, publisher and CAS.',
        'not_established':['live API deployment','Linux binary dependency execution','mathematical correctness of user evidence']}
(H/'RUNTIME-VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result,indent=2))
