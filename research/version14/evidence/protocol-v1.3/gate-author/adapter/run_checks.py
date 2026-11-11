import hashlib,io,json,pathlib,platform,subprocess,unittest
import git_manifest as m
import test_adapter
H=pathlib.Path(__file__).resolve().parent
log=io.StringIO();result=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_adapter))
(H/'test-results.txt').write_text(log.getvalue(),encoding='utf-8')
comparisons=[]
root=H.parents[2]
for name,folder in [('public','repository'),('private','private-repository')]:
 manifest=m.load_json(H/(name+'-manifest.json'));m.verify_manifest(manifest)
 repo=root/'work/quartic-version6-release'/folder
 raw=subprocess.check_output(['git','-C',str(repo),'ls-tree','-r','-l','-z',manifest['commit']])
 expected={}
 for line in raw.split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t',1);mode,kind,oid,size=meta.split();assert kind==b'blob'
  expected[path.decode()]={'mode':mode.decode(),'blob':oid.decode(),'size':int(size)}
 actual={p:{k:v[k] for k in ('mode','blob','size')} for p,v in manifest['files'].items()}
 assert expected==actual
 comparisons.append({'repository':name,'commit':manifest['commit'],'git_ls_tree_full_match':True,'manifest_bytes':(H/(name+'-manifest.json')).stat().st_size,'manifest_canonical_sha256':m.sha(m.canonical(manifest)),**manifest['stats']})
files=['git_manifest.py','manifest_transport.py','test_adapter.py','PLAN.md','APP-SETTINGS.json','APP-SETUP.md','public-manifest.json','private-manifest.json']
report={'passed':result.wasSuccessful(),'tests':result.testsRun,'python':platform.python_version(),'git':subprocess.check_output(['git','--version']).decode().strip(),'actual_repositories':comparisons,'sha256':{f:hashlib.sha256((H/f).read_bytes()).hexdigest() for f in files},'github_origin_authenticated':False,'agent_provenance_implemented':False,'github_publisher_implemented':False,'independent_review':'pending'}
(H/'VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(0 if result.wasSuccessful() else 1)
