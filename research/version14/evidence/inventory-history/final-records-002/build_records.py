"""Author final V14 records from exact frozen text; create no approval files."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import inventory_core as core
import install_inventory as installer
from application_specs import S

H=Path(__file__).resolve().parent; PREP=H.parent; ROOT=PREP.parents[2]
REPO=ROOT/'work/quartic-v14-release/preview-repository'
R6=ROOT/'work/quartic-optimization-20261107/resume-release-inventory-20261107-r6'
P=core.PREFIX
def load(p):return core.parse(p.read_bytes())
def pin(path,data):return {'path':path,'sha256':core.digest(data)}
def out(name,obj):
    data=installer.encoded(obj);(H/name).write_bytes(data);return data
schema=load(PREP/'validation-schema.json')
core.require(core.digest((PREP/'FROZEN-MANIFEST.json').read_bytes())=='ac776d87f5ea3ebc03ddd6d33112fdcba54ed5bf4b17bd025931cde0f9d7b53a','preparation changed')
mp=pin('manuscripts/quartic_v14.tex',(REPO/'manuscripts/quartic_v14.tex').read_bytes())
ap=pin(P+'addition.tex',(REPO/(P+'addition.tex')).read_bytes())
core.require(mp['sha256']=='b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d','wrong final text')
core.require(ap['sha256']=='b5840b3598c655fc7f3db3475b089b65800b98f136a601c4360c72d22d6f95a0','wrong addition')
manuscript=(REPO/mp['path']).read_bytes();addition=(REPO/ap['path']).read_bytes()
old_addition=(ROOT/'work/quartic-v14-release/preview-manuscript-001/docs/manuscript-revisions/version14/addition.tex').read_bytes()
layout_bytes=(ROOT/'work/quartic-v14-prep/LAYOUT-V2.json').read_bytes()
layout=core.parse(layout_bytes)
core.require(core.digest(old_addition)==layout['original_sha256'],'old addition changed')
transformed=old_addition
for change in layout['changes']:
    before=change['old'].encode();after=change['new'].encode()
    core.require(transformed.count(before)==1,'ambiguous layout replacement')
    transformed=transformed.replace(before,after)
core.require(transformed==addition,'unrecorded text change')
core.require(manuscript.count(addition)==1,'addition embedding')
offset=manuscript[:manuscript.index(addition)].count(b'\n')
core.require(offset==21632,'unexpected addition offset')
files=core.Files(REPO)
base=load(REPO/schema['baselineInventory']['path'])
route=load(PREP/'ROUTE-SELECTION.json')
relation=load(R6/'CANONICAL-RELATION.json')
entries=load(R6/'APPLICATION-DELTA.json')['newInternalEntries']
adapt={a['applicationId']:a for a in load(PREP/'BASELINE-ADAPTATION.json')['applications']}
span_transport={}
def move_range(r):
    key=tuple(r)
    if key in span_transport:return tuple(span_transport[key]['newLines'])
    oldlines=old_addition.splitlines(keepends=True)
    raw=b''.join(oldlines[r[0]-1:r[1]])
    newraw=raw
    for change in layout['changes']:
        newraw=newraw.replace(change['old'].encode(),change['new'].encode())
    core.require(addition.count(newraw)==1,'passage content anchor not unique or crossed layout edit')
    startbyte=addition.index(newraw)
    core.require(startbyte==0 or addition[startbyte-1:startbyte]==b'\n','anchor not line-aligned')
    start=addition[:startbyte].count(b'\n')+1
    end=start+len(newraw.splitlines())-1
    span_transport[key]={'oldLines':list(r),'newLines':[start,end],
                         'oldSpanSha256':core.digest(raw),'newSpanSha256':core.digest(newraw)}
    return start,end
def a_span(r):return core.bind_span(files,ap,*move_range(r))
def m_span(r):
    start,end=move_range(r)
    return core.bind_span(files,mp,start+offset,end+offset)
def relocate(ref):
    name=ref['path']; expected=ref['sha256']
    candidates=[name]
    old='work/quartic-version6-release/repository/'
    if name.startswith(old):candidates.append(name.removeprefix(old))
    candidates.append('quartics/quartic-299-314/sources/'+name)
    for target in candidates:
        path=REPO/target
        if path.is_file() and core.digest(path.read_bytes())==expected:
            return {'path':target,'sha256':expected}
    raise core.Invalid('missing historical source '+name)
def old_span(ref):
    p=relocate(ref)
    return core.bind_span(files,p,ref.get('startLine',ref.get('start_line')),
                          ref.get('endLine',ref.get('end_line')))
def unique(items):
    result=[];seen=set()
    for item in items:
        key=core.canonical(item)
        if key not in seen:seen.add(key);result.append(item)
    return result
def all_pins(obj):
    if isinstance(obj,dict):
        if 'path' in obj and 'sha256' in obj:yield obj
        else:
            for value in obj.values():yield from all_pins(value)
    elif isinstance(obj,list):
        for value in obj:yield from all_pins(value)

# Current derivations are deliberately finer than whole-section citations.
entry_ranges={
 1:[(75,101)],2:[(103,115)],3:[(117,131),(374,394)],
 4:[(249,281),(341,355)],5:[(275,281),(628,685)],6:[(257,281),(341,355)],
 7:[(149,204)],8:[(205,226)],9:[(320,338),(528,538)],
 13:[(320,373)],14:[(619,639),(641,685)],15:[(159,183)],
 16:[(184,204)],17:[(205,226)],18:[(229,247)],
 21:[(900,933)],22:[(854,864)],24:[(283,373)],25:[(540,586)],
 26:[(619,685)],27:[(294,300),(854,864)],29:[(687,705)],
 30:[(706,741)],31:[(743,753)],32:[(755,790)],33:[(674,685),(706,721),(777,790)],
 36:[(528,538)],37:[(492,515)],38:[(540,586)],39:[(588,606)],
 40:[(396,458)],41:[(459,490),(802,826)],43:[(411,426),(828,835)],
 44:[(492,524)],45:[(479,490),(802,835)],46:[(517,586),(608,615)],
 48:[(900,954)]}
roles={e['entryId']:e for e in route['entryDispositions']}
by_app={a['id']:[] for a in base['applications']}
bound_edges=[]
for edge in relation['edges']:
    number=int(edge['entryId'][1:3]); r=roles[edge['entryId']]
    role={'current_application':'current_consumer','supporting_source':'supporting_derivation'}.get(r['role'],'archived')
    selected=role!='archived'
    source=unique([old_span(ref) for ref in edge['sourceProof']]) if selected else []
    consumed=unique([m_span(x) for x in entry_ranges[number]]+[m_span(x) for x in S[edge['applicationId']]['consumers']]) if selected else []
    reason=(r['justification']+' ' if not selected else '')+edge['reason']
    if selected:
        reason+=' The exact current derivation is bound here; the application consumer is bound separately. '+S[edge['applicationId']]['downstream']
    bound={'applicationId':edge['applicationId'],'entryId':edge['entryId'],'role':role,
           'justification':reason,'sourceSpans':source,'consumerSpans':consumed,
           'sourceRelationship':'historical proof evidence, not a new external theorem' if selected else 'preserved historical branch only'}
    bound_edges.append(bound)
    if selected:by_app[edge['applicationId']]+=source

applications=[]
for old in base['applications']:
    aid=old['id'];s=S[aid];old_ob=old['obligations']
    statements={
     'required_inputs':s['required'] if s['required'] is not None else old_ob['required_inputs'],
     'constructed_inputs':s['constructed'],
     'domain_and_index_coverage':s['domain'],
     'transition_maps_and_scalars':s['transition'],
     'identity_of_consumed_object':s['constructed']+' The bound downstream argument consumes these same objects and the normalization specified in the transition statement.',
     'exceptional_cases':s['exceptions'],
     'affected_downstream_claims':s['downstream'],
     'source_version_and_conventions':old_ob['source_version_and_conventions'],
     'validation_and_acceptance_scope':'Author record for the exact Version14 manuscript and selected corrected299/ordinary314 artifacts. Historical component reviews retain their original scope. Structural checking is not mathematical proof; no final contract approval or renewed audit of the entire inherited argument is asserted here.'}
    historical=old_span(old['source']['newDerivation'])
    current=[a_span(r) for r in s['ranges']]
    consumers=[m_span(r) for r in s['consumers']]
    source=unique([historical]+current+by_app[aid])
    dispositions={}
    for key in core.OBLIGATIONS:
        preserved=statements[key]==old_ob[key]
        why=adapt[aid]['retainedDependencyJustification']+' '+adapt[aid]['currentConstructionAndConsumerChanges']
        why+=(' This source obligation is retained verbatim; its applicability is checked using the current construction, domain and exception statements in this record.' if preserved else ' The current statement replaces the old obligation where its object, use or scope changed; it does not carry forward the old construction by textual identity.')
        dispositions[key]={'mode':'preserved' if preserved else 'replaced','justification':why,
                            'sourceSpans':source,'consumerSpans':consumers}
    applications.append({'id':aid,'priorRecordSha256':core.digest(core.canonical(old)),
                         'sourceVersionAndConventions':old['source'],
                         'obligations':statements,'dependencyDisposition':dispositions})

new_entries=[]
for e in entries:
    eid=e['id']; n=int(eid[1:3]);r=roles[eid];active=n in entry_ranges
    proofs=[old_span(ref) for ref in e['authorProof']] if active else []
    reviews=unique([relocate(ref) for ref in all_pins(e['recordedReview'])])
    new_entries.append({'entryId':eid,'disposition':r['role'],'justification':r['justification'],
       'internalOrExternal':'internally proved transformation or application; no new external theorem',
       'historicalAuthorProof':e['authorProof'],'portableProofSpans':proofs,
       'historicalRecordedReview':e['recordedReview'],'portableReviewPins':reviews,
       'currentDerivationSpans':[m_span(x) for x in entry_ranges[n]] if active else [],
       'historicalComponents':r['recordedComponents'],'selectedComponents':r['selectedComponents'],
       'newAcceptanceCreated':False})

mapping={'schema':'v14-selected-application-map-v1','manuscript':mp,'addition':ap,
 'selected':schema['selected'],'assemblyOrder':route['assemblyTopologicalOrder'],
 'edges':bound_edges,'scope':'All263 research edges are classified; current consumption is distinct from assembly ancestry and archived evidence.'}
new={'schema':'v14-selected-internal-entries-v1','manuscript':mp,'entries':new_entries,
     'repairHistory':schema['repairHistory'],'scope':'Current use of internal lemmas and exact substitutions. Historical reviews do not self-approve the current exposition.'}
mapbytes=out('selected-application-map.json',mapping);newbytes=out('selected-entries.json',new)
extra={P+'evidence/route-selection.json':(PREP/'ROUTE-SELECTION.json').read_bytes(),
       P+'evidence/selected-application-map.json':mapbytes,
       P+'evidence/selected-entries.json':newbytes,
       P+'evidence/pre-layout-addition.tex':old_addition,
       P+'evidence/layout-v2.json':layout_bytes}
inv={k:schema[k] for k in ('selected','baselineInventory','baselineManuscript','routeSelection','r6Relation','r6Manifest','repairHistory','finalArtifacts')}
inv.update(schema='portable-application-inventory-v3',status='author_records_pending_independent_review',
           manuscript=mp,addition=ap,edits=pin(P+'new-edits.json',(REPO/(P+'new-edits.json')).read_bytes()),
           externalSources=base['externalSources'],existingSourceCatalog=base['existingSourceCatalog'],
           assemblyOrder=route['assemblyTopologicalOrder'],applications=applications,
           edgeBindings=bound_edges,mathematicalAcceptanceClaim=False,
           selectedApplicationMap=pin(P+'evidence/selected-application-map.json',mapbytes),
           newInternalEntries=pin(P+'evidence/selected-entries.json',newbytes),
           historicalSourceScope='Version13 source/convention records are retained exactly as historical records; their old constructed objects are not adopted where this record replaces them.')
invbytes=out('APPLICATIONS.json',inv)

oldcontract=load(REPO/'docs/manuscript-revisions/version13/quartic-application.json')
edits=load(REPO/(P+'new-edits.json'))
evidence={'application-inventory':pin(P+'APPLICATIONS.json',invbytes),
          'selected-map':inv['selectedApplicationMap'],'internal-entries':inv['newInternalEntries'],
          'addition':ap,'baseline-inventory':schema['baselineInventory'],
          'baseline-manuscript':schema['baselineManuscript'],'route':schema['routeSelection'],
          'repair-history':schema['repairHistory'],
          'symbolic299':schema['finalArtifacts']['299']['files'][0],
          'ordinary314':schema['finalArtifacts']['314']['files'][0]}
evidence['pre-layout-addition']=pin(P+'evidence/pre-layout-addition.tex',old_addition)
evidence['layout-v2']=pin(P+'evidence/layout-v2.json',layout_bytes)
for name in ['mathematical-review','ordinary-review','artifact-review','inventory-review']:
    path='quartics/quartic-299-314/reviews/'+name+'.md'
    evidence[name]=pin(path,(REPO/path).read_bytes())
summary={
 'source_hypotheses':('Retained model, quaternion, formal-log, height, scalar-depth24, contact-prime and real-progression inputs with their exact source qualifications.',
   'The same field, roots and integer input construction; new all-E auxiliary comparisons and common anchor/gamma certificate.',
   'All39 application records explicitly compare the source hypotheses with current objects. New local lemmas are proved in the addition and bound to historical proof evidence; inherited source-first coverage is a separate review, not asserted by these records.'),
 'constructed_objects':('The objects submitted to each source result must satisfy its actual domain and construction conditions.',
   'The shifted/unscaled anchor, Kummer/squared-H recovery, reciprocal cubics and oriented differences, common-scale groups, scalar interface and exact ordinary lift.',
   'Root reconstruction and parity precede height. H recovery and low tests precede raw ratio cancellation. Completeness uses the same fixed roots and scalar point, then one anchor and final H.'),
 'index_domain_coverage':('Root labels remain nonzero odd integers; formal-log identities must cover all represented auxiliary points, including zero and torsion exceptions.',
   'U_i=k_iR0+T_i and H=mR0+T_H, with half-integral free labels and doubled identities for all four pairs.',
   'The two extra factors2 kill both torsion terms. The one-place arguments cover arbitrary gamma valuations, all zero-leaf patterns and both split/inert cases; auxiliary labels need not be globally integral.'),
 'transition_maps':('Every exact substitution must recover the same downstream values; domain extensions require soundness and completeness separately.',
   'The displayed Kummer, anchor unscaling, oriented slope, alternate-ordinate, sparse-Lucas and unique ordinary-chain maps.',
   'The exact scalar S orientation is retained. The all-E reciprocal extension claims equality of input projections, not a bijection of old square-root fibers. Later ordinate deletion is an exact map only on the globally justified full zero set.'),
 'limiting_object_identity':('The approximate ratios, scalar point, root abscissa product and coefficient polynomial consumed downstream must be the originally intended objects.',
   'Unchanged external L/LP and scalar values, original three scales, exact2g0g1 scalar coefficient and selected corrected299/ordinary314 tables.',
   'Physical source consumers and current spans are bound in the263-edge map. S uses cache196/197 and the fixed root ordinate; rejected202/203 and alternative g1²/ordinary branches are preserved only as history.'),
 'coefficient_conventions':('Keep K=Q(rho),rho²=2,D=(3-rho)²,negative reciprocal ordinates, conjugations and primitive integer row normalization.',
   'f=1/x,h=-y/x²; selected compact maps preserve input and all coefficients. The ordinary maximum is3^4098+K0 with6496bits.',
   'The source and current convention records are explicit. The original source-ID ordinary text has222890bytes, distinct from compact264430bytes. The old2^3247 bound is not copied.'),
 'local_conditions':('All consumed local hypotheses and real/finite completeness conditions must hold simultaneously for one witness choice.',
   'One successful place supplies all group bounds. The fixed anchor quadric is approximated at2,3,17,contacts and the real place; final H comes afterwards.',
   'The explicit local targets, dense rational parametrization and rational CRT/real approximation justify common gamma. The originalPi19 construction suffices; extra denominator primes alter only square factors in pole values.'),
 'exceptional_cases':('Prove all nonzero divisions and include zero/identity/tangent/empty-support branches without circular use.',
   'Squared-H U=0/Q=0 leaves, finite torsion, either auxiliary identity, equal-abscissa tangent, nonzero root product, and global A=1-DB cancellation.',
   'The pre-H root/anchor contradiction supplies nonempty contact support; low tests and regular ratio equations then establish required denominators. Analytic units take value1 atO, and the quadric has nonzero constant.'),
 'downstream_consumption':('Changed hypotheses and constructions must be connected to every affected proof consumer and final coefficient assertion.',
   'The39 current applications,351 obligations,48 historical/current internal entries,263 dispositions and selected24-IR assembly history.',
   'Exact raw spans distinguish new derivations, inherited supporting arguments and unused alternatives. Historical component reviews retain their scope. The current contract awaits an actual non-author decision and does not certify the full inherited proof by itself.')}
contract={'id':'QUARTIC-299-COMPOSITION','manuscript':mp,
 'authors':['/root','/root/astra_bl_horizontal_repair','/root/astra_quartic_opt01_elimination',
            '/root/astra_quartic_opt03_depth','/root/astra_quartic_opt05_anchor','/root/astra_quartic_opt10_combination'],
 'sources':oldcontract['sources'],'evidence':evidence,
 'reviewed_edits':{e['id']:core.digest(core.canonical(e)) for e in edits if e.get('contract_id')=='QUARTIC-299-COMPOSITION'},
 'manuscript_spans':[], 'obligations':{},
 'dependency_impact':'This author contract binds the new Version14 abstract/introduction/addition, the current39 applications and selected corrected299/ordinary314 artifacts. It preserves the prior source conventions and separately marks replaced constructions, all-E domain uses, local conditions and downstream consumers. Historical accepted components are evidence, not acceptance of this contract. Full inherited source-first coverage, actual final mathematical/structural review and audit-registry incorporation remain separate decisions; no approval is generated here.'}
for role,ranges in [('construction',[(75,247),(283,338),(396,524),(687,705),(900,933)]),
                    ('application',[(339,394),(540,685),(706,790)]),
                    ('consumer',[(608,615),(802,835),(886,954)])]:
    for r in ranges:
        s=m_span(r);contract['manuscript_spans'].append({'role':role,'start_line':s['start_line'],'end_line':s['end_line'],'sha256':s['sha256_raw_utf8_span']})
for key,(required,constructed,why) in summary.items():
    contract['obligations'][key]={'status':'checked','required':required,'constructed':constructed,
     'justification':why,'sources':['silverman','voight','internal-v12'],
     'evidence':['application-inventory','selected-map','internal-entries','addition','mathematical-review','ordinary-review','artifact-review']}
out('quartic-application.json',contract)
out('SPAN-TRANSPORT.json',{'originalAddition':evidence['pre-layout-addition'],'newAddition':ap,
                         'layoutChanges':evidence['layout-v2'],'method':'Exact unique passage content after only the three pinned formatting replacements',
                         'passages':[span_transport[k] for k in sorted(span_transport)]})
result=installer.prepare(REPO,inv,contract,schema,extra)
dest=H/'install-root'
core.require(not dest.exists(),'output frozen or already exists')
installer.write_new(dest,result)
print(json.dumps({'applications':len(applications),'obligations':9*len(applications),
 'edges':len(bound_edges),'entries':len(new_entries),'files':len(result),
 'contractSha256':core.digest(installer.encoded(contract)),
 'inventorySha256':core.digest(invbytes),'manuscript':mp,'output':str(dest)}))
