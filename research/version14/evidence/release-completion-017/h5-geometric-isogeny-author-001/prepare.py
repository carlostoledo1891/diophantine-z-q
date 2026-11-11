from pathlib import Path
import hashlib,json

ROOT=Path.cwd()
D=ROOT/'work/source-risk-review-20261107/h5-geometric-isogeny-author-001'
def sha(b): return hashlib.sha256(b).hexdigest()
def rec(path,expected=None):
 p=ROOT/path; b=p.read_bytes(); h=sha(b)
 if expected: assert h==expected,(str(path),h,expected)
 return dict(path=str(path).replace('\\','/'),sha256=h,bytes=len(b))
def loc(path,a,z):
 r=rec(path); ls=(ROOT/path).read_bytes().splitlines(keepends=True)
 assert 1<=a<=z<=len(ls)
 return dict(**r,start_line=a,end_line=z,excerpt_sha256=sha(b''.join(ls[a-1:z])))
def write(name,obj):
 p=D/name; assert not p.exists(),str(p)
 p.write_bytes((json.dumps(obj,indent=2,ensure_ascii=False)+'\n').encode())

current='work/quartic-v14-combined-20261108-008/candidate/manuscripts/quartic_v14.tex'
cover='work/source-risk-review-20261107/h5-d210-fine-cover-compiler-002/PROOF.md'
central='work/source-risk-review-20261107/combined005-forward-hodge-author-sol-004/CONNECTIONS.md'
proof='work/source-risk-review-20261107/h5-geometric-isogeny-author-001/PROOF.md'
def section(path,heading,next_heading):
 ls=(ROOT/path).read_text(encoding='utf-8-sig').splitlines()
 a=next(i+1 for i,s in enumerate(ls) if s.startswith(heading))
 z=next((i for i,s in enumerate(ls) if i+1>a and s.startswith(next_heading)),len(ls))
 return loc(path,a,z)
inputs=[rec(current,'1aac9fc4637250dbbdab47d2930aeb1af0ff431d41104b775eaf26a01e13542d'),rec(cover,'054ec4a656b82e1d1d17c7e9d3575afe722c42594f933256e7ea225f6a3f5e3b'),rec(central,'8bbb16bcc972320689a8e287b94467e07fef9e97b6670460a9d822b859641ab6')]
for path,h in [
 ('work/quartic-v14-prep/independent-source-review/h5-d210-current-review-001/MANIFEST.json','9875bfa37bff87dfcccdced9d019f872879865c547d4bc948d851969c2456984'),
 ('work/source-risk-review-20261107/forward-hodge-independent-adoption-001/MANIFEST.json','baade81e5f0f1d03950a665f00023973f117ab5a4f92f42d1580698ed00be3ee'),
 ('work/source-risk-review-20261107/h5-isogeny-sourcefirst-arithmetic-001/MANIFEST.json','d58e016853be1db99eebf6c5403f14eb659650dc61144d54f9efe2895e32e215')]: inputs.append(rec(path,h))
local='work/source-risk-review-20261107/h5-geometric-isogeny-author-001/local-only/'
sources=[dict(id='VOIGHT-QUADRATIC-EMBEDDINGS',publication='John Voight, Quaternion Algebras, GTM 288, Springer, 2021, Chapter 7, Corollary 7.1.5 and direct proof, p.97',url='https://link.springer.com/content/pdf/10.1007/978-3-030-56694-4_7.pdf',file=rec(local+'voight2021-chapter7-final.pdf','98764f8bbf0a53a82c6043c171e2df42455fb17bcdf064dc28f4c12405765c5e'),pdf_page=3,available='An isomorphism between two quadratic subfields of a quaternion algebra is induced by conjugation by an invertible element.',limits='Only this quaternionic corollary and its direct proof are selected. The application is over Q.'),dict(id='VOIGHT-ERRATUM-19',publication='Official first-edition errata, August 5, 2026, p.2 item19',url='https://jvoight.github.io/quat-errata.pdf',file=rec(local+'voight-errata-20260805.pdf','42987c03960d3c5d36e5920243e6defc587710cd7e106e79b3a688d1e3bf3232'),pdf_page=2,available='Correct the unit-group notation after separable scalar extension and omit the optional linearly-disjoint splitting-field parenthesis.',limits='A proof correction is retained explicitly; no whole-book or uncorrected-proof approval.')]
locations={'consumer':loc(current,7833,7839),'same_L_Hom':loc(current,7805,7819),'cover_integral':section(cover,'## 6.','## 7.'),'cover_canonical':section(cover,'## 7.','## 8.'),'centralizer':loc(central,15,24),'geometric_Hom_descent':loc(central,5,13)}
cards=[]
data=[
 ('H5-GI-NORMALIZER','2.','3.','Each actual normalizer-related fiber surface is geometrically isogenous to the given fiber surface.',['cover_integral','cover_canonical','geometric_Hom_descent'],'The rational PEL object stays fixed; commensurable integral lattices are realized by finite torsion quotients.','All components and level multipliers of the actual U(3) model; no degree estimate or coherent choices.'),
 ('H5-GI-ENDOMORPHISMS','3.','4.','The full geometric rational endomorphism algebra of the actual non-CM surface is B.',['centralizer'],'Apply the existing rank-one quaternionic Hodge-centralizer calculation and its algebraic-closure descent.','Non-CM only for End=B; the CM alternative is M2(k), not a domain for the following B-correction.'),
 ('H5-GI-QUADRATIC-CORRECTION','4.','5.','For the specified two embeddings of E, there is a geometric E-linear isogeny A to A_sigma.',['consumer'],'Apply Voight7.1.5 to i(E), f^(-1)i_sigma(E)f; use g=f b^(-1), then clear its denominator.','E is an abstract quadratic number field with both specified embeddings. The intertwining equation preserves that identification, not only its image.'),
 ('H5-GI-SAME-FIELD','5.','6.','The corrected isogeny and E-actions are defined over the existing field L.',['same_L_Hom'],'Apply the already established simultaneous Hom descent to the integral homomorphism and to rational endomorphisms.','Same actual fiber surfaces over L; no additional extension, bounded Q-descent or cocycle conclusion.')]
for ident,a,z,out,keys,deriv,limits in data:
 cards.append(dict(id=ident,status='unresolved_author_proposal',objects='Actual discriminant-210 principal-three fiber surfaces A,A_sigma over L; B and the specified E when used.',needed=out,output=out,incoming_locations=[locations[k] for k in keys],source_ids=['VOIGHT-QUADRATIC-EMBEDDINGS','VOIGHT-ERRATUM-19'] if ident.endswith('CORRECTION') else [],derivation=deriv,proof_location=section(proof,'## '+a,'## '+z),current_occurrence=locations['consumer'],scope_limits=limits))
write('INPUTS.json',dict(author='/root/astra_v14_source_review',inputs=inputs,sourcefirst_review_is_not_acceptance=True))
write('SOURCES.json',sources)
write('LOCATIONS.json',locations)
write('APPLICATIONS.json',dict(format='bounded author connection cards; not a deployed ordinary schema',applications=cards))
write('DEPENDENCIES.json',dict(edges=[['H5-GI-ENDOMORPHISMS','H5-GI-QUADRATIC-CORRECTION'],['H5-GI-NORMALIZER','H5-GI-QUADRATIC-CORRECTION'],['H5-GI-QUADRATIC-CORRECTION','H5-GI-SAME-FIELD']],retained=['Chosen integral datum','Actual normalizer orbit of this fiber','Accepted full-cover rational PEL comparison','Accepted geometric Hodge-centralizer and Hom descent','Existing same-L simultaneous Hom theorem'],excluded=['Cocycle-compatible choices','New compatible system','Degree bound on isogenies','Bounded descent to Q','Whole H5 or whole manuscript approval']))
write('SOURCE-READING.json',dict(published_pdf_page=3,printed_page=97,errata_pdf_page=2,errata_item=19,mode='Published text and official errata read directly; selected local PDF pages rendered for visual check.',assets=[rec(local+n) for n in ['voight2021-chapter7-final-selected.png','voight-errata-20260805-selected.png','voight2021-chapter7-final-selected.txt','voight-errata-20260805-selected.txt']]))
write('REVIEW-STATUS.json',dict(status='pending_independent_review',author='/root/astra_v14_source_review',reviewer='/root/astra_v14_assertions_arithmetic',independent_acceptance=False,prior_exposure='Author previously reviewed H5 full-cover and contributed related Hodge-source work. Those prior decisions do not independently approve this new connection.',no_live_edit=True))
checks=[]
for obj in [locations]+[c['proof_location'] for c in cards]:
 values=obj.values() if 'path' not in obj else [obj]
 for v in values:
  if isinstance(v,dict) and 'excerpt_sha256' in v:
   assert loc(v['path'],v['start_line'],v['end_line'])==v
   checks.append(v['path']+':'+str(v['start_line'])+'-'+str(v['end_line']))
write('CHECKS.json',dict(exact_locations_verified=checks,input_files_verified=len(inputs),source_pdfs_verified=2,assertion='Author consistency checks only; no mathematical acceptance.'))
write('PUBLIC-SELECTION.json',dict(include=['PROOF.md','SOURCES.json','APPLICATIONS.json','DEPENDENCIES.json','REVIEW-STATUS.json'],exclude=['local-only'],note='Source assets remain local; source statements are author paraphrases. No archive or release selection implied.'))
members=[rec(str(p.relative_to(ROOT))) for p in sorted(D.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
write('MANIFEST.json',dict(schema_version=1,status='author_frozen_pending_review',members=members))
print(json.dumps(dict(manifest=rec(str((D/'MANIFEST.json').relative_to(ROOT))),proof=rec(proof),members=len(members)),indent=2))
