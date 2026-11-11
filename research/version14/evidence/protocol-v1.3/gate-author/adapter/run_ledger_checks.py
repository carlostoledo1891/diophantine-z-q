import hashlib,io,json,pathlib,platform,unittest
import test_operator_ledger
H=pathlib.Path(__file__).resolve().parent
log=io.StringIO();r=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_operator_ledger))
(H/'operator-ledger-tests.log').write_text(log.getvalue(),encoding='utf-8')
files=['operator_ledger.py','test_operator_ledger.py','OPERATOR-LEDGER.md','run_ledger_checks.py']
report={'passed':r.wasSuccessful(),'tests':r.testsRun,'python':platform.python_version(),'sha256':{f:hashlib.sha256((H/f).read_bytes()).hexdigest() for f in files},'keys_used':'synthetic fixtures only; no actual keys generated or printed','automatic_capture_implemented':False,'durable_storage_implemented':False,'provider_attestation':False,'merge_authorized':False,'independent_review':'pending'}
(H/'LEDGER-VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,indent=2))
raise SystemExit(0 if r.wasSuccessful() else 1)
