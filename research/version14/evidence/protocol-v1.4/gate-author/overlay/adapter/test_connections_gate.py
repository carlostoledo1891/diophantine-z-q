"""Synthetic relationships and ephemeral ledger keys, never research acceptance."""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch
import coverage_gate as c
import offline_manifest_gate as g
import test_coverage_gate as old
import test_manifest_gate as t
import ledger_evidence_bridge as bridge


class Case14(old.Case):
    def __init__(self):
        super().__init__()
        self.profile.update(schema='protocol-coverage-policy/v2', protocol_version='1.4',
                            connection_record_path='coverage/connections.json')
        self.profile['governing_protocol']['sha256'] = c.PROTOCOL14_SHA256
        self.files['head'][c.PROTOCOL_PATH] = ('100644',(Path(__file__).parent/'PROTOCOL-V1.4.md').read_bytes())
        self.dossier['profile_sha256'] = g.digest(self.profile)
        u = self.dossier['reconciled_uses'][0]
        loc = copy.deepcopy(self.dossier['coverage_index'][0]['location'])
        available = copy.deepcopy(u['assertion']); available['statement'] = u['supplier']['statement']
        connection = {'use_id':'U','use_sha256':g.digest(u),'supplier_passage_role':'statement',
                      'available_assertion':available,'needed_assertion':copy.deepcopy(u['assertion']),
                      'required_capabilities':['uniform-bound','endpoint'], 'available_capabilities':['uniform-bound'],
                      'derived_capabilities':['endpoint'],
                      'connecting_derivation':{'kind':'derivation','location':loc,'application_id':'B','output_assertion':copy.deepcopy(u['assertion'])},
                      'adverse_cases':{'status':'checked','reason':'Synthetic endpoint requires the displayed extension.','evidence':[loc]},
                      'consumer_locations':[loc]}
        correction = {'rejected_assertion':'Endpoint omitted','current_assertion':'Endpoint included',
                      'canonical_location':loc, 'representations':[{'id':'main','location':loc,'status':'current',
                      'recorded_assertion':'Endpoint included','reason':'Current synthetic representation.'}],
                      'scope':'All synthetic copies.','limitations':'This is a test declaration, not a proof.'}
        finding = {'finding_id':'F1','finding_sha256':g.digest(self.p['findings'][0]),
                   'classification':'substantive_failure','mechanism':'Endpoint excluded from initial bound.',
                   'search_scope':[loc],'scope_reason':'The only synthetic invocation.','exclusions':[],
                   'occurrences':[{'id':'O1','use_ids':['U'],'location':loc,'inclusion_reason':'Original occurrence.',
                                   'disposition':'corrected_reviewed','evidence':[loc]}],
                   'correction':correction,'limitations':'Finite synthetic example only.'}
        self.record = {'schema':'protocol-connections/v1','profile_sha256':g.digest(self.profile),
                       'coverage_sources':copy.deepcopy(self.dossier['sources']), 'connections':[connection],
                       'findings':[finding], 'scope':'Synthetic B only.', 'limitations':'Not real research evidence.'}
        self.sync14()

    def reports(self):
        def decision(subject, value):
            return {'subject':subject,'subject_sha256':g.digest(value),'outcome':'accepted_within_scope',
                    'review_basis':'reconstructed','prior_review':None,'scope':'Exact synthetic comparison only.',
                    'limitations':'Does not prove a mathematical assertion.'}
        self.cover_report = {'schema':'protocol14-review/v1','scope':'Synthetic coverage and connections.',
                             'limitations':'Synthetic fixture.', 'decisions':
                             [decision('connection:'+v['use_id'],v) for v in self.record['connections']] +
                             [decision('finding:'+v['finding_id'],v) for v in self.record['findings']] +
                             [decision('inventory',self.record)]}
        self.assembly_report = {'schema':'protocol14-review/v1','scope':'Synthetic final composition.',
                                'limitations':'Synthetic fixture.','decisions':[decision('assembly',self.record)]}

    def sync14(self, reports=True, receipts=True, include_record=True):
        self.files['head']['coverage/connections.json'] = ('100644',g.canonical(self.record))
        if include_record:
            self.dossier['protocol14_record'] = self.pin('head','coverage/connections.json')
        else:
            self.dossier.pop('protocol14_record',None)
        if reports:
            self.reports()
        self.files['head']['reviews/coverage14.json'] = ('100644',g.canonical(self.cover_report))
        self.files['head']['reviews/assembly14.json'] = ('100644',g.canonical(self.assembly_report))
        super().sync(receipts=False)
        apps = {a['id']:a for a in self.p['applications']}
        apps[c.COVERAGE_ID]['files'].append(self.pin('head','coverage/connections.json'))
        for path in ('coverage/connections.json','reviews/coverage14.json','reviews/assembly14.json'):
            apps['P']['files'].append(self.pin('head',path))
        if receipts:
            t.refresh(self.p,self.e)
            for r in self.e['receipts']:
                if (r['kind'],r['target']) == ('application',c.COVERAGE_ID):
                    r['report'] = self.pin('head','reviews/coverage14.json')
                elif r['kind'] == 'assembly':
                    r['report'] = self.pin('head','reviews/assembly14.json')


class ConnectionTests(unittest.TestCase):
    def setUp(self): self.c = Case14()
    def reject(self, code):
        with self.assertRaisesRegex(g.Invalid,code): self.c.run()
    def test_positive_exact_record(self):
        out=self.c.run(); self.assertEqual(out['protocol_coverage'],'1.4-substantive-records-reviewed')
        self.assertFalse(out['merge_authorized']); self.assertIn('Does not establish',out['protocol14_limitation'])
    def test_no_profile(self):
        with self.assertRaisesRegex(g.Invalid,'profile-required'):self.c.run(False)
    def test_downgrade(self):
        self.c.profile.update(schema='protocol-coverage-policy/v1',protocol_version='1.3')
        del self.c.profile['connection_record_path'];self.reject('unapproved-governing')
    def test_missing_record(self):
        self.c.sync14(include_record=False);self.reject('schema:coverage-record')
    def test_unbound_record(self):
        self.c.p['applications'][-1]['files'].pop();t.refresh(self.c.p,self.c.e);self.reject('unbound-connection-record')
    def test_missing_required_connection(self):
        self.c.record['connections']=[];self.c.sync14();self.reject('missing-or-extra-required-connection')
    def test_missing_derivation(self):
        self.c.record['connections'][0]['connecting_derivation']=None;self.c.sync14();self.reject('schema:connecting-derivation')
    def test_weaker_capabilities_with_favorable_reports(self):
        self.c.record['connections'][0]['derived_capabilities']=[];self.c.sync14();self.reject('weaker-recorded-supplier')
    def test_output_weaker_than_required(self):
        self.c.record['connections'][0]['connecting_derivation']['output_assertion']['uniformity']='Pointwise only'
        self.c.sync14();self.reject('connection-output-too-weak')
    def test_plausible_prose_is_not_identification(self):
        self.c.record['connections'][0]['connecting_derivation']['kind']='identification'
        self.c.sync14();self.reject('nonidentical-contract-needs-derivation')
    def test_reviewer_verdict_is_not_supplier(self):
        self.c.record['connections'][0]['supplier_passage_role']='review';self.c.sync14();self.reject('supplier-passage-is-not-evidence')
    def test_missing_consumer(self):
        self.c.record['connections'][0]['consumer_locations']=[];self.c.sync14();self.reject('incomplete-connection-consumers')
    def test_stale_exact_excerpt(self):
        self.c.record['connections'][0]['connecting_derivation']['location']=copy.deepcopy(self.c.record['connections'][0]['consumer_locations'][0])
        self.c.record['connections'][0]['connecting_derivation']['location']['excerpt_sha256']='0'*64
        self.c.sync14();self.reject('stale-connection-excerpt')
    def test_unclassified_finding(self):
        self.c.record['findings']=[];self.c.sync14();self.reject('unclassified-or-extra-finding')
    def test_unknown_failure_type(self):
        self.c.record['findings'][0]['classification']='';self.c.sync14();self.reject('unclassified-failure')
    def test_related_occurrence_open(self):
        self.c.record['findings'][0]['occurrences'][0]['disposition']='open';self.c.sync14();self.reject('unresolved-required-related-occurrence')
    def test_no_related_occurrences(self):
        self.c.record['findings'][0]['occurrences']=[];self.c.sync14();self.reject('missing-related-failure-occurrences')
    def test_missing_consistency(self):
        self.c.record['findings'][0]['correction']=None;self.c.sync14();self.reject('missing-current-representation-check')
    def test_stale_rejected_assertion_in_current_copy(self):
        self.c.record['findings'][0]['correction']['representations'][0]['recorded_assertion']='Endpoint omitted'
        self.c.sync14();self.reject('stale-current-representation')
    def test_retired_canonical_is_not_current(self):
        self.c.record['findings'][0]['correction']['representations'][0]['status']='retired'
        self.c.sync14();self.reject('canonical-current-representation-missing')
    def test_forged_author_acceptance_field(self):
        self.c.record['connections'][0]['accepted']=True;self.c.sync14();self.reject('schema:connection')
    def test_stale_explicit_review_despite_fresh_envelope(self):
        self.c.record['connections'][0]['adverse_cases']['reason']='Changed scope'
        self.c.sync14(reports=False);self.reject('stale-protocol14-acceptance')
    def test_missing_explicit_acceptance(self):
        self.c.cover_report['decisions'].pop(0);self.c.sync14(reports=False);self.reject('missing-or-extra-protocol14-acceptance')
    def test_consistency_cannot_accept_derivation(self):
        self.c.cover_report['decisions'][0]['review_basis']='consistency_only'
        self.c.sync14(reports=False);self.reject('consistency-cannot-accept-connection')
    def test_prior_review_must_be_exact_pin(self):
        self.c.cover_report['decisions'][0].update(review_basis='reused_exact_derivation',prior_review={'path':'reviews/report.md'})
        self.c.sync14(reports=False);self.reject('schema:file-pin')
    def test_prior_review_changed_hash(self):
        p=self.c.pin('head','reviews/report.md');p['sha256']='0'*64
        self.c.cover_report['decisions'][0].update(review_basis='reused_exact_derivation',prior_review=p)
        self.c.sync14(reports=False);self.reject('stale-file-pin')
    def test_exact_prior_review_reuse(self):
        self.c.cover_report['decisions'][0].update(review_basis='reused_exact_derivation',prior_review=self.c.pin('head','reviews/report.md'))
        self.c.sync14(reports=False);self.assertTrue(self.c.run()['records_consistent'])
    def test_self_approval_still_rejected(self):
        r=next(r for r in self.c.e['receipts'] if r['target']==c.COVERAGE_ID);r['run_id']='authorA'
        self.reject('self-acceptance')
    def test_stale_envelope_not_refreshed(self):
        self.c.record['scope']='Changed scope';self.c.sync14(receipts=False);self.reject('stale-or-wrong-candidate-binding')
    def test_nonmath_scope_does_not_certify_math(self):
        self.c.nonmath()
        self.c.profile['allowed_nonmath_paths'] += ['coverage/connections.json','reviews/coverage14.json','reviews/assembly14.json']
        self.c.dossier['profile_sha256']=g.digest(self.c.profile)
        self.c.record.update(profile_sha256=g.digest(self.c.profile),coverage_sources=copy.deepcopy(self.c.dossier['sources']),connections=[])
        raw=self.c.files['head']['proof.md'][1]
        loc={'pin':self.c.pin('head','proof.md'),'start_line':1,'end_line':len(raw.splitlines()),'excerpt_sha256':g.sha(raw)}
        f=self.c.record['findings'][0]
        f.update(classification='not_substantive_failure',search_scope=[loc],occurrences=[])
        f['correction']['canonical_location']=loc
        f['correction']['representations'][0]['location']=loc
        self.c.sync14()
        self.assertEqual(self.c.run()['protocol_coverage'],'1.4-non-substantive-scope-only')
        f['classification']='substantive_failure';self.c.sync14();self.reject('missing-related-failure-occurrences')


class Authenticated14Tests(old.AuthenticatedCoverageTests):
    def setUp(self):
        with patch.object(old,'Case',Case14):super().setUp()
    def test_signed_coverage_receipt_with_exact_target(self):
        result=bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile).evaluate(self.case.p,self.case.blobs)
        self.assertEqual(result['protocol_coverage'],'1.4-substantive-records-reviewed')
        self.assertFalse(result['merge_authorized'])
    def test_forged_favorable_report_not_in_authenticated_ledger(self):
        self.case.cover_report['decisions'][0]['scope']='Forged new favorable scope'
        self.case.sync14(reports=False)
        with self.assertRaises((g.Invalid,ValueError)):
            bridge.LedgerEvidenceBridge(self.store,self.verifier,self.case.profile).evaluate(self.case.p,self.case.blobs)


if __name__ == '__main__': unittest.main(verbosity=2)
