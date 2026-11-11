"""Build R6 only after the final corrected299 reviews have been read and pinned."""
from pathlib import Path
import copy,hashlib,json
from spec import NEW,O,U,E
H=Path(__file__).resolve().parent;ROOT=H.parents[2];OLD=H.with_name('resume-release-inventory-20261107-r5')
REVIEW299_SHA='f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699'
REVIEW_S_SHA='2f59aebb6074faea51a64204b734eb14a68fecdeb387541f93b86651681e0bc2'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_bytes())
def write(n,v):(H/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert sha(OLD/'FROZEN-MANIFEST.json')=='806ebae648a51487df9661b3f4d25b3142dd3435f8e1ac0b058f554747ebbf1f'
for n,r in load(OLD/'FROZEN-MANIFEST.json').items():assert sha(OLD/n)==r['sha256']
assert isinstance(REVIEW299_SHA,str) and isinstance(REVIEW_S_SHA,str),'Final299 review not yet recorded'
pins=load(OLD/'SOURCE-PINS.json')
def ref(path):
    p=ROOT/path;pins[path]={'sha256':sha(p),'bytes':p.stat().st_size};return {'path':path,'sha256':sha(p)}
def section(path,heading):
    r=ref(path);ls=(ROOT/path).read_text(encoding='utf-8').splitlines()
    if heading=='Whole report':return dict(r,heading=heading,startLine=1,endLine=len(ls))
    loc=[i for i,l in enumerate(ls) if l==heading];assert len(loc)==1,(path,heading)
    start=loc[0];end=next((i for i in range(start+1,len(ls)) if ls[i].startswith('## ')),len(ls))
    return dict(r,heading=heading,startLine=start+1,endLine=end)
prior={p.name:ref(p.relative_to(ROOT).as_posix()) for p in OLD.iterdir() if p.is_file()}
oldreview=ref(O+'resume-review-inventory-r5-sol/REVIEW.md');assert oldreview['sha256']=='1b41b4fab9b32caaa1dc34a2ffc13be7f4ac777995e1df85cf040c87b66687d7'
finalreview=ref(U+'review-reciprocal299/REVIEW.md');assert finalreview['sha256']==REVIEW299_SHA
sreview=ref(O+'resume-depth-20261107/review-s299/REVIEW.md');assert sreview['sha256']==REVIEW_S_SHA
apps=load(OLD/'APPLICATION-DELTA.json');cat=load(OLD/'CANDIDATES.json');rel=load(OLD/'CANONICAL-RELATION.json');mapping=load(OLD/'INTEGRATION-MAP.json')
apps['revision']=6;apps['status']='Preparatory R6; existing final reviews recorded, independent inventory review pending.'
apps['priorEntryScope']='N01..N42 retain their exact previous records and cutoff statements. N43..N48 cover301, corrected299-r2 and its ordinary lifts; failed299 is adverse history, never accepted.'
for d in NEW:
    e=dict(id=d['id'],component=d['component'],kind=d['kind'],selectedCandidateDependency=d['selected'],oldObject=d['old'],newObject=d['new'],requiredInternalLemmaOrMap=d['lemma'],baselineApplications=[],authorProof=[section(*s) for s in d['sources']],recordedReview=ref(d['review']),author=d['author'],reviewer=d['reviewer'],recordedStatus='accepted_exact_component_by_recorded_non_author',newApprovalCreatedHere=False,actualConsumer=d['consumers'],arithmeticInputClassification=d['inputs'])
    if 'covered' in d:e['coveredComponentIds']=d['covered']
    if d['component']=='reciprocal299r2':e.update(additionalSApplicationReview=sreview,physicalConsumerCertificate=ref(E+'reciprocal299-r2/CERTIFICATE.json'))
    elif d['component']=='reciprocal301':e['physicalConsumerCertificate']=ref(E+'reciprocal301/CERTIFICATE.json')
    apps['newInternalEntries'].append(e)
    for target in d['targets'].split():rel['edges'].append({'applicationId':'V13-'+target,'entryId':d['id'],'reason':d['consumers'],'scope':{'selectedCandidateDependency':d['selected'],'componentIds':d.get('covered',[d['component']])},'sourceProof':e['authorProof']})
rel['status']='author_prepared_r6_pending_independent_inventory_review';rel['edges'].sort(key=lambda e:(e['applicationId'],e['entryId']))
edges={(e['applicationId'],e['entryId']) for e in rel['edges']};entries={e['id']:e for e in apps['newInternalEntries']}
for a in apps['applications']:
    a['revision5NewEntryIds']=a['newEntryIds'];a['newEntryIds']=sorted(e for x,e in edges if x==a['id'])
    if a['newEntryIds']!=a['revision5NewEntryIds']:
        a['revision5DeltaClassification']=a['deltaClassification'];a['deltaClassification']='updated_with_explicit_r6_application_entries'
for e in entries.values():e['baselineApplications']=sorted(a for a,b in edges if b==e['id'])
ordinary=next(a for a in apps['applications'] if a['id']=='V13-ORDINARY-GATE')
ordinary['revision5OrdinaryArtifactScope']=copy.deepcopy(ordinary['ordinaryArtifactScope'])
ordinary['deltaClassification']='accepted_source_specific_299_lifts_selected314_bound_2pow6496'
ordinary['ordinaryArtifactScope']['acceptedFamilies']['reciprocal299r2']=['ordinaryReciprocal299_316','ordinaryReciprocal299_315','ordinaryReciprocal299_314']
ordinary['ordinaryArtifactScope'].update(selectedCandidateId='reciprocal299r2',selectedCandidateLiftIncluded=True,selectedOrdinaryCompanion='ordinaryReciprocal299_314',selectedStrictCoefficientBound='2^6496',meaning='Earlier source-specific families remain accepted. All three corrected299 lifts are included; selected314 uses the updated strict2^6496 bound.')

def addcandidate(cid,folder,name,parent,review,poly=None,report=None,author=None,reviewer='10'):
    irp=folder+'/'+name;ir=load(ROOT/irp);old=load(ROOT/cat['components'][parent]['candidate']['path']);delta={}
    for k in ('coordinates','residuals'):
        a={x['id']:x for x in old[k]};b={x['id']:x for x in ir[k]}
        delta[k]={'deleted':sorted(a.keys()-b.keys()),'added':sorted(b.keys()-a.keys()),'changed':sorted(i for i in a.keys()&b.keys() if a[i]!=b[i])}
    item=dict(id=cid,displayId=cid,candidate=ref(irp),report=ref(report or folder+'/REPORT.md'),review=review,componentAuthor=author or ('01' if cid=='reciprocal301' else 'root+01'),recordedReviewer=reviewer,recordedStatus='accepted_component',comparedWith=parent,variables=len(ir['coordinates']),residuals=len(ir['residuals']),newApprovalCreatedHere=False,countIsNotIdentity=True,objectDelta=delta,polynomial=ref(folder+'/'+(poly or 'polynomial'+str(len(ir['coordinates']))+'.json')))
    item['canonicalCandidateId']='sha256:'+item['candidate']['sha256'];item['maximumCoefficientExpression']='186624*C^2, C=3^(2^25)'
    cat['components'][cid]=item;cat['dependencyEdges'].append({'candidate':cid,'dependsOn':parent,'role':'immediate exact source; new global/domain obligations explicitly recorded'})
    return item
r301=ref(U+'review-reciprocal301/REVIEW.md');assert r301['sha256']=='ab035cfec699f36adddff3792a0de89a30c6719e59deef3f4361198bac2bd6aa'
x=addcandidate('reciprocal301',E+'reciprocal301','candidate301-ir.json','reciprocal307',r301);assert x['candidate']['sha256']=='ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6';x['monomials']=6423
x['equivalenceScope']='Inverse maps on complete rational zero sets, using global low tests to restore missing raw ratios.'
x=addcandidate('reciprocal299r2',E+'reciprocal299-r2','candidate299-ir.json','reciprocal301',finalreview);assert x['candidate']['sha256']=='8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815';x['monomials']=6630
x['additionalReview']=sreview;x['equivalenceScope']='Same rational input projection via enlarged S auxiliary domain; no private square-root-fiber bijection claimed.'
cat['revision5SelectedCandidate']=cat['selectedAcceptedCandidate'];cat['selectedAcceptedCandidate']='reciprocal299r2';cat['selectedAcceptedCanonicalId']=x['canonicalCandidateId'];apps['selectedCandidateId']=x['canonicalCandidateId']
cat['selectedAcceptedLineage']+=['reciprocal301','reciprocal299r2'];cat['revision5OrdinaryScope']=cat['ordinaryScope'];cat['ordinaryScope']=ordinary['ordinaryArtifactScope']
cat['publication']='Symbolic threshold is reached by accepted299. Selected ordinary314 has coefficients strictly below2^6496. This inventory is preparation, not exposition acceptance or publication authorization.'
cat['soundnessOrderFor299']=['Reconstruct every missing k and both curves by polynomial identities.','Use complete oriented closure and retained root conditions; S orientation row identifies the exact scalar point.','Use root-height/anchor to exclude empty radicals before any missing raw ratio or logarithm.','Use actual cache periods and low tests to prove1-D*F^2 nonzero, then restore missing raw ratios.','Apply all-four auxiliary-domain identities, global N/Q certificates, H bootstrap and original integer root-label arguments.']
cat['completenessOrderFor299']=['Use accepted301 complete witnesses.','Map old S square-root coordinates to raw reciprocals and choose the exact chord/tangent slope.','The same old oriented S root satisfies the added ordinate equation.','Keep all external values, finite/real neighborhoods, contact primes, scalar/anchor data and final H choices unchanged.']
ordinaryreview=ref(O+'resume-depth-20261107/review-ordinary299/REVIEW.md');assert ordinaryreview['sha256']=='13ed2acad2b751abfdb8000a931e6f93bd41b038a965f38c4c2d4902c17318db'
for n in (316,315,314):
    v=addcandidate('ordinaryReciprocal299_'+str(n),U+'ordinary-reciprocal299/'+str(n),'candidate-ir.json','reciprocal299r2',ordinaryreview,poly='polynomial.json',report=U+'ordinary-reciprocal299/REPORT.md',author='10',reviewer='03')
    v['decimalPolynomial']=ref(U+'ordinary-reciprocal299/'+str(n)+'/polynomial.txt')
    v['maximumCoefficientBits']={316:1627,315:3250,314:6496}[n];v['monomials']={316:6678,315:6675,314:6672}[n]
    v['maximumCoefficientExpression']={316:'3^1026+K',315:'3^2050+K',314:'3^4098+K'}[n]
cat['selectedOrdinaryCompanion']='ordinaryReciprocal299_314';cat['selectedOrdinaryCanonicalId']=cat['components'][cat['selectedOrdinaryCompanion']]['canonicalCandidateId']
cat['selectedOrdinaryStrictCoefficientBound']='2^6496'

bad=E+'reciprocal299/';good=E+'reciprocal299-r2/'
repair={'id':'S299-1','status':'rejected_attempt_repaired_before_acceptance','failedIR':ref(bad+'candidate299-ir.json'),'failedPolynomial':ref(bad+'polynomial299.json'),'authorRejection':ref(bad+'REJECTED.md'),'independentFinding':ref(O+'resume-depth-20261107/review-s299/FINDING-S299-1.md'),'correctionNote':ref(good+'PRE-FREEZE-CORRECTION.md'),'correctedIR':x['candidate'],'correctedPolynomial':x['polynomial'],'finalReviews':[finalreview,sreview],'failure':'First299 referenced undeclared202/203 instead of the actual S cache196/197. It had299 declared but301 active coordinates. Declaring the extra coordinates would not repair the disconnected old cache.','repair':'Use physical B=v196+2*rho*v197; regenerate tables; enforce full active-ID equality and a negative fixture that reinserts202/203.','acceptanceBoundary':'No review accepted the ab42 bytes. Final verdicts bind only corrected8ea42607 bytes.','provenance':'The author states original rejected bytes were restored deterministically; their exact hash is independently checked here.'}
assert repair['failedIR']['sha256']=='ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd'
write('REPAIR-HISTORY.json',repair)
alt=load(OLD/'PRESERVED-ALTERNATIVES.json');alt.append({'source':repair['failedIR'],'disposition':repair['failure']+' Never accepted; see REPAIR-HISTORY.json for exact evidence and corrected binding.'})

oldmap={e['entryId']:e for e in mapping['entries']};tex=(OLD/'PROOF-INTEGRATION-OUTLINE.tex').read_text(encoding='utf-8')
tex=tex.replace('\\begin{document}','\\begin{document}\n\\paragraph{Revision 6 scope.} Historical cutoffs remain below. The final appended section covers accepted301 and corrected299-r2. The rejected first299 is not a source theorem.\n',1)
def esc(s):
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#'),('^',r'\textasciicircum{}')]:s=s.replace(a,b)
    return s
extra=['\\section{Revision 6: eliminated ordinates and the oriented scalar-root interface}']
for d in NEW:extra+=['\\subsection{'+esc(d['id'])+'}','\\label{outline:r6-'+d['id'].lower()+'}',esc(d['lemma']),'\\par '+esc(d['inputs']),'\\par Consumers: '+esc(d['consumers'])]
extra.append((H/'NEW-PROOF-TEXT.tex').read_text(encoding='utf-8'))
tex=tex.replace('\\end{document}','\n'.join(extra)+'\n\\end{document}');(H/'PROOF-INTEGRATION-OUTLINE.tex').write_text(tex,encoding='utf-8')
ls=tex.splitlines();out=[]
for e in entries.values():
    label=oldmap[e['id']]['outlineLabel'] if e['id'] in oldmap else 'outline:r6-'+e['id'].lower();loc=[i+1 for i,l in enumerate(ls) if '\\label{'+label+'}' in l];assert len(loc)==1
    out.append({'entryId':e['id'],'outlineLabel':label,'outlineLabelLine':loc[0],'authorProof':e['authorProof'],'recordedNonAuthorReview':e['recordedReview'],'inventoryConsumers':[{'applicationId':a['id'],'baselineConsumerSpans':a['baselineConsumers']} for a in apps['applications'] if a['id'] in e['baselineApplications']],'actualConsumer':e.get('actualConsumer','Inherited consumer binding; unchanged.')})
mapping.update(entries=out,outline=ref((H/'PROOF-INTEGRATION-OUTLINE.tex').relative_to(ROOT).as_posix()),status='Preparatory R6 outline and draft proof text; no final exposition acceptance.')
ret=load(OLD/'RETAINED-SOURCES.json');ret['revision6ArithmeticInputs']=[{'entryId':e['id'],'classification':e['arithmeticInputClassification'],'proof':e['authorProof']} for e in apps['newInternalEntries'] if e['id'] not in oldmap]
inputs=load(OLD/'NEW-INPUT-CLASSIFICATION.json');inputs['revision6Applications']=[{'entryId':d['id'],'classification':d['inputs'],'actualConsumer':d['consumers']} for d in NEW]
inputs['revision6Boundary']='No new external theorem. N44 is a new global redundancy application, not unrestricted polynomial cancellation. N46 applies the all-four domain statement to S with an explicitly preserved scalar ordinate.'
for p in [E+'reciprocal301/MANIFEST.json',good+'MANIFEST.json',good+'CHECKS.json',good+'verify.py',O+'root-ordinate299/PROOF.md',U+'ordinary-reciprocal299/MANIFEST.json',U+'ordinary-reciprocal299/INHERITED-CONSTANT.json',O+'resume-depth-20261107/review-ordinary299/CHECKS.json']:ref(p)
for n,v in [('APPLICATION-DELTA.json',apps),('CANDIDATES.json',cat),('CANONICAL-RELATION.json',rel),('INTEGRATION-MAP.json',mapping),('RETAINED-SOURCES.json',ret),('NEW-INPUT-CLASSIFICATION.json',inputs),('PRESERVED-ALTERNATIVES.json',alt),('PREVIOUS-REVISION.json',{'files':prior,'independentReview':oldreview}),('SOURCE-PINS.json',pins)]:write(n,v)
idx=['# Canonical identities, revision6','','Counts do not identify artifacts. Rejected299 is indexed only in REPAIR-HISTORY.json.','', '| ID | Variables | Parent | IR or polynomial identity |','|---|---:|---|---|']
for cid,v in cat['components'].items():idx.append(f"| {cid} | {v['variables']} | {v.get('comparedWith')} | {v['canonicalCandidateId']} |")
for cid,v in cat['polynomialVariants'].items():idx.append(f"| {cid} | {v['variables']} | {v['residualSource']} | {v['canonicalPolynomialId']} |")
(H/'CANONICAL-INDEX.md').write_text('\n'.join(idx)+'\n',encoding='utf-8')
print(json.dumps({'applications':len(apps['applications']),'entries':len(entries),'edges':len(edges),'IRs':len(cat['components']),'variants':len(cat['polynomialVariants'])}))
