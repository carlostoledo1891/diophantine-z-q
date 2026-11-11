from pathlib import Path
import json,hashlib,re
ROOT=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo');R=ROOT/'work/quartic-version6-release/repository';O=ROOT/'work/quartic-v14-prep/baseline-coverage/gaussian'
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf8'))
initial=load(O/'INITIAL-SOURCE-USES.json');freeze=load(O/'INITIAL-FREEZE.json')
for p,h in freeze['frozen_files'].items():assert sha((O/p).read_bytes())==h
source=(R/'manuscripts/quartic_v13.tex').read_bytes();lines=source.splitlines(keepends=True)
files=['docs/theorem-application-audit/applications.json','docs/theorem-application-audit/internal-references.json','docs/theorem-application-audit/coverage.json','docs/quartic-962/new-applications.json','docs/quartic-962/dependency-graph.json','docs/quartic-962/internal-results.json','docs/quartic-523-540/inventory.json','docs/audit-history/current.json','docs/manuscript-revisions/version13/quartic-carryforward-application.json','docs/manuscript-revisions/version13/quartic-carryforward-acceptance.json','docs/manuscript-revisions/version12/evidence/author-applications.json']
pins=[{'path':p,'sha256':sha((R/p).read_bytes())} for p in files]
v6=load(R/files[3]);graph=load(R/files[4]);v9=load(R/files[6]);v12=load(R/files[-1])
nodes={n['id']:n for n in graph['internal_nodes']}
for n in v9['dependency_nodes']:nodes[n['id']]=n
v5file='docs/quartic-1272/new-applications.json'
v5=load(R/v5file)
pins.append({'path':v5file,'sha256':sha((R/v5file).read_bytes())})
apps=v6['applications']+v9['new_applications']+[x for x in v5['applications'] if x['id'] in v6['inherit_v5_applications']]+v12['applications']
explicit_owners={'GAU-016':['lem:gn-norm-transfer'],'GAU-018':['gi-moments'],'GAU-021':['gi-progressions','gi-minor-arc'],'GAU-030':['prop:gf-factorization'],'GAU-031':['prop:gf-factorization'],'GAU-037':['subsec:gaussian-gowers-bridge'],'GAU-039':['prop:v5-artin-patterns'],'GAU-047':['v9chart:prop:chart']}
out=[];cross=[];edgechecks=[]
baselines={str(p.relative_to(R)):p.read_bytes() for p in [R/'manuscripts/quartic_v7.tex',R/'manuscripts/quartic_v9.tex',R/'manuscripts/quartic_v12.tex'] if p.exists()}
for row in initial['uses']:
    a,b=row['start_line'],row['end_line'];blob=b''.join(lines[a-1:b]);labels=re.findall(rb'\\label\{([^}]+)\}',blob);labels=[x.decode() for x in labels]
    match_labels=labels+explicit_owners.get(row['id'],[])
    matched=[]
    for app in apps:
        aset=set(app.get('current_labels',[])+([app['label']] if app.get('label') else [])+[x.get('label','') for x in app.get('consumers',[])])
        if aset.intersection(match_labels):matched.append({'application_id':app['id'],'matched_consumer_labels':sorted(aset.intersection(match_labels)),'status':app.get('status','V9/V12 reviewed scope with current carryforward; see inventory'),'source_version_qualification':app.get('qualification','Consult exact source record in pinned inventory')})
    node_matches=[k for k in match_labels if k in nodes]
    old_matches=[]
    for p,raw in baselines.items():
        pos=raw.find(blob)
        if pos>=0:old_matches.append({'path':p,'sha256':sha(raw),'start_byte':pos,'end_byte_exclusive':pos+len(blob),'comparison':'entire source-use passage byte-identical'})
    refs=row['literal_direct_references']
    for ref in refs:
        if ref['edge_scope']=='cross_slice':cross.append({'source_use_id':row['id'],**ref})
        # A missing edge here is only a comparison candidate. Equations and proof
        # resumption paragraphs can have a different owner from a result node.
        target=ref['supplier_label'];owners=[]
        for n in node_matches:
            node=nodes[n];deps=node.get('dependencies',[])+node.get('declared_dependencies',[])+node.get('references',[])
            if target in deps:owners.append(n)
        edgechecks.append({'source_use_id':row['id'],'consumer_line':ref['consumer_line'],'supplier_label':target,'passage_result_nodes':node_matches,'exact_direct_edge_found_in_nodes':owners,'comparison_status':'direct edge represented' if owners else 'not represented under a result node in this passage; consult row disposition, not an automatic mathematical gap'})
    if a>=19800:
        disp='Current V13 QUARTIC-498-COMPOSITION contract and acceptance retain the full V12 composition; this reconstruction supplies finer direct-use locations, including prose and unnamed estimates. The acceptance retains inherited source qualifications.'
    elif a>=19176:
        disp='V9 inventory maps new named results and four external applications. Source-first table retains all explicit inherited inputs and inline maps; byte comparison and V13 carryforward do not re-prove old arithmetic.'
    elif matched or node_matches:
        disp='Matched analytic application/result records. Required contracts were independently reconstructed before this comparison. Direct-use additions for unnamed estimates are retained in the new table; no transitive path is treated as direct review.'
    else:
        disp='Unnumbered setup, proof resumption, or inline arithmetic/analytic step. Covered by initial source-use contract and nearby result application; retain explicit row instead of omitting it because no named inventory entry matches.'
    out.append({'source_use_id':row['id'],'range':[a,b],'excerpt_sha256':row['excerpt_sha256'],'consumer_labels':labels,'application_matches':matched,'internal_node_matches':node_matches,'exact_historical_passage_matches':old_matches,'disposition':disp,'review_scope':'dependency coverage/reconciliation; old acceptance retained only with original limitations; no new blanket acceptance'})
result={'initial_source_uses_sha256':sha((O/'INITIAL-SOURCE-USES.json').read_bytes()),'inventories':pins,'reconciled_uses':out,'cross_slice_edges':cross,'direct_edge_comparison':edgechecks,'limitations':['A graph match is evidence of recorded dependence, not proof of the theorem application.','Direct-edge comparison includes equations, aliases and proof-resumption passages; absent matches are not automatically unsupported inference.','V12 current contract has composition-level granularity; initial table provides finer direct uses.','DK/BL/BHB final published edition comparisons remain unresolved in the inspected historical evidence.']}
(O/'RECONCILIATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
# Export a concise, explicit direct-use supplement, with manual contracts and
# exact literal references rather than inventing named source theorems.
supp=[]
for row in initial['uses']:
    supp.append({'id':row['id'],'consumer_range':[row['start_line'],row['end_line']],'required_assertion':row['required_assertion_objects_maps_conventions_consumers'],'supplier_contract':row['source_derived_supplier_contract_and_inline_argument'],'direct_uses':row['literal_direct_references'],'citation_uses':row['literal_external_citations'],'source_sha256':initial['metadata']['source_sha256'],'excerpt_sha256':row['excerpt_sha256']})
(O/'RECONCILED-DIRECT-USES.json').write_text(json.dumps(supp,indent=2)+'\n',encoding='utf8')
# Verify raw-byte coverage independently of the initial generation.
c=load(O/'COVERAGE-INDEX.json')['lines'];assert [x['line'] for x in c]==list(range(16545,20772))
assert all(source[x['byte_start']:x['byte_end_exclusive']]==lines[x['line']-1] and sha(lines[x['line']-1])==x['raw_line_sha256'] for x in c)
assert b''.join(source[x['byte_start']:x['byte_end_exclusive']] for x in c)==(O/'assigned-source.tex').read_bytes()
receipt={'source_sha256':sha(source),'initial_immutable_hashes_verified':True,'coverage_exactly_lines_16545_through_20771':True,'every_raw_line_hash_and_byte_offset_verified':True,'line_count':len(c),'source_use_count':len(out),'cross_slice_reference_occurrences':len(cross),'direct_reference_occurrences':len(edgechecks),'rows_with_exact_historical_byte_match':sum(bool(x['exact_historical_passage_matches']) for x in out),'scope':'Byte coverage and recorded-link consistency only; not mathematical validity or semantic exhaustiveness.'}
(O/'COVERAGE-VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt))
