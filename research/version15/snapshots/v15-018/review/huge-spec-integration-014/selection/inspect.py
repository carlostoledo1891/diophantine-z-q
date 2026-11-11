from pathlib import Path
import json,hashlib,re
B=Path.cwd();S=B/'work/quartic-v14-release/preview-repository';C=S/'construction';O=B/'work/v15-huge-spec-selection-001'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((C/'SOURCE_MANIFEST.json').read_bytes());graph={};external=set();rows=[]
for r in m['files']:
 p=C/r['file'];actual=h(p)
 rows.append({'source':str(p),'destination':'construction/'+r['file'],'sha256':actual,'bytes':p.stat().st_size,'manifest_expected_sha256':r['release_sha256'],'matches_source_manifest':actual==r['release_sha256'],'original_path':r['original_path'],'original_sha256':r['original_sha256'],'portability_change':r.get('change')})
 if p.suffix=='.js':
  deps=re.findall(r'''require\(["']([^"']+)["']\)''',p.read_text())
  graph[p.name]=[d[2:] for d in deps if d.startswith('./')]
  external.update(d for d in deps if not d.startswith('./'))
for src in ['construction/SOURCE_MANIFEST.json','scripts/check_construction.py']:
 p=S/src;rows.append({'source':str(p),'destination':src,'sha256':h(p),'bytes':p.stat().st_size,'role':'unchanged supported-check entry point or exact curated-input manifest'})
closure=set();pending=['ordinary-integer-polynomial.js']
while pending:
 x=pending.pop()
 if x in closure:continue
 closure.add(x);pending.extend(graph.get(x,[]))
assert all((C/x).exists() for x in closure)
obj={'source_root':str(S),'scope':'Proposal only; no destination copied or modified','recommended_distribution':rows,'generator_javascript_closure':sorted(closure),'generator_data_inputs':['precision-natural-polynomial.json'],'generator_reference_output':'ordinary-integer-definition.json','local_require_graph':graph,'builtin_requires':sorted(external),'total_files':len(rows),'total_bytes':sum(r['bytes'] for r in rows),'manifest_mismatches':[r['destination'] for r in rows if r.get('matches_source_manifest') is False]}
(O/'SELECTION.json').write_text(json.dumps(obj,indent=2)+'\n');print({k:obj[k] for k in ['total_files','total_bytes','generator_javascript_closure','builtin_requires','manifest_mismatches']})
