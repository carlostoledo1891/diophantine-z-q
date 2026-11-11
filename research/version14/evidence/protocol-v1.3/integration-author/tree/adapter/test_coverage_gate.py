"""Synthetic v1.3 rejection tests. Fixtures are not actual review evidence."""
import copy
import base64
import json
from pathlib import Path
import unittest
import coverage_gate as c
import offline_manifest_gate as g
import test_manifest_gate as t
import test_store_bridge as sb
import ledger_evidence_bridge as bridge


class Case:
    def __init__(self):
        self.p,self.e,self.blobs = t.fixture()
        self.files = {side:{path:(row['mode'],self.blobs.values[row['sha256']])
                           for path,row in self.p[side]['files'].items()} for side in ('base','head')}
        self.files['base'][c.PROTOCOL_PATH] = ('100644',b'Previous protocol\n')
        self.files['head'][c.PROTOCOL_PATH] = ('100644',(Path(__file__).parent/'PROTOCOL-V1.3.md').read_bytes())
        self.profile = {'schema':'protocol-coverage-policy/v1','protocol_version':'1.3',
            'governing_protocol':{'path':c.PROTOCOL_PATH,'sha256':c.PROTOCOL_SHA256},
            'runtime_policy_sha256':self.p['policy_sha256'],'mode':'substantive',
            'claim_ids':['B'],'proof_paths':['proof.md','sources/input.md'],'allowed_nonmath_paths':[]}
        def pin(path):return {'side':'head','path':path,'sha256':g.sha(self.files['head'][path][1])}
        def loc(path):
            raw=self.files['head'][path][1]
            return {'pin':pin(path),'start_line':1,'end_line':len(raw.splitlines()),'excerpt_sha256':g.sha(raw)}
        use={'id':'U','consumer':'B','passages':['B-proof'],
             'assertion':{k:'Exact synthetic '+k for k in 'statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order'.split()},
             'classification':'dependency','reason':'B invokes A here.','shared_contract_justification':None,
             'supplier':{'kind':'internal','application_id':'A','location':loc('sources/input.md'),'statement':'Exact synthetic A','publication':None},
             'application_id':'B','inline_argument':None}
        sources=[pin(p) for p in self.profile['proof_paths']]
        self.initial={'schema':'protocol-source-first/v1','sources':copy.deepcopy(sources),'uses':[copy.deepcopy(use)]}
        edge={'consumer':'B','supplier':'A','use_ids':['U'],'reason':'Direct use of A by B.'}
        self.dossier={'schema':'protocol-coverage/v1','profile_sha256':g.digest(self.profile),'mode':'substantive',
            'sources':sources,'scope':'Synthetic complete B argument only.',
            'coverage_index':[
                {'id':'B-proof','claim_ids':['B'],'location':loc('proof.md'),'status':'reviewed','reason':'Full synthetic proof.','use_ids':['U'],'no_imports_reason':None},
                {'id':'A-proof','claim_ids':['A'],'location':loc('sources/input.md'),'status':'reviewed','reason':'Synthetic source.','use_ids':[],'no_imports_reason':'A is a direct derivation with no imported inputs.'}],
            'initial':None,'reconstruction':{'run_id':'reviewer','method':'Read frozen sources before inventory comparison.',
            'prior_exposure':'No prior exposure in this synthetic fixture.','limitations':'Synthetic data tests structure only.',
            'frozen_at':'2026-11-07T01:00:00Z','compared_at':'2026-11-07T01:01:00Z'},
            'reconciled_uses':[use],'declared_edges_before':[copy.deepcopy(edge)],'declared_edges':[edge],'reconciliation':[]}
        papp=copy.deepcopy(self.p['applications'][0]);papp.update(id='P',kind='policy',dependencies=[])
        self.p['applications'].append(papp)
        self.p['applications'].append({'id':c.COVERAGE_ID,'kind':'coverage','authors':['authorA'],
            'dependencies':['A','B','P'],'files':[],'coverage_record':None})
        self.e['authorship']['application:P']=['authorA']
        self.e['authorship']['application:'+c.COVERAGE_ID]=['authorA']
        self.sync()

    def pin(self,side,path):return {'side':side,'path':path,'sha256':g.sha(self.files[side][path][1])}

    def sync(self, receipts=True):
        self.files['head']['coverage/initial.json']=('100644',g.canonical(self.initial))
        if self.dossier['mode']=='substantive':
            self.dossier['initial']=self.pin('head','coverage/initial.json')
        self.files['head']['coverage/dossier.json']=('100644',g.canonical(self.dossier))
        for side in ('base','head'):
            self.p[side],values=t.manifest(self.files[side],side);self.blobs.values.update(values)
        apps={a['id']:a for a in self.p['applications']}
        for a in ('A','B'):
            if a in apps:
                for pin in apps[a]['files']:
                    pin['sha256']=self.pin(pin['side'],pin['path'])['sha256']
        sourcepin=self.pin('head','sources/input.md')
        if sourcepin not in apps['B']['files']:apps['B']['files'].append(sourcepin)
        apps['P']['files']=[self.pin(s,p) for s in ('base','head') for p in (c.PROTOCOL_PATH,'coverage/initial.json','coverage/dossier.json') if p in self.files[s]]
        for o in apps['P']['obligations'].values():o['evidence']=[self.pin('head',c.PROTOCOL_PATH)]
        if c.COVERAGE_ID in apps:
            apps[c.COVERAGE_ID]['files']=[self.pin('head',p) for p in ('coverage/dossier.json','coverage/initial.json','proof.md','sources/input.md')]
            apps[c.COVERAGE_ID]['coverage_record']=self.pin('head','coverage/dossier.json')
        changes=[]
        for path in sorted(set(self.files['base'])|set(self.files['head'])):
            if self.files['base'].get(path)!=self.files['head'].get(path):
                aid='B' if path=='proof.md' else ('A' if path=='sources/input.md' else 'P')
                changes.append({'path':path,'kind':apps[aid]['kind'],'applications':[aid]})
        self.p['changes']=changes
        if receipts:t.refresh(self.p,self.e)

    def run(self, profile=True):return g.check_records(self.p,self.e,self.blobs,self.profile if profile else None)

    def nonmath(self):
        self.files['head']['proof.md']=self.files['base']['proof.md']
        self.profile.update(mode='non_substantive',claim_ids=[],allowed_nonmath_paths=[c.PROTOCOL_PATH,'coverage/initial.json','coverage/dossier.json'])
        self.dossier={k:self.dossier[k] for k in ('schema','profile_sha256','mode','sources','scope')}
        self.dossier.update(profile_sha256=g.digest(self.profile),mode='non_substantive',
            sources=[self.pin('head',p) for p in self.profile['proof_paths']],scope='Only the reviewed policy paths change; proof and source bytes unchanged. No mathematical completion claim.')
        for a in self.p['applications']:
            if a['kind']!='coverage':a['kind']='policy'
        self.sync()

    def resolve_use(self):
        old=self.initial['uses'][0];new=self.dossier['reconciled_uses'][0]
        self.dossier['reconciliation']=[{'id':'use:U','before_sha256':g.digest(old),'after_sha256':g.digest(new),
            'history':[{'status':'resolved','reason':'Reviewed changed supplier contract.','finding_ids':[]}]}]


class CoverageTests(unittest.TestCase):
    def setUp(self):self.c=Case()
    def reject(self,pattern):
        with self.assertRaisesRegex(g.Invalid,pattern):self.c.run()
    def test_complete_bound_fixture(self):
        result=self.c.run();self.assertEqual(result['source_uses'],1);self.assertFalse(result['merge_authorized'])
    def test_legacy_fixture_unchanged(self):
        p,e,b=t.fixture();self.assertEqual(g.check_records(p,e,b)['protocol_coverage'],'legacy-records-only')
    def test_no_profile_cannot_claim_v13(self):
        with self.assertRaisesRegex(g.Invalid,'profile-required'):self.c.run(False)
    def test_unknown_profile_version(self):self.c.profile['protocol_version']='1.4';self.reject('unknown-coverage-profile')
    def test_unknown_protocol_hash(self):self.c.profile['governing_protocol']['sha256']='0'*64;self.reject('unapproved-governing')
    def test_wrong_governing_path(self):self.c.profile['governing_protocol']['path']='missing.md';self.reject('unapproved-governing')
    def test_alternate_governing_path_is_not_supported(self):
        self.c.profile['governing_protocol']['path']='alternate/PROTOCOL.md'
        self.c.files['head']['alternate/PROTOCOL.md']=self.c.files['head'][c.PROTOCOL_PATH]
        self.reject('unapproved-governing')
    def test_unknown_hash_does_not_fall_back_to_legacy(self):
        p,e,b=t.fixture()
        for side in ('base','head'):
            files={path:(v['mode'],b.values[v['sha256']]) for path,v in p[side]['files'].items()}
            files[c.PROTOCOL_PATH]=b'Unknown changed policy\n';p[side],values=t.manifest(files,side);b.values.update(values)
        t.refresh(p,e)
        with self.assertRaisesRegex(g.Invalid,'unknown-governing'):g.check_records(p,e,b)
    def test_v13_document_at_other_path_requires_profile(self):
        p,e,b=t.fixture()
        for side in ('base','head'):
            files={path:(v['mode'],b.values[v['sha256']]) for path,v in p[side]['files'].items()}
            files['alternate/PROTOCOL.md']=(Path(__file__).parent/'PROTOCOL-V1.3.md').read_bytes()
            p[side],values=t.manifest(files,side);b.values.update(values)
        t.refresh(p,e)
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):g.check_records(p,e,b)
    def test_wrong_runtime_policy(self):self.c.profile['runtime_policy_sha256']='0'*64;self.reject('runtime-policy')
    def test_changed_profile_invalidates_dossier(self):self.c.profile['claim_ids']=['A','B'];self.reject('profile-binding')
    def test_protocol_bytes_changed(self):
        self.c.files['head'][c.PROTOCOL_PATH]=('100644',b'Altered v1.3');self.c.sync();self.reject('changed-or-missing-governing')
    def test_no_coverage_application(self):
        self.c.p['applications'].pop();del self.c.e['authorship']['application:'+c.COVERAGE_ID];self.c.sync();self.reject('separate-coverage')
    def test_no_separate_coverage_receipt(self):
        self.c.e['receipts']=[r for r in self.c.e['receipts'] if r['target']!=c.COVERAGE_ID];self.reject('missing-or-extra-acceptance')
    def test_same_agent_new_run_cannot_accept(self):
        self.c.e['runs'][2]['agent_id']='authorB-agent';self.reject('self-acceptance|coverage-author')
    def test_coverage_reviewer_must_be_nonauthor_of_all_apps(self):
        # Other decisions retain a different reviewer; only coverage uses B's author.
        r=next(r for r in self.c.e['receipts'] if r['target']==c.COVERAGE_ID);r['run_id']='authorB'
        self.reject('coverage-author')
    def test_coverage_binds_all_applications(self):
        self.c.p['applications'][-1]['dependencies']=['B'];self.c.sync();self.reject('bind-all-applications')
    def test_stale_coverage_dependency_receipt(self):
        old=copy.deepcopy(next(r for r in self.c.e['receipts'] if r['target']==c.COVERAGE_ID))
        self.c.p['applications'][0]['obligations']['source_hypotheses']['justification']='New supplier contract'
        self.c.sync();self.c.e['receipts']=[old if r['target']==c.COVERAGE_ID else r for r in self.c.e['receipts']]
        self.reject('stale-review-content')
    def test_missing_source(self):self.c.dossier['sources'].pop();self.c.sync();self.reject('proof-source-inventory')
    def test_missing_coverage_passage(self):self.c.dossier['coverage_index'].pop();self.c.sync();self.reject('unindexed-proof-lines')
    def test_awaiting_review_prevents_closure(self):self.c.dossier['coverage_index'][0]['status']='awaiting_review';self.c.sync();self.reject('unreviewed-proof-passage')
    def test_claimed_passage_cannot_be_excluded(self):self.c.dossier['coverage_index'][0]['status']='outside_claimed_proof';self.c.sync();self.reject('claimed-passage')
    def test_no_imports_requires_explicit_statement(self):self.c.dossier['coverage_index'][1]['no_imports_reason']=None;self.c.sync();self.reject('explicit-no-imports')
    def test_missing_outside_reason(self):
        row=self.c.dossier['coverage_index'][1];row.update(claim_ids=[],status='outside_claimed_proof',reason='')
        self.c.sync();self.reject('passage-specific-reason')
    def test_repeated_use_missing_contract(self):
        row=copy.deepcopy(self.c.dossier['coverage_index'][0]);row['id']='B-second';self.c.dossier['coverage_index'].append(row)
        self.c.dossier['reconciled_uses'][0]['passages'].append('B-second');self.c.sync();self.reject('shared-contract')
    def test_repeated_use_omitted_location(self):
        row=copy.deepcopy(self.c.dossier['coverage_index'][0]);row['id']='B-second';self.c.dossier['coverage_index'].append(row)
        self.c.sync();self.reject('incomplete-repeated-use-locations')
    def test_non_dependency_needs_passage_specific_reason(self):
        self.c.dossier['reconciled_uses'][0]['reason']='';self.c.sync();self.reject('use-reason')
    def test_deleted_referenced_use(self):self.c.dossier['reconciled_uses']=[];self.c.sync();self.reject('missing-passage-claim-or-use')
    def test_deleted_direct_edge(self):self.c.p['applications'][1]['dependencies']=[];self.c.sync();self.reject('missing-direct-internal')
    def test_named_section_and_unnamed_uses_each_need_direct_edge(self):
        for prose,required in [('By Theorem 4.2, the bound follows.', 'Theorem 4.2 bound'),
                               ('The construction of Section 3 supplies this estimate.', 'Section 3 comparison estimate'),
                               ('Uniformly in n, the error is O(1/n).', 'Uniform error constant independent of n')]:
            with self.subTest(prose=prose):
                self.c=Case();self.c.files['head']['proof.md']=('100644',(prose+'\n').encode())
                pin=self.c.pin('head','proof.md');self.c.dossier['sources'][0]=copy.deepcopy(pin)
                self.c.initial['sources'][0]=copy.deepcopy(pin)
                self.c.dossier['coverage_index'][0]['location']={'pin':pin,'start_line':1,'end_line':1,'excerpt_sha256':pin['sha256']}
                for use in (self.c.initial['uses'][0],self.c.dossier['reconciled_uses'][0]):
                    use['assertion']['statement']=required;use['reason']=prose
                self.c.sync();self.assertTrue(self.c.run()['records_consistent'])
                self.c.p['applications'][1]['dependencies']=[];self.c.sync();self.reject('missing-direct-internal')
    def test_transitive_edge_does_not_replace_direct(self):
        self.c.p['applications'][2]['dependencies']=['A'];self.c.p['applications'][1]['dependencies']=['P'];self.c.sync();self.reject('missing-direct-internal')
    def test_application_cycle(self):
        self.c.p['applications'][0]['dependencies']=['B']
        # Avoid the fixture's naive recursive receipt generator.
        with self.assertRaisesRegex(g.Invalid,'dependency-cycle'):self.c.run()
    def test_changed_supplier_contract_with_unchanged_consumer(self):
        self.c.files['head']['sources/input.md']=('100644',b'New supplier statement\n');self.c.sync();self.reject('stale-file-pin')
    def test_updated_supplier_pins_do_not_refresh_old_coverage_decision(self):
        old=copy.deepcopy(next(r for r in self.c.e['receipts'] if r['target']==c.COVERAGE_ID))
        self.c.files['head']['sources/input.md']=('100644',b'New supplier statement\n')
        pin=self.c.pin('head','sources/input.md')
        for sources in (self.c.dossier['sources'],self.c.initial['sources']):sources[1]=copy.deepcopy(pin)
        location={'pin':pin,'start_line':1,'end_line':1,'excerpt_sha256':pin['sha256']}
        self.c.dossier['coverage_index'][1]['location']=copy.deepcopy(location)
        for use in (self.c.initial['uses'][0],self.c.dossier['reconciled_uses'][0]):use['supplier']['location']=copy.deepcopy(location)
        self.c.sync()
        current=next(r for r in self.c.e['receipts'] if r['target']==c.COVERAGE_ID)
        # Even forged refresh of envelope/target fields cannot preserve old dependencies.
        current['dependency_sha256']=old['dependency_sha256']
        self.reject('stale-review-content-or-dependencies')
    def test_stale_excerpt(self):self.c.dossier['reconciled_uses'][0]['supplier']['location']['excerpt_sha256']='0'*64;self.c.sync();self.reject('stale-source-excerpt')
    def test_missing_supplier(self):self.c.dossier['reconciled_uses'][0]['supplier']=None;self.c.sync();self.reject('schema:supplier')
    def test_unchecked_genuine_use(self):self.c.dossier['reconciled_uses'][0]['application_id']=None;self.c.sync();self.reject('unchecked-genuine')
    def test_missing_match_parameter(self):del self.c.dossier['reconciled_uses'][0]['assertion']['uniformity'];self.c.sync();self.reject('schema:required-assertion')
    def test_reconstruction_identity_cannot_be_invented(self):self.c.dossier['reconstruction']['run_id']='unknown';self.c.sync();self.reject('reconstruction-reviewer')
    def test_reconstruction_requires_exposure_record(self):self.c.dossier['reconstruction']['prior_exposure']='';self.c.sync();self.reject('reconstruction-attestation')
    def test_initial_freeze_before_comparison(self):self.c.dossier['reconstruction']['frozen_at']='2026-11-07T01:02:00Z';self.c.sync();self.reject('frozen-before')
    def test_initial_sources_stale(self):self.c.initial['sources'][0]['sha256']='0'*64;self.c.sync();self.reject('stale-initial')
    def test_initial_table_must_be_actual_rows(self):self.c.initial['uses']=[{'id':'U'}];self.c.sync();self.reject('initial-source-use')
    def test_unresolved_reconciliation(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.sync();self.reject('unresolved-reconciliation-difference')
    def test_reviewed_reconciliation_preserves_both_versions(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.resolve_use();self.c.sync();self.assertTrue(self.c.run()['records_consistent'])
    def test_stale_reconciliation(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.resolve_use();self.c.dossier['reconciliation'][0]['after_sha256']='0'*64;self.c.sync();self.reject('stale-reconciliation')
    def test_disputed_history_must_enter_findings(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.resolve_use();self.c.dossier['reconciliation'][0]['history'].insert(0,{'status':'disputed','reason':'Substantive doubt','finding_ids':[]});self.c.sync();self.reject('unrecorded-substantive-doubt')
    def test_preserved_dispute_with_finding_and_resolution(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.resolve_use();self.c.dossier['reconciliation'][0]['history'].insert(0,{'status':'disputed','reason':'Substantive doubt','finding_ids':['F1']});self.c.sync();self.assertTrue(self.c.run()['records_consistent'])
    def test_last_disposition_unresolved(self):
        self.c.dossier['reconciled_uses'][0]['reason']='Corrected match';self.c.resolve_use();self.c.dossier['reconciliation'][0]['history'][-1].update(status='disputed',finding_ids=['F1']);self.c.sync();self.reject('unresolved-reconciliation')
    def test_unlisted_extra_graph_edge(self):
        self.c.p['applications'][2]['dependencies']=['A'];self.c.sync();self.reject('incomplete-declared-edge')
    def test_extra_graph_edge_requires_disposition(self):
        self.c.p['applications'][2]['dependencies']=['A'];self.c.dossier['declared_edges'].append({'consumer':'P','supplier':'A','use_ids':[],'reason':'Retained redundant information'});self.c.sync();self.reject('unresolved-reconciliation-difference')
    def test_nonmath_scope_positive(self):self.c.nonmath();self.assertEqual(self.c.run()['protocol_coverage'],'1.3-non-substantive-scope-only')
    def test_nonmath_scope_still_needs_receipt(self):
        self.c.nonmath();self.c.e['receipts']=[r for r in self.c.e['receipts'] if r['target']!=c.COVERAGE_ID];self.reject('missing-or-extra-acceptance')
    def test_nonmath_cannot_include_math_application(self):self.c.nonmath();self.c.p['applications'][0]['kind']='argument';self.c.sync();self.reject('nonmath-substantive')
    def test_nonmath_cannot_change_proof(self):
        self.c.nonmath();self.c.files['head']['proof.md']=('100644',b'New proof\n');self.c.dossier['sources'][0]=self.c.pin('head','proof.md');self.c.sync();self.reject('nonmath-change-outside|nonmath-proof-source-changed')
    def test_nonmath_cannot_expand_allowed_paths_into_proof(self):self.c.nonmath();self.c.profile['allowed_nonmath_paths'].append('proof.md');self.reject('profile-paths')
    def test_unsigned_evidence_still_has_no_authority(self):
        with self.assertRaisesRegex(g.IntegrationMissing,'authentication'):g.validate_offline(self.c.p,blob_reader=self.c.blobs,coverage_profile=self.c.profile)


class AuthenticatedCoverageTests(sb.StoreFixture):
    """Ephemeral keyed fixture ledger; no production receipts or approvals."""
    def setUp(self):
        super().setUp();self.case=Case();case=self.case;selected={};n=0
        for run in case.e['runs']:
            n+=1
            event={'kind':'run_observed','observation':sb.observation(n),'run_id':run['id'],
                   'agent_id':run['agent_id'],'model':run['model'],'tools':run['tools']}
            self.store.append(event,'fixture',self.cp())
        for receipt in case.e['receipts']:
            key=receipt['kind']+':'+receipt['target'];n+=1
            authors=case.e['authorship'][key] if receipt['kind']!='assembly' else ['authorA','authorB']
            event={'kind':'target_frozen','observation':sb.observation(n),'freeze_id':'f-'+key,
                'target_kind':receipt['kind'],'target_id':receipt['target'],'target_sha256':receipt['target_sha256'],
                'dependency_sha256':receipt['dependency_sha256'],'binding':case.e['binding'],'author_runs':authors}
            self.store.append(event,'fixture',self.cp());n+=1;selected[key]='r-'+key
            report={'kind':'report_observed','observation':sb.observation(n),'report_id':'r-'+key,
                'run_id':receipt['run_id'],'freeze_id':'f-'+key,'decision':'accepted','scope':'Synthetic coverage test only.',
                'body_base64':base64.b64encode(case.blobs.values[receipt['report']['sha256']]).decode()}
            self.store.append(report,'fixture',self.cp())
        _,checkpoint,state=self.store.read_verified()
        self.context=bridge.VerifiedContext(case.e['binding'],case.e['policy_paths'],case.e['findings'],selected,checkpoint,g.digest(bridge.inventory(state)))
        context=self.context
        class Verifier:
            def verify_context(self,*args):return context
        self.verifier=Verifier()

    def test_signed_coverage_receipt_with_exact_target(self):
        result=bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile).evaluate(self.case.p,self.case.blobs)
        self.assertEqual(result['protocol_coverage'],'1.3-substantive-records-reviewed')
        self.assertFalse(result['merge_authorized'])

    def test_signed_old_route_still_cannot_omit_profile(self):
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):
            bridge.LedgerEvidenceBridge(self.store,self.verifier).evaluate(self.case.p,self.case.blobs)

    def test_other_acceptance_cannot_substitute_for_coverage(self):
        self.context.selected_reports['application:'+c.COVERAGE_ID]=self.context.selected_reports['application:B']
        with self.assertRaisesRegex(ValueError,'stale or wrong'):
            bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile).evaluate(self.case.p,self.case.blobs)

    def test_signed_assembly_does_not_replace_coverage(self):
        del self.context.selected_reports['application:'+c.COVERAGE_ID]
        with self.assertRaisesRegex(g.Invalid,'incomplete receipt selection'):
            bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile).evaluate(self.case.p,self.case.blobs)

    def test_protected_profile_copied_before_evaluation(self):
        evaluator=bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile)
        self.case.profile['mode']='non_substantive'
        self.assertTrue(evaluator.evaluate(self.case.p,self.case.blobs)['records_consistent'])


if __name__=='__main__':unittest.main(verbosity=2)
