"""Fixture-only intake integration and authenticated transport tests."""
import base64
import copy
import hashlib
import shutil
import unittest
from unittest.mock import patch
import audit_intake as a
from audit_intake_store import AuditStore
from durable_intake import IntakeRecorder,AuditObservationSource
from protected_ledger_store import ProtectedPath,SQLiteAnchor,Conflict,RecoveryRequired,connect
from test_store_bridge import StoreFixture,run
import test_operator_ledger as opfixtures
import test_github_read_context as githubfixtures
import github_read_context as g
import manifest_transport as t
import probe_github_payloads as probe

def b64(value):return base64.b64encode(value).decode()
OBS=b64(b'SYNTHETIC trusted operator classification, not an actual review')

class IntakeFixture(StoreFixture):
    def setUp(self):
        super().setUp()
        self.p,self.policy,self.transport=githubfixtures.fixture();self.p['findings']=[]
        self.reader=g.ReadContext(self.policy,self.transport)
        self.audit_location=ProtectedPath(self.root/'ledger/intake.sqlite',(self.root/'candidate',))
        self.audit_anchor_location=ProtectedPath(self.root/'external-anchor/intake.sqlite',(self.root/'candidate',))
        self.audit=AuditStore(self.audit_location,SQLiteAnchor(self.audit_anchor_location),'fixture-intake',self.keys)
        self.audit.initialize();self.collector_sha='e'*64;self.collector_key=b'\xab'*32
        self.recorder=IntakeRecorder(self.audit,self.store,self.reader,self.collector_sha,{'collector':self.collector_key})
        self.envelopes={}
        for side in ('base','head'):
            m=self.p[side];binding={'repository_id':1,'commit':m['commit'],'tree':m['tree'],'collector_sha256':self.collector_sha}
            self.envelopes[side]=t.seal(m,binding,'collector',self.collector_key)
        self.serial=0
    def state(self):return self.audit.read_verified()[2]
    def add(self,event):return self.audit.append(event,'fixture',self.audit.anchor.read())
    def capture(self):
        self.serial+=1
        return self.recorder.capture(self.p,self.envelopes,'capture'+str(self.serial),'fixture',self.audit.anchor.read())
    def classify(self,mapping=None):
        state=self.state();which='1/7';context=a.context_digest(state,which)
        for mid in state['materials'][which]:
            self.add({'kind':'classified','scope':which,'context_sha256':context,'material_id':mid,
                      'finding_ids':(mapping or {}).get(mid,[]),'reason':'Synthetic inspected source classification',
                      'observation_base64':OBS})
    def register(self,fid='F',mids=None,body=b'Synthetic issue'):
        mids=mids or list(self.state()['materials']['1/7'])[:1]
        self.add({'kind':'finding_registered','scope':'1/7','finding_id':fid,'body_base64':b64(body),
                  'material_ids':mids,'observation_base64':OBS})
        return mids
    def finding(self,fid='F',body=b'Synthetic issue'):
        return {'id':fid,'body_sha256':hashlib.sha256(body).hexdigest(),'status':'repaired',
                'reason':'Synthetic explanation','authors':['author'],'applications':['A'],'duplicate_of':None}

class IntakeTests(IntakeFixture):
    def test_capture_and_reconcile_no_findings(self):
        self.capture();self.classify();r=self.recorder.reconcile(self.p)
        self.assertTrue(r['intake_consistent']);self.assertFalse(r['merge_authorized']);self.assertFalse(r['fresh_github_state_checked'])
        self.assertEqual(r['material_count'],3)
    def test_intake_archive_does_not_require_green_ci(self):
        self.transport.routes[githubfixtures.ROOT+'/actions/runs/20'][0]['conclusion']='failure'
        self.recorder.github_reader=AuditObservationSource(self.reader)
        self.capture();self.classify();r=self.recorder.reconcile(self.p)
        self.assertTrue(r['intake_consistent'])
        event=next(iter(self.state()['captures'].values()))
        self.assertFalse(event['observation']['ci_evaluated'])
        self.assertFalse(any('/actions/' in p for p in self.transport.calls))
    def test_intake_archive_origin_mismatch(self):
        self.recorder.github_reader=AuditObservationSource(self.reader)
        self.transport.routes[githubfixtures.ROOT+'/git/ref/heads/main'][0]['object']['sha']='1'*40
        with self.assertRaises(g.core.Invalid):self.capture()
        self.assertEqual(self.state()['captures'],{})
    def test_missing_capture(self):
        with self.assertRaisesRegex(a.Invalid,'missing captured'):self.recorder.reconcile(self.p)
    def test_every_material_requires_classification(self):
        self.capture()
        with self.assertRaisesRegex(a.Invalid,'unclassified'):self.recorder.reconcile(self.p)
    def test_unsigned_manifest_raw_digest_tamper(self):
        self.p['head']['files']['paper.md']['sha256']='0'*64
        with self.assertRaisesRegex(t.Invalid,'changed manifest'):self.capture()
        self.assertEqual(self.audit.read_verified()[0],[])
    def test_missing_collector_signature(self):
        self.envelopes['head'].pop('signature')
        with self.assertRaises(t.Invalid):self.capture()
    def test_wrong_collector_code(self):
        self.recorder.collector_sha256='d'*64
        with self.assertRaisesRegex(t.Invalid,'binding'):self.capture()
    def test_revoked_collector_key_blocks_reconciliation(self):
        self.capture();self.classify();self.recorder.collector_keys={}
        with self.assertRaisesRegex(t.Invalid,'unknown transport'):self.recorder.reconcile(self.p)
    def test_modified_comment_retains_both_bodies(self):
        self.capture();path=githubfixtures.ROOT+'/issues/7/comments?per_page=100&page=1'
        self.transport.routes[path][0][0]['body']='Revised objection';self.capture()
        records=self.state()['materials']['1/7'];bodies=[v['record']['body'] for v in records.values()]
        self.assertIn('Original audit text',bodies);self.assertIn('Revised objection',bodies);self.assertEqual(len(records),4)
    def test_deleted_comment_stays_and_requires_reclassification_context(self):
        self.capture();self.classify();path=githubfixtures.ROOT+'/issues/7/comments?per_page=100&page=1'
        self.transport.routes[path]=([],{});self.capture()
        self.assertEqual(len(self.state()['materials']['1/7']),3)
        # Same full history/packet/operator context remains classified.
        self.assertEqual(self.recorder.reconcile(self.p)['material_count'],3)
    def test_new_comment_invalidates_previous_classifications(self):
        self.capture();self.classify();path=githubfixtures.ROOT+'/issues/7/comments?per_page=100&page=1'
        self.transport.routes[path][0].append({'id':101,'body':'New objection'});self.capture()
        with self.assertRaisesRegex(a.Invalid,'unclassified'):self.recorder.reconcile(self.p)
    def test_operator_checkpoint_change_requires_recapture(self):
        self.capture();self.classify();self.store.append(run(900),'fixture',self.cp())
        with self.assertRaisesRegex(a.Invalid,'operator ledger changed'):self.recorder.reconcile(self.p)
    def test_all_operator_reports_including_rejections_retained(self):
        for e in (opfixtures.run_event('author-run','author-agent',1),opfixtures.run_event('review-run','review-agent',2),opfixtures.freeze_event()):
            self.store.append(e,'fixture',self.cp())
        e=opfixtures.report_event();e['decision']='rejected';self.store.append(e,'fixture',self.cp())
        self.capture();materials=self.state()['materials']['1/7']
        reports=[m for m in materials.values() if m['source']=='operator_ledger']
        self.assertEqual(len(reports),1);self.assertEqual(reports[0]['record']['report']['decision'],'rejected')
    def test_registered_finding_exact_disposition(self):
        self.p['findings']=[self.finding()];self.capture();mids=self.register();self.classify({mids[0]:['F']})
        r=self.recorder.reconcile(self.p);self.assertEqual(r['findings'][0]['id'],'F')
    def test_registered_finding_cannot_be_dropped(self):
        self.capture();mids=self.register();self.classify({mids[0]:['F']})
        with self.assertRaisesRegex(a.Invalid,'missing or extra'):self.recorder.reconcile(self.p)
    def test_open_finding_rejected(self):
        self.p['findings']=[self.finding()];self.p['findings'][0]['status']='open';self.capture();mids=self.register();self.classify({mids[0]:['F']})
        with self.assertRaisesRegex(a.Invalid,'lacks disposition'):self.recorder.reconcile(self.p)
    def test_wrong_finding_body_rejected(self):
        self.p['findings']=[self.finding(body=b'Changed')];self.capture();mids=self.register();self.classify({mids[0]:['F']})
        with self.assertRaisesRegex(a.Invalid,'body changed'):self.recorder.reconcile(self.p)
    def test_finding_registration_cannot_replace_original(self):
        self.capture();self.register()
        with self.assertRaisesRegex(a.Invalid,'cannot be replaced'):self.register(body=b'Rewritten')
    def test_finding_needs_registered_source(self):
        self.capture()
        with self.assertRaisesRegex(a.Invalid,'unknown finding source'):self.register(mids=['fake'])
    def test_cannot_classify_known_finding_as_no_finding_everywhere(self):
        self.capture();self.register();self.classify()
        with self.assertRaisesRegex(a.Invalid,'omitted from material'):self.recorder.reconcile(self.p)
    def test_classification_cannot_move_finding_to_other_source(self):
        self.capture();mids=self.register();other=next(x for x in self.state()['materials']['1/7'] if x not in mids)
        with self.assertRaisesRegex(a.Invalid,'not linked'):self.classify({other:['F']})
    def test_no_finding_requires_explicit_reason(self):
        self.capture();s=self.state();mid=next(iter(s['materials']['1/7']))
        with self.assertRaisesRegex(a.Invalid,'requires reason'):
            self.add({'kind':'classified','scope':'1/7','context_sha256':a.context_digest(s,'1/7'),
                      'material_id':mid,'finding_ids':[],'reason':'','observation_base64':OBS})
    def test_stale_classification_rejected(self):
        self.capture();s=self.state();mid=next(iter(s['materials']['1/7']))
        with self.assertRaisesRegex(a.Invalid,'stale context'):
            self.add({'kind':'classified','scope':'1/7','context_sha256':'f'*64,
                      'material_id':mid,'finding_ids':[],'reason':'Synthetic','observation_base64':OBS})
    def test_external_registration_preserved_and_invalidates_context(self):
        self.capture();self.classify()
        self.add({'kind':'external_registered','scope':'1/7','source_id':'external-audit-session',
                  'body_base64':b64(b'External objection'),'observation_base64':OBS})
        with self.assertRaisesRegex(a.Invalid,'unclassified'):self.recorder.reconcile(self.p)
        self.classify();self.assertEqual(self.recorder.reconcile(self.p)['material_count'],4)
    def test_packet_content_change_not_just_binding_invalidates(self):
        self.capture();self.classify();self.p['applications'][0]['description']='New contents'
        with self.assertRaisesRegex(a.Invalid,'candidate changed'):self.recorder.reconcile(self.p)
    def test_repeated_capture_id_rejected(self):
        self.capture();self.serial=0
        with self.assertRaisesRegex(a.Invalid,'repeated'):self.capture()
    def test_unsigned_flag_not_imported(self):
        with self.assertRaisesRegex(a.Invalid,'unknown intake'):
            self.add({'kind':'verified','verified':True})
    def test_verify_context_unimplemented(self):
        with self.assertRaises(g.core.IntegrationMissing):self.recorder.verify_context(self.p,{}, {})
    def test_capture_operator_race_keeps_failed_capture_stale(self):
        original=self.store.assert_current;calls=0
        def check(cp):
            nonlocal calls
            calls+=1
            if calls==2:self.store.append(run(901),'fixture',self.cp())
            return original(cp)
        with patch.object(self.store,'assert_current',side_effect=check),self.assertRaises(Conflict):self.capture()
        self.assertEqual(len(self.state()['captures']),1)
    def test_reconcile_audit_race_rejected(self):
        self.capture();self.classify();original=self.audit.assert_current
        def check(cp):
            self.add({'kind':'external_registered','scope':'1/7','source_id':'late','body_base64':b64(b'Late'),'observation_base64':OBS})
            return original(cp)
        with patch.object(self.audit,'assert_current',side_effect=check),self.assertRaises(Conflict):self.recorder.reconcile(self.p)

class StorageTests(IntakeFixture):
    def test_domain_separation_from_operator_ledger(self):
        self.assertNotEqual(a.genesis('same'),opfixtures.l.genesis('same'))
    def test_reopen_verifies(self):
        self.capture();self.classify();other=AuditStore(self.audit_location,SQLiteAnchor(self.audit_anchor_location),'fixture-intake',self.keys)
        self.assertEqual(len(other.read_verified()[2]['materials']['1/7']),3)
    def test_stale_cas_rejected(self):
        before=self.audit.anchor.read();self.capture()
        with self.assertRaises(Conflict):self.audit.append({},'fixture',before)
    def test_anchor_exception_preserves_recovery_checkpoint(self):
        old=self.audit.anchor.read()
        with patch.object(self.audit.anchor,'compare_and_swap',side_effect=OSError('fixture')):
            with self.assertRaises(RecoveryRequired) as err:self.capture()
        new=err.exception.pending_checkpoint;self.assertIsNotNone(new)
        with self.assertRaises(RecoveryRequired):self.audit.read_verified()
        self.audit.recover_forward(old,new);self.assertEqual(self.audit.read_verified()[1],new)
    def test_intake_rollback_detected(self):
        saved=self.root/'old-intake.sqlite';shutil.copyfile(self.audit_location.path,saved)
        self.capture();shutil.copyfile(saved,self.audit_location.path)
        with self.assertRaises(RecoveryRequired):self.audit.read_verified()
    def test_mac_tamper_rejected(self):
        self.capture();entries,cp,_=self.audit.read_verified();entries[0]['event']['capture_id']='fake'
        with self.assertRaisesRegex(a.Invalid,'authentication'):a.verify(entries,self.keys,cp)
    def test_event_size_cap(self):
        with patch.object(a,'MAX_EVENT',100),self.assertRaisesRegex(a.Invalid,'byte limit'):self.capture()
    def test_database_size_cap(self):
        self.capture()
        with patch.object(a,'MAX_EVENT',100),self.assertRaisesRegex(a.Invalid,'database byte'):self.audit.read_verified()
    def test_no_fixture_key_material_stored(self):
        self.capture();raw=self.audit_location.path.read_bytes()
        self.assertFalse(self.collector_key in raw,'fixture collector key persisted')
        self.assertFalse(self.keys['fixture']['secret'] in raw,'fixture operator key persisted')

class ProbeTests(unittest.TestCase):
    def test_rejects_unapproved_repository_before_request(self):
        with self.assertRaises(g.core.Invalid):probe.probe(None,'evil/repo')
    def test_rejects_arbitrary_event(self):
        with self.assertRaises(g.core.Invalid):probe.probe(None,probe.REPOSITORIES[0],'workflow_dispatch')
    def test_bounded_probe_success(self):
        _,_,old=githubfixtures.fixture();root='/repos/'+probe.REPOSITORIES[0]
        routes={k.replace(githubfixtures.ROOT,root):v for k,v in old.routes.items()}
        routes[root][0]['full_name']=probe.REPOSITORIES[0]
        routes[root+'/actions/runs?per_page=1&page=1&event=pull_request']=({'workflow_runs':[{'id':20}]},{})
        transport=githubfixtures.Transport(routes);result=probe.probe(transport,probe.REPOSITORIES[0],'pull_request')
        self.assertEqual(len(transport.calls),5);self.assertFalse(result['complete_ci_evaluation'])
        self.assertTrue(result['jobs'][0]['run_attempt_present']);self.assertFalse(result['portable_authenticated_receipt'])

if __name__=='__main__':unittest.main()
