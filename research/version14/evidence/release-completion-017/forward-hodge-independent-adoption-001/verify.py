from pathlib import Path
import json,hashlib,sys,copy
R=Path(__file__).resolve().parents[3]
O=Path(__file__).resolve().parent
D=R/'work/source-risk-review-20261107'
A=D/'combined005-forward-hodge-author-sol-004'
P=D/'combined005-forward-hodge-author-sol-002'
h=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
checks=[]
pins=[]
def ck(n,v):
 assert v,n
 checks.append(n)
def pin(p,expected=None):
 b=p.read_bytes();v=h(b)
 if expected:ck('hash '+str(p.relative_to(R)),v==expected)
 pins.append({'path':p.relative_to(R).as_posix(),'sha256':v})
 return v
for name,want in [('002','4f41fbbe5c6bc8285348b091509530c9801a792f07cbde7a0c8b67df7150ba90'),('003','4b6d68cd68e0702339f31604ac7efc09a10a9dc55040ed65429a075d59fdcecf'),('004','d79f061f30cd9f424020d71c7f28def3e6ac545b17c97cc43aeb947258d2d6ff')]:
 p=D/('combined005-forward-hodge-author-sol-'+name)/'MANIFEST.json';pin(p,want)
 for x in read(p)['files']:pin(R/x['path'],x['sha256'])
for x in read(A/'INPUTS.json'):pin(R/x['path'],x['sha256'])
for x in read(A/'SOURCE-PROVENANCE.json'):pin(R/x['original']['path'],x['original']['sha256'])
pin(D/'milne-hodge-published-author-001/local-only/milne2005-svi-final.pdf','6336f0a23084dc0bf815a901c61a0f925dbc8dc1c395af8864c1d90bea69c4a1')
for folder in ['forward-rank-current-review-001','hodge-centralizer-current-review-001']:
 p=R/'work/quartic-v14-prep/independent-source-review'/folder/'MANIFEST.json'
 for x in read(p)['files']:
  q=R/x['path'] if x['path'].startswith('work/') else p.parent/x['path']
  pin(q,x['sha256'])
passive=A/'proposed-repository/research/version14/source-adoption-ordinary-v1/reviews/milne.md'
origin=D/'milne-hodge-published-review-gaussian-001/REVIEW.md'
ck('passive Milne review verbatim',passive.read_bytes()==origin.read_bytes());pin(origin)
sp='proposed-repository/research/version14/proofs/forward-rank-hodge-v1/SOURCE-STATEMENTS.md'
oldsource=(P/sp).read_bytes();newsource=(A/sp).read_bytes()
oldphrase='the elliptic identity identifies its degree-zero Picard variety with the elliptic curve.'
newphrase='the elliptic identity identifies its degree-zero divisor-class group with the elliptic curve.'
ck('one raw source correction only',oldsource.replace(oldphrase.encode(),newphrase.encode())==newsource and oldsource.count(oldphrase.encode())==1)
repl={oldphrase:newphrase,h(oldsource):h(newsource),h(oldsource.splitlines(keepends=True)[18]):h(newsource.splitlines(keepends=True)[18]),
'Divisors under finite maps of smooth projective curves and Pic0 of an elliptic curve with identity.':'Degree-zero divisor classes under finite maps of smooth projective curves and the elliptic identity.',
'The finite curve-map divisor identity and elliptic Picard identification.':'The finite curve-map divisor identity and the elliptic degree-zero divisor-class group identification.'}
removed='CURRENT-HODGE-TORSION-DESCENT-FROM-CURRENT-MILNE-CAV-HODGE'
def replace(x):
 if isinstance(x,str):
  for a,b in repl.items():x=x.replace(a,b)
  return x
 if isinstance(x,list):return [replace(v) for v in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
olduses=read(P/'USES.json')
expecteduses=replace([u for u in olduses if u['id']!=removed])
ck('uses exact correction replay',expecteduses==read(A/'USES.json'))
canonical=lambda x:h(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
newby={u['id']:u for u in expecteduses}
for u in olduses:
 if u['id']!=removed:repl[canonical(u)]=canonical(newby[u['id']])
for n in ['APPLICATIONS.json','CONNECTIONS.json','INDEX.json','EDGES.json']:
 x=replace(read(P/n))
 if n=='APPLICATIONS.json':
  for a in x:
   if a['id']=='CURRENT-HODGE-TORSION-DESCENT':a['dependencies']=[]
   if a['id']=='CURRENT-MILNE-CAV-HODGE':
    q=a['obligations']['downstream_consumption']
    q['required']='Supply the rational Hodge/algebraic quasi-endomorphism equality atcombined005 lines 1427–1430 (ed992 predecessor lines 883–886).'
    q['constructed']='The equality is used beforecombined005 lines 1431–1440 (ed992 predecessor lines 887–896).'
 elif n=='CONNECTIONS.json':x=[a for a in x if a['use_id']!=removed]
 elif n=='INDEX.json':x=[a for a in x if a['id']!=removed+'-P']
 elif n=='EDGES.json':x=[a for a in x if removed not in a['use_ids']]
 ck('exact agreed delta '+n,x==read(A/n))
ck('local proof unchanged', (P/'CONNECTIONS.md').read_bytes()==(A/'CONNECTIONS.md').read_bytes())
ck('passive source projection unchanged',(P/'proposed-repository/research/version14/source-adoption-ordinary-v1/source-statements/MILNE.md').read_bytes()==(A/'proposed-repository/research/version14/source-adoption-ordinary-v1/source-statements/MILNE.md').read_bytes())
apps=read(A/'APPLICATIONS.json');U={x['id']:x for x in read(A/'USES.json')};I={x['id']:x for x in read(A/'INDEX.json')};C={x['use_id']:x for x in read(A/'CONNECTIONS.json')}
ck('all72 statuses retained',sum(len(a['obligations']) for a in apps)==72 and all(v['status']=='unresolved' for a in apps for v in a['obligations'].values()))
for c in C.values():ck('canonical '+c['use_id'],c['use_sha256']==canonical(U[c['use_id']]))
def resolve(s):
 return R/'work/quartic-v14-combined-20261108-005/candidate'/s if s=='manuscripts/quartic_v14.tex' else A/'proposed-repository'/s
def walk(x):
 if isinstance(x,dict):
  if {'side','path','sha256'}<=set(x):ck('head pin '+x['path'],h(resolve(x['path']).read_bytes())==x['sha256'])
  if {'pin','start_line','end_line','excerpt_sha256'}<=set(x):
   b=resolve(x['pin']['path']).read_bytes().splitlines(keepends=True)
   ck('span '+x['pin']['path']+':'+str(x['start_line']),h(b''.join(b[x['start_line']-1:x['end_line']]))==x['excerpt_sha256'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
for n in ['APPLICATIONS.json','USES.json','CONNECTIONS.json','INDEX.json','SOURCE-PROVENANCE.json','TRANSPORT.json','ROLE-AUDIT.json','FRONTIER.json','PICARD-REVIEW-DELTA.json']:walk(read(A/n))
deps={a['id']:a['dependencies'] for a in apps}
def visit(a,stack):
 ck('acyclic '+a,a not in stack)
 for d in deps[a]:visit(d,stack+[a])
for a in deps:visit(a,[])
for a in apps:ck('actual dependencies '+a['id'],set(a['dependencies'])=={u['supplier']['application_id'] for u in U.values() if u['consumer']==a['id'] and u['supplier']['kind']=='internal'})
for u in U.values():
 for i in u['passages']:ck('use backref '+u['id'],u['id'] in I[i]['use_ids'])
for i in I.values():
 for u in i['use_ids']:ck('index backref '+i['id'],i['id'] in U[u]['passages'])
ck('both centralizer inputs retained',set(deps['CURRENT-HODGE-QUATERNION-CENTRALIZER'])=={'CURRENT-HODGE-TORSION-DESCENT','CURRENT-MILNE-CAV-HODGE'})
q=O/'CHECKS-004.json';ck('prior full current check passed',read(q)['summary']['errors']==[] and read(q)['summary']['checks_passed']==614)
pin(R/'work/protocol-v14-20261107/docs-author/source/mathematical-research-review-protocol-v1.4.md','3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9')
if (O/'MANIFEST.json').exists():
 for x in read(O/'MANIFEST.json')['files']:ck('review member '+x['path'],h((O/x['path']).read_bytes())==x['sha256'])
result={'status':'passed','checks':len(checks),'input_pins':list({x['path']:x for x in pins}.values()),'comparison':'Exact agreed replay from002 to004; no other core record changes','statuses_retained':72,'checks_detail':checks}
if '--record' in sys.argv:
 p=O/'FINAL-CHECKS.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'passed','checks':len(checks),'statuses_retained':72,'comparison':result['comparison']}))
