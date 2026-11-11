import json,hashlib
from pathlib import Path
R=Path('work/source-risk-review-20261107')
O=R/'v14-cj-normalizer-source-reconciliation-001'
I=R/'v14-final-composite-review-001/cj-level-normalizer-source-initial-001'
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(n,x): (O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
uses=json.loads((I/'INITIAL-SOURCE-USES.json').read_text())['uses']
ps=json.loads((I/'INITIAL-PASSAGES.json').read_text())
raw=(R/'v14-cj-level-normalizer-author-001/overlay/research/version14/evidence/cj-level-normalizer-001/PROOF.md').read_bytes()
roles=['conditional_model_and_domain','local_matrix_derivation','local_projector_derivation','conditional_character_calculation','scope_boundary']
reasons=[
 'The local model and cyclic line are the explicit domain of this conditional lemma. Their realization by the actual global geometric correspondence is not asserted and remains a caller obligation.',
 'Direct multiplication of the displayed matrices proves determinant, square and conjugation formulas. No outgoing normalizer result is imported as its own premise.',
 'Within the stated support, the explicit integral complementary projectors have trace one and diagonal residues one and zero. The preceding conjugation formula exchanges these residues. This proves selected-root reversal without identifying dyadic roots merely by their residues.',
 'Multiplicativity gives alpha(-r)/alpha(r)=alpha(-1); the displayed parity is a stipulated character choice. Unramifiedness makes a character depend only on the norm valuation e. Neither stipulated parity nor unramifiedness is proved by this calculation.',
 'Explicit limitation of the result. It does not prove any of the separate global geometric, character-choice or newform assertions.'
]
requirements=[
 ['Actual split Eichler model and cyclic line; geometric identification of its normalizer at any global caller.'],
 [],
 ['Actual split-unit support and selected eigenline; at two, (1+x)/2 belongs to R and r is odd.'],
 ['Prescribed root character with the stated parity; unramified norm character; separate actual modular eigen-action.'],
 ['Global adelic/geometric correspondence identification and actual character choices remain separate.']
]
rows=[]
for u,p,role,reason,req in zip(uses,ps,roles,reasons,requirements):
 loc=p['location']; assert sha(raw)==loc['pin']['sha256']
 assert sha(b''.join(raw.splitlines(keepends=True)[loc['start_line']-1:loc['end_line']]))==loc['excerpt_sha256']
 rows.append(dict(initial_use_id=u['id'],initial_use_sha256=sha(json.dumps(u,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()),classification=u['classification'],location=loc,source_role=role,incoming_use_ids=[],no_imports_reason=reason,outgoing_provenance_use_ids=['ACTIVE-CJ-SPLIT-LEVEL-NORMALIZER'] if role!='scope_boundary' else [],caller_requirements=req))
dump('RECONCILIATION.json',dict(initial_source_uses_sha256=sha((I/'INITIAL-SOURCE-USES.json').read_bytes()),initial_passages_sha256=sha((I/'INITIAL-PASSAGES.json').read_bytes()),rows=rows,scope='Conditional source-level local calculation only; no global caller premise is discharged by this reconciliation.'))
dump('CHECKS.json',dict(initial_rows=5,raw_locations=5,all_pass=True))
dump('PENDING.json',dict(global_caller_obligations=['Identify the actual geometric Atkin-Lehner operation with the supplied local matrix action.','Bind actual split support, character parity and unramifiedness at the relevant caller.'],not_claimed='No new global eigen-action or geometric theorem.'))
dump('MANIFEST.json',dict(files={p.name:dict(sha256=sha(p.read_bytes()),bytes=p.stat().st_size) for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}))
print(sha((O/'MANIFEST.json').read_bytes()))
