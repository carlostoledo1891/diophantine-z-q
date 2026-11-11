import base64
import copy
import hashlib
import unittest
from git_state import GitState, Invalid, Conflict, Snapshot, canonical, object_id


class FakeGitHub:
    def __init__(self):
        self.blobs={}; self.trees={}; self.commits={}; self.ref=None
        self.private=True; self.race=False; self.truncated=False; self.writes=[]
        index={'schema':1,'generation':0,'parent':None,'files':{},'checkpoints':{}}
        raw=canonical(index); b=self.add_blob(raw)
        t=self.add_tree({'state/index.json':b}); self.ref=self.add_commit(t,[])

    def add_blob(self,raw):
        key=object_id('blob',raw);self.blobs[key]=raw;return key

    def add_tree(self,files):
        key=hashlib.sha1(canonical(files)).hexdigest();self.trees[key]=dict(files);return key

    def add_commit(self,tree,parents):
        key=hashlib.sha1(canonical([tree,parents])).hexdigest()
        self.commits[key]={'sha':key,'tree':{'sha':tree},'parents':[{'sha':x} for x in parents]}
        return key

    def request(self,method,path,data=None):
        tail=path.removeprefix('/repos/owner/controller')
        if method!='GET':self.writes.append((method,tail,copy.deepcopy(data)))
        if tail=='':return {'id':42,'full_name':'owner/controller','private':self.private}
        if tail=='/git/ref/heads/protocol-state':return {'ref':'refs/heads/protocol-state','object':{'type':'commit','sha':self.ref}}
        if tail.startswith('/git/commits/'):
            return copy.deepcopy(self.commits[tail.rsplit('/',1)[-1]])
        if tail.startswith('/git/trees/'):
            sha=tail.rsplit('/',1)[-1].split('?')[0]
            return {'sha':sha,'truncated':self.truncated,'tree':[{'path':p,'sha':s,'mode':'100644','type':'blob'} for p,s in self.trees[sha].items()]}
        if tail.startswith('/git/blobs/'):
            sha=tail.rsplit('/',1)[-1];raw=self.blobs[sha]
            return {'sha':sha,'size':len(raw),'encoding':'base64','content':base64.b64encode(raw).decode()}
        if method=='POST' and tail=='/git/blobs':
            return {'sha':self.add_blob(base64.b64decode(data['content']))}
        if method=='POST' and tail=='/git/trees':
            files=dict(self.trees[data['base_tree']])
            for item in data['tree']:files[item['path']]=item['sha']
            return {'sha':self.add_tree(files)}
        if method=='POST' and tail=='/git/commits':
            sha=self.add_commit(data['tree'],data['parents']);return copy.deepcopy(self.commits[sha])
        if method=='PATCH' and tail=='/git/refs/heads/protocol-state':
            assert data['force'] is False
            if self.race:
                current=self.commits[self.ref]
                self.ref=self.add_commit(current['tree']['sha'],[self.ref])
            if self.commits[data['sha']]['parents']!=[{'sha':self.ref}]:
                raise Conflict('fake server rejected non-fast-forward update')
            self.ref=data['sha'];return {'object':{'sha':self.ref}}
        raise AssertionError((method,path))


class TestState(unittest.TestCase):
    def setUp(self):
        self.api=FakeGitHub();self.store=GitState(self.api,'owner/controller',42)

    def test_roundtrip_append(self):
        old=self.store.load();path='state/entries/operator/0000000001.json'
        commit=self.store.append(old,{path:b'{"signed":"entry"}'},{'operator':'checkpoint'})
        new=self.store.load()
        self.assertEqual(new.commit,commit);self.assertEqual(new.index['generation'],1)
        self.assertEqual(new.entries[path],b'{"signed":"entry"}')
        self.assertEqual(new.index['parent'],old.commit)

    def test_stale_snapshot(self):
        old=self.store.load();self.store.append(old,{}, {'n':1})
        with self.assertRaises(Conflict):self.store.append(old,{}, {'n':2})

    def test_immutable_entries(self):
        path='state/entries/intake/0000000001.json'
        self.store.append(self.store.load(),{path:b'a'}, {})
        with self.assertRaises(Invalid):self.store.append(self.store.load(),{path:b'b'}, {})

    def test_identity_and_privacy(self):
        with self.assertRaises(Invalid):GitState(self.api,'owner/controller',43).load()
        self.api.private=False
        with self.assertRaises(Invalid):self.store.load()

    def test_truncated_tree(self):
        self.api.truncated=True
        with self.assertRaises(Invalid):self.store.load()

    def test_raw_blob_tamper(self):
        old=self.store.load();sha=self.api.trees[old.tree]['state/index.json']
        self.api.blobs[sha]+=b' '
        with self.assertRaises(Invalid):self.store.load()

    def test_racing_sibling_never_overwritten(self):
        old=self.store.load();self.api.race=True
        with self.assertRaises(Conflict):self.store.append(old,{}, {'n':1})
        self.assertNotEqual(self.api.ref,old.commit)
        self.assertEqual(self.api.commits[self.api.ref]['tree']['sha'],old.tree)

    def test_paths_restricted(self):
        old=self.store.load()
        for path in ('../secret','state/entries/operator/../key.json','state/index.json','.github/workflows/pwn.yml'):
            with self.subTest(path=path),self.assertRaises(Invalid):
                self.store.append(old,{path:b'a'}, {})

    def test_identical_entry_can_be_repeated(self):
        path='state/entries/operator/0000000001.json'
        self.store.append(self.store.load(),{path:b'a'}, {})
        snap=self.store.load();self.store.append(snap,{path:b'a'}, {'n':2})
        self.assertEqual(self.store.load().entries,{path:b'a'})

    def test_mutated_snapshot_cannot_replace_history(self):
        path='state/entries/operator/0000000001.json'
        self.store.append(self.store.load(),{path:b'a'}, {})
        snap=self.store.load();del snap.entries[path]
        with self.assertRaises(Invalid):self.store.append(snap,{path:b'b'}, {})
        self.assertEqual(self.store.load().entries[path],b'a')

    def test_constructed_snapshot_cannot_delete_history(self):
        path='state/entries/operator/0000000001.json'
        empty=self.store.load();self.store.append(empty,{path:b'a'}, {})
        current=self.store.load()
        forged=Snapshot(current.commit,empty.tree,empty.index,{})
        self.store.append(forged,{}, {})
        self.assertEqual(self.store.load().entries[path],b'a')

    def test_float_repository_identity_rejected(self):
        original=self.api.request
        def altered(method,path,data=None):
            value=original(method,path,data)
            if path=='/repos/owner/controller':value['id']=42.0
            return value
        self.api.request=altered
        with self.assertRaises(Invalid):self.store.load()


if __name__=='__main__':unittest.main()
