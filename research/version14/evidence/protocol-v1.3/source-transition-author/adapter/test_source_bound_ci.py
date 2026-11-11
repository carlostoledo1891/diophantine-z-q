"""Source-bound CI evidence tests. Synthetic API only; no network or credentials."""
import copy
import unittest
from unittest.mock import patch

import github_fork_context as fork
import test_github_read_context as original
from test_github_fork_context import forkify


class SourceBoundCITests(unittest.TestCase):
    def setUp(self):
        self.packet, self.policy, self.transport = original.fixture()
        forkify(self.packet, self.transport)
        self.reader = fork.ForkReadContext(self.policy, self.transport)
        workflow = self.policy.workflows[0]
        self.profile = patch.multiple(fork,
            SOURCE_BOUND_WORKFLOW=workflow.path,
            SOURCE_BOUND_WORKFLOW_SHA256=workflow.source_sha256[workflow.path],
            SOURCE_BOUND_PROFILES={('fixture/repo', 1, 10): fork.core.digest(workflow.source_sha256)},
            SOURCE_BOUND_JOB_LABELS={'check': 'ubuntu-24.04'})
        self.profile.start(); self.addCleanup(self.profile.stop)
        self.job.update(steps=[], runner_id=12, runner_name='hosted runner', runner_group_id=0,
                        runner_group_name='GitHub Actions', labels=['ubuntu-24.04'],
                        started_at='2026-11-08T03:38:34Z', completed_at='2026-11-08T03:39:34Z')
        self.runobj.update(run_started_at='2026-11-08T03:38:00Z', updated_at='2026-11-08T03:40:00Z')
        self.transport.routes[original.ROOT+'/actions/jobs/30'] = (self.job, {})

    @property
    def job(self):
        return self.transport.routes[original.ROOT+'/actions/runs/20/attempts/2/jobs?per_page=100&page=1'][0]['jobs'][0]

    @property
    def runobj(self):
        return self.transport.routes[original.ROOT+'/actions/runs/20'][0]

    def observe(self):
        return self.reader.observe(self.packet)

    def rejects(self, text):
        with self.assertRaisesRegex(fork.core.Invalid, text):
            self.observe()

    def verified_state(self):
        state = self.reader.state(7)
        self.reader.sources(state, self.packet)
        return state

    def test_empty_steps_keep_raw_evidence_and_name_alternate_basis(self):
        result = self.observe()
        ci = result['ci'][0]
        self.assertEqual(ci['jobs'][0]['steps'], [])
        self.assertEqual(ci['job_evidence'], [{'job_id': 30,
            'evidence_mode': 'source-bound-job-conclusion/v1', 'steps_unavailable': True,
            'workflow_sha256': self.policy.workflows[0].source_sha256[self.policy.workflows[0].path],
            'source_map_sha256': fork.core.digest(self.policy.workflows[0].source_sha256)}])
        path = original.ROOT+'/actions/runs/20/attempts/2/jobs?per_page=100&page=1'
        self.assertEqual(self.transport.calls.count(path), 2)
        self.assertTrue(any('/git/blobs/' in p for p in self.transport.calls))
        self.assertFalse(result['merge_authorized'])

    def test_complete_step_route_does_not_need_empty_step_profile(self):
        self.job['steps'] = [{'status':'completed', 'conclusion':'success'}]
        with patch.object(fork, 'SOURCE_BOUND_PROFILES', {}):
            evidence = self.observe()['ci'][0]['job_evidence'][0]
        self.assertEqual(evidence, {'job_id':30, 'evidence_mode':'api-step-conclusions',
                                   'steps_unavailable':False})

    def test_direct_job_response_must_agree_including_unknown_fields(self):
        direct = copy.deepcopy(self.job)
        self.transport.routes[original.ROOT+'/actions/jobs/30'] = (direct, {})
        direct['steps'] = [{'status':'completed','conclusion':'success'}]
        self.rejects('job detail disagrees')
        direct['steps'] = []
        direct['new_field'] = 'changed'
        self.rejects('job detail disagrees')

    def test_all_supplied_non_success_or_partial_steps_rejected(self):
        for step in ({'status':'completed','conclusion':'failure'},
                     {'status':'completed','conclusion':'skipped'},
                     {'status':'completed','conclusion':'cancelled'},
                     {'status':'completed','conclusion':'neutral'},
                     {'status':'in_progress','conclusion':None},
                     {'status':'completed'}, None):
            with self.subTest(step=step):
                self.job['steps'] = [step]
                self.rejects('CI step not actually successful')

    def test_missing_null_and_malformed_steps_do_not_use_route(self):
        for value in (None, {}, '', False):
            with self.subTest(value=value):
                self.job['steps'] = value
                self.rejects('missing or malformed steps')
        del self.job['steps']
        self.rejects('missing or malformed steps')

    def test_source_check_cannot_be_skipped_by_calling_ci_directly(self):
        state = self.reader.state(7)
        with self.assertRaisesRegex(fork.core.Invalid, 'current source verification'):
            self.reader.ci(state, 7)

    def test_failed_reverification_revokes_previous_source_stamp(self):
        state = self.verified_state()
        invalid = copy.deepcopy(self.packet); invalid['policy_sha256'] = 'f'*64
        with self.assertRaises(fork.core.Invalid):
            self.reader.sources(state, invalid)
        with self.assertRaisesRegex(fork.core.Invalid, 'current source verification'):
            self.reader.ci(state, 7)

    def test_source_stamp_binds_merge_tree_and_entire_policy(self):
        state = self.verified_state()
        state['commits']['merge']['tree'] = 'f'*40
        with self.assertRaisesRegex(fork.core.Invalid, 'current source verification'):
            self.reader.ci(state, 7)
        state = self.verified_state()
        self.reader.policy.workflows[0].source_sha256['scripts/check.py'] = 'f'*64
        with self.assertRaisesRegex(fork.core.Invalid, 'current source verification'):
            self.reader.ci(state, 7)

    def test_new_state_read_revokes_source_stamp(self):
        self.verified_state()
        state = self.reader.state(7)
        with self.assertRaisesRegex(fork.core.Invalid, 'current source verification'):
            self.reader.ci(state, 7)

    def test_source_check_binds_packet_commit_and_tree(self):
        state = self.reader.state(7)
        invalid = copy.deepcopy(self.packet); invalid['head']['tree'] = 'f'*40
        with self.assertRaisesRegex(fork.core.Invalid, 'context mismatch'):
            self.reader.sources(state, invalid)

    def test_removed_input_pin_rejected_by_complete_profile(self):
        del self.reader.policy.workflows[0].source_sha256['scripts/check.py']
        self.rejects('unapproved source-bound workflow profile')

    def test_changed_source_bytes_rejected_before_ci(self):
        self.reader.policy.workflows[0].source_sha256['scripts/check.py'] = 'f'*64
        self.rejects('unapproved policy or workflow source')
        self.assertFalse(any('/actions/' in p for p in self.transport.calls))

    def test_unknown_workflow_digest_and_profile_rejected(self):
        with patch.object(fork, 'SOURCE_BOUND_WORKFLOW_SHA256', 'f'*64):
            self.rejects('unapproved source-bound workflow profile')
        with patch.object(fork, 'SOURCE_BOUND_PROFILES', {}):
            self.rejects('unapproved source-bound workflow profile')

    def test_complete_profile_job_inventory_required(self):
        with patch.object(fork, 'SOURCE_BOUND_JOB_LABELS', {'check':'ubuntu-24.04', 'extra':'ubuntu-24.04'}):
            self.rejects('complete reviewed job inventory')

    def test_real_runner_required(self):
        original_job = copy.deepcopy(self.job)
        for key, value in [('id',True),('runner_id',0),('runner_id',True),('runner_id',1.0),
                           ('runner_name',''),('runner_group_id',True),('runner_group_id',-1),
                           ('runner_group_name',None)]:
            with self.subTest(key=key,value=value):
                self.job.clear(); self.job.update(copy.deepcopy(original_job)); self.job[key]=value
                self.rejects('invalid API record ID' if key == 'id' else 'assigned runner')

    def test_wrong_or_extra_runner_labels_rejected(self):
        for labels in ([],['windows-2022'],['ubuntu-24.04','self-hosted'],'ubuntu-24.04'):
            with self.subTest(labels=labels):
                self.job['labels'] = labels
                self.rejects('runner labels mismatch')

    def test_invalid_and_unordered_execution_times_rejected(self):
        for key, value in [('started_at',None),('started_at','2026-11-08T03:38:34'),
                           ('started_at','2026-99-08T03:38:34Z'),('started_at','1970-01-01T00:00:00Z'),
                           ('completed_at','2026-11-08T03:38:34Z'),('completed_at','2026-11-08T03:37:00Z'),
                           ('completed_at','2026-11-08T03:41:00Z')]:
            with self.subTest(key=key,value=value):
                saved=self.job[key]; self.job[key]=value
                self.rejects('execution times'); self.job[key]=saved

    def test_empty_steps_still_require_exact_job_attempt_head_and_success(self):
        for key,value,reason in [('run_id',21,'job provenance'),('run_attempt',1,'job provenance'),
                                 ('head_sha','f'*40,'job provenance'),('conclusion','skipped','job not successful'),
                                 ('conclusion','neutral','job not successful'),('status','in_progress','job not successful')]:
            with self.subTest(key=key,value=value):
                saved=self.job[key]; self.job[key]=value
                self.rejects(reason); self.job[key]=saved

    def test_recovered_step_metadata_between_reads_requires_new_observation(self):
        path=original.ROOT+'/actions/runs/20/attempts/2/jobs?per_page=100&page=1'
        count=0
        def hook(current):
            nonlocal count
            if current==path:
                count+=1
                if count==2:self.job['steps']=[{'status':'completed','conclusion':'success'}]
        self.transport.hook=hook
        self.rejects('CI changed during collection')

    def test_failed_step_on_second_read_never_falls_back(self):
        path=original.ROOT+'/actions/runs/20/attempts/2/jobs?per_page=100&page=1'
        count=0
        def hook(current):
            nonlocal count
            if current==path:
                count+=1
                if count==2:self.job['steps']=[{'status':'completed','conclusion':'failure'}]
        self.transport.hook=hook
        self.rejects('CI step not actually successful')


if __name__ == '__main__':
    unittest.main()
