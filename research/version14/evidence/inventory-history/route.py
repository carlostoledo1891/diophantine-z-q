"""Select literal assembly ancestors separately from current proof uses."""
from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent; ROOT=H.parents[2]
R6=ROOT/'work/quartic-optimization-20261107/resume-release-inventory-20261107-r6'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(R6/'FROZEN-MANIFEST.json')=='207e7ca6cca93a79fabc19db02ee5c8d2a3d9370d0ec7f19d2847d3bb6e02ae7'
for n,v in json.loads((R6/'FROZEN-MANIFEST.json').read_bytes()).items():assert sha(R6/n)==v['sha256']
c=json.loads((R6/'CANDIDATES.json').read_bytes());a=json.loads((R6/'APPLICATION-DELTA.json').read_bytes());r=json.loads((R6/'CANONICAL-RELATION.json').read_bytes())
targets=['reciprocal299r2','ordinaryReciprocal299_314']
parents={k:set() for k in c['components']}
for e in c['dependencyEdges']:parents[e['candidate']].add(e['dependsOn'])
closure=set();visiting=set();ordered=[]
def visit(k):
    assert k not in visiting,'Cyclic source graph'
    if k in closure:return
    visiting.add(k)
    for p in sorted(parents[k]):visit(p)
    visiting.remove(k);closure.add(k);ordered.append(k)
for k in targets:visit(k)

# Explicit dispositions are not inferred from the earlier selectedDependency
# flags: intermediate formulas can be superseded while their IRs remain in the
# actual assembly history. The final manuscript mapping is a separate step.
special={
9:('supporting_source','The pre-H curve/valuation analysis is reused through current H reconstruction and all-E period arguments; the old four-group cache layout is not the displayed final detector.'),
10:('superseded_intermediate_circuit','Four332 belongs to literal assembly history, but its four-group formula is replaced by the common three-group detector.'),
11:('superseded_intermediate_circuit','The strong330 H circuit is an intermediate ancestor; current H depth comes from the unit-L bootstrap, not a retained direct stronger-H test.'),
12:('superseded_intermediate_circuit','The chain327 finite transport is historical; the final local/shared powers are explicitly defined by shared314 and anchor-gamma313.'),
13:('supporting_source','Three326 supplies pre-H/same-place reasoning in the accepted derivation, but its former weights are not the final displayed common-scale groups.'),
14:('supporting_source','The original Pi19 completeness depths and real/finite choices support shared314; the final common coefficients require the separate N26 estimates.'),
19:('unused_alternative','Alternative358 uses a different squared scalar numerator and is not the selected exact2*g0*g1 route.'),
20:('superseded_intermediate_circuit','The chain323 transport is a literal ancestor of combined315, but the final common-scale chain is supplied later. Do not state its old local chain as the final circuit.'),
21:('supporting_source','Earlier reviewed weighted-chain construction supplies the same exact exponent identity; the current ordinary314 transport and bound are separately established by N48.'),
22:('supporting_source','The sparse-Lucas identity has an earlier source-specific320 application. The actual selected shared314 application is N27, not an automatic reuse of the320 artifact.'),
23:('unused_alternative','Restricted lower-bound claims for earlier constant chains are not needed for the existence theorem or selected314 artifact.'),
28:('unused_alternative','Ordinary sparse314 lifts331/330/329 are archived alternatives on a different symbolic source.'),
34:('unused_alternative','Ordinary anchor313 lifts are archived alternatives, not the selected corrected299 lift.'),
35:('unused_alternative','Positive weighted313/328 polynomials are not applied to selected299/314.'),
42:('unused_alternative','Ordinary reciprocal307 lifts are archived alternatives on a different source.'),
47:('artifact_repair_history','The rejected-cache incident is required provenance and a finite negative control; it is not a new arithmetic theorem or a claimed main-text proof step.')}
uses=[]
for e in a['newInternalEntries']:
    n=int(e['id'][1:3]);role,reason=special.get(n,('current_application','Retained final argument or exact source-specific transformation; bind its actual final text and consumers before acceptance.'))
    components=e.get('coveredComponentIds',[e['component']])
    if n==48:selected=['ordinaryReciprocal299_314']
    else:selected=[x for x in components if x in closure]
    uses.append({'entryId':e['id'],'role':role,'justification':reason,'recordedComponents':components,'selectedComponents':selected,'recordedProof':e['authorProof'],'recordedReview':e['recordedReview'],'manuscriptBinding':'pending_final_author_text' if role in ('current_application','supporting_source') else 'not_claimed_as_a_current_mathematical_application'})
roles={u['entryId']:u['role'] for u in uses}
current=[e for e in r['edges'] if roles[e['entryId']]=='current_application']
support=[e for e in r['edges'] if roles[e['entryId']]=='supporting_source']
out={'schema':'v14-route-selection-v1','status':'Author route selection; final text and independent review pending','r6Manifest':{'path':str((R6/'FROZEN-MANIFEST.json').relative_to(ROOT)).replace('\\','/'),'sha256':sha(R6/'FROZEN-MANIFEST.json')},'selectedSymbolic':'reciprocal299r2','selectedOrdinary':'ordinaryReciprocal299_314','assemblyTopologicalOrder':ordered,'assemblyComponents':{k:c['components'][k] for k in ordered},'assemblyEdges':[e for e in c['dependencyEdges'] if e['candidate'] in closure and e['dependsOn'] in closure],'archivedOtherIRs':sorted(set(c['components'])-closure),'archivedPolynomialVariants':c['polynomialVariants'],'entryDispositions':uses,'candidateCurrentApplicationEdges':current,'supportingSourceEdges':support,'notAllR6EdgesConsumed':True,'r6EdgeCount':len(r['edges']),'candidateCurrentEdgeCount':len(current),'supportingEdgeCount':len(support)}
(H/'ROUTE-SELECTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assemblyIRs':len(closure),'currentEntries':sum(u['role']=='current_application' for u in uses),'currentEdges':len(current),'supportingEdges':len(support),'allR6Edges':len(r['edges'])}))
