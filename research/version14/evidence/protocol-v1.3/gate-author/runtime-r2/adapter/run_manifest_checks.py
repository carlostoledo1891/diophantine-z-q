import contextlib,hashlib,io,json,pathlib,platform,unittest
import offline_manifest_gate as g
import git_manifest as m
import test_manifest_gate as tests
H=pathlib.Path(__file__).resolve().parent
core=H.parent/'gate/offline_gate.py'
assert hashlib.sha256(core.read_bytes()).hexdigest()=='2fa1678f4533bfd1067e8b73e8d9ab8a1e85c1716ba9b72dfb4bc9fcd626c5ad'
results=[]
for label,module in [('schema1-unchanged',tests.v1),('schema2-manifest',tests)]:
 log=io.StringIO();r=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
 (H/(label+'-tests.log')).write_text(log.getvalue(),encoding='utf-8')
 results.append({'suite':label,'passed':r.wasSuccessful(),'tests':r.testsRun})
actual=[]
for name,folder in [('public','repository'),('private','private-repository')]:
 manifest=m.load_json(H/(name+'-manifest.json'));content_map,_=g.snapshot(manifest,manifest['git_hash'])
 repo=H.parents[2]/'work/quartic-version6-release'/folder
 reader=g.GitBlobReader({'head':repo});checked=[]
 for path in ['scripts/check_application_reviews.py','docs/audit-history/current.json','manuscripts/quartic_v12.tex']:
  if path not in manifest['files']:continue
  entry=manifest['files'][path]
  with contextlib.closing(reader.open('head',path,entry)) as stream:m.verify_blob(stream,entry,manifest['git_hash'])
  checked.append({'path':path,'size':entry['size'],'sha256':entry['sha256']})
 actual.append({'repository':name,'commit':manifest['commit'],'complete_files':len(content_map),'content_manifest_sha256':g.digest(content_map),'verified_blobs':checked,'review_receipts_created':False})
files=['offline_manifest_gate.py','test_manifest_gate.py','MANIFEST-CORE.md','git_manifest.py','manifest_transport.py','run_manifest_checks.py']
out={'passed':all(x['passed'] for x in results),'suites':results,'actual_tree_prechecks':actual,'python':platform.python_version(),'sha256':{f:hashlib.sha256((H/f).read_bytes()).hexdigest() for f in files},'merge_authorized':False,'independent_review':'pending'}
(H/'MANIFEST-VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
