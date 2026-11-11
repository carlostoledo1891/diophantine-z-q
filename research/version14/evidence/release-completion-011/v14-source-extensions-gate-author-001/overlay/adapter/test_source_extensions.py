"""Synthetic extension records, not scientific or chronology attestations."""
import copy
import unittest
import coverage_gate as c
import offline_manifest_gate as g
import test_manifest_gate as t
from test_connections_gate import Case14
from test_coverage_gate import Case

class ExtensionCase(Case14):
    def __init__(self):
        super().__init__()
        self.files['head']['added.md'] = ('100644', b'Added proof observation.\n')
        p = self.pin('head', 'added.md')
        loc = dict(pin=p, start_line=1, end_line=1, excerpt_sha256=p['sha256'])
        u = copy.deepcopy(self.initial['uses'][0])
        u.update(id='S1', passages=['S-proof'], classification='background', supplier=None,
                 application_id=None, inline_argument=None, reason='Source-derived supplemental observation.')
        self.sub = dict(schema='protocol-source-first/v1', sources=[p], uses=[u])
        self.passages = [dict(id='S-proof', location=loc, use_ids=['S1'], reason='Full added file.')]
        self.ext = dict(schema='protocol-source-extension/v1', original_initial=copy.deepcopy(self.dossier['initial']),
                        sources=[p], initial=None, initial_passages=None,
                        reconstruction=dict(run_id='reviewer', method='Fresh proof-derived rereading.',
                        prior_exposure='Substantial earlier familiarity; not blind.', limitations='Synthetic fixture.',
                        frozen_at='2026-11-07T02:00:00Z', compared_at='2026-11-07T02:01:00Z'))
        self.dossier['source_extensions'] = [self.ext]
        self.dossier['sources'].append(p)
        self.profile['proof_paths'].append('added.md')
        self.dossier['profile_sha256'] = g.digest(self.profile)
        self.record['profile_sha256'] = g.digest(self.profile)
        self.record['coverage_sources'] = copy.deepcopy(self.dossier['sources'])
        self.dossier['reconciled_uses'].append(copy.deepcopy(u))
        self.dossier['coverage_index'].append(dict(id='S-proof', claim_ids=['B'], location=loc,
            status='reviewed', reason='Full added proof.', use_ids=['S1'], no_imports_reason='Background only.'))
        self.sync_ext()

    def sync_ext(self):
        for path, value in [('coverage/sub.json', self.sub), ('coverage/sub-passages.json', self.passages)]:
            self.files['head'][path] = ('100644', g.canonical(value))
        self.ext['initial'] = self.pin('head', 'coverage/sub.json')
        self.ext['initial_passages'] = self.pin('head', 'coverage/sub-passages.json')
        self.sync14(receipts=False)
        apps = {a['id']:a for a in self.p['applications']}
        for path in ('added.md','coverage/sub.json','coverage/sub-passages.json'):
            apps['P']['files'].append(self.pin('head',path))
            apps[c.COVERAGE_ID]['files'].append(self.pin('head',path))
        t.refresh(self.p,self.e)
        for r in self.e['receipts']:
            if (r['kind'],r['target']) == ('application',c.COVERAGE_ID): r['report']=self.pin('head','reviews/coverage14.json')
            elif r['kind']=='assembly': r['report']=self.pin('head','reviews/assembly14.json')

class ExtensionTests(unittest.TestCase):
    def setUp(self): self.x=ExtensionCase()
    def reject(self, pattern):
        self.x.sync_ext()
        with self.assertRaisesRegex(g.Invalid,pattern): self.x.run()
    def test_append(self): self.assertEqual(self.x.run()['source_uses'],2)
    def test_original_path(self): self.assertEqual(Case14().run()['source_uses'],1)
    def test_missing_extension(self): self.x.dossier['source_extensions']=[];self.reject('empty-source-extensions')
    def test_duplicate_source(self): self.x.ext['sources'].append(self.x.ext['sources'][0]);self.reject('extension-source-paths')
    def test_overlap_original(self): self.x.ext['sources']=[self.x.initial['sources'][0]];self.reject('overlapping-source-extension')
    def test_changed_source(self): self.x.ext['sources'][0]['sha256']='0'*64;self.reject('stale-file-pin')
    def test_stale_original_pin(self): self.x.ext['original_initial']['sha256']='0'*64;self.reject('source-extension-original-initial')
    def test_stale_original_source(self): self.x.initial['sources'][0]['sha256']='0'*64;self.x.ext['original_initial']=self.x.pin('head','coverage/initial.json');self.reject('source-extension-original-initial|source-extension-union-mismatch')
    def test_stale_sub_sources(self): self.x.sub['sources']=[];self.reject('stale-supplemental-sources')
    def test_duplicate_use(self): self.x.sub['uses'][0]['id']='U';self.reject('duplicate-supplemental-use')
    def test_missing_sub_use(self): self.x.sub['uses']=[];self.reject('supplemental-passage-uses')
    def test_displaced_use(self): self.x.sub['uses'][0]['passages']=['B-proof'];self.reject('supplemental-missing-use-passage')
    def test_unlinked_use(self): self.x.passages[0]['use_ids']=[];self.reject('supplemental-displaced-use')
    def test_initial_line_omission(self): self.x.passages=[];self.reject('supplemental-unindexed-lines')
    def test_final_line_omission(self): self.x.dossier['coverage_index'].pop();self.reject('unindexed-proof-lines')
    def test_false_chronology(self): self.x.ext['reconstruction']['frozen_at']='2026-11-07T02:01:00Z';self.reject('supplemental-reconstruction-chronology')
    def test_pre_original_chronology(self): self.x.ext['reconstruction']['frozen_at']='2026-11-07T00:59:00Z';self.reject('supplemental-reconstruction-chronology')
    def test_missing_exposure(self): self.x.ext['reconstruction']['prior_exposure']='';self.reject('incomplete-supplemental-attestation')
    def test_unknown_reviewer(self): self.x.ext['reconstruction']['run_id']='unknown';self.reject('reconstruction-reviewer-mismatch')
    def test_author_reviewer(self): self.x.ext['reconstruction']['run_id']='authorA';self.reject('reconstruction-reviewer-mismatch')
    def test_author_continuation(self):
        self.x.ext['reconstruction'].update(run_id='authorA',continuation=dict(schema='protocol-review-continuation/v1',run_ids=['authorA','reviewer'],initial=self.x.ext['initial'],sources_sha256=g.digest(self.x.ext['sources']),attestation='Claimed chain.'))
        self.reject('reconstruction-reviewer-mismatch')
    def test_drop_final_use_without_reconciliation(self):
        self.x.dossier['reconciled_uses'].pop();self.x.dossier['coverage_index'][-1]['use_ids']=[]
        self.reject('unresolved-reconciliation-difference')
    def test_resolved_removed_use(self):
        u=self.x.dossier['reconciled_uses'].pop();self.x.dossier['coverage_index'][-1]['use_ids']=[]
        self.x.dossier['reconciliation'].append(dict(id='use:S1',before_sha256=g.digest(u),after_sha256=None,history=[dict(status='resolved',reason='Independent comparison found this background observation redundant.',finding_ids=[])]))
        self.x.sync_ext();self.assertTrue(self.x.run()['records_consistent'])
    def test_v13_forbidden(self):
        x=Case();x.dossier['source_extensions']=[];x.sync()
        with self.assertRaisesRegex(g.Invalid,'source-extensions-require'):x.run()
    def test_nonmath_forbidden(self):
        x=Case();x.nonmath();x.dossier['source_extensions']=[];x.sync()
        with self.assertRaisesRegex(g.Invalid,'source-extensions-require'):x.run()


    def test_original_bytes_substituted_in_final_union(self):
        self.x.files['head']['proof.md']=('100644',b'Replacement proof.\n')
        self.x.dossier['sources'][0]=self.x.pin('head','proof.md')
        self.reject('source-extension-union-mismatch')
    def test_original_continuation_keeps_original_sources(self):
        reviewer=next(r for r in self.x.e['runs'] if r['id']=='reviewer')
        self.x.e['runs'].append(dict(copy.deepcopy(reviewer),id='old-run'))
        self.x.dossier['reconstruction'].update(run_id='old-run',continuation=dict(
            schema='protocol-review-continuation/v1',run_ids=['old-run','reviewer'],
            initial=copy.deepcopy(self.x.dossier['initial']),sources_sha256=g.digest(self.x.initial['sources']),
            attestation='Original frozen scope remains exactly preserved.'))
        self.x.sync_ext();self.assertTrue(self.x.run()['records_consistent'])
    def test_original_continuation_cannot_claim_final_sources(self):
        self.test_original_continuation_keeps_original_sources()
        self.x.dossier['reconstruction']['continuation']['sources_sha256']=g.digest(self.x.dossier['sources'])
        self.reject('reconstruction-continuation-sources')


    def test_missing_final_added_source(self):
        self.x.dossier['sources'].pop();self.reject('incomplete-proof-source-inventory')
    def test_reordered_final_union(self):
        self.x.dossier['sources'].reverse();self.reject('source-extension-union-mismatch')
    def test_supplement_wrong_source_passage(self):
        self.x.passages[0]['location']=copy.deepcopy(self.x.dossier['coverage_index'][0]['location'])
        self.reject('supplemental-passage-source')

from test_review_continuity import AuthenticatedContinuityTests
class AuthenticatedExtensionTests(AuthenticatedContinuityTests):
    def setUp(self):
        super().setUp()
        self.c=ExtensionCase()
        reviewer=next(r for r in self.c.e['runs'] if r['id']=='reviewer')
        self.c.e['runs'].append(dict(copy.deepcopy(reviewer),id='initial-run'))
        self.c.ext['reconstruction'].update(run_id='initial-run',continuation=dict(
            schema='protocol-review-continuation/v1',run_ids=['initial-run','reviewer'],
            initial=copy.deepcopy(self.c.ext['initial']),sources_sha256=g.digest(self.c.ext['sources']),
            attestation='Same authenticated agent adopts the independently frozen supplement.'))
        self.c.sync_ext()
    def test_signed_receipt_does_not_fix_bad_chronology(self):
        self.c.ext['reconstruction']['frozen_at']='2026-11-07T02:02:00Z';self.c.sync_ext()
        with self.assertRaisesRegex(g.Invalid,'supplemental-reconstruction-chronology'):self.seed().evaluate(self.c.p,self.c.blobs)
    def test_authenticated_author_agent_rejected(self):
        with self.assertRaisesRegex(g.Invalid,'reviewer-mismatch'):
            self.seed(initial_agent='authorA-agent').evaluate(self.c.p,self.c.blobs)

if __name__=='__main__': unittest.main()
