"""End-to-end fixture evaluation. No real keys, model attestations or network."""
import base64,copy,hashlib,io,unittest
from unittest.mock import patch
import test_durable_intake as intake_fixtures
import test_manifest_gate as manifests
import test_github_read_context as github
from test_store_bridge import observation,run
import github_read_context as g
import live_protocol_context as live
import ledger_evidence_bridge as bridge
import manifest_transport
from durable_intake import IntakeRecorder,AuditObservationSource

def augment_fixture():
    ghpacket,policy,transport=github.fixture()
    packet,evidence,blobs=manifests.fixture()
    extra={'policy.md':b'approved policy','.github/workflows/ci.yml':b'approved workflow',
           'scripts/check.py':b'approved checker','paper.md':b'unchanged'}
    values={}; allfiles={}
    for side in ('base','head'):
        files={p:(v['mode'],blobs.values[v['sha256']]) for p,v in packet[side]['files'].items()}
        files.update(extra);allfiles[side]=files
        packet[side],more=manifests.manifest(files,side);values.update(more)
    packet['repository_id']=1;packet['policy_sha256']=hashlib.sha256(extra['policy.md']).hexdigest()
    replacements={ghpacket[s][k]:packet[s][k] for s in ('base','head') for k in ('commit','tree')}
    def replace(v):
        if type(v) is str:
            for old,new in replacements.items():v=v.replace(old,new)
            return v
        if type(v) is list:return [replace(x) for x in v]
        if type(v) is tuple:return tuple(replace(x) for x in v)
        if type(v) is dict:return {replace(k):replace(x) for k,x in v.items()}
        return v
    transport.routes=replace(transport.routes)
    def tree(files):
        nodes={}
        for path,value in files.items():
            mode,body=value if type(value) is tuple else ('100644',value)
            node=nodes;parts=path.split('/')
            for part in parts[:-1]:node=node.setdefault(part,{})
            node[parts[-1]]=(mode,body)
        def emit(node):
            rows=[];raw=b''
            for name in sorted(node,key=lambda n:n+('/' if type(node[n]) is dict else '')):
                val=node[name]
                if type(val) is dict:mode='040000';kind='tree';sha=emit(val)
                else:
                    mode,body=val;kind='blob';sha=g.core.git_object('blob',body,'sha1')
                    transport.routes[github.ROOT+'/git/blobs/'+sha]=({'sha':sha,'size':len(body),'encoding':'base64','content':base64.b64encode(body).decode()}, {})
                rows.append({'path':name,'mode':mode,'type':kind,'sha':sha})
                raw+=(mode.lstrip('0')+' '+name).encode()+b'\0'+bytes.fromhex(sha)
            sha=g.core.git_object('tree',raw,'sha1')
            transport.routes[github.ROOT+'/git/trees/'+sha]=({'sha':sha,'truncated':False,'tree':rows},{})
            return sha
        return emit(nodes)
    for side in ('base','head'):assert tree(allfiles[side])==packet[side]['tree']
    manifests.refresh(packet,evidence)
    return packet,evidence,manifests.Blobs(values),policy,transport

class LiveFixture(intake_fixtures.IntakeFixture):
    def setUp(self):
        super().setUp();self.p,self.e,self.blobs,self.policy,self.transport=augment_fixture()
        self.reader=g.ReadContext(self.policy,self.transport)
        self.recorder=IntakeRecorder(self.audit,self.store,AuditObservationSource(self.reader),self.collector_sha,{'collector':self.collector_key})
        self.envelopes={}
        for side in ('base','head'):
            m=self.p[side];expected={'repository_id':1,'commit':m['commit'],'tree':m['tree'],'collector_sha256':self.collector_sha}
            self.envelopes[side]=manifest_transport.seal(m,expected,'collector',self.collector_key)
        n=100;self.selected={}
        for r in self.e['runs']:
            n+=1;event={'kind':'run_observed','observation':observation(n),'run_id':r['id'],'agent_id':r['agent_id'],'model':r['model'],'tools':r['tools']}
            self.store.append(event,'fixture',self.cp())
        for r in self.e['receipts']:
            n+=1;name=r['kind']+':'+r['target']
            authors=self.e['authorship'][name] if r['kind']!='assembly' else sorted({a for v in self.e['authorship'].values() for a in v})
            freeze={'kind':'target_frozen','observation':observation(n),'freeze_id':'freeze-'+name,'target_kind':r['kind'],'target_id':r['target'],
                    'target_sha256':r['target_sha256'],'dependency_sha256':r['dependency_sha256'],'binding':copy.deepcopy(self.e['binding']),'author_runs':authors}
            self.store.append(freeze,'fixture',self.cp());n+=1;rid='report-'+name;self.selected[name]=rid
            report={'kind':'report_observed','observation':observation(n),'report_id':rid,'run_id':r['run_id'],'freeze_id':freeze['freeze_id'],
                    'decision':'accepted','scope':'Synthetic independent review','body_base64':base64.b64encode(self.blobs.values[r['report']['sha256']]).decode()}
            self.store.append(report,'fixture',self.cp())
        self.capture();mids=self.register('F1',body=b'Original objection');self.classify({mids[0]:['F1']})
    def evaluate(self,blobs=None):return live.evaluate(self.p,self.recorder,self.reader,self.selected,blobs or self.blobs)

class LiveTests(LiveFixture):
    def test_full_evaluation_real_blobs_and_independent_receipts(self):
        result=self.evaluate()
        self.assertTrue(result['records_consistent']);self.assertTrue(result['live_context_verified'])
        self.assertGreater(result['verified_evidence_blobs'],0)
        self.assertFalse(result['merge_authorized']);self.assertFalse(result['publication_token_authenticated'])
    def test_missing_receipt_selection(self):
        self.selected.pop('application:A')
        with self.assertRaisesRegex(g.core.Invalid,'incomplete explicit'):self.evaluate()
    def test_wrong_receipt_target(self):
        self.selected['application:A']=self.selected['application:B']
        with self.assertRaisesRegex(intake_fixtures.a.Invalid,'stale or wrong'):self.evaluate()
    def test_unknown_receipt(self):
        self.selected['application:A']='candidate invented'
        with self.assertRaisesRegex(intake_fixtures.a.Invalid,'unknown observed'):self.evaluate()
    def test_new_comment_requires_registration(self):
        self.transport.routes[github.ROOT+'/issues/7/comments?per_page=100&page=1'][0].append({'id':222,'body':'New finding'})
        with self.assertRaisesRegex(g.core.Invalid,'differs from registered capture'):self.evaluate()
    def test_deleted_comment_still_requires_fresh_capture(self):
        self.transport.routes[github.ROOT+'/issues/7/comments?per_page=100&page=1']=([],{})
        with self.assertRaisesRegex(g.core.Invalid,'differs from registered capture'):self.evaluate()
    def test_failing_ci_rejected_despite_valid_intake(self):
        self.transport.routes[github.ROOT+'/actions/runs/20'][0]['conclusion']='failure'
        with self.assertRaisesRegex(g.core.Invalid,'run not successful'):self.evaluate()
    def test_archive_only_reader_cannot_serve_as_live_reader(self):
        with self.assertRaisesRegex(g.core.Invalid,'strict live'):
            live.evaluate(self.p,self.recorder,AuditObservationSource(self.reader),self.selected,self.blobs)
    def test_policy_mismatch(self):
        other=copy.deepcopy(self.policy);object.__setattr__(other,'policy_paths',('paper.md',))
        with self.assertRaisesRegex(g.core.Invalid,'configurations differ'):
            live.evaluate(self.p,self.recorder,g.ReadContext(other,self.transport),self.selected,self.blobs)
    def test_collector_revoked(self):
        self.recorder.collector_keys={}
        with self.assertRaisesRegex(manifest_transport.Invalid,'unknown transport'):self.evaluate()
    def test_changed_operator_checkpoint(self):
        self.store.append(run(901),'fixture',self.cp())
        with self.assertRaisesRegex(intake_fixtures.a.Invalid,'operator ledger changed'):self.evaluate()
    def test_wrong_actual_blob_bytes(self):
        base=self.blobs
        class Bad:
            def open(self,side,path,entry):return io.BytesIO(b'fake')
        with self.assertRaises(g.core.Invalid):self.evaluate(Bad())
    def test_comment_added_during_blob_check(self):
        base=self.blobs;transport=self.transport;done=False
        class Race:
            def open(self,side,path,entry):
                nonlocal done
                if not done:
                    done=True;transport.routes[github.ROOT+'/issues/7/comments?per_page=100&page=1'][0].append({'id':223,'body':'New finding'})
                return base.open(side,path,entry)
        with self.assertRaisesRegex(g.core.Invalid,'GitHub changed during core'):self.evaluate(Race())
    def test_audit_added_during_blob_check(self):
        base=self.blobs;fixture=self;done=False
        class Race:
            def open(self,side,path,entry):
                nonlocal done
                if not done:
                    done=True;fixture.add({'kind':'external_registered','scope':'1/7','source_id':'new external',
                        'body_base64':intake_fixtures.b64(b'New issue'),'observation_base64':intake_fixtures.OBS})
                return base.open(side,path,entry)
        with self.assertRaisesRegex(intake_fixtures.a.Invalid,'unclassified historical'):self.evaluate(Race())
    def test_operator_added_during_blob_check(self):
        base=self.blobs;fixture=self;done=False
        class Race:
            def open(self,side,path,entry):
                nonlocal done
                if not done:done=True;fixture.store.append(run(902),'fixture',fixture.cp())
                return base.open(side,path,entry)
        with self.assertRaises(intake_fixtures.Conflict):self.evaluate(Race())
    def test_finish_cannot_run_before_context(self):
        verifier=live.TrustedContextVerifier(self.recorder,self.reader,self.selected)
        with self.assertRaisesRegex(g.core.Invalid,'did not complete'):verifier.finish()
    def test_verifier_single_use_and_finish_single_use(self):
        verifier=live.TrustedContextVerifier(self.recorder,self.reader,self.selected)
        _,cp,s=self.store.read_verified();reports=bridge.inventory(s)
        verifier.verify_context(self.p,cp,reports)
        with self.assertRaisesRegex(g.core.Invalid,'single-use'):verifier.verify_context(self.p,cp,reports)
        verifier.finish()
        with self.assertRaisesRegex(g.core.Invalid,'already consumed'):verifier.finish()
    def test_forged_inventory_rejected(self):
        verifier=live.TrustedContextVerifier(self.recorder,self.reader,self.selected)
        with self.assertRaisesRegex(g.core.Invalid,'inventory is not current'):
            verifier.verify_context(self.p,self.cp(),{})
    def test_selection_copied_at_construction(self):
        verifier=live.TrustedContextVerifier(self.recorder,self.reader,self.selected)
        self.selected.clear();_,cp,s=self.store.read_verified()
        verifier.verify_context(self.p,cp,bridge.inventory(s));verifier.finish()
    def test_session_rechecks_and_returns_defensive_copies(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        session.recheck();session.recheck();b=session.binding;b['repository_id']=99
        result=session.result;result['records_consistent']=False
        observation=session.observation;observation['state']['repository_id']=99
        self.assertEqual(session.binding['repository_id'],1);self.assertTrue(session.result['records_consistent'])
        self.assertEqual(session.observation['state']['repository_id'],1)
    def test_changed_dependency_pin_rejected(self):
        with patch.dict(live.DEPENDENCY_PINS,{'audit_intake.py':'0'*64}),self.assertRaisesRegex(g.core.Invalid,'dependency pin changed'):
            self.evaluate()
    def test_session_cannot_be_constructed_from_result_json(self):
        with self.assertRaises(g.core.Invalid):live.LiveEvaluation(None,{'records_consistent':True},None)
    def test_failed_session_latches_even_after_state_restored(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        row=self.transport.routes[github.ROOT+'/actions/runs/20'][0];row['conclusion']='failure'
        with self.assertRaises(g.core.Invalid):session.recheck()
        row['conclusion']='success'
        with self.assertRaisesRegex(g.core.Invalid,'permanently invalidated'):session.recheck()
    def test_collector_revocation_after_evaluation_blocks_recheck(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        self.recorder.collector_keys={}
        with self.assertRaisesRegex(manifest_transport.Invalid,'unknown transport'):session.recheck()
    def test_collector_code_change_after_evaluation_blocks_recheck(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        self.recorder.collector_sha256='1'*64
        with self.assertRaisesRegex(manifest_transport.Invalid,'binding'):session.recheck()
    def test_source_policy_weakening_after_evaluation_blocks_recheck(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        self.reader.policy.workflows[0].source_sha256.pop('scripts/check.py')
        with self.assertRaisesRegex(g.core.Invalid,'protected policy changed'):session.recheck()

if __name__=='__main__':unittest.main()
