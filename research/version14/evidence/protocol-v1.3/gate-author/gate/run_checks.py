import hashlib,io,json,platform,unittest
from pathlib import Path
import test_offline_gate
H=Path(__file__).resolve().parent
packet,evidence=test_offline_gate.fixture()
for name,value in [('example-packet.json',packet),('example-unverified-evidence.json',evidence)]:
 (H/name).write_text(json.dumps(value,indent=2,sort_keys=True)+'\n',encoding='utf-8')
log=io.StringIO();result=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_offline_gate))
(H/'test-results.txt').write_text(log.getvalue(),encoding='utf-8')
files=['offline_gate.py','test_offline_gate.py','README.md','example-packet.json','example-unverified-evidence.json','title-classifier-review.md','title-classifier-checks.json','review_title_classifier.py','run_checks.py']
report={'passed':result.wasSuccessful(),'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'python':platform.python_version(),'platform':platform.platform(),'authentication_implemented':False,'live_github_implemented':False,'deployment_eligible':False,'independent_implementation_review':'pending','sha256':{n:hashlib.sha256((H/n).read_bytes()).hexdigest() for n in files}}
(H/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(0 if result.wasSuccessful() else 1)
