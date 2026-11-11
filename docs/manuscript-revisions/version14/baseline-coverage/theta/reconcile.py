from pathlib import Path
import json,hashlib,re,difflib,datetime
HERE=Path(__file__).resolve().parent; WORK=HERE.parents[2]; WS=WORK.parent
REPO=WORK/'quartic-version6-release/repository'; AUD=REPO/'docs/theorem-application-audit'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
initial=read(HERE/'INITIAL-SOURCE-USES.json'); frozen=read(HERE/'INITIAL-FREEZE.json')
for name in ['INITIAL-SOURCE-USES.json','COVERAGE-INDEX.json','assigned-source.tex']:assert sha((HERE/name).read_bytes())==frozen[name]
src=REPO/'manuscripts/quartic_v13.tex';data=src.read_bytes(); lines=data.splitlines(keepends=True)
apps={a['id']:a for a in read(AUD/'applications.json')};sources={a['id']:a for a in read(AUD/'sources.json')};sites=read(AUD/'application-sites.json')
hist=read(REPO/'docs/audit-history/current.json');evidence={a['id']:a for a in read(AUD/'evidence.json')}
mapping='''
T001 A022 A023 A024 A025 A027 A028 A029 A031 A034 A037 A038 A039 A040 A011 A014 A015 A003 A004 A018 A021 A046 A082 A020
T002 A023 A049 A050 A051 A080 A081
T003 A049
T004 A050
T005 A080
T006 A051 A080
T007 A051 A080
T008 A050 A051
T009 A050 A081
T010 A023 A033
T011 A023 A049 A051 A033
T012 A023 A080 A081
T013 A081
T014 A075
T015 A075
T016 A075 A042 A073 A074
T017 A075
T018 A075 A050
T019 A075 A023 A081
T020 A045 A082
T021 A037 A045
T022 A045 A081 A082
T023 A030
T024 A030 A053
T025 A029 A030
T026 A031 A072
T027 A029 A031
T028 A029 A031 A032
T029 A022 A025
T030 A027 A059 A070 A082 A068
T031 A033 A059
T032 A067 A061
T033 A052 A066 A070
T034 A026 A052 A053
T035 A052 A053
T036 A053
T037 A053
T038 A053
T039 A053 A054
T040 A054
T041 A053 A054
T042 A032 A052 A070
T043 A028 A052 A068
T044 A028
T045 A028 A070
T046 A027 A020
T047 A032 A053 A054
T048 A032 A053 A054
T049 A032 A067
T050 A032 A067
T051 A032 A067 A068
T052 A032
T053 A032 A067
T054 A032 A067
T055 A057 A076
T056 A024 A026 A057
T057 A024 A026 A057
T058 A075 A076 A082
T059 A027 A040
T060 A076
T061 A076 A082
T062 A029 A031
T063 A032
T064 A032 A057 A059 A067
T065 A076
T066 A076
T067
T068
T069 A057 A076
T070 A038 A039 A040 A041 A044 A045 A075
T071 A075 A076
T072 A009
T073 A009
T074 A009
'''
mp={x.split()[0]:x.split()[1:] for x in mapping.strip().splitlines()}
audsrc=AUD/'source/audited-baseline.tex'; old=audsrc.read_bytes().splitlines(keepends=True)
v10=REPO/'manuscripts/quartic_v10.tex'; v10lines=v10.read_bytes().splitlines(keepends=True)
def linemap(old,new):
    result={}
    for block in difflib.SequenceMatcher(None,old,new,autojunk=False).get_matching_blocks():
        for i in range(block.size):result[block.b+i+1]=block.a+i+1
    return result
amap=linemap(old,lines); vmap=linemap(v10lines,lines)
def intervals(ns):
    out=[]
    for n in sorted(ns):
        if out and n==out[-1][1]+1:out[-1][1]=n
        else:out.append([n,n])
    return out
def bridge(a,b,m):
    pairs=[(n,m[n]) for n in range(a,b+1) if n in m]; out=[]
    for n,o in pairs:
        if out and n==out[-1]['current'][1]+1 and o==out[-1]['historical'][1]+1:
            out[-1]['current'][1]=n;out[-1]['historical'][1]=o
        else:out.append({'current':[n,n],'historical':[o,o]})
    return dict(equal_line_blocks=out,unmatched_current_lines=intervals(set(range(a,b+1))-set(m)))
recs=[]
for r in initial['uses']:
    a,b=r['lines']; ids=mp[r['id']]
    recs.append(dict(source_use_id=r['id'],lines=r['lines'],excerpt_sha256=r['excerpt_sha256'],application_ids=ids,matching_basis='Manual comparison of required assertion and maps against actual application source_locator, objects, hypotheses, conventions and translation fields. IDs are scoped source-family matches, not blanket discharge of all internal assertions.',application_contracts=[{k:apps[i][k] for k in ['id','title','source_locator','sources','objects_and_maps','hypotheses_and_discharge','conventions','translation_justification','review_scope'] if k in apps[i]} for i in ids],historical_audited_baseline_bridge=bridge(a,b,amap),version10_bridge=bridge(a,b,vmap),disposition='Existing source-family contract retained only for matching use and unchanged bytes; independently reconstructed inline steps and cross-slice prerequisites remain explicit in initial record. See RECONCILIATION.md for occurrence refinements and scope limits.'))
    hist_lines={amap[n] for n in range(a,b+1) if n in amap}
    recs[-1]['historical_occurrence_matches']=[s['id'] for s in sites if s['application_id'] in ids and any(s['anchor']['line_start']<=n<=s['anchor']['line_end'] for n in hist_lines)]
    recs[-1]['classification']='inline-internal-derivation' if not ids else 'source-family-and-occurrence-reconciliation'
(HERE/'RECONCILED-SOURCE-USES.json').write_text(json.dumps({'initial_sha256':frozen['INITIAL-SOURCE-USES.json'],'records':recs},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
# Every literal ref is recorded with exact supplier label. This checks links, not semantic completeness.
labels={}
for n,l in enumerate(lines,1):
    for label in re.findall(rb'\\label\{([^}]+)\}',l):labels.setdefault(label.decode(),[]).append(n)
edges=[]
for n in range(12194,16545):
    for label in re.findall(rb'\\(?:ref|eqref)\{([^}]+)\}',lines[n-1]):
        key=label.decode();sup=labels.get(key,[])
        edges.append(dict(consumer_line=n,consumer_line_sha256=sha(lines[n-1]),label=key,supplier_label_lines=sup,cross_slice=bool(sup and not 12194<=sup[0]<=16544),supplier_line_sha256=[sha(lines[k-1]) for k in sup],status='unique-label-linked' if len(sup)==1 else 'unresolved-label'))
(HERE/'EXACT-REFERENCE-EDGES.json').write_text(json.dumps(edges,indent=2)+'\n',encoding='utf-8')
used=set(s for r in recs for app in r['application_contracts'] for s in app['sources'])
sb=[]
for sid in sorted(used):
    s=sources[sid].copy(); verified=[]
    for f in s.get('files',[]):
        p=WS/f['workspace_relative_path'];match=p.exists() and sha(p.read_bytes())==f['sha256']
        verified.append(dict(path=str(p),exists=p.exists(),sha256_matches=match,content_read_in_this_review=False))
    s['local_binding_checks']=verified;s['status_in_this_review']='Exact source pin inherited from existing scoped contract; bytes checked where available. This review does not claim to have freshly read every primary source.';sb.append(s)
(HERE/'SOURCE-BINDINGS.json').write_text(json.dumps(sb,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pins={}
paths=[src,audsrc,v10,AUD/'applications.json',AUD/'application-sites.json',AUD/'sources.json',AUD/'evidence.json',AUD/'internal-references.json',AUD/'named-input-index.json',AUD/'DEPENDENCY_PHASES.json',REPO/'docs/audit-history/current.json',REPO/'docs/audit-history/PROTOCOL.md']
paths.append(REPO/'docs/audit-history/issue2/register.json')
for name in ['closure-batch-006','closure-batch-007','parallel-a009-independent','parallel-theta-local-final-dependency-review']:
    paths.append(AUD/evidence[name]['path'])
for name in ['norms','interface']:paths.append(REPO/f'docs/manuscript-revisions/version11/evidence/{name}.md')
for name in ['kato-carryforward-application.json','kato-carryforward-acceptance.json','evidence/kato-carryforward-review.md']:paths.append(REPO/f'docs/manuscript-revisions/version13/{name}')
for p in paths:pins[str(p.relative_to(REPO))]=sha(p.read_bytes())
(HERE/'RECONCILIATION-INPUT-HASHES.json').write_text(json.dumps(pins,indent=2)+'\n',encoding='utf-8')
stats=dict(initial_unchanged=True,lines=4351,passages=74,historic_equal_lines=sum(n in amap for n in range(12194,16545)),v10_equal_lines=sum(n in vmap for n in range(12194,16545)),historical_unmatched=intervals(set(range(12194,16545))-set(amap)),v10_unmatched=intervals(set(range(12194,16545))-set(vmap)),cross_slice_refs=[e for e in edges if e['cross_slice']],source_files_missing=[v['path'] for s in sb for v in s['local_binding_checks'] if not v['exists']],source_hash_mismatch=[v['path'] for s in sb for v in s['local_binding_checks'] if v['exists'] and not v['sha256_matches']])
(HERE/'CHECKS.json').write_text(json.dumps(stats,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in stats.items() if k!='cross_slice_refs'},indent=2))
print('CROSS-SLICE LABELS',sorted(set(e['label'] for e in stats['cross_slice_refs'])))
