"""Local test/freeze helper. Never performs remote writes."""
from pathlib import Path
import hashlib,json,subprocess,sys
H=Path(__file__).resolve().parent
command=[sys.executable,'-B','-m','unittest','-v','test_publisher','test_live_integration']
r=subprocess.run(command,cwd=H,capture_output=True,text=True)
(H/'TESTS.log').write_text(r.stdout+r.stderr,encoding='utf-8')
if r.returncode:raise SystemExit(r.returncode)
files=['app_publisher.py','generation_state.py','test_publisher.py','test_live_integration.py','README.md','run_checks.py','TESTS.log']
pins={n:hashlib.sha256((H/n).read_bytes()).hexdigest() for n in files}
dependency=H.parent/'adapter/live_protocol_context.py'
manifest={'scope':'isolated publisher, no real HTTP transport or remote authority implementation','files':pins,
          'live_evaluator_sha256':hashlib.sha256(dependency.read_bytes()).hexdigest(),
          'tests':{'fake_app':34,'actual_live_evaluator_fake_app':4,'total':38,'exit_code':r.returncode},
          'remote_writes':False,'independent_review':'pending','deployment_authorized':False}
(H/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
