from pathlib import Path
import json,hashlib,subprocess,sys,time
H=Path(__file__).resolve().parent;P=H/'quartic-299-314'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={p.relative_to(P).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(P.rglob('*')) if p.is_file() and p.name!='PACKAGE-MANIFEST.json'}
raw=(json.dumps(files,indent=2)+'\n').encode();mf=P/'PACKAGE-MANIFEST.json'
if mf.exists():assert mf.read_bytes()==raw
else:mf.write_bytes(raw)
t=time.monotonic()
run=subprocess.run([sys.executable,'-B',str(P/'verify_lineage.py')],capture_output=True,text=True,encoding='utf-8')
(H/'PACKAGE-VERIFICATION.txt').write_text(run.stdout+run.stderr,encoding='utf-8')
assert run.returncode==0,run.stderr
receipt={'status':'PASS','package':'quartic-299-314','manifestSha256':sha(mf),'manifestBytes':mf.stat().st_size,
 'filesExcludingManifest':len(files),'bytesExcludingManifest':sum(x['bytes'] for x in files.values()),
 'filesIncludingManifest':len(files)+1,'bytesIncludingManifest':sum(x['bytes'] for x in files.values())+mf.stat().st_size,
 'sourceManifestSha256':sha(P/'SOURCE-MANIFEST.json'),'artifactManifestSha256':sha(P/'ARTIFACTS.json'),
 'verificationPlanSha256':sha(P/'VERIFICATION-PLAN.json'),'verifierSha256':sha(P/'verify_lineage.py'),
 'artifactVerifierSha256':sha(P/'verify_artifacts.py'),'readmeSha256':sha(P/'README.md'),'acceptanceSha256':sha(P/'ACCEPTANCE.json'),
 'elapsedSeconds':round(time.monotonic()-t,3),'logSha256':sha(H/'PACKAGE-VERIFICATION.txt'),
 'scope':'Author packaging verification; independent source, lift, and compact reviews preserved. No new publication or optimization.'}
(H/'PACKAGE-FREEZE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
