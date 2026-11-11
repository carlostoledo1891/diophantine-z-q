"""Check this preparatory package against actual local frozen source bytes."""
from pathlib import Path
import json
from inventory_core import digest, canonical, require, OBLIGATIONS

H=Path(__file__).resolve().parent;ROOT=H.parents[2]
REPO=ROOT/'work/quartic-version6-release/repository'
PKG=ROOT/'work/quartic-v14-prep/quartic-299-314'
def load(p):return json.loads(p.read_bytes())
def resolve(name):
    if name.startswith('quartics/quartic-299-314/'):
        return PKG/name.removeprefix('quartics/quartic-299-314/')
    if name.endswith('/evidence/route-selection.json'):return H/'ROUTE-SELECTION.json'
    return REPO/name
schema=load(H/'validation-schema.json')
pins=[schema[k] for k in ('baselineInventory','baselineManuscript','routeSelection',
                          'r6Relation','r6Manifest','repairHistory')]
pins += [p for a in schema['finalArtifacts'].values() for p in a['files']]
for pin in pins:
    require(digest(resolve(pin['path']).read_bytes())==pin['sha256'], 'source mismatch: '+pin['path'])
require(digest((PKG/'PACKAGE-MANIFEST.json').read_bytes())==
        '5369f80f69742958ea31f3a32b62b43e6b23b284063e6870af2dc2f0073977fb','package changed')
base=load(resolve(schema['baselineInventory']['path']))
plan=load(H/'BASELINE-ADAPTATION.json')['applications']
require([p['applicationId'] for p in plan]==schema['applicationIds'],'application order')
for current,old in zip(plan,base['applications']):
    require(current['priorRecordSha256']==digest(canonical(old)), 'prior record mismatch')
    require(set(current['obligationKeysRequiringFinalDecision'])==set(OBLIGATIONS),'obligation keys')
    require(current['retainedDependencyJustification'] and current['currentConstructionAndConsumerChanges'],
            'missing comparison')
route=load(H/'ROUTE-SELECTION.json')
relation=load(resolve(schema['r6Relation']['path']))
require(len(relation['edges'])==263,'R6 edges')
require(len(route['assemblyTopologicalOrder'])==24,'selected source closure')
require(route['selectedSymbolic']=='reciprocal299r2' and route['selectedOrdinary']=='ordinaryReciprocal299_314','selected pair')
print(json.dumps({'status':'preparation_source_pins_pass','realPinnedFiles':len(pins),
 'baselineApplications':len(plan),'obligationsRequiringFinalBindings':len(plan)*9,
 'r6Edges':263,'assemblyIRs':24,'finalApplicationRecordsCreated':False,
 'finalManuscriptBound':False,'acceptanceCreated':False},sort_keys=True))
