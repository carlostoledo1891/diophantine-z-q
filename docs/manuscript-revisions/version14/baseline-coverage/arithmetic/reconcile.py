from pathlib import Path
import json, hashlib, re
O=Path(__file__).parent
R=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-version6-release/repository')
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
source=R/'manuscripts/quartic_v13.tex'; raw=source.read_bytes(); bl=raw.splitlines(keepends=True)
text=raw.decode('utf-8'); normalized=text.replace('\r\n','\n'); ls=normalized.splitlines()
initial=load(O/'INITIAL-SOURCE-USES.json'); coverage=load(O/'COVERAGE-INDEX.json')
base=R/'docs/theorem-application-audit'
apps=load(base/'applications.json'); old=(base/'source/audited-baseline.tex').read_text(encoding='utf-8').splitlines()
labels={m.group(1):i for i,line in enumerate(ls,1) for m in re.finditer(r'\\label\{([^}]+)\}',line)}
# Independently read contracts matched by mathematical assertion, not name alone.
MAP={
234:'',258:'55',271:'56',306:'57 71',322:'58 59',370:'60',420:'55',
486:'1',519:'2 78',556:'78',585:'1 78',620:'61 79',657:'3 4 65',690:'5 6',708:'62',741:'7 68',794:'8 9 10',831:'11',852:'64 67',872:'12 13 71',924:'63 14',953:'15 16 6',983:'17 18',1025:'',1049:'',1080:'65',1104:'57 58 71',1157:'19',1171:'20 82 66',1208:'71',1251:'56 71',1287:'71',1333:'60',1366:'',1385:'',1438:'57',1500:'21',1573:'21',1622:'21',1672:'72',1718:'21 72',1762:'21',1823:'57 71',1877:'22 65 66',1940:'23 49 50 51 81',1970:'23 49 50 51 80 81',2040:'23 45 75 81',2097:'24 25 26 57',2135:'57 68',2197:'29 31 76',2231:'32',2280:'57',2305:'',2351:'57 76',2419:'23 29',2472:'24 25 57 82',2532:'27',2589:'25 27 33 67',2629:'28 52 53 54 76',2682:'29 30 31 32',2713:'27 82 76',2757:'57',2793:'57 76',2855:'68',2898:'37 38',2971:'33',3051:'34 35 70',3106:'68 80',3171:'36 71 80',3225:'35 71 80',3339:'34 68 80',3434:'38 80',3509:'75 80',3549:'37 38 75',3607:'39',3637:'68 67',3734:'33 67 68',3840:'38 75',3917:'37 38 75',4014:'',4049:'34 38 75',4124:'75',4154:'20 27 40 45 82',4235:'40 69',4327:'41',4418:'67 68 41',4515:'27 45 75',4568:'75 76',4639:'42 73 74',4731:'37 43 44 75',4798:'39 75',4836:'75 76',4905:'75 76',4933:'33 67',4995:'67 76',5019:'44',5095:'44 75 76',5162:'33 38 44',5241:'44 67',5340:'38 44 75',5393:'39 41 45 82',5455:'45',5501:'39 45 75',5580:'75',5672:'75',5731:'75',5805:'75',5833:'',5880:''}
appby={a['id']:a for a in apps}
anchor_matches={}
for a in apps:
    matches=[]
    for ix,an in enumerate(a.get('manuscript_anchors',[])):
        excerpt='\n'.join(old[an['line_start']-1:an['line_end']])
        starts=[]; pos=normalized.find(excerpt)
        while pos>=0 and excerpt:
            line=normalized.count('\n',0,pos)+1
            starts.append({'start_line':line,'end_line':line+excerpt.count('\n'),'raw_excerpt_sha256':sha(b''.join(bl[line-1:line+excerpt.count('\n')]))})
            pos=normalized.find(excerpt,pos+1)
        matches.append({'anchor_index':ix,'historical_span':[an['line_start'],an['line_end']],'matches':starts,'comparison':'exact decoded lines after CRLF-to-LF solely for matching; raw current span separately hashed'})
    anchor_matches[a['id']]=matches
reconciled=[]; cross=[]
for u in initial['uses']:
    start=u['start_line']; end=u['end_line']; frag='\n'.join(ls[start-1:end])
    aids=['A'+n.zfill(3) for n in MAP.get(start,'').split()]
    # Add only exact anchored occurrences intersecting this source-first span.
    exact=[]
    for aid,als in anchor_matches.items():
        hits=[{'anchor_index':m['anchor_index'],**h} for m in als for h in m['matches'] if h['start_line']<=end and h['end_line']>=start]
        if hits: exact.append({'application_id':aid,'matching_anchors':hits})
    refs=sorted(set(m.group(1) for m in re.finditer(r'\\(?:ref|eqref)\{([^}]+)\}',frag)))
    direct=[]
    for ref in refs:
        n=labels.get(ref)
        entry={'label':ref,'supplier_start_line':n,'scope':'within_assigned_slice' if n and n<=5930 else 'cross_slice' if n else 'unresolved_label','classification':'direct textual reference; may denote announced conclusion or supplier, review assertion in initial row'}
        direct.append(entry)
        if n and n>5930: cross.append({'source_use_id':u['source_use_id'],'consumer_span':[start,end],**entry})
    mapped=[]
    for aid in aids:
        a=appby[aid]
        mapped.append({'application_id':aid,'title':a['title'],'source_ids':a['sources'],'exact_locator':a['source_locator'],'objects_and_maps':a['objects_and_maps'],'contract_bound_manuscript_sha256':a['manuscript_sha256'],'inheritance_scope':'Retain historical source-interface acceptance only for matching unchanged assertion. Initial row identifies additional inline derivations and dependencies. This is not fresh primary-source reproof.'})
    reconciled.append({'source_use_id':u['source_use_id'],'consumer_span':[start,end],'assertion_matched_application_contracts':mapped,'exact_historical_anchor_overlaps':exact,'direct_textual_references':direct,'additional_inline_inputs':u['proposed_exact_supplier'],'disposition':'Recorded direct uses and elementary/inline derivations added to source-first coverage. Cross-slice supplier joins remain for assembled review.'})
files=['applications.json','application-sites.json','internal-references.json','DEPENDENCY_PHASES.json','coverage.json','sources.json','evidence/pole.md','evidence/descent.md','evidence/descent-addendum.md','FINDINGS.md','DEPENDENCIES.md']
pins={str((base/f).relative_to(R)):sha((base/f).read_bytes()) for f in files}
for f in ['docs/audit-history/current.json','docs/audit-history/issue2/register.json','docs/audit-history/issue2/evidence/valuation.md','docs/manuscript-revisions/version11/evidence/norms.md','docs/manuscript-revisions/version11/evidence/interface.md','docs/manuscript-revisions/version13/kato-carryforward-application.json','docs/manuscript-revisions/version13/kato-carryforward-acceptance.json','docs/manuscript-revisions/version13/evidence/kato-carryforward-review.md']:
    pins[f]=sha((R/f).read_bytes())
payload={'schema':'arithmetic-reconciliation-v1','initial_freeze_sha256':sha((O/'INITIAL-FREEZE.json').read_bytes()),'inventory_and_history_pins':pins,'matching_method':'First source-use assertion was frozen independently; named contracts compared subsequently for mathematical objects and conventions. Historical anchors matched mechanically by exact decoded line text, with raw current spans hashed separately. Overlapping anchor is evidence of textual coverage, not proof of the entire initial row. Broad contract IDs are not substitutes for its additional direct internal dependencies.','reconciled_uses':reconciled,'cross_slice_references':cross}
(O/'RECONCILIATION.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
(O/'HISTORICAL-ANCHOR-MATCHES.json').write_text(json.dumps(anchor_matches,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'uses':len(reconciled),'with_named_application_matches':sum(bool(u['assertion_matched_application_contracts']) for u in reconciled),'with_exact_old_anchor_overlap':sum(bool(u['exact_historical_anchor_overlaps']) for u in reconciled),'cross_slice_reference_count':len(cross),'cross_slice_unique_labels':sorted(set(x['label'] for x in cross))},indent=2))
