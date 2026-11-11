import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fetch',HERE/'overlay/scripts/fetch_lean_cache.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class RetryTests(unittest.TestCase):
 def exercise(self,results):
  calls=[];sleeps=[];output=[]
  def run(cmd,**kw):
   calls.append((cmd,kw));return SimpleNamespace(returncode=results[len(calls)-1][0],stdout=results[len(calls)-1][1])
  code=m.fetch(run=run,sleep=sleeps.append,emit=output.append)
  for cmd,kw in calls:
   self.assertEqual(cmd,['lake','exe','cache','get']);self.assertEqual(kw['cwd'],m.ROOT/'lean')
  return code,calls,sleeps,output
 def test_success_once(self):
  code,calls,sleeps,_=self.exercise([(0,'done')]);self.assertEqual(code,0);self.assertEqual(len(calls),1);self.assertFalse(sleeps)
 def test_504_then_success(self):
  code,calls,sleeps,_=self.exercise([(1,'error: could not download file\nhttp request returned an unsuccessful status code: 504'),(0,'done')]);self.assertEqual(code,0);self.assertEqual(len(calls),2);self.assertEqual(sleeps,[2])
 def test_bounded_preserves_last_exit(self):
  text='downloading file\nHTTP Error 503: unavailable'
  code,calls,sleeps,_=self.exercise([(1,text),(2,text),(17,text)]);self.assertEqual(code,17);self.assertEqual(len(calls),3);self.assertEqual(sleeps,[2,4])
 def test_each_explicit_transient(self):
  for code in [408,429,500,502,503,504]:self.assertTrue(m.transient_download('curl: (22) The requested URL returned error: '+str(code)))
 def test_permanent_and_nondownload_do_not_retry(self):
  for text in ['could not download file: HTTP Error 404','could not download file: HTTP Error 403','HTTP Error 504','ordinary proof failed','network timeout']:
   code,calls,sleeps,_=self.exercise([(7,text)]);self.assertEqual(code,7);self.assertEqual(len(calls),1);self.assertFalse(sleeps)
 def test_build_errors_override_network_text(self):
  for tail in ['Main.lean:10:2: error: unsolved goals','error: build failed','build failed']:
   self.assertFalse(m.transient_download('downloading file HTTP Error 504\n'+tail))
 def test_integrity_overrides_prior_transient(self):
  for tail in ['checksum mismatch','SHA256 verification failed','hash mismatch','integrity check failed']:
   code,calls,sleeps,_=self.exercise([(23,'downloading file HTTP Error 504\n'+tail)])
   self.assertEqual(code,23);self.assertEqual(len(calls),1);self.assertFalse(sleeps)
 def test_compiler_overrides_prior_transient(self):
  for tail in ['error: unknown constant x','error: Lean exited with code 1','compilation failed','tactic simp failed','type mismatch']:
   code,calls,sleeps,_=self.exercise([(31,'downloading file HTTP Error 504\n'+tail)])
   self.assertEqual(code,31);self.assertEqual(len(calls),1);self.assertFalse(sleeps)
 def test_output_preserved(self):
  code,calls,sleeps,out=self.exercise([(9,'failure text\n')]);self.assertEqual(out,['failure text\n'])
 def test_no_exception_retry(self):
  calls=[]
  def bad(*args,**kwargs):calls.append(1);raise FileNotFoundError('lake missing')
  with self.assertRaises(FileNotFoundError):m.fetch(run=bad,sleep=lambda _:self.fail('slept'),emit=lambda _:None)
  self.assertEqual(calls,[1])
if __name__=='__main__':unittest.main()
