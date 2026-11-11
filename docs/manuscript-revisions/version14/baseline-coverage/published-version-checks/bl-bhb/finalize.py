from pathlib import Path
import hashlib,json

OUT=Path(__file__).resolve().parent
ROOT=Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pin=lambda p:dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
write=lambda n,x:(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
manuscript=ROOT/'work/quartic-version6-release/repository/manuscripts/quartic_v13.tex'
assert sha(manuscript)=='9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd'
assert sha(OUT/'bl-final.pdf')=='51bafd17097d8bf227a63c885973586a9645546fadb7eea6b5e5ebefe2a361c3'
lines=manuscript.read_bytes().splitlines(keepends=True)
consumer=b''.join(lines[16649:16694])
(OUT/'BL-consumer-v13.tex').write_bytes(consumer)
accepted=ROOT/'work/quartic-version5-release/sun-proof/sources'
write('COMPARISON.json',dict(
 schema='published-version-comparison-v1',reviewer='/root/astra_v14_baseline_compiler',
 date_local='2026-11-07',retrieved_utc_date='2026-11-08',
 scope='Final-publication statement/convention comparison; no whole-paper reproof, no main manuscript edit',
 governing_manuscript=pin(manuscript),
 BL=dict(
  decision='final_statement_and_consumed_conventions_match_accepted_version',
  publication='Browning–Loughran, Trans. Amer. Math. Soc. 371 (2019), 5757–5785',
  doi='10.1090/tran/7514',final_source=pin(OUT/'bl-final.pdf'),
  publisher_url='https://www.ams.org/journals/tran/2019-371-08/S0002-9947-2018-07514-6/S0002-9947-2018-07514-6.pdf',
  source_status='Final published typeset article, journal imprint directly inspected',
  final_pages_inspected=[dict(pdf_page=1,printed_page=5757),dict(pdf_page=16,printed_page=5772),dict(pdf_page=17,printed_page=5773)],
  accepted_source=pin(accepted/'BL-accepted.pdf'),accepted_pages_inspected=[dict(pdf_page=17,author_page=16),dict(pdf_page=18,author_page=17)],
  assertion='Theorem4.1 together with equations4.1/4.2, definition of weighted count, and following modulus-independence paragraph',
  consumer=dict(label='lem:v5-primitive-count',lines=[16650,16694],snapshot=pin(OUT/'BL-consumer-v13.tex')),
  historical_application='V5-SUN-BL-CONGRUENCES',independent_gaussian_contract='GAU-003',
  convention_checks=['n>=5; isotropic nonsingular integral quadratic form','arbitrary nonempty local subsets with nonzero reduction','M coprime 2Delta','smooth nonnegative compact support; nonvanishing gradient','unprimitive weighted integral count','local factor cardinality/p^(a(n-1))','error O_epsilon,F,w(B^(n/2+epsilon)M^(n/2+epsilon)), uniform in M and subset choice'],
  application_transport=['Q_kappa isotropic via (1,0,1,0,0); discriminant supported on2kappa','support away origin supplies gradient bound','empty subsets separate','Mobius inversion remains internal, not attributed directly to Theorem4.1'],
  mathematical_changes_required=[],
  qualification_removable='For this bounded application only: final typeset text was not accessible',
  limitations=['No full Section4 proof re-verification','No assertion of whole-PDF textual identity','Other Gaussian proof/source qualifications remain']
 ),
 BHB=dict(
  decision='final_version_not_obtained_comparison_unresolved',
  publication='Browning–Heath-Brown, Forum Math.33(2021),147–165',doi='10.1515/forum-2020-0074',
  target_assertions=['Lemma2.1','Lemma4.1','Section4 lattice basis/inverse estimates'],
  final_source=None,accepted_source=pin(accepted/'BHB-accepted.pdf'),
  publisher_record='https://www.degruyterbrill.com/document/doi/10.1515/forum-2020-0074/html',
  repository_record='https://ora.ox.ac.uk/objects/uuid:029537a5-f3a1-4ec7-a96f-07533accd494',
  access_findings=['Publisher web record provides metadata, says full text unavailable','Ordinary HTTPS HTML/PDF requests returned405 human-verification HTML, notPDF','Oxford explicitly labels copy accepted manuscript','Browning publication page links arXiv'],
  challenges_bypassed=False,qualification_removable=None,
  required_action='Retain accepted/arXiv qualification until a legitimate final text is available and exact statements/conventions are compared',
  mathematical_defect_identified=False
 ),
 no_repository_edits=True,no_remote_mutations=True,
 evidence_images=[pin(OUT/n) for n in ['bl-page-1.png','bl-page-16.png','bl-page-17.png','bl-accepted-page-17.png','bl-accepted-page-18.png']],
 retrieval_records=['RETRIEVAL.json','RETRIEVAL-network.json']))
files=[dict(name=p.name,sha256=sha(p),bytes=p.stat().st_size) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
write('MANIFEST.json',dict(schema='published-version-check-artifacts-v1',files=files))
print(json.dumps(dict(BL='bounded final-version comparison complete',BHB='final-version comparison unresolved',files=len(files),comparison_sha256=sha(OUT/'COMPARISON.json'),review_sha256=sha(OUT/'REVIEW.md')),indent=2))
