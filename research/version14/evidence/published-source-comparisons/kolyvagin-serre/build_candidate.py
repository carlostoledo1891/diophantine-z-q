"""Create a separate source-replacement proposal; never alter release TeX."""
from pathlib import Path
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT / 'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex'
sha = lambda data: hashlib.sha256(data).hexdigest()
raw = BASE.read_bytes()
assert sha(raw) == 'b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d'
original = raw.decode('utf-8')
edits = [
    ('kolyvagin-application',
     r'Apply \cite[Theorem 1, pp.~4--5]{kolyvagin}, whose statement',
     r'Apply \cite[Theorem 1, pp.~430--431]{kolyvagin}, whose statement'),
    ('kolyvagin-bibliography',
     r'''\bibitem{kolyvagin} V. A. Kolyvagin,
\emph{On the Mordell--Weil group and the Shafarevich--Tate group
of modular elliptic curves}, MPIM preprint MPI/90-69 (1990),
Theorems 1--5, pp.~4--5.
\url{https://archive.mpim-bonn.mpg.de/id/eprint/325/1/preprint_1990_69.pdf}.''',
     r'''\bibitem{kolyvagin} V. A. Kolyvagin,
\emph{On the Mordell--Weil group and the Shafarevich--Tate group
of modular elliptic curves}, Proceedings of the International Congress
of Mathematicians, Kyoto 1990, Vol.~I, Mathematical Society of Japan,
1991, pp.~429--436, Theorems 1--5, pp.~430--431.
\url{https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1990.1/ICM1990.1.ocr.pdf}.'''),
    ('local-character-application',
     r'''The twisting
character is a de Rham subrepresentation of the Hom representation
and is unramified outside finitely many primes. Local algebraicity
\cite[Appendix B, pp.~32--33]{conrad-local-characters} and class field
theory over $\mathbb Q$ make it a finite character times an integral
power of the cyclotomic character: removing its integral local
Hodge--Tate weight leaves finite inertia at five and at every other
prime, hence a finite ray-class character.''',
     r'''The twisting
character is a de Rham subrepresentation of the Hom representation
and is unramified outside finitely many primes. Choose a finite
coefficient extension $E/\Q_5$ containing its values. On the underlying
$\Q_5$-representation, inertia acts semisimply: after scalar extension
to $\overline{\Q}_5$, multiplication in $E$ splits under the embeddings
of $E$ as a direct sum of characters. Tate's local-algebraicity theorem
\cite[Chapter III, \S1.2 and Appendix A.7, Theorem 3]{serre-ladic-published}
therefore applies. The associated algebraic map from $\mathbb G_m$
commutes with $E$, since it does so on an open subgroup of $\Q_5^\times$.
It consequently takes values in $\operatorname{Res}_{E/\Q_5}\mathbb G_m$.
The adjunction defining restriction of scalars identifies such maps
with the integer powers of $\mathbb G_m$ over $E$. Taking account of
the inverse in the source's reciprocity convention, the twisting
character agrees on an open inertia subgroup with an integral power
of the cyclotomic character. Dividing by that power leaves finite
inertia at five and at every other prime. Class field theory over
$\mathbb Q$ then makes the remaining character a finite ray-class
character.'''),
    ('local-character-bibliography',
     r'''\bibitem{conrad-local-characters} B. Conrad,
\emph{Lifting global representations with local properties},
author preprint, December 11, 2011, Appendix B, pp.~32--33.
\url{https://math.stanford.edu/~conrad/papers/locchar.pdf}.''',
     r'''\bibitem{serre-ladic-published} J.-P. Serre,
\emph{Abelian $\ell$-adic representations and elliptic curves},
Addison--Wesley, 1989, reprint of the 1968 edition,
Chapter III, \S1.2, p.~III-7, and Appendix A.7,
Theorem 3, pp.~III-52--53.
\url{https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf}.'''),
]
candidate = original
rows = []
for identity, before, after in edits:
    if candidate.count(before) != 1:
        before = before.replace('\n', '\r\n')
        after = after.replace('\n', '\r\n')
    assert candidate.count(before) == 1, identity
    start = original.index(before)
    rows.append({'id': identity, 'base_start_line': original[:start].count('\n') + 1,
                 'before': before, 'after': after, 'before_sha256': sha(before.encode()),
                 'after_sha256': sha(after.encode()), 'status': 'proposed_pending_independent_acceptance'})
    candidate = candidate.replace(before, after)
assert 'conrad-local-characters' not in candidate
(HERE / 'quartic_v14.source-proposal.tex').write_bytes(candidate.encode('utf-8'))
(HERE / 'EDITS.json').write_text(json.dumps({'base_sha256': sha(raw), 'candidate_sha256': sha(candidate.encode()),
    'author': '/root', 'independent_acceptance': None, 'edits': rows}, indent=2) + '\n', encoding='utf-8')
(HERE / 'PROPOSED.patch').write_bytes(''.join(difflib.unified_diff(original.splitlines(True), candidate.splitlines(True),
    fromfile='base/quartic_v14.tex', tofile='proposal/quartic_v14.tex')).encode('utf-8'))
names = ['COMPARISON.md', 'build_candidate.py', 'EDITS.json', 'PROPOSED.patch', 'quartic_v14.source-proposal.tex']
files = [{'path': name, 'bytes': len((HERE / name).read_bytes()), 'sha256': sha((HERE / name).read_bytes())} for name in names]
(HERE / 'PROPOSAL-MANIFEST.json').write_text(json.dumps({'author': '/root', 'status': 'pending_independent_review',
    'files': files, 'source_pdfs_local_only': True}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'candidate_sha256': sha(candidate.encode()), 'edits': len(rows), 'release_manuscript_changed': False}))
