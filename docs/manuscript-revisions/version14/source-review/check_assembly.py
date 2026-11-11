from pathlib import Path
import json,hashlib,difflib,copy
H=Path(__file__).resolve().parent
ROOT=H.parents[2]
base=ROOT/'work/quartic-version6-release/repository/manuscripts/quartic_v13.tex'
preview=ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
addition=H.parent/'addition.tex'
edits=ROOT/'work/quartic-v14-release/preview-repository/docs/manuscript-revisions/version14/new-edits.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(base)=='9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd'
assert sha(addition)=='6feff3f223c8363847da846706db313e1b7ca0fe2ddd6cbed1307fb944f7d87f'
assert sha(preview)=='200a2af2b33bcca5a214f049225add3b928e7b570657e5d59fc7308805c37e3b'
baseline=base.read_text();actual=preview.read_text();newproof=addition.read_text()
es=json.loads(edits.read_bytes())
assert [e['id'] for e in es]==['v14-title','v14-abstract','v14-introduction','v14-proof-addition']
assert es[-1]['new']==newproof+'\n\\begin{thebibliography}{99}'
constructed=baseline
for e in es:
    assert constructed.count(e['old'])==1
    constructed=constructed.replace(e['old'],e['new'])
assert constructed==actual
a=baseline.splitlines();b=actual.splitlines()
ops=[(tag,i+1,j,k+1,l) for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes() if tag!='equal']
assert ops==[('replace',39,39,39,39),('replace',52,56,52,56),('replace',122,127,122,127),('insert',21633,21632,21633,22587)]
assert b[21632:22586]==newproof.splitlines()
assert b[22586]==''
assert b[22587:]==a[21632:]
assert b[127:21632]==a[127:21632]
coverage=[]
for item in json.loads((H/'BASELINE-COVERAGE.json').read_bytes())['coverage']:
    r=copy.deepcopy(item)
    r['baseline_start_line']=r['start_line'];r['baseline_end_line']=r['end_line']
    shift=955 if r['start_line']>=21633 else 0
    r['start_line']+=shift;r['end_line']+=shift
    r['file']=str(preview.relative_to(ROOT));r['file_sha256']=sha(preview)
    r['raw_span_sha256']=hashlib.sha256(b''.join(preview.read_bytes().splitlines(keepends=True)[r['start_line']-1:r['end_line']])).hexdigest()
    coverage.append(r)
for item in json.loads((H/'V14-COVERAGE.json').read_bytes())['coverage']:
    r=copy.deepcopy(item);r['addition_start_line']=r['start_line'];r['addition_end_line']=r['end_line']
    r['start_line']+=21632;r['end_line']+=21632
    r['file']=str(preview.relative_to(ROOT));r['file_sha256']=sha(preview)
    r['raw_span_sha256']=hashlib.sha256(b''.join(preview.read_bytes().splitlines(keepends=True)[r['start_line']-1:r['end_line']])).hexdigest()
    coverage.append(r)
coverage.append({'file':str(preview.relative_to(ROOT)),'file_sha256':sha(preview),
    'start_line':22587,'end_line':22587,'status':'nonproof whitespace separator','reviewer_argument':'The added blank line separates the reviewed addition from the unchanged bibliography.'})
coverage.sort(key=lambda r:r['start_line'])
assert [i for r in coverage for i in range(r['start_line'],r['end_line']+1)]==list(range(20772,len(b)+1))
(H/'ASSEMBLED-COVERAGE.json').write_text(json.dumps({'reviewer':'/root/astra_v14_source_review','manuscript_sha256':sha(preview),'coverage':coverage,'range':[20772,len(b)],'scope':'This assigned partition plus the inserted Version14 section; other baseline partitions require their assigned reviewers.'},indent=2)+'\n')
result={'status':'PASS exact normalized-text assembly and reviewed mathematical incorporation',
    'baseline_sha256':sha(base),'addition_sha256':sha(addition),'manuscript_sha256':sha(preview),
    'edits_sha256':sha(edits),'text_changes':ops,'unchanged_old_math_body_lines':[128,21632],
    'unchanged_bibliography_and_AI_baseline_lines':[21633,22087],
    'inserted_addition_lines':[21633,22586],'assigned_assembled_coverage':[20772,len(b)],
    'limits':'No fresh whole-proof theorem acceptance or PDF visual inspection is inferred from this comparison. Final contract and release tree must match these reviewed source bytes.'}
(H/'ASSEMBLY-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
