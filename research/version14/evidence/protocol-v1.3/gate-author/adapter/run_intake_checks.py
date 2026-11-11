"""Pin intake candidate and run fixture suites. No credentials or network."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
names=['audit_intake.py','audit_intake_store.py','durable_intake.py','test_durable_intake.py',
       'probe_github_payloads.py','DURABLE-INTAKE.md','run_intake_checks.py',
       'operator_ledger.py','protected_ledger_store.py','ledger_evidence_bridge.py',
       'offline_manifest_gate.py','manifest_transport.py','git_manifest.py','github_read_context.py']
results={}
for test in ('test_durable_intake.py','test_github_read_context.py','test_store_bridge.py','test_manifest_gate.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/test)],cwd=HERE,text=True,capture_output=True)
    logfile='intake-'+test.removesuffix('.py')+'.log'
    (HERE/logfile).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[test]={'returncode':run.returncode,'log':logfile}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'tests':results,'network_used':False,'fixture_keys_only':True,'merge_authorized':False}
(HERE/'INTAKE-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2));sys.exit(any(x['returncode'] for x in results.values()))
