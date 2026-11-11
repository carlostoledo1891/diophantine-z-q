# Independent review of the 354-coordinate detector

Decision: accepted for the exact research candidate below, on the retained arithmetic inputs. It has the same rational input projection as accepted366. It has 354 total coordinates including the input, 324 quadratic residuals, 5,903 quartic monomials, degree four, content one and maximum coefficient `16*3^(2^26)`. This is not publication approval or a result below 300 variables.

Reviewer: `/root/astra_bl_synthesis`. The changed detector was authored by `/root/astra_quartic_opt06_product`. I did not author its construction. During review I identified the premature interpretation of the generic V0 leaf and supplied the valuation-only correction described below. The author incorporated it in the pinned final report. This report records that review contribution; it does not claim the corrected sentence arose independently in both reviews.

## Exact scope

| Artifact | SHA-256 |
|---|---|
| Source366 IR | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| Source366 review | `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2` |
| Corrected author report | `d6f4746d63dbf23b4be16541c2358260c87af47326e4399ca94cf7d0522fec3c` |
| Candidate354 IR | `cf62d9dc594e037e26d2569563f36a4d51a02197b7a3285740338441981e121a` |
| Polynomial354 | `3d159cab0b036eea9c4321d5bbb7f1a29727b2ad8baae85bf7e5eef44535189c` |
| Independent `check354.py` | `c3ea283737b343d063a88d0f731259918a950ecdf7ea943b4cb4c57620978276` |
| Independent `CHECKS354.json` | `b682ad526c16aa747129cb527f0dd3dc557da6f26356f68e8d836253b78cbbc9` |

The candidate and author report are in `06-detector-next`; this review and checker are in `12-independent-next`, relative to `work/quartic-under300-20261107`. The inherited manuscript is Version12, SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. I read its preparation-zero statement and proof near line 10564, one-place proof near line 11038, and ordered prime/real construction near line 11217. I also inspected the actual 392t and squared-H reconstruction, accepted372 detector interfaces, guard removal, scalar parity restoration, and the biquadratic square-output identities.

These are retained inputs with their existing qualifications, including the simultaneous-prime and restricted-converse dependencies. This review supplies a new detector argument and checks its consumers. It does not newly prove every historical arithmetic theorem or change any released artifact.

## The local argument and the corrected domain step

For each of the three detectors the unchanged contact construction gives `R=F5(A*lambda)`, `E=1/R`. At each prime in its required odd-contact radical, `p>76176`, the valuation `alpha=v_p(R)` is positive and odd, and `1+R` is a unit. No assertion about arbitrary other odd valuations of R is needed.

The ordered triples are exactly

```
[conjugate(f(V0)^2), f(U1)^2, f(U2)^2]
[conjugate(f(V1)^2), f(U3)^2, f(U4)^2]
[conjugate(f(V2)^2), conjugate(f(V3)^2), conjugate(f(V4)^2)].
```

Their replacement is `G=1+E*Y1+E^2*Y2+E^3*Y3`. At every place above a consumed prime, each nonzero Y has valuation divisible by four. For the eight primary/difference outputs with indices 1 through 4 this follows directly from the retained biquadratic identities, which express them as fourth powers. Those identities include zero outputs and require no H interpretation. The retained root equations supply the needed nonzero root parameter.

For the V0 output, the generic squared-H reconstruction gives nonzero f, a field value F, and `f*F=v^2`, together with `S^2=1/f-D*f`. Therefore `(1/f,S/f)` is a genuine point on the original curve. On that curve, at an unramified good place with D a unit, the equation `y^2=x*(x^2-D)` makes v(x) even: positive v(x) equals 2v(y), while negative v(x) satisfies 3v(x)=2v(y). Thus v(f) is even. If F is nonzero, `v(F)=2v(v)-v(f)` is even. If F is zero the corresponding term vanishes. The conjugated F-squared leaf has valuation in `4Z` in either case where it is nonzero.

This is the corrected argument. Before excluding `c*x(H)+D=0`, F cannot simply be called the reciprocal abscissa of H-P. The required valuation conclusion does not need that interpretation. The original report's premature interpretation is removed in the pinned corrected report.

The nongeneric squared-H branches are also covered before any detector conclusion. When U=0, the V0 leaf is the conjugate of `1/c^2`. When the Kummer Q is zero it is the conjugate of `-v^2`, with `v=(3+2*rho)/4` or `v=(-36+16*rho)/49`. The displayed coefficients and norms make these units at every consumed place. Their valuations are zero, hence divisible by four. No fourth root of a negative exceptional leaf is assumed.

The nonzero summands of G have valuations `0,4k1-alpha,4k2-2alpha,4k3-3alpha`. For odd alpha these occupy distinct residue classes modulo four. There is a unique minimum, so G is nonzero and its valuation equals that minimum, at most zero. Removing a zero leaf preserves uniqueness. Every unchanged higher-order factor is likewise nonzero with nonpositive valuation by its odd-valuation argument, including the permitted signed square on the exceptional H branch.

Consequently the full product W is nonzero at all places over a required prime. The literal norm equation `Norm(W)=2*Re(W)*z` forces `Re(W)` and z nonzero over K. It follows that `T=Tr(W^-1)=1/z`. Since `1+R` is a unit at this prime, the literal B equation gives

```
B=R/[T^2*(1+R)^2],
v_p(B) <= alpha+2*Lambda,
Lambda=max_{w|p} v_w(W).
```

The trace inequality uses its integral local normalization; it applies at split and inert primes. The valuation of B is odd. The unchanged pole obstruction therefore makes it positive and gives `Lambda>-alpha/2`. At a place attaining Lambda, every factor has valuation at least Lambda because all factor valuations are nonpositive. Each nonzero summand of every G consequently has valuation greater than `-alpha/2`. Thus `v(Yj)>(j-1/2)*alpha`. Its divisibility by four implies `v(Yj)>=4`, so each original low-order f has valuation at least two, sufficient for order one. The unchanged order-ten and order-forty factors give their original orders at this same place. The proof never combines different successful places.

## Exceptional branches and downstream use

In either squared-H exception the first packed group contains a fixed-unit V0 leaf. The local conclusion would force it to have positive valuation at any required prime. Hence all three radicals would be one. The independently restored scalar anchor and unchanged root-height inequality contradict that conclusion before H, the scalar height upper bound, or logarithm quotients are used.

The scalar parity argument of source366 depends only on the retained root/scalar/anchor rows. Its global sign normalization remains a symmetry of every new residual; I checked that directly. It therefore remains available before the root-height application. After excluding the squared-H branches, later fixed-point exceptions are treated using the same order-forty H test and fixed-unit contradictions. The corrected valuation proof above remains valid during that stage.

The subsequent logarithm comparisons, order-forty Lucas divisibility, order-ten input-error divisibility, three-scale height bound, scalar depth twenty-four and odd-label input bridge receive exactly their former hypotheses. A detector with no radical prime has no local obligation. It may still have an uninterpreted zero product; no removed inverse guard is restored for that case. This preserves the source369 treatment of such witnesses.

## Completeness with one common construction

The retained construction fixes the integer input, scalar data, roots and scales, then fixes the finite neighborhoods and real bounds before the selected contact primes and final H progression. The changed detector uses the same field functions. Only its output values, trace, B and private pole witnesses are recomputed.

At every selected contact prime alpha is one. At the designated place the old order-one condition gives positive valuation of each genuine reciprocal abscissa. Its valuation is even, so it is at least two and the corresponding Y valuation is at least four. All three nonconstant terms of G then have positive valuation, including the term weighted by E cubed. Thus G has residue one. At another place, unique minimum implies that its inverse has residue zero if its valuation is negative, and residue one if its valuation is zero. The unchanged factors have the same alternatives. The trace has residue one or two at a split prime, or the trace of one, namely two, in the inert case. Hence it is a unit and B has positive odd valuation one at every selected prime.

Outside those primes, the retained square multiplier relating R to the old contact expression gives even valuation of R. Both denominator factors in B are rational squares, so new divisors of the sums or of `1+R` contribute only even valuations. The reduced denominator of B remains a square. This conclusion does not require listing the prime divisors of the new sums in advance.

At 2, 3 and 17, the old neighborhoods bound the valuations of the finitely many Y values below. The freely prescribed denominator divisibility makes v(E) tend to positive infinity after these bounds are fixed. Every new term tends to zero, W tends to one and T tends to two with any required precision, including at the ramified prime two. The identity for B preserves the old local squareclasses. Its valuation is `-v_p(R)-2v_p(T)` once v_p(R) is negative, so the required preparation thresholds remain attainable. No finite neighborhood is selected after the contact primes.

At both real embeddings the genuine Y values are nonnegative. For large positive lambda, E is positive and tends to zero. All G values are positive and `1+O(lambda^-5)` uniformly on the same bounded real neighborhood. The trace stays positive and `B~1/[4*(A*lambda)^5]`. One sufficiently large lambda makes all three B values lie in `(0,17)`. Together with the square denominator, local squareclasses and depth bounds, these are precisely the preparation-zero hypotheses inspected in the source. The scalar conditions continue to hold for the same final H. Thus every integer input has a complete new witness.

## Exact finite evidence

My standard-library checker imports no producer or prior checker. It verifies the complete source/target difference, every old consumer of the twelve deleted coordinates, the eighteen literal changed component rows with their conjugations and factors of two, all low-order and mixed product consumers, retained E-power and toric equations, norm/trace and B interfaces, and all four squared-H field equations. It binds the 48 primary structural/output rows to the accepted394 source and checks the scalar-root sign symmetry against every current residual.

It independently expands every primitive residual square and compares all 5,903 coefficients. All 354 coordinates occur; C powers do not collide on specialization. The unique C-squared coefficient is 16, C-linear coefficients have magnitude at most 96, and the remaining coefficients have fewer than 2,048 bits. The checker passes. These finite facts supplement the valuation and simultaneous-completeness proof above; they do not prove the inherited arithmetic inputs.

No unresolved gap remains in this exact 366-to-354 application. Future compositions and any ordinary-coefficient companion require their own exact checks. Released files and mathematical acceptance records were not edited.
