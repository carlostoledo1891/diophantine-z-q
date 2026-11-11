# Review of the Section 12 geometric join

Reviewer: `/root/astra_v14_assertions_arithmetic`, a model agent distinct from Gaussian, the author of the reviewed join. I authored the upstream LP04 packet and previously discussed its interface with Gaussian. This review assesses the new connecting construction conditional on those upstream inputs. It does not supply independent acceptance of LP04. I read the proposed join before reconstructing the calculations; this was not a blind review.

The initial review target is `local-proof-section12-join-gaussian/MANIFEST.json`, SHA-256 `d2f428562527abbaa58624a4e230691015ce18ddc34bd502ddb693247de3226e`, with proof SHA-256 `3d944477a67cffe70f806cad7c2dad7d18459f3474dadb295da1727c3d8ffb1b`. Exact final reviewed successor details and the disposition are recorded in `DECISION.json`. The scope is the geometric join and its exact interface, not the inverse theorem or all of Sections 10–13.

## The construction checked

The input is the specific homogeneous quotient whose petal ideal is abelian at every weight, with the integral Hall coordinates and petal-scaling identities supplied by LP04. It is not an arbitrary nilpotent group with a similarly named subgroup. The group, weights, character and integral model are fixed standard data before the orbit coefficients or limit parameters are chosen.

The character extension in §2 checks on that input. The central ordinary top group has its weight-`m` Hall basis; the degree-rank top `T` consists of the length-`R` sublist. The integer lattice is the direct integer span of the corresponding group commutators, whose logarithms are exactly their Lie brackets at weight `m`. Assigning zero on the complementary basis therefore extends the character integrally. An arbitrary rational subtorus would not justify this particular zero-coordinate extension without the stated lattice splitting. That splitting is an explicit LP04 input here. The new test function is chosen with the extended character before using LP04. Its restriction to `T` remains the required original character, so the cancellation used in LP04 is unchanged.

The finite local-section construction gives a smooth unit vector with this character, not merely a scalar section that might vanish. On each local torus trivialization, the component is a smooth bump times the character. Normalizing the bumps by their Euclidean squared sum gives unit vector norm globally; supports inside the charts make extension by zero smooth. The rational central quotient and its lattice give the required torus bundle. Thus this construction applies first to `G_m` and later to the actual multidegree top `P_m`.

For the first semidirect product, the map `(g,p) -> (g,gp)` embeds `K` as the subgroup of `G x G` whose coordinates agree modulo `P`. Pulling back multiplication gives exactly `(g,p)(g',p')=(gg',g'^{-1}pg'p')`. It also gives the stated inverse. The shear `rho_t(g,p)=(g M_t(p),p)` is multiplicative because scaling commutes with conjugation and the petal group is abelian. Its composition law is additive, so its inverse is `rho_-t` even when `M_t` is not invertible. There is no use of a nonexistent inverse for `M_0`.

The second law is a right-action convention. In that convention conjugating `K` by `(t,1)` acts as `rho_-t`. Differentiating gives the two shear terms `M_(t')Y - M_tY'` in the first Lie coordinate. The second coordinate is `[X,Y']+[Y,X']`. The signs and coordinate positions in the displayed bracket are correct. Each nonzero bracket adds the declared bidegrees, with first degree at most one and second degree at most `m`. Since each generator has positive total degree, the claimed class bound `m+1` follows.

The filtration is the sum of homogeneous pieces dominating each index. This proves nesting, normality and the sum-index commutator inclusions, including the zero-index cases. Its `H_(0,1)` contains the entire first `G` coordinate, so the core part of the orbit is permitted. The subgroups `H_(1,0)` and `H_(0,1)` generate the ambient group, as required for tautness. Its actual top is the first petal copy of `P_m`, rather than the potentially smaller degree-rank top `T`.

The initial text's phrase “with `j>0`” before the filtration display could restrict the declaration `H_(a,j)=1` for `a>1` and leave `H_(a,0)` unstated. The following homogeneous description already forces those cases to be trivial. I requested that the author state the full index range explicitly in a preserved successor. This is a definition-level clarification, not a change to the bracket calculation or intended construction.

The lattice calculation checks both subgroup and compactness claims. Integral shears and their negatives preserve `Gamma semidirect Lambda`, so they preserve it bijectively. The three-coordinate integer set is therefore a subgroup, and it is discrete in the product topology. Right reduction first puts `t` into a compact cube, then reduces the first `G` coordinate, and finally reduces the conjugated petal coordinate. The intermediate conjugate need not be bounded; the final reductions still give a fixed compact product representative set. The same operations inside each filtered subgroup give the claimed rationality. This proves more than discreteness alone.

## Polynomiality, charts and values

I read Corollary B.4 in the actual final GTZ PDF, printed p. 1334, together with the surrounding definition and derivative criterion. It applies to two groups filtered by the same index set. The join explicitly gives the `N^2` source filtration on `Z^2`, with only the coordinate axes nontrivial at positive indices. For a factor depending only on `n`, every derivative in the `h` direction vanishes, while `n` differences lie in `H_(0,j)`. The linear `h` factor takes values in `H_(1,0)` and has zero second `h` difference. Unrestricted zero-index derivatives preserve these assertions; increments in any other source subgroup are zero. Thus all three factors have precisely the common filtered domain required by B.4. Their product is the claimed polynomial map, including its mixed derivatives.

The explicit generator factors are polynomial by ordinary finite differences of the binomial exponents. A difference of order at most the exponent degree remains in the generator's one-parameter subgroup, which lies in every required lower weight group, and higher differences vanish. No commutativity between distinct core factors is assumed; product closure supplies their product. The petal factors commute for the separate reason that `P` is abelian.

For `z_h=alpha h-{alpha h}`, right multiplication of the lifted orbit by `(-z_h,1,1)` applies `rho_-z_h`. It changes the first group coordinate to `g_0(n) M_(alpha h-z_h)(g_1(n))`, which is exactly the required representative. The second petal coordinate is unchanged. This checks the fractional-part identity with the actual lattice and action sign.

The local chart over a torus box of width less than one is also exact. Two representatives whose `t` coordinates lie in that box differ by a lattice element only when the integer displacement in `t` is zero; their remaining coordinates then differ by the ordinary right `K` lattice. Hence the chart really is a product with `K/Lambda_K`. The map from this fiber to `G/Gamma` is well-defined since projection to the first coordinate of `K` is a homomorphism respecting the lattices.

The finite list of inner boxes is fixed before `alpha`, `h`, the coefficients, or `N`. It covers the closed fundamental cube, with fixed positive margins inside larger injective boxes. Consequently one box contains at least a `1/J` fraction of every finite nonempty parameter set. The cutoff derivatives have fixed bounds. No chart radius shrinks with a parameter, and a box may meet the boundary of the chosen fundamental cube without losing injectivity in its larger lift.

The local unit vector `W` has the character on the actual central top `P_m`, by the stronger initial choice of the test. The global unit vector `W_0` has the same character. The pair `(cos(theta) W, sin(theta) W_0)` has squared norm one on the chart, extends smoothly beyond it, and has this same vertical character everywhere. On the selected inner box it is exactly `(W,0)`. This proves the fixed coordinate isometry required by the downstream contract; it gives neither a scalar cutoff approximation nor a division by a chosen component.

All maps whose derivatives enter the test bounds are fixed maps on compact manifolds or fixed relatively compact chart closures with compact fibers. The orbit coefficients do not appear in their derivative bounds. The dimensions, finite list of tests, and Lipschitz constants are therefore standard and independent of `h`, `N` and unbounded orbit coefficients. Uniformity over unbounded choices of the vertical character is not claimed.

## Exact downstream interface

I compared the join with Theta's frozen `rank-iteration-001` §3. Its first required output is a global unit multidegree `(1,m)` nilcharacter `Z(h,n)` whose restriction on a dense family is one fixed coordinate isometry of `zeta_h(n)`. The construction supplies exactly this, with `zeta_h=Ftilde(b_h Gamma)` and the fixed zero padding. The finite chart selection preserves positive standard density.

Its second required output is the entire matrix `V_h=chi_h tensor conjugate(zeta_h)` on one common lower-degree-rank model, with uniform bounds and internal dependence. LP04's comparison proof restricts the whole tensor function to one fixed rational subgroup and descends it through the same central top subgroup. Thus the replacement of `Ftilde` by the new fixed smooth test changes neither the subgroup nor the vanishing character. The same common model and uniform argument apply to every component simultaneously. This is a comparison with the LP04 interface, not an independent verification of LP04's proof or its analytic premises.

The component identity follows from the squared norm of `zeta_h` being one. It is a fixed finite sum, with no individual component required to be nonzero. The ordinary degree drops to at most `m-1` only when `R=1`. For `R>1` the supplied bound is degree-rank at most `(m,R-1)`. The join preserves this distinction and does not claim to perform the remaining rank iteration itself.

The construction uses fixed standard formulas and choices. Applying them to representative sequences gives internal parameter-dependent orbits and comparisons. The unit and vertical identities hold for every ordinary group point and every real parameter before passage to the ultrapower, so their natural extensions hold on the full limit domains. This is stronger than checking equivariance only at standard points. The dense restriction is used for equality with `zeta_h`; the new nilcharacter itself remains globally defined on the entire internal `Z^2`.

Compiler's Section 13 contract requires that eventual global unit multidegree nilcharacter, with standard geometry and polynomial orbit. It does not directly consume the Section 12 quotient construction. This review confirms the geometric output needed at Theta's boundary; the correlation and rank iteration must still supply the whole Section 13 input. The new packet does not close those missing analytic or assembly premises.

## Source comparison and related-use coverage

The final GTZ PDF is pinned at SHA-256 `cd320f5c1217df9bb41395e847ae2a924e70521021ca1b01c7abc20550123be1`. I read the printed construction on pp. 1308–1315 and B.4 on p. 1334. The following bounded findings agree with the author's occurrence record.

* The p. 1312 illustration omits the core coordinate from `H_(0,1)`, though its displayed orbit contains that coordinate. The general definition on p. 1314 includes it. The reviewed proof uses the general definition and checks it.
* The final top group can exceed the degree-rank character domain. The reviewed integral extension and order of choosing the test supply the larger-domain frequency required on p. 1315.
* The scalar cutoff formulas alone do not give global unit norm. The reviewed same-character completion supplies that property and exact equality on the inner box.
* The literal near-zero pigeonhole assertion on p. 1308 fails for `alpha=1/2` and odd shifts. Fixed boxes at arbitrary positions suffice for this construction. This is not an assertion that every possible earlier use of a near-zero normalization has been removed.
* The lattice must be in the new semidirect group, and the exact fractional-part reduction must use right lattice multiplication. Both are explicit in the reviewed proof.
* The corrected comparison gives a rank drop at `R>1`. The review does not restore the stronger ordinary-degree assertion merely from that comparison.

The original LP04 packet remains unchanged and is not relabeled as having included the new character extension or geometric proofs. The join's working assembly reference is a consumer, not a mathematical supplier. Its exact newer rank-iteration boundary was also read for this review. The nine findings and repeated occurrences were checked within this bounded scope; no whole-GI source inventory or global corrections audit is certified.

## Nine application checks

| Check | Result |
|---|---|
| Source hypotheses | Specific homogeneous LP04 quotient and all its additional comparison premises remain explicit. B.4 is applied to the checked common filtered domain. |
| Objects | Both groups, actions, lattice, top group, tests and charts were reconstructed from their formulas. |
| Domains and indices | Full `N^2` filtration, all integer inputs, and all real scaling parameters are used. The notation clarification is tracked separately. |
| Maps | Signs, exact lattice reduction, character restriction, and fixed zero-padding map check. |
| Consumed object | The global unit nilcharacter restricts to the actual chosen `zeta_h`; the full tensor comparison remains on the common lower-rank model. |
| Normalizations | Right cosets, half-open fractional parts, additive shears, and integral character values are consistent. |
| Local conditions | Torus chart margins and vertical stabilizers are checked; chart functions have common character and fixed bounds. |
| Exceptions | Zero petal dimension, zero character, trivial top group, and noninvertible `M_0` are handled. `R=1` and `R>1` remain distinct. |
| Downstream and limits | Theta's exact isometry/tensor interface is supplied conditionally; compiler's final correlation input is not claimed. Full limit identities follow from universal ordinary identities. |

This is a conditional acceptance of the geometric join after the explicit indexing clarification, with the final frozen target recorded in `DECISION.json`. LP04's non-author review, analytic frequency decomposition, Theorem 11.1 hypotheses, rank iteration acceptance, and the remaining inverse-theorem assembly are separate obligations.
