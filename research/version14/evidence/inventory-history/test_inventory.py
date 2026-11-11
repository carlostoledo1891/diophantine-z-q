"""Synthetic record tests. Fixtures are not mathematical review evidence."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

import inventory_core as c
import install_inventory as installer

H=Path(__file__).resolve().parent
ROOT=H.parents[2]
REPO=ROOT/'work/quartic-version6-release/repository'
R6=ROOT/'work/quartic-optimization-20261107/resume-release-inventory-20261107-r6'


def fixture():
    schema=json.loads((H/'validation-schema.json').read_bytes())
    overlay={}
    def add(path,data):
        overlay[path]=data
        return {'path':path,'sha256':c.digest(data)}
    # Use real baseline and route identities but synthetic current prose.
    baseline=json.loads((REPO/schema['baselineInventory']['path']).read_bytes())
    overlay[schema['baselineInventory']['path']]=(REPO/schema['baselineInventory']['path']).read_bytes()
    overlay[schema['baselineManuscript']['path']]=(REPO/schema['baselineManuscript']['path']).read_bytes()
    overlay[schema['routeSelection']['path']]=(H/'ROUTE-SELECTION.json').read_bytes()
    for key,name in [('r6Relation','CANONICAL-RELATION.json'),('r6Manifest','FROZEN-MANIFEST.json'),('repairHistory','REPAIR-HISTORY.json')]:
        overlay[schema[key]['path']]=(R6/name).read_bytes()
    for item in schema['finalArtifacts'].values():
        for pin in item['files']:
            pin['sha256']=c.digest(b'fixture artifact, not a real coefficient table\n')
            overlay[pin['path']]=b'fixture artifact, not a real coefficient table\n'
    addition=b''.join(('\\label{'+label+'}\n').encode() for label in schema['requiredLabels'])
    addition+=b'This is synthetic prose for structural negative tests only.\n'
    ap=add(c.PREFIX+'addition.tex',addition)
    mp=add('manuscripts/quartic_v14.tex',b'Fixture preamble.\n'+addition+b'Fixture end.\n')
    source=add(c.PREFIX+'evidence/fixture-source.txt',b'Explicit synthetic source.\n')
    files=c.Files(REPO,overlay)
    source_span=c.bind_span(files,source,1,1)
    consumer=c.bind_span(files,mp,2,2,label='sec:v14')
    inv={k:deepcopy(schema[k]) for k in ('selected','baselineInventory','baselineManuscript','routeSelection','r6Relation','r6Manifest','repairHistory','finalArtifacts')}
    inv.update(schema='portable-application-inventory-v3',status='author_records_pending_independent_review',
               manuscript=mp,addition=ap,mathematicalAcceptanceClaim=False,
               externalSources=baseline['externalSources'],existingSourceCatalog=baseline['existingSourceCatalog'])
    inv['applications']=[]
    for old in baseline['applications']:
        inv['applications'].append({'id':old['id'],'priorRecordSha256':c.digest(c.canonical(old)),
          'sourceVersionAndConventions':deepcopy(old['source']),'obligations':deepcopy(old['obligations']),
          'dependencyDisposition':{key:{'mode':'preserved','justification':'Synthetic fixture checks structure only.',
          'sourceSpans':[deepcopy(source_span)],'consumerSpans':[deepcopy(consumer)]} for key in c.OBLIGATIONS}})
    route=json.loads(overlay[schema['routeSelection']['path']])
    relation=json.loads(overlay[schema['r6Relation']['path']])
    entries={e['entryId']:e['role'] for e in route['entryDispositions']}
    inv['assemblyOrder']=deepcopy(route['assemblyTopologicalOrder'])
    inv['edgeBindings']=[]
    for e in relation['edges']:
        role={'current_application':'current_consumer','supporting_source':'supporting_derivation'}.get(entries[e['entryId']],'archived')
        inv['edgeBindings'].append({'applicationId':e['applicationId'],'entryId':e['entryId'],'role':role,
          'justification':'Synthetic fixture disposition, not an approved proof map.',
          'sourceSpans':[] if role=='archived' else [deepcopy(source_span)],
          'consumerSpans':[] if role=='archived' else [deepcopy(consumer)]})
    edits=[{'id':'v14-fixture','old':'old','new':'new','kind':'mathematical','contract_id':'QUARTIC-299-COMPOSITION'}]
    inv['edits']=add(c.PREFIX+'new-edits.json',installer.encoded(edits))
    invpin=add(c.PREFIX+'APPLICATIONS.json',installer.encoded(inv))
    contract={'id':'QUARTIC-299-COMPOSITION','manuscript':mp,'authors':['fixture-author'],
       'sources':[{'id':'fixture','url':'https://example.invalid/fixture','version':'fixture',
                   'locator':'fixture','sha256':source['sha256']}],
       'evidence':{'inventory':invpin,'source':source},
       'manuscript_spans':[{'role':r,'start_line':2,'end_line':2,'sha256':consumer['sha256_raw_utf8_span']} for r in ('construction','application','consumer')],
       'obligations':{key:{'status':'checked','required':'Fixture condition.','constructed':'Fixture object.',
          'justification':'This is synthetic test data only.','sources':['fixture'],'evidence':['inventory','source']} for key in installer.CONTRACT_KEYS},
       'reviewed_edits':{'v14-fixture':c.digest(c.canonical(edits[0]))},
       'dependency_impact':'Synthetic fixture, not a mathematical acceptance.'}
    return inv,schema,overlay,contract


class InventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed=fixture()
    def setUp(self):
        self.inv,self.schema,self.data,self.contract=deepcopy(self.seed)
    def check(self):
        return c.validate(self.inv,self.schema,c.Files(REPO,self.data))
    def reject(self):
        with self.assertRaises((c.Invalid,KeyError)):
            self.check()
    def first(self):return self.inv['applications'][0]
    def disp(self):return self.first()['dependencyDisposition']['required_inputs']
    def test_good_fixture(self):
        self.assertEqual(self.check()['obligations'],351)
        self.assertEqual(self.check()['edgeDispositions'],{'current_consumer':185,'supporting_derivation':31,'archived':47})
    def test_missing_application(self):self.inv['applications'].pop();self.reject()
    def test_duplicate_application(self):self.inv['applications'][1]=deepcopy(self.first());self.reject()
    def test_missing_obligation(self):self.first()['obligations'].pop('required_inputs');self.reject()
    def test_missing_disposition(self):self.first()['dependencyDisposition'].pop('required_inputs');self.reject()
    def test_stale_prior_record(self):self.first()['priorRecordSha256']='0'*64;self.reject()
    def test_changed_source_convention(self):self.first()['sourceVersionAndConventions']['status']='revised';self.reject()
    def test_empty_justification(self):self.disp()['justification']='';self.reject()
    def test_placeholder_justification(self):self.disp()['justification']='pending';self.reject()
    def test_missing_source(self):self.disp()['sourceSpans']=[];self.reject()
    def test_missing_consumer(self):self.disp()['consumerSpans']=[];self.reject()
    def test_preserved_text_change(self):self.first()['obligations']['required_inputs']='Changed';self.reject()
    def test_explicit_replacement(self):
        self.disp()['mode']='replaced';self.first()['obligations']['required_inputs']='Explicit fixture replacement.';self.check()
    def test_stale_span(self):self.disp()['consumerSpans'][0]['sha256_raw_utf8_span']='0'*64;self.reject()
    def test_stale_file(self):self.data[self.inv['manuscript']['path']]+=b'x';self.reject()
    def test_bool_line(self):self.disp()['sourceSpans'][0]['start_line']=True;self.reject()
    def test_float_line(self):self.disp()['sourceSpans'][0]['end_line']=1.0;self.reject()
    def test_outside_source(self):self.disp()['sourceSpans'][0]['path']='../x';self.reject()
    def test_missing_edge(self):self.inv['edgeBindings'].pop();self.reject()
    def test_duplicate_edge(self):self.inv['edgeBindings'].append(deepcopy(self.inv['edgeBindings'][0]));self.reject()
    def test_archive_as_current(self):
        next(e for e in self.inv['edgeBindings'] if e['role']=='archived')['role']='current_consumer';self.reject()
    def test_support_as_current(self):
        next(e for e in self.inv['edgeBindings'] if e['role']=='supporting_derivation')['role']='current_consumer';self.reject()
    def test_current_without_consumer(self):
        next(e for e in self.inv['edgeBindings'] if e['role']=='current_consumer')['consumerSpans']=[];self.reject()
    def test_lost_current_entry(self):
        key=next(e['entryId'] for e in self.inv['edgeBindings'] if e['role']=='current_consumer')
        for e in self.inv['edgeBindings']:
            if e['entryId']==key:e.update(role='archived',sourceSpans=[],consumerSpans=[])
        self.reject()
    def test_wrong_chain(self):self.inv['assemblyOrder'].pop();self.reject()
    def test_wrong_companion(self):self.inv['selected']['ordinary']='ordinaryReciprocal299_315';self.reject()
    def test_old_bound(self):self.inv['finalArtifacts']['314']['coefficientQualification']='below2^3247';self.reject()
    def test_float_artifact_count(self):self.inv['finalArtifacts']['314']['variables']=314.0;self.reject()
    def test_bool_artifact_content(self):self.inv['finalArtifacts']['314']['content']=True;self.reject()
    def test_no_self_acceptance(self):self.inv['mathematicalAcceptanceClaim']=True;self.reject()
    def test_no_accepted_status(self):self.inv['status']='accepted';self.reject()
    def test_repair_history_stale(self):self.inv['repairHistory']['sha256']='0'*64;self.reject()
    def test_external_source_changed(self):self.inv['externalSources']={};self.reject()
    def test_duplicate_json_keys(self):
        with self.assertRaises(c.Invalid):c.parse(b'{"a":1,"a":2}')
    def test_nan_rejected(self):
        with self.assertRaises(c.Invalid):c.parse(b'{"a":NaN}')
    def test_path_normalization(self):
        for name in ('a//b','a/../b','/absolute','C:/x','a\\b','a/'):
            with self.assertRaises(c.Invalid):c.path_ok(name)
    def test_raw_crlf_span(self):
        data=b'one\r\ntwo\n';pin={'path':'mixed.txt','sha256':c.digest(data)}
        files=c.Files(REPO,{'mixed.txt':data});span=c.bind_span(files,pin,1,1)
        self.assertEqual(span['sha256_raw_utf8_span'],c.digest(b'one\r\n'))
    def test_full_prepare(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,data in self.data.items():
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
            output=installer.prepare(root,self.inv,self.contract,self.schema)
            manifest=json.loads(output[c.PREFIX+'inventory-install-manifest.json'])
            self.assertTrue(manifest['noAcceptanceCreated']);self.assertTrue(manifest['noCurrentRegistryCreated'])
            self.assertNotIn('docs/audit-history/current.json',output)
            for name,data in output.items():
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
            with patch('sys.argv',['validate-applications.py','--repo',str(root),'--self-test']),redirect_stdout(io.StringIO()) as report:
                c.main()
            self.assertEqual(json.loads(report.getvalue())['negativeSelfTests'],5)
            destination=root.parent/(root.name+'-prepared')
            try:
                installer.write_new(destination,output)
                with self.assertRaises(c.Invalid):installer.write_new(destination,output)
                for name,data in output.items():self.assertEqual((destination/name).read_bytes(),data)
            finally:
                if destination.exists():installer.shutil.rmtree(destination)
    def test_wrong_contract_edits(self):
        self.contract['reviewed_edits']={}
        with self.assertRaises(c.Invalid):installer.contract_check(self.contract,self.inv,c.Files(REPO,self.data))
    def test_wrong_contract_manuscript(self):
        self.contract['manuscript']=deepcopy(self.contract['manuscript']);self.contract['manuscript']['sha256']='0'*64
        with self.assertRaises(c.Invalid):installer.contract_check(self.contract,self.inv,c.Files(REPO,self.data))
    def test_missing_contract_obligation(self):
        self.contract['obligations'].pop('exceptional_cases')
        with self.assertRaises(c.Invalid):installer.contract_check(self.contract,self.inv,c.Files(REPO,self.data))
    def test_stale_contract_evidence(self):
        self.contract['evidence']['inventory']['sha256']='0'*64
        with self.assertRaises(c.Invalid):installer.contract_check(self.contract,self.inv,c.Files(REPO,self.data))
    def test_no_acceptance_extra(self):
        with self.assertRaises(c.Invalid):installer.prepare(REPO,self.inv,self.contract,self.schema,
                    {c.PREFIX+'quartic-acceptance.json':b'{}'})


if __name__=='__main__':unittest.main()
