from pathlib import Path
import json, hashlib, re, difflib, bisect

ROOT=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo')
REPO=ROOT/'work/quartic-version6-release/repository'
OUT=ROOT/'work/quartic-v14-prep/baseline-coverage/compiler'
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
write=lambda n,x:(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
initial=read(OUT/'INITIAL-SOURCE-USES.json')
assert sha((OUT/'INITIAL-SOURCE-USES.json').read_bytes())=='930862328bc6b9ab15ed12e0006348189e9c7705a4c5d8bcce70b664fc995445'
raw=(REPO/'manuscripts/quartic_v13.tex').read_bytes()
assert sha(raw)==initial['sha256']
text=raw.decode('utf-8'); lines=raw.splitlines(keepends=True)
cur=text.splitlines(); old=(REPO/'manuscripts/archive/quartic_v7.tex').read_text(encoding='utf-8').splitlines()
matcher=difflib.SequenceMatcher(None,old,cur,autojunk=False)
mapping={b.a+k+1:b.b+k+1 for b in matcher.get_matching_blocks() for k in range(b.size)}
def mapspan(span):
 a,b=span['first_line'],span['last_line']; m=[mapping.get(n) for n in range(a,b+1)]
 return dict(start=m[0],end=m[-1],old_start=a,old_end=b) if m and None not in m and m==list(range(m[0],m[-1]+1)) else None
offsets=[0]+[m.end() for m in re.finditer('\n',text)]
lineno=lambda n:bisect.bisect_right(offsets,n)
labels={m[1]:lineno(m.start()) for m in re.finditer(r'\\label\{([^}]+)\}',text)}
alluses=[]
for m in re.finditer(r'\\(ref|eqref|cite)((?:\s*\[[^\]]*\])*)\s*\{([^}]+)\}',text):
 for key in m[3].split(','):
  key=key.strip(); loc=labels.get(key)
  alluses.append(dict(kind=m[1],supplier=key,line=lineno(m.start()),end_line=lineno(m.end()-1),printed_locator=m[2],supplier_label_line=loc,cross_slice=loc is not None and not 5931<=loc<=12193))
internal=read(REPO/'docs/quartic-962/internal-results.json')
graph=read(REPO/'docs/quartic-962/dependency-graph.json')
internal_by_label={label:item for item in internal for label in item.get('labels',[])}
matched_internal=[]
for item in internal:
 s=mapspan(item['statement_and_proof'])
 if s and s['start']<=12193 and s['end']>=5931:
  matched_internal.append(dict(id=item['id'],labels=item['labels'],span=s,status=item.get('status'),explicit_dependencies=item.get('explicit_internal_dependencies',[]),explicit_citations=item.get('explicit_citation_keys',[]),review_limit=item.get('review_limit')))
reconciliation=read(OUT/'RECONCILIATION.json')
reconciliation['schema']='compiler-reconciliation-v2'
reconciliation['limitations']=['An existing ledger match establishes identity and preserves only its prior scoped status; it is not a new proof of that source.','Dependency edges include section/equation references, not only result environments. Unnamed mathematical imports remain in the initial manually reconstructed assertion/supplier descriptions.','Every assigned line was read. Cross-slice suppliers remain conditional on their independently assigned reviews. Artifact expansion counts are not newly replayed by this slice.']
added=[]
for p,row in zip(initial['passages'],reconciliation['rows']):
 direct=[u for u in alluses if p['start']<=u['line']<=p['end']]
 row['complete_literal_uses']=direct
 row['existing_internal_matches']=[x for x in matched_internal if x['span']['start']<=p['end'] and x['span']['end']>=p['start']]
 oldkeys={(u['kind'],u['supplier'],u['line']) for u in p['direct_named_uses']}
 for u in direct:
  if (u['kind'],u['supplier'],u['line']) not in oldkeys:added.append(dict(passage=p['id'],**u))
 row['independent_supplier_description']=p['independently_identified_suppliers']
 row['consumer']=dict(passage=p['id'],start=p['start'],end=p['end'])
incoming=[dict(consumer=next(p['id'] for p in initial['passages'] if p['start']<=u['line']<=p['end']),**u) for u in alluses if 5931<=u['line']<=12193 and u['cross_slice']]
outgoing=[u for u in alluses if not 5931<=u['line']<=12193 and u['supplier_label_line'] is not None and 5931<=u['supplier_label_line']<=12193]
reconciliation['literal_parser_additions_after_freeze']=added
reconciliation['matched_internal_results']=matched_internal
reconciliation['cross_slice_edges']=dict(incoming=incoming,outgoing=outgoing)
changes=[]
for tag,i,j,a,b in matcher.get_opcodes():
 if tag!='equal' and a+1<=12193 and b>=5931:
  changes.append(dict(kind=tag,v7_lines=[i+1,j],v13_lines=[a+1,b],v13_text='\n'.join(cur[a:b])))
reconciliation['changes_from_v7_in_slice']=changes
extra=['docs/manuscript-revisions/version10/new-applications.json','docs/manuscript-revisions/version10/sources.json','docs/manuscript-revisions/version10/inventory.json','docs/manuscript-revisions/version10/templates.tex','docs/manuscript-revisions/version13/quartic-carryforward-application.json','docs/manuscript-revisions/version13/quartic-carryforward-acceptance.json','docs/audit-history/issue2/evidence/templates.md','docs/audit-history/issue2/evidence/corollaries.md']
reconciliation['inventory_pins'] += [dict(path=p,sha256=sha((REPO/p).read_bytes())) for p in extra]
reconciliation['changed_application_dispositions']=[
 dict(lines=[6660,6686],application='V10-MAZUR-CONJECTURE2',disposition='Published 1995 original pp.165-166 inspected using retained page images after matching the PDF hash. Conjecture2 explicitly implies finite simplicial homotopy type. An infinite set of components of the closure contradicts it. 1992 source remains attribution only, not newly inspected.'),
 dict(lines=[6732,6738],application='OpenAI attribution',disposition='No stronger theorem imported: manuscript expressly distinguishes attributed Turing completeness from its own conditional many-one deduction. Unpublished attribution is not treated as a premise.'),
 dict(lines=[11965,11972],application='Source provenance',disposition='No additional mathematical premise. Exact commit/source claim retains historical provenance qualification.'),
 dict(lines=[12059,12146],application='Complete template and recipe identification',disposition='Read all dictionary entries and matches to surrounding constructor semantics. Existing issue2 historical proof records same shared index slots and private blocks. This source reading does not rerun byte-level builder, expansion, or all output coefficients.')]
write('RECONCILIATION.json',reconciliation)
write('CROSS-SLICE-EDGES.json',dict(schema='compiler-cross-slice-v2',incoming=incoming,outgoing=outgoing))
write('INTERNAL-RESULT-MATCHES.json',matched_internal)
write('INVENTORY-DELTA.json',dict(schema='compiler-inventory-delta-v1',scope='Additive independent coverage overlay; no historical record overwritten.',initial_literal_parser_additions=added,novel_coverage='141 contiguous manually reconstructed consuming passages, including unnamed imports and constructor/section/equation dependencies outside the older result-only inventory.',matched_internal_result_count=len(matched_internal),cross_slice_incoming_count=len(incoming),cross_slice_outgoing_count=len(outgoing),v7_changes=changes,retired_source_warning='Historical v5 Frei-Tinkova application is retired by the v7 internal simultaneous-prime theorem. The cross-slice theorem is the consumed supplier; do not restore the preprint as a current premise.'))
covered=[]
for p in initial['passages']:
 assert p['excerpt_sha256']==sha(b''.join(lines[p['start']-1:p['end']]))
 covered.extend(range(p['start'],p['end']+1))
assert covered==list(range(5931,12194))
assert (OUT/'ASSIGNED-SLICE.tex').read_bytes()==b''.join(lines[5930:12193])
checks=dict(manuscript_sha256=sha(raw),initial_sha256=sha((OUT/'INITIAL-SOURCE-USES.json').read_bytes()),slice_sha256=sha((OUT/'ASSIGNED-SLICE.tex').read_bytes()),passages=len(initial['passages']),covered_lines=len(covered),coverage_contiguous_exact=True,all_passage_hashes_match=True,initial_unchanged=True,matched_internal_results=len(matched_internal),incoming_edges=len(incoming),outgoing_edges=len(outgoing),multiline_literal_additions=len(added),exact_unchanged_lines_from_v7=sum(n in set(mapping.values()) for n in covered),finite_artifact_checks_rerun=False)
write('VALIDATION.json',checks)
print(json.dumps(checks,indent=2))
