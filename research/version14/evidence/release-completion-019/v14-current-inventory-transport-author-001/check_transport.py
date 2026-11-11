from pathlib import Path
import sys,runpy,json,importlib.util,copy
root=Path("C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-v14-release/preview-repository/")
here=Path(__file__).parent
target=root/'docs/manuscript-revisions/version14/APPLICATIONS.json'
replacement=(here/'overlay/docs/manuscript-revisions/version14/APPLICATIONS.json').read_bytes()
read=Path.read_bytes
def overlay_read(p):
 return replacement if p.resolve()==target.resolve() else read(p)
Path.read_bytes=overlay_read
sys.argv=[str(root/'docs/manuscript-revisions/version14/validate-applications.py'),'--repo',str(root),'--self-test']
try:runpy.run_path(sys.argv[0],run_name='__main__')
finally:Path.read_bytes=read
spec=importlib.util.spec_from_file_location('validator',root/'docs/manuscript-revisions/version14/validate-applications.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
inv=json.loads(replacement);schema=json.loads(read(root/'docs/manuscript-revisions/version14/validation-schema.json'))
cases=[]
x=copy.deepcopy(inv);x['manuscript']['sha256']='0'*64;cases.append(('stale main',x,{}))
x=copy.deepcopy(inv);x['applications'][0]['dependencyDisposition']['required_inputs']['consumerSpans'][0]['start_line']+=1;cases.append(('shifted span',x,{}))
x=copy.deepcopy(inv);x['applications'][0]['dependencyDisposition']['required_inputs']['consumerSpans'][0]['sha256_raw_utf8_span']='0'*64;cases.append(('changed span digest',x,{}))
addpath=inv['addition']['path'];cases.append(('changed addition',inv,{addpath:read(root/addpath)+b'changed'}))
mainpath=inv['manuscript']['path'];cases.append(('changed main bytes',inv,{mainpath:read(root/mainpath)+b'changed'}))
for label,value,overlay in cases:
 try:m.validate(value,schema,m.Files(root,overlay))
 except (m.Invalid,KeyError):pass
 else:raise AssertionError('Negative passed: '+label)
print(json.dumps({'extra_negative_controls':len(cases),'result':'pass'}))
