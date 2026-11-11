from pathlib import Path
import json, hashlib, re, difflib
from datetime import datetime, timezone

H = Path(__file__).resolve().parent
R = H.parents[2]
def sha(raw): return hashlib.sha256(raw).hexdigest()
def write_once(path, raw):
    if path.exists():
        assert path.read_bytes() == raw, str(path)
    else:
        path.write_bytes(raw)
def jsonbytes(value): return (json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode()
base = R/'work/quartic-version6-release/repository/manuscripts/quartic_v13.tex'
current = R/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
addition = H.parent/'addition-layout-v2.tex'
edits = R/'work/quartic-v14-release/preview-repository/docs/manuscript-revisions/version14/new-edits.json'
assert sha(base.read_bytes()) == '9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd'
assert sha(current.read_bytes()) == 'b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d'
assert sha(addition.read_bytes()) == 'b5840b3598c655fc7f3db3475b089b65800b98f136a601c4360c72d22d6f95a0'
expected=base.read_text()
es=json.loads(edits.read_bytes())
assert [e['id'] for e in es] == ['v14-title','v14-abstract','v14-introduction','v14-proof-addition']
assert es[-1]['new'] == addition.read_text()+'\n\\begin{thebibliography}{99}'
for e in es:
    assert expected.count(e['old']) == 1
    expected=expected.replace(e['old'],e['new'])
assert expected == current.read_text()
a=base.read_text().splitlines(); b=current.read_text().splitlines()
ops=difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes()
changes=[(tag,i+1,j,k+1,l) for tag,i,j,k,l in ops if tag!='equal']
assert changes[:3] == [('replace',39,39,39,39),('replace',52,56,52,56),('replace',122,127,122,127)]
assert len(changes)==4 and changes[3][0:3]==('insert',21633,21632)
offset=len(b)-len(a)
assert b[21632:21632+len(addition.read_text().splitlines())] == addition.read_text().splitlines()
assert b[127:21632] == a[127:21632]
assert b[21632+offset:] == a[21632:]
pin={'side':'head','path':'manuscripts/quartic_v14.tex','sha256':sha(current.read_bytes())}
rawlines=current.read_bytes().splitlines(keepends=True)
def location(start,end):
    return {'pin':pin,'start_line':start,'end_line':end,'excerpt_sha256':sha(b''.join(rawlines[start-1:end]))}

notes=(H/'WHOLE-INITIAL-SOURCE-USES.md').read_text(encoding='utf-8')
uses=[]; passages=[]; batch=None
fields=['objects','hypotheses','quantifiers','parameter_range','uniformity','constants','normalizations','exceptional_cases','limit_order']
def initial_use(uid,pid,statement,conditions,phase,kind='dependency'):
    assertion={'statement':statement,'objects':'The actual mathematical objects named in this source-derived statement; no substitution by inventory labels has been made.',
        'hypotheses':conditions}
    for key in fields:
        if key not in assertion:
            assertion[key]='Initial notes preserve this dimension in the statement and conditions without a separate field extraction. It remains to be separated and checked against the pinned source during reconciliation; this initial row is not an acceptance.'
    uses.append({'id':uid,'consumer':'source-local:'+uid,'passages':[pid], 'assertion':assertion,
        'classification':kind,'reason':phase+' The supplier and ordinary application identity remain unresolved in this source-first schema projection.',
        'shared_contract_justification':None,'supplier':None,'application_id':None,'inline_argument':None})
for line in notes.splitlines():
    match=re.match(r'^#{2,3} .*?(\d+)–(\d+)',line)
    if match:
        batch=tuple(map(int,match.groups()))
        pid='initial-baseline-%d-%d'%batch
        passages.append({'id':pid,'location':location(*batch),'reason':'Direct sequential reading batch; individual initial rows are observations within this batch, not assertions that each occupies every line.'})
    if re.match(r'^\| B\d+ \|',line):
        pieces=line.split('|')
        uid=pieces[1].strip(); statement=pieces[2].strip(); conditions='|'.join(pieces[3:-1]).strip()
        initial_use(uid,pid,statement,conditions,'Expanded personal direct-source reconstruction after the limited V13/V14 review, before final inventories or other slice reports.')
assert len(uses)==220
tail=json.loads((H/'BASELINE-COVERAGE.json').read_bytes())['coverage']
for i,row in enumerate(tail,1):
    lo,hi=row['start_line'],row['end_line']
    shift=offset if lo>=21633 else 0
    pid='initial-tail-%d-%d'%(lo,hi)
    passages.append({'id':pid,'location':location(lo+shift,hi+shift),'reason':'Earlier personally read baseline tail, mapped through exact unchanged-source comparison. This portion was already compared with its limited inventory before the whole-source task.'})
    initial_use('T%02d'%i,pid,row['reviewer_argument'],'Retain the hypotheses and exposure qualifications stated in this earlier source-derived review.',
       'Earlier limited review, already reconciled before whole-source expansion; no claim of new blind reconstruction.',
       'background' if lo>=21633 else 'dependency')
old=(H/'INITIAL-SOURCE-USES.md').read_text(encoding='utf-8')
items=re.findall(r'(?ms)^(\d+)\. (.*?)(?=^\d+\. |^Initial disposition:|\Z)',old)
assert len(items)==16
pid='initial-addition-complete'
passages.append({'id':pid,'location':location(21633,21632+len(addition.read_text().splitlines())),'reason':'Entire final addition. Original sixteen discovery rows arose from earlier proof sources and a partial draft; full-draft review followed. These are broad obligation records, not invented precise initial locations.'})
for i,text in items:
    initial_use('N%02d'%int(i),pid,text.strip(),'All explicit guards, exceptional cases, order of choices and numerical constants in the recorded obligation remain part of the requested assertion.',
       'Original limited source-first sixteen-obligation record, subsequently checked against the complete addition and limited route inventory before whole-source expansion.')
initial={'schema':'protocol-source-first/v1','sources':[pin],'uses':uses}
write_once(H/'WHOLE-INITIAL-SOURCE-USES.frozen.md',notes.encode())
write_once(H/'whole-initial.json',jsonbytes(initial))
write_once(H/'whole-initial-passages.json',jsonbytes({'source':pin,'passages':passages}))
write_once(H/'quartic_v14.initial-frozen.tex',current.read_bytes())
assembly={'status':'PASS exact current assembly','source':pin,'baseline_sha256':sha(base.read_bytes()),'addition_sha256':sha(addition.read_bytes()),
 'edits_sha256':sha(edits.read_bytes()),'changes':changes,'baseline_lines':len(a),'current_lines':len(b),'bibliography_shift':offset,
 'limit':'Mathematical source comparison, not PDF visual inspection or whole-proof acceptance.'}
write_once(H/'ASSEMBLY-CHECKS-layout-v2.json',jsonbytes(assembly))
stamp={'run_id':'/root/astra_v14_source_review','frozen_at':datetime.now(timezone.utc).isoformat(),
 'source':pin,'initial_sha256':sha((H/'whole-initial.json').read_bytes()),'notes_sha256':sha((H/'WHOLE-INITIAL-SOURCE-USES.frozen.md').read_bytes()),
 'passages_sha256':sha((H/'whole-initial-passages.json').read_bytes()),'use_count':len(uses),
 'method':'Personal sequential reading of every baseline line, earlier personal complete addition review, exact assembly comparison and honest source-local schema projection. Original narrative and source bytes are preserved. Initial unresolved dimensions are explicitly marked, not asserted checked.',
 'prior_exposure':'Parent supplied targets, risk areas and lineage acceptance claims. Original sixteen-obligation record preceded limited V13 and R6 inventory reconciliation. Expanded baseline reconstruction then read the manuscript itself, including its application/input tables, after exposure to those limited inventories and favorable reports. No other baseline slice table or final whole-manuscript inventory was opened before this freeze. Parent messages disclosed final-inventory counts. The earlier tail/addition rows are preserved with their different chronology.',
 'limitations':'Whole inventory comparison and supplier matching remain pending. The source reading does not independently reprove every external publication. No synthetic receipt or authenticated acceptance is created. Initial batch locations are deliberately broad, with unresolved ordinary application labels and unseparated assertion dimensions to be resolved in the final table.'}
write_once(H/'WHOLE-INITIAL-FREEZE.json',jsonbytes(stamp))
print(json.dumps({'assembly':assembly,'freeze':stamp},indent=2))
