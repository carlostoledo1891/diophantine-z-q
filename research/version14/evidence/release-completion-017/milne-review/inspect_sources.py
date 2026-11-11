from pathlib import Path
import hashlib,json,logging,sys
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf8')
logging.getLogger('pypdf').setLevel(logging.ERROR)
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
man=ROOT/'work/source-risk-review-20261107/milne-author/MANIFEST.json'
assert H(man.read_bytes())=='814f3b20201fef78db3627e1def49b41bd538363fd536fe33b78e0c6fdf1cda9'
for p in json.loads(man.read_bytes())['files']:
    b=(ROOT/p['path']).read_bytes();assert H(b)==p['sha256'] and len(b)==p['bytes']
book=ROOT/'work/astra-arithmetic-final-composition-001/milne-ADT-2006.pdf'
assert H(book.read_bytes())=='2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31'
r=PdfReader(book)
pages=list(range(1,20))+list(range(27,46))+list(range(48,69))+list(range(81,101))+[163,164,165]
out=HERE/'local-only';out.mkdir(exist_ok=True)
for n in pages:
    (out/('book-p%03d.txt'%n)).write_text(r.pages[n+7].extract_text(),encoding='utf8')
a=PdfReader(out/'ADT2006-addendum.pdf')
(out/'addendum.txt').write_text('\n\n'.join('PDF PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(a.pages)),encoding='utf8')
src=ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
raw=src.read_bytes();assert H(raw)=='81d421af9dedd0d975024c9d0ff1b1d11249b7b36f2c9215bd2c80278f4934fc'
lines=raw.splitlines(keepends=True)
bound=json.loads((ROOT/'work/source-risk-review-20261107/milne-author/SOURCE-BINDINGS.json').read_bytes())
for p in bound['consumers']:
    assert H(b''.join(lines[p['start_line']-1:p['end_line']]))==p['excerpt_sha256']
sections=[(730,778),(3588,3650),(4240,4365),(4698,4790),(7200,7243),(12248,12265),(13210,13305)]
(HERE/'current-consumers.txt').write_text('\n\n'.join('\n'.join(str(i+1)+': '+lines[i].decode().rstrip() for i in range(a-1,b)) for a,b in sections),encoding='utf8')
print(json.dumps({'author_manifest_verified':True,'book_pages':len(r.pages),'extracted_printed_pages':pages,'addendum_pages':len(a.pages),'addendum_sha256':H((out/'ADT2006-addendum.pdf').read_bytes())}))
