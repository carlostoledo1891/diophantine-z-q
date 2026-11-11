import hashlib,json,shutil
from pathlib import Path
O=Path(__file__).resolve().parent;OLD=O.parent/'v14-ly-source-inputs-author-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for p in OLD.iterdir():
 if p.is_file() and p.name not in ['author.py','MANIFEST.json']:shutil.copyfile(p,O/p.name)
data=json.loads((O/'USE-LOCATION-DELTAS.json').read_bytes())
for x in data:x['append_consumer_locations']=[l for l in x['append_consumer_locations'] if not (l['pin']['path'].endswith('/PROOF.md') and l['start_line']==78)]
save('USE-LOCATION-DELTAS.json',data)
save('SOURCE-ROLE-REPAIR.json',{'path':'research/version14/proofs/ly-d6-normalization-v1/PROOF.md','line':78,'role':'Declaration of separately required A001 inputs, not their actual application.','outgoing_provenance_use_ids':['ACTIVE-DATUM-SOURCE-COARSE','ACTIVE-DATUM-SOURCE-PRINCIPAL'],'incoming_use_ids':[],'retained_applications':'COARSE at PROOF85 supplies the Q-defined moduli map; both actual same-datum identifications in CURRENT-INTERFACE7-9 remain conditional on their stated datum.'})
save('DELTA.json',{'old_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'components_sha256':sha((O/'COMPONENTS.json').read_bytes()),'only_change':'Remove two actual-application location appends at declaration PROOF78; add explicit declaration/provenance role. Five components unchanged.'})
save('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
