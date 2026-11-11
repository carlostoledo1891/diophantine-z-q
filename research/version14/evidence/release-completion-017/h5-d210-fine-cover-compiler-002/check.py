from pathlib import Path
import hashlib,json,sys
R=Path.cwd(); P=Path(__file__).resolve().parent
def digest(b): return hashlib.sha256(b).hexdigest()
def save(n,v): (P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pins={}; errors=[]
def walk(x,loc):
 if isinstance(x,dict):
  if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str):
   f=Path(x['path']);f=f if f.is_absolute() else R/f
   try:
    b=f.read_bytes();assert digest(b)==x['sha256']
    if 'bytes' in x: assert len(b)==x['bytes']
    if 'excerpt_sha256' in x:
     a,z=x['lines'] if 'lines' in x else (x['start_line'],x['end_line'])
     assert digest(b''.join(b.splitlines(keepends=True)[a-1:z]))==x['excerpt_sha256']
    pins[str(f.resolve())]=x['sha256']
   except Exception as e: errors.append(dict(location=loc,path=str(f),error=repr(e)))
  for k,v in x.items():walk(v,loc+'.'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,loc+'['+str(i)+']')
for f in P.glob('*.json'):
 if f.name not in ['MANIFEST.json','CHECKS.json']:walk(json.loads(f.read_text(encoding='utf-8')),f.name)
apps=json.loads((P/'APPLICATIONS.json').read_text(encoding='utf-8'));rows=json.loads((P/'OBLIGATION-COMPARISONS.json').read_text(encoding='utf-8'))
assert len(apps)==7 and len(rows)==63
want={'statement','hypotheses','objects','quantifiers','domain','normalizations','same_objects','connection','dependencies'}
for app in apps: assert {r['obligation'] for r in rows if r['application_id']==app['application_id']}==want
source_ids={s['source_id'] for s in json.loads((P/'SOURCES.json').read_text(encoding='utf-8'))}
assert all(set(a['source_ids'])<=source_ids for a in apps)
parent=R/'work/source-risk-review-20261107/h5-d210-connections-compiler-001'
def remove_target(x):
 if isinstance(x,dict):
  if x.get('application_id')=='H5-D210-TAME-MODEL' or x.get('id')=='H5-D210-TAME-MODEL':return {'application_id':'H5-D210-TAME-MODEL','removed_for_unchanged_comparison':True}
  return {k:remove_target(v) for k,v in x.items()}
 if isinstance(x,list):return [remove_target(v) for v in x]
 return x
for name in ['APPLICATIONS.json','OBLIGATION-COMPARISONS.json']:
 old=json.loads((parent/name).read_text(encoding='utf-8'));new=json.loads((P/('EFFECTIVE-PARENT-'+name)).read_text(encoding='utf-8'))
 assert remove_target(old)==remove_target(new),name
deps=json.loads((P/'DEPENDENCIES.json').read_text(encoding='utf-8')); order={x:i for i,x in enumerate(deps['order'])}
assert all(order[a]<order[b] for a,b in deps['edges'])
assert 3**4-3**2==72 and 72//2==36 and 36*2**4==576
save('CHECKS.json',dict(status='pass' if not errors else 'fail',distinct_file_pins=len(pins),applications=len(apps),obligation_comparisons=len(rows),parent_nontarget_records_unchanged=True,acyclic_declared_dependencies=True,arithmetic={'stack_degree':72,'coarse_degree':36,'normalizer_degree':576},errors=errors,scope='Byte identity, raw excerpts, declared source links, record preservation and finite arithmetic only. Not independent mathematical acceptance.'))
assert not errors,errors
if '--freeze' in sys.argv:
 assert not (P/'MANIFEST.json').exists(),'Preserve an existing freeze.'
 members=[]
 for f in sorted(P.rglob('*')):
  if f.is_file() and '__pycache__' not in f.parts and f.name!='MANIFEST.json':
   b=f.read_bytes();members.append(dict(path=f.relative_to(P).as_posix(),sha256=digest(b),bytes=len(b),public_selected=f.name in {Path(x['path']).name for x in json.loads((P/'PUBLIC-SELECTION.json').read_text(encoding='utf-8'))} and f.parent==P))
 save('MANIFEST.json',dict(packet='H5-D210-FULL-ISOMORPHISM-CONSTRUCTION-002',author='/root/astra_v14_baseline_compiler',status='author-frozen; independent review pending',proof_sha256=digest((P/'PROOF.md').read_bytes()),members=members,independent_acceptance=False,live_edits=False))
 print('MANIFEST',digest((P/'MANIFEST.json').read_bytes()),'PROOF',digest((P/'PROOF.md').read_bytes()),'MEMBERS',len(members))
print(json.dumps(json.loads((P/'CHECKS.json').read_text(encoding='utf-8')),indent=2))
