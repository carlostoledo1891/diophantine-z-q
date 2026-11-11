"""Read-only replay of final author records; optional report is written locally."""
from pathlib import Path
from copy import deepcopy
import argparse,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import inventory_core as core
import install_inventory as installer

H=Path(__file__).resolve().parent;ROOT=H.parent.parents[2]
REPO=ROOT/'work/quartic-v14-release/preview-repository'
P=core.PREFIX
ap=argparse.ArgumentParser();ap.add_argument('--report',type=Path);args=ap.parse_args()
def load(p):return core.parse(p.read_bytes())
overlay={str(p.relative_to(H/'install-root')).replace('\\','/'):p.read_bytes()
         for p in (H/'install-root').rglob('*') if p.is_file()}
files=core.Files(REPO,overlay)
inv=core.parse(overlay[P+'APPLICATIONS.json'])
schema=core.parse(overlay[P+'validation-schema.json'])
contract=core.parse(overlay[P+'quartic-application.json'])
result=core.validate(inv,schema,files)
installer.contract_check(contract,inv,files)
for name in ['APPLICATIONS.json','quartic-application.json']:
    core.require((H/name).read_bytes()==overlay[P+name],'local/staged record mismatch')
mapping=core.parse(files.pin(inv['selectedApplicationMap']))
entries=core.parse(files.pin(inv['newInternalEntries']))
core.require(core.identical(mapping['edges'],inv['edgeBindings']),'duplicate maps differ')
core.require(mapping['assemblyOrder']==inv['assemblyOrder'],'assembly map mismatch')
core.require(len(entries['entries'])==48,'entry inventory incomplete')
active={e['entryId'] for e in entries['entries'] if e['disposition']=='current_application'}
core.require(len(active)==32,'current entry count')
source_spans=review_pins=0
for entry in entries['entries']:
    core.require(entry['newAcceptanceCreated'] is False,'invented acceptance')
    for span in entry['portableProofSpans']+entry['currentDerivationSpans']:
        files.span(span);source_spans+=1
    for pin in entry['portableReviewPins']:
        files.pin(pin);review_pins+=1
    if entry['entryId'] in active:
        core.require(entry['portableProofSpans'] and entry['currentDerivationSpans'],'unbound current entry')
manifest=core.parse(overlay[P+'inventory-install-manifest.json'])
for name,pin in manifest['files'].items():
    data=files.read(name)
    core.require(core.digest(data)==pin['sha256'] and len(data)==pin['bytes'],'installed byte mismatch')
for name,pin in manifest['readOnlyDependencies'].items():
    data=files.read(name)
    core.require(core.digest(data)==pin['sha256'] and len(data)==pin['bytes'],'source changed since installation')

transport=load(H/'SPAN-TRANSPORT.json')
old=files.pin(transport['originalAddition']);new=files.pin(transport['newAddition'])
layout=core.parse(files.pin(transport['layoutChanges']))
transformed=old
for change in layout['changes']:
    before=change['old'].encode();after=change['new'].encode()
    core.require(transformed.count(before)==1,'layout source ambiguity')
    transformed=transformed.replace(before,after)
core.require(transformed==new,'non-layout change')
for passage in transport['passages']:
    a,b=passage['oldLines'];x,y=passage['newLines']
    left=b''.join(old.splitlines(keepends=True)[a-1:b])
    right=b''.join(new.splitlines(keepends=True)[x-1:y])
    core.require(core.digest(left)==passage['oldSpanSha256'] and core.digest(right)==passage['newSpanSha256'],'span transport hash')
    for change in layout['changes']:left=left.replace(change['old'].encode(),change['new'].encode())
    core.require(left==right and new.count(right)==1,'span not moved by unique content')

mutations={
 'missing_obligation':lambda d:d['applications'][0]['obligations'].pop('required_inputs'),
 'missing_dependency_disposition':lambda d:d['applications'][0]['dependencyDisposition'].pop('exceptional_cases'),
 'self_acceptance':lambda d:d.update(mathematicalAcceptanceClaim=True),
 'wrong_ordinary':lambda d:d['selected'].update(ordinary='ordinaryReciprocal299_315'),
 'old_manuscript':lambda d:d['manuscript'].update(sha256='200a2af2b33bcca5a214f049225add3b928e7b570657e5d59fc7308805c37e3b'),
 'missing_edge':lambda d:d['edgeBindings'].pop(),
 'wrong_coefficient_bound':lambda d:d['finalArtifacts']['314'].update(coefficientQualification='below2^3247'),
 'stale_current_span':lambda d:d['applications'][0]['dependencyDisposition']['required_inputs']['consumerSpans'][0].update(sha256_raw_utf8_span='0'*64),
}
for name,mutate in mutations.items():
    changed=deepcopy(inv);mutate(changed)
    try:core.validate(changed,schema,core.Files(REPO,overlay))
    except (core.Invalid,KeyError):pass
    else:raise core.Invalid('negative accepted: '+name)

preserved=sum(d['mode']=='preserved' for a in inv['applications'] for d in a['dependencyDisposition'].values())
result.update({'status':'author structural replay passed; no mathematical acceptance created',
 'preservedObligationStatements':preserved,'replacedObligationStatements':351-preserved,
 'selectedEntryCount':32,'allEntryCount':48,'entryProofAndCurrentSpans':source_spans,
 'historicalReviewPinsChecked':review_pins,'contentAnchoredPassages':len(transport['passages']),
 'negativeControls':list(mutations),'negativeControlsPassed':len(mutations),
 'inventorySha256':core.digest(overlay[P+'APPLICATIONS.json']),
 'contractSha256':core.digest(overlay[P+'quartic-application.json']),
 'manuscript':inv['manuscript']})
if args.report:args.report.write_bytes(installer.encoded(result))
print(json.dumps(result,sort_keys=True))
