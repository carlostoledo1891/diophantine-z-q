from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[3]
D=B/'work/source-risk-review-20261107/a007-a011-current-projection-theta-002'
P=B/'work/source-risk-review-20261107/a007-a011-current-projection-theta-001'
OUT=Path(__file__).resolve().parent
H=lambda x:hashlib.sha256(x).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
checks=[]
def ck(n,v):
 checks.append({'check':n,'pass':bool(v)})
 if not v: print('FAILED',n)
def hp(p):return H(p.read_bytes())
ck('target manifest',hp(D/'MANIFEST.json')=='2378239b4e43a9648ba0fd6f37e4c8fdc2185f0317aad531e6c4b933f1fb2393')
ck('predecessor manifest',hp(P/'MANIFEST.json')=='c857f8276d6c56f67ba1a88f635f46542135b1593199c31be73035bbdc1aca3e')
pinpaths={}
for folder in [D,P]:
 for r in read(folder/'MANIFEST.json')['files']:
  p=folder/r['path'];ck('member '+str(p.relative_to(B)),hp(p)==r['sha256']);pinpaths.setdefault(r['sha256'],p)
for r in read(D/'INPUTS.json'):
 p=B/r['path'];ck('input '+r['path'],hp(p)==r['sha256']);pinpaths.setdefault(r['sha256'],p)
for r in read(D/'SOURCE-PINS.json'):
 p=B/r['primary']['path'];ck('published pin '+r['id'],hp(p)==r['primary']['sha256'])
for name,origin in [('INHERITED-APPLICATIONS.json','a007-a011-current-anchor-001/APPLICATIONS.json'),('INHERITED-ASSERTIONS.json','a007-a011-current-anchor-002/ASSERTIONS.json'),('INHERITED-SOURCE-COMPARISONS.json','a007-a011-current-anchor-002/SOURCE-TO-APPLICATIONS.json'),('SOURCE-PINS.json','a007-a011-current-anchor-001/SOURCE-PINS.json')]:
 ck('inherited '+name,(D/name).read_bytes()==(B/'work/source-risk-review-20261107'/origin).read_bytes())
apps=read(D/'APPLICATIONS.json');old={r['id']:r for r in read(D/'INHERITED-APPLICATIONS.json')}
ck('six applications',len(apps)==len(old)==6)
for r in apps:
 a=old[r['id']];ck('nine fields '+r['id'],len(r['obligations'])==9 and set(r['obligations'])==set(a['obligations']))
 for k,v in r['obligations'].items():
  ck('preserved comparison '+r['id']+'/'+k,all(v[t]==a['obligations'][k][t] for t in ['required','constructed']))
uses=read(D/'USES.json');cons=read(D/'CONNECTIONS.json');idx=read(D/'INDEX.json')
ck('14 use connections index',len(uses)==len(cons)==len(idx)==14)
ck('unique use IDs',len({r['id'] for r in uses})==14)
cm={r['use_id']:r for r in cons};im={r['id']:r for r in idx}
role_summaries=[]
for u in uses:
 c=cm[u['id']];supplier=u['supplier'];internal=supplier['kind']!='published_external'
 candidates=[json.dumps(u,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode(),json.dumps(u,ensure_ascii=False,sort_keys=True).encode()]
 ck('use hash '+u['id'],c['use_sha256'] in [H(x) for x in candidates])
 ck('needed assertion '+u['id'],c['needed_assertion']==u['assertion'])
 ck('supplied equals needed '+u['id'],c['available_assertion']==c['needed_assertion'])
 ck('capability inclusion '+u['id'],set(c['required_capabilities'])<=set(c['available_capabilities']))
 ck('no derived capability '+u['id'],c['derived_capabilities']==[])
 ck('source role '+u['id'],c['supplier_passage_role']==('proof' if internal else 'statement'))
 for iid in u['passages']:
  ck('index use '+iid,u['id'] in im[iid]['use_ids'] and u['consumer'] in im[iid]['claim_ids'])
 ck('application consumer '+u['id'],u['application_id']==u['consumer'] and u['consumer'] in old)
 role_summaries.append({'id':u['id'],'consumer':u['consumer'],'kind':supplier['kind'],'supplier_application':supplier.get('application_id'),'statement':u['assertion']['statement'],'proof_range':[c['connecting_derivation']['location']['start_line'],c['connecting_derivation']['location']['end_line']],'role':c['supplier_passage_role']})
pub=[u for u in uses if u['supplier']['kind']=='published_external']
ck('ten published imports',len(pub)==10)
ck('C6 active Emerton',any('EMERTON' in u['id'] and u['consumer']=='CURRENT-A011-TATE-CONDUCTOR' for u in pub))
ck('C5 no manufactured Tate imports',all(u['consumer']!='CURRENT-A011-SHIMURA-QUOTIENT' for u in pub if any(z in u['id'] for z in ['EMERTON','FALTINGS','SERRE'])))
edges={(u['supplier'].get('application_id'),u['consumer']) for u in uses if u['supplier']['kind']!='published_external'}
expect={('CURRENT-A007-SQUARE-BOUNDARY','CURRENT-A007-GLOBAL-SPLITTING'),('CURRENT-A007-GLOBAL-SPLITTING','CURRENT-A007-RAMIFICATION'),('CURRENT-A011-FRICKE-SPAN','CURRENT-A011-SHIMURA-QUOTIENT'),('CURRENT-A011-SHIMURA-QUOTIENT','CURRENT-A011-TATE-CONDUCTOR')}
ck('four exact internal edges',edges==expect)
for a in apps:ck('dependency graph '+a['id'],set(a['dependencies'])=={x for x,y in expect if y==a['id']})
locations={};headpins={}
def walk(x):
 if isinstance(x,dict):
  if 'pin' in x and all(k in x for k in ['start_line','end_line','excerpt_sha256']):
   locations[json.dumps(x,sort_keys=True)]=x
  if x.get('side')=='head' and 'path' in x and 'sha256' in x:headpins[(x['path'],x['sha256'])]=x
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
for f in D.glob('*.json'):walk(read(f))
for logical,sha in headpins:
 ck('head pin '+logical+' '+sha[:8],sha in pinpaths and hp(pinpaths[sha])==sha)
for n,l in enumerate(locations.values()):
 p=pinpaths.get(l['pin']['sha256'])
 good=p is not None and 1<=l['start_line']<=l['end_line']
 if good:
  lines=p.read_bytes().splitlines(keepends=True)
  good=l['end_line']<=len(lines) and H(b''.join(lines[l['start_line']-1:l['end_line']]))==l['excerpt_sha256']
 ck('unique raw location '+str(n),good)
delta=read(D/'TRANSPORT-DELTA.json')
p6=B/'work/quartic-v14-combined-20261108-006/candidate/manuscripts/quartic_v14.tex'
p7=B/'work/quartic-v14-combined-20261108-007/candidate/manuscripts/quartic_v14.tex'
v6=p6.read_bytes();v7=p7.read_bytes();off=delta['byte_offset'];before=delta['before'].encode();after=delta['after'].encode()
ck('sole source spelling replay',v6[off:off+len(before)]==before and v6[:off]+after+v6[off+len(before):]==v7)
ck('inverse source replay',v7[:off]+before+v7[off+len(after):]==v6)
ck('source line549',v6[:off].count(b'\n')+1==549)
for f in delta['byte_identical_files']:ck('unchanged projection '+f,(D/f).read_bytes()==(P/f).read_bytes())
for f in delta['target_binding_only_files']:
 a=(P/f).read_bytes().replace(delta['previous_target_sha256'].encode(),delta['current_target_sha256'].encode())
 ck('hash-only retarget '+f,a==(D/f).read_bytes())
for r in read(D/'SOURCE-MAP.json'):
 src=B/r['source'] if r['source'].startswith('work/') else D/r['source']
 dst=D/'proposed-repository'/r['path']
 ck('source payload '+r['path'],hp(src)==r['sha256'] and src.read_bytes()==dst.read_bytes())
owners=read(D/'OWNER-REPLACEMENTS.json');cards={r['id']:r for r in read(B/'work/source-risk-review-20261107/pan-calegari-direct-author-001/SOURCE-APPLICATIONS.json')}
ck('two distinct owners',{r['owner'] for r in owners}=={'QM-FIRST-MODULARITY-APPLICATION','QM-SECOND-MODULARITY-APPLICATION'})
for r in owners:
 ck('exact accepted caller card '+r['owner'],r['accepted_source_card']==cards[r['accepted_source_card']['id']])
 for s in r['reviews']:
  ck('owner review '+r['owner']+s['manifest'],hp(B/s['manifest'])==s['manifest_sha256'] and hp(B/s['review'])==s['review_sha256'])
occ=read(D/'APPLICATION-OCCURRENCES.json')
ck('twelve occurrences',len(occ)==12)
ck('root occurrences retained',read(D/'ROOT-ATTACHMENTS.json')['occurrences']==occ)
ck('root attachment stays pending',read(D/'ROOT-ATTACHMENTS.json')['status']=='pending whole-root association')
result={'checks':len(checks),'passed':sum(r['pass'] for r in checks),'failed':[r['check'] for r in checks if not r['pass']],'unique_locations':len(locations),'head_pins':len(headpins),'role_summaries':role_summaries,'checks_detail':checks}
out=OUT/'MECHANICAL-CHECKS.json'
assert not out.exists(),'Refusing overwrite'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks_detail'},indent=2))

