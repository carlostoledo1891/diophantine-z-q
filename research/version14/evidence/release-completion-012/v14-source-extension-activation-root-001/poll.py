from pathlib import Path
import importlib.util,json,datetime
W=Path.cwd();O=W/'work/source-risk-review-20261107/v14-source-extension-activation-root-001'
s=importlib.util.spec_from_file_location('gh',W/'work/quartic-version7-release/github.py');g=importlib.util.module_from_spec(s);s.loader.exec_module(g);t=g.token()
repo='/repos/elliotglazer/research-review-controller';head='d135affeb727346e9d36d08d34874bae1e76cc76';activation=json.loads((O/'ACTIVATION.json').read_bytes())
r=g.request(repo+'/actions/workflows/protocol-controller.yml/runs?head_sha='+head+'&per_page=10',t)
runs=[x for x in r['workflow_runs'] if x['event']=='workflow_dispatch' and x['head_sha']==head]
out={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'approved_sha':g.request(repo+'/actions/variables/PROTOCOL_APPROVED_SHA',t)['value'],'runs':[]}
for x in runs:
 jobs=g.request(repo+'/actions/runs/'+str(x['id'])+'/jobs?per_page=100',t)['jobs']
 out['runs'].append({'id':x['id'],'created_at':x['created_at'],'status':x['status'],'conclusion':x['conclusion'],'url':x['html_url'],'jobs':[{'id':j['id'],'name':j['name'],'status':j['status'],'conclusion':j['conclusion'],'steps':[{'name':z['name'],'conclusion':z['conclusion']} for z in j['steps']]} for j in jobs]})
(O/'RUN-OBSERVATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
