"""Freeze/test ingress with mock services and fixture-only secrets."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
names=['ingress.py','test_ingress.py','ingress.workflow.template.yml','INGRESS.md','run_ingress_checks.py','runtime.py','git_state.py']
results={}
for test in ('test_ingress.py','test_git_state.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/test)],cwd=HERE,capture_output=True,text=True)
    log='ingress-'+test.removesuffix('.py')+'.log';(HERE/log).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[test]={'returncode':run.returncode,'log':log}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'tests':results,'network_used':False,'fixture_keys_only':True,'merge_authorized':False}
(HERE/'INGRESS-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2));sys.exit(any(v['returncode'] for v in results.values()))
