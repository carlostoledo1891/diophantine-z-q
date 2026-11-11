import ast, hashlib, json, pathlib, sys, traceback
root=pathlib.Path(sys.argv[1]); dep=pathlib.Path(sys.argv[2]); folder=pathlib.Path(sys.argv[3])
sys.path.insert(0,str(dep/'adapter'))
import offline_manifest_gate as g, coverage_gate as cv, connections_gate as cg
packet=json.loads((folder/'PACKET-CANDIDATE.json').read_text()); profile=json.loads((folder/'PROFILE.json').read_text())
apps={a['id']:a for a in packet['applications']}
repo=root/'work/quartic-v14-release/preview-repository'; overlay=folder/'overlay'
reads={}
def read_pin(pin):
 p=overlay/pin['path']
 if not p.is_file(): p=repo/pin['path']
 raw=p.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=pin['sha256']: raise g.Invalid('preflight-stale-pin:'+pin['path'])
 reads[pin['path']]=pin['sha256'];return raw
src=(dep/'adapter/coverage_gate.py').read_text()
start=src.index('    common =',src.index('def validate(')); middle=src.index("    if profile['mode'] == 'non_substantive':",start)
a=src[start:middle]
start2=src.index('    claims =',middle); end=src.index("    result = {'protocol_coverage':'1.3-substantive-records-reviewed'",start2)
b=src[start2:end]
b=b.replace('    reconstruction_identity(reconstruction, receipt, original_scope, runs,\n                            forbidden | app_agents[COVERAGE_ID], v14)\n','')
body='def structural_coverage(packet,profile,apps,read_pin):\n    app=apps[COVERAGE_ID]\n    ordinary=set(apps)-{COVERAGE_ID}\n    dossier=g.parse_json_bytes(read_pin(app["coverage_record"]),"coverage-record")\n'+a+b+'    return {"uses":len(uses),"rows":len(index),"histories":len(reconciled)}\n'
ns=dict(vars(cv));exec(compile(body,'existing-coverage-structural-excerpt','exec'),ns)
cs=(dep/'adapter/connections_gate.py').read_text();cs=cs[:cs.index('    # Report bytes are bound')]+ '    return {"connections":len(connections),"findings":len(reviews)}\n'
cn={};exec(compile(cs,'existing-connections-structural-excerpt','exec'),cn)
result={'scope':'Structural preflight only. Exact existing validator data-checking sections; authenticated identity, receipt/report checks and Git provenance are deliberately not executed. No successful gate decision is asserted.','excluded':['coverage receipt and author independence','reconstruction authenticated run continuity','connection and assembly authenticated report decisions','packet Git/change/author validation'],'validator_sha256':{n:hashlib.sha256((dep/'adapter'/n).read_bytes()).hexdigest() for n in ['coverage_gate.py','connections_gate.py']},'checks':{}}
for name,fn in [('coverage',lambda:ns['structural_coverage'](packet,profile,apps,read_pin)),('connections',lambda:cn['validate'](packet,profile,json.loads(read_pin(apps[cv.COVERAGE_ID]['coverage_record'])),apps,{},read_pin))]:
 try: result['checks'][name]={'ok':True,'result':fn()}
 except Exception as e: result['checks'][name]={'ok':False,'error':str(e),'traceback':traceback.format_exc()}
result['verified_file_count']=len(reads)
(folder/'PREFLIGHT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
