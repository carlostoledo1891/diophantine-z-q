"""Pin and check fork/restoration candidates without network or real secrets."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
names=['github_fork_context.py','test_github_fork_context.py','restore_verified_stores.py','test_restore_verified_stores.py',
       'FORK-AND-RESTORE.md','run_fork_restore_checks.py','probe_fork_refs.py','github_read_context.py',
       'protected_ledger_store.py','audit_intake_store.py']
results={}
for name in ('test_github_fork_context.py','test_restore_verified_stores.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/name)],cwd=HERE,capture_output=True,text=True)
    log='fork-'+name.removesuffix('.py')+'.log';(HERE/log).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[name]={'returncode':run.returncode,'log':log}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'tests':results,'network_used':False,'merge_authorized':False}
(HERE/'FORK-RESTORE-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2));sys.exit(any(v['returncode'] for v in results.values()))
