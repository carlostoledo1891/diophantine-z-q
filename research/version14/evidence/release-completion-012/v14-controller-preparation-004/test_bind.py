import importlib.util,json,tempfile,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('binder',Path(__file__).with_name('bind.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class RefusalTests(unittest.TestCase):
 def test_duplicate_json(self):
  with self.assertRaises(ValueError):m.decode(b'{"x":1,"x":2}')
 def test_nonfinite_json(self):
  with self.assertRaises(ValueError):m.decode(b'{"x":NaN}')
 def test_unbound_nested(self):
  with self.assertRaises(ValueError):m.resolved({'x':[{'$required':'real observation'}]})
 def test_exact_pin(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/'a').write_bytes(b'actual bytes')
   self.assertEqual(m.pin(p,{'path':'a','sha256':m.sha(b'actual bytes'),'bytes':12}),b'actual bytes')
   with self.assertRaises(ValueError):m.pin(p,{'path':'a','sha256':'0'*64,'bytes':12})
 def test_path_escape(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ValueError):m.pin(Path(d),{'path':'../secret','sha256':'0'*64,'bytes':1})
 def test_finding_inventory_is_json(self):
  import ast
  tree=ast.parse(Path(m.__file__).read_text(encoding='utf8'))
  assignment=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='values' for t in n.targets))
  expression=ast.Expression(assignment.value);ast.fix_missing_locations(expression)
  result=eval(compile(expression,'finding-inventory-regression','eval'),{'decode':m.decode,'source':{'finding_inventory':b'[{"id":"regression-only","body_sha256":"not-a-gate-fixture"}]','scope_review':b'original scope prose','policy_review':b'original policy prose','observation_provenance':b'original capture provenance'}})
  self.assertEqual(result,{'finding_inventory':[{'id':'regression-only','body_sha256':'not-a-gate-fixture'}]})
if __name__=='__main__':unittest.main()
