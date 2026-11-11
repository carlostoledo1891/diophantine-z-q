import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(o):return sha(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
base=ROOT/'work/source-risk-review-20261107/v14-main-active-connections-author-001'
theta=ROOT/'work/source-risk-review-20261107/v14-theta-active-author-003/COMPONENTS.json'
targets={c['use']['id']:c for c in json.loads(theta.read_bytes())}
specs=[('KATO-CLASS-INTERFACE-COMPONENT.json',11,'Only the retained index-domain, repeated/new-prime norm cases and equality of the supplied dyadic class. The rational hypotheses, original2004 construction and full-H2 correction remain separate.'),('PARITY-COMPONENT.json',29,'Only the implication from full rational 2-primary Selmer corank one to root number minus one for this same E. BFH nonvanishing and sequential witness choices remain separate.'),('CJ-COMPONENT.json',44,'Only fixed-type labelled conductor-one reduction, equivariance, multiplicity one and the same unaveraged finite sum. Opposite orientation and total mass remain separate in T045.')]
rows=[]
for filename,n,scope in specs:
 p=base/filename;c=json.loads(p.read_bytes());t=targets['ACTIVE-THETA-T'+str(n).zfill(3)]
 assert c['use']['consumer']==t['use']['consumer']
 assert c['connection']['use_sha256']==digest(c['use'])
 rows.append({'initial_use':'HIST-theta-T'+str(n).zfill(3),'current_clause':t['use']['id'],'current_clause_use_sha256':digest(t['use']),'existing_use':c['use']['id'],'existing_use_sha256':digest(c['use']),'existing_component':{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':sha(p.read_bytes())},'scope':scope,'effect':'Add observation mapping only. No component, dependency, assertion, consumer or accepted source bytes change.'})
data={'author':'/root/v14_sign_conductor','status':'Author mapping proposal pending independent comparison','theta_components':{'path':str(theta.relative_to(ROOT)).replace('\\','/'),'sha256':sha(theta.read_bytes())},'rows':rows,'limits':'These repeated observations consume existing current uses. This file neither creates a new mathematical supplier nor promotes source ancestry or all of a theta clause to accepted.'}
(OUT/'MAPPINGS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
manifest={'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}}
(OUT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
print(sha((OUT/'MANIFEST.json').read_bytes()))
