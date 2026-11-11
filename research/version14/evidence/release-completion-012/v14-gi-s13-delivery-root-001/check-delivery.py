from pathlib import Path
import json,shutil,subprocess,zipfile,hashlib
h=Path(__file__).resolve().parent
r=h/'candidate/research/version14/proofs/local-gi-v1'
m=json.loads((r/'CUMULATIVE-HANDOFF.json').read_bytes())
out=h/'reduced-verification'
assert not out.exists()
names={e['path'] for e in m['retained']}|{e['path'] for e in m['added_text']}|{'CUMULATIVE-HANDOFF.json','PROOF-ONLY-MANIFEST.json','verify-handoff.py'}
for n in names:
 p=out/n;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(r/n,p)
res=subprocess.run([__import__('sys').executable,'-B',str(out/'verify-handoff.py')],capture_output=True,text=True)
print(res.stdout);assert res.returncode==0,res.stderr
with zipfile.ZipFile(h/'candidate/research/version14/proofs/GI-PROOF-ONLY.zip') as z:
 assert z.testzip() is None
 fm=json.loads(z.read('PROOF-ONLY-MANIFEST.json'))
 assert set(z.namelist())=={e['path'] for e in fm['files']}|{'PROOF-ONLY-MANIFEST.json'}
 for e in fm['files']:
  b=z.read(e['path']);assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256']
result={'reduced_check':json.loads(res.stdout),'standalone_zip_full_members':len(fm['files']),'standalone_zip_all_pins_match':True}
(h/'DELIVERY-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
