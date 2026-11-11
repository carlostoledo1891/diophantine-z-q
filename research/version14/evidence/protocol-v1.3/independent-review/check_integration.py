from pathlib import Path
import json,hashlib,subprocess,ast
root=Path.cwd(); p=root/'work/protocol-v13-20261107/integration-author'; tree=p/'tree';m=json.loads((p/'MANIFEST.json').read_bytes());i=json.loads((p/'INTEGRATION.json').read_bytes());b=json.loads((tree/'deployment-bundle/BUNDLE-MANIFEST.json').read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in m['files'].items():assert sha(p/n)==h,n
for n,r in i['accepted_overlays'].items():assert sha(tree/n)==r['sha256'] and sha(root/r['source'])==r['sha256'],n
for n,r in i['baseline_files'].items():
 if n not in i['accepted_overlays']:assert sha(tree/n)==r['sha256'],n
for n,r in b['files'].items():assert sha(tree/'deployment-bundle'/n)==r['sha256'],n
assert b['production_edges']==i['production_edges'];assert b['test_edges']==i['test_edges'];assert not b['protected_config_present']
print('hashes passed',len(i['baseline_files']),len(i['accepted_overlays']),len(i['production_files']),len(b['files']))
print('newproduction',sorted(set(i['production_files'])-set(json.loads((root/'work/protocol-ruleset-20261107/deployment-repository/BUNDLE-MANIFEST.json').read_bytes())['production_edges'])))
