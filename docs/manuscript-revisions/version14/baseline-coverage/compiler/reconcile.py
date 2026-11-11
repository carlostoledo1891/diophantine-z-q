from pathlib import Path
import json,hashlib,re,difflib
ROOT=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo')
REPO=ROOT/'work/quartic-version6-release/repository'
OUT=ROOT/'work/quartic-v14-prep/baseline-coverage/compiler'
sha=lambda b:hashlib.sha256(b).hexdigest()
initial=json.loads((OUT/'INITIAL-SOURCE-USES.json').read_text(encoding='utf-8'))
cur=(REPO/'manuscripts/quartic_v13.tex').read_text(encoding='utf-8').splitlines()
old=(REPO/'manuscripts/archive/quartic_v7.tex').read_text(encoding='utf-8').splitlines()
mapping={}
for block in difflib.SequenceMatcher(None,old,cur,autojunk=False).get_matching_blocks():
 for k in range(block.size):mapping[block.a+k+1]=block.b+k+1
files=['docs/theorem-application-audit/applications.json','docs/theorem-application-audit/coverage.json','docs/theorem-application-audit/DEPENDENCY_PHASES.json','docs/theorem-application-audit/internal-references.json','docs/quartic-4973/theorem-applications.json','docs/quartic-4973/dependency-closure.json','docs/quartic-4973/baseline-bridge.json','docs/quartic-4973/acceptance.json','docs/quartic-962/theorem-applications.json','docs/quartic-962/internal-results.json','docs/quartic-962/dependency-graph.json','docs/quartic-962/new-applications.json','docs/quartic-962/inherited-bridge.json','docs/audit-history/current.json']
data={p:json.loads((REPO/p).read_text(encoding='utf-8')) for p in files}
pins=[dict(path=p,sha256=sha((REPO/p).read_bytes())) for p in files]
graph=data['docs/quartic-962/dependency-graph.json']
internal=data['docs/quartic-962/internal-results.json']
print('graph keys',list(graph))
print('graph edge samples',str(graph.get('edges',[])[:3]))
apps=[]
for app in graph['application_nodes']:
 spans=[]
 for s in app.get('current_sites',[]):
  a,b=s['first_line'],s['last_line']; mapped=[mapping.get(n) for n in range(a,b+1)]
  if mapped and all(n is not None for n in mapped) and mapped==list(range(mapped[0],mapped[-1]+1)):
   spans.append({'start':mapped[0],'end':mapped[-1],'old_start':a,'old_end':b,'text_unchanged':True})
 apps.append({'id':app['id'],'old_status':app.get('status'),'matched_spans':spans})
labels={k:n for n,line in enumerate(cur,1) for k in re.findall(r'\\label\{([^}]+)\}',line)}
internal_by_label={label:item for item in internal for label in item.get('labels',[])}
out=[]
for p in initial['passages']:
 row={k:p[k] for k in ('id','start','end','excerpt_sha256','required_assertion')}
 row['existing_application_matches']=[dict(id=a['id'],old_status=a['old_status'],spans=[s for s in a['matched_spans'] if s['start']<=p['end'] and s['end']>=p['start']]) for a in apps if any(s['start']<=p['end'] and s['end']>=p['start'] for s in a['matched_spans'])]
 row['direct_uses']=[]
 for u in p['direct_named_uses']:
  item=dict(u)
  if u['kind']!='cite':
   target=internal_by_label.get(u['supplier'])
   item['existing_result_id']=target['id'] if target else None
   item['disposition']='direct supplier resolved in frozen manuscript; cross-slice review must be joined' if u['cross_slice'] else 'direct supplier resolved in frozen manuscript; inspected in this slice'
   if target is None:item['disposition']+='; section/equation/prose edge added by this reconstruction beyond result-only inventory'
  else:
   item['disposition']='citation occurrence retained; source contract mapped through nearby unchanged application spans, not accepted merely from key match'
  row['direct_uses'].append(item)
 row['v7_text_unchanged_lines']=sum(n in set(mapping.values()) for n in range(p['start'],p['end']+1))
 row['disposition']='Read proof and retain exact direct uses in INITIAL-SOURCE-USES; listed matching historical applications preserve their old scoped status only. Inline algebra/valuation/choice-order arguments checked by this reading. No whole-proof acceptance inferred.'
 out.append(row)
cross=[dict(passage=p['id'],**u) for p in initial['passages'] for u in p['direct_named_uses'] if u['cross_slice']]
result={'schema':'compiler-reconciliation-v1','initial_sha256':sha((OUT/'INITIAL-SOURCE-USES.json').read_bytes()),'manuscript_sha256':initial['sha256'],'inventory_pins':pins,'line_match_rule':'Compare decoded UTF-8 lines after universal newline decoding, with no whitespace or mathematical normalization; passage digests separately retain original bytes. Matching an old application span is identity evidence, not source acceptance.','rows':out,'cross_slice_edges':cross}
(OUT/'RECONCILIATION.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
(OUT/'CROSS-SLICE-EDGES.json').write_text(json.dumps(cross,indent=2)+'\n',encoding='utf-8',newline='\n')
summary=[{'id':p['id'],'range':[p['start'],p['end']],'applications':[a['id'] for a in p['existing_application_matches']],'unchanged':p['v7_text_unchanged_lines']} for p in out]
(OUT/'MATCH-SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
print('matched applications',sorted(set(a['id'] for p in out for a in p['existing_application_matches'])))
print('cross slice suppliers',sorted(set(e['supplier'] for e in cross)))
print('unmatched rows',[(p['id'],p['start'],p['end']) for p in out if not p['existing_application_matches']])
print('assigned unchanged line count',sum(p['v7_text_unchanged_lines'] for p in out))
