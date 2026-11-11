"""Protected configuration to real coverage validator; all I/O is mocked.

These tests do not manufacture production observations or make network requests.
Existing runtime tests separately exercise real signed fixture ledgers/publisher.
"""
import contextlib
import copy
from dataclasses import asdict
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch

import runtime as r
import coverage_gate as c
import offline_manifest_gate as g
import test_coverage_gate as coverage
import test_manifest_gate as legacy
import test_github_read_context as gh
import github_app_transport


class RuntimeCoverageTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.case=coverage.Case()
        self.p,self.e,self.blobs=self.case.p,self.case.e,self.case.blobs
        _,policy,_=gh.fixture();self.policy_dict=asdict(policy)
        self.policy_dict.update(repository_id=self.p['repository_id'],policy_sha256=self.p['policy_sha256'])
        self.job={'id':'fixture-job','publisher':{'repository':'fixture/repo','repository_id':self.p['repository_id'],
            'app_id':42,'installation_id':43,'base_ref':'main','target_mode':'head','required_merge_ci':[]},
            'policy':self.policy_dict,'packet':'packet.json','selected_reports':'selected.json','collector_sha256':'a'*64,
            'coverage_profile':copy.deepcopy(self.case.profile)}
        self.config={'schema':'protocol-controller/v1','controller_repository':'owner/controller',
                     'controller_repository_id':42,'jobs':[self.job]}
        self.env={'GITHUB_TOKEN':'synthetic-token','GITHUB_REPOSITORY':'owner/controller','GITHUB_REPOSITORY_ID':'42',
            'GITHUB_REF':'refs/heads/main','GITHUB_SHA':'a'*40,'PROTOCOL_APPROVED_SHA':'a'*40,
            'GITHUB_EVENT_NAME':'workflow_dispatch','PROTOCOL_APP_PRIVATE_KEY':'synthetic-no-private-key'}
        self.write_inputs();self.observed=[]

    def write_inputs(self):
        (self.root/'controller').mkdir(exist_ok=True)
        (self.root/'controller/config.json').write_text(json.dumps(self.config),encoding='utf-8')
        (self.root/'packet.json').write_text(json.dumps(self.p),encoding='utf-8')
        (self.root/'selected.json').write_text('{}',encoding='utf-8')

    @contextlib.contextmanager
    def composition(self):
        owner=self
        remote=MagicMock();remote.entries.return_value=([],{})
        state=MagicMock();state.read.return_value={'generation':0}
        authority=SimpleNamespace(active=None)
        class FakePublisher:
            def __init__(self,config,state,transport,runner,authority):
                owner.observed.append(('publisher',runner));self.runner=runner
            def key(self,head):return head
            def run(self,head,expected):
                session=self.runner.evaluate(None)
                return {'published_success':session.result['records_consistent'],'target_sha':head}
        def live(packet,recorder,reader,selected,blob_reader,profile=None):
            owner.observed.append(('validator',copy.deepcopy(profile)))
            return SimpleNamespace(result=g.check_records(packet,owner.e,blob_reader,profile))
        with contextlib.ExitStack() as stack:
            for name,value in [('restore_operator_store',MagicMock()),('restore_audit_store',MagicMock()),
                               ('SQLiteGenerationState',MagicMock(return_value=state)),
                               ('RemoteGenerationAuthority',MagicMock(return_value=authority)),
                               ('IntakeRecorder',MagicMock()),('AuditObservationSource',MagicMock()),
                               ('CachingAPI',MagicMock()),('GitBlobReader',MagicMock(return_value=self.blobs))]:
                stack.enter_context(patch.object(r,name,value))
            stack.enter_context(patch.object(r.github_fork_context,'ForkReadContext',return_value=MagicMock()))
            stack.enter_context(patch.object(r.publisher,'Publisher',FakePublisher))
            stack.enter_context(patch.object(r.live_protocol_context_forks,'evaluate_session',side_effect=live))
            yield remote

    def run_main(self):
        self.write_inputs()
        with self.composition() as remote, contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(r,'ROOT',self.root))
            api=MagicMock()
            api.request.side_effect=lambda method,path,data=None: (
                {'id':42,'full_name':'owner/controller','private':True} if path.endswith('/owner/controller')
                else {'ref':'refs/heads/main','object':{'type':'commit','sha':'a'*40}})
            stack.enter_context(patch.object(r,'ControllerHTTPS',return_value=api))
            stack.enter_context(patch.object(r,'load_keys',return_value={'operator':{},'intake':{},'collector':{}}))
            stack.enter_context(patch.object(github_app_transport.RS256Signer,'from_pem',return_value=object()))
            stack.enter_context(patch.object(github_app_transport,'GitHubAppTransport',return_value=object()))
            stack.enter_context(patch.object(r,'RemoteState',return_value=remote))
            stack.enter_context(patch.object(r,'GitState',return_value=object()))
            output=stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            result=r.main(self.env)
            return result,json.loads(output.getvalue())

    def test_load_job_preserves_ingress_four_tuple(self):
        result=r.load_job(self.root,self.job)
        self.assertEqual(len(result),4);self.assertEqual(result[2],self.p)

    def test_load_job_missing_profile_fails(self):
        del self.job['coverage_profile']
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):r.load_job(self.root,self.job)

    def test_load_job_altered_profile_fails(self):
        self.job['coverage_profile']['protocol_version']='1.4'
        with self.assertRaisesRegex(g.Invalid,'unknown-coverage-profile'):r.load_job(self.root,self.job)

    def test_load_job_profile_must_be_inline_object(self):
        for value in (None,'profile.json',[],True):
            self.job['coverage_profile']=value
            with self.subTest(value=value),self.assertRaisesRegex(r.Invalid,'inline protected object'):
                r.load_job(self.root,self.job)

    def test_candidate_cannot_supply_profile(self):
        del self.job['coverage_profile'];self.p['coverage_profile']=copy.deepcopy(self.case.profile);self.write_inputs()
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):r.load_job(self.root,self.job)

    def test_load_job_legacy_without_profile(self):
        self.p,self.e,self.blobs=legacy.fixture();del self.job['coverage_profile'];self.write_inputs()
        self.assertEqual(len(r.load_job(self.root,self.job)),4)

    def test_main_valid_profile_reaches_real_validator_and_publisher(self):
        code,results=self.run_main()
        self.assertEqual(code,0);self.assertTrue(results[0]['published_success'])
        profile=next(v for k,v in self.observed if k=='validator')
        self.assertEqual(profile,self.case.profile)
        self.assertIsNot(profile,self.job['coverage_profile'])

    def test_main_missing_profile_cannot_reach_publisher(self):
        del self.job['coverage_profile']
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):self.run_main()
        self.assertFalse(self.observed)

    def test_main_altered_profile_cannot_reach_publisher(self):
        self.job['coverage_profile']['governing_protocol']['sha256']='0'*64
        with self.assertRaisesRegex(g.Invalid,'unapproved-governing'):self.run_main()
        self.assertFalse(self.observed)

    def test_main_candidate_field_cannot_override_protected_profile(self):
        self.p['coverage_profile']={'mode':'legacy'}
        with self.assertRaisesRegex(g.Invalid,'schema:packet'):self.run_main()
        self.assertEqual(next(v for k,v in self.observed if k=='validator'),self.case.profile)

    def test_main_legacy_remains_valid(self):
        self.p,self.e,self.blobs=legacy.fixture();del self.job['coverage_profile']
        code,results=self.run_main()
        self.assertEqual(code,0);self.assertTrue(results[0]['published_success'])
        self.assertIsNone(next(v for k,v in self.observed if k=='validator'))

    def direct_evaluate(self,profile):
        config,policy,packet,selected=r.load_job(self.root,self.job)
        with self.composition() as remote:
            result=r.evaluate(remote,self.root,(self.root/'candidate',),{'operator':{},'intake':{},'collector':{}},
                config,object(),packet,selected,policy,'a'*64,blob_reader=self.blobs,coverage_profile=profile)
            return result

    def test_direct_evaluate_checks_missing_profile_before_state(self):
        with self.assertRaisesRegex(g.Invalid,'coverage-profile-required'):self.direct_evaluate(None)
        self.assertFalse(self.observed)

    def test_direct_evaluate_checks_altered_profile_before_state(self):
        profile=copy.deepcopy(self.case.profile);profile['runtime_policy_sha256']='0'*64
        with self.assertRaisesRegex(g.Invalid,'runtime-policy-mismatch'):self.direct_evaluate(profile)
        self.assertFalse(self.observed)

    def test_direct_evaluate_passes_protected_profile(self):
        self.assertTrue(self.direct_evaluate(self.case.profile)['published_success'])
        self.assertEqual(next(v for k,v in self.observed if k=='validator'),self.case.profile)

    def test_runner_takes_profile_copy_not_input_provider_data(self):
        profile=copy.deepcopy(self.case.profile)
        inputs=r.publisher.EvaluationInputs(self.p,object(),object(),{},self.blobs)
        runner=r.ForkProtocolRunner(lambda _:inputs,profile)
        profile['mode']='non_substantive'
        with self.composition():result=runner.evaluate(None)
        self.assertTrue(result.result['records_consistent'])
        self.assertEqual(next(v for k,v in self.observed if k=='validator'),self.case.profile)


if __name__=='__main__':unittest.main(verbosity=2)
