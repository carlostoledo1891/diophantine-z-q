"""Read-only, independently implemented final-records-002 structural audit."""
from pathlib import Path
import collections
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
PACK = OUT.parent / 'final-records-002'
REPO = ROOT / 'work/quartic-v14-release/preview-repository'
PREFIX = 'docs/manuscript-revisions/version14/'
errors, observations, checked_pins, checked_spans = [], [], {}, {}

def check(ok, message):
    if not ok:
        errors.append(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def pairs(items):
    obj = {}
    for key, value in items:
        if key in obj:
            raise ValueError('duplicate JSON key: ' + key)
        obj[key] = value
    return obj

def parse(path):
    return json.loads(path.read_bytes(), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()

def resolve(name):
    check(not Path(name).is_absolute() and ':' not in name and '\\' not in name
          and '..' not in Path(name).parts, 'unsafe path: ' + name)
    if name.startswith('work/'):
        return ROOT / name
    staged = PACK / 'install-root' / name
    return staged if staged.is_file() else REPO / name

def pin(obj, context):
    path = resolve(obj['path'])
    if not path.is_file():
        errors.append(context + ': missing ' + obj['path'])
        return b''
    data = path.read_bytes()
    check(sha(data) == obj['sha256'], context + ': hash ' + obj['path'])
    if 'bytes' in obj:
        check(len(data) == obj['bytes'], context + ': size ' + obj['path'])
    checked_pins[str(path.relative_to(ROOT))] = sha(data)
    return data

def walk(obj, context):
    if isinstance(obj, dict):
        if 'path' in obj and 'sha256' in obj:
            data = pin(obj, context)
            start, end = obj.get('start_line'), obj.get('end_line')
            if start is not None:
                lines = data.splitlines(keepends=True)
                check(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), context + ': span bounds')
                raw = b''.join(lines[start-1:end])
                check(sha(raw) == obj['sha256_raw_utf8_span'], context + ': span hash')
                checked_spans[(obj['path'], start, end)] = sha(raw)
            if 'label' in obj:
                label = ('\\label{' + obj['label'] + '}').encode()
                check(data.count(label) == 1, context + ': label uniqueness')
                if 'line' in obj:
                    check(label in data.splitlines()[obj['line']-1], context + ': label line')
            if 'startLine' in obj:
                lo, hi = obj['startLine'], obj['endLine']
                lines = data.decode('utf-8').splitlines()
                check(1 <= lo <= hi <= len(lines), context + ': historical bounds')
                if 'heading' in obj:
                    if obj['heading'] == 'Whole report':
                        check(lo == 1 and hi == len(lines), context + ': whole report range')
                    else:
                        check(obj['heading'] in lines[lo-1:hi], context + ': historical heading')
        for key, val in obj.items():
            walk(val, context + '/' + key)
    elif isinstance(obj, list):
        for i, val in enumerate(obj):
            walk(val, context + '/' + str(i))

manifest = parse(PACK/'FROZEN-MANIFEST.json')
check(sha((PACK/'FROZEN-MANIFEST.json').read_bytes()) == '45b012aaf2fc75698c8c62d4a9ac24fe2593116d1a75a838072365a938aa75f5', 'requested manifest pin')
for name, item in manifest['files'].items():
    data = (PACK/name).read_bytes()
    check(sha(data) == item['sha256'] and len(data) == item['bytes'], 'manifest file: '+name)
actual = {str(p.relative_to(PACK)).replace('\\','/') for p in PACK.rglob('*') if p.is_file() and '__pycache__' not in str(p)}
check(actual == set(manifest['files']) | {'FROZEN-MANIFEST.json'}, 'frozen file enumeration')
inv = parse(PACK/'APPLICATIONS.json')
contract = parse(PACK/'quartic-application.json')
entries = parse(PACK/'selected-entries.json')
mapping = parse(PACK/'selected-application-map.json')
transport = parse(PACK/'SPAN-TRANSPORT.json')
gate = parse(PACK/'GATE-OBLIGATION-TEXTS.json')
check(sha((PACK/'APPLICATIONS.json').read_bytes()) == 'a3c7f119e53f59ed81f4f9a3ac6b57f069c1d24da191aef5e150b38a50933abf', 'requested applications pin')
check(sha((PACK/'quartic-application.json').read_bytes()) == '92dac763a44921556152bd0cbdf050eed7fb26ea12fb935b6060345c138f6ad1', 'requested contract pin')
for name in ['APPLICATIONS.json', 'quartic-application.json', 'selected-entries.json', 'selected-application-map.json']:
    target = PREFIX + (('evidence/' if name.startswith('selected-') else '') + name)
    check((PACK/name).read_bytes() == resolve(target).read_bytes(), 'staged duplicate '+name)
for name,obj in [('inventory',inv),('contract',contract),('entries',entries),('mapping',mapping),('transport',transport)]:
    walk(obj,name)
sourcepins = parse(PACK/'SOURCE-PINS.json')
walk(sourcepins, 'sourcepins')
for path, item in sourcepins['readOnlyRepositoryDependencies'].items():
    pin(dict(path=path, **item), 'sourcepins dependencies')
install = parse(resolve(PREFIX+'inventory-install-manifest.json'))
for group in ['files','readOnlyDependencies']:
    for path,item in install[group].items():
        pin(dict(path=path, **item), 'install manifest '+group)
schema = parse(resolve(PREFIX+'validation-schema.json'))
baseline = parse(resolve(inv['baselineInventory']['path']))
route = parse(resolve(inv['routeSelection']['path']))
relation = parse(resolve(inv['r6Relation']['path']))
manuscript = pin(inv['manuscript'],'manuscript')
addition = pin(inv['addition'],'addition')
check(inv['manuscript']['sha256'] == 'b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d','b842 target')
check(inv['addition']['sha256'] == 'b5840b3598c655fc7f3db3475b089b65800b98f136a601c4360c72d22d6f95a0','b584 target')
check(manuscript.count(addition)==1,'addition unique embedding')
offset = len(manuscript[:manuscript.index(addition)].splitlines())
for obj in [contract,entries,mapping]:
    check(obj['manuscript']==inv['manuscript'],'shared manuscript pin')
check(mapping['addition']==inv['addition'],'shared addition pin')
for label in schema['requiredLabels']:
    needle=('\\label{'+label+'}').encode()
    check(manuscript.count(needle)==1 and addition.count(needle)==1,'required label '+label)
keys=set('required_inputs constructed_inputs domain_and_index_coverage transition_maps_and_scalars identity_of_consumed_object exceptional_cases affected_downstream_claims source_version_and_conventions validation_and_acceptance_scope'.split())
ids=[a['id'] for a in inv['applications']]
check(len(ids)==len(set(ids))==39 and ids==schema['applicationIds'],'39 exact application IDs')
old={a['id']:a for a in baseline['applications']}
modes=collections.Counter()
obligation_rows=[]
for a in inv['applications']:
    aid=a['id']; prior=old[aid]
    check(sha(canonical(prior))==a['priorRecordSha256'],'prior record '+aid)
    check(a['sourceVersionAndConventions']==prior['source'],'source retention '+aid)
    check(set(a['obligations'])==set(a['dependencyDisposition'])==keys,'nine keys '+aid)
    for key in sorted(keys):
        value=a['obligations'][key]; d=a['dependencyDisposition'][key]; modes[d['mode']]+=1
        check(isinstance(value,str) and value.strip().lower() not in ['','pending','todo','tbd','unchanged'],'substantive text '+aid+'/'+key)
        check(d['mode'] in ['preserved','replaced'] and d['justification'].strip(),'disposition '+aid+'/'+key)
        if d['mode']=='preserved':
            check(value==prior['obligations'][key],'preserved exact text '+aid+'/'+key)
        check(bool(d['sourceSpans']) and bool(d['consumerSpans']),'evidence lists '+aid+'/'+key)
        for s in d['consumerSpans']:
            check(all(s[k]==inv['manuscript'][k] for k in ['path','sha256']),'current consumer '+aid+'/'+key)
        obligation_rows.append({'applicationId':aid,'key':key,'mode':d['mode'],'textSha256':sha(value.encode()),'sourceSpanCount':len(d['sourceSpans']),'consumerSpanCount':len(d['consumerSpans'])})
pair=lambda e:(e['applicationId'],e['entryId'])
edgepairs=[pair(e) for e in inv['edgeBindings']]
check(len(edgepairs)==len(set(edgepairs))==263,'263 unique edges')
check(set(edgepairs)=={pair(e) for e in relation['edges']},'R6 complete edge set')
check(mapping['edges']==inv['edgeBindings'],'selected map edge equality')
expectedroles={pair(e):'current_consumer' for e in route['candidateCurrentApplicationEdges']}
expectedroles.update({pair(e):'supporting_derivation' for e in route['supportingSourceEdges']})
roles=collections.Counter()
for e in inv['edgeBindings']:
    expected=expectedroles.get(pair(e),'archived');roles[e['role']]+=1
    check(e['role']==expected,'route edge role '+str(pair(e)))
    check(e['applicationId'] in ids and e['justification'].strip(),'edge ID/justification '+str(pair(e)))
    check(bool(e['sourceSpans'])==bool(e['consumerSpans'])==(e['role']!='archived'),'edge evidence state '+str(pair(e)))
    for s in e['consumerSpans']:
        check(all(s[k]==inv['manuscript'][k] for k in ['path','sha256']),'edge current consumer '+str(pair(e)))
entryids=[e['entryId'] for e in entries['entries']]
check(len(entryids)==len(set(entryids))==48,'48 unique entries')
routeentries={e['entryId']:e for e in route['entryDispositions']}
check(set(entryids)==set(routeentries),'exact route entry set')
entryroles=collections.Counter()
for e in entries['entries']:
    olde=routeentries[e['entryId']];entryroles[e['disposition']]+=1
    for left,right in [('disposition','role'),('historicalAuthorProof','recordedProof'),('historicalRecordedReview','recordedReview'),('historicalComponents','recordedComponents'),('selectedComponents','selectedComponents')]:
        check(e[left]==olde[right],'entry inherited '+e['entryId']+'/'+left)
    check(e['newAcceptanceCreated'] is False,'entry acceptance flag')
    active = e['disposition'] in ['current_application','supporting_source']
    check(len(e['portableProofSpans'])==(len(e['historicalAuthorProof']) if active else 0),'proof transport count '+e['entryId'])
    for h,s in zip(e['historicalAuthorProof'],e['portableProofSpans']):
        check(h['sha256']==s['sha256'] and h['startLine']==s['start_line'] and h['endLine']==s['end_line'],'proof transport '+e['entryId'])
    check(len(e['portableReviewPins'])==1 and e['portableReviewPins'][0]['sha256']==e['historicalRecordedReview']['sha256'],'review transport '+e['entryId'])
    check(bool(e['currentDerivationSpans'])==active,'entry current span state '+e['entryId'])
    for s in e['currentDerivationSpans']:
        check(all(s[k]==inv['manuscript'][k] for k in ['path','sha256']),'entry target '+e['entryId'])
check(all(e['entryId'] in entryids for e in inv['edgeBindings']),'edge entries resolve')
assembly=route['assemblyTopologicalOrder']; positions={name:i for i,name in enumerate(assembly)}
check(len(assembly)==len(set(assembly))==24 and assembly==inv['assemblyOrder']==mapping['assemblyOrder'],'24 assembly identity')
for edge in route['assemblyEdges']:
    check(positions[edge['dependsOn']]<positions[edge['candidate']],'assembly topological edge')
check(inv['selected']=={'symbolic':'reciprocal299r2','ordinary':'ordinaryReciprocal299_314'}==mapping['selected']==schema['selected'],'exact route selection')
check(inv['mathematicalAcceptanceClaim'] is False,'no mathematical acceptance')
check(inv['externalSources']==baseline['externalSources'] and inv['existingSourceCatalog']==baseline['existingSourceCatalog'],'external qualification retention')
for span in contract['manuscript_spans']:
    raw=b''.join(manuscript.splitlines(keepends=True)[span['start_line']-1:span['end_line']])
    check(sha(raw)==span['sha256'],'contract span '+str(span['start_line']))
edits=parse(resolve(inv['edits']['path']))
check(contract['reviewed_edits']=={e['id']:sha(canonical(e)) for e in edits if e.get('contract_id')==contract['id']},'contract exact reviewed edits')
check(set(contract['obligations'])==set('source_hypotheses constructed_objects index_domain_coverage transition_maps limiting_object_identity coefficient_conventions local_conditions exceptional_cases downstream_consumption'.split()),'contract nine obligation keys')
for key,obj in contract['obligations'].items():
    check(obj['status'] in ['checked','not_applicable'] and all(obj[k].strip() for k in ['required','constructed','justification']),'contract text '+key)
    check(set(obj['sources']) <= {s['id'] for s in contract['sources']} and bool(obj['sources']),'contract source refs '+key)
    check(set(obj['evidence']) <= set(contract['evidence']) and bool(obj['evidence']),'contract evidence refs '+key)
original=pin(transport['originalAddition'],'transport original'); layout=parse(resolve(transport['layoutChanges']['path']))
changed=original
for edit in layout['changes']:
    left,right=edit['old'].encode(),edit['new'].encode()
    check(changed.count(left)==1,'unique layout replacement')
    changed=changed.replace(left,right)
check(len(layout['changes'])==3 and changed==addition,'exact three layout replacements')
check(len(transport['passages'])==84,'84 transported passages')
for p in transport['passages']:
    lo,hi=p['oldLines']; left=b''.join(original.splitlines(keepends=True)[lo-1:hi])
    lo,hi=p['newLines']; right=b''.join(addition.splitlines(keepends=True)[lo-1:hi])
    check(sha(left)==p['oldSpanSha256'] and sha(right)==p['newSpanSha256'],'transport hashes')
    for edit in layout['changes']:
        left=left.replace(edit['old'].encode(),edit['new'].encode())
    check(left==right and addition.count(right)==1,'content anchored transport')
    mapped=b''.join(manuscript.splitlines(keepends=True)[lo+offset-1:hi+offset])
    check(mapped==right,'transport manuscript embedding')
check([f['id'] for f in gate['fragments']]==ids,'39 gate fragment IDs')
for f,a in zip(gate['fragments'],inv['applications']):
    check(len(f['obligations'])==9,'gate nine text slots')
    check(f['sources']==a['sourceVersionAndConventions'],'gate source metadata')
    for obj in f['obligations'].values():
        check(obj['required']==a['obligations']['required_inputs'] and obj['constructed']==a['obligations']['constructed_inputs'],'gate text transport')
        check(obj['evidence']==f['proposedFiles'],'gate evidence transport')
check(len(gate['missingRequiredGateFields'])==3,'gate incomplete disclaimer')
mojibake=[]
for row in inv['applications']:
    for key,value in row['obligations'].items():
        if '\u00c2' in value or '\u00c3' in value:
            mojibake.append({'applicationId':row['id'],'key':key,'text':value})
result={'scope':'Independent structural and byte-binding review; no mathematical acceptance or gate approval',
        'packetManifestSha256':sha((PACK/'FROZEN-MANIFEST.json').read_bytes()),
        'errors':errors,'counts':{'frozenFiles':len(manifest['files']),'applications':len(ids),'obligations':len(obligation_rows),'modes':dict(modes),'edges':len(edgepairs),'edgeRoles':dict(roles),'entries':len(entryids),'entryRoles':dict(entryroles),'assemblyIRs':len(assembly),'distinctResolvedPins':len(checked_pins),'distinctRawSpans':len(checked_spans),'contractSpans':len(contract['manuscript_spans']),'contentAnchoredPassages':len(transport['passages'])},
        'additionFirstManuscriptLine':offset+1,'mojibakeObligationFields':mojibake,'resolvedPins':checked_pins}
(OUT/'INDEPENDENT-CHECK.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(OUT/'OBLIGATION-COVERAGE.json').write_text(json.dumps(obligation_rows,indent=2)+'\n',encoding='utf-8')
(OUT/'EDGE-COVERAGE.json').write_text(json.dumps([
    {'applicationId':e['applicationId'],'entryId':e['entryId'],'role':e['role'],
     'recordSha256':sha(canonical(e)),'sourceSpanCount':len(e['sourceSpans']),
     'consumerSpanCount':len(e['consumerSpans'])} for e in inv['edgeBindings']],indent=2)+'\n',encoding='utf-8')
(OUT/'ENTRY-COVERAGE.json').write_text(json.dumps([
    {'entryId':e['entryId'],'role':e['disposition'],'recordSha256':sha(canonical(e)),
     'portableProofSpanCount':len(e['portableProofSpans']),
     'currentSpanCount':len(e['currentDerivationSpans']),
     'historicalReviewPinCount':len(e['portableReviewPins'])} for e in entries['entries']],indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['resolvedPins','mojibakeObligationFields']},indent=2))
print('mojibake fields',len(mojibake))
