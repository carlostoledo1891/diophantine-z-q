import json,pathlib,hashlib,collections
D=pathlib.Path(__file__).resolve().parent;ROOT=D.parents[2];R=ROOT/'work/source-risk-review-20261107';S=R/'v14-release-increment-author-018';REPO=ROOT/'work/quartic-v14-release/preview-repository'
sha=lambda b:hashlib.sha256(b).hexdigest(); canon=lambda o:json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def read(p):return json.loads(p.read_bytes())
def save(n,o):(D/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
sel=read(S/'SELECTION.json');mapping=read(S/'WHITELIST.json')['files'];loc={x['path']:ROOT/x['source']for x in mapping};byhash=collections.defaultdict(list)
for n,h in sel.items():byhash[h].append(n)
def pin(p,ptr=None):
 b=p.read_bytes();h=sha(b);names=byhash.get(h,[])
 assert names,str(p)
 q={'path':names[0],'sha256':h,'bytes':len(b)}
 if ptr is not None:q['json_pointer']=ptr
 return q
scan=read(D/'EXPLICIT-FINDINGS-SCAN.json')['rows'];records=[];seen=set()
for x in scan:
 ident=x['id'];group=None
 if ident.startswith(('DF-F','MF-F','LP05-F','S13-F'))or ident=='GTZ-LP-VECTOR-SCALAR-SHIFT':group='historical_GI_named_objection'
 elif ident.startswith('MILNE-M'):group='superseded_source_metadata_objection'
 elif ident.startswith('GAU-'):group='historical_Gaussian_source_or_coverage_obligation'
 elif ident.startswith('FH-'):group='superseded_adoption_objection'
 elif ident in ['V12-SERIALIZATION','DOCS-1','SETUP-1','SETUP-2','SETUP-3']:group='historical_protocol_finding'
 if not group:continue
 key=(ident,x['object_sha256'])
 if key in seen:continue
 seen.add(key);body=x['body'];field=next((k for k in ['issue','failure','finding','detail','available_vs_needed_difference','reason','resolution_required','history']if isinstance(body.get(k),str)),None)
 rec={'finding_id':ident,'classification':group,'original_location':{'path':x['selected_file'],'sha256':x['file_sha256'],'json_pointer':x['json_pointer']},'original_object_sha256':x['object_sha256'],'original_object':body,'original_status':x['status'],'body_field':field,'body_sha256':sha(body[field].encode())if field else body.get('body_sha256'),'body_hash_rule':'UTF8 exact named string field; supplied original body_sha256 retained when no body text','recorded_authors':body.get('authors'),'recorded_applications':body.get('applications',body.get('application')),'recorded_related_use_ids':body.get('use_ids',body.get('related_use_ids')),'current_disposition':None,'current_disposition_evidence':[],'uncertainty':None}
 if group=='historical_GI_named_objection':
  rec['uncertainty']='No exact final finding-ID disposition located. Accepted current GI module/flow reviews are available, but are not automatically a disposition of this historical ID or proof that its old open status persists.'
 elif ident.startswith('MILNE-'):
  rec['current_disposition']='Explicitly resolved on R3 at bounded source scope; rejected original claims remain historical.';rec['current_disposition_evidence']=[pin(R/'milne-review/DECISION.json'),pin(R/'milne-review/FINDINGS.json','/findings/'+str(int(ident[-2:])-1))]
 elif ident.startswith('FH-'):
  rec['current_disposition']='Explicitly resolved in independently accepted author004.';rec['current_disposition_evidence']=[pin(R/'forward-hodge-independent-adoption-001/DECISION.json','/resolved_findings'),pin(R/'forward-hodge-independent-adoption-001/REVIEW.md')]
 elif ident.startswith('GAU-'):
  rec['current_disposition']='Original supplement records resolution only'if ident=='GAU-PROSE-DIRECT-USES'else None;rec['uncertainty']='No exact later ID-level disposition verified; later Gaussian clause reviews must not be treated as automatic ID closure.'
 else:
  rec['current_disposition']='Recorded historical packet status only: '+str(body.get('status'));rec['current_disposition_evidence']=[rec['original_location']];rec['uncertainty']='Historical protocol packet, not a current mathematical finding. Its body hash/authors are retained as recorded, not newly authenticated or assigned to a current application.'
 records.append(rec)
p=R/'forward-hodge-independent-adoption-001/DECISION.json';j=read(p)
records.append({'finding_id':'FH-003','classification':'superseded_adoption_objection','original_location':pin(p,'/resolved_findings/2'),'body_sha256':sha(j['resolved_findings'][2].encode()),'body_hash_rule':'UTF8 exact resolved_findings[2] summary; original standalone finding body not located','original_status':None,'current_disposition':'Explicitly resolved on author004: old current narrative line references corrected; structured pins already current.','current_disposition_evidence':[pin(p),pin(R/'forward-hodge-independent-adoption-001/REVIEW.md')],'recorded_authors':None,'recorded_applications':j['applications'],'uncertainty':'No standalone earlier FH-003 finding object located; do not substitute this later summary for an authenticated original body.'})
code=[]
for topic,rel,paragraph in [('Lean cache retry classifier','v14-ci-cache-retry-review-root-001/REVIEW.md',3),('Tectonic download retry','v14-build-download-retry-independent-001/REVIEW.md',1)]:
 p=R/rel;text=p.read_text();parts=text.split('\n\n');body=parts[paragraph]
 code.append({'finding_id':None,'topic':topic,'original_location':pin(p),'body':body,'body_sha256':sha(body.encode()),'body_hash_rule':'UTF8 exact review paragraph after universal newline decoding','original_status':None,'current_disposition':'Explicit bounded code repair accepted by this independent review; no mathematical or final CI approval inferred.','current_disposition_evidence':[pin(p)],'uncertainty':'No historical stable finding ID in this review; do not invent one or reuse a mathematical ID.','recorded_authors':None})
respath=R/'v14-sign-pending-resolution-002/RESOLUTION.json';res=read(respath);attribute=[]
for i,x in enumerate(res['rows']):attribute.append({'id':x['original']['id'],'kind':'source_attribution_obligation_not_automatically_mathematical_error','original':x['original'],'original_object_sha256':x['original_sha256'],'source':pin(respath,'/rows/'+str(i)),'disposition':x['disposition'],'reason':x['role_note'],'accepted_evidence':x['accepted_evidence'],'resolution_artifacts':x['resolution_artifacts'],'consolidation_review':pin(R/'v14-sign-pending-resolution-002/REVIEW-GI.json'),'residual':x['residual']})
meta=[]
for x in scan:
 if x['id'].startswith('ACTIVE-THETA-STACKS-'):
  meta.append({'id':x['id'],'source':{'path':x['selected_file'],'sha256':x['file_sha256'],'json_pointer':x['json_pointer']},'classification':'historical_reviewer_snapshot_lookup_not_mathematical_objection','original_status':x['status'],'later_evidence':pin(R/'v14-arithmetic-range13256-review-001/FIRST-SLICE-002-REVIEW.json'),'reason':'Later review accepted corrected first slice after exact source packet lookup; do not turn baseline-not-found into a current missing theorem.'})
save('NAMED-FINDINGS.json',{'selection_sha256':sha((S/'SELECTION.json').read_bytes()),'records':records,'code_findings_without_stable_ids':code})
save('SOURCE-ATTRIBUTION-RESOLUTIONS.json',attribute);save('HISTORICAL-STATUS-DISPOSITIONS.json',meta)
summary={'distinct_finding_ids':len(set(x['finding_id'] for x in records)),'named_records':len(records),'groups':dict(collections.Counter(x['classification']for x in records)),'code_topics_without_ids':len(code),'source_attribution_obligations':len(attribute),'historical_lookup_records':len(meta),'priority_scan_objects':355,'explicit_key_scan_objects':len(scan),'limitations':['Canonical Issue2/Issue3 and F001-F008 deliberately left to integration.','No new mathematical review, authenticated authorship, or final schema2 status assigned.','28 GI IDs and four Gaussian IDs lack verified later ID-level reconciliation here; this is a mapping limitation, not 32 newly established proof gaps.','Free-text Markdown findings not exhaustively enumerated. Only two requested code review topics and FH003 were manually added.','Related-use IDs and accepted-clause rows under a findings key are not automatically objections.','Source-first completeness review remains separately open per root.']}
save('SUMMARY.json',summary)
names=['scan.py','scan_explicit.py','build_inventory.py','SCAN.json','EXPLICIT-FINDINGS-SCAN.json','NAMED-FINDINGS.json','SOURCE-ATTRIBUTION-RESOLUTIONS.json','HISTORICAL-STATUS-DISPOSITIONS.json','SUMMARY.json']
save('MANIFEST.json',{'state':'Neutral source-pinned intake, not a final schema2 findings array','files':[dict(path=n,sha256=sha((D/n).read_bytes()),bytes=(D/n).stat().st_size)for n in names]})
print(json.dumps(dict(summary=summary,manifest_sha256=sha((D/'MANIFEST.json').read_bytes()))))

