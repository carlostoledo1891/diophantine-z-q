"""Build inventory notes from immutable source records; execute no candidate code."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = HERE.with_name('resume-release-inventory-20261107')
O = 'work/quartic-optimization-20261107/'
U = 'work/quartic-under300-20261107/'
pins = {}

def pin(path, expected=None):
    p = ROOT / path
    raw = p.read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    if expected:
        assert h == expected, (path, h, expected)
    pins[path] = {'sha256': h, 'bytes': len(raw)}
    return {'path': path, 'sha256': h}

def read(path):
    pin(path)
    return json.loads((ROOT / path).read_bytes())

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def section(path, heading):
    p = pin(path)
    lines = (ROOT / path).read_text(encoding='utf-8-sig').splitlines()
    found = [i for i,s in enumerate(lines) if s == heading]
    assert len(found) == 1, (path, heading)
    start = found[0]
    end = next((i for i in range(start+1,len(lines)) if lines[i].startswith('## ')),len(lines))
    return dict(p, heading=heading, startLine=start+1, endLine=end)

# Preserve the whole preceding packet, including its historical pending status.
prior = {}
for p in sorted(OLD.iterdir()):
    if p.is_file():
        prior[p.name] = pin(p.relative_to(ROOT).as_posix())
old_prefix = OLD.relative_to(ROOT).as_posix()+'/'
old_pins = read(old_prefix+'SOURCE-PINS.json')
for path, meta in old_pins.items():
    if path.endswith('/STATUS.json'):
        continue  # The immutable preceding snapshot preserves its original bytes.
    pin(path, meta['sha256'])
apps = read(old_prefix+'APPLICATION-DELTA.json')
catalog = read(old_prefix+'CANDIDATES.json')
retained = read(old_prefix+'RETAINED-SOURCES.json')
alternatives = read(old_prefix+'PRESERVED-ALTERNATIVES.json')
components = catalog['components']

review318 = pin(O+'resume-sol-review318-20261107/REVIEW.md', 'b1282b2283b940df8b61c04d67eaf3b2e89906fa0ec41c07af006e073003ceaf')
components['combined318'].update(recordedStatus='accepted_composition', recordedReviewer='/root/sol_protocol_final_review', review=review318)

def add(key, directory, irname, polyname, reviewpath, reviewhash, source, author, reviewer, status):
    irpath = directory+'/'+irname
    data = read(irpath)
    src = read(components[source]['candidate']['path'])
    delta = {}
    for field in ('coordinates','residuals'):
        a = {x['id']:x for x in src[field]}
        b = {x['id']:x for x in data[field]}
        assert len(b) == len(data[field])
        delta[field] = {'deleted':sorted(a.keys()-b.keys()), 'added':sorted(b.keys()-a.keys()), 'changed':sorted(i for i in a.keys()&b.keys() if a[i]!=b[i])}
    components[key] = {'id':key, 'candidate':pin(irpath), 'polynomial':pin(directory+'/'+polyname),
        'report':pin(directory+'/REPORT.md'), 'review':pin(reviewpath,reviewhash),
        'recordedStatus':status, 'componentAuthor':author, 'recordedReviewer':reviewer,
        'comparedWith':source, 'variables':len(data['coordinates']), 'residuals':len(data['residuals']),
        'objectDelta':delta, 'newApprovalCreatedHere':False}
    return data

add('chain323', O+'resume-depth-20261107/chain323', 'candidate323-ir.json','polynomial323.json',
    O+'resume-sol-review323-20261107/REVIEW.md','ab7a9e1c126823950c76e6fa9ae8523fb166c89e46f0ac3202d6b06752c2ece4',
    'three326','/root/astra_quartic_opt03_depth','/root/sol_protocol_policy_review','accepted_exact_component')
add('combined315', U+'10-combination/combined315', 'candidate315-ir.json','polynomial315.json',
    O+'resume-sol-review315-20261107/REVIEW.md','4585097b153c7bcb534eb209bd1bcea504a4f894d48fbdfa41dea5522007ca5c',
    'combined318','/root/astra_quartic_opt10_combination','/root/sol_protocol_final_review','accepted_composition')
ordinary = O+'resume-elimination-20261107/ordinary-chains'
ordinary_review = O+'resume-sol-review-ordinary-chains-20261107/REVIEW.md'
ordinary_hash = '6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3'
manifest = read(ordinary+'/MANIFEST.json')
for name, h in manifest.items():
    pin(ordinary+'/'+name,h)
for n in (336,335,334):
    # Shared author report lives one level above each IR, unlike other packets.
    directory = ordinary+'/'+str(n)
    data = read(directory+'/candidate-ir.json')
    source = read(components['exact319']['candidate']['path'])
    delta = {}
    for field in ('coordinates','residuals'):
        a={x['id']:x for x in source[field]}; b={x['id']:x for x in data[field]}
        assert len(b)==len(data[field])
        delta[field]={'deleted':sorted(a.keys()-b.keys()),'added':sorted(b.keys()-a.keys()),'changed':sorted(i for i in a.keys()&b.keys() if a[i]!=b[i])}
    key='ordinaryExact319_'+str(n)
    components[key]={'id':key,'candidate':pin(directory+'/candidate-ir.json'),'polynomial':pin(directory+'/polynomial.json'),
        'report':pin(ordinary+'/REPORT.md'),'review':pin(ordinary_review,ordinary_hash),
        'recordedStatus':'accepted_ordinary_lift_of_exact319_only','componentAuthor':'/root/astra_quartic_opt01_elimination',
        'recordedReviewer':'/root/sol_protocol_final_review','comparedWith':'exact319','variables':len(data['coordinates']),
        'residuals':len(data['residuals']),'objectDelta':delta,'newApprovalCreatedHere':False}
add('sparseLucas320', U+'10-combination/sparse-lucas320','candidate320-ir.json','polynomial320.json',
    O+'review-sparse-lucas320-20261107/REVIEW.md','fef1d4cc3fad17ee386d7a2999128efab23deb3a825258ae653cfbad4de5cbd2',
    'combined320','/root/astra_quartic_opt10_combination','/root/astra_bl_horizontal_repair','accepted_exact_term_count_alternative')

# Counts are explicitly imported from reviewed reports, not a new SOS computation.
for key, count in {'chain323':5840,'combined315':5729,'ordinaryExact319_336':5707,'ordinaryExact319_335':5704,'ordinaryExact319_334':5701,'sparseLucas320':5598}.items():
    components[key]['reviewedMonomialCount']=count
for key,c in components.items():
    c['canonicalCandidateId']='sha256:'+c['candidate']['sha256']
    c['displayId']=key
    c['countIsNotIdentity']=True
components['combined315']['transportedComponent']='chain323'
components['combined318']['transportedComponent']='exact319'
components['threeAnchor319']['transportedComponent']='abscissa359'
components['combined320']['transportedComponent']='abscissa359'

catalog['selectedAcceptedCandidate']='combined315'
catalog['selectedAcceptedCanonicalId']=components['combined315']['canonicalCandidateId']
catalog['selectedAcceptedLineage']=catalog.pop('selectedPendingLineage')+['combined315']
catalog['soundnessOrderFor315']=['Invert the exact chain map to recover every coordinate of an actual combined318 solution.']+catalog.pop('soundnessOrderForPending318')
catalog['completenessOrderFor315']=catalog.pop('completenessOrderForPending318')+['Assign the unique R^3 helper values of chain323 last; all arithmetic outputs and previous choices stay fixed.']
catalog['canonicalIdRule']='The SHA-256 of the exact candidate IR is authoritative; display IDs and variable counts are only labels.'
catalog['ordinaryScope']='The three ordinary lifts are accepted only on exact319. They are not accepted lifts of combined318 or combined315.'
catalog['sparseScope']='SparseLucas320 is accepted only on combined320. A transport onto combined315 needs its own literal and finite review.'
catalog['publication']='315 is above the strict below-300 threshold; this packet authorizes no publication.'
catalog['dependencyEdges']=[{'candidate':k,'dependsOn':c['comparedWith'],'role':'immediate source or literal comparison base'}
    for k,c in components.items() if c.get('comparedWith')]
catalog['dependencyEdges'] += [{'candidate':k,'dependsOn':c['transportedComponent'],'role':'transported separately reviewed component'}
    for k,c in components.items() if c.get('transportedComponent')]

for row in apps['newInternalEntries']:
    row['selected315Dependency']=row.pop('selected318Dependency')
apps['selectedCandidateId']=catalog['selectedAcceptedCanonicalId']
apps['revision']=2
apps['status']='Preparatory inventory revision 2. Recorded component acceptances only; no new proof or exposition approval.'

def entry(key,comp,kind,headings,old,new,proof,consumers,selected):
    c=components[comp]
    e={'id':key,'component':comp,'kind':kind,'selected315Dependency':selected,'oldObject':old,'newObject':new,
       'requiredInternalLemmaOrMap':proof,'baselineApplications':['V13-'+x for x in consumers.split()],
       'authorProof':[section(c['report']['path'],h) for h in headings], 'recordedReview':c['review'],
       'author':c['componentAuthor'],'reviewer':c['recordedReviewer'],'recordedStatus':c['recordedStatus'],'newApprovalCreatedHere':False}
    apps['newInternalEntries'].append(e)
    for a in apps['applications']:
        if a['id'] in e['baselineApplications']:
            a['newEntryIds'].append(key)
    return e

entry('N20-EXACT-LAURENT-CHAIN','chain323','exact_private_helper_equivalence',
      ['## Exact equations and domains','## Both witness maps','## Literal incidence and count'],
      'Private E2 and E11 intermediates in each of the three326 detectors.',
      'Delete E2; repurpose E11 as J=R^3 with EJ=R^2, E4J=E, E19J=E8^2.',
      'Retained ER=1 proves R,E nonzero on every rational solution, before H interpretation. The first equation forces J=R^3 nonzero; successive assignments force the identical powers E4,E8,E19,E39,E79,E158,E157. Reverse restores E2=E^2 and E11=E^11. No square-root choice or extra arithmetic hypothesis. In combined315 every outside consumer and the unscaled anchor remain fixed.',
      'TORIC-POWERS GROUPED-POLYNOMIALS FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',True)
entry('N21-ORDINARY-WEIGHTED-CHAIN','ordinaryExact319_334','exact_unique_constant_extension',
      ['## Weighted squaring chains','## Quadratic lift and both maps','## Exact coefficient maxima'],
      'Fixed coefficient C=3^(2^25) in exact319 rows504 and903.',
      'Add Q=q and 14,15 or16 uniquely assigned constants c0=3^a0, ci=3^ai*cprev^2; use c_last in both anchor consumers.',
      'Integer exponent recurrence ends at 2^25 for each recorded list. Output-linear equations force unique rational chain values. Forget Q and constants for the inverse. Q prevents cubic C-variable times root-coordinate-square terms. Exact maxima include the inherited constant coefficient K and equal 3^4098+K,3^2050+K,3^1026+K. Only exact319 is within the accepted scope.',
      'ORDINARY-GATE ANCHOR-RESCALING SOS-FINITE FINITE-COUNTS FINAL-COMPLETENESS',False)
entry('N22-SPARSE-LUCAS','sparseLucas320','unconditional_affine_coordinate_equivalence',[],
      'Private C=A*Z and V=A*T; F+1=T^2+4Z^2-4ZC+2ZV+C^2-CV.',
      'S=C-2Z=(A-2)Z; F+1=T^2+S^2-SV.',
      'Forward subtracts twice slots244/245 from slots249/250; inverse adds them. The only consumers are rows201,202,205,206. Keep physical output components v253 and2*v254, V=A*T and every other coordinate. No division, nonzero condition or arithmetic change. This saves61 monomials, zero variables, on combined320 only.',
      'LOG-TRANSFER GROUPED-POLYNOMIALS INPUT-PARITY FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',False)
apps['newInternalEntries'][-1]['authorProof']=[dict(pin(U+'10-combination/sparse-lucas320/REPORT.md'),startLine=1,endLine=len((ROOT/U/'10-combination/sparse-lucas320/REPORT.md').read_text().splitlines()),heading='Whole report')]
entry('N23-RESTRICTED-CONSTANT-BOUND','ordinaryExact319_334','optional_finite_circuit_bound_not_arithmetic_input',
      ['## What the chain lower bound proves'],
      'No unrestricted gate-minimality statement in the selected construction.',
      'Only acyclic output-linear monomial constant gates, counted seeds, exponent cap A, at most two earlier factors and fixed separate Q lift.',
      'Induction gives absolute exponent <=A(2^n-1). The isolated squared multiplier coefficient bounds A by bit_length(3^(2A))<=B. For caps3247 and8193, A<=1024 and2584, hence at least16 and14 constant gates. Exclude implicit definitions, division, uncounted seeds, nonconstant shared gates and alternative rescalings. This claim is optional and never a premise for integer projection.',
      'ORDINARY-GATE FINITE-COUNTS',False)
for e in apps['newInternalEntries']:
    if e['id'].startswith(('N21-','N23-')):
        e['coveredComponentIds']=['ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336']

for a in apps['applications']:
    # Preserve historical prose as history rather than leaving an obsolete status current.
    a['revision1ReleaseNote']=a.pop('releaseNote')
    if a['id'] in ('V13-FINITE-COUNTS','V13-SOS-FINITE'):
        a['revision2Note']='The selected symbolic candidate is combined315:315 variables,285 residuals,5732 coefficient-power entries and5729 monomials. Ordinary and sparse variants have separate canonical IDs and reviews.'
    elif a['id']=='V13-FINAL-COMPLETENESS':
        a['revision2Note']='After the accepted318 construction, assign the unique new chain helpers. No new finite, real or contact-prime choice. Selected315 retains original Pi19.'
    elif a['id']=='V13-ORDINARY-GATE':
        a['revision2Note']='The 334/335/336 ordinary lifts now have independent acceptance on exact319 only; the previous packet correctly recorded their absence at its snapshot time.'
    elif a['id']=='V13-TORIC-POWERS':
        a['revision2Note']='Add N20 for the selected315 chain; all consumed powers are unchanged.'

write('APPLICATION-DELTA.json',apps)
write('CANDIDATES.json',catalog)
write('RETAINED-SOURCES.json',retained)
alternatives.append({'id':'separate-transports','status':'not_approved_by_this_packet','description':'Separate sparse315 and ordinary-sparse315 transports are outside this revision. No files or counts for those compositions are treated as accepted here.'})
write('PRESERVED-ALTERNATIVES.json',alternatives)
write('PREVIOUS-REVISION.json',prior)
write('STATUS-SNAPSHOT.json',read(U+'10-combination/STATUS.json'))
write('SOURCE-PINS.json',pins)

# The TeX is a proposed exposition, not a new mathematical authority.
outline_path=HERE/'PROOF-INTEGRATION-OUTLINE.tex'
outline_lines=outline_path.read_text(encoding='utf-8').splitlines()
sections={
    'charts':[1,2,3], 'contact':[4,5,6], 'anchor':[7,8,15,16,17],
    'detectors':[9,10,11,13,14], 'unscale':[18], 'chain':[12,20],
    'variants':[19,21,22,23],
}
mapping=[]
for label,nums in sections.items():
    marker='\\label{outline:'+label+'}'
    hits=[i+1 for i,s in enumerate(outline_lines) if marker in s]
    assert len(hits)==1,(label,hits)
    for n in nums:
        entry_obj=next(e for e in apps['newInternalEntries'] if e['id'].startswith('N%02d-'%n))
        consumers=[a for a in apps['applications'] if a['id'] in entry_obj['baselineApplications']]
        mapping.append({'entryId':entry_obj['id'],'outlineLabel':'outline:'+label,'outlineLabelLine':hits[0],
            'authorProof':entry_obj['authorProof'],'recordedNonAuthorReview':entry_obj['recordedReview'],
            'inventoryConsumers':[{'applicationId':a['id'],'baselineConsumerSpans':a['baselineConsumers']} for a in consumers],
            'constructionConsumers':(['combined315'] if entry_obj['selected315Dependency'] else entry_obj.get('coveredComponentIds',[entry_obj['component']])),
            'newTextApprovalRequired':True})
assert len(mapping)==23
write('INTEGRATION-MAP.json',{'outline':{'path':outline_path.relative_to(ROOT).as_posix(),
    'sha256':hashlib.sha256(outline_path.read_bytes()).hexdigest()},'status':'proposed exposition only','entries':mapping})

lines=['# Canonical candidate index','',
    'The IR hash identifies the candidate. Equal variable counts do not identify the same construction.','',
    '| Display ID | Variables | Immediate comparison source | Exact IR SHA-256 | Recorded status |',
    '|---|---:|---|---|---|']
for k,c in components.items():
    lines.append('| '+k+' | '+str(c['variables'])+' | '+str(c.get('comparedWith') or 'published baseline')+' | `'+c['candidate']['sha256']+'` | '+c['recordedStatus']+' |')
(HERE/'CANONICAL-INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Structural checks only. Source acceptance is read from the pinned independent reports.
assert len(apps['applications'])==39 and len(apps['newInternalEntries'])==23
assert len(components)==22
assert len({x['canonicalCandidateId'] for x in components.values()})==22
for e in apps['newInternalEntries']:
    assert e['author']!=e['reviewer'] and not e['newApprovalCreatedHere']
    assert set(e['baselineApplications']) <= {a['id'] for a in apps['applications']}
for k in ('combined318','chain323','combined315','sparseLucas320','ordinaryExact319_334','ordinaryExact319_335','ordinaryExact319_336'):
    assert components[k]['review'] and components[k]['recordedStatus'].startswith('accepted')
for n,p in prior.items():
    pin(p['path'],p['sha256'])
write('CHECKS.json',{'status':'passed_structural_notes_checks','baselineApplications':39,'internalEntries':23,'canonicalCandidates':22,
    'selected':'combined315','selectedVariables':315,'sourceFiles':len(pins),'priorPacketUnchanged':True,
    'ordinaryAndSparseTransportsNotApproved':True,'newMathematicalAudit':False,'productionFilesModified':False})
print(json.dumps({'applications':39,'entries':23,'candidates':22,'pins':len(pins)}))
