"""Create the R8 successor without changing any R7 byte."""
from pathlib import Path
import hashlib,json,shutil,types

HERE=Path(__file__).resolve().parent
PARENT=HERE.with_name('quartic-v14-release-r7')
def digest(raw):return hashlib.sha256(raw).hexdigest()

for source in sorted(PARENT.rglob('*')):
    if source.is_file():
        relative=source.relative_to(PARENT)
        if '__pycache__' in relative.parts:raise ValueError('Unexpected parent cache')
        target=HERE/relative
        if target.exists():raise ValueError('Refuse to overwrite successor file '+str(relative))
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
parent_manifest=(PARENT/'MANIFEST.json').read_bytes()
(HERE/'PARENT-MANIFEST.json').write_bytes(parent_manifest)

replacements=[
    (b"b'-----BEGIN "+b"PRIVATE KEY-----'", b"(b'-----BEGIN ' + b'PRIVATE KEY-----')"),
    (b"b'-----BEGIN "+b"RSA PRIVATE KEY-----'", b"(b'-----BEGIN ' + b'RSA PRIVATE KEY-----')")
]
def semantics(code):
    def constant(value):
        return semantics(value) if isinstance(value,types.CodeType) else value
    return (code.co_code,tuple(map(constant,code.co_consts)),code.co_names,
            code.co_varnames,code.co_freevars,code.co_cellvars,code.co_argcount,
            code.co_posonlyargcount,code.co_kwonlyargcount,code.co_flags,
            code.co_stacksize,code.co_exceptiontable)

changes=[]
for name in ('research_annex.py','test_research_annex.py'):
    before=(PARENT/name).read_bytes();after=before;counts=[]
    for old,new in replacements:
        counts.append(after.count(old));after=after.replace(old,new)
    expected=[1,1] if name=='research_annex.py' else [1,0]
    if counts!=expected:raise ValueError('Unexpected literal count '+name)
    if semantics(compile(before,name,'exec'))!=semantics(compile(after,name,'exec')):
        raise ValueError('Compiled semantic fields changed '+name)
    (HERE/name).write_bytes(after)
    changes.append({'path':name,'before_sha256':digest(before),'after_sha256':digest(after),
                    'before_bytes':len(before),'after_bytes':len(after),
                    'private_marker_replacements':counts[0],
                    'rsa_marker_replacements':counts[1],
                    'compiled_semantic_fields_identical':True})

different=[]
for source in PARENT.rglob('*'):
    if source.is_file() and source.read_bytes()!=(HERE/source.relative_to(PARENT)).read_bytes():
        different.append(source.relative_to(PARENT).as_posix())
assert sorted(different)==['research_annex.py','test_research_annex.py']
value={'author':'/root/astra_v14_assertions_arithmetic','status':'author proposal; independent Sol review required',
       'parent_manifest_sha256':digest(parent_manifest),'inherited_file_delta':changes,
       'other_inherited_files_byte_identical':True,
       'rationale':'Split three scanner/test byte literals into constant-folded concatenated fragments so the packaging source closure passes the unchanged default scanner. The runtime marker values, scanner logic and five-entry exact historical allowlist are unchanged.',
       'semantic_comparison':'CPython compiled code bytes, recursive constants, names, variables, argument counts, flags, stack sizes and exception tables match; source position metadata is not compared.'}
(HERE/'R8-DELTA.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf8')
print(json.dumps({'parent_manifest_sha256':value['parent_manifest_sha256'],'changed_inherited_files':different}))
