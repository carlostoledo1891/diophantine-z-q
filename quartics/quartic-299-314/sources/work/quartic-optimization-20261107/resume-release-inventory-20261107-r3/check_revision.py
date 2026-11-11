from pathlib import Path
import hashlib,json,copy
from validate_relation import validate

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def read(n):return json.loads((HERE/n).read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p,m in read('SOURCE-PINS.json').items():
    if p.endswith('/STATUS.json'):continue
    assert sha(ROOT/p)==m['sha256'],p
for p in read('PREVIOUS-REVISION.json').values():assert sha(ROOT/p['path'])==p['sha256']
a=read('APPLICATION-DELTA.json');r=read('CANONICAL-RELATION.json');m=read('INTEGRATION-MAP.json')
edges=validate(a,r,m)
old=read('PREVIOUS-REVISION.json')['APPLICATION-DELTA.json']['path']
old=json.loads((ROOT/old).read_bytes())
for now,then in zip(a['applications'],old['applications']):
    for key in ['id','baselineSource','baselineConsumers','baselineRecordSha256Canonical']:
        assert now[key]==then[key]
assert sha(ROOT/m['outline']['path'])==m['outline']['sha256']
tex=(ROOT/m['outline']['path']).read_text(encoding='utf-8').splitlines()
for item in m['entries']:
    assert '\\label{'+item['outlineLabel']+'}' in tex[item['outlineLabelLine']-1]

# These mutations must be rejected even if the other two projections agree.
tests=[]
def rejects(name,change):
    aa,rr,mm=copy.deepcopy((a,r,m));change(aa,rr,mm)
    try:validate(aa,rr,mm)
    except (AssertionError,KeyError):tests.append(name);return
    raise AssertionError('accepted negative fixture: '+name)
def app_with_edge(aa):return next(x for x in aa['applications'] if x['newEntryIds'])
rejects('missing_application_edge',lambda a,r,m:app_with_edge(a)['newEntryIds'].pop())
rejects('extra_application_edge',lambda a,r,m:app_with_edge(a)['newEntryIds'].append('unknown'))
rejects('missing_entry_edge',lambda a,r,m:a['newInternalEntries'][0]['baselineApplications'].pop())
rejects('missing_map_edge',lambda a,r,m:m['entries'][0]['inventoryConsumers'].pop())
rejects('duplicate_canonical_edge',lambda a,r,m:r['edges'].append(copy.deepcopy(r['edges'][0])))
rejects('unknown_canonical_endpoint',lambda a,r,m:r['edges'][0].update(entryId='unknown'))
rejects('scope_drift',lambda a,r,m:r['edges'][0]['scope'].update(selected315Dependency=not r['edges'][0]['scope']['selected315Dependency']))
rejects('consumer_span_drift',lambda a,r,m:m['entries'][0]['inventoryConsumers'][0].update(baselineConsumerSpans=[]))
rejects('stale_ordinary_classification',lambda a,r,m:next(x for x in a['applications'] if x['id']=='V13-ORDINARY-GATE').update(deltaClassification='new_artifact_required_not_accepted'))
rejects('unapproved_selected_lift',lambda a,r,m:next(x for x in a['applications'] if x['id']=='V13-ORDINARY-GATE')['ordinaryArtifactScope'].update(selected315LiftIncluded=True))
result={'status':'structural checks passed','canonicalEdges':edges,'applications':39,'entries':23,
    'directionsCompared':['canonical','application','entry','integrationMap'],'negativeFixturesRejected':tests,
    'priorPacketUnchanged':True,'baselineSourceAndConsumerRecordsUnchanged':True,
    'independentInventoryAcceptance':False,'newMathematicalAcceptance':False}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
