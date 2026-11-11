"""Freeze/test fork-capable evaluation. No credentials, network or API mutation."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
names=['live_protocol_context_forks.py','live_protocol_context.py','github_fork_context.py',
       'test_live_protocol_context_forks.py','LIVE-FORK-PROFILE.md','run_live_fork_checks.py']
results={}
for test in ('test_live_protocol_context_forks.py','test_github_fork_context.py','test_restore_verified_stores.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/test)],cwd=HERE,capture_output=True,text=True)
    log='profile-'+test.removesuffix('.py')+'.log';(HERE/log).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[test]={'returncode':run.returncode,'log':log}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'tests':results,'network_used':False,'merge_authorized':False}
(HERE/'LIVE-FORK-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2));sys.exit(any(v['returncode'] for v in results.values()))
