from datetime import date
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import research_annex as annex
import package_v14
from release_common import sha


class AnnexTests(unittest.TestCase):
    def fixture(self,root,raw=b'research result\n'):
        (root/'note.txt').write_bytes(raw)
        row={'path':'work/note.txt','sha256':sha(raw),'bytes':len(raw),'category':'research','status':'historical'}
        manifest={'schema':'research-annex/v1','scope':'Synthetic fixture; no mathematical acceptance','files':[row],'unavailable':[]}
        return manifest,{sha(raw):'note.txt'}

    def test_exact_and_deduplicated_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root)
            m['files'].append(dict(m['files'][0],path='work/second-copy.txt'))
            result=annex.build(m,s,root,root/'out.zip',date(2026,11,7))
            self.assertEqual(result['logical_files'],2)
            self.assertEqual(result['unique_contents'],1)

    def test_only_exact_annex_path_is_allowed(self):
        package_v14.admissible(annex.ANNEX)
        self.assertIn(annex.ANNEX,package_v14.REQUIRED)
        with self.assertRaises(ValueError):package_v14.admissible('research/other.zip')

    def test_changed_source_fails_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root)
            (root/'note.txt').write_bytes(b'changed')
            with self.assertRaises(ValueError):annex.build(m,s,root,root/'out.zip',date(2026,11,7))
            self.assertFalse((root/'out.zip').exists())

    def test_unsafe_logical_names_and_duplicate_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            m,s=self.fixture(Path(tmp))
            for path in ('../escape','/absolute','.git/config','secrets/key.txt','notes/paper.pdf','nested.zip'):
                bad=copy.deepcopy(m);bad['files'][0]['path']=path
                with self.subTest(path=path),self.assertRaises(ValueError):annex.catalogue(bad)
            m['files'].append(m['files'][0])
            with self.assertRaises(ValueError):annex.catalogue(m)

    def test_extra_member_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root);out=root/'out.zip'
            annex.build(m,s,root,out,date(2026,11,7))
            with zipfile.ZipFile(out,'a') as z:z.writestr('extra.txt','unexpected')
            with self.assertRaises(ValueError):annex.validate(out.read_bytes())

    def test_key_marker_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root,(b'-----BEGIN ' + b'PRIVATE KEY-----'))
            with self.assertRaises(ValueError):annex.build(m,s,root,root/'out.zip',date(2026,11,7))

    def test_source_escape_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root)
            s[next(iter(s))]='../elsewhere'
            with self.assertRaises(ValueError):annex.build(m,s,root,root/'out.zip',date(2026,11,7))

    def test_deterministic_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,s=self.fixture(root)
            annex.build(m,s,root,root/'a.zip',date(2026,11,7))
            annex.build(m,s,root,root/'b.zip',date(2026,11,7))
            self.assertEqual((root/'a.zip').read_bytes(),(root/'b.zip').read_bytes())


if __name__=='__main__':unittest.main()
