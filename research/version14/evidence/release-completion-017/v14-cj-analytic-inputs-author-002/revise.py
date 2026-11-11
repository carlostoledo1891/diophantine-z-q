import hashlib,json,shutil
from pathlib import Path
O=Path(__file__).resolve().parent;OLD=O.parent/'v14-cj-analytic-inputs-author-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for p in OLD.iterdir():
 if p.is_file() and p.name not in ['author.py','MANIFEST.json']:shutil.copyfile(p,O/p.name)
c=json.loads((O/'COMPONENTS.json').read_bytes())
for x in c:x['connection']['connecting_derivation']['kind']='derivation'
save('COMPONENTS.json',c);save('DELTA.json',{'old_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'only_change':'All three connecting_derivation.kind fields are derivation. No assertion, location or use hash changes.'})
save('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
