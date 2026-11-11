import copy
import base64
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import git_manifest as m
import manifest_transport as t

class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.repo=Path(self.tmp.name)
        self.git('init','--bare')
        self.content=b'hello\n';blob=self.obj('blob',self.content)
        leaf=self.git('mktree',input=b'100644 blob '+blob.encode()+b'\tproof.md\n').decode().strip()
        self.commit=self.obj('commit',b'tree '+leaf.encode()+b'\nauthor Test <test@example.invalid> 0 +0000\ncommitter Test <test@example.invalid> 0 +0000\n\nfixture\n')
        self.manifest=m.collect(self.repo,self.commit)
    def tearDown(self):self.tmp.cleanup()
    def git(self,*args,input=None):
        return subprocess.run(['git','-C',str(self.repo),*args],input=input,check=True,capture_output=True,env=m.git_environment()).stdout
    def obj(self,kind,raw):return self.git('hash-object','-w','-t',kind,'--stdin',input=raw).decode().strip()
    def binding(self):return {'repository_id':1,'commit':self.commit,'tree':self.manifest['tree'],'collector_sha256':'a'*64}
    def test_all_bytes_and_commit_link(self):
        entry=self.manifest['files']['proof.md'];self.assertEqual(entry['sha256'],hashlib.sha256(self.content).hexdigest())
        self.assertEqual(self.manifest['stats']['path_bytes'],len(self.content));self.assertTrue(m.verify_manifest(self.manifest)['complete_tree_verified'])
    def test_omitted_file(self):
        del self.manifest['files']['proof.md']
        with self.assertRaisesRegex(m.Invalid,'tree mismatch'):m.verify_manifest(self.manifest)
    def test_commit_tampering(self):
        self.manifest['commit']='0'*40
        with self.assertRaisesRegex(m.Invalid,'commit object'):m.verify_manifest(self.manifest)
    def test_mode_tampering(self):
        self.manifest['files']['proof.md']['mode']='100755'
        with self.assertRaisesRegex(m.Invalid,'tree mismatch'):m.verify_manifest(self.manifest)
    def test_blob_verification(self):
        self.assertTrue(m.verify_blob(io.BytesIO(self.content),self.manifest['files']['proof.md'],'sha1'))
    def test_changed_blob(self):
        with self.assertRaisesRegex(m.Invalid,'hash mismatch'):m.verify_blob(io.BytesIO(b'HELLO\n'),self.manifest['files']['proof.md'],'sha1')
    def test_truncated_blob(self):
        with self.assertRaisesRegex(m.Invalid,'truncated'):m.verify_blob(io.BytesIO(b'h'),self.manifest['files']['proof.md'],'sha1')
    def test_trailing_blob(self):
        with self.assertRaisesRegex(m.Invalid,'trailing'):m.verify_blob(io.BytesIO(self.content+b'x'),self.manifest['files']['proof.md'],'sha1')
    def test_large_blob_is_streamed(self):
        size=9*1024*1024;raw=b'x'*size;oid=self.obj('blob',raw)
        tree=self.git('mktree',input=b'100644 blob '+oid.encode()+b'\tlarge.bin\n').decode().strip()
        commit=self.obj('commit',b'tree '+tree.encode()+b'\nauthor T <t@e.invalid> 0 +0000\ncommitter T <t@e.invalid> 0 +0000\n\nlarge\n')
        got=m.collect(self.repo,commit);self.assertEqual(got['files']['large.bin']['size'],size)
        class Reader(io.BytesIO):
            def read(self,n=-1):
                if n<0 or n>m.CHUNK:raise AssertionError('unbounded read')
                return super().read(n)
        self.assertTrue(m.verify_blob(Reader(raw),got['files']['large.bin'],'sha1'))
    def test_replacement_refs_are_ignored(self):
        other=self.obj('blob',b'wrong\n');old=self.manifest['files']['proof.md']['blob']
        self.git('update-ref','refs/replace/'+old,other)
        self.assertEqual(m.collect(self.repo,self.commit),self.manifest)
    def test_caller_git_environment_ignored(self):
        import os
        old=os.environ.get('GIT_OBJECT_DIRECTORY');os.environ['GIT_OBJECT_DIRECTORY']='not-a-repository'
        try:self.assertEqual(m.collect(self.repo,self.commit),self.manifest)
        finally:
            if old is None:os.environ.pop('GIT_OBJECT_DIRECTORY',None)
            else:os.environ['GIT_OBJECT_DIRECTORY']=old
    def test_authenticated_transport_is_not_origin_auth(self):
        key=b'k'*32;e=t.seal(self.manifest,self.binding(),'fixture',key)
        r=t.verify(self.manifest,e,self.binding(),{'fixture':key})
        self.assertTrue(r['transport_authenticated']);self.assertFalse(r['github_origin_authenticated']);self.assertFalse(r['merge_authorized'])
    def test_transport_tamper(self):
        key=b'k'*32;e=t.seal(self.manifest,self.binding(),'fixture',key);self.manifest['files']['proof.md']['sha256']='0'*64
        with self.assertRaisesRegex(m.Invalid,'changed manifest'):t.verify(self.manifest,e,self.binding(),{'fixture':key})
    def test_transport_wrong_key(self):
        e=t.seal(self.manifest,self.binding(),'fixture',b'k'*32)
        with self.assertRaisesRegex(m.Invalid,'authentication'):t.verify(self.manifest,e,self.binding(),{'fixture':b'z'*32})
    def test_unknown_key(self):
        e=t.seal(self.manifest,self.binding(),'fixture',b'k'*32)
        with self.assertRaisesRegex(m.Invalid,'unknown'):t.verify(self.manifest,e,self.binding(),{})
    def test_cross_repository_replay(self):
        e=t.seal(self.manifest,self.binding(),'fixture',b'k'*32);binding=self.binding();binding['repository_id']=2
        with self.assertRaisesRegex(m.Invalid,'unexpected'):t.verify(self.manifest,e,binding,{'fixture':b'k'*32})
    def test_boolean_identity_rejected(self):
        binding=self.binding();binding['repository_id']=True
        with self.assertRaisesRegex(m.Invalid,'repository'):t.seal(self.manifest,binding,'fixture',b'k'*32)
    def test_short_key_rejected(self):
        with self.assertRaisesRegex(m.Invalid,'32 bytes'):t.seal(self.manifest,self.binding(),'fixture',b'k')
    def test_unsupported_symlink(self):
        blob=self.obj('blob',b'outside');tree=self.git('mktree',input=b'120000 blob '+blob.encode()+b'\tlink\n').decode().strip()
        commit=self.obj('commit',b'tree '+tree.encode()+b'\nauthor T <t@e.invalid> 0 +0000\ncommitter T <t@e.invalid> 0 +0000\n\nlink\n')
        with self.assertRaisesRegex(m.Invalid,'unsupported'):m.collect(self.repo,commit)
    def commit_for_tree(self,tree):
        return self.obj('commit',b'tree '+tree.encode()+b'\nauthor T <t@e.invalid> 0 +0000\ncommitter T <t@e.invalid> 0 +0000\n\nfixture\n')
    def nested_commit(self):
        tree=self.git('mktree',input=b'040000 tree '+self.manifest['tree'].encode()+b'\tdir\n').decode().strip()
        return self.commit_for_tree(tree)
    def test_empty_root_allowed(self):
        tree=self.git('mktree',input=b'').decode().strip()
        self.assertEqual(m.collect(self.repo,self.commit_for_tree(tree))['files'],{})
    def test_empty_child_rejected_immediately(self):
        empty=self.git('mktree',input=b'').decode().strip()
        tree=self.git('mktree',input=b'040000 tree '+empty.encode()+b'\ta\n040000 tree '+empty.encode()+b'\tb\n').decode().strip()
        with self.assertRaisesRegex(m.Invalid,'empty subtree'):m.collect(self.repo,self.commit_for_tree(tree))
    def test_collect_and_reconstruct_depth_budget(self):
        commit=self.nested_commit();manifest=m.collect(self.repo,commit)
        with patch.object(m,'MAX_TREE_DEPTH',0):
            with self.assertRaisesRegex(m.Invalid,'depth'):m.collect(self.repo,commit)
            with self.assertRaisesRegex(m.Invalid,'depth'):m.verify_manifest(manifest)
    def test_collect_and_reconstruct_work_budget(self):
        commit=self.nested_commit();manifest=m.collect(self.repo,commit)
        with patch.object(m,'MAX_TREE_VISITS',1):
            with self.assertRaisesRegex(m.Invalid,'work'):m.collect(self.repo,commit)
            with self.assertRaisesRegex(m.Invalid,'work'):m.verify_manifest(manifest)
    def test_collect_and_reconstruct_byte_budget(self):
        with patch.object(m,'MAX_TREE_BYTES',1):
            with self.assertRaises(m.Invalid):m.collect(self.repo,self.commit)
            with self.assertRaisesRegex(m.Invalid,'byte budget'):m.verify_manifest(self.manifest)
    def test_exact_decoded_commit_limit(self):
        raw=base64.b64decode(self.manifest['commit_raw_base64'])
        raw+=b'x'*(m.MAX_COMMIT+1-len(raw))
        self.manifest['commit_raw_base64']=base64.b64encode(raw).decode()
        self.manifest['commit']=m.object_hash('commit',raw,'sha1')
        with self.assertRaisesRegex(m.Invalid,'decoded commit too large'):m.verify_manifest(self.manifest)

if __name__=='__main__':unittest.main(verbosity=2)
