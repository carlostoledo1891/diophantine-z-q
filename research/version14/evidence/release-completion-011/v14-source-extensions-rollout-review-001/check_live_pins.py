import pathlib,sys,json
from unittest.mock import patch
sys.path.insert(0,sys.argv[1])
import live_protocol_context as a, live_protocol_context_forks as b
results=[]
for m in (a,b):
 m.verify_dependencies()
 for name in ('coverage_gate.py','connections_gate.py'):
  original=pathlib.Path.read_bytes
  def changed(p):
   data=original(p)
   return data+b'\n# changed' if p.name==name else data
  rejected=False
  with patch.object(pathlib.Path,'read_bytes',changed):
   try: m.verify_dependencies()
   except Exception as e:
    rejected='dependency pin changed' in str(e)
  assert rejected,(m.__name__,name)
  results.append(dict(module=m.__name__,tampered=name,rejected=rejected))
print(json.dumps(results))
