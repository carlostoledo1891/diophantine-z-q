from pathlib import Path
import hashlib,json,zipfile
from pypdf import PdfReader
r=Path(__file__).resolve().parent.parent
p=r/'v14-gi-s13-delivery-root-001'
c=p/'candidate'
m=json.loads((p/'MANIFEST.json').read_text())
checks=[]
for x in m['files']:
 b=(c/x['path']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'];checks.append(x['path'])
g=c/'research/version14/proofs/local-gi-v1'
a=PdfReader(g/'GI-SUPPLEMENT.pdf');o=PdfReader(g/'proof/history/pre-s13-addendum/GI-SUPPLEMENT.pdf')
assert len(a.pages)==106 and len(o.pages)==103
for i in range(103):assert a.pages[i+1].extract_text()==o.pages[i].extract_text(),i
s=(g/'proof/addenda/s13/GI-S13-BOUNDED-SELECTION.md').read_text()
t=''.join((a.pages[104].extract_text()+' '+a.pages[105].extract_text()).split())
(Path(__file__).parent/'EXTRACTED.txt').write_text(t,encoding='utf8')
(Path(__file__).parent/'SOURCE.txt').write_text(s,encoding='utf8')
fm=json.loads((g/'PROOF-ONLY-MANIFEST.json').read_text())
with zipfile.ZipFile(c/'research/version14/proofs/GI-PROOF-ONLY.zip') as z:
 names=z.namelist();print('ZIP_PREFIX',names[:3])
 for x in fm['files']:
  matches=[n for n in names if n==x['path'] or n.endswith('/'+x['path'])];assert len(matches)==1,(x['path'],matches)
  b=z.read(matches[0]);assert hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes']
print(json.dumps({'manifest_members':len(checks),'old_pages_exact_text':103,'new_pages':106,'source_paragraphs_verbatim':True,'archive_members_checked':len(fm['files'])}))
