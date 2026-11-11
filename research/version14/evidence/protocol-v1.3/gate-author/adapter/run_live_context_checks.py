"""Run/pin the live evaluator fixture candidate without network or credentials."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
import live_protocol_context as live
names=['live_protocol_context.py','test_live_protocol_context.py','LIVE-PROTOCOL-CONTEXT.md','run_live_context_checks.py']+list(live.DEPENDENCY_PINS)
results={}
for test in ('test_live_protocol_context.py','test_durable_intake.py','test_store_bridge.py','test_manifest_gate.py'):
    run=subprocess.run([sys.executable,'-B',str(HERE/test)],cwd=HERE,capture_output=True,text=True)
    log='live-'+test.removesuffix('.py')+'.log';(HERE/log).write_text(run.stdout+run.stderr,encoding='utf-8')
    results[test]={'returncode':run.returncode,'log':log}
record={'files':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'tests':results,'network_used':False,'fixture_keys_only':True,'merge_authorized':False}
(HERE/'LIVE-CONTEXT-VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2));sys.exit(any(v['returncode'] for v in results.values()))
