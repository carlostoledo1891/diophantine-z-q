import hashlib,json,shutil
from pathlib import Path
O=Path(__file__).resolve().parent;OLD=O.parent/'v14-cj-igusa-source-index-author-002'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for p in OLD.iterdir():
 if p.is_file() and p.name not in ['revise.py','MANIFEST.json']:shutil.copyfile(p,O/p.name)
reasons={66:'The good-reduction input specializes an already supplied geometric Atkin-Lehner quotient/dual operation and its finite diagram. It does not construct that operation or identify the split local normalizer with it; those are explicit caller requirements retained with the pending transformation row83.',79:'Finite-sum linearity is a local argument under input4: the same additive lambda_M is defined on the actual F_(q^2) domain and the parametrization values lie there. This line does not prove that map, its domain or those rationality facts; the actual detector/geometric caller bindings remain required in the pending caller row87.'}
affected={}
for filename in ['INDEX.json','INDEX-DRAFT.json']:
 data=json.loads((O/filename).read_bytes())
 for row in data:
  l=row['location']
  if l['pin']['path'].endswith('/cj-conductor-one-v1/proof.md') and l['start_line'] in reasons:
   row['reason']=reasons[l['start_line']]
   if l['start_line']==79:row['no_imports_reason']=row['reason']
   affected[row['id']]=l['start_line']
 save(filename,data)
roles=json.loads((O/'SOURCE-ROLES.json').read_bytes())
for row in roles:
 if row['id'] in affected:
  line=affected[row['id']];row['reason']=reasons[line];row['caller_requirements']=reasons[line];row['role']='conditional specialization of supplied operation' if line==66 else 'finite-sum deduction under supplied additive map and domain'
save('SOURCE-ROLES.json',roles)
pending=json.loads((O/'PENDING.json').read_bytes())
for row in pending:
 if row['location']['start_line']==83:row['requirement']+=' Also retain the geometric quotient/dual realization of the actual Atkin-Lehner operation used at66.'
 if row['location']['start_line']==87:row['requirement']+=' Also bind the actual additive lambda_M and F_(q^2) domain used at79; finite-sum algebra does not supply these.'
save('PENDING.json',pending)
save('DELTA003.json',{'old_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'change':'Explicit conditional boundaries at CJ66 and79; reinforce existing pending83/87 caller requirements. No new use or location, and no promotion of pending rows.'})
save('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
