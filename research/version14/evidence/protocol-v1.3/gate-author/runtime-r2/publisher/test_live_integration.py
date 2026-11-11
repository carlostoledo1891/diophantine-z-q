"""Actual live evaluator and protected fixture stores; fake App writes only."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'adapter'))
from test_live_protocol_context import LiveFixture
from test_store_bridge import run
import test_github_read_context as gh
import app_publisher as p
from generation_state import SQLiteGenerationState
from test_publisher import FakeTransport,FakeAuthority

class FixtureApp(FakeTransport):
    def __init__(self,fixture):
        self.fixture=fixture;super().__init__(self.current())
        self.auth=p.AppIdentity(42,43,1)
    def current(self):
        s=self.fixture.reader.state(7);c=s['commits'];pr=s['pr']
        return p.PullContext(1,'fixture/repo',7,pr['base']['ref'],c['base']['commit'],c['base']['tree'],c['head']['commit'],c['head']['tree'],c['merge']['commit'],c['merge']['tree'])
    def open_contexts(self,repo,head):
        assert repo==1;c=self.current();return (c,) if c.head_sha==head else ()
    def list_checks(self,repo,head):
        assert repo==1;return tuple(c for c in self.checks.values() if c.head_sha==head)
    def get_check(self,repo,cid):assert repo==1;return self.checks[cid]
    def create_check(self,repo,payload):
        assert repo==1;self.next_id+=1;return self._write(self.next_id,payload['head_sha'],payload)
    def update_check(self,repo,cid,payload):
        assert repo==1;return self._write(cid,self.checks[cid].head_sha,payload)

class IntegrationTests(LiveFixture):
    def publisher(self,barrier_hook=None):
        app=FixtureApp(self)
        state=SQLiteGenerationState(self.root/'ledger/publisher.sqlite',(self.root/'candidate',));state.initialize()
        auth=FakeAuthority(state)
        if barrier_hook:
            original=auth.before_success
            def barrier(*args):original(*args);barrier_hook()
            auth.before_success=barrier
        inputs=lambda c:p.EvaluationInputs(self.p,self.recorder,self.reader,self.selected,self.blobs)
        config=p.Config('fixture/repo',1,42,43,'main','head')
        return p.Publisher(config,state,app,p.LiveProtocolRunner(inputs),auth),app
    def test_actual_full_live_evaluator_to_fake_check(self):
        pub,app=self.publisher()
        with patch('http.client.HTTPSConnection',side_effect=AssertionError('real network forbidden')):
            result=pub.run(self.p['head']['commit'],0)
        self.assertTrue(result['published_success'],result)
        self.assertEqual([c.conclusion for c in app.checks.values()],['success'])
        self.assertEqual(result['target_sha'],self.p['head']['commit'])
    def test_actual_operator_append_at_barrier_blocks_success(self):
        pub,app=self.publisher(lambda:self.store.append(run(999),'fixture',self.cp()))
        result=pub.run(self.p['head']['commit'],0)
        self.assertFalse(result['published_success']);self.assertFalse(any(c.conclusion=='success' for c in app.checks.values()))
    def test_actual_new_comment_at_barrier_blocks_success(self):
        def comment():self.transport.routes[gh.ROOT+'/issues/7/comments?per_page=100&page=1'][0].append({'id':987,'body':'New unresolved observation'})
        pub,app=self.publisher(comment);result=pub.run(self.p['head']['commit'],0)
        self.assertFalse(result['published_success']);self.assertFalse(any(c.conclusion=='success' for c in app.checks.values()))
    def test_actual_missing_receipt_cannot_publish(self):
        self.selected.pop('assembly:complete');pub,app=self.publisher()
        result=pub.run(self.p['head']['commit'],0)
        self.assertFalse(result['published_success']);self.assertFalse(any(c.conclusion=='success' for c in app.checks.values()))

if __name__=='__main__':unittest.main(verbosity=2)
