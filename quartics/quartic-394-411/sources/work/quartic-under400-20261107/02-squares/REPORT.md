# Pole and square-circuit candidates below the frozen 498-variable source

This packet contains a 494-variable transport of the earlier factored-pole construction and a new 493-variable candidate. Neither changes the published Version 12 source. No candidate below 400 variables has been found in this workstream.

## Baselines must be kept separate

The old 497-variable candidate in `work/quartic-optimization-20261107/02-squares/factored` starts from the old 501-variable source and removes four second-conic square coordinates.

The frozen Version 12 498-variable source instead starts from that same 501-variable source and removes two scalar denominator-square coordinates and one scalar norm-square coordinate. It excludes the four factored-pole changes. Thus transporting the four factorizations to frozen 498 gives 494, not 497 and not 490.

`build494.py` checks the affected source rows by exact coordinate names and polynomial equality before transporting them. The scalar reciprocal and norm changes are disjoint. `verify494.py` independently checks every old residual under simultaneous polynomial reconstruction, the exceptional branches, and the full sum of squares.

| Stage | Total variables | Witnesses | Residuals | Degree | Monomials |
| --- | ---: | ---: | ---: | ---: | ---: |
| Frozen v12 | 498 | 497 | 467 | 4 | 24,669 |
| Four factored second conics | 494 | 493 | 463 | 4 | 24,653 |
| Guarded scalar-preparation conic | 493 | 492 | 462 | 4 | 24,645 |

Every stage here has primitive content one. The fixed integer remains C=3^(2^25), and the largest coefficient magnitude remains 16*C^2.

Frozen source: `work/quartic-version6-release/repository/quartics/quartic-498-514/candidate498-ir.json`.

Frozen source SHA-256: `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.

Candidate494 SHA-256: `fc6ae1c382688596b5434f2412700ac42f4b800e0a8d4f2ff28b5151f3c45ccf`.

Candidate493 SHA-256: `c4298c8a7e147797e0ab8e1cc3e7e3d3f4431d29609fec394154345306441b2d`.

Polynomial493 SHA-256: `63b56d3582ea1732f25b9b02e0f7ae0a2ba0a64b722d941915a31141ab41f2ea`.

## The new scalar-preparation reduction

Write b for the actual scalar pole input. The old preparation has five coordinates t,z,T,W,N, with four equations

```
z = t^2,
b(T-z) = 1,
TW = 2,
N = (W-b)^2.
```

Here W-b is the semantic prepared quantity U, and N=U^2 is the only prepared quantity consumed outside this private block. The old equations give

```
U = b(1-bt^2)/(1+bt^2).
```

Replace the five coordinates by four coordinates U,J,V,N, with three equations

```
N = U^2,
bJ = 1,
JN + V^2 = b.
```

All equations are quadratic, and b remains explicitly nonzero. Multiplying the last equation by b gives the conic

```
U^2 + bV^2 = b^2.
```

The explicit inverse equation is essential. The unguarded conic by itself would allow b=U=0 and would not preserve the source's domain. The new circuit retains that guard without using an extra coordinate beyond the four listed above.

### Old solutions give new solutions

For every old solution set

```
U = W-b,
J = T-z,
V = tW,
N = N.
```

This map is polynomial. The first new equation is the old fourth equation, and bJ=1 is the old second equation. To verify the conic equation, use z=t^2, T=z+J, TW=2 and bJ=1:

```
JN+V^2
 = J(W-b)^2 + t^2 W^2
 = (J+z)W^2 - 2bJW + b^2J
 = TW^2 - 2W + b
 = b.
```

`verify493.py` checks the corresponding full polynomial identity with explicit multiples of the four old residuals. It also verifies that t,z,T,W have no consumers outside those four rows.

### New solutions give old solutions

The inverse equation gives b nonzero. Put d=b+U.

If d is nonzero, define

```
t = V/d,
z = t^2,
T = z+J,
W = d.
```

The conic identity implies `TW=2`. One can check this without dividing by b again: after multiplying the desired equation by d, its residual is a polynomial combination of `U^2-N`, `1-bJ`, and `JN+V^2-b`. The verifier checks that exact identity. Also W-b=U, so N is unchanged.

If d=0, then U=-b, N=b^2 and J=1/b. The last conic equation gives V^2=0, hence V=0 over Q. Define instead

```
t=0, z=0, T=J, W=2b.
```

These values satisfy all four old equations. In this case W-b=b, which is the negative of the new U, but its square N is exactly the same. Only N is consumed downstream, so this sign change does not affect any other equation.

These two cases cover every rational new solution. No positivity, genericity or extra arithmetic assumption is needed for this preparation replacement. It preserves the projection onto every coordinate outside the block, including N and the input.

## Actual coefficient normalization

In the frozen source the stored scalar input coordinate b0 represents b=-K*b0, where

```
K=80990493410131000784375977023646274345820490095244015289194989569855772668241364832628280392076492800000000000000.
```

The stored N coordinate represents N=K^2*N0. The new rows in actual source IDs are

```
U^2 - K^2*N0 = 0,
1 + K*b0*J = 0,
K^2*N0*J + V^2 + K*b0 = 0.
```

The old coordinate 50 becomes U, 528 becomes J, 529 becomes V, and 530 is removed. Coordinate 531 remains N0, with its original meaning. `certificate493.json` records all row and coordinate IDs and the exact K. The check does not infer signs from coordinate names.

## Four factored second conics and simultaneous completeness

The 494 stage transports the previously documented replacements `F=t*v`, `q=t*Q`, `q2=t^2*Q2`, `t2=t^2` in the three detector poles and scalar pole. Their polynomial reconstruction works on every rational new solution, including t=0.

For completeness, the existing construction provides positive semantic pole inputs. When t is nonzero the inverse divides F and q by t. When t=0, the old second conic with positive input forces F=q=0, and the zero lift supplies the new coordinates. The stored scalar input is negative under its compiler normalization; the checker uses its actual semantic sign.

The new preparation equivalence fixes N and the semantic scalar input b. Therefore it composes with that positive-input completeness construction without changing any detector condition, scalar pole quantity, or previously chosen root, scale, prime, or congruence. The 494 stage needs the existing positive-pole completeness property; the 493 stage adds no further requirement.

Detailed earlier factored-pole proofs remain untouched in `work/quartic-optimization-20261107/02-squares/factored/REPORT.md` and `REPORT497.md`. This transport does not claim that the author independently reviewed those earlier self-authored transformations.

## Further searches and limits

A targeted search found no further saving from multiplying the five essential variables in a factored detector block by integer powers of its nonzero input b. This has an exact parity explanation.

For the first conic, rescale E=b^a E' and p=b^c p'. The E'^2 and p'^2 terms have b exponents 2a and 1+2c. To obtain a quadratic residual directly, after clearing a common b power, both exponents must become zero. This requires 2a=1+2c, impossible for integers a,c.

For the factored second conic, rescale t=b^d t', v=b^h v', Q=b^f Q'. Its quadratic terms have b exponents 2d,d+h,2h,1+2f. Direct quadratic degree would require them all equal, again impossible by parity. `search_rescalings.py` confirms this over exponents -12 through 12; the parity arguments prove the stated restricted obstruction for all integer exponents. This is not a lower bound for arbitrary coordinate changes or other arithmetic presentations.

I also considered removing the scalar W^2 attachment by rescaling all scalar pole witnesses by the norm-tree value W. That naive replacement loses the W nonzero guard formerly supplied by the preparation equation. Adding an explicit guard cancels the apparent saving. No candidate from that route is claimed.

## Reproduction and review status

```
python -B build494.py
python -B verify494.py
python -B build493.py
python -B verify493.py
python -B search_rescalings.py
```

The producers use the existing sparse-arithmetic helper code. The verifiers import no producer and implement their own rational polynomial operations. `verify493.py` first checks the 494 transport, then checks all scalar-preparation identities, both inverse branches, complete outside-block preservation, and the full 493 sum of squares. Its output is in `verification493.txt`.

All stated exact checks passed. This packet supplies candidates for independent review and composition. It does not authorize a release or claim that the below-400 threshold has been reached. The frozen manuscript and repository were not modified.
