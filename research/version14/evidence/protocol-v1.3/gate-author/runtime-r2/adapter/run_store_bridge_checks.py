import hashlib,io,json,pathlib,unittest
import test_store_bridge
import test_operator_ledger
import test_manifest_gate
H=pathlib.Path(__file__).resolve().parent
expected={'operator_ledger.py':'5e2cec65c3b516f62ec4bbd9ae071c431c11ab7456edd4d7000c986782c072d7','offline_manifest_gate.py':'4d57a1b1300dab80957d39857e12a9a5c0926c8dddf5874c5ba1c0d80ff0e5a0','git_manifest.py':'8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef'}
for f,d in expected.items():assert hashlib.sha256((H/f).read_bytes()).hexdigest()==d
results=[]
for name,module in [('store-bridge',test_store_bridge),('accepted-ledger',test_operator_ledger),('accepted-schema2',test_manifest_gate)]:
 log=io.StringIO();r=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
 (H/(name+'-integration-tests.log')).write_text(log.getvalue(),encoding='utf-8');results.append({'suite':name,'passed':r.wasSuccessful(),'tests':r.testsRun})
files=['protected_ledger_store.py','ledger_evidence_bridge.py','test_store_bridge.py','STORE-BRIDGE.md','run_store_bridge_checks.py']
out={'passed':all(x['passed'] for x in results),'results':results,'sha256':{f:hashlib.sha256((H/f).read_bytes()).hexdigest() for f in files},'accepted_dependencies_unchanged':expected,'fixture_keys_only':True,'automatic_capture':False,'live_context_verifier':False,'github_publisher':False,'merge_authorized':False,'independent_review':'pending'}
(H/'STORE-BRIDGE-VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
