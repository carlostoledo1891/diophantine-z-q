# Independent review of the scalar norm replacement

I accept the scalar norm replacement in `06-product/REPORT.md`, at the hashes below, and its literal scalar equations in `10-combination/candidate505-ir.json`. I found no blocking mathematical issue and no required repair to those equations. This is an internal model review, conditional on the inherited manuscript results, not an independent proof of those results.

My independence is limited to this scalar replacement: I did not author approach 06. I authored the separate five-guard chart replacement used in the combination. This document therefore does not independently approve the entire 505-variable combination, my chart replacement, the depth change, or the new anchor.

## Bound artifacts and evidence

| Artifact | SHA-256 |
| --- | --- |
| `06-product/REPORT.md` | `d052ad884b7f73186f68a711e31e5667338b81061dd1d9f23471f03a779f8eef` |
| `06-product/candidate518-ir.json` | `7dc601732d8c2d5236d41effbfb116e95d2d0187f010707e506b22161d47aee5` |
| `10-combination/candidate505-ir.json` | `bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966` |
| Original 523-variable residual system | `48a8b8f9263a97d3a1c59f3f0f3553eae628b7aba342d44003e8da840ae84928` |
| `03-depth/beta12/final/candidate-ir.json` | `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c` |
| `manuscripts/quartic_v11.tex` | `1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662` |

I read the actual arguments at `v5:scalar32-bridge`, lines 10422–10558; `hyp:o8-pole`, near line 7713; `lem:original-seven-parity-completeness`, near line 7886; `lem:v5-point-domains`, near line 10777; `lem:v5-unramified-log`, near line 10813; `lem:quartic-doubled-private-comparison`, near line 9404; the scalar source equations near lines 10912–10950; and the Version 9 bridge and shifted-scalar completeness near lines 19268–19323 and 19578–19664. I also read the source builder, approach 06 verifier, and combination builder and verifier, then checked the actual combined residuals separately.

For the published formal-group input, I verified the PDF hash `72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25` for `work/astra-final-size-independent-review-001/silverman-2009.pdf`. I read Proposition IV.5.5, Lemma IV.6.3 and Theorem IV.6.4 in the source extraction `work/theorem-application-audit-20261105/primary/silverman.txt`, printed pages 129–132. These give the normalized logarithm, its homomorphism property, and the valuation-preserving isomorphism on depth greater than `v(p)/(p-1)`. Their actual hypotheses, rather than only the earlier audit verdict, are checked below. Existing source-version and errata qualifications remain unchanged.

## The local norm argument

Use `r` for the rational contact product and `rho=v_p(r)`. At a prime in the inherited radical `M_5(beta)`, `rho` is odd. The correction is a unit because `p>76176`. The retained scalar preparation forces its input `b` nonzero. Consequently `W` and `r` are nonzero, and the old pole obstruction applies to the new `b=c r W^2`, giving

    rho + 2 v_p(W) > 0.

In a node `N_r(u,v)=u^2+r v^2`, nonzero summands have different valuation parity. Thus its valuation is their minimum; the same statement with infinite valuations covers a zero leaf. This requires only odd `rho`, not a squareclass assumption on `r` at every completion.

The constant leaf gives `v_p(A)<=0` if `rho<0`, and then `v_p(W)<=0`; that contradicts the displayed strict positivity. Hence `rho>0`. From

    A=N_r(1,q/r), B=N_r(U,V), W=N_r(A,B)

one obtains

    v_p(A)>-rho/4, v_p(B)>-3rho/4,
    v_p(q/r)>-5rho/8,
    v_p(U)>-3rho/8, v_p(V)>-7rho/8.

Since `U=z0/r^32` and `V=z1/r^32`, these imply

    v_p(q)>3rho/8>0,
    v_p(z0)>(32-3/8)rho,
    v_p(z1)>(32-7/8)rho.

All these are valuations of rational numbers. Integral valuations and positive odd `rho` therefore give `v_p(q)>=1` and `v_p(z0),v_p(z1)>=32`. In particular, no hidden residue-degree factor enters these leaf bounds.

## Why the field norm suffices here

The new `q` is exactly `f0^2-2f1^2=Norm(f(H))`. At a split prime its valuation is the sum of the two local valuations. At an inert prime it is twice the single local valuation, because the extension is unramified of residue degree two. Positivity therefore gives at least one place `w` with `v_w(f(H))>0`. It does not prove positivity at both split places, and the proof does not use that stronger assertion.

The retained point domain has `f(H)=1/x(H)` with `H` finite and nonidentity. At that selected place, `v_w(x(H))<0`, so `H` is formal and `t=v_w(z(H))>=1`.

Both rational coefficients of the ratio have valuation at least 32. Since `sqrt(2)` is a unit at every consumed place,

    v_w(z0+z1 sqrt(2)) >= 32

at every place above `p`, including the one selected by the norm. Therefore `v_w(z(R))>=t+32`. This is the crucial compatibility: the norm chooses the place, but the separate rational coefficient bounds already work at that place. No simultaneous choice across different primes is needed; the downstream conclusion is the rational divisibility of the same index `s`.

This argument would not justify replacing the odd product-height object by a field norm, nor a construction where distinct norms choose unrelated places for distinct needed tests. Neither change occurs here.

## The two-torsion branch and the logarithm application

The shifted scalar point is `R=S-P=[s]P`, with `s=a-1`. The retained subtraction guard excludes the identity case and preserves nonzero affine abscissa and ordinate. Thus `z(R)` is an actual nonzero field element, not an unconstrained quotient witness. The infinite-order generator implies `[2]R` is nonidentity as well.

At `p>76176`, the model is integral with good reduction, `2` and `D` are units, and `K_w/Q_p` is unramified. Put `m=v_w(x(R))`. From

    z(R)^2 = x(R)/(x(R)^2-D)

and `v_w(z(R))>0`, one has `m!=0`. For `m=0`, the denominator is integral, so the right side has valuation at most zero; this branch is impossible.

For `m>0`, `v_w(z(R))=m/2`, and for `m<0` it is `-m/2`. The exact duplication formula gives

    x([2]R)=(x(R)^2+D)^2/[4x(R)(x(R)^2-D)].

Its valuation is `-m` in the first case and `m` in the second. In both cases it equals `-2v_w(z(R))<0`. The numerator and denominator are nonzero, because their candidate terms have unequal valuations when `m!=0`. Hence `[2]R` is formal and `v_w(z([2]R))=v_w(z(R))`.

This handles reduction to `T0=(0,0)` correctly. One must not apply the formal logarithm directly to the possibly nonformal `R`. The submitted proof applies it to `[2]R`, which is valid. The same branch issue was already handled in the manuscript's doubled-formal-comparison lemma; that statement is written for split primes, but its actual elementary valuation proof and the direct duplication proof above extend to the unramified inert case. Historical disposition: prior justification found for the branch mechanism; the new scalar use is a newly reviewed application of it.

Now `H` and `[2]R` lie in formal depth at least one. In the normalization `v_w(p)=1`, the value group is `Z` at both split and inert places, and `1>1/(p-1)`. Silverman's hypotheses are met. The normalized logarithm is a homomorphism and preserves the parameter valuation on these points and their integer multiples. Apply it to the actual group identity

    [h]([2]R)=[2s]H.

Both indices are nonzero; the logarithms of the two base points are nonzero by isometry. Taking valuations gives

    v_p(h)+v_w(z([2]R))=v_p(s)+v_w(z(H)).

The factor 2 is a unit, so it contributes zero valuation. Consequently `v_p(s/h)>=32`, and the nonzero integer `h` has nonnegative valuation. Thus `v_p(s)>=32`. This is exactly the old scalar tree's downstream conclusion `M_5(beta)^32 | s`. The selected local field has disappeared from that rational integer divisibility statement.

## Completeness and fresh pole witnesses

For an integer input, the new `beta=2X^2+3` gives a nonzero integral `r` with absolute value greater than one. The inherited finite correction chooses `c` with `cr>0` and `cr` square at 2, 3 and 17. The inherited scalar preparation can make the old six normalized leaves integral at every prime dividing `r`, and divisible by the prime at every prime dividing `c` but not `r`, with arbitrary additional divisibility of `h0` and `s`. This is a constructive choice of points, not an assumption that the old tree remains an equation of the candidate.

At `p|r`, these choices imply `v_p(f0),v_p(f1)>=v_p(r)`, so `q/r` is integral. The two ratio leaves remain integral. At `p|c`, `p` not dividing `r`, all four relevant quantities are divisible by `p`. The new tree consequently gives `A=1 mod p` and `W=1 mod p` throughout the support of `cr`.

That support is nonempty because `r` is a nonunit integer and `c` is an integer. Thus `W` is nonzero. The new `b=crW^2` is positive, has nonnegative valuations on the support of `cr`, and has even valuations everywhere else. Its reduced denominator is a square, and multiplication by `W^2` preserves the local squareclasses at 2, 3 and 17.

These are precisely the hypotheses of the full seven-witness pole completeness lemma. The scalar block retains its preparation variable; it is not the preparation-zero specialization used by the comparison detectors. Therefore there is no missing real upper bound `b<17` or lower-depth condition from that different specialization. The full lemma supplies fresh preparation and pole witnesses for this new value of `b`. Keeping the old witnesses would not be justified, and the submitted proof does not do that.

With `R` fixed, the new quantities are rational functions of the shared point, defined at the chosen nonidentity point. The unit conditions persist on sufficiently small neighborhoods at the finite support primes, so the inherited congruence-modulus argument applies. The old construction of the four roots and the later prime choices can be performed in the same order. The separate anchor replacement is reported as equivalent for all allowed even nonzero scalar indices; compatibility here requires only that unchanged admissible index set and its arbitrary divisibility. This review does not replace the anchor's independent review.

## Literal residuals and consumers

The independent script `04-charts/review-product-check.py` imports neither a producer nor another checker. Its output is `review-product-check.json`.

It confirms the eight displayed new equations in the actual combined 505-variable residual file, the attachment of `W^2` to the correctly scaled old `scalar.W2` value, and the retained inverse chain giving `r^-32`. It confirms all 35 other scalar and shifted-scalar rows from the depth precursor, up to their nonzero row factors. It also checks that the thirteen removed baseline coordinates occur only in the thirteen removed old-tree rows and the rewritten `scalar.W2` row. Thus no deleted leaf or node has an unaccounted consumer.

The coefficients of `f(R)` remain defined. The replacement does not delete their point-domain equations, and the combination's separate anchor continues to consume the appropriate scalar coefficient. The source values `U0.f.0` and `U0.f.1` are the literal coefficients of `f(H)`. The retained ratio equations are `h_H zRatio=-j_H z(R)`, so the nonzero chart factor gives exactly `z(R)/z(H)`, including its sign. The scalar preparation rows still force `b!=0` and the preparation denominator nonzero. No inverse guard has been added to a formerly permitted zero pole witness.

The script also checks 2,352,980 bounded valuation cases, including negative odd `rho`, as a regression test. Those cases do not establish the unbounded valuation proof; the symbolic argument above does.

## Review disposition

No repair is required before accepting this scalar replacement. For a later manuscript integration, cite the existing doubled-formal lemma and explicitly state its unramified inert extension, the norm's residue-degree factor, and the use of fresh full-pole witnesses. Those details are supplied above and are consistent with the submitted proof.

The accepted claim is that this replacement preserves the final integer input projection, conditional on the same inherited arithmetic inputs. It is not equality of old and new scalar-tree witness sets. Changing either bound candidate, the tree, its ratio inputs, the nonzero guards, or the consuming index argument invalidates this scoped acceptance and requires another review.
