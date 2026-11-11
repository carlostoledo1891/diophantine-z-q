"""Validate the canonical relation in every direction; no candidate execution."""
def validate(apps,relation,mapping):
    app={a['id']:a for a in apps['applications']}
    ent={e['id']:e for e in apps['newInternalEntries']}
    assert len(app)==len(apps['applications'])
    assert len(ent)==len(apps['newInternalEntries'])
    raw=[(e['applicationId'],e['entryId']) for e in relation['edges']]
    canonical=set(raw)
    assert len(canonical)==len(raw),'duplicate canonical edge'
    assert all(a in app and e in ent for a,e in canonical),'unknown endpoint'
    for e in relation['edges']:
        source=ent[e['entryId']]
        assert e['scope']['selected315Dependency'] is source['selected315Dependency'],'scope drift'
        assert e['scope']['componentIds']==source.get('coveredComponentIds',[source['component']]),'component scope drift'
        assert e['sourceProof']==source['authorProof'],'proof drift'
        assert isinstance(e['reason'],str) and e['reason'].strip()
    forward=[]
    for a in app.values():
        assert len(a['newEntryIds'])==len(set(a['newEntryIds'])),'duplicate app edge'
        forward += [(a['id'],e) for e in a['newEntryIds']]
    reverse=[]
    for e in ent.values():
        assert len(e['baselineApplications'])==len(set(e['baselineApplications'])),'duplicate entry edge'
        reverse += [(a,e['id']) for a in e['baselineApplications']]
    assert set(forward)==canonical,'application direction differs'
    assert set(reverse)==canonical,'entry direction differs'
    assert len({m['entryId'] for m in mapping['entries']})==len(mapping['entries'])
    assert {m['entryId'] for m in mapping['entries']}==set(ent)
    mapped=[]
    for m in mapping['entries']:
        seen=[]
        for c in m['inventoryConsumers']:
            a=c['applicationId'];seen.append(a)
            assert a in app
            assert c['baselineConsumerSpans']==app[a]['baselineConsumers'],'consumer span drift'
            mapped.append((a,m['entryId']))
        assert len(seen)==len(set(seen)),'duplicate map edge'
    assert set(mapped)==canonical,'integration map differs'
    ordinary=app['V13-ORDINARY-GATE']
    assert ordinary['deltaClassification']=='accepted_exact319_ordinary_lifts_only_no_selected315_lift_in_scope'
    assert ordinary['ordinaryArtifactScope']['acceptedSourceId']=='exact319'
    assert ordinary['ordinaryArtifactScope']['acceptedArtifactIds']==['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336']
    assert ordinary['ordinaryArtifactScope']['selected315LiftIncluded'] is False
    return len(canonical)
