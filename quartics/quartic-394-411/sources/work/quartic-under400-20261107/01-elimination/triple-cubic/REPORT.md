# Three cubic groups give 470 total variables

This packet changes the frozen combined486 presentation to 470 total rational
variables, including the input, with 439 quadratic residuals. Their primitive
integer sum of squares has degree four, 6,646 nonzero monomials, content one,
and largest coefficient `16*3^(2^26)`. The fixed coefficient parameter remains
`C=3^(2^25)`. No coefficient is expanded into its enormous decimal value.

The author has checked exact polynomial identities, every outside consumer,
all nine elimination certificates, and the complete sum of squares. Independent
acceptance of this new packet is pending. It improves the independently reviewed
476 presentation by six variables but starts from the same frozen486 source.
It does not meet the requested publication threshold of fewer than 400 variables.
The previously accepted478/476 files have not been changed.

## Frozen artifacts

| Artifact | SHA-256 |
| --- | --- |
| `baseline486.json` | `55043867418ca00c68add72560b11055c71d082747d6bea61522168885875787` |
| `candidate479-ir.json` | `e8aea4b56037c0be0a8e9906e377bceea8c7bebd8fc3bf3314366032cfeae1f7` |
| `elimination/candidate470-ir.json` | `eff9369864da6bd2ed46fa300f51f5a0cc9217d3b790380713644ee31f512b72` |
| `elimination/elimination470-certificate.json` | `561d709106bc7e580b8ee237645204b4aeb038ea5ffa4cffb678c9ba247a4744` |
| `elimination/polynomial470.json` | `80a23d972ee8bc4d04a2cb002b480395cada31b6580ee2bb765df52f9e7bf74c` |

The semantic reference is the released depth519 residual artifact, SHA-256
`4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.
Source486 has the same test-square expressions and IDs, with order12 labels
changed to order10 in its evaluation and weights. The shared symmetric rows
retain their historical order12 names. The checker handles these aliases
explicitly and verifies the actual polynomial identities.

## Exact detector replacement

Write the retained squared field test values as `Y_i` in `Q(sqrt(2))`. Each
order output is `product_i (1+q*Y_i)`. For order1, the nine source factors have
indices `[U1,U2,U3,U4,V0,V1,V2,V3,V4]`; these labels mean their squared test
values, including the existing conjugation convention on the V side.

The new grouping is

```text
order1:  [V0,U1,U2], [V1,U3,U4], [V2,V3,V4]
order10: one pair
order40: the original pair and triple
```

The implementation records the order1 index permutation `[4,0,1,5,2,3,6,7,8]`.
Within each group, it shares polynomial coefficients between all three
detectors, evaluates using retained powers of q, and multiplies group values.
It initially retains q1^5 because the order10 toric equations consume it.
This first step yields 479 variables, 448 residuals, and 6,418 SOS monomials.

As in the accepted478 construction, six old affine-normalized W coordinates
are changed to the literal rational components of W. The certificate gives
each map `oldW=(newW-rest)/a` with nonzero rational constant a. Every outside
row is substituted exactly, and every deleted private coordinate cancels.
No shared semantic value or branch condition is changed.

The checker solves the old and new private circuits by constant pivots. It
expands and compares all nine order outputs against the same complete factor
polynomials, then checks the small final W multiplication networks using the
already established order outputs. It checks every outside row under the six
coordinate maps. Thus factor reordering is proved by exact identities, not
assumed from matching labels. Private reconstruction is unique and polynomial
in retained inputs, and the W maps divide only by nonzero constants. Forward
and reverse maps retain shared values, reconstruct the respective private
circuits, and apply these inverse W coordinate maps. Both maps fix the input.

## Nine further eliminations

For a triple of field values a,b,c, the coefficient construction initially
stores d=bc, e2=a(b+c)+d, and e3=ad. Eliminate d using

```text
d = e2-a(b+c),
e3 = a*e2-a^2*(b+c).
```

For the chosen first roots V0,V1,V2, the existing logarithm equations already
express a^2 through retained coordinates. The final equation is therefore
quadratic. This removes two rational coordinates from each of three triples.
The exact component certificates use retained source rows132/133 for V0,
144/145 for V1, and150/151 for V2. They check all affine normalizations rather
than treating the stored coordinates as raw field components.

Finally, the sole remaining consumer of each q1^5 coordinate is its toric
equation. Substituting `q1^5=q1^2*q1^3` directly into that consumer stays
quadratic. This removes one further coordinate for each of three detectors.
The exact final equations replace source rows545,551,557, respectively.

For each elimination x=q, the replay checker verifies a nonzero constant
pivot, all affected rows, and the identity

```text
newRow = oldRow[x:=q] + sum_j multiplier_j * unchangedRow_j.
```

Every multiplier is free of x, and each unchanged row is outside the affected
set. The checker compares the resulting entire coordinate and residual maps
with the candidate. In the forward direction, old solutions satisfy the new
rows after forgetting x. In reverse, insert x=q; unchanged rows vanish, so
every old row vanishes. Repeating this for all nine steps proves exact rational
solution-set equivalence and hence preservation of the input projection.

## Reproduction and limits

From this directory run `python -B build_candidate.py`, followed by
`python -B check_hybrid_semantics.py`. The latter imports only the released
polynomial arithmetic helper, not the producer. It writes the full circuit
certificate and `HYBRID-VERIFICATION.json`.

From `elimination`, run `python -B verify_result.py`. It uses only Python's
standard library and imports neither the producer nor the search. It replays
the saved exact certificate and expands the final sum of squares. Its result
is `VERIFIED470.json`. The optional command `python -B macaulay_search.py 2000`
reproduces the nine eliminations from `baseline498.json`, whose historical
filename contains an exact copy of candidate479, not the released498 system.

The working local executable is `C:/Users/glaze/.local/bin/python3.14.exe`.
These checks take seconds and one Python process. The finite equivalence proof
adds no arithmetic premise. The arithmetic input-projection theorem remains
the separately reviewed dependency of source486. No global minimality claim
is made, and no released repository or manuscript was edited.
