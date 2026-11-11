"""Full live evaluator regressions repeated under authenticated fork profile."""
import unittest
from pathlib import Path
from unittest.mock import patch
import test_live_protocol_context as original
import test_github_fork_context as forks
import live_protocol_context_forks as live
from durable_intake import AuditObservationSource

class ForkLiveTests(original.LiveTests):
    def setUp(self):
        replacement=patch.object(original,'live',live);replacement.start();self.addCleanup(replacement.stop)
        super().setUp()
        forks.forkify(self.p,self.transport)
        self.reader=forks.fork.ForkReadContext(self.policy,self.transport)
        self.recorder.github_reader=AuditObservationSource(self.reader)
        self.capture()
    def test_session_binds_actual_fork_and_base_pull_refs(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        self.assertEqual(session.observation['state']['head_repository']['id'],42)
        self.assertEqual(session.observation['state']['pull_refs']['head']['commit'],self.p['head']['commit'])
        self.assertTrue(all(path.startswith(original.github.ROOT) for path in self.transport.calls))
        session.recheck()
    def test_changed_fork_ref_after_evaluation_rejected(self):
        session=live.evaluate_session(self.p,self.recorder,self.reader,self.selected,self.blobs)
        self.transport.routes[original.github.ROOT+'/git/ref/pull/7/head'][0]['object']['sha']='9'*40
        with self.assertRaisesRegex(original.g.core.Invalid,'pull ref mismatch'):session.recheck()

class ExactProfileTests(unittest.TestCase):
    def test_only_declared_profile_delta(self):
        root=Path(__file__).resolve().parent
        expected=(root/'live_protocol_context.py').read_text()
        expected=expected.replace('import github_read_context\n','import github_read_context\nimport github_fork_context\n')
        expected=expected.replace('DEPENDENCY_PINS={',"DEPENDENCY_PINS={\n    'github_fork_context.py':'0de8fbbb6bd9a0de03a30645ca72ed981e3347da8599e37ce1828f1a0b245345',")
        expected=expected.replace('type(live_reader) is github_read_context.ReadContext','type(live_reader) in (github_read_context.ReadContext, github_fork_context.ForkReadContext)')
        expected=expected.replace('Protected-process live evaluation; no GitHub mutations or merge authority.', 'Fork-capable protected-process live evaluation; no GitHub mutations or merge authority.')
        self.assertEqual((root/'live_protocol_context_forks.py').read_text(),expected)

if __name__=='__main__':unittest.main()
