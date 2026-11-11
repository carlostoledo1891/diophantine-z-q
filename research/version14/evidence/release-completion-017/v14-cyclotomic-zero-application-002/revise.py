import json,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;A=O.parent/'v14-cyclotomic-zero-application-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
d=json.loads((A/'COMPONENTS.json').read_text());d[0]['connection']['supplier_passage_role']='proof';dump('COMPONENTS.json',d)
for n in ['USE-LOCATION-DELTAS.json','RECONCILIATION.json']:(O/n).write_bytes((A/n).read_bytes())
dump('MANIFEST.json',{'author':'/root/v14_sign_conductor','change':'Only supplier_passage_role corrected from statement to proof for the actual local proof.','files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in O.iterdir() if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
