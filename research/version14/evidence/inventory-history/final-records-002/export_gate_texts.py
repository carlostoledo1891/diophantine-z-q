"""Export caller-authored ordinary obligation text, not authenticated runs."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import inventory_core as core
import install_inventory as installer
H=Path(__file__).resolve().parent;P=core.PREFIX
inv=core.parse((H/'APPLICATIONS.json').read_bytes())
by_key={
 'source_hypotheses':'required_inputs',
 'constructed_objects':'constructed_inputs',
 'index_domain_coverage':'domain_and_index_coverage',
 'transition_maps':'transition_maps_and_scalars',
 'consumed_object_identity':'identity_of_consumed_object',
 'coefficient_conventions':'source_version_and_conventions',
 'exceptional_cases':'exceptional_cases',
 'downstream_consumption':'affected_downstream_claims'}
files=[{'side':'head','path':P+'APPLICATIONS.json','sha256':core.digest((H/'APPLICATIONS.json').read_bytes())},
       dict(side='head',**inv['manuscript']),dict(side='head',**inv['selectedApplicationMap'])]
fragments=[]
for app in inv['applications']:
    obs={}
    for key,sourcekey in by_key.items():
        obs[key]={'status':'checked','required':app['obligations']['required_inputs'],
         'constructed':app['obligations']['constructed_inputs'],
         'justification':app['obligations'][sourcekey]+' '+app['dependencyDisposition'][sourcekey]['justification'],
         'evidence':files}
    obs['local_conditions']={'status':'checked','required':app['obligations']['required_inputs'],
      'constructed':app['obligations']['constructed_inputs'],
      'justification':app['obligations']['domain_and_index_coverage']+' '+app['obligations']['exceptional_cases']+' '+app['obligations']['transition_maps_and_scalars'],
      'evidence':files}
    fragments.append({'id':app['id'],'kind':'argument','proposedFiles':files,
      'obligations':obs,'sources':app['sourceVersionAndConventions'],
      'authorship':'These obligation strings were authored by /root/astra_quartic_opt05_anchor. Actual run identities and all other application/assembly authors must be supplied by the trusted orchestrator; this string authenticates nobody.'})
out={'schema':'v14-gate-obligation-fragments-v1','status':'Caller-authored text only, not complete gate applications',
 'missingRequiredGateFields':['actual authors/run IDs','reviewed ordinary application dependencies','complete actual base/head file coverage and commits'],
 'integration':'The parent must add actual authors, dependencies and complete files to construct the exact ordinary schema2 shape. proposedFiles are proposed committed-head pins, not an assertion that a head commit exists. sources/authorship/proposedFiles are explanatory fragment metadata, not extra fields for the gate application.',
 'fragments':fragments}
(H/'GATE-OBLIGATION-TEXTS.json').write_bytes(installer.encoded(out))
print('Exported39 obligation-text fragments; no complete gate application, receipt or review created.')
