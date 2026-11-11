import hashlib,json,shutil
from pathlib import Path
O=Path(__file__).resolve().parent;OLD=O.parent/'v14-atkin-newform-input-author-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def dig(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for p in OLD.rglob('*'):
 if p.is_file() and p.name not in ['MANIFEST.json','author.py']:
  dest=O/p.relative_to(OLD);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
c=json.loads((O/'COMPONENTS.json').read_bytes());x=c[1];u=x['use'];co=x['connection']
raw=(O/'SOURCE-CONNECTION.md').read_bytes();sl=u['supplier']['location'];sl['end_line']=11;sl['excerpt_sha256']=sha(b''.join(raw.splitlines(keepends=True)[6:11]))
u['inline_argument']=sl;co['connecting_derivation']['location']=sl
co['consumer_locations']=co['consumer_locations'][:2];u['passages']=u['passages'][:2]
co['adverse_cases']['evidence']=[sl]+co['consumer_locations'];co['use_sha256']=dig(u)
save('COMPONENTS.json',c)
save('DELTA.json',{'old_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'change':'The actual quotient output is supplied by full proof7-11 and consumed only in the two actual main callers. Remove source11 as self-consumer; primitive theorem is still imported at source9.'})
save('CHECKS.json',{'uses':len(c),'hashes':all(dig(x['use'])==x['connection']['use_sha256'] for x in c),'counts':all(len(x['use']['passages'])==len(x['connection']['consumer_locations']) for x in c),'source_lines':len(raw.splitlines())})
save('MANIFEST.json',{'files':{str(p.relative_to(O)).replace('\\','/'):{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
