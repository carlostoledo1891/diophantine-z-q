# Independent acceptance of combined417

Accepted for the frozen research composition below, on its inherited arithmetic inputs. The result has 417 total rational variables, including the input, 416 witnesses, 386 quadratic residuals and 6,296 quartic monomials. The polynomial has degree four, content one and maximum coefficient 16*3^(2^26). It does not meet the below-400 publication threshold.

Reviewer: `/root/astra_quartic_opt01_elimination`. I authored neither correction change nor this composition. This is a whole-composition decision: it includes the new input bridge, restricted correction-unit assertion, enlarged finite support, choice order, and compatibility with the accepted identity-inclusive point domains. It does not treat the changed correction witness fibers as equivalent to their old finite-choice fibers.

## Frozen bindings

| Object under `10-combination` unless noted | SHA-256 |
|---|---|
| Accepted source `combined423-ir.json` | `3c19ce0d46ae80732e76fd243b7fd1c91599f4274e1c67b9a4ac6c5bd86899bf` |
| Source acceptance `inputs/composition423-review.md` | `77e57ad1b956a5bc503ef32c6c6048ae5d28f153909f4fb67222ad46a10e352d` |
| Result `combined417-ir.json` | `b7d124eb221df55d49131854b541a4c97c5689b18882dfa4a24cc6b8c2d1b6a9` |
| Polynomial `combined417-polynomial.json` | `8272326ab3ea2e7b6996221cee758658dc1a4266e68ada3748af75b5ef289ae6` |
| `inputs/one-correction-review.md` | `e49af5208d1f35393071d17ac369b0299e1f319a25bbbb6c46fe7e2262f4d15e` |
| `inputs/deterministic-correction-review.md` | `ccaf3f1c6166af2bcde71f3cfa18c11778e8fdcba12eb0cc25d46133a5b9b04a` |

The component source/target hashes are also checked through `combined417-certificate.json`: scalar24-448 `e9d6622e...`, one-correction444 `c2c60a1b...`, and deterministic442 `e163f864...`. Their complete hashes and review pins are in that frozen certificate and the local replay output. The source manuscript is `manuscripts/quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

I read the actual root one-correction proposal, both correction component arguments and independent reviews, the accepted 423 review and its H/V0/zero-numerator arguments, and the depth24 review. I checked the original preparation and continuity passage at manuscript lines 10520–10559 and the final anchor, height, odd-label and choice-order passages around 20534–20638. The source's older unit-root construction is not substituted for the accepted depth24 integrality construction.

## Independent finite transport and actual scalar input

The new local `check.py` does not import any producer or other checker for its own calculations. It independently substitutes Y -> 102Y+102X+76 in every source residual except Y=X squared, accounts for the six deleted rows and the separately replaced scalar-input row, and matches the entire final row and coordinate inventory. All row IDs remain unique. Each unchanged metadata record is compared, not merely its polynomial support.

Exactly thirteen retained rows change by this affine substitution: the two direct beta-test square rows, the relevant scalar contact/power/root rows, the two hybrid coefficient rows and the three hybrid order-ten evaluation rows. The input-square equation is literally unchanged. Another 372 retained rows have unchanged polynomial values. The old additional Y consumer in the corrected-product equation disappears; the scalar-input equation is handled by its new identity rather than by a stale consumer count.

Coordinates 61–65 and 524 are removed. Every occurrence in the old system is in the deleted correction/product rows or the replaced scalar-input row. No remaining residual refers to them. Every other coordinate object and the fixed parameter are preserved.

The independent check derives the affine r from the shifted old corrected-product equation, before reading the new scalar-input equation. It agrees exactly with r recovered from the physical depth24 norm-root equation. The retained coordinate600 equation gives r squared. Consequently the final row

    (coordinate600+4896*r)*coordinate525+82479248*coordinate526=0

has exactly the intended old pole-input normalization with c=r+4896, including its sign. In particular the stored W-square and stored pole input are not silently interpreted as unscaled positive variables. This derivation and the accepted source normalization identify the semantic input as c*r*W squared.

The local checker independently expands every primitive residual square and matches every frozen polynomial coefficient. It checks degree, integer content, the complete coordinate support, and the symbolic coefficient bound without expanding the huge fixed integer. I also replayed both requested frozen checkers. The verification-file write of `verify_combination.py 417` was redirected to this review directory; the author code and files were unchanged. Hashes before and after confirm that no frozen combination file was modified. Both replays passed.

## New input and soundness

Put tau=2X+1 and beta=51*tau squared+2504. For rational X, beta>=2504, beyond each of the five real contact roots, so r is strictly positive. At every consumed p>76176, 51 and both leading contact coefficients are units. Negative valuation of beta is then even, as is the sum of the five contact valuations. Thus the odd valuation eta supplied at a scalar contact prime is positive before any correction-unit claim is used.

Since 4896=2^5*3^2*17 is a unit at that prime and r has positive valuation, c=r+4896 is a unit there. This is the precise scope needed by the scalar pole obstruction. It is neither asserted nor needed that c is a unit at all large primes. The pole input therefore still has valuation eta+2v(W), and the accepted depth24 norm inequalities apply to the same physical B, Q and W equations. They give the two coefficient depths at least 24, the required formal place of H, and the same scalar-index divisibility after treating both scalar branches near O and T0. The correction changes none of these point equations or ratios.

The same exponent-19 height theorem consequently gives h(beta)<=Hcal*|s|^(19/24). The literal scalar anchor and guard remain unchanged, and (5/24)*25165823.5>2093966+7 gives the same h(beta)<|a|/40 margin. The order-40 Lucas argument and order-ten input contradiction therefore still force n=beta. They use the height of this actual beta, not an unchanged formula for its height in terms of X.

The unchanged odd root chart makes n odd. If tau=u/v in lowest terms, integrality of 51*tau squared implies v squared divides 51. Squarefreeness of 51 forces v=1. Then oddness of n and evenness of 2504 force tau odd, so X=(tau-1)/2 is integral. Integrality of beta alone would not suffice, and is not the argument accepted here.

## Preserved point-domain interfaces

This candidate retains H in the accepted doubled-point chart; the later H-domain enlargement is not included. Its rescaled H/V0 equations, rational-log denominators, primary reciprocal equations, zero-numerator fused consumers, odd-root charts, scalar f1 guard and physical anchor are among the unchanged rows.

In particular the proof that V0 is nonidentity still precedes all division by its logarithm. If V0=O, the accepted H reconstruction gives H=P. Its f value is a unit at every consumed place, contradicting any contact prime via the retained order-40 test. If all three contact radicals are 1, the root-height inequality with N=1 contradicts the unchanged scalar anchor. This argument does not use a scalar upper bound for h(beta), the new correction, or an interpreted LP slot. The change of beta in the other detector tests does not affect the zero-tolerant one-place lemma or that contradiction.

Thus ell0 is nonzero and the accepted zero-numerator analytic-unit identities remain available for U_i=O or V_i=O. Their integrality-first argument gives the same label congruences, now with the correctly substituted beta test. The root scales and logarithm square-output interfaces are preserved. No old V1-nonzero argument or old finite-choice correction equation is used implicitly.

## Completeness and order of choices

For an arbitrary integer X, tau is odd and beta is a positive odd integer. The exact local calculations give v2(r)=2 with r/4=1 modulo 8, v3(r)=1, and r=15 modulo 17. My residue check corroborates the formulas over a full common residue range; the argument for all inputs is the polynomial calculation in the accepted proposal. At 2,3,17 the valuations of 4896/r are respectively 3,1,1. Hence c/r=1+4896/r is a square in each local field. Therefore c*r is a positive integer and a local square at all three required fields.

Compute r and c first, then fix the full finite prime support of c*r. New large prime factors of c are retained in that support. The source preparation permits any fixed finite set of places and arbitrary finite depth requirements, including bad and ramified places. It first chooses a sufficiently deep shared point, then a deeper scalar point with the anchor and divisibility conditions. At p dividing r, the accepted bounds 8eta on f coefficients and 24eta on scalar-ratio coefficients make B and W integral. At p dividing c but not r, positive depths suffice because r is a unit. The semantic W is positive and nonzero because r>0 and Norm(f(H)) is nonzero.

Thus c*r*W squared has nonnegative valuation on the full support and even valuation outside it. It has square reduced denominator and the required local squareclasses, so the unchanged pole-completeness theorem supplies witnesses. It is unnecessary to claim that the new W is a unit on the support.

After these choices, fix the other odd root labels and root scales, then the continuity modulus preserving all scalar and comparison conditions. Only then select the contact primes. The original finite-support preparation and prime-selection framework allows the resulting enlarged modulus and exclusion of a fixed finite set; no bound on the new prime factors is assumed. The final shared-point congruence preserves the prepared scalar inequalities. The accepted identity-inclusive chart construction can use the old nonidentity choices throughout completeness, so no additional boundary lifting or prime theorem is needed.

The composition therefore preserves the intended rational zero projection onto the integers. This acceptance is limited to the exact 417 candidate and its pinned inherited inputs; later H-domain or inverse-addition changes require another composition check.

Reproduction: run `python -B check.py` in this directory. `CHECKS.json` records the independent results, exact shifted-row and removed-consumer inventories, frozen-checker pins, and both replay outputs. No released file or frozen author artifact was edited.
