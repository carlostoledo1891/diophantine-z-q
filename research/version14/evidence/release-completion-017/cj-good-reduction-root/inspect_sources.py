from pathlib import Path
import hashlib
import json
import re
import unicodedata
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'local-only'
OUT.mkdir(exist_ok=True)
source = ROOT / 'work/astra-final-size-independent-review-001/silverman-2009.pdf'
doc = pdfium.PdfDocument(str(source))
needles = ('potentialgoodreduction', 'reductionofanisogeny', 'mappingproperty', 'extendsuniquely', 'quotientby', 'corollary15', 'theorem15', 'finiteetale')
hits = []
for i in range(len(doc)):
    page = doc[i]
    tp = page.get_textpage()
    txt = tp.get_text_range()
    normalized = re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD',txt).casefold())
    found = [n for n in needles if n in normalized]
    if found or 211 <= i+1 <= 223:
        target = OUT / f'silverman-page{i+1:03}.txt'
        target.write_text(txt, encoding='utf-8')
        hits.append({'page': i+1, 'matches': found, 'path': str(target.relative_to(ROOT)), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    tp.close()
    page.close()
data = {'source':str(source.relative_to(ROOT)), 'sha256':hashlib.sha256(source.read_bytes()).hexdigest(), 'pages':len(doc), 'hits':hits}
(OUT / 'scan.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
print(json.dumps(data, indent=2))
