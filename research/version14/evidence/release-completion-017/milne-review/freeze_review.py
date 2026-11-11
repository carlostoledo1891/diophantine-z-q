"""Freeze the reviewer's written decisions; no mathematical decision is inferred by code."""
from pathlib import Path
import json
import hashlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def pin(p):
    p = Path(p)
    b = p.read_bytes()
    return {'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def write(name, value):
    (HERE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf8')

target = ROOT/'work/source-risk-review-20261107/milne-author-r3/MANIFEST.json'
assert pin(target)['sha256'] == '9b975f6059c97ac83e5455a2b9707736fca4d886ca94789de3525e88a7fa4c12'
manuscript = ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
assert pin(manuscript)['sha256'] == '81d421af9dedd0d975024c9d0ff1b1d11249b7b36f2c9215bd2c80278f4934fc'
for name in ['SOURCE-PINS.json','ERRATA-APPLICABILITY.json','FINDINGS.json','OCCURRENCES.json','CHECKS.json']:
    json.loads((HERE/name).read_bytes())
write('DECISION.json',{
    'schema':'bounded-independent-source-decision/v1',
    'reviewer':'/root/astra_quartic_opt05_anchor',
    'author':'/root/sol_protocol_final_review',
    'date':'2026-11-07',
    'target':pin(target),
    'manuscript':pin(manuscript),
    'decision':'accepted within the exact bounded source and correction scopes in REVIEW.md',
    'report':pin(HERE/'REVIEW.md'),
    'findings':pin(HERE/'FINDINGS.json'),
    'accepted_brauer_fragment':pin(ROOT/'work/source-risk-review-20261107/milne-author-r3/PROPOSED-BRAUER.tex'),
    'accepted_scopes':['Constant-coefficient Brauer obstruction and exact citation replacement','Finite-place Kummer orthogonality and the written derived local comparison','Finite-Sha isogeny arithmetic signs, dyadic and real conventions, with inherited forward and component inputs retained','Global and local residual dimension formulas','Listed current repetitions and exact full-addendum applicability','R3 corrections of M01/M02/M03 with predecessors preserved'],
    'excluded_scopes':['Whole manuscript or whole source book','Separate Nekovar global Selmer transport and limits','Independent forward-finiteness and Edixhoven/Poonen-Stoll source acceptance','Manuscript installation, current registry, live gate receipt, or release authorization'],
    'unresolved_findings_in_this_bounded_target':[],
    'history':'R1 false one-page completeness claim and R2 source-domain/transitive omissions remain preserved; their exact current corrections are accepted only on R3.',
    'authorship_disclosure':'Reviewer identified missing source connections and checked the existing official repair. No replacement mathematical theorem was jointly authored. This unsigned record is not provider or gate authentication.'
})
names = ['README.md','REVIEW.md','DECISION.json','FINDINGS.json','ERRATA-APPLICABILITY.json','SOURCE-PINS.json','OCCURRENCES.json','CHECKS.json','review_checks.py','freeze_review.py','inspect_sources.py','current-consumers.txt']
write('MANIFEST.json',{'schema':'bounded-independent-source-review-freeze/v1','reviewer':'/root/astra_quartic_opt05_anchor','target':pin(target),'scope':'Exact Milne-ADT applications and their listed repetitions on manuscript81d421; source-only evidence; no whole-release approval','files':[pin(HERE/n) for n in names],'excluded':['local-only/ primary PDFs, full source text extractions and page images'],'private_material':'No private conversation or personal assessment included.'})
print(json.dumps({name:pin(HERE/name)['sha256'] for name in ['REVIEW.md','DECISION.json','CHECKS.json','MANIFEST.json']},indent=2))
