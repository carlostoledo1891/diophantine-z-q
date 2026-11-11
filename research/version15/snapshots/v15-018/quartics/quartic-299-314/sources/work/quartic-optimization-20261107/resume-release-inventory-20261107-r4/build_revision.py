"""Prepare r4 from immutable r3 and explicit new application specifications."""
from pathlib import Path
import copy,hashlib,json
from spec import NEW,O,U
H=Path(__file__).resolve().parent; ROOT=H.parents[2]
R3=H.with_name('resume-release-inventory-20261107-r3')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_bytes())
def write(name,obj):(H/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert sha(R3/'FROZEN-MANIFEST.json')=='8cb4db6dfbe323dc71dde53c46e82a73e207f11ef99fc4b2b68e59f5ea700fb1'
for name,m in load(R3/'FROZEN-MANIFEST.json').items():assert sha(R3/name)==m['sha256']
pins=load(R3/'SOURCE-PINS.json')
# Live status paths were never immutable evidence; retain their pinned snapshots in r3.
mutable={p:m for p,m in pins.items() if p.endswith('/STATUS.json')}
pins={p:m for p,m in pins.items() if p not in mutable}
def ref(path):
    p=ROOT/path; value={'path':path,'sha256':sha(p)}
    pins[path]={'sha256':value['sha256'],'bytes':p.stat().st_size}
    return value
prior={p.name:ref(p.relative_to(ROOT).as_posix()) for p in sorted(R3.iterdir()) if p.is_file()}
r3review=ref(O+'resume-review-inventory-r3-sol/REVIEW.md')
assert r3review['sha256']=='a0264397cb0dc380c03b19b1ee97aab9e464c94e984386d0a20709d80a3d17d1'
def section(path,heading):
    r=ref(path);lines=(ROOT/path).read_text(encoding='utf-8').splitlines()
    starts=[i for i,s in enumerate(lines) if s==heading];assert len(starts)==1,(path,heading)
    start=starts[0];end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('## ')),len(lines))
    return dict(r,heading=heading,startLine=start+1,endLine=end)
apps=load(R3/'APPLICATION-DELTA.json');catalog=load(R3/'CANDIDATES.json')
relation=load(R3/'CANONICAL-RELATION.json');mapping=load(R3/'INTEGRATION-MAP.json')
apps['revision']=4;apps['status']='Preparatory r4; existing acceptances recorded, independent inventory review pending.'
for e in apps['newInternalEntries']:
    e['revision3Selected315Dependency']=e.pop('selected315Dependency')
    e['selectedCandidateDependency']=e['revision3Selected315Dependency']
for d in NEW:
    proofs=[section(p,s) for p,s in d['sources']]
    item=dict(id=d['id'],component=d['component'],kind=d['kind'],selectedCandidateDependency=d['selected'],oldObject=d['old'],newObject=d['new'],requiredInternalLemmaOrMap=d['lemma'],baselineApplications=[],authorProof=proofs,recordedReview=ref(d['review']),author=d['author'],reviewer=d['reviewer'],recordedStatus='accepted_exact_component_by_recorded_non_author',newApprovalCreatedHere=False,actualConsumer=d['consumers'],arithmeticInputClassification=d['inputs'])
    if 'covered' in d:item['coveredComponentIds']=d['covered']
    if d['component']=='shared314':item['additionalConstructionReview']=ref(U+'review-shared314/REVIEW.md')
    apps['newInternalEntries'].append(item)
    for name in d['targets'].split():
        relation['edges'].append(dict(applicationId='V13-'+name,entryId=d['id'],reason=d['consumers']))
entries={e['id']:e for e in apps['newInternalEntries']}
for edge in relation['edges']:
    e=entries[edge['entryId']]
    edge['scope']={'selectedCandidateDependency':e['selectedCandidateDependency'],'componentIds':e.get('coveredComponentIds',[e['component']])}
    edge['sourceProof']=e['authorProof']
relation['schema']=2;relation['status']='author_prepared_r4_pending_independent_inventory_review'
relation['edges'].sort(key=lambda e:(e['applicationId'],e['entryId']))
edgekeys={(e['applicationId'],e['entryId']) for e in relation['edges']}
for a in apps['applications']:
    a['revision3NewEntryIds']=a['newEntryIds']
    a['newEntryIds']=sorted(e for x,e in edgekeys if x==a['id'])
    extra=[entries[e] for e in a['newEntryIds'] if e not in a['revision3NewEntryIds']]
    if extra:
        a['revision3DeltaClassification']=a['deltaClassification']
        a['deltaClassification']='updated_with_explicit_r4_application_entries'
        a['revision4DeltaClasses']=sorted({e['kind'] for e in extra})
for e in entries.values():e['baselineApplications']=sorted(a for a,b in edgekeys if b==e['id'])
ordinary=next(a for a in apps['applications'] if a['id']=='V13-ORDINARY-GATE')
ordinary['revision3OrdinaryArtifactScope']=ordinary['ordinaryArtifactScope']
ordinary['deltaClassification']='accepted_exact319_and_sparseShared314_lifts_no_anchorGamma313_lift_in_scope'
ordinary['ordinaryArtifactScope']={'acceptedFamilies':{'exact319':['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336'],'sparseShared314':['ordinaryShared314_331','ordinaryShared314_330','ordinaryShared314_329']},'selectedCandidateId':'anchorGamma313','selectedCandidateLiftIncluded':False,'meaning':'Source-specific exact lifts only. No approval transfers between equal counts.'}

def addcandidate(cid,folder,irname,report,review,author,reviewer,source,polyname):
    path=folder+'/'+irname;ir=load(ROOT/path);oldpath=catalog['components'][source]['candidate']['path'];old=load(ROOT/oldpath)
    delta={}
    for key in ['coordinates','residuals']:
        a={x['id']:x for x in old[key]};b={x['id']:x for x in ir[key]}
        delta[key]={'deleted':sorted(a.keys()-b.keys()),'added':sorted(b.keys()-a.keys()),'changed':sorted(k for k in a.keys()&b.keys() if a[k]!=b[k])}
    item={'id':cid,'displayId':cid,'candidate':ref(path),'report':ref(report),'review':ref(review),'componentAuthor':author,'recordedReviewer':reviewer,'recordedStatus':'accepted_component','comparedWith':source,'variables':len(ir['coordinates']),'residuals':len(ir['residuals']),'newApprovalCreatedHere':False,'countIsNotIdentity':True,'objectDelta':delta,'polynomial':ref(folder+'/'+polyname)}
    item['canonicalCandidateId']='sha256:'+item['candidate']['sha256'];catalog['components'][cid]=item
    catalog['dependencyEdges'].append({'candidate':cid,'dependsOn':source,'role':'immediate exact source; application obligations recorded separately'})
    return item
addcandidate('shared314',O+'resume-elimination-20261107/shared-scale314','candidate314-ir.json',O+'resume-elimination-20261107/shared-scale314/REPORT.md',O+'resume-review-shared314-20261107/REVIEW.md','03+01','05 arithmetic;10 construction','combined315','polynomial314.json')['additionalReview']=ref(U+'review-shared314/REVIEW.md')
addcandidate('sparseShared314',U+'sparse-shared314','candidate314-ir.json',U+'sparse-shared314/REPORT.md',O+'resume-review-transports314-20261107/REVIEW.md','10','05','shared314','polynomial314.json')
for n in (331,330,329):
    item=addcandidate('ordinaryShared314_'+str(n),U+'ordinary-sparse-shared314/'+str(n),'candidate-ir.json',U+'ordinary-sparse-shared314/REPORT.md',O+'resume-review-transports314-20261107/REVIEW.md','10','05','sparseShared314','polynomial.json')
    item['decimalPolynomial']=ref(U+'ordinary-sparse-shared314/'+str(n)+'/polynomial.txt')
    item['maximumCoefficientBits']={331:1627,330:3250,329:6496}[n]
selected=addcandidate('anchorGamma313',O+'resume-anchor-shared314-20261107/anchor-gamma313','candidate313-ir.json',O+'resume-anchor-shared314-20261107/anchor-gamma313/REPORT.md',U+'review-anchor-gamma313/REVIEW.md','05+03','10','sparseShared314','polynomial313.json')
assert selected['review']['sha256']=='981dff20bd980f2a040e8b31418cdd0c74e7bcf6e1356c6322fd01f9b42cca13'
selected['contributedProof']=ref(O+'resume-depth-20261107/anchor313/PROOF.md')
expected={'shared314':'7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5','sparseShared314':'aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382','ordinaryShared314_331':'4489f4207f1e212c5a11db0457528dc745710ee68663eb0ddafe9d60ab6a4291','ordinaryShared314_330':'eb4d673fcc6a1eee73e832977f634a346dd3bbe1ecf0104d6dab70c0cf739cf4','ordinaryShared314_329':'561f483ce198969090d83f3cb797798f5d640ae8db98a6438a177d519962e8b0','anchorGamma313':'6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a'}
for cid,pin in expected.items():assert catalog['components'][cid]['candidate']['sha256']==pin
assert selected['contributedProof']['sha256']=='ba0b08bf1d155d22d152e1dd2ec23f1b264951663cb53e90f1ed3da214b271a1'
catalog['revision3SelectedCandidate']=catalog['selectedAcceptedCandidate']
catalog['selectedAcceptedCandidate']='anchorGamma313';catalog['selectedAcceptedCanonicalId']=selected['canonicalCandidateId']
catalog['selectedAcceptedLineage']+=['shared314','sparseShared314','anchorGamma313']
for key in ['ordinaryScope','sparseScope','publication']:catalog['revision3'+key[0].upper()+key[1:]]=catalog[key]
catalog['ordinaryScope']=ordinary['ordinaryArtifactScope']
catalog['sparseScope']='sparseShared314 is separately accepted on shared314. Earlier sparse320/315 approvals alone do not authorize this source.'
catalog['publication']='313 remains above the strict below300 threshold. Preparatory inventory only.'
catalog['agentIdentityAliases']={x:'/root/astra_quartic_opt'+x+'_'+name for x,name in [('01','elimination'),('03','depth'),('05','anchor'),('10','combination')]}
catalog['soundnessOrderFor313']=['Use explicit u inverse and chain to reconstruct sparseShared314 before any arithmetic interpretation.','Invert the exact sparse-Lucas map to restore shared314 with identical F.','Use shared314 local residues and one-place bounds; obtain initial formality and integral L ratios, then unit Li and depth10 H.','Only then use full approximation precision, height and input conclusions. All inherited root/parity/anchor restorations retain their earlier order.']
catalog['completenessOrderFor313']=['Impose Fs in8Z2 during allowed scalar finite preparation; choose scalar and odd roots, then T and rational anchor basepoint.','Fix comparison neighborhoods and bounds; choose denominator depths including nu3>2^25; select contacts avoiding fixed T denominators and then lambda.','Construct one rational anchor point meeting small-prime/contact valuations and real interval using the internal reflection/CRT lemma.','Set gamma=1/u, then choose final H in unchanged Pi19 progression. Apply exact sparse map and unique eight-coordinate chain.']
apps['selectedCandidateId']=selected['canonicalCandidateId']

# Preserve the old outline as a historical section and append individually addressable r4 entries.
tex=(R3/'PROOF-INTEGRATION-OUTLINE.tex').read_text(encoding='utf-8')
tex=tex.replace('\\begin{document}','\\begin{document}\n\\paragraph{Revision 4 scope.} The inherited sections below retain the revision 3 cutoff. The appended revision 4 section supplies the selected 313-variable route; old 315-specific scope statements are historical, not current approval restrictions. This remains a preparatory outline.\n',1)
def escape(s):
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#'),('^',r'\textasciicircum{}')]:s=s.replace(a,b)
    return s
addition=['\\section{Revision 4: common scale and constrained anchor witnesses}']
for d in NEW:
    addition += ['\\subsection{'+escape(d['id'])+'}','\\label{outline:r4-'+d['id'].lower()+'}',escape(d['lemma']),'\\par '+escape(d['inputs']),'\\par Consumers: '+escape(d['consumers'])]
tex=tex.replace('\\end{document}','\n'.join(addition)+'\n\\end{document}')
(H/'PROOF-INTEGRATION-OUTLINE.tex').write_text(tex,encoding='utf-8')
lines=tex.splitlines()
oldmap={e['entryId']:e for e in mapping['entries']};newmap=[]
for e in apps['newInternalEntries']:
    label=oldmap[e['id']]['outlineLabel'] if e['id'] in oldmap else 'outline:r4-'+e['id'].lower()
    loc=[i+1 for i,s in enumerate(lines) if '\\label{'+label+'}' in s];assert len(loc)==1
    newmap.append({'entryId':e['id'],'outlineLabel':label,'outlineLabelLine':loc[0],'authorProof':e['authorProof'],'recordedNonAuthorReview':e['recordedReview'],'inventoryConsumers':[{'applicationId':a['id'],'baselineConsumerSpans':a['baselineConsumers']} for a in apps['applications'] if a['id'] in e['baselineApplications']], 'actualConsumer':e.get('actualConsumer','Inherited r3 consumer binding; no change in this revision.')})
mapping['entries']=newmap;mapping['outline']=ref((H/'PROOF-INTEGRATION-OUTLINE.tex').relative_to(ROOT).as_posix())
mapping['status']='Preparatory r4 outline; not final exposition or new proof acceptance.'
alternatives=load(R3/'PRESERVED-ALTERNATIVES.json')
alternatives.append({'source':ref(O+'resume-depth-20261107/common-scale/REPORT.md'),'disposition':'Rejected original gamma^-156 proposal: P2 residue class collides for even c. Preserved; not a source of accepted shared314 arithmetic.'})
alternatives.append({'source':ref(O+'resume-review-common-scale-20261107/REVIEW.md'),'disposition':'Source-level reciprocal variant acceptance has a narrower scope and does not approve shared314 H bootstrap. The latter has its own review.'})
alternatives.append({'source':ref(O+'resume-depth-20261107/common-scale/ERRATUM.md'),'disposition':'Author-withdrawn156 residue-class claim retained with its explicit collision and corrected variant distinction.'})
ref(O+'resume-depth-20261107/common-scale/RECIPROCAL-VARIANT.md')
alternatives.append({'source':ref(O+'resume-anchor-shared314-20261107/PROPOSAL.md'),'disposition':'Original exploratory anchor note retained. Final313 proof and10 independent acceptance supersede its open-work status without editing it.'})
retained=load(R3/'RETAINED-SOURCES.json');retained['revision4ArithmeticInputs']=[{'entryId':e['id'],'classification':e['arithmeticInputClassification'],'proof':e['authorProof']} for e in apps['newInternalEntries'] if e['id'] not in oldmap]
write('APPLICATION-DELTA.json',apps);write('CANDIDATES.json',catalog);write('CANONICAL-RELATION.json',relation);write('INTEGRATION-MAP.json',mapping)
write('PRESERVED-ALTERNATIVES.json',alternatives);write('RETAINED-SOURCES.json',retained)
write('PREVIOUS-REVISION.json',{'files':prior,'independentReview':r3review,'mutableHistoricalStatusReferencesNotRevalidated':mutable})
manuscript='work/quartic-version6-release/repository/manuscripts/quartic_v13.tex'
v13=ref(manuscript);vlines=(ROOT/manuscript).read_text(encoding='utf-8').splitlines()
def span(first,last):
    return dict(v13,startLine=first,endLine=last,sha256_normalized_LF_span=hashlib.sha256(('\n'.join(vlines[first-1:last])+'\n').encode()).hexdigest())
primeend=next(i+1 for i in range(16565,len(vlines)) if vlines[i]=='\\end{theorem}')
inputs={
 'scope':'Classifies proof ingredients; does not create an external theorem acceptance or claim elementary invoked facts were proved in the new notes.',
 'retainedArithmeticApplications':[
  {'name':'Depth-one formal logarithm unit identity','source':span(20885,20900),'newEntries':['N25-H-DEPTH-BOOTSTRAP'],'qualifications':'Same field/curve/normalization and identity extension; initial formality only. High depth is concluded later.'},
  {'name':'Scalar preparation with arbitrary further finite depths','source':span(21430,21439),'newEntries':['N30-ANCHOR-SMALL-LOCAL','N33-ANCHOR-COMPLETE-ORDER'],'qualifications':'Same H0 fixed first, N0 multiple6m0, positive dense progression; impose Fs in8Z2 before choosing s.'},
  {'name':'Three-witness quaternion criterion','source':span(20177,20197),'newEntries':['N30-ANCHOR-SMALL-LOCAL','N32-ANCHOR-RATIONAL-APPROXIMATION'],'qualifications':'Same (2,3)_Q and rational t integral at2,3; supplies a rational basepoint on Q=N. No generalized quadric theorem is assumed.'},
  {'name':'Real-progression lemma','source':span(10638,10660),'newEntries':['N26-COMMON-SCALE-COMPLETE','N30-ANCHOR-SMALL-LOCAL','N33-ANCHOR-COMPLETE-ORDER'],'qualifications':'Same finite pole sets/nonzero maps; modulus and residue multiples of component index for density; bounds fixed before contact primes.'},
  {'name':'Simultaneous-prime theorem','source':span(16566,primeend),'newEntries':['N26-COMMON-SCALE-COMPLETE','N31-ANCHOR-CONTACT-LOCAL','N33-ANCHOR-COMPLETE-ORDER'],'qualifications':'All original coefficient/odd-squarefree/coprimality/separation assumptions retained through baseline contracts; enlarge only fixed denominator divisibility and finite lower prime cutoff.'}],
 'internallyProvedNewLemmas':['Shared314 residue separation and quantitative bounds','H depth bootstrap from unit Li and exact primary coordinate identity','Uniform common-coefficient finite and real estimates','Explicit anchor local-point formulas','Reflection rational-map identity and density of its domain in local targets','Coordinatewise rational approximation construction and final ordering'],
 'standardExternalFactsInvokedNotReproved':[
  {'fact':'Unit square criteria in Q2 and odd Qp, equivalently local square roots near1','entries':['N30-ANCHOR-SMALL-LOCAL','N32-ANCHOR-RATIONAL-APPROXIMATION']},
  {'fact':'Cyclicity of a finite-field multiplicative group','entries':['N31-ANCHOR-CONTACT-LOCAL'],'use':'Norm surjectivity is deduced in the note using this standard fact.'},
  {'fact':'One-variable Hensel lemma at a nonzero derivative','entries':['N31-ANCHOR-CONTACT-LOCAL']},
  {'fact':'Integer Chinese remainder theorem and elementary real mesh approximation','entries':['N26-COMMON-SCALE-COMPLETE','N32-ANCHOR-RATIONAL-APPROXIMATION']}],
 'notInvoked':['General weak approximation theorem for quadrics','New prime-pattern theorem','Stronger Pi progression','Unrestricted extra prime-support condition on gamma or anchor witnesses']}
write('NEW-INPUT-CLASSIFICATION.json',inputs)
write('SOURCE-PINS.json',pins)
index=['# Canonical candidate index, r4','','The exact IR hash is the identity. Counts are labels.','', '| ID | Variables | Source | IR SHA-256 |','| --- | ---: | --- | --- |']
for k,c in catalog['components'].items():index.append(f"| {k} | {c['variables']} | {c.get('comparedWith')} | {c['candidate']['sha256']} |")
(H/'CANONICAL-INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
print(json.dumps({'entries':len(entries),'applications':len(apps['applications']),'edges':len(edgekeys),'candidates':len(catalog['components'])}))
