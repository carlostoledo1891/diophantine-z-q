from pathlib import Path
import json,hashlib,shutil
R=Path('work/source-risk-review-20261107'); A=R/'v14-cj-igusa-source-index-author-003'; O=R/'v14-cj-igusa-source-index-author-004'
def sha(x):return hashlib.sha256(x).hexdigest()
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def wr(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for p in A.iterdir():
 if p.is_file() and p.name not in ['MANIFEST.json','revise.py']:shutil.copyfile(p,O/p.name)
index=rd(A/'INDEX.json'); pending=rd(A/'PENDING.json'); roles=rd(A/'SOURCE-ROLES.json')
changes={
 'SRC-CJ-IGUSA-136':(['ACTIVE-CJ-LOCAL-DIVISION-INPUT'],'The accepted local division input supplies the cyclic presentation, maximal-order residue and unit/uniformizer action. The two labelled classes and norm parity are the ensuing local classification; no global geometric realization is inferred.'),
 'SRC-CJ-IGUSA-138':(['ACTIVE-CJ-CONJUGACY-INPUT','ACTIVE-CJ-CENTRALIZER-INPUT'],'The accepted specified-embedding conjugacy and pointwise centralizer inputs supply the two imported assertions. The adelic representative statement then consumes the preceding fixed-tuple local calculations; it does not quotient by the larger normalizer.')}
for p in pending:
 if p['id'] in changes:
  ids,reason=changes[p['id']]
  index.append(dict(id=p['id'],claim_ids=['V14-MAIN-POLYNOMIAL-DEFINITION'],location=p['location'],status='reviewed',reason=reason,use_ids=ids,no_imports_reason=None))
  for row in roles:
   if row['id']==p['id']:row.update(role='import_and_local_derivation',source_binding_use_ids=ids,reason=reason)
index.sort(key=lambda x:x['id'])
wr('INDEX.json',index);wr('SOURCE-ROLES.json',roles);wr('PENDING.json',[p for p in pending if p['id'] not in changes])
components=rd(R/'v14-cj-local-structure-author-001/COMPONENTS.json')
links=[]
for rowid,(ids,reason) in changes.items():
 for uid in ids:
  c=next(c for c in components if c['use']['id']==uid)
  loc=next(p['location'] for p in pending if p['id']==rowid)
  assert loc in c['connection']['consumer_locations']
  links.append(dict(index_id=rowid,use_id=uid,use_sha256=c['connection']['use_sha256'],exact_existing_consumer_location=loc,reason=reason))
wr('ADDITIONAL-BINDINGS.json',dict(bindings=links,source_review='v14-final-composite-review-001/CJ-LOCAL-FOUR-MATHEMATICAL-REVIEW.json',source_review_sha256='2955b7d281ab32e90e683b9acbfd7b77eea80e54b6bc453fa6daeb0a276bcb65',scope='Only two formerly pending rows; no new consumer locations or theorem claims.'))
wr('DELTA004.json',dict(added_classified_rows=list(changes),remaining_pending_rows=[p['id'] for p in pending if p['id'] not in changes],acceptance='Author proposal pending independent index comparison'))
wr('MANIFEST.json',dict(files={p.name:dict(sha256=sha(p.read_bytes()),bytes=p.stat().st_size) for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}))
print(sha((O/'MANIFEST.json').read_bytes()))
