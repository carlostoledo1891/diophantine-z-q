from pathlib import Path
import argparse,base64,datetime,hashlib,importlib.util,json
p=argparse.ArgumentParser();p.add_argument('--activate',action='store_true');a=p.parse_args()
W=Path.cwd();O=W/'work/source-risk-review-20261107/v14-source-extension-activation-root-001'
s=importlib.util.spec_from_file_location('gh',W/'work/quartic-version7-release/github.py');g=importlib.util.module_from_spec(s);s.loader.exec_module(g);t=g.token()
repo='elliotglazer/research-review-controller';head='d135affeb727346e9d36d08d34874bae1e76cc76';base='/repos/'+repo
ref=g.request(base+'/git/ref/heads/main',t);assert ref['object']['sha']==head,'remote head differs'
spec=json.loads((W/'work/source-risk-review-20261107/v14-source-extensions-rollout-author-002/TARGETS.json').read_bytes())
checked=[]
for r in spec['files']+spec['unchanged_pins']:
 v=g.request(base+'/contents/'+r['path']+'?ref='+head,t);raw=base64.b64decode(v['content']);h=hashlib.sha256(raw).hexdigest();expected=r.get('after_sha256',r.get('sha256'));assert h==expected,r['path'];checked.append({'path':r['path'],'sha256':h})
v=g.request(base+'/actions/variables/PROTOCOL_APPROVED_SHA',t);old=v['value'];assert old in (spec['baseline_commit'],head),'unexpected existing approval'
receipt={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'remote_files':checked,'approval_before':old,'activated':False}
if a.activate:
 if old!=head:g.request(base+'/actions/variables/PROTOCOL_APPROVED_SHA',t,'PATCH',{'name':'PROTOCOL_APPROVED_SHA','value':head})
 assert g.request(base+'/actions/variables/PROTOCOL_APPROVED_SHA',t)['value']==head
 receipt['approval_after']=head;receipt['dispatch_requested_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 g.request(base+'/actions/workflows/protocol-controller.yml/dispatches',t,'POST',{'ref':'main'})
 receipt['activated']=True
name='ACTIVATION.json' if a.activate else 'REMOTE-READBACK.json';(O/name).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'head':head,'files_verified':len(checked),'approval_before':old,'activated':receipt['activated']}))
