from pathlib import Path
import hashlib,json,shutil,re,zipfile,sys
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from pypdf import PdfReader,PdfWriter
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
REPO=BASE/'work/quartic-v14-release/preview-repository'
OLD=REPO/'research/version14/proofs/local-gi-v1'
CAND=HERE/'candidate'
NEW=CAND/'research/version14/proofs/local-gi-v1'
TMP=HERE/'tmp/pdfs'
H=lambda b:hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_bytes())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def row(p,root=NEW):
 b=p.read_bytes();return {'path':p.relative_to(root).as_posix(),'sha256':H(b),'bytes':len(b)}
assert not CAND.exists(),'Immutable attempt already exists'
oldm=load(OLD/'PROOF-ONLY-MANIFEST.json')
for r in oldm['files']:
 b=(OLD/r['path']).read_bytes();assert H(b)==r['sha256'] and len(b)==r['bytes'],r['path']
source=REPO/'research/version14/source-adoption-ordinary-v1/local-derivations/GI-S13-BOUNDED-SELECTION.md'
assert H(source.read_bytes())=='e245e0eb1025ab11bcbd47b3f6928bd050076969dfb07c2a9cf950e46cbcaacf'
review=BASE/'work/source-risk-review-20261107/v14-final-composite-review-001/S13-ADDITIVE-SOURCE-REVIEW.json'
assert H(review.read_bytes())=='aafedda9a1eebd0b3e89d23877df32ee24574e6552ee3593a177534536dfced0'
shutil.copytree(OLD,NEW)
TMP.mkdir(parents=True,exist_ok=True)
history=NEW/'proof/history/pre-s13-addendum';history.mkdir(parents=True)
for n in ['GI-SUPPLEMENT.pdf','PDF-PAGE-MAP.json','PACKAGING-CHECK.json','README.md','PROOF-ONLY-MANIFEST.json','SOURCE-REGISTER.json','CUMULATIVE-HANDOFF.json','CUMULATIVE-HANDOFF.md','verify-handoff.py']:
 shutil.copyfile(OLD/n,history/n)
a=NEW/'proof/addenda/s13';a.mkdir(parents=True)
shutil.copyfile(source,a/source.name);shutil.copyfile(review,a/'S13-ADDITIVE-SOURCE-REVIEW.json')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyTextS13',fontName='Times-Roman',fontSize=10.5,leading=13.4,spaceAfter=8))
styles.add(ParagraphStyle(name='SmallS13',fontName='Helvetica',fontSize=8.5,leading=11,spaceAfter=7))
styles.add(ParagraphStyle(name='TitleS13',fontName='Times-Bold',fontSize=18,leading=21,spaceAfter=14))
styles.add(ParagraphStyle(name='HeadS13',fontName='Times-Bold',fontSize=12,leading=15,spaceAfter=8))
def p(s,style='BodyTextS13'):return Paragraph(escape(s),styles[style])
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#555555'));c.drawString(54,30,'Section 13 addendum 1 | 8 November 2026');c.drawRightString(558,30,str(d.page))
text=source.read_text(encoding='utf8');paras=text.strip().split('\n\n')
assert paras[0]=='# Later bounded selection for Section 13'
story=[p('Addendum 1: later bounded selection for Section 13','TitleS13'),p('8 November 2026. This addendum is separate from the original version 1 supplement. It supplies the bounded-selection application for Section 13, proof.tex lines 26-39 and 88-108.','SmallS13'),p('The proof text below reproduces the registered Markdown source verbatim, apart from its heading. The original author-proposal label is retained as provenance. The separately supplied S13-ADDITIVE-SOURCE-REVIEW.json records the later bounded acceptance; it is not a release approval.','SmallS13')]
for q in paras[1:]:story.append(p(q))
SimpleDocTemplate(str(TMP/'addendum.pdf'),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=48,title='Section 13 bounded-selection addendum',author='',invariant=1).build(story,onFirstPage=footer,onLaterPages=footer)
np=len(PdfReader(TMP/'addendum.pdf').pages)
oldpdf=OLD/'GI-SUPPLEMENT.pdf';op=PdfReader(oldpdf);assert len(op.pages)==103
front=[p('A local proof supplement for the required Gowers inverse theorem','TitleS13'),p('Version 1, with Section 13 addendum 1','HeadS13'),p('Original supplement: 8 November 2026, packaging revision 3. Addendum: 8 November 2026. This delivery keeps the original 103 pages and appends the separately identified bounded-selection argument.','BodyTextS13'),p('Contents and page map','HeadS13'),p('PDF page 1: this delivery guide. PDF pages 2-104: the original guide and sixteen proof modules, unchanged. PDF pages 105-'+str(104+np)+': Section 13 addendum 1. Original module-local page numbers are retained.','BodyTextS13'),p('The Section 13 module occupies PDF pages 88-94 in this delivery (pages 87-93 in the original package). Its lower-test correlation to internal bounded represented-family step is supplied by the addendum. The later plain-quadruple argument consumes this bounded family; the addendum does not use the initial inverse theorem as a premise.','BodyTextS13'),p('Source register','HeadS13'),p('The seven published inputs retain their entries in SOURCE-REGISTER.json. Its local_derivations entry now identifies the exact S13 Markdown source and bounded independent review. The addendum invokes the source applications itemized there: ordinary global tests (GTZ Lemma 6.4), countability of model tags, and Appendix A internal-set and selection results.','BodyTextS13'),p('The historical PDF, original source register and original page map are preserved under proof/history/pre-s13-addendum/. The new proof text and review are under proof/addenda/s13/. The source hash is e245e0eb1025ab11bcbd47b3f6928bd050076969dfb07c2a9cf950e46cbcaacf.','SmallS13'),p('This delivery update makes the newly registered argument accessible from the main manuscript\'s existing supplement citation. It does not change the main manuscript or enlarge the mathematical scope of any review. Final source coverage and release approval remain separate.','SmallS13')]
SimpleDocTemplate(str(TMP/'delivery-guide.pdf'),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=48,title='GI supplement delivery guide',author='',invariant=1).build(front)
assert len(PdfReader(TMP/'delivery-guide.pdf').pages)==1
w=PdfWriter();w.append(TMP/'delivery-guide.pdf',outline_item='Delivery guide and addendum source register');w.append(oldpdf,outline_item='Original version 1 supplement (unchanged)');w.append(TMP/'addendum.pdf',outline_item='Addendum 1: Section 13 bounded selection');w.add_metadata({'/Title':'Local GI proof supplement, version 1 with Section 13 addendum 1','/Author':'','/Subject':'Original 103-page supplement plus separately identified bounded-selection addendum'})
with (NEW/'GI-SUPPLEMENT.pdf').open('wb') as out:w.write(out)
newpdf=PdfReader(NEW/'GI-SUPPLEMENT.pdf')
assert len(newpdf.pages)==104+np
for i,pg in enumerate(op.pages):assert pg.extract_text()==newpdf.pages[i+1].extract_text(),('old page changed',i)
norm=lambda s:re.sub(r'\s+','',s)
rendered=norm(''.join(pg.extract_text() for pg in PdfReader(TMP/'addendum.pdf').pages))
for q in paras[1:]:assert norm(q) in rendered,'Missing source paragraph'
pm=load(OLD/'PDF-PAGE-MAP.json');pm.update({'pages':104+np,'guide_pages':2,'sha256':H((NEW/'GI-SUPPLEMENT.pdf').read_bytes()),'original_pdf_page_offset':1,'original_page_map':row(history/'PDF-PAGE-MAP.json'),'delivery_guide_page':1})
for m in pm['modules']:m['start_pdf_page']+=1;m['end_pdf_page']+=1
pm['addenda']=[{'id':'S13-BOUNDED-SELECTION','start_pdf_page':105,'end_pdf_page':104+np,'source':row(a/source.name),'review':row(a/'S13-ADDITIVE-SOURCE-REVIEW.json')}];dump(NEW/'PDF-PAGE-MAP.json',pm)
reg=load(OLD/'SOURCE-REGISTER.json');reg['local_derivations']=[{'id':'S13-BOUNDED-SELECTION','source':row(a/source.name),'review':row(a/'S13-ADDITIVE-SOURCE-REVIEW.json'),'location':'Addendum 1, PDF pages 105-'+str(104+np),'scope':'Section 13 bounded selection from the actual pointwise lower-test correlation premise; source-level incoming premise and remaining global coverage are separately recorded.'}];dump(NEW/'SOURCE-REGISTER.json',reg)
readme=(OLD/'README.md').read_text(encoding='utf8');readme=readme.replace('GI-SUPPLEMENT.pdf contains the current 103-page supplement: one guide page and sixteen proof modules.','GI-SUPPLEMENT.pdf contains '+str(104+np)+' pages: a new delivery guide, the unchanged 103-page version 1 supplement, and the separately identified Section 13 addendum.');readme+='\n## Section 13 addendum\n\nThe bounded-selection proof is printed at PDF pages 105-'+str(104+np)+'. Its exact Markdown source and later bounded independent review are in proof/addenda/s13/. SOURCE-REGISTER.json and PDF-PAGE-MAP.json identify the argument and its use in the original Section 13 module. Historical author-proposal labels are preserved as provenance. The original PDF and its metadata remain in proof/history/pre-s13-addendum/. The original main manuscript and module sources are unchanged.\n';(NEW/'README.md').write_text(readme,encoding='utf8')
check={'original_pages':103,'pages':104+np,'addendum_pages':np,'all_original_page_text_unchanged':True,'all_source_paragraphs_present':True,'main_manuscript_changed':False,'source_sha256':H(source.read_bytes()),'review_sha256':H(review.read_bytes()),'scope':'Artifact identity and text-presence checks only. Visual review and independent delivery-link review are separate.'};dump(NEW/'PACKAGING-CHECK.json',check)
# Rebuild the full standalone file manifest without including reduced-handoff controls.
paths={r['path'] for r in oldm['files']}
paths.update(p.relative_to(NEW).as_posix() for p in history.rglob('*') if p.is_file())
paths.update(p.relative_to(NEW).as_posix() for p in a.rglob('*') if p.is_file())
m={'status':'Original version 1 proof package with exact later S13 source and bounded review; artifact delivery is not global proof or release acceptance.','files':[row(NEW/r) for r in sorted(paths)]};dump(NEW/'PROOF-ONLY-MANIFEST.json',m)
zipout=CAND/'research/version14/proofs/GI-PROOF-ONLY.zip';zipout.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(zipout,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for r in m['files']+ [row(NEW/'PROOF-ONLY-MANIFEST.json')]:
  zi=zipfile.ZipInfo(r['path'],date_time=(2026,11,8,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o100644<<16;z.writestr(zi,(NEW/r['path']).read_bytes())
# Preserve the same cumulative PDF restriction; add the historical merged PDF to exclusions.
oldh=load(OLD/'CUMULATIVE-HANDOFF.json');omit={r['path']:r for r in oldh['excluded']}
histpdf=(history/'GI-SUPPLEMENT.pdf').relative_to(NEW).as_posix()
omit[histpdf]={**row(history/'GI-SUPPLEMENT.pdf'),'reason':'Historical PDF outside the current approved project-PDF set; exact bytes remain in the complete standalone package.','retained_source':row(history/'PDF-PAGE-MAP.json')}
newh={**oldh,'full_package_manifest':row(NEW/'PROOF-ONLY-MANIFEST.json'),'original_members':len(m['files']),'retained':[r for r in m['files'] if r['path'] not in omit],'excluded':list(omit.values()),'external_exclusions':[{'path':'research/version14/proofs/GI-PROOF-ONLY.zip','sha256':H(zipout.read_bytes()),'bytes':zipout.stat().st_size,'reason':'Standalone ZIP is not nested in cumulative handoff.','scope':'Outside this GI directory.'}]}
for r in newh['excluded']:
 r.update(next(x for x in m['files'] if x['path']==r['path']))
htext='# GI files in the cumulative handoff\n\nThe complete package contains the unchanged sixteen module sources and their original version 1 PDF, plus the separately identified S13 addendum in the current merged PDF. The full standalone archive is GI-PROOF-ONLY.zip. Its file manifest is PROOF-ONLY-MANIFEST.json.\n\nThe cumulative handoff retains '+str(len(newh['retained']))+' of the '+str(len(m['files']))+' full-manifest files and excludes '+str(len(omit))+' historical or guide PDFs under the unchanged project-PDF restriction. Every omission and its retained source or page-assembly map is enumerated in CUMULATIVE-HANDOFF.json. The historical merged PDF is assembled from the preserved original page map and original module/guide sources; its exact bytes are supplied in the complete standalone archive. Recreating those historical bytes from a reduced copy alone is not established.\n\nRun python -B verify.py in the complete package. Run python -B verify-handoff.py only in the reduced cumulative copy; it deliberately rejects the excluded PDFs if present. File verification does not establish mathematical validity or release approval.\n\nThe standalone ZIP is not nested in the cumulative archive. Its SHA-256 is '+H(zipout.read_bytes())+'. The existing main manuscript remains unchanged.\n'
(NEW/'CUMULATIVE-HANDOFF.md').write_text(htext,encoding='utf8');newh['added_text']=[row(NEW/'CUMULATIVE-HANDOFF.md')];dump(NEW/'CUMULATIVE-HANDOFF.json',newh)
vs=(OLD/'verify-handoff.py').read_text(encoding='utf8');vs=re.sub(r"EXPECTED='[0-9a-f]{64}'","EXPECTED='"+H((NEW/'CUMULATIVE-HANDOFF.json').read_bytes())+"'",vs);(NEW/'verify-handoff.py').write_text(vs,encoding='utf8')
alias=CAND/'manuscripts/quartic-local-gi-supplement.pdf';alias.parent.mkdir(parents=True);shutil.copyfile(NEW/'GI-SUPPLEMENT.pdf',alias)
changed=[]
for f in CAND.rglob('*'):
 if not f.is_file():continue
 rel=f.relative_to(CAND);dest=REPO/rel
 if not dest.exists() or dest.read_bytes()!=f.read_bytes():changed.append(row(f,CAND))
dump(HERE/'MANIFEST.json',{'author':'/root','status':'Candidate delivery update awaiting visual and independent link review','original_manuscript_sha256':H((REPO/'manuscripts/quartic_v14.tex').read_bytes()),'original_supplement_sha256':H(oldpdf.read_bytes()),'files':changed})
dump(HERE/'CHECKS.json',check)
print(json.dumps({'pages':104+np,'addendum_pages':np,'changed_files':len(changed),'full_manifest_files':len(m['files']),'pdf_sha256':H((NEW/'GI-SUPPLEMENT.pdf').read_bytes()),'zip_sha256':H(zipout.read_bytes()),'manifest_sha256':H((HERE/'MANIFEST.json').read_bytes())}))
