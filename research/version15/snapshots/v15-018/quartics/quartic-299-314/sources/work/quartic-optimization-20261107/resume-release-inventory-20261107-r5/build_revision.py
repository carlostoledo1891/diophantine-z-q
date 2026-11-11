"""Build preparatory r5 from frozen r4; execute no candidate program."""
from pathlib import Path
import copy,hashlib,json
from spec import NEW,O,U
H=Path(__file__).resolve().parent; ROOT=H.parents[2]
OLD=H.with_name('resume-release-inventory-20261107-r4')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_bytes())
def write(n,v):(H/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert sha(OLD/'FROZEN-MANIFEST.json')=='82c69afd7fbe52ba96617b6430346bc5fb77a8acf6ef7ef54c7afe4c5cb8b660'
for n,r in load(OLD/'FROZEN-MANIFEST.json').items():assert sha(OLD/n)==r['sha256']
pins=load(OLD/'SOURCE-PINS.json')
def ref(path):
    p=ROOT/path
    pins[path]={'sha256':sha(p),'bytes':p.stat().st_size}
    return {'path':path,'sha256':sha(p)}
def section(path,heading):
    r=ref(path);ls=(ROOT/path).read_text(encoding='utf-8').splitlines()
    if heading=='Whole report':return dict(r,heading=heading,startLine=1,endLine=len(ls))
    loc=[i for i,l in enumerate(ls) if l==heading];assert len(loc)==1,(path,heading)
    start=loc[0];end=next((i for i in range(start+1,len(ls)) if ls[i].startswith('## ')),len(ls))
    return dict(r,heading=heading,startLine=start+1,endLine=end)
previous={p.name:ref(p.relative_to(ROOT).as_posix()) for p in OLD.iterdir() if p.is_file()}
oldreview=ref(O+'resume-review-inventory-r4-01/REVIEW.md')
assert oldreview['sha256']=='2e85fde8b45ad2a5196c436d4a5c93f913b1fd86f213ae0370c2412e2a2da8f5'
fullreview=ref(O+'resume-review-reciprocal307-01/REVIEW.md')
assert fullreview['sha256']=='055f82695b4757c534f5d8a915afe2ede778730f3291fd2b1da6d69564d472e8'
apps=load(OLD/'APPLICATION-DELTA.json');cat=load(OLD/'CANDIDATES.json')
rel=load(OLD/'CANONICAL-RELATION.json');mapping=load(OLD/'INTEGRATION-MAP.json')
apps['revision']=5;apps['status']='Preparatory r5; records existing independent acceptances; inventory review pending.'
apps['priorEntryScope']='N01..N33 retain their exact r4 records and cutoff statements; newly included families are recorded by N34..N42.'
for d in NEW:
    e=dict(id=d['id'],component=d['component'],kind=d['kind'],selectedCandidateDependency=d['selected'],oldObject=d['old'],newObject=d['new'],requiredInternalLemmaOrMap=d['lemma'],baselineApplications=[],authorProof=[section(*s) for s in d['sources']],recordedReview=ref(d['review']),author=d['author'],reviewer=d['reviewer'],recordedStatus='accepted_exact_component_by_recorded_non_author',newApprovalCreatedHere=False,actualConsumer=d['consumers'],arithmeticInputClassification=d['inputs'])
    if 'covered' in d:e['coveredComponentIds']=d['covered']
    if d['component']=='reciprocal307':
        e['fullCandidateInterfaceReview']=fullreview
        e['physicalConsumerCertificate']=ref(O+'reciprocal307-20261107/CERTIFICATE.json')
    apps['newInternalEntries'].append(e)
    for target in d['targets'].split():rel['edges'].append({'applicationId':'V13-'+target,'entryId':d['id'],'reason':d['consumers'],'scope':{'selectedCandidateDependency':d['selected'],'componentIds':d.get('covered',[d['component']])},'sourceProof':e['authorProof']})
rel['status']='author_prepared_r5_pending_independent_inventory_review'
rel['edges'].sort(key=lambda e:(e['applicationId'],e['entryId']))
edges={(e['applicationId'],e['entryId']) for e in rel['edges']}
entries={e['id']:e for e in apps['newInternalEntries']}
for a in apps['applications']:
    a['revision4NewEntryIds']=a['newEntryIds'];a['newEntryIds']=sorted(e for x,e in edges if x==a['id'])
    if a['newEntryIds']!=a['revision4NewEntryIds']:
        a['revision4DeltaClassification']=a['deltaClassification'];a['deltaClassification']='updated_with_explicit_r5_application_entries'
for e in entries.values():e['baselineApplications']=sorted(a for a,b in edges if b==e['id'])
ordinary=next(a for a in apps['applications'] if a['id']=='V13-ORDINARY-GATE')
ordinary['revision4OrdinaryArtifactScope']=copy.deepcopy(ordinary['ordinaryArtifactScope'])
families=copy.deepcopy(ordinary['ordinaryArtifactScope']['acceptedFamilies'])
families.update(anchorGamma313=['ordinaryAnchor313_330','ordinaryAnchor313_329','ordinaryAnchor313_328'],reciprocal307=['ordinaryReciprocal307_324','ordinaryReciprocal307_323','ordinaryReciprocal307_322'])
ordinary['deltaClassification']='accepted_source_specific_exact319_sparse314_anchor313_reciprocal307_lifts'
ordinary['ordinaryArtifactScope']={'acceptedFamilies':families,'selectedCandidateId':'reciprocal307','selectedCandidateLiftIncluded':True,'weightedPolynomialVariants':['positiveWeights328'],'meaning':'Each lift has its own source and review. Weighted328 uses ordinaryAnchor313_328, not reciprocal307.'}

def candidate(cid,folder,irname,report,review,author,reviewer,parent,poly):
    ip=folder+'/'+irname;ir=load(ROOT/ip);old=load(ROOT/cat['components'][parent]['candidate']['path'])
    delta={}
    for k in ('coordinates','residuals'):
        a={v['id']:v for v in old[k]};b={v['id']:v for v in ir[k]}
        delta[k]={'deleted':sorted(a.keys()-b.keys()),'added':sorted(b.keys()-a.keys()),'changed':sorted(i for i in a.keys()&b.keys() if a[i]!=b[i])}
    item=dict(id=cid,displayId=cid,candidate=ref(ip),report=ref(report),review=ref(review),componentAuthor=author,recordedReviewer=reviewer,recordedStatus='accepted_component',comparedWith=parent,variables=len(ir['coordinates']),residuals=len(ir['residuals']),newApprovalCreatedHere=False,countIsNotIdentity=True,objectDelta=delta,polynomial=ref(folder+'/'+poly))
    item['canonicalCandidateId']='sha256:'+item['candidate']['sha256'];cat['components'][cid]=item
    cat['dependencyEdges'].append({'candidate':cid,'dependsOn':parent,'role':'immediate exact source; application obligations separately recorded'})
    return item
for n in (330,329,328):
    x=candidate('ordinaryAnchor313_'+str(n),U+'ordinary-anchor313/'+str(n),'candidate-ir.json',U+'ordinary-anchor313/REPORT.md',O+'resume-review-ordinary313-20261107/REVIEW.md','10','05','anchorGamma313','polynomial.json')
    x['decimalPolynomial']=ref(U+'ordinary-anchor313/'+str(n)+'/polynomial.txt');x['maximumCoefficientBits']={330:1627,329:3250,328:6496}[n]
x=candidate('reciprocal307',O+'reciprocal307-20261107','candidate307-ir.json',O+'reciprocal307-20261107/REPORT.md',fullreview['path'],'BL+root+10+05','01','anchorGamma313','polynomial307.json')
assert x['candidate']['sha256']=='0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1'
x['conditionalArithmeticReview']=ref(U+'review-auxiliary-domain313/REVIEW.md')
x['reviewScope']='Full307 algebra/interface and finite delta accepted relative to inherited313 arithmetic; auxiliary arithmetic independently accepted by10. No global theorem recertification.'
x['monomials']=6438;x['maximumCoefficientExpression']='186624*C^2, C=3^(2^25)'
for n in (324,323,322):
    x=candidate('ordinaryReciprocal307_'+str(n),U+'ordinary-reciprocal307/'+str(n),'candidate-ir.json',U+'ordinary-reciprocal307/REPORT.md',O+'resume-review-ordinary307-20261107/REVIEW.md','10','05','reciprocal307','polynomial.json')
    x['decimalPolynomial']=ref(U+'ordinary-reciprocal307/'+str(n)+'/polynomial.txt');x['maximumCoefficientBits']={324:1627,323:3250,322:6496}[n]
    x['monomials']={324:6486,323:6483,322:6480}[n]
    x['conditionalReviewDischargedBy']=fullreview
cat['polynomialVariants']={}
for cid,parent,file,monos in [('positiveWeights313','anchorGamma313','weighted-polynomial.json',5982),('positiveWeights328','ordinaryAnchor313_328','ordinary328-polynomial.json',6024)]:
    item={'id':cid,'kind':'positive_weighted_compiler_variant_no_new_IR','residualSource':parent,'residualSourceCanonicalId':cat['components'][parent]['canonicalCandidateId'],'variables':cat['components'][parent]['variables'],'residuals':cat['components'][parent]['residuals'],'monomials':monos,'weights':ref(O+'root-sparse313/integer-weights/WEIGHTS.json'),'polynomial':ref(O+'root-sparse313/integer-weights/'+file),'report':ref(O+'root-sparse313/REPORT.md'),'review':ref(O+'resume-review-weighted313-01/REVIEW.md'),'componentAuthor':'root','recordedReviewer':'01','recordedStatus':'accepted_compiler_variant','newApprovalCreatedHere':False,'map':'Identity on all original rational witnesses; all weights strictly positive integers.'}
    item['canonicalPolynomialId']='sha256:'+item['polynomial']['sha256']
    if cid.endswith('328'):item['decimalPolynomial']=ref(O+'root-sparse313/integer-weights/ordinary328-polynomial.txt');item['maximumCoefficientBits']=6496
    else:item['maximumCoefficientExpression']='186624*C^2+64, C=3^(2^25)'
    cat['polynomialVariants'][cid]=item
cat['revision4SelectedCandidate']=cat['selectedAcceptedCandidate'];cat['selectedAcceptedCandidate']='reciprocal307'
cat['selectedAcceptedCanonicalId']=cat['components']['reciprocal307']['canonicalCandidateId'];apps['selectedCandidateId']=cat['selectedAcceptedCanonicalId']
cat['selectedAcceptedLineage']+=['reciprocal307']
cat['revision4OrdinaryScope']=cat['ordinaryScope'];cat['ordinaryScope']=ordinary['ordinaryArtifactScope']
cat['publication']='307 remains above strict below300 threshold; research preparation only.'
cat['identityConvention']='IR identities remain sha256(IR). Compiler variants have distinct sha256(polynomial) IDs and explicit unchanged residual-source identities; no invented new IR.'
cat['agentIdentityAliases'].update(root='/root',BL='/root/astra_bl_horizontal_repair')
cat['soundnessOrderFor307']=['Use explicit raw curves and three-slope closure to produce oriented roots.','Use unchanged height-product inverse chain to prove c nonzero, restore b=yR/a and old2E roots.','Restore old parity, height, H/V0 exceptional exclusions before logarithms.','Use allE pre-H valuation periods and low tests; apply torsion-killed logarithm identities, unit transfer and depth10H bootstrap.','Retain old order10/40 label congruences, scalar depth24 and final conclusions.']
cat['completenessOrderFor307']=['Use accepted313 complete witnesses and same root points.','Map old reciprocal values to f=r^2,h=-Jr and analogous alternate pair.','Use actual rational chord or tangent slope; regular ratios hold including O.','All retained downstream values and finite/real/prime choices are unchanged.']

oldmap={e['entryId']:e for e in mapping['entries']}
tex=(OLD/'PROOF-INTEGRATION-OUTLINE.tex').read_text(encoding='utf-8')
tex=tex.replace('\\begin{document}','\\begin{document}\n\\paragraph{Revision 5 scope.} Earlier sections retain their historical cutoffs. The appended entries record the accepted 307 route, ordinary companions and separate weighted compiler variants. This is preparatory exposition only.\n',1)
def esc(s):
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#'),('^',r'\textasciicircum{}')]:s=s.replace(a,b)
    return s
extra=['\\section{Revision 5: reciprocal auxiliary domains and source-specific compiler variants}']
for d in NEW:extra+=['\\subsection{'+esc(d['id'])+'}','\\label{outline:r5-'+d['id'].lower()+'}',esc(d['lemma']),'\\par '+esc(d['inputs']),'\\par Consumers: '+esc(d['consumers'])]
tex=tex.replace('\\end{document}','\n'.join(extra)+'\n\\end{document}');(H/'PROOF-INTEGRATION-OUTLINE.tex').write_text(tex,encoding='utf-8')
ls=tex.splitlines();mm=[]
for e in entries.values():
    label=oldmap[e['id']]['outlineLabel'] if e['id'] in oldmap else 'outline:r5-'+e['id'].lower()
    loc=[i+1 for i,l in enumerate(ls) if '\\label{'+label+'}' in l];assert len(loc)==1
    mm.append({'entryId':e['id'],'outlineLabel':label,'outlineLabelLine':loc[0],'authorProof':e['authorProof'],'recordedNonAuthorReview':e['recordedReview'],'inventoryConsumers':[{'applicationId':a['id'],'baselineConsumerSpans':a['baselineConsumers']} for a in apps['applications'] if a['id'] in e['baselineApplications']],'actualConsumer':e.get('actualConsumer','Inherited r4 consumer binding; unchanged.')})
mapping.update(entries=mm,outline=ref((H/'PROOF-INTEGRATION-OUTLINE.tex').relative_to(ROOT).as_posix()),status='Preparatory r5 outline, not final exposition approval.')
retained=load(OLD/'RETAINED-SOURCES.json');retained['revision5ArithmeticInputs']=[{'entryId':e['id'],'classification':e['arithmeticInputClassification'],'proof':e['authorProof']} for e in apps['newInternalEntries'] if e['id'].startswith(tuple('N'+str(i) for i in range(34,43)))]
inputs=load(OLD/'NEW-INPUT-CLASSIFICATION.json');vp='work/quartic-version6-release/repository/manuscripts/quartic_v13.tex';vref=ref(vp);vl=(ROOT/vp).read_text(encoding='utf-8').splitlines()
def span(a,b):return dict(vref,startLine=a,endLine=b,sha256_normalized_LF_span=hashlib.sha256(('\n'.join(vl[a-1:b])+'\n').encode()).hexdigest())
for name,a,b,ids,qual in [
 ('Root squareclass kernel and full group decomposition',19539,19564,['N38-AUXILIARY-TORSION-LOG-TRANSFER','N41-ROOT-RESTORATION-AND-COMPLETENESS'],'Roots require restored nonzero square abscissa; auxiliary free indices may lie in halfZ and carry2torsion.'),
 ('Formal-unit ratios and exact approximation orders',20830,20900,['N36-AUXILIARY-ALL-E-VALUATIONS','N38-AUXILIARY-TORSION-LOG-TRANSFER'],'Use only after local formality; extra2 kills both torsions; depth10H obtained before precision40 use.'),
 ('Shared primary sign and ratio convention',20924,20935,['N37-ZERO-SAFE-RAW-RATIOS'],'S=-1/z(H); raw h=-y/x^2 and regular denominator1-DY.'),
 ('Global N/Q nonvanishing and enlargedH log identities',21060,21156,['N38-AUXILIARY-TORSION-LOG-TRANSFER','N39-GLOBAL-APPROXIMANT-DOMAIN'],'Reuse exact N/Q on allE cosets. The old smaller group coefficients are replaced by doubled coefficients for auxiliary torsion.')]:
    inputs['retainedArithmeticApplications'].append({'name':name,'source':span(a,b),'newEntries':ids,'qualifications':qual})
inputs['revision5InternalStatements']=[d['id']+': '+d['lemma'] for d in NEW]
inputs['revision5Boundary']='No new external theorem is assumed. New uses of the existing group, formal-log, nonvanishing and root-descent inputs are bound above. Literal algebra and ordered-Q positive-square equivalence are internal.'
alternatives=load(OLD/'PRESERVED-ALTERNATIVES.json')
for p,reason in [(O+'resume-auxiliary-domain-20261107/PROPOSAL.md','Original single addition equation remains insufficient on f=F,k=-h. Acceptance of its conditional arithmetic does not accept that equation.'),(O+'resume-depth-20261107/root-domain313/REPORT.md','Exploratory enlarged-root, input-repair and torsion-CRT alternatives are NOT inputs to accepted307; roots retain2E.'),(O+'resume-anchor-post313-20261107/PROGRESS.md','Earlier affine-anchor slice obstructions remain exploratory, not full-circuit counterexamples.'),(O+'root-sparse313/REPORT.md','Only positive integer weights are accepted; earlier rational-weight search is not adopted.')]:alternatives.append({'source':ref(p),'disposition':reason})
# Pin exact physical consumer certificate and every new author/reviewer manifest as evidence.
for p in [O+'reciprocal307-20261107/CERTIFICATE.json',O+'reciprocal307-20261107/MANIFEST.json',O+'resume-review-reciprocal307-01/PACKET-CHECKS.json',O+'root-sparse313/MANIFEST.json',U+'ordinary-anchor313/MANIFEST.json',U+'ordinary-reciprocal307/MANIFEST.json',O+'resume-review-ordinary307-20261107/CHECKS.json',O+'resume-review-weighted313-01/CHECKS.json']:ref(p)
for n,v in [('APPLICATION-DELTA.json',apps),('CANDIDATES.json',cat),('CANONICAL-RELATION.json',rel),('INTEGRATION-MAP.json',mapping),('RETAINED-SOURCES.json',retained),('NEW-INPUT-CLASSIFICATION.json',inputs),('PRESERVED-ALTERNATIVES.json',alternatives),('PREVIOUS-REVISION.json',{'files':previous,'independentReview':oldreview}),('SOURCE-PINS.json',pins)]:write(n,v)
index=['# Exact candidate and polynomial identities, revision5','','IR hash identifies a residual system. Polynomial variants below additionally identify their compiler output.','', '| ID | Variables | Parent | Exact identity |','|---|---:|---|---|']
for cid,x in cat['components'].items():index.append(f"| {cid} | {x['variables']} | {x.get('comparedWith')} | {x['canonicalCandidateId']} |")
for cid,x in cat['polynomialVariants'].items():index.append(f"| {cid} | {x['variables']} | {x['residualSource']} | polynomial {x['canonicalPolynomialId']} |")
(H/'CANONICAL-INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
print(json.dumps({'applications':len(apps['applications']),'entries':len(entries),'edges':len(edges),'IRs':len(cat['components']),'polynomialVariants':len(cat['polynomialVariants'])}))
