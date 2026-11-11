from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, logging
logging.disable(logging.CRITICAL)
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[3]
PREP=ROOT/'work/quartic-v14-prep'
def sha(b): return hashlib.sha256(b).hexdigest()
def pin(p):
    b=p.read_bytes()
    return {'path':p.relative_to(ROOT).as_posix(),'bytes':len(b),'sha256':sha(b)}
tex=ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
assert pin(tex)['sha256']=='b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d'
review=PREP/'independent-source-review/SOURCE-VERSION-DISPOSITIONS-001.json'
rows=json.loads(review.read_text(encoding='utf-8'))['rows']
lines=tex.read_bytes().splitlines(keepends=True)
def span(a,b): return {'pin':pin(tex),'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b])),'excerpt_convention':'original bytes including original line endings'}
base={'schema':'source-version-comparison-v1','recorded_at_utc':datetime.now(timezone.utc).isoformat(),'author_agent':'/root/astra_v14_assertions_arithmetic','author_run':'local:v14:arithmetic-assertion-author:20261107','approval':False,'intake_pin':pin(review)}
bg=PREP/'final-source-baba-granath'
bz=PREP/'final-source-buzzard'
bg_author=ROOT/'work/astra-final-height-producers-001/primary/baba-granath-2005.pdf'
bz_author=ROOT/'work/astra-final-height-producers-001/primary/buzzard-1996.pdf'
assert pin(bg_author)['sha256']=='b049ce64f9b662af0e078f4faa9e5325cc7a99bf2d6ccda0a31a84719d031c32'
assert pin(bz_author)['sha256']=='4854cb4adc99fec7eac47596dea86832e2e468f3c80d78726afeb98d2404b915'
bg_final=bg/'local-only/baba-granath-published.pdf'
assert pin(bg_final)['sha256']=='c711b2bed2aa0dd70d1bc1dd06c6d4a921c4b8735452bc143431f080a8cac12c'
assert len(PdfReader(bg_final).pages)==24
bg_data={**base,'source_id':'babagranath','application_ids':['A001'],'status':'final-needed-statements-compared-with-explicit-normalization-correction','final_version_compared':True,'intake_row':next(r for r in rows if r['source_id']=='babagranath'),'author_pdf':pin(bg_author),'final_pdf':pin(bg_final),'final_url':'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E6B7F5233E98E9C8E013658575FF713F/S0008414X00022008a.pdf/genus-2-curves-with-quaternionic-multiplication.pdf','doi':'10.4153/CJM-2008-033-7','access':'freely retrieved directly from publisher','manuscript_uses':[span(486,498),span(499,517),span(608,617)],'statement_map':[
{'preprint':'section 2.1 pp.3-5, Theorem 1 p.4','final':'section 2.1 pp.736-738, Theorem 2.1 p.737','final_pdf_pages':[3,4,5],'dependency':'polarized coarse quotient V_Z=V/W; stable-ring and principal-polarization conventions','result':'needed quotient conclusion preserved; twisting definition corrected; displayed Riemann form needs separate normalization'},
{'preprint':'section 3 p.6; Lemma 2 p.7','final':'section 3 p.739; Lemma 3.1 pp.739-740','final_pdf_pages':[6,7],'dependency':'discriminant-six data and rational projective-line quotient','result':'needed data and statement preserved; proof subscript typo persists'},
{'preprint':'section 3.1 table p.7','final':'section 3.1 table p.740','final_pdf_pages':[7],'dependency':'full-normalizer branch orders 4,6,2 at z2,z3,z6','result':'table preserved with full-normalizer row explicitly named Gamma_W'},
{'preprint':'Proposition 7 p.9','final':'Proposition 3.6 p.742','final_pdf_pages':[9],'dependency':'finite nonzero arithmetic j and weighted Igusa coordinates','result':'formula and excluded points preserved'},
{'preprint':'Proposition 10 pp.11-12','final':'Proposition 3.9 p.744','final_pdf_pages':[11],'dependency':'j=j_m^2 and labelled values 0,infinity,-16/27','result':'needed equality and values preserved'}],
'separate_correction':{'kind':'principal-polarization-form-normalization','current_form':'Trd(mu^-1 x conjugate(y))','published_displayed_form':'Trd(conjugate(x) mu y)','published_to_current_factor':6,'current_determinant':1,'published_determinant':1296,'checker':pin(bg/'check_normalization.py'),'result':pin(bg/'NORMALIZATION-CHECK.json'),'additional_preserved_dependencies':['positive sign and Rosati identification via manuscript/Lin-Yang','all determinant components','degree bound 324','integral level-three construction and descent']},'other_source_corrections':['Final twisting definition uses full normalizer instead of preprint positive normalizer, and expands trace/primitive description.','Lemma 3.1 proof final paragraph needs z2 rationality rather than its printed z3 reference; z2 rationality was already proved.'],'proposed_disposition':'Independent reviewer may close final-statement-comparison gap for listed uses while retaining normalization correction and separate manuscript obligations.'}
bz_data={**base,'source_id':'buzzard','application_ids':['A001','A002'],'status':'unresolved-final-statements-and-2002-correction-scope','final_version_compared':False,'intake_row':next(r for r in rows if r['source_id']=='buzzard'),'author_pdf':pin(bz_author),'author_url':'https://www.ma.imperial.ac.uk/~buzzard/maths/research/papers/shimura.pdf','doi':'10.1215/S0012-7094-97-08719-6','crossref':pin(bz/'local-only/crossref.json'),'manuscript_uses':[span(486,496),span(519,555)],'author_locators':[{'pdf_page':3,'locator':'section 1 canonical principal polarization; Definition 1.1'},{'pdf_pages':[4,5],'locator':'V1(N), conditions (i)-(iii), Theorem 2.1'},{'pdf_page':7,'locator':'Corollary 2.3'}],'actual_application':{'D':'(2,-3) over Q','d':6,'U':'V1(5)','N':5,'M_U':5,'base_ring':'Z[1/30]','conditions':['full determinant image','maximal level at division primes 2 and 3','U subset V1(N), N>=4 coprime to d'],'supplied_conclusion':'initial model smooth proper relative curve; represented by regular projective scheme','not_supplied_directly':['full level three at ramified prime 3','all determinant components for full markings','free forgetting-five quotient','universal abelian scheme descent']},'browser_observation':{'date':'2026-11-07 session (UTC evidence timestamp above)','method':'ordinary Chrome browser via cua_repl','page':'https://projecteuclid.org/journals/duke-mathematical-journal/volume-87/issue-3/Integral-models-of-certain-Shimura-curves/10.1215/S0012-7094-97-08719-6.short','visible_price':'$30.00','visible_access':'full article restricted; sign-in or single-article purchase','preview_url':'https://projecteuclid.org/JournalArticle/PreviewFirstPage?urlid=10.1215%2fS0012-7094-97-08719-6','preview_pages':1,'printed_page':591,'preview_content':'introduction, acknowledgements and beginning of section 1 ending during false elliptic curve definition','sufficient_for_needed_statements':False,'local_preview_pdf_saved':False,'purchase_or_login_attempted':False},'correction_scope':'Author cover says original 13 May 1996, typos fixed 14 June 2002. No itemized correction list obtained. Final1997 statements not accessible for comparison.','proposed_disposition':'Keep corrected-author-version qualification and unresolved final comparison; no extra corrective proof claimed.'}
for out,data in [(bg,bg_data),(bz,bz_data)]:
    data['report']=pin(out/'COMPARISON.md')
    data['local_only_artifacts']=[pin(p) for p in sorted((out/'local-only').iterdir()) if p.is_file()]
    (out/'EVIDENCE.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    public=[p for p in out.iterdir() if p.is_file() and p.name!='FROZEN-PACKAGE.json']
    frozen={'status':data['status'],'approval':False,'files':[pin(p) for p in sorted(public)],'local_only_excluded_from_release':True}
    (out/'FROZEN-PACKAGE.json').write_text(json.dumps(frozen,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'directory':out.relative_to(ROOT).as_posix(),'evidence':pin(out/'EVIDENCE.json'),'manifest':pin(out/'FROZEN-PACKAGE.json')}))
