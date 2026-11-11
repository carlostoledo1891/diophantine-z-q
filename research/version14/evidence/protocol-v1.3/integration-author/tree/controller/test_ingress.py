"""Ingress fixtures are synthetic owner observations, never production audits."""
import copy,io,unittest
from pathlib import Path
from unittest.mock import patch
import ingress as i
import runtime as r
from test_runtime import ControlAPI
from test_live_protocol_context import LiveFixture
from test_github_fork_context import forkify
import github_fork_context
import audit_intake
from protected_ledger_store import ProtectedPath
from restore_verified_stores import restore_operator_store,restore_audit_store
from durable_intake import IntakeRecorder,AuditObservationSource
import live_protocol_context_forks as live

class FixtureCollector:
    def __init__(self,packet,blobs):self.packet=packet;self.blobs=blobs;self.calls=0
    def collect_pair(self,packet):
        self.calls+=1;checked=set()
        for side in ('base','head'):
            i.git_manifest.verify_manifest(self.packet[side])
            for path,entry in self.packet[side]['files'].items():
                if entry['blob'] not in checked:
                    with self.blobs.open(side,path,entry) as stream:i.git_manifest.verify_blob(stream,entry,'sha1')
                    checked.add(entry['blob'])
        return {s:copy.deepcopy(self.packet[s]) for s in ('base','head')}

class IngressTests(LiveFixture):
    def setUp(self):
        super().setUp()
        self.transport.root=self.reader.root
        self.reader.api=r.CachingAPI(self.transport)
        self.control=ControlAPI();self.git=r.GitState(self.control,'owner/controller',42)
        env={'GITHUB_REPOSITORY':'owner/controller','GITHUB_REPOSITORY_ID':'42','GITHUB_REF':'refs/heads/main',
             'GITHUB_SHA':'a'*40,'GITHUB_EVENT_NAME':'workflow_dispatch'}
        self.guard=r.RevisionGuard(self.control,'owner/controller',42,'a'*40,env)
        wrapper={'schema':'protocol-controller-generation/v1','controller_sha':None,
                 'state':{'schema':'protocol-publisher-state/v1','generations':[],'targets':[]},'publication':None}
        raw=r.canonical(wrapper);sha=r.digest(raw)
        cps={'operator':i.operator_ledger.genesis('fixture-ledger'),'intake':i.audit_intake.genesis('ingress-audit'),
             'publisher':{'snapshot_sha256':sha}}
        self.git.append(self.git.load(),{'state/snapshots/'+sha+'.json':raw},cps)
        self.remote=r.RemoteState(self.git,self.guard)
        self.ingress_keys={'operator':self.store.keys,'intake':self.audit.keys,'collector':{'collector':self.collector_key}}
        self.collector=FixtureCollector(self.p,self.blobs)
        source_rows=self.reader.intake(7)
        materials=audit_intake.materials_from({'intake':source_rows},{})
        source_ids=sorted(materials);self.first_material=source_ids[0]
        events=[copy.deepcopy(e['event']) for e in self.store.read_verified()[0]]
        classifications=[{'source':{'material_id':mid},'finding_ids':['F1'] if mid==self.first_material else [],
                           'reason':'SYNTHETIC owner classification','observation_base64':i.base64.b64encode(b'SYNTHETIC recorded classification').decode()}
                         for mid in source_ids]
        for entry in events:
            if entry['kind']=='report_observed':
                classifications.append({'source':{'report_id':entry['report_id'],'report_sha256':r.digest(i.base64.b64decode(entry['body_base64']))},
                    'finding_ids':[],'reason':'SYNTHETIC owner says no additional findings in this exact report',
                    'observation_base64':i.base64.b64encode(b'SYNTHETIC actual operator observation').decode()})
        self.batch={'schema':'protocol-owner-ingress/v1','id':'synthetic-batch','job_id':'fixture-job','mode':'finalize',
            'key_ids':{'operator':'fixture','intake':'fixture','collector':'collector'},'operator_events':events,'external_materials':[],
            'findings':[{'finding_id':'F1','body_base64':i.base64.b64encode(b'Original objection').decode(),
                         'sources':[{'material_id':self.first_material}],
                         'observation_base64':i.base64.b64encode(b'SYNTHETIC finding registration').decode()}],
            'classifications':classifications}
    def apply(self):
        return i.apply_batch(self.remote,self.ingress_keys,self.policy,self.p,self.selected,self.batch,self.collector,self.reader)
    def test_one_atomic_commit_contains_signed_entries_and_checkpoints(self):
        before=self.remote.current.index['generation'];publisher=copy.deepcopy(self.remote.current.index['checkpoints']['publisher'])
        result=self.apply();self.assertFalse(result['merge_authorized']);self.assertFalse(result['unclassified_material_ids'])
        self.assertEqual(self.remote.current.index['generation'],before+1)
        self.assertEqual(self.remote.current.index['checkpoints']['publisher'],publisher)
        op,opcp=self.remote.entries('operator',i.operator_ledger,self.ingress_keys['operator'])
        inc,incp=self.remote.entries('intake',i.audit_intake,self.ingress_keys['intake'])
        self.assertTrue(op);self.assertTrue(inc);self.assertEqual(len(op),opcp['sequence']);self.assertEqual(len(inc),incp['sequence'])
    def test_bootstrap_can_feed_real_live_evaluator(self):
        self.apply();path=self.root/'fresh';path.mkdir()
        op,opcp=self.remote.entries('operator',i.operator_ledger,self.ingress_keys['operator'])
        inc,incp=self.remote.entries('intake',i.audit_intake,self.ingress_keys['intake'])
        ops=restore_operator_store(ProtectedPath(path/'op.sqlite',(self.root/'candidate',)),r.ReadOnlyRemoteAnchor(self.remote,'operator'),op,self.ingress_keys['operator'],opcp)
        ins=restore_audit_store(ProtectedPath(path/'in.sqlite',(self.root/'candidate',)),r.ReadOnlyRemoteAnchor(self.remote,'intake'),inc,self.ingress_keys['intake'],incp)
        recorder=IntakeRecorder(ins,ops,AuditObservationSource(self.reader),i.COLLECTOR_SHA,self.ingress_keys['collector'])
        session=live.evaluate_session(self.p,recorder,self.reader,self.selected,self.blobs)
        self.assertTrue(session.result['records_consistent']);session.recheck()
    def test_exact_batch_replay_does_not_resign_or_recollect(self):
        self.apply();commit=self.remote.current.commit;calls=self.collector.calls
        result=self.apply();self.assertTrue(result['already_committed']);self.assertEqual(self.remote.current.commit,commit);self.assertEqual(self.collector.calls,calls)
    def test_reused_batch_id_for_new_input_rejected(self):
        self.apply();self.batch['mode']='capture'
        with self.assertRaisesRegex(i.Invalid,'batch ID reused'):self.apply()
    def test_incomplete_classification_never_advances_remote(self):
        before=self.remote.current.commit;self.batch['classifications'].pop()
        with self.assertRaises(i.operator_ledger.Invalid):self.apply()
        self.assertEqual(self.git.tip(),before)
    def test_capture_mode_retains_unclassified_material_without_success(self):
        self.batch['mode']='capture';self.batch['findings']=[];self.batch['classifications']=[]
        result=self.apply();self.assertTrue(result['unclassified_material_ids']);self.assertFalse(result['merge_authorized'])
    def test_missing_selected_receipt_blocks_finalize(self):
        self.selected.pop('assembly:complete');before=self.git.tip()
        with self.assertRaisesRegex(i.Invalid,'receipt selections'):self.apply()
        self.assertEqual(self.git.tip(),before)
    def test_false_report_selector_rejected(self):
        item=next(c for c in self.batch['classifications'] if 'report_id' in c['source']);item['source']['report_sha256']='0'*64
        with self.assertRaisesRegex(i.Invalid,'one exact archived report'):self.apply()
    def test_unknown_material_selector_rejected(self):
        self.batch['findings'][0]['sources']=[{'material_id':'candidate invents ID'}]
        with self.assertRaisesRegex(i.Invalid,'unknown exact'):self.apply()
    def test_no_auto_generated_classifications(self):
        self.batch['classifications']=[]
        with self.assertRaisesRegex(i.operator_ledger.Invalid,'unclassified'):self.apply()
    def test_candidate_boolean_not_supported(self):
        self.batch['verified']=True
        with self.assertRaisesRegex(i.Invalid,'invalid ingress batch'):self.apply()
    def test_original_report_bytes_must_be_signed_from_supplied_observation(self):
        entry=next(e for e in self.batch['operator_events'] if e['kind']=='report_observed')
        entry['body_base64']=i.base64.b64encode(b'Other report').decode()
        with self.assertRaises(i.Invalid):self.apply()
    def test_all_blob_contents_verified_even_if_not_core_evidence(self):
        entry=self.p['head']['files']['paper.md'];self.blobs.values[entry['sha256']]=b'corrupt'
        before=self.git.tip()
        with self.assertRaises(i.git_manifest.Invalid):self.apply()
        self.assertEqual(self.git.tip(),before)
    def test_changed_unconsumed_raw_metadata_cannot_be_signed(self):
        self.p=copy.deepcopy(self.p);self.p['head']['files']['paper.md']['sha256']='0'*64
        with self.assertRaisesRegex(i.Invalid,'collection differs'):self.apply()
    def test_operator_observation_not_dropped_on_second_capture(self):
        self.apply();count=self.remote.current.index['checkpoints']['operator']['sequence']
        self.batch=dict(self.batch,id='second-capture',mode='capture',operator_events=[],findings=[],classifications=[])
        self.apply();self.assertEqual(self.remote.current.index['checkpoints']['operator']['sequence'],count)
        state=i.audit_intake.verify(*self._audit_verify_args())
        reports=[v for v in state['materials']['1/7'].values() if v['source']=='operator_ledger']
        self.assertEqual(len(reports),len(self.selected))
    def _audit_verify_args(self):
        entries,cp=self.remote.entries('intake',i.audit_intake,self.ingress_keys['intake'])
        return entries,self.ingress_keys['intake'],cp
    def test_cas_race_preserves_existing_state(self):
        before=self.git.tip();old=self.collector.collect_pair
        def race(packet):
            result=old(packet)
            snap=self.git.load();self.git.append(snap,{},snap.index['checkpoints']);return result
        self.collector.collect_pair=race
        with self.assertRaises(Exception):self.apply()
        self.assertNotEqual(self.git.tip(),before)
        self.assertEqual(self.git.load().index['checkpoints']['operator']['sequence'],0)
    def test_fork_capture_supported_without_executing_fork(self):
        forkify(self.p,self.transport)
        self.reader=github_fork_context.ForkReadContext(self.policy,self.transport)
        self.reader.api=r.CachingAPI(self.transport)
        result=self.apply();self.assertFalse(result['unclassified_material_ids'])

class BareCollectorTests(unittest.TestCase):
    def test_production_argv_has_no_token_or_checkout(self):
        import tempfile
        from types import SimpleNamespace
        with tempfile.TemporaryDirectory() as d:
            policy=SimpleNamespace(repository='fixture/repo',base_ref='main')
            token='fixture-secret-not-real'
            collector=i.BareGitCollector(policy,SimpleNamespace(_access=lambda:token),d,git_executable=str(Path(d)/'git'))
            packet={'git_hash':'sha1','pull_request':7,'base':{'commit':'a'*40},'head':{'commit':'b'*40}}
            calls=[]
            def run(args,env):
                calls.append((list(args),dict(env)))
                return (('a' if args[-1].endswith('base') else 'b')*40+'\n').encode() if 'rev-parse' in args else b''
            workers=[]
            def worker(argv,env):
                workers.append((list(argv),dict(env)));Path(argv[-1]).write_text('{}');return b'{}'
            secrets={'PROTOCOL_APP_PRIVATE_KEY':'fixture-private-key','PROTOCOL_OPERATOR_KEYS':'fixture-operator-key',
                     'PROTOCOL_INTAKE_KEYS':'fixture-intake-key','PROTOCOL_COLLECTOR_KEYS':'fixture-collector-key',
                     'GITHUB_TOKEN':'fixture-controller-token','GH_TOKEN':'fixture-gh-token'}
            with patch.dict(i.os.environ,secrets),patch.object(collector,'_run',side_effect=run),patch.object(collector,'_run_argv',side_effect=worker),patch.object(i.git_manifest,'verify_manifest'):
                collector.collect_pair(packet)
            self.assertFalse(any(token in ' '.join(args) for args,_ in calls))
            self.assertFalse(any('checkout' in args for args,_ in calls))
            fetch=next(args for args,_ in calls if 'fetch' in args)
            self.assertIn('+refs/pull/7/head:refs/heads/approved-head',fetch)
            self.assertTrue(all('PROTOCOL_OPERATOR_KEYS' not in env for _,env in calls))
            self.assertEqual(len(workers),2)
            self.assertTrue(all('-I' in argv for argv,_ in workers))
            self.assertTrue(all(not set(secrets)&set(env) for _,env in workers))
            self.assertTrue(all(token not in ' '.join(argv) for argv,_ in workers))

if __name__=='__main__':unittest.main()
