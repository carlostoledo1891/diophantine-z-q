"""Independent R6 metadata/source binding check; no mathematical reapproval."""
from pathlib import Path
import hashlib,json,copy
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
FOLDER=HERE.with_name('resume-release-inventory-20261107-r6')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((FOLDER/n).read_bytes())
assert sha(FOLDER/'FROZEN-MANIFEST.json')=='207e7ca6cca93a79fabc19db02ee5c8d2a3d9370d0ec7f19d2847d3bb6e02ae7'
manifest=read('FROZEN-MANIFEST.json')
snapshot={p.name:sha(p) for p in FOLDER.iterdir() if p.is_file()}
assert set(snapshot)==set(manifest)|{'FROZEN-MANIFEST.json'}
for name,rec in manifest.items():assert snapshot[name]==rec['sha256'] and (FOLDER/name).stat().st_size==rec['bytes'],name
pins=read('SOURCE-PINS.json')
for name,rec in pins.items():assert sha(ROOT/name)==rec['sha256'] and (ROOT/name).stat().st_size==rec['bytes'],name
prior=read('PREVIOUS-REVISION.json')
for rec in list(prior['files'].values())+[prior['independentReview']]:assert sha(ROOT/rec['path'])==rec['sha256']
for revision,pin in [(4,'82c69afd7fbe52ba96617b6430346bc5fb77a8acf6ef7ef54c7afe4c5cb8b660'),(5,'806ebae648a51487df9661b3f4d25b3142dd3435f8e1ac0b058f554747ebbf1f')]:
 folder=FOLDER.with_name(f'resume-release-inventory-20261107-r{revision}')
 assert sha(folder/'FROZEN-MANIFEST.json')==pin
 for name,rec in json.loads((folder/'FROZEN-MANIFEST.json').read_bytes()).items():
  assert sha(folder/name)==rec['sha256'] and (folder/name).stat().st_size==rec['bytes']
def previous(n):return json.loads((ROOT/prior['files'][n]['path']).read_bytes())
a=read('APPLICATION-DELTA.json');r=read('CANONICAL-RELATION.json');m=read('INTEGRATION-MAP.json');c=read('CANDIDATES.json')
apps={x['id']:x for x in a['applications']};entries={x['id']:x for x in a['newInternalEntries']};maps={x['entryId']:x for x in m['entries']}
assert len(apps)==len(a['applications'])==39
assert len(entries)==len(a['newInternalEntries'])==len(maps)==len(m['entries'])==48
assert set(entries)==set(maps)
old=previous('APPLICATION-DELTA.json');oldapps={x['id']:x for x in old['applications']};oldentries={x['id']:x for x in old['newInternalEntries']}
assert set(apps)==set(oldapps)
for aid,app in apps.items():
 for key in ['baselineSource','baselineConsumers','baselineRecordSha256Canonical']:assert app[key]==oldapps[aid][key]
 assert len(app['newEntryIds'])==len(set(app['newEntryIds']))
for eid,entry in oldentries.items():assert entries[eid]==entry,eid
edges=[(x['applicationId'],x['entryId']) for x in r['edges']];edge_set=set(edges)
assert len(edges)==len(edge_set)
oldedges={(x['applicationId'],x['entryId']) for x in previous('CANONICAL-RELATION.json')['edges']}
assert oldedges<=edge_set
edge_objects={(x['applicationId'],x['entryId']):x for x in r['edges']}
for x in previous('CANONICAL-RELATION.json')['edges']:assert edge_objects[x['applicationId'],x['entryId']]==x
assert edge_set=={(aid,eid) for aid,x in apps.items() for eid in x['newEntryIds']}
assert edge_set=={(aid,eid) for eid,x in entries.items() for aid in x['baselineApplications']}
assert edge_set=={(x['applicationId'],eid) for eid,z in maps.items() for x in z['inventoryConsumers']}
for edge in r['edges']:
 e=entries[edge['entryId']]
 assert edge['scope']=={'selectedCandidateDependency':e['selectedCandidateDependency'],'componentIds':e.get('coveredComponentIds',[e['component']])}
 assert edge['sourceProof']==e['authorProof'] and edge['reason'].strip()
for eid,e in entries.items():
 assert not e['newApprovalCreatedHere'] and len(e['baselineApplications'])==len(set(e['baselineApplications']))
 for ref in e['authorProof']:
  p=ROOT/ref['path'];assert sha(p)==ref['sha256'];ls=p.read_text(encoding='utf-8').splitlines();lo,hi=ref['startLine'],ref['endLine']
  assert 1<=lo<=hi<=len(ls)
  if ref['heading']=='Whole report':assert (lo,hi)==(1,len(ls))
  else:assert ls[lo-1]==ref['heading']
 rev=e['recordedReview'];assert sha(ROOT/rev['path'])==rev['sha256']
 mm=maps[eid];assert mm['authorProof']==e['authorProof'] and mm['recordedNonAuthorReview']==rev
 if 'actualConsumer' in e:assert mm['actualConsumer']==e['actualConsumer']
 for use in mm['inventoryConsumers']:assert use['baselineConsumerSpans']==apps[use['applicationId']]['baselineConsumers']
 if int(eid[1:3])>=24:
  assert e['reviewer'] not in e['author'].split('+') and e['actualConsumer'] and e['arithmeticInputClassification']
components=c['components'];variants=c['polynomialVariants'];assert len(components)==40 and len(variants)==2
irs={}
for cid,obj in components.items():
 ref=obj['candidate'];assert sha(ROOT/ref['path'])==ref['sha256'];assert obj['canonicalCandidateId']=='sha256:'+ref['sha256']
 ir=json.loads((ROOT/ref['path']).read_bytes());irs[cid]=ir
 assert len(ir['coordinates'])==obj['variables'] and len(ir['residuals'])==obj['residuals']
 for key in ['coordinates','residuals']:assert len({v['id'] for v in ir[key]})==len(ir[key])
 for key in ['review','additionalReview','report','polynomial','decimalPolynomial']:
  if key in obj:assert sha(ROOT/obj[key]['path'])==obj[key]['sha256'],(cid,key)
assert len({x['canonicalCandidateId'] for x in components.values()})==40
graph={cid:set() for cid in components}
for edge in c['dependencyEdges']:
 child,parent=edge['candidate'],edge['dependsOn'];assert child in graph and parent in graph and parent not in graph[child];graph[child].add(parent)
def ancestors(cid,path=()):
 assert cid not in path,'cyclic lineage'
 return set().union(*({p}|ancestors(p,path+(cid,)) for p in graph[cid])) if graph[cid] else set()
for cid,obj in components.items():
 ancestors(cid)
 if 'objectDelta' in obj:
  parent=obj['comparedWith'];assert parent in graph[cid]
  for key in ['coordinates','residuals']:
   left={x['id']:x for x in irs[parent][key]};right={x['id']:x for x in irs[cid][key]}
   delta={'deleted':sorted(left.keys()-right.keys()),'added':sorted(right.keys()-left.keys()),'changed':sorted(i for i in left.keys()&right.keys() if left[i]!=right[i])}
   assert delta==obj['objectDelta'][key],(cid,key)
for cid,obj in variants.items():
 assert obj['kind']=='positive_weighted_compiler_variant_no_new_IR'
 parent=components[obj['residualSource']];assert obj['residualSourceCanonicalId']==parent['canonicalCandidateId']
 assert obj['canonicalPolynomialId']=='sha256:'+obj['polynomial']['sha256']
 for key in ['polynomial','weights']:assert sha(ROOT/obj[key]['path'])==obj[key]['sha256']
 table=json.loads((ROOT/obj['polynomial']['path']).read_bytes())['terms']
 assert len({tuple(t['monomial']) for t in table})==obj['monomials']
 assert obj['variables']==parent['variables'] and obj['residuals']==parent['residuals']
def check_selection(cat,app):
 objs=cat['components'];sel=objs['reciprocal299r2']
 assert cat['selectedAcceptedCandidate']=='reciprocal299r2'
 assert cat['selectedAcceptedCanonicalId']==app['selectedCandidateId']==sel['canonicalCandidateId']
 assert sel['candidate']['sha256']=='8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815'
 assert sel['review']['sha256']=='f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699'
 assert sel['additionalReview']['sha256']=='2f59aebb6074faea51a64204b734eb14a68fecdeb387541f93b86651681e0bc2'
 assert sel['equivalenceScope']=='Same rational input projection via enlarged S auxiliary domain; no private square-root-fiber bijection claimed.'
 assert sel['maximumCoefficientExpression']=='186624*C^2, C=3^(2^25)'
 assert cat['selectedOrdinaryCompanion']=='ordinaryReciprocal299_314'
 ordinary=objs['ordinaryReciprocal299_314']
 assert cat['selectedOrdinaryCanonicalId']==ordinary['canonicalCandidateId']
 assert ordinary['candidate']['sha256']=='02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7'
 assert ordinary['review']['sha256']=='13ed2acad2b751abfdb8000a931e6f93bd41b038a965f38c4c2d4902c17318db'
 assert cat['selectedOrdinaryStrictCoefficientBound']=='2^6496'
 scope=cat['ordinaryScope'];assert scope['selectedCandidateLiftIncluded'] is True
 assert scope['selectedOrdinaryCompanion']=='ordinaryReciprocal299_314' and scope['selectedStrictCoefficientBound']=='2^6496'
 assert scope==next(x for x in app['applications'] if x['id']=='V13-ORDINARY-GATE')['ordinaryArtifactScope']
 for parent,children in scope['acceptedFamilies'].items():
  assert len(children)==3
  for child in children:assert objs[child]['comparedWith']==parent
 assert set(scope['acceptedFamilies'])=={'exact319','sparseShared314','anchorGamma313','reciprocal307','reciprocal299r2'}
check_selection(c,a)
assert c['selectedAcceptedLineage']==previous('CANDIDATES.json')['selectedAcceptedLineage']+['reciprocal301','reciprocal299r2']
for cid in ['reciprocal301','reciprocal299r2','ordinaryReciprocal299_316','ordinaryReciprocal299_315','ordinaryReciprocal299_314']:
 ir=irs[cid];active={i for row in ir['residuals'] for t in row['terms'] for i in t['monomial']}
 assert active=={x['id'] for x in ir['coordinates']}
for count,rows,terms,bits in [(316,296,6678,1627),(315,295,6675,3250),(314,294,6672,6496)]:
 obj=components[f'ordinaryReciprocal299_{count}'];assert obj['comparedWith']=='reciprocal299r2'
 assert obj['variables']==count and obj['residuals']==rows and obj['monomials']==terms and obj['maximumCoefficientBits']==bits
 table=json.loads((ROOT/obj['polynomial']['path']).read_bytes())['terms']
 assert len(table)==len({tuple(t['monomial']) for t in table})==terms and all(t['sPower']==0 for t in table)
 assert max(abs(int(t['coefficient'])) for t in table).bit_length()==bits
 assert obj['objectDelta']['residuals']['changed']==[504,1903]
assert (ROOT/components['ordinaryReciprocal299_314']['decimalPolynomial']['path']).stat().st_size==222890
# Proof spans and exposition labels are metadata bindings, not proof acceptance.
outline=ROOT/m['outline']['path'];assert sha(outline)==m['outline']['sha256'];ls=outline.read_text(encoding='utf-8').splitlines()
for obj in maps.values():
 label='\\label{'+obj['outlineLabel']+'}';assert label in ls[obj['outlineLabelLine']-1] and sum(label in l for l in ls)==1
classification=read('NEW-INPUT-CLASSIFICATION.json')
for name in ['NEW-INPUT-CLASSIFICATION.json','RETAINED-SOURCES.json']:
 current=read(name)
 for key,value in previous(name).items():assert current[key]==value,(name,key)
old_alternatives=previous('PRESERVED-ALTERNATIVES.json')
assert read('PRESERVED-ALTERNATIVES.json')[:len(old_alternatives)]==old_alternatives
for item in classification['retainedArithmeticApplications']:
 ref=item['source'];p=ROOT/ref['path'];assert sha(p)==ref['sha256'];lines=p.read_text(encoding='utf-8').splitlines()
 text='\n'.join(lines[ref['startLine']-1:ref['endLine']])+'\n';assert hashlib.sha256(text.encode()).hexdigest()==ref['sha256_normalized_LF_span']
 assert set(item['newEntries'])<=set(entries)
# The rejected attempt is adverse history only, with exact literal repair.
repair=read('REPAIR-HISTORY.json')
assert repair['status']=='rejected_attempt_repaired_before_acceptance'
for key in ['failedIR','failedPolynomial','authorRejection','independentFinding','correctionNote','correctedIR','correctedPolynomial']:
 ref=repair[key];assert sha(ROOT/ref['path'])==ref['sha256']
assert repair['correctedIR']==components['reciprocal299r2']['candidate'] and repair['correctedPolynomial']==components['reciprocal299r2']['polynomial']
assert repair['finalReviews']==[components['reciprocal299r2']['review'],components['reciprocal299r2']['additionalReview']]
assert not any(x['candidate']['sha256']==repair['failedIR']['sha256'] for x in components.values())
bad=json.loads((ROOT/repair['failedIR']['path']).read_bytes());good=irs['reciprocal299r2']
active=lambda ir:{i for row in ir['residuals'] for t in row['terms'] for i in t['monomial']}
assert len(bad['coordinates'])==299 and len(active(bad))==301 and active(bad)-{x['id'] for x in bad['coordinates']}=={202,203}
br={x['id']:x for x in bad['residuals']};gr={x['id']:x for x in good['residuals']}
assert set(br)==set(gr) and {i for i in br if br[i]!=gr[i]}=={120,121,148,149}
for i in br:
 repaired=copy.deepcopy(br[i])
 if i in {120,121,148,149}:
  for t in repaired['terms']:t['monomial']=[{202:196,203:197}.get(j,j) for j in t['monomial']]
 assert repaired==gr[i]
# Own negative controls for selected metadata and fiber scope.
negative=[]
for label,mutate in [('false_fiber_bijection',lambda x:x['components']['reciprocal299r2'].update(equivalenceScope='Full private-fiber bijection')),
 ('wrong_ordinary_bound',lambda x:x.update(selectedOrdinaryStrictCoefficientBound='2^3247')),
 ('wrong_ordinary_parent',lambda x:x['components']['ordinaryReciprocal299_314'].update(comparedWith='reciprocal307')),
 ('wrong_reviewer_pin',lambda x:x['components']['reciprocal299r2']['review'].update(sha256='0'*64)),
 ('rejected_candidate_selected',lambda x:x['components']['reciprocal299r2']['candidate'].update(sha256=repair['failedIR']['sha256']))]:
 mutant=copy.deepcopy(c);mutate(mutant)
 try:check_selection(mutant,a)
 except AssertionError:negative.append(label)
 else:raise AssertionError('negative control accepted: '+label)
assert {p.name:sha(p) for p in FOLDER.iterdir() if p.is_file()}==snapshot
result={'status':'PASS','scope':'Independent structural/source-binding metadata review only; no renewed arithmetic approval',
 'manifest_sha256':sha(FOLDER/'FROZEN-MANIFEST.json'),'source_pins':len(pins),'baseline_applications':len(apps),'entries':len(entries),'canonical_edges':len(edges),
 'prior_edges_preserved':len(oldedges),'prior_entries_preserved':len(oldentries),'candidate_IRs':len(components),'polynomial_variants':len(variants),
 'selected_symbolic':'reciprocal299r2','selected_ordinary':'ordinaryReciprocal299_314','own_negative_controls':negative,'all_author_files_unchanged':True}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
