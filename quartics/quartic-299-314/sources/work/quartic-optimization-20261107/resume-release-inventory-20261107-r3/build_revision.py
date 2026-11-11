"""Build corrected preparatory inventory from pinned r2 and one edge specification."""
from pathlib import Path
import hashlib,json,copy
from relation_spec import SPEC,REJECTED

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OLD=HERE.with_name('resume-release-inventory-20261107-r2')
REVIEW=HERE.with_name('resume-review-inventory-r2-sol')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_bytes())
def write(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert sha(OLD/'FROZEN-MANIFEST.json')=='56a0e6a76318e56af6158ea1ccb325457b0c3a4772974c5849b935b52c9ba97d'
assert sha(REVIEW/'REVIEW.md')=='b2eaa221d8ec036a6fd9f51b76679be50e4388225ccc3561eb40ed99e3475e98'
for name,meta in read(OLD/'FROZEN-MANIFEST.json').items():
    assert sha(OLD/name)==meta['sha256'] and (OLD/name).stat().st_size==meta['bytes']
pins=read(OLD/'SOURCE-PINS.json')
prior={}
for folder in (OLD,REVIEW):
    for p in sorted(folder.iterdir()):
        if p.is_file():
            key=p.relative_to(ROOT).as_posix()
            pins[key]={'sha256':sha(p),'bytes':p.stat().st_size}
            if folder==OLD:prior[p.name]={'path':key,'sha256':sha(p)}
for name in ('CANDIDATES.json','RETAINED-SOURCES.json','PRESERVED-ALTERNATIVES.json',
             'STATUS-SNAPSHOT.json','CANONICAL-INDEX.md','PROOF-INTEGRATION-OUTLINE.tex'):
    (HERE/name).write_bytes((OLD/name).read_bytes())
apps=read(OLD/'APPLICATION-DELTA.json')
previous=copy.deepcopy(apps)
entries={int(e['id'][1:3]):e for e in apps['newInternalEntries']}
appids={a['id'] for a in apps['applications']}
assert set(SPEC)==set(entries)
edges=[]
for n,(targets,reason) in SPEC.items():
    e=entries[n]
    target_ids=['V13-'+t for t in targets.split()]
    assert len(set(target_ids))==len(target_ids) and set(target_ids)<=appids
    for target in target_ids:
        edges.append({'applicationId':target,'entryId':e['id'],'reason':reason,
            'scope':{'selected315Dependency':e['selected315Dependency'],
                     'componentIds':e.get('coveredComponentIds',[e['component']])},
            'sourceProof':e['authorProof']})
edges.sort(key=lambda x:(x['applicationId'],x['entryId']))
relation={'schema':1,'status':'author_reconciled_pending_independent_inventory_review',
    'meaning':'Direct changed application, exact transport, or explicitly restored hypothesis; not an exhaustive transitive dependency graph.',
    'edges':edges}
edgekeys={(x['applicationId'],x['entryId']) for x in edges}

oldforward={(a['id'],e) for a in previous['applications'] for e in a['newEntryIds']}
oldreverse={(a,e['id']) for e in previous['newInternalEntries'] for a in e['baselineApplications']}
decisions=[]
for app,eid in sorted(oldforward^oldreverse):
    n=int(eid[1:3]);keep=(app,eid) in edgekeys
    reason=SPEC[n][1] if keep else REJECTED[(app,n)]
    decisions.append({'applicationId':app,'entryId':eid,'r2ApplicationSide':(app,eid) in oldforward,
        'r2EntrySide':(app,eid) in oldreverse,'decision':'include' if keep else 'exclude','reason':reason})
extra=[]
for app,n in REJECTED:
    eid=entries[n]['id']
    assert (app,eid) not in edgekeys
    if (app,eid) in oldforward&oldreverse:
        extra.append({'applicationId':app,'entryId':eid,'decision':'exclude','reason':REJECTED[(app,n)]})
assert edgekeys<=oldforward|oldreverse  # This correction adds no unrelated new proof interface.
for a in apps['applications']:
    a['revision2NewEntryIds']=a['newEntryIds']
    a['newEntryIds']=sorted(e for app,e in edgekeys if app==a['id'])
for e in entries.values():
    e['revision2BaselineApplications']=e['baselineApplications']
    e['baselineApplications']=sorted(a for a,entry in edgekeys if entry==e['id'])
ordinary=next(a for a in apps['applications'] if a['id']=='V13-ORDINARY-GATE')
ordinary['revision2DeltaClassification']=ordinary['deltaClassification']
ordinary['deltaClassification']='accepted_exact319_ordinary_lifts_only_no_selected315_lift_in_scope'
ordinary['ordinaryArtifactScope']={
    'acceptedSourceId':'exact319',
    'acceptedArtifactIds':['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336'],
    'selected315LiftIncluded':False,
    'cutoff':'Retains revision2 scope. This is not a claim about later sparse315 or ordinary-sparse315 packets.'}
apps['revision']=3
apps['status']='Preparatory revision3 correcting the r2 relation and scoped ordinary classification; independent inventory review pending.'
apps['canonicalRelation']='CANONICAL-RELATION.json'
mapping=read(OLD/'INTEGRATION-MAP.json')
mapping['outline']['path']=(HERE/'PROOF-INTEGRATION-OUTLINE.tex').relative_to(ROOT).as_posix()
mapping['canonicalRelation']='CANONICAL-RELATION.json'
byid={a['id']:a for a in apps['applications']}
for m in mapping['entries']:
    ids=sorted(a for a,e in edgekeys if e==m['entryId'])
    m['inventoryConsumers']=[{'applicationId':a,'baselineConsumerSpans':byid[a]['baselineConsumers']} for a in ids]
write('CANONICAL-RELATION.json',relation)
write('EDGE-DECISIONS.json',{'r2DisagreementApplications':len({d['applicationId'] for d in decisions}),
    'disputedEdges':decisions,'additionalRejectedAgreedEdges':extra,
    'method':'Manual SPEC with explicit reasons; both public directions and integration map generated from this single relation, not their union.'})
write('APPLICATION-DELTA.json',apps)
write('INTEGRATION-MAP.json',mapping)
write('PREVIOUS-REVISION.json',prior)
write('SOURCE-PINS.json',pins)
print(json.dumps({'edges':len(edges),'disputedEdges':len(decisions),'applications':39,'entries':23,'additionalRejectedAgreedEdges':len(extra)}))
