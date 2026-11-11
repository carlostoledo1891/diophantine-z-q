from pathlib import Path
import hashlib,json,subprocess,sys,importlib.util
r=Path.cwd();out=r/'work/source-risk-review-20261107/v14-controller-preparation-001';d=r/'work/protocol-ruleset-20261107/deployment-repository'
raw=(out/'bindings.template.json').read_bytes();target=out/'draft-must-not-bind'
cmd=[sys.executable,'-B',str(out/'bind.py'),'--bindings',str(out/'bindings.template.json'),'--bindings-sha256',hashlib.sha256(raw).hexdigest(),'--input-root',str(out),'--repo',str(r/'work/quartic-v14-release/preview-repository'),'--deployment',str(d),'--output',str(target)]
q=subprocess.run(cmd,capture_output=True,text=True)
assert q.returncode!=0 and 'unbound draft field' in q.stderr and not target.exists(),(q.returncode,q.stdout,q.stderr)
compile((out/'bind.py').read_text(encoding='utf8'),str(out/'bind.py'),'exec')
sys.path.insert(0,str(d/'controller'));import runtime
result={'schema':'v14-controller-preparation-tests/v1','pure_refusal_tests':5,'draft_rejected':True,'draft_returncode':q.returncode,'draft_stderr':q.stderr.strip(),'no_output_on_refusal':not target.exists(),'runtime_import':True,'runtime_dispatch':False,'positive_gate_fixture_used':False,'limitations':'No final-source/PR/observation inputs yet; no successful bound bundle or live gate run claimed.'}
(out/'TESTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
files={p.relative_to(out).as_posix():{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts}
manifest={'schema':'v14-controller-preparation-manifest/v1','author':'/root/v14_arithmetic_author','status':'author draft awaiting independent review; no deployable bindings or live observations fabricated','files':files}
(out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
print(json.dumps({'files':len(files),'manifest_sha256':hashlib.sha256((out/'MANIFEST.json').read_bytes()).hexdigest(),'tests':result}))
