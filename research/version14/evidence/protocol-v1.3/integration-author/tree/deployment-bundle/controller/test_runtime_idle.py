"""Idle main-entry checks, including the real owner revision guard."""
import contextlib
import io
import unittest
from unittest.mock import patch

import runtime


class IdleRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.config = {
            'schema': 'protocol-controller/v1',
            'controller_repository': 'owner/controller',
            'controller_repository_id': 42,
            'jobs': [],
        }
        self.environment = {
            'GITHUB_TOKEN': 'fixture-token',
            'GITHUB_REPOSITORY': 'owner/controller',
            'GITHUB_REPOSITORY_ID': '42',
            'GITHUB_REF': 'refs/heads/main',
            'GITHUB_SHA': 'a' * 40,
            'PROTOCOL_APPROVED_SHA': 'a' * 40,
            'GITHUB_EVENT_NAME': 'schedule',
        }
        self.repository = {'id': 42, 'full_name': 'owner/controller', 'private': True}
        self.ref = {'ref': 'refs/heads/main', 'object': {'type': 'commit', 'sha': 'a' * 40}}

    def run_main(self):
        with patch.object(runtime, 'read_protected_json', return_value=self.config), \
             patch.object(runtime.ControllerHTTPS, 'request', side_effect=[self.repository, self.ref]) as requests, \
             patch.object(runtime, 'load_keys', side_effect=AssertionError('idle loaded keys')), \
             patch.object(runtime, 'evaluate', side_effect=AssertionError('idle evaluated a PR')), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            result = runtime.main(self.environment)
        self.assertEqual(requests.call_count, 2)
        return result, output.getvalue()

    def test_empty_jobs_succeeds_without_app_or_ledger_credentials(self):
        result, output = self.run_main()
        self.assertEqual(result, 0)
        self.assertEqual(output, '[]\n')

    def test_idle_rejects_wrong_approved_revision(self):
        self.environment['GITHUB_SHA'] = 'b' * 40
        with self.assertRaises(runtime.Invalid):
            self.run_main()

    def test_idle_rejects_changed_remote_main(self):
        self.ref['object']['sha'] = 'b' * 40
        with self.assertRaises(runtime.Invalid):
            self.run_main()

    def test_idle_rejects_wrong_owner_identity(self):
        self.repository['id'] = 99
        with self.assertRaises(runtime.Invalid):
            self.run_main()

    def test_idle_rejects_public_controller(self):
        self.repository['private'] = False
        with self.assertRaises(runtime.Invalid):
            self.run_main()

    def test_invalid_job_containers_remain_rejected(self):
        for jobs in (None, {}, 'empty', [None] * (runtime.MAX_JOBS + 1)):
            with self.subTest(jobs=type(jobs).__name__):
                self.config['jobs'] = jobs
                with self.assertRaises(runtime.Invalid):
                    self.run_main()

    def test_active_job_still_requires_keys(self):
        self.config['jobs'] = [{'id': 'active'}]
        with self.assertRaisesRegex(AssertionError, 'idle loaded keys'):
            self.run_main()


if __name__ == '__main__':
    unittest.main(verbosity=2)
