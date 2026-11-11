"""Projection regressions using actual live sessions and publisher writes."""
from unittest.mock import patch
import unittest
import copy

from test_runtime import RuntimeTests
import test_github_read_context as gh
import github_read_context as reader


class ProjectionTests(RuntimeTests):
    def after_success(self, change):
        pr = self.transport.routes[gh.ROOT + '/pulls/7'][0]
        pr.update(mergeable_state='blocked', mergeable=True, rebaseable=True,
                  title='Reviewed title', body='Reviewed body', labels=[], requested_reviewers=[])
        self.setup_remote()
        original = self.app.update_check
        def update(repo, cid, payload):
            result = original(repo, cid, payload)
            if payload.get('conclusion') == 'success':
                change(pr)
            return result
        with patch.object(self.app, 'update_check', side_effect=update):
            result = self.execute()
        return result

    def test_own_success_derived_state_change_remains_successful(self):
        result = self.after_success(lambda pr: pr.update(mergeable_state='clean', rebaseable=None))
        self.assertTrue(result['published_success'], result)
        self.assertEqual([c.conclusion for c in self.app.checks.values()], ['success'])

    def test_repository_and_ci_counters_can_change(self):
        def counters(pr):
            for side in ('base', 'head'):
                pr[side]['repo'].update(size=999, open_issues=12, open_issues_count=12)
            run = self.transport.routes[gh.ROOT + '/actions/runs/20'][0]
            for key in ('repository', 'head_repository'):
                run[key].update(size=999, open_issues=12, open_issues_count=12)
        result = self.after_success(counters)
        self.assertTrue(result['published_success'], result)

    def test_repository_activity_does_not_revoke_review(self):
        def activity(pr):
            for side in ('base', 'head'):
                pr[side]['repo'].update(stargazers_count=55, watchers=55,
                    watchers_count=55, forks=6, forks_count=6, network_count=6,
                    subscribers_count=9, updated_at='later', pushed_at='later')
            run = self.transport.routes[gh.ROOT + '/actions/runs/20'][0]
            for key in ('repository', 'head_repository'):
                run[key].update(stargazers_count=55, updated_at='later', pushed_at='later')
        result = self.after_success(activity)
        self.assertTrue(result['published_success'], result)

    def test_repository_privacy_change_revokes_review(self):
        result = self.after_success(lambda pr: pr['base']['repo'].update(private=True))
        self.assertFalse(result['published_success'])

    def test_repository_permission_change_revokes_review(self):
        result = self.after_success(lambda pr: pr['head']['repo'].update(permissions={'push':False}))
        self.assertFalse(result['published_success'])

    def test_repository_unknown_field_change_revokes_review(self):
        result = self.after_success(lambda pr: pr['base']['repo'].update(new_security_field='changed'))
        self.assertFalse(result['published_success'])

    def test_body_edit_revokes_success(self):
        result = self.after_success(lambda pr: pr.update(body='Changed after review'))
        self.assertFalse(result['published_success'])
        self.assertTrue(result['revocation_confirmed'])

    def test_draft_edit_revokes_success(self):
        result = self.after_success(lambda pr: pr.update(draft=True))
        self.assertFalse(result['published_success'])

    def test_head_edit_revokes_success(self):
        result = self.after_success(lambda pr: pr['head'].update(sha='9' * 40))
        self.assertFalse(result['published_success'])

    def test_ci_failure_revokes_success(self):
        def failure(pr):
            self.transport.routes[gh.ROOT + '/actions/runs/20'][0]['conclusion'] = 'failure'
        result = self.after_success(failure)
        self.assertFalse(result['published_success'])

    def test_new_intake_revokes_success(self):
        def comment(pr):
            self.transport.routes[gh.ROOT + '/issues/7/comments?per_page=100&page=1'][0].append(
                {'id': 78909, 'body': 'New substantive objection'})
        result = self.after_success(comment)
        self.assertFalse(result['published_success'])

    def test_projection_preserves_all_other_fields_and_raw_input(self):
        pr = {'title': 'T', 'body': 'B', 'draft': False, 'state': 'open', 'merged': False,
              'labels': [{'name': 'hold'}], 'requested_reviewers': [{'id': 4}],
              'unknown': {'size': 12}, 'mergeable_state': 'blocked', 'mergeable': True,
              'rebaseable': True, 'base': {'repo': {'id': 1, 'private': True,
              'default_branch': 'main', 'size': 42, 'open_issues': 4, 'open_issues_count': 4,
              'unknown': 'preserved'}}, 'head': {'repo': {'id': 2, 'size': 51}}}
        original = copy.deepcopy(pr)
        projected = reader.project_pr(pr)
        expected = copy.deepcopy(pr)
        for field in reader.PR_DERIVED_FIELDS:
            expected.pop(field)
        for side in ('base', 'head'):
            for field in reader.REPOSITORY_ACTIVITY_FIELDS:
                expected[side]['repo'].pop(field, None)
        self.assertEqual(projected, expected)
        self.assertEqual(pr, original)
        self.assertEqual(projected['unknown'], {'size': 12})


if __name__ == '__main__':
    suite = unittest.TestSuite(ProjectionTests(name) for name in ProjectionTests.__dict__ if name.startswith('test_'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())
