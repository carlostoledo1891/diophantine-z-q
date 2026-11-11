"""Remote-authority restoration tests with synthetic anchors and fixture keys."""
import copy,threading,unittest
from pathlib import Path
from unittest.mock import patch
import restore_verified_stores as restore
from protected_ledger_store import ProtectedPath,Conflict
from test_store_bridge import StoreFixture,run
import audit_intake

class RemoteAnchor:
    def __init__(self,checkpoint):self.current=copy.deepcopy(checkpoint);self.reads=0;self.cas_calls=0
    def read(self):self.reads+=1;return copy.deepcopy(self.current)
    def compare_and_swap(self,expected,replacement):
        self.cas_calls+=1
        if self.current!=expected:return False
        self.current=copy.deepcopy(replacement);return True
    def initialize(self,*args):raise AssertionError('remote initialization forbidden')

class RestoreTests(StoreFixture):
    def setUp(self):
        super().setUp();self.store.append(run(1),'fixture',self.cp())
        self.entries,self.checkpoint,_=self.store.read_verified();self.remote=RemoteAnchor(self.checkpoint)
        self.destination=ProtectedPath(self.root/'ledger/restored.sqlite',(self.root/'candidate',))
    def restore(self):
        return restore.restore_operator_store(self.destination,self.remote,self.entries,self.keys,self.checkpoint)
    def test_restore_and_append_use_remote_authority(self):
        store=self.restore();self.assertEqual(store.read_verified()[1],self.checkpoint)
        next_cp=store.append(run(2),'fixture',self.checkpoint)
        self.assertEqual(self.remote.current,next_cp);self.assertEqual(self.remote.cas_calls,1)
    def test_restore_never_initializes_or_changes_remote(self):
        self.restore();self.assertEqual(self.remote.cas_calls,0);self.assertEqual(self.remote.current,self.checkpoint)
    def test_remote_advance_invalidates_local_mirror(self):
        store=self.restore();self.remote.current=dict(self.checkpoint,sequence=2)
        with self.assertRaises(restore.operator_ledger.Invalid):store.read_verified()
    def test_wrong_remote_checkpoint_rejected_before_file_creation(self):
        self.remote.current['entry_sha256']='0'*64
        with self.assertRaises(Conflict):self.restore()
        self.assertFalse(self.destination.path.exists())
    def test_unsigned_entries_rejected_before_file_creation(self):
        self.entries[0]['event']['agent_id']='candidate'
        with self.assertRaises(restore.operator_ledger.Invalid):self.restore()
        self.assertFalse(self.destination.path.exists())
    def test_existing_target_never_overwritten(self):
        self.destination.path.write_bytes(b'preserve')
        with self.assertRaises(restore.operator_ledger.Invalid):self.restore()
        self.assertEqual(self.destination.path.read_bytes(),b'preserve')
    def test_remote_change_during_restore_rejected(self):
        original=self.remote.read
        def read():
            if self.remote.reads==1:self.remote.current['entry_sha256']='0'*64
            return original()
        with patch.object(self.remote,'read',side_effect=read),self.assertRaises(Conflict):self.restore()
        self.assertFalse(self.destination.path.exists())
    def test_remote_change_after_install_blocks_read(self):
        original=self.remote.read
        def read():
            if self.remote.reads==2:self.remote.current['entry_sha256']='0'*64
            return original()
        with patch.object(self.remote,'read',side_effect=read),self.assertRaises(restore.operator_ledger.Invalid):self.restore()
        self.assertTrue(self.destination.path.exists()) # Stale verified copy, never authority.
    def test_hardlink_failure_does_not_replace(self):
        with patch.object(restore.os,'link',side_effect=OSError('unsupported')),self.assertRaises(OSError):self.restore()
        self.assertFalse(self.destination.path.exists());self.assertFalse(list(self.destination.path.parent.glob('verified-ledger-*.sqlite')))
    def test_audit_domain_restore(self):
        cp=audit_intake.genesis('remote-audit');anchor=RemoteAnchor(cp)
        store=restore.restore_audit_store(self.destination,anchor,[],self.keys,cp)
        self.assertEqual(store.read_verified()[1],cp);self.assertEqual(anchor.cas_calls,0)
    def test_wrong_codec_rejected(self):
        with self.assertRaises(audit_intake.Invalid):restore.restore_audit_store(self.destination,self.remote,self.entries,self.keys,self.checkpoint)

if __name__=='__main__':unittest.main()
