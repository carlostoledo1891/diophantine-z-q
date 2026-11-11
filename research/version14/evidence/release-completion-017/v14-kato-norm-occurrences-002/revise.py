import json,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;A=O.parent/'v14-kato-norm-occurrences-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
d=json.loads((A/'USE-LOCATION-DELTAS.json').read_text());r=d[0];r['append_consumer_locations']=r['append_consumer_locations'][1:];r['append_passage_ids']=['ACTIVE-THETA-SOURCE-KATO-NORM-RELATION-REPEAT-'+str(i) for i in range(1,5)];dump('USE-LOCATION-DELTAS.json',d)
n=json.loads((A/'ROLE-NOTES.json').read_text());n['locations'][0]['role']='Source roadmap/provenance only. No consumer append at13355–61. The four later calculations are the actual applications.';dump('ROLE-NOTES.json',n)
dump('MANIFEST.json',{'author':'/root/v14_sign_conductor','change':'Removes roadmap actual-use append and supplies four unique proposed passage IDs; other source/profile/location assertions unchanged.','files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in O.iterdir() if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
