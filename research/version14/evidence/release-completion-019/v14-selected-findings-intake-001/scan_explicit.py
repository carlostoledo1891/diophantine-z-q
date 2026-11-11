import json,pathlib,hashlib,re,collections
D=pathlib.Path(__file__).resolve().parent;ROOT=D.parents[2];R=ROOT/'work/source-risk-review-20261107';S=R/'v14-release-increment-author-018'
sel=json.loads((S/'SELECTION.json').read_bytes());mapping=json.loads((S/'WHITELIST.json').read_bytes())['files'];paths={x['path']:ROOT/x['source']for x in mapping};repo=ROOT/'work/quartic-v14-release/preview-repository'
sha=lambda b:hashlib.sha256(b).hexdigest()
counts=collections.Counter();rows=[];files=[]
for name,digest in sel.items():
 if not name.endswith('.json'):continue
 if '/docs/audit-history/issue2/'in name or '/docs/audit-history/issue3/'in name:continue
 p=paths.get(name,repo/name)
 try:b=p.read_bytes();o=json.loads(b)
 except (OSError,ValueError):continue
 if sha(b)!=digest:raise ValueError(name)
 local=[]
 def walk(x,ptr=''):
  if isinstance(x,dict):
   ident=x.get('finding_id',x.get('id'))
   if isinstance(ident,str) and ('finding_id'in x or 'finding' in ptr.lower() or ('FINDING' in name.upper() and ('status'in x or 'failure'in x or 'issue'in x))):
    if not re.fullmatch('F00[1-8]',ident):
     row=dict(id=ident,selected_file=name,file_sha256=digest,json_pointer=ptr,object_sha256=sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()),status=x.get('status'),disposition=x.get('disposition'),keys=list(x),body=x)
     local.append(row)
   for k,v in x.items():walk(v,ptr+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,ptr+'/'+str(i))
 walk(o)
 if local:rows.extend(local);files.append(dict(path=name,sha256=digest,rows=len(local)))
(D/'EXPLICIT-FINDINGS-SCAN.json').write_text(json.dumps(dict(files=files,rows=rows),indent=2)+'\n')
print(json.dumps(dict(files=len(files),rows=len(rows),summary=sorted(files,key=lambda x:-x['rows'])[:25])))
