from pathlib import Path
import json,hashlib

ROOT=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo')
REPO=ROOT/'work/quartic-version6-release/repository'
OUT=ROOT/'work/quartic-v14-prep/baseline-coverage/compiler'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda n,x:(OUT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
reports=[
 'docs/theorem-application-audit/FINDINGS.md',
 'docs/theorem-application-audit/applications.json',
 'docs/audit-history/PROTOCOL.md',
 'docs/degree8-original/README.md',
 'docs/degree8-original/research/accepted-h5/review/H5_FINAL_ACCEPTANCE.md',
 'docs/degree8-original/research/accepted-h5/review/GLOBAL_LEVEL_REVIEW.md',
 'docs/quartic-4973/README.md',
 'docs/quartic-4973/evidence/normalized_review.md',
 'docs/quartic-4973/evidence/linear_pole_review.md',
 'docs/quartic-962/README.md',
 'docs/quartic-962/evidence/work--quartic-version6-preparation--lower-bound--independent-review--REVIEW.md',
 'docs/audit-history/issue2/evidence/templates.md',
 'docs/audit-history/issue2/evidence/corollaries.md',
 'docs/manuscript-revisions/version10/README.md',
 'docs/manuscript-revisions/version10/new-applications.json',
 'docs/manuscript-revisions/version10/sources.json',
]
evidence=[dict(path=str(REPO/p),sha256=sha(REPO/p),role='Read historical argument or scope/source record after initial freeze; not independent primary proof merely because favorable') for p in reports]
for name in ['mazur-1995.pdf','page-02.png','page-03.png']:
 p=ROOT/'work/astra-mazur-corollary-001/primary'/name
 evidence.append(dict(path=str(p),sha256=sha(p),role='Published 1995 source; PDF hash verified, retained page images 165-166 directly viewed'))
for p in [REPO/'AGENTS.md',Path('C:/Users/glaze/Downloads/protocol-v1.3.md')]:
 evidence.append(dict(path=str(p),sha256=sha(p),role='Governing instructions read'))
write('CHECKED-EVIDENCE.json',evidence)
rec=json.loads((OUT/'RECONCILIATION.json').read_text(encoding='utf-8'))
validation=json.loads((OUT/'VALIDATION.json').read_text(encoding='utf-8'))
apps=sorted({a['id'] for row in rec['rows'] for a in row['existing_application_matches']})
write('DECISION.json',dict(
 schema='compiler-coverage-decision-v1',reviewer='/root/astra_v14_baseline_compiler',date='2026-11-07',
 source='work/quartic-version6-release/repository/manuscripts/quartic_v13.tex',
 source_sha256=validation['manuscript_sha256'],initial_sha256=validation['initial_sha256'],range=[5931,12193],
 disposition='coverage_complete_with_retained_and_cross_slice_dependencies',
 all_assigned_lines_read=True,all_lines_byte_indexed=True,unsupported_mathematical_inferences_identified=[],
 inherited_application_families=apps,inherited_application_family_count=len(apps),
 independent_reproof_of_all_sources=False,new_global_acceptance=False,
 cross_slice_join_required=True,cross_slice_edge_file='CROSS-SLICE-EDGES.json',
 finite_artifact_replay_this_review=False,
 preserved_qualifications=['Historical RC scope; upstream proof assigned elsewhere','Pan journal inaccessible; published Calegari bridge and inspected Pan author version','Yuan author-attested English translation; Chinese text not compared','Corrected Green-Tao source material','Exact height metric, Frobenius, diamond and twist conventions','Kollar author-source versus published typesetting distinction','Mazur 1992 attribution source not directly inspected; published 1995 statement directly viewed'],
 corrections_to_initial_inventory=['Add multiline Silverman citation at 8201-8202','Add multiline Diamond-Im citation at 8966-8967'],
 validation_file='VALIDATION.json',findings_file='FINDINGS.md'))
manifest=[dict(path=p.name,sha256=sha(p),bytes=p.stat().st_size) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='ARTIFACT-MANIFEST.json']
write('ARTIFACT-MANIFEST.json',dict(schema='compiler-coverage-artifacts-v1',files=manifest))
print(json.dumps(dict(files=len(manifest),application_families=len(apps),initial_sha256=sha(OUT/'INITIAL-SOURCE-USES.json'),decision_sha256=sha(OUT/'DECISION.json'),findings_sha256=sha(OUT/'FINDINGS.md')),indent=2))
