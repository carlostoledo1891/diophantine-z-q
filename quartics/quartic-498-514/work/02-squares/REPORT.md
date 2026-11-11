# Three detector-square eliminations

Status: candidate awaiting independent review. The author of this packet has not independently accepted it. This packet proves an algebraic equivalence to the pinned 523-coordinate residual system, conditional on whatever arithmetic claims establish that baseline. It does not audit or strengthen those arithmetic claims.

## Result

| Quantity | Baseline | Candidate |
| --- | ---: | ---: |
| Total rational coordinates, including input | 523 | 520 |
| Existential witnesses | 522 | 519 |
| Quadratic residuals | 492 | 489 |
| Degree of sum of squares | 4 | 4 |
| Nonzero monomials after collecting fixed-S coefficient terms | 35,163 | 35,154 |
| Content | 1 | 1 |
| Largest absolute coefficient | `64 * 3^(2^27)` | `64 * 3^(2^27)` |

The fixed coefficient remains `S = 3^(2^26)`. The input coordinate is unchanged. No new arithmetic hypothesis, nonzero condition, or positivity assumption is added.

## Exact baseline

Repository-relative source: `quartics/quartic-523-540/final523_540/symbolic523/candidate-ir.json`.

SHA-256: `48a8b8f9263a97d3a1c59f3f0f3553eae628b7aba342d44003e8da840ae84928`.

The 520-coordinate polynomial has SHA-256 `fc381687af90a783ad39e9379b7ce4de7d6126fe0d880d9d717a21b5f696ed47`.

## The transformation

Perform the following separately in detector blocks 0, 1 and 2. Write `b` for the baseline coordinate named `detector{k}.B`. This is the pole input, so the quantity called `B` in the mathematical pole equations is `17b`.

The pole contains coordinates `e,p,s,q,p2,s2,q2,u2,f`, where the last coordinate is the compiler-normalized `Bh.quadratic`. Its seven residuals are

```
p^2 - p2 = 0
17b p2 + 3e^2 - 34eb - 289b^2 = 0
b^2 - u2 = 0
17eb - e u2 - 17f = 0
s^2 - s2 = 0
q^2 - q2 = 0
17b q2 + 867f^2 - 34f s2 - s2^2 = 0.
```

Thus the stored `f` equals the mathematical `Bh/17`. This factor must be retained when translating this packet to another representation.

Use new coordinates `E,P,T,Q,P2,T2,Q2,F`, with the old coordinates recovered by

```
e = bE           p = bP           s = bT           q = b^2 Q
p2 = b^2 P2      s2 = b^2 T2      q2 = b^4 Q2
u2 = b^2        f = b^2 F.
```

The letter T here is just the normalized s witness; it has no relation to the elliptic point named T elsewhere in the construction. The actual JSON preserves original coordinate IDs and marks their names as normalized.

Replace the seven old residuals with these six:

```
P^2 - P2 = 0
17b P2 + 3E^2 - 34E - 289 = 0
17E - Eb - 17F = 0
T^2 - T2 = 0
Q^2 - Q2 = 0
17b Q2 + 867F^2 - 34F T2 - T2^2 = 0.
```

Every residual is quadratic. The removed coordinate is `u2`, named `detector{k}.U2.quadratic`. Its IDs in the pinned source are 399, 443 and 487. All other coordinate IDs remain unchanged in the residual artifact. The polynomial table alone renumbers surviving coordinates consecutively, recording the source ID for each.

Under the displayed substitution, the old `u2` residual becomes identically zero. The old `p2`, first-conic, `Bh`, and `s2` residuals equal `b^2` times their respective new residuals. The old `q2` and second-conic residuals equal `b^4` times their new residuals. Every other old residual is unchanged. The verifier checks these statements on the actual complete sparse polynomials, not just the displayed block formulas.

## Why division by b is legitimate

Both systems retain the same three guard equations in each detector. With `w0,w1` the exact affine expressions saved in the baseline and `n` the baseline `normOver2w0` coordinate, these equations give

```
w0 * inverse = 1
w0^2 - 2w1^2 - 2w0*n = 0
n^2 + b*A = 0
```

Here A is the exact retained affine expression in `eWeight` and `eDelta.quadratic`; its coefficients differ between detector blocks because of compiler normalizations. Its value is irrelevant to this proof. The checker verifies the first two identities and checks that setting `b=0` in the third gives exactly `n^2`.

If `b=0`, then `n=0`, so `w0^2=2w1^2`. Since 2 is not a square in Q, this implies `w0=w1=0`, contrary to the first equation. Thus `b` is nonzero in every rational solution of either full system. This argument uses no claimed positivity of a complicated polynomial and no unchecked denominator cancellation.

Given an old solution, divide its listed coordinates by the appropriate powers of b and delete u2. The retained guard proves these rational divisions are defined. The exact residual identities then imply the new equations. Given a new solution, the displayed polynomial formulas recover an old solution. These operations are mutual inverses, including `u2=b^2`, and fix the input.

## Sum of squares and coefficient table

For each residual, clear rational denominators and divide integer content. Sum the resulting squares. Rational squares are nonnegative, so their sum is zero exactly when every residual is zero. This gives the same existential projection over Q.

`polynomial520.json` contains the complete sparse table. Coefficients use integer multiples of powers of the fixed S. Here no two distinct S powers occur at the same variable monomial. The largest S-free coefficient has fewer than 2048 bits, every coefficient linear in S has multiplier at most 768, and the unique S-squared term is `64*S^2*anchor.U^2`, with no lower-S contribution to that monomial. Since the stipulated S exceeds `2^2048` and 12, the largest absolute coefficient is exactly `64*S^2`.

## Reproduction

From this directory, using Python 3.10 or newer:

```
python -B build.py
python -B verify.py
```

`build.py` writes only this packet's artifacts. `verify.py` is read-only, uses only the standard library, and imports neither the producer nor its polynomial implementation. It checks the pinned baseline hash, every residual substitution, the concrete nonzero guards, coordinate coverage, degree, primitive content, full polynomial expansion, counts, and the coefficient maximum. Its expansion uses upper-triangular square collection, separately implemented from the producer's full multiplication.

The producer's `search.py` dependency also contains an earlier bounded elimination search. Running `search.py` is not required for reproduction of this candidate. Its result file reports that none of 396 tested constant-pivot substitutions yielded another quadratic system through the explored unaffected-row multiples: 333 failed within the completed closure, and 63 hit the 1,500-monomial bound. This is only a negative finding for that bounded search, not a lower bound on the number of coordinates.

No shared manuscript, baseline source, audit ledger, or release file was edited. The packet is ready for a separate reviewer to test both the algebraic argument and the executable certificates.
`quartics/quartic-523-540/final523_540/verify_all.py` also passed on the baseline repository. It confirmed the nine prior eliminations, the 523/540 coordinate counts, and the 35,163/35,213 monomial counts.
