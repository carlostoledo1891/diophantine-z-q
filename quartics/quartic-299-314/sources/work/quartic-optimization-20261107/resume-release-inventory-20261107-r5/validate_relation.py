"""Validate the single relation, its views and source-specific artifact identities."""
def validate(apps,relation,mapping,catalog):
    aa={a['id']:a for a in apps['applications']};ee={e['id']:e for e in apps['newInternalEntries']}
    assert len(aa)==len(apps['applications'])==39
    assert len(ee)==len(apps['newInternalEntries'])==42
    assert all(any(e.startswith('N'+str(i)+'-') for e in ee) for i in range(24,43))
    raw=[(r['applicationId'],r['entryId']) for r in relation['edges']];edges=set(raw)
    assert len(raw)==len(edges) and all(a in aa and e in ee for a,e in edges)
    components=catalog['components'];variants=catalog['polynomialVariants']
    assert len(components)==35 and len(variants)==2
    known=set(components)|set(variants)
    for r in relation['edges']:
        e=ee[r['entryId']]
        assert r['scope']=={'selectedCandidateDependency':e['selectedCandidateDependency'],'componentIds':e.get('coveredComponentIds',[e['component']])}
        assert r['sourceProof']==e['authorProof'] and r['reason'].strip()
        if int(e['id'][1:3])>=34:assert set(r['scope']['componentIds'])<=known
    forward=[];reverse=[]
    for a in aa.values():
        assert len(a['newEntryIds'])==len(set(a['newEntryIds']))
        forward.extend((a['id'],e) for e in a['newEntryIds'])
    for e in ee.values():
        assert e['newApprovalCreatedHere'] is False
        assert len(e['baselineApplications'])==len(set(e['baselineApplications']))
        reverse.extend((a,e['id']) for a in e['baselineApplications'])
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
            assert c['baselineConsumerSpans']==aa[a]['baselineConsumers'];mapped.append((a,eid))
    assert set(mapped)==edges
    ordinary=aa['V13-ORDINARY-GATE']
    assert ordinary['deltaClassification']=='accepted_source_specific_exact319_sparse314_anchor313_reciprocal307_lifts'
    expected={'exact319':['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336'],'sparseShared314':['ordinaryShared314_331','ordinaryShared314_330','ordinaryShared314_329'],'anchorGamma313':['ordinaryAnchor313_330','ordinaryAnchor313_329','ordinaryAnchor313_328'],'reciprocal307':['ordinaryReciprocal307_324','ordinaryReciprocal307_323','ordinaryReciprocal307_322']}
    scope=ordinary['ordinaryArtifactScope']
    assert scope['acceptedFamilies']==expected and scope['selectedCandidateId']=='reciprocal307'
    assert scope['selectedCandidateLiftIncluded'] is True and scope['weightedPolynomialVariants']==['positiveWeights328']
    assert catalog['ordinaryScope']==scope and catalog['selectedAcceptedCandidate']=='reciprocal307'
    selected=components['reciprocal307']
    assert apps['selectedCandidateId']==catalog['selectedAcceptedCanonicalId']==selected['canonicalCandidateId']
    assert selected['variables']==307 and selected['recordedReviewer']=='01'
    assert selected['review']['sha256']=='055f82695b4757c534f5d8a915afe2ede778730f3291fd2b1da6d69564d472e8'
    assert selected['maximumCoefficientExpression']=='186624*C^2, C=3^(2^25)'
    for source,children in expected.items():
        for cid in children:
            child=components[cid];assert child['comparedWith']==source
            if source=='reciprocal307':assert child['conditionalReviewDischargedBy']==selected['review']
    for cid,parent in [('positiveWeights313','anchorGamma313'),('positiveWeights328','ordinaryAnchor313_328')]:
        v=variants[cid]
        assert v['kind']=='positive_weighted_compiler_variant_no_new_IR'
        assert v['residualSource']==parent and v['residualSourceCanonicalId']==components[parent]['canonicalCandidateId']
        assert v['canonicalPolynomialId']=='sha256:'+v['polynomial']['sha256']
        assert v['variables']==components[parent]['variables'] and v['residuals']==components[parent]['residuals']
        assert v['componentAuthor']=='root' and v['recordedReviewer']=='01' and v['newApprovalCreatedHere'] is False
    assert variants['positiveWeights313']['polynomial']['sha256']=='c7863b51f07115db9f5f0d9ecce4173921a40bb93d02d442eb0bb98b480c1101'
    assert variants['positiveWeights328']['polynomial']['sha256']=='25cac3ad2777b39e628795bc2ea598932228796b822f03df5bc3cc832b313337'
    return len(edges)
