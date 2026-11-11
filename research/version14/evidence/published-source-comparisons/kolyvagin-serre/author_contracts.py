"""Author proposed source contracts; all independent decisions remain unset."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sha = lambda data: hashlib.sha256(data).hexdigest()
candidate = HERE / 'quartic_v14.source-proposal.tex'
raw = candidate.read_bytes()
assert sha(raw) == '1a00bb350cea66b0e205f78a937d7eade1c0cf3c793b5ddc7e2b85f2615d06c4'
text = raw.decode('utf-8')
lines = text.splitlines(keepends=True)

def excerpt(first, last):
    start = next(i for i, line in enumerate(lines) if first in line)
    end = next(i for i in range(start, len(lines)) if last in lines[i])
    return {'pin': {'path': str(candidate.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha(raw)},
            'start_line': start + 1, 'end_line': end + 1,
            'excerpt_sha256': sha(''.join(lines[start:end+1]).encode())}

def source(name, file, url, locator):
    path = HERE / file
    data = path.read_bytes()
    return {'id': name, 'pin': {'path': str(path.relative_to(ROOT)).replace('\\', '/'),
            'sha256': sha(data), 'bytes': len(data)}, 'url': url, 'locator': locator,
            'redistribution': 'Local audit only; source PDF is not a proposed repository artifact.'}

sources = [
    source('kolyvagin-icm1991', 'icm1990.pdf',
           'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1990.1/ICM1990.1.ocr.pdf',
           'ICM Kyoto 1990, published 1991, volume I, article pp429-436; Theorem1 p430, Theorems2-5 p431; PDF517-524'),
    source('serre-1989-tate', 'serre-published.pdf',
           'https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf',
           '1989 Addison-Wesley reprint; III section1.1 ppIII1-4; section1.2 pIII7; AppendixA.7 Theorem3 ppIII52-53'),
    source('serre-1979-errata', 'serre1979-errata.pdf',
           'https://www.numdam.org/article/AST_1979__65__155_0.pdf',
           'Groupes algebriques associes aux modules de Hodge-Tate, Asterisque65 (1979), pp155-188; errata p188'),
]

k_loc = excerpt(r'\begin{lemma}[Forward analytic rank zero', r'\end{proof}')
t_loc = excerpt('It gives a cuspidal eigenform up to character twist.', 'This duality preserves the conductor.')

k_specs = {
    'source_hypotheses': ('Modular elliptic curve over Q with analytic rank at most1.', 'A/Q is the elliptic curve in the forward-rank lemma; modularity is supplied separately by BCDT.', 'The final theorem has no residual-image condition or prime exclusion; BCDT final-source review remains separate.'),
    'constructed_objects': ('The usual elliptic L-function at s=1, Mordell-Weil rank and the full localization-kernel Sha.', 'The manuscript uses those same objects before passing to the2-primary Kummer sequence.', 'Published p429 defines Sha with all places; p430 fixes L and analytic rank.'),
    'index_domain_coverage': ('Every modular elliptic curve over Q in analytic ranks0 or1.', 'The entire family in the lemma is covered, since each curve is modular and its assumed analytic rank is at most1.', 'The inclusive inequality was checked in the actual printed page, not OCR alone.'),
    'transition_maps': ('Auxiliary-field restriction if the explanatory proof chain is used.', 'The manuscript restricts Sha(Q) to Sha(K) and retains its finite2-torsion kernel.', 'Published p431 explicitly gives this containment; no isomorphism between the two Sha groups is asserted.'),
    'consumed_object_identity': ('Rank and finiteness over Q.', 'Exactly A(Q) and Sha(A/Q) enter the Kummer sequence.', 'Theorem1 directly supplies the Q-result; Theorems3-5 explain the auxiliary route and do not replace the final object.'),
    'coefficient_conventions': ('Integral group rank and finiteness of the entire Sha.', 'The downstream corank is over Z2 after tensoring A(Q) by Q2/Z2.', 'Finite Sha contributes zero corank, so the corank equals the same integral rank.'),
    'local_conditions': ('Modular parametrization X0(N) to A; the full Sha at every place.', 'N is the conductor, and BCDT supplies the modularity input.', 'The theorem is global; it requires no ordinary or good reduction at2.'),
    'exceptional_cases': ('Both analytic ranks0 and1; no higher-rank conclusion.', 'The lemma assumes r at most1; all later uses are in this range.', 'Neither the cited theorem nor this replacement establishes a converse or the restricted2-converse.'),
    'downstream_consumption': ('Forward rank and finiteSha for the two curves after the restricted converse.', 'The pole-completeness argument consumes rank1 and finiteSha after applying RC.', 'Only the citation edition and page locator change. RC and all other inputs stay independently pending as applicable.'),
}
t_specs = {
    'source_hypotheses': ('Abelian p-adic representation of a finite local extension, Hodge-Tate with semisimple inertia.', 'Base field Q5, finite coefficient field E, one-dimensional E-valued deRham character.', 'Restriction of scalars is Hodge-Tate; multiplication in E diagonalizes after scalar extension, including on inertia.'),
    'constructed_objects': ('Finite-dimensional Qp-vector space with continuous Galois action.', 'The underlying Q5-vector space of the E-line.', 'The representation used by Tate is this restriction of scalars, not an incorrectly assumed Q5-valued character.'),
    'index_domain_coverage': ('All inertia elements and a nonempty local-unit neighborhood in the local algebraicity conclusion.', 'The entire character restriction is semisimple; the theorem supplies an open subgroup of local units.', 'No finite list of units is substituted for the open-subgroup assertion.'),
    'transition_maps': ('Local reciprocity and an algebraic torus morphism.', 'G_m maps to GL_Q5(E) and then to Res_E/Q5 G_m because it commutes with E on a Zariski-dense open subgroup.', 'Weil-restriction adjunction identifies this morphism with an integral power; the inverse in Serre reciprocity agrees with the cyclotomic unit convention.'),
    'consumed_object_identity': ('The actual twisting character is finite order times an integral cyclotomic power.', 'The power comes from the algebraic map; the quotient has finite inertia at5 and at the other finitely many ramified primes.', 'Class field theory over Q factors the quotient through a finite ray-class group, so it is the same global character up to that power.'),
    'coefficient_conventions': ('Q5-linear Hodge-Tate condition and Serre local reciprocity convention.', 'Finite E/Q5 coefficients; manuscript Tate convention assigns cyclotomic weight-1.', 'The argument tracks the inverse on local units and only then compares weight multisets; it does not assume identical sign notation in Serre.'),
    'local_conditions': ('Finite base field over Qp, local algebraicity only near1.', 'Q5 satisfies the source hypotheses. Other local inertia groups are addressed through local class field theory and the pro-l/pro-5 argument.', 'Finitely many ramified places allow one finite global conductor. The real place is included in the ray modulus when needed.'),
    'exceptional_cases': ('No assertion for nonabelian representations or infinite coefficient fields; negative powers allowed.', 'The twisting character is abelian and defined over a finite coefficient extension; the integral power can have either sign.', 'The surrounding proof establishes its deRham property separately; that premise is retained rather than inferred from this theorem.'),
    'downstream_consumption': ('The modular twist becomes finite after matching the two Hodge-Tate weights.', 'The existing weight comparison forces weight2 and zero cyclotomic exponent; the finite Dirichlet character is absorbed into the eigenform.', 'The replacement supplies exactly the character classification used there. Modularity, weight comparison, Shimura and Li inputs remain separately inventoried.'),
}

applications = []
for identity, old, specs, location, supplier in [
    ('V14-SOURCE-KOLYVAGIN-PUBLISHED', ['A020', 'A082'], k_specs, k_loc, sources[0]['id']),
    ('V14-SOURCE-TATE-LOCAL-ALGEBRAICITY', ['A011'], t_specs, t_loc, sources[1]['id']),
]:
    obligations = {key: {'required': req, 'constructed': con, 'justification': why,
        'evidence': [location], 'status': 'unresolved_independent_review'}
        for key, (req, con, why) in specs.items()}
    applications.append({'id': identity, 'affected_inherited_applications': old, 'authors': ['/root'],
        'kind': 'source_replacement', 'supplier': supplier, 'status': 'unaccepted author proposal',
        'obligations': obligations})

record = {'schema': 'proposed-nine-obligation-contracts/v1', 'author': '/root',
    'status': 'All independent decisions remain unset. Serre errata scope is being checked by the independent reviewer.',
    'candidate_sha256': sha(raw), 'sources': sources, 'applications': applications,
    'unresolved_sources': ['Lauter-Naehrig-Yang final coordinate normalization', 'Jetchev-Kane final geometric/adelic descriptions']}
dest = HERE / 'APPLICATION-CONTRACTS.json'
dest.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
files = [{'path': p.name, 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size}
         for p in [Path(__file__), dest]]
(HERE / 'CONTRACT-MANIFEST.json').write_text(json.dumps({'files': files, 'candidate_sha256': sha(raw)}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'applications': len(applications), 'obligations': sum(len(a['obligations']) for a in applications),
                  'independent_acceptance': None}))
