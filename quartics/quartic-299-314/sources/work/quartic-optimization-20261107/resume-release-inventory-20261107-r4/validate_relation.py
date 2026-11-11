"""Check all relation projections, scopes and source-specific ordinary status."""
def validate(apps,relation,mapping,catalog):
    aa={a['id']:a for a in apps['applications']};ee={e['id']:e for e in apps['newInternalEntries']}
    assert len(aa)==len(apps['applications'])==39
    assert len(ee)==len(apps['newInternalEntries'])==33
    assert 'N25-H-DEPTH-BOOTSTRAP' in ee and 'N32-ANCHOR-RATIONAL-APPROXIMATION' in ee
    raw=[(r['applicationId'],r['entryId']) for r in relation['edges']];edges=set(raw)
    assert len(edges)==len(raw) and all(a in aa and e in ee for a,e in edges)
    for r in relation['edges']:
        e=ee[r['entryId']]
        assert r['scope']=={'selectedCandidateDependency':e['selectedCandidateDependency'],'componentIds':e.get('coveredComponentIds',[e['component']])}
        assert r['sourceProof']==e['authorProof'] and r['reason'].strip()
    forward=[];reverse=[]
    for a in aa.values():
        assert len(a['newEntryIds'])==len(set(a['newEntryIds']))
        forward += [(a['id'],e) for e in a['newEntryIds']]
    for e in ee.values():
        assert e['newApprovalCreatedHere'] is False
        assert len(e['baselineApplications'])==len(set(e['baselineApplications']))
        reverse += [(a,e['id']) for a in e['baselineApplications']]
        if int(e['id'][1:3])>=24:
            assert e['reviewer'] not in e['author'].split('+')
            assert e['actualConsumer'].strip() and e['arithmeticInputClassification'].strip()
    assert set(forward)==set(reverse)==edges
    mm={m['entryId']:m for m in mapping['entries']};assert len(mm)==len(mapping['entries']) and set(mm)==set(ee)
    mapped=[]
    for eid,m in mm.items():
        assert m['authorProof']==ee[eid]['authorProof'] and m['recordedNonAuthorReview']==ee[eid]['recordedReview']
        if 'actualConsumer' in ee[eid]:assert m['actualConsumer']==ee[eid]['actualConsumer']
        seen=set()
        for c in m['inventoryConsumers']:
            a=c['applicationId'];assert a in aa and a not in seen;seen.add(a)
            assert c['baselineConsumerSpans']==aa[a]['baselineConsumers']
            mapped.append((a,eid))
    assert set(mapped)==edges
    ordinary=aa['V13-ORDINARY-GATE']
    assert ordinary['deltaClassification']=='accepted_exact319_and_sparseShared314_lifts_no_anchorGamma313_lift_in_scope'
    expected={'exact319':['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336'],'sparseShared314':['ordinaryShared314_331','ordinaryShared314_330','ordinaryShared314_329']}
    assert ordinary['ordinaryArtifactScope']['acceptedFamilies']==expected
    assert ordinary['ordinaryArtifactScope']['selectedCandidateId']=='anchorGamma313'
    assert ordinary['ordinaryArtifactScope']['selectedCandidateLiftIncluded'] is False
    assert catalog['ordinaryScope']==ordinary['ordinaryArtifactScope']
    assert catalog['selectedAcceptedCandidate']=='anchorGamma313'
    selected=catalog['components']['anchorGamma313']
    assert apps['selectedCandidateId']==catalog['selectedAcceptedCanonicalId']==selected['canonicalCandidateId']
    assert selected['variables']==313 and selected['recordedReviewer']=='10'
    for source,children in expected.items():
        for cid in children:assert catalog['components'][cid]['comparedWith']==source
    return len(edges)
