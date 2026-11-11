# Independent finite review of the combined candidate

The frozen 505-coordinate candidate passes this independent finite and
source-fidelity review. I found no coefficient, coordinate transport,
unrecorded deletion, hidden-consumer, or fixed-parameter error. I accept the
finite construction in the scope below. This does not independently accept
the arithmetic projection proofs for the changed depth, chart, anchor, or
scalar blocks.

I authored none of these five transformations or their combination. The
previous work in the parent `01-elimination` directory found no improvement
and is not used in this candidate.

## Frozen artifacts

The reviewed files are copied into `snapshot/`. Their SHA-256 bindings are:

| Artifact | SHA-256 |
| --- | --- |
| `candidate505-ir.json` | `bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966` |
| `certificate505.json` | `9dbcd233afb2acc2a8d0977701a0d7252a99040a483e0170372b0bf1235869c3` |
| `polynomial505.json` | `a935109cf0617bc9b2cb12abc147251e039fdb739bde1f6369d3320175edcfcd` |
| Combination `REPORT.md` | `5bf29e4df2981ba423c5afda46548b8dd345b2f0f01f061a8378c190d14ab80a` |
| Combination `verify.py` | `fece162ea2444521637181198ef384bce8002368de2e9a1824169eefb38c8a65` |

The baseline hash is
`48a8b8f9263a97d3a1c59f3f0f3553eae628b7aba342d44003e8da840ae84928`.
The manuscript hash is
`1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`.
Every entry of the combination's `SOURCES.json` and every patch hash in its
certificate matched the file read during this review. The individual hashes
and exact row/coordinate changes are in `FINITE-REVIEW.json`.

## Checks actually rerun

I inspected and reran the standalone combination checker from the copied
snapshot with `--product`. It imports no candidate producer. It reconstructs
the expected equations and expands the sum of squares independently of the
builder. The result was:

| Quantity | Symbolic candidate | Ordinary lift |
| --- | ---: | ---: |
| Total rational coordinates | 505 | 521 |
| Existential witnesses | 504 | 520 |
| Quadratic residuals | 474 | 490 |
| Degree | 4 | 4 |
| Nonzero coordinate monomials | 24,748 | 24,795 |
| Primitive content | 1 | 1 |

The symbolic maximum coefficient magnitude is exactly
`16*C^2 = 16*3^(2^26)`, for the fixed integer `C=3^(2^25)`.
The ordinary maximum is exactly `3^2048+1005072314881896`.
Every coordinate occurs, input coordinate zero remains protected, and all
coefficients of every expanded square agree with the supplied tables.
The ordinary system has exactly sixteen extra constant-chain coordinates,
with the first equal to `3^1024` and fifteen further squarings. No huge power
was expanded.

I also wrote `review.py` independently of the combination producer. It:

* checks uniqueness of every coordinate ID/name and residual ID/name, exact
  declared support, and preservation of the protected input;
* derives each patch's removed, changed, added, and renamed objects from its
  complete comparison with the frozen baseline, then checks the certificate;
* verifies every map by exact names, including newly introduced scalar
  coordinates, and reconstructs every final residual from the pinned patches;
* requires every changed or deleted baseline row to equal its transported
  mixed-depth counterpart before applying the patch;
* checks every final coordinate name and ID, so reuse of a deleted ID cannot
  silently preserve its former meaning;
* verifies that the anchor is the only consumer of the fixed parameter both
  before and after the change from S to C.

These checks passed. In particular, the five chart inverse pairs occur only
in their ten old guard equations. The removed anchor intermediate occurs
only in its definition and anchor equation; its three private witnesses
occur only in the anchor equation. The pole substitutions were tested against
the entire mixed-depth residual system, not only against the pole rows.
There were no undeclared outside consumers. The scalar replacement keeps
both coefficients of f(S-P), and its attachment uses the actual normalized
`scalar.W2` expression.

## Depth source provenance

I reconstructed the mixed-depth builder from the frozen asymmetric builder
using exactly seven single-occurrence textual changes: the fixed-parameter
metadata correction, the V1 logarithm order, the two input-related test
orders, the list of coefficient groups, the evaluation split implementation,
and the product that includes the order-12 group. The reconstructed builder
equals the delivered builder exactly as text.

I then ran that builder in `depth-rebuild/`, with its pinned mathematical
source copied into that directory. Both raw residual systems and the census
equal the delivered depth artifacts as complete JSON objects. This closes
the gap that would remain if one checked a compiled table without checking
which raw program generated it.

Finally, I reran the existing standalone depth gate/compiler checker and all
final elimination certificates. The driver was copied and changed only to
locate `03-depth` by its absolute path; its outputs were redirected to this
review directory. The result remains 519 coordinates, 488 residuals, degree
four, and 24,986 monomials. Its table hash is
`d29a7cb7ba2f43ea4930b4e370be040fb25993854c875eaaebca3e524d22fe78`.
The exact candidate-to-normalized-row relation and full table were checked.

## Forward and reverse coverage

The following distinctions matter when describing what the certificates
prove.

The compiler operations, depth final eliminations, and shears have exact
forward and reverse rational maps. Every affected row and every retained
identity used in a reduction is covered by the replay. Constant pivots are
nonzero rational numbers. The input is fixed. These certificates establish
equivalence between their specified source and output systems; they do not
establish the mathematical validity of changing the source test orders.

For the three pole normalizations, the full polynomial substitution identities
pass with factors b^2 or b^4. The retained inverse, norm, and B equations force
b nonzero over Q: b=0 would force n=0, then w0^2=2w1^2, then w0=0, contrary
to its inverse equation. Division by the indicated powers of b therefore
gives the reverse map, and the polynomial formulas give the forward map.
This part is an algebraic equivalence of rational solution sets with the
input fixed.

The chart replacement is a strengthening, not an invertible change of every
old witness assignment. Its new guard A*c=1 implies A nonzero, hence
A^2-2B^2 nonzero, and the old inverse is reconstructed as
`(A,-B)/(A^2-2B^2)`. The five pairs have no other consumers. The converse
direction required for the integer projection is the separate completeness
argument that chooses witnesses with A nonzero. The report states this
qualification correctly; no finite certificate silently supplies that step.

The anchor replacement is an existential replacement of private witnesses.
The code checks its literal f1 coefficient, private-variable incidence,
replacement equation, and the affine translation by C. Equivalence of its
semilocal predicate with the old two-coefficient condition uses the stated
3-adic leading-coefficient argument and three-witness theorem. The exact
doubling and residue starting calculation passes, but finitely checking that
calculation alone is not a proof of the assertion for every even index.

The scalar norm tree is likewise a changed mathematical certificate. Its
eight equations and W-squared attachment match the proposal exactly, and all
outside rows are preserved. It is not algebraically equal to the old tree.
The new local valuation argument and the construction of new scalar pole
witnesses are needed for soundness and completeness. The combination report
explicitly supplies those obligations and does not claim a bijection with
old scalar-tree witnesses.

Thus no forward/reverse algebraic coverage is missing where the packet
claims algebraic equivalence. Four source-level changes still rely on their
stated mathematical proofs. The combination author's internal acceptance of
those proofs is a separate review, not a conclusion of this finite audit.
I did not independently reprove them here.

## Reproduction and disposition

From `snapshot/`, run:

```text
python -B verify.py --product
```

From this review directory, run:

```text
python -B review.py
```

The latter also regenerates `depth-rebuild/` and runs the relocated depth
certificate replay. It requires the frozen source/proposal files at the
recorded paths and Node.js, in addition to standard-library Python. On this
workstation I used `C:/Users/glaze/.local/bin/python3.14.exe`.

Disposition: finite construction accepted by independent internal model
review for the hashes above. No finite correction requested. Overall
arithmetic projection acceptance and repository release integration remain
outside this review's scope. No repository or contributor artifact was
modified, and no external theorem was newly assumed or independently
revalidated.
