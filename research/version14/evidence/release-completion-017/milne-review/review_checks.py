"""Independent byte, occurrence and orientation checks. This does not prove duality."""
from pathlib import Path
from hashlib import sha256
import json
import re
from fractions import Fraction
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MANUSCRIPT = 'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
AUTHOR = ROOT / 'work/source-risk-review-20261107/milne-author'
H = lambda b: sha256(b).hexdigest()

def pin(p):
    p = Path(p)
    b = p.read_bytes()
    return {'path': p.relative_to(ROOT).as_posix(), 'sha256': H(b), 'bytes': len(b)}

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf8')

assert H((AUTHOR/'MANIFEST.json').read_bytes()) == '814f3b20201fef78db3627e1def49b41bd538363fd536fe33b78e0c6fdf1cda9'
author_manifest = json.loads((AUTHOR/'MANIFEST.json').read_bytes())
for row in author_manifest['files']:
    assert pin(ROOT/row['path']) == row
successors = []
for dirname, expected in [('milne-author-r2','037a180fccf370a828c6ffb614dfae1335018db8c947acc2fcc250eaf48777ed'),('milne-author-r3','9b975f6059c97ac83e5455a2b9707736fca4d886ca94789de3525e88a7fa4c12')]:
    folder = AUTHOR.with_name(dirname)
    mpath = folder/'MANIFEST.json'
    assert H(mpath.read_bytes()) == expected
    m = json.loads(mpath.read_bytes())
    assert pin(ROOT/m['parent']['path']) == m['parent']
    for f in m['files']:
        assert pin(ROOT/f['path']) == f
    assert (folder/'PROPOSED-BRAUER.tex').read_bytes() == (AUTHOR/'PROPOSED-BRAUER.tex').read_bytes()
    original_tail = (AUTHOR/'REPORT.md').read_bytes().split(b'## Scalar descent and Brauer reciprocity',1)[1]
    assert (folder/'REPORT.md').read_bytes().split(b'## Scalar descent and Brauer reciprocity',1)[1] == original_tail
    successors.append({'manifest':pin(mpath),'files':m['files']})
book = HERE/'local-only/ADTnot-official.pdf'
addendum = HERE/'local-only/ADT2006-addendum.pdf'
assert H(book.read_bytes()) == '2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31'
assert H(addendum.read_bytes()) == '2eff84551aa72ce16ae20554e46baf03494fa1130612875041905f9df34ea50c'
assert book.read_bytes() == (ROOT/'work/astra-arithmetic-final-composition-001/milne-ADT-2006.pdf').read_bytes()
assert len(PdfReader(book).pages) == 347
assert len(PdfReader(addendum).pages) == 10
raw = (ROOT/MANUSCRIPT).read_bytes()
assert H(raw) == '81d421af9dedd0d975024c9d0ff1b1d11249b7b36f2c9215bd2c80278f4934fc'
lines = raw.splitlines(keepends=True)
bindings = json.loads((AUTHOR/'SOURCE-BINDINGS.json').read_bytes())
for row in bindings['consumers']:
    assert H(b''.join(lines[row['start_line']-1:row['end_line']])) == row['excerpt_sha256']
for dirname in ['milne-author-r2','milne-author-r3']:
    sb = json.loads((AUTHOR.with_name(dirname)/'SOURCE-BINDINGS.json').read_bytes())
    assert sb['manuscript'] == bindings['manuscript']
    for row in sb['consumers']:
        assert H(b''.join(lines[row['start_line']-1:row['end_line']])) == row['excerpt_sha256']
    assert sb['official_addendum']['pin'] == pin(addendum)
    assert sb['official_addendum']['pages'] == 10
old = bindings['proposed_edit']['old']
assert old['start_line'] == 770 and old['end_line'] == 774
assert H(b''.join(lines[769:774])) == old['excerpt_sha256']
replacement = (AUTHOR/'PROPOSED-BRAUER.tex').read_bytes()
assert H(replacement) == 'e54eade4962e6b81eb2113ecd2d458267fcdb096a1e8257bfd34489542230484'
candidate = b''.join(lines[:769]) + replacement + b''.join(lines[774:])
assert candidate.startswith(b''.join(lines[:769]))
assert candidate.endswith(b''.join(lines[774:]))
assert replacement.endswith(b'\n')
assert b'proof of II.2.1, p.~164' in replacement

citations = []
for n, line in enumerate(lines, 1):
    for content in re.findall(rb'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', line):
        if b'milne' in content.split(b','):
            citations.append(n)
assert citations == [774, 3622, 4255, 4755, 4776, 12254, 12259]

occurrences = [
    (746,783,'Brauer lifting','direct','Constant coefficients, finite local two-torsion and global invariant sum.'),
    (1180,1194,'Cofinite Sha quotient','related erratum','Explicit divisible summand and finite complement; Poonen-Stoll input remains separate.'),
    (3214,3242,'Finite unramified local descent','related erratum','Finite complete extension first; no completion of the infinite unramified union.'),
    (3592,3648,'Derived finite Kummer condition','direct','Finite-place Milne comparison; global Nekovar theorem remains separate.'),
    (3960,3998,'Fixed old-support comparison','repetition','Same finite Kummer map and torsion-preserving free resolutions, then scalar extension.'),
    (4235,4246,'Maximal divisible Selmer image','related erratum','Divisible kernel with finite quotient identifies the maximal divisible image.'),
    (4248,4258,'Isogeny calibration announcement','direct','Finite Sha at specified constituents; no BSD leading-term assumption.'),
    (4278,4365,'Isogeny signs and measures','direct','Dual maps and canonical heights; Edixhoven component geometry is inherited.'),
    (4694,4771,'Global residual dimensions','direct','Imaginary quadratic K, S includes dyadic and archimedean places.'),
    (4773,4785,'Local residual dimensions','direct','Full rational E[2], field characteristic zero, dyadic index retained.'),
    (5112,5127,'Switch exact-annihilator consumer','boundary','Requires separately retained Nekovar localization and actual transported diagrams.'),
    (5258,5295,'Transported local planes','boundary','Explicit tame-coordinate action and cup identities; no inference from residual alternation alone.'),
    (5480,5542,'Ordinary Kummer budget','repetition','Finite-place orthogonality repeated; global self-duality and limit steps are separate.'),
    (7209,7245,'Second scalar-lift occurrence','repetition','Same constant-coefficient obstruction, including p=2 and the real invariant.'),
    (7921,7932,'Repeated corank argument','related erratum','Same cofinite decomposition and paired finite cyclic factors, not a finite-Sha premise.'),
    (12254,12261,'Summary table','summary','Summarizes Kummer/global-duality and finite-Sha isogeny interfaces without a new theorem.'),
    (13238,13304,'Real convention and finite Kummer repetition','mixed boundary','Finite-place comparison is repeated; real Tate groups and global Nekovar sequence are separately identified.'),
    (22836,22838,'Bibliography','bibliography','Second edition 2006, not first edition.')
]
rows = []
for a,b,label,role,scope in occurrences:
    rows.append({'label':label,'role':role,'scope':scope,'location':{'path':MANUSCRIPT,'start_line':a,'end_line':b,'file_sha256':H(raw),'excerpt_sha256':H(b''.join(lines[a-1:b]))}})
pole = ROOT/'work/quartic-v14-release/preview-repository/docs/theorem-application-audit/evidence/pole.md'
pl = pole.read_bytes().splitlines(keepends=True)
rows.append({'label':'Finite-quotient alternating-pairing proof','role':'related erratum','scope':'Explicit maximal divisible quotient and paired cyclic factors; no restricted F[2] pairing is assumed nondegenerate.','location':{**pin(pole),'start_line':94,'end_line':110,'excerpt_sha256':H(b''.join(pl[93:110]))}})

# Independent orientation algebra from Milne 7.3.1. Variables are 2-adic
# logarithms: torsionA,torsionB,I,J,periodA,periodB,componentsA,componentsB.
# sA-sB = (2*gA-2*gB+j-i) - [(oA-oB)+(cA-cB)].
zphi_coefficients = [1,-1,-1,0,0,0,0,0]
zpsi_coefficients = [-1,1,0,-1,0,0,0,0]
volume_coefficients = [0,0,0,0,1,-1,1,-1]
orientation = [a-b-c for a,b,c in zip(zphi_coefficients,zpsi_coefficients,volume_coefficients)]
assert orientation == [2,-2,-1,1,-1,1,-1,1]
assert Fraction(4,4**2) == Fraction(1,4)
for d in range(1,9):
    assert 2-(4+2*d)+2 == -2*d
    assert Fraction(2**2*2**2,2**(4+2*d)) == Fraction(1,2**(2*d))
for I in [1,2]:
    J = 2//I
    assert Fraction(J,I) == Fraction(2,I**2)
    for ga in range(5):
        for gb in range(5):
            zphi = Fraction(2**ga, 2**gb*I)
            zpsi = Fraction(2**gb, 2**ga*J)
            assert zphi/zpsi == Fraction(2**ga,2**gb)**2 * Fraction(2,I**2)

write('OCCURRENCES.json', {'manuscript':pin(ROOT/MANUSCRIPT),'direct_milne_citation_lines':citations,'occurrences':rows,'scope':'Current repetitions located by literal citation, lemma-reference, and mechanism-specific text search. Boundary rows are not accepted as global Nekovar consequences by this review.'})
write('SOURCE-PINS.json', {'author_manifest':pin(AUTHOR/'MANIFEST.json'),'author_files':author_manifest['files'],'manuscript':pin(ROOT/MANUSCRIPT),'primary_sources':[{'url':'https://www.jmilne.org/math/Books/ADTnot.pdf',**pin(book),'pages':347,'role':'Second-edition primary theorem and proof source'},{'url':'https://www.jmilne.org/math/Books/add/ADT2006.pdf',**pin(addendum),'pages':10,'revision':'2025-10-26','role':'Complete official second-edition corrections and addenda'},{'url':'https://www.jmilne.org/math/Books/adt.html',**pin(HERE/'local-only/edition.html'),'role':'Author publication/edition identity'}],'distribution':'The local-only directory is excluded from the review handoff. Source PDFs, page images and full source extractions are not proposed for repository installation.'})
source_pins = json.loads((HERE/'SOURCE-PINS.json').read_bytes())
source_pins['author_successors'] = successors
write('SOURCE-PINS.json', source_pins)
write('CHECKS.json', {'schema':'bounded-independent-source-checks/v1','reviewer':'/root/astra_quartic_opt05_anchor','author_manifest_verified':True,'author_files_verified':len(author_manifest['files']),'all_frozen_consumer_spans_verified':True,'official_book_equals_author_copy':True,'official_addendum_pages':10,'direct_milne_citations':citations,'current_occurrence_records':len(rows),'brauer_replacement_exact':True,'brauer_replay_sha256':H(candidate),'brauer_replay_bytes':len(candidate),'unchanged_prefix_and_suffix':True,'isogeny_orientation_vector':orientation,'finite_arithmetic_sanity_checks':'passed; do not prove the source theorems','primary_pages_visually_inspected':[28,42,67,98,99,100,164],'limits':['No author code executed.','No manuscript or successor004 change.','No global proof/gate approval.','The mathematical decisions are in REVIEW.md, not inferred from these checks.']})
checks = json.loads((HERE/'CHECKS.json').read_bytes())
checks.update({'successor_manifests_verified':2,'successor_files_verified':8,'successor_main_mathematical_sections_identical_to_R1':True,'successor_consumer_spans_verified':True,'addendum_pages_visually_inspected':[2,3]})
write('CHECKS.json',checks)
print(json.dumps({'checks':'passed','citations':len(citations),'occurrences':len(rows),'brauer_replay_sha256':H(candidate)}))
