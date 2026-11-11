"""Reproduce the scoped review of the parent's exact title-classifier patch."""
import ast,hashlib,json,pathlib,re
H=pathlib.Path(__file__).resolve().parent
P=H.parents[1]/'quartic-version6-release/repository/scripts/check_application_reviews.py'
raw=P.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='581b74870e47069fd56f28755088733ba18aa3853540ad70bec0fa0a3c1a93e6'
tree=ast.parse(raw.decode())
functions=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='title_fragment']
assert len(functions)==1
namespace={'re':re}
exec(compile(ast.fix_missing_locations(ast.Module(body=functions,type_ignores=[])),str(P),'exec'),namespace)
cases={r'\large Version 1.':True,r'\large Version 12.':True,r'\large Version 13':True,r'\large Version 100':True,r'\large Version 0.':False,r'\large Version 01.':False,r'\large Version 12':False,r'\large Version 13.':False,r'\large Version 13 theorem':False,r'\large Version 13\input{evil}':False,'\\large Version 13\n':False,r'prefix\large Version 13':False}
for value,expected in cases.items():assert namespace['title_fragment'](value)==expected,value
print(json.dumps({'passed':True,'cases':len(cases),'source_sha256':hashlib.sha256(raw).hexdigest()},indent=2))
