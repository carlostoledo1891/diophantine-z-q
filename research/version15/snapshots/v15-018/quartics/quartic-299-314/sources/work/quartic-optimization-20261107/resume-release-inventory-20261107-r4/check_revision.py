from pathlib import Path
import hashlib,json,copy
from validate_relation import validate
H=Path(__file__).resolve().parent;ROOT=H.parents[2]
def load(n):return json.loads((H/n).read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins=load('SOURCE-PINS.json')
for path,m in pins.items():
    assert sha(ROOT/path)==m['sha256'],path
    assert (ROOT/path).stat().st_size==m['bytes'],path
prior=load('PREVIOUS-REVISION.json')
for item in prior['files'].values():assert sha(ROOT/item['path'])==item['sha256']
a,r,m,c=(load(n) for n in ['APPLICATION-DELTA.json','CANONICAL-RELATION.json','INTEGRATION-MAP.json','CANDIDATES.json'])
count=validate(a,r,m,c)
old=json.loads((ROOT/prior['files']['APPLICATION-DELTA.json']['path']).read_bytes())
assert [x['id'] for x in a['applications']]==[x['id'] for x in old['applications']]
for new,prev in zip(a['applications'],old['applications']):
    for key in ['baselineSource','baselineConsumers','baselineRecordSha256Canonical']:assert new[key]==prev[key]
oldrel=json.loads((ROOT/prior['files']['CANONICAL-RELATION.json']['path']).read_bytes())
oldedges={(x['applicationId'],x['entryId']) for x in oldrel['edges']}
assert oldedges<={(x['applicationId'],x['entryId']) for x in r['edges']}
for entry in a['newInternalEntries']:
    for source in entry['authorProof']:
        assert sha(ROOT/source['path'])==source['sha256']
        lines=(ROOT/source['path']).read_text(encoding='utf-8').splitlines()
        assert 1<=source['startLine']<=source['endLine']<=len(lines)
        if source['heading']=='Whole report':assert source['startLine']==1 and source['endLine']==len(lines)
        else:assert lines[source['startLine']-1]==source['heading']
assert sha(ROOT/m['outline']['path'])==m['outline']['sha256']
lines=(ROOT/m['outline']['path']).read_text(encoding='utf-8').splitlines()
for item in m['entries']:assert '\\label{'+item['outlineLabel']+'}' in lines[item['outlineLabelLine']-1]
for item in load('NEW-INPUT-CLASSIFICATION.json')['retainedArithmeticApplications']:
    s=item['source'];assert sha(ROOT/s['path'])==s['sha256']
    ls=(ROOT/s['path']).read_text(encoding='utf-8').splitlines()
    span='\n'.join(ls[s['startLine']-1:s['endLine']])+'\n'
    assert hashlib.sha256(span.encode()).hexdigest()==s['sha256_normalized_LF_span']
for cid,item in c['components'].items():
    ir=json.loads((ROOT/item['candidate']['path']).read_bytes())
    assert sha(ROOT/item['candidate']['path'])==item['candidate']['sha256']
    assert item['canonicalCandidateId']=='sha256:'+item['candidate']['sha256']
    assert (len(ir['coordinates']),len(ir['residuals']))==(item['variables'],item['residuals'])
    if item.get('comparedWith') and 'objectDelta' in item:
        source=c['components'][item['comparedWith']]
        src=json.loads((ROOT/source['candidate']['path']).read_bytes())
        for key in ['coordinates','residuals']:
            p={v['id']:v for v in src[key]};q={v['id']:v for v in ir[key]}
            delta={'deleted':sorted(p.keys()-q.keys()),'added':sorted(q.keys()-p.keys()),'changed':sorted(k for k in p.keys()&q.keys() if p[k]!=q[k])}
            assert delta==item['objectDelta'][key],(cid,key)
tests=[]
def rejects(name,mutate):
    aa,rr,mm,cc=copy.deepcopy((a,r,m,c));mutate(aa,rr,mm,cc)
    try:validate(aa,rr,mm,cc)
    except (AssertionError,KeyError):tests.append(name);return
    raise AssertionError('Negative fixture accepted: '+name)
rejects('missing_application_edge',lambda a,r,m,c:next(x for x in a['applications'] if x['newEntryIds'])['newEntryIds'].pop())
rejects('extra_application_edge',lambda a,r,m,c:a['applications'][0]['newEntryIds'].append('unknown'))
rejects('missing_entry_edge',lambda a,r,m,c:a['newInternalEntries'][-1]['baselineApplications'].pop())
rejects('missing_map_edge',lambda a,r,m,c:m['entries'][-1]['inventoryConsumers'].pop())
rejects('duplicate_canonical_edge',lambda a,r,m,c:r['edges'].append(copy.deepcopy(r['edges'][0])))
rejects('unknown_canonical_endpoint',lambda a,r,m,c:r['edges'][0].update(entryId='unknown'))
rejects('scope_drift',lambda a,r,m,c:r['edges'][0]['scope'].update(selectedCandidateDependency=not r['edges'][0]['scope']['selectedCandidateDependency']))
rejects('consumer_span_drift',lambda a,r,m,c:m['entries'][0]['inventoryConsumers'][0].update(baselineConsumerSpans=[]))
rejects('stale_ordinary_classification',lambda a,r,m,c:next(x for x in a['applications'] if x['id']=='V13-ORDINARY-GATE').update(deltaClassification='accepted_exact319_only'))
rejects('unapproved_selected313_lift',lambda a,r,m,c:next(x for x in a['applications'] if x['id']=='V13-ORDINARY-GATE')['ordinaryArtifactScope'].update(selectedCandidateLiftIncluded=True))
rejects('wrong_ordinary_parent',lambda a,r,m,c:c['components']['ordinaryShared314_331'].update(comparedWith='anchorGamma313'))
rejects('missing_H_bootstrap',lambda a,r,m,c:a['newInternalEntries'].pop(24))
rejects('author_self_review',lambda a,r,m,c:a['newInternalEntries'][-1].update(reviewer='05'))
rejects('invented_new_approval',lambda a,r,m,c:a['newInternalEntries'][-1].update(newApprovalCreatedHere=True))
rejects('proof_mapping_drift',lambda a,r,m,c:m['entries'][-1]['authorProof'][0].update(sha256='0'*64))
rejects('actual_consumer_drift',lambda a,r,m,c:m['entries'][-1].update(actualConsumer='Changed H order'))
result={'status':'structural checks passed; independent inventory review pending','canonicalEdges':count,'applications':len(a['applications']),'entries':len(a['newInternalEntries']),'candidates':len(c['components']),'allPriorEdgesPreserved':True,'baselineSourceConsumerRecordsUnchanged':True,'priorPacketUnchanged':True,'negativeFixturesRejected':tests,'sourcePinsChecked':len(pins),'newMathematicalApprovalCreated':False,'independentInventoryAcceptance':False}
(H/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
