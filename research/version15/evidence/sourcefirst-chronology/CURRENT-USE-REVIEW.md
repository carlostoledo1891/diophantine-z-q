# Current-use review after initial reconstruction

Reviewer: `/root/v15_sourcefirst_review`, a distinct non-author model reviewer. Root explicitly spawned this reviewer with `gpt-6-astra` and no inherited turn history. Two direct host-metadata attempts timed out. The controller must bind the actual host-run evidence before counting this document as policy-eligible acceptance. No previous favorable mathematical review was used to derive the initial table.

The reviewed manuscript is `work/version15-protocold-233-20261110/full-draft-002/quartic_v15.tex`, SHA-256 `8867d26272fcfb91b76d1786d5126f06159fdd1ff2f7dbb33d64c392ffd976c2`. The initial reconstruction was frozen at `2026-11-10T06:44:10.4116437Z`, with `INITIAL-FREEZE.json` SHA-256 `e427d7fb818024c734706ba7be2e1084120b9ea4f58f3e06ffad3f3f78954272`. All author records discussed below were read after that freeze.

## SF31: the actual order-four formal error

**Decision: accepted within this precise mathematical scope.** The printed coefficient argument supplies the relative order-four error used at lines 32806–32843. This decision includes the transition to the stated absolute congruences, relative to the already stated local-extraction and nonzero-reference inputs. It is not acceptance of all of `V15-LOGS`, its analytic inputs, or the complete baseline.

I independently reconstructed the following calculation before reading `source-use-clarification-014/DERIVATION.json`. I then checked that author derivation against the same calculation. Its SHA-256 is `e4e6a42b4cc5536be852697560a1dad607002c10e12b2f38ee0bf71091fc48b6`.

Let the consumed prime satisfy `p>76176`, let its completion be unramified and normalized by `v(p)=1`, and let `e=v(z(Q))>=1`. The actual curve is `y^2=x^3-Dx`, with integral `D=11-6sqrt(2)`. The printed identity `f=z^2(1-Df^2)` gives `v(f)=2e`. In the printed series `L=z sum_j c_j(Df^2)^j`, the term with `j=1` has relative valuation at least `4e`, since `c_1=-2/5` is integral at the consumed prime. For `j>=2`, the printed coefficient estimate gives relative valuation at least `4je-j`. This exceeds or equals `4e`, because `(4j-4)e-j>=3j-4>=2`. The lower bound tends to infinity, so the convergent sum of the nonconstant terms has valuation at least `4e`.

Thus `L(Q)=z(Q) A(Q)`, with `A(Q)=1 mod p^(4e)`. At the identity, the formal power series defines `A(O)=1` without division by `z(O)`. The general `3J` tail theorem remains correct on its broader odd-prime domain. That theorem with `J=1`, taken alone, would not justify order four; the coefficient proof is the required supplier.

The two actual denominator points are `H` and `H-P`. Their nonzero formal domains come from the prior extraction and forced-149 exclusion. The integral group identities at 32819–32825 give full logarithmic ratios `u_i/h` and `(u_i-n_i)/(h-1)`, with `h=m/2`. Since the consumed prime is odd, both `h` and `h-1` are integral, and at least one is a unit. The corresponding full ratio is integral. Multiplication or division by the formal units `A` preserves valuation. The positive-valuation difference test `C_i` transfers integrality to the other plain ratio and then to the other full ratio. Only after that step do the relative errors give absolute congruences modulo `p^4`. The argument includes zero numerator points and the inert case, where conjugation preserves the unique valuation.

The nine relevant application comparisons are therefore explicit: the prime/depth hypotheses match; the objects are the actual `f,z,D`; the denominator domain is inherited and named; the maps are formal logarithm and the printed integral group identities; the normalized valuation and leading term agree; zero numerators use the power-series convention; estimates are uniform in formal depth and all consumed primes; integrality precedes use of an absolute error; and the downstream conclusion is exactly the congruence used in the baseline, not a stronger all-prime statement.

No manuscript repair is required by this calculation. The author contract must link this derivation or its equivalent instead of relying only on the coarse `3J` statement. Historical justification beyond the frozen manuscript has not been searched and is not classified as new.

## SF39 and SF40: current 237-variable scalar arithmetic

**Decision: accepted relative to the explicit retained arithmetic inputs below, with finite circuit correspondence excluded.** I checked the changed scalar inference and its insertion into the stated soundness and completeness argument at 35010–35152, including its use by the inverse-coordinate removals at 35153–35285. I did not use the earlier parity review's verdict to derive this judgment. This does not accept the entire `V15-PARITY237` finite record, prove its inherited inputs anew, or accept the final polynomial.

The retained inputs are the actual elliptic point and ratio interpretations over `K=Q(sqrt(2))`; the positive scalar normalizer with forced valuations at 149; the short-pole obstruction and realization assertion at 32259–32329; the contact-height and aggregate-height inequalities; the baseline local tests and global comparison argument; and the scalar-S choice of `c=|a|` with its Lucas lower bound and completeness construction at 33130–33155. The current-use source graph must retain direct connections to those statements. Their own full source-level acceptance is separate work.

The constructed variables satisfy `R>0`, `R2=R^2`, `Z=R(u+sqrt(2)v)`, `W=w/R^2`, `D1=v^2`, and `F=Norm(f(H))!=0`. From `u^2=RC` and `C^2+R D1+F^2=R^2 w`, division by the already nonzero `R` gives exactly

`W=Z0^4/R^10+Z1^2/R^5+F^2/R^4`.

This computation uses the factor-two storage convention `f^2=x86+2sqrt(2)x87`, hence `F^2=x86^2-8x87^2`. It does not silently identify physical and scaled coordinates.

For `p=149` or `p>76176` with positive odd `nu=v_p(R)`, the fixed number `9792` and `D` are units and reduction is good and unramified. Positivity and `F!=0` imply `W>0` and `b=R(R+9792)W^2!=0`. The pole obstruction applied to its odd valuation gives `v(W)>-nu/2`.

For an actual point on the curve, if `v(x)>0`, then `2v(y)=v(x)`; if `v(x)<0`, then `2v(y)=3v(x)`; valuation zero is already even. Thus every finite `v(f)` is even. At a split prime, `v_p(F)` is the sum of the two even valuations. At an inert prime it is twice the unique valuation. It is even in either case.

The three terms of `R^4W` have valuations `4v(Z0)-6nu`, `2v(Z1)-nu`, and `2v(F)`, in the disjoint classes `2 mod4`, odd, and `0 mod4`. Omit any zero component of `Z`; the last term remains nonzero. The least finite valuation is unique. Since `v(R^4W)>7nu/2`, each term exceeds that bound. The resulting inequalities are exactly `v(Z0)>19nu/8`, `v(Z1)>9nu/4`, and `v(F)>7nu/4`.

A positive norm valuation gives a place where `H` is formal. The ratio `Z` has valuation greater than `9nu/4` there. The permitted two-torsion translation makes the comparison point formal without changing the valuation of its parameter. The identity `[2m]S'=[4a]H`, with `h=m/2` integral at this odd prime, gives `v_p(a)>=v(Z)>9nu/4`. No additional divisibility assumption on `m` is used. Each selected radical prime contributes at least three to `v_p(a)`. The forced prime 149 lies below the radical cutoff, so `149^L'_N M5(beta)^3` divides `|a|`, where `L'_N=floor(9(2N-1)/4)+1`.

The same norm inequality at 149 excludes the finite exceptional reference points before interpreting later reference ratios. In particular `f=-a/c` in the inverse-coordinate argument has norm `(41/56)^2`, a 149-adic unit, and cannot occur. This use needs only the recovered actual reference point and the retained scalar equations; it does not require the deleted reference value or its square to have been interpreted already.

For soundness, the retained two-contact and aggregate argument applies with the unchanged tests. Replacing `L_N` by `L'_N` changes the scalar upper bound but retains its decay and `|a|>=149^L'_N`. The scalar-S Lucas estimate `(c-4)log(c-1)` for `c=|a|` dominates `C'+7C3*149^-L'_N*c*(1+log(c)/3)` for all sufficiently large `N`, uniformly in `c>=149^L'_N`. Earlier defect elimination still uses the unchanged exponent `7/4<2`. The threshold can remain ineffective because the retained aggregate intercept is ineffective.

For completeness, keep the fixed compact real neighborhoods used by the scalar-S construction. Bounded `Z0,Z1,F` and `R>=A_N/(1+149^2)` give `W=O(R^-4)` and `b=O(R^-6)`, with constants independent of the integer input. At fixed finite support, first choose `H` sufficiently formal and then the comparison index sufficiently divisible, making `F` and both components of `Z` arbitrarily deep. Fixed powers of the nonzero `R` in denominators therefore cause no obstruction. At odd-valuation numerator primes this makes `W` integral; elsewhere the squareclass determines even valuations, and the designated depths at 2,3,17 are imposed separately. The squareclass of `b` is unchanged, and its reduced denominator is square after this preparation. The stated recurrence and compatible progression keep the real neighborhoods and finite conditions simultaneously; later primes avoid the support already fixed. Setting `C=u^2/R`, `D1=v^2`, `w=R^2W` recovers the changed equations. This is separate existence in both arithmetic directions, not a bijection of old and new scalar witnesses.

The numerical bounds, exceptional zero cases, order of choices and downstream nonvanishing use match. Exact deletion of raw coordinate 137/row82, compaction, source-IR equality and final sparse compilation are finite correspondence obligations and are not certified here.

## Coverage and reconciliation status

The initial 45-row table and the 69-section index remain immutable. A contiguous line index is evidence of explicit coverage status, not evidence that all lines are reviewed. Most retained foundations, primary external statements and exact finite artifacts are still unreviewed by this reviewer.

The author routing aid 016 supplies candidate matches after the freeze. I checked the actual `V15-LOGS`, `V15-PARITY237`, `V15-AGGREGATE`, `V15-BASE248`, `V15-FOUNDATION` and `V15-GAUSSIAN` obligation contents. Other routes remain candidates unless a separate review supplies their comparison.

The four-label sum contract does not cover the manuscript's product-aggregate or number-field claims. The logs and Gaussian contracts do not yet give complete direct comparisons for the strip/order-separation and weight-replacement arguments. The baseline obligation text does not bind its exact finite tables and certificates. The short-pole realization and complete conic charts need their own direct source-use mapping, including their exceptional branches. The parity contract's dependency list must account directly for scalar-S, since its unshifted `|a|` route is actually consumed. These are unresolved inventory and scope differences. They are not findings that those mathematical assertions are false.

The separate new-235/233 reviewer disclosed authorship of the 237 arithmetic and excluded that premise from his own acceptance. The height reviewer disclosed authorship of raw/sparse233 and excluded final233 finite acceptance. Those exclusions must be retained in the assembled coverage record. No component decision here supplies whole-proof, full-inventory or release acceptance.
