from pathlib import Path
import json, hashlib, datetime

HERE=Path(__file__).resolve().parent
RISK=HERE.parent
BASE=RISK.parent.parent
REPO=BASE/'work/quartic-v14-release/preview-repository'
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
division=read(RISK/'v14-division-polynomial-edit-proposal-001/EDITS.json')
catalogue=read(RISK/'v14-elementary-published-replacements-root-001/CATALOGUE-EDIT.json')
qroot=read(RISK/'v14-qroot2-class-unit-proof-002/EDIT-PROPOSAL.json')
twist=read(RISK/'v14-local-twist-application-002/CALLER-CLARIFICATION.json')
note_path=division['target']
main_path='manuscripts/quartic_v14.tex'
old_note=(REPO/note_path).read_bytes()
old_main=(REPO/main_path).read_bytes()
assert sha(old_note)==division['base_sha256']==qroot['base_sha256']
assert sha(old_main)==twist['source_sha256']
note_lines=old_note.decode('utf-8').splitlines(keepends=True)
scope_old=note_lines[3].rstrip('\r\n')
scope_new=('This note supplies only the elementary connections assigned to A055–A058. '
           'Its original review target was the main manuscript with SHA256 '
           +sha(old_main)+'. Source replacements and current manuscript bindings are recorded '
           'in the Version 14 review evidence; this note does not itself claim whole-proof acceptance. '
           'Historical closure-batch-001/002/010 are retained as author derivations, not relabelled '
           'independent acceptances. Generator finite enumeration, rank/torsion, height saturation, '
           'local duplication, formal groups, reduction, Hasse bounds and the M0 construction '
           'remain separately supplied.')
note_changes=[{'line':4,'old':scope_old,'new':scope_new}]+division['changes']+catalogue['edits']+[
 {'line':qroot['line'],'old':qroot['old'],'new':qroot['new'].replace('Reducing a positive unit','Reducing a unit positive at the real embedding s>0')}]

def edit_lines(raw, changes):
    lines=raw.decode('utf-8').splitlines(keepends=True)
    for c in changes:
        a=c.get('start_line',c.get('line')); b=c.get('end_line',a)
        current=''.join(lines[a-1:b])
        assert current.replace('\r\n','\n').rstrip('\n')==c['old'].replace('\r\n','\n').rstrip('\n'), (a,b,'unexpected base')
        ending='\r\n' if lines[a-1].endswith('\r\n') else '\n'
        replacement=c['new'].replace('\r\n','\n').rstrip('\n').split('\n')
        assert len(replacement)==b-a+1
        lines[a-1:b]=[s+ending for s in replacement]
    return ''.join(lines).encode('utf-8')

main_changes=[qroot['main_edit'],{'start_line':twist['start_line'],'end_line':twist['end_line'],'old':twist['old'],'new':twist['proposed']}]
edits=[]
for path, raw, changes in [(note_path,old_note,note_changes),(main_path,old_main,main_changes)]:
    new=edit_lines(raw,changes)
    for folder,data in [('before',raw),('candidate',new)]:
        dest=HERE/folder/path
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(data)
    edits.append({'path':path,'before_sha256':sha(raw),'after_sha256':sha(new),
                  'before_lines':len(raw.splitlines()),'after_lines':len(new.splitlines()),'changes':changes})

record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'author':'/root','scope':'Grouped accepted source replacements and local-generator clarification; no release acceptance',
        'edits':edits,'unchanged_outside_listed_lines':True,
        'prior_reviews':[
          'v14-division-polynomial-edit-proposal-001/REVIEWER-EDIT-REVIEW.json',
          'v14-catalogue-published-replacement-review-gi-001/REVIEW.md',
          'v14-qroot2-class-unit-proof-002/REVIEWER-RECONCILIATION-REVIEW.json',
          'v14-qroot2-class-unit-proof-003/REVIEWER-COMPONENT-REVIEW.json',
          'v14-local-twist-review-arithmetic-001/APPLICATION002-REVIEW.json'],
        'new_review_scope':['Scope line labels original manuscript hash as historical, not current.',
          'Quadratic unit reduction explicitly means positive at the embedding s>0; original proof says this.',
          'Exact main344–346 adoption of accepted norm-Euclidean/class/unit argument.',
          'Exact main13668–13669 states the minimal differential or dual convention required by the accepted application.',
          'Composition of previously accepted disjoint replacements; full post-edit source transport remains separate.']}
(HERE/'PROPOSAL.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'proposal_sha256':sha((HERE/'PROPOSAL.json').read_bytes()),'files':[{k:e[k] for k in ('path','before_sha256','after_sha256')} for e in edits]}))
