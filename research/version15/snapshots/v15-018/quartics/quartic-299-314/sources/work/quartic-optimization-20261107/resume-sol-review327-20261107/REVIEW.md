# Independent acceptance of the 327-variable weight chain

I accept the exact330-to327 replacement as an algebraic equivalence of complete rational solution sets after changing private helper coordinates. It preserves the distinguished input and every detector output and outside coordinate. It therefore inherits the arithmetic conclusion and qualifications of my accepted330 review without a new arithmetic premise.

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Author `/root/astra_quartic_opt03_depth`. I did not author the proposed chain or modify its artifacts. Exact serving-model metadata is not independently attested.

## Exact target

| Artifact | SHA-256 |
| --- | --- |
| Candidate report | `025ccfce6b15e7eef4428ab9b1e1a61c39aa4002c2d0d8096bf7e295f7730706` |
| Source330 IR | `41602bf9d25d52ae6e461f958eb21e1d752190ef71a72c1cc7c444f4e0a9fff6` |
| Candidate327 IR | `d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665` |
| Candidate polynomial | `884e02a0d5b3c2bc8179e7911a77375ed3871c7f353adc14339549a95cf6fe49` |

The source330 acceptance is my separate `resume-sol-review330-20261107/REVIEW.md`, SHA-256 `0a2774c9debd513a5ee7f9591c1eb8e2c6ad83ee23e04d84307b47e42d0043c1`. The author's reference to330 as pending records its earlier status. This decision uses the exact330 artifact already reviewed and does not alter that review.

## Unique chain and both maps

I extracted each R from the retained ER-1 row and checked that it is affine in the stored rational coordinates. ER=1 holds for every rational solution, so E and R are nonzero independently of any H interpretation, contact prime or sign assumption.

The retained equations force E2=E² and E4=E⁴. The new chain then gives successively

```text
E8 = E4² = E⁸
E11 = E8*E4/E = E¹¹
E19 = E11*E8 = E¹⁹
E39 = E19²/R = E³⁹
E79 = E39²/R = E⁷⁹
E158 = E79² = E¹⁵⁸.
```

Every division is by E or R, already nonzero. There is no square-root choice. Negative E values obey the same equations, and zero helper values cannot create an extra branch.

From a source330 solution, preserve E,E2,E4,E8,E19,E79,E158 and every outside coordinate. Replace old c by E11=E¹¹ and old E38 by E39=E³⁹, and forget E3. The new equations hold exactly.

Conversely, from a327 solution retain those same outputs and outside coordinates, restore c=R³, E3=E³ and E38=E³⁸. The old equations hold because E*c=R², c*E8=E2*E3, c*E19=E8², c*E79=E38² and E38=E19². All source helper values are uniquely determined, and the new helper values are uniquely determined. Thus composing these maps returns the original full solution in either direction, with the understood helper-coordinate renaming.

## Literal incidence and finite verification

The independent checker imports no producer or author verifier. For each detector it reconstructs the five replacement rows from the extracted R and verifies exact rational coefficients, not just degree or exponent labels. It checks the retained E2,E4,E158 square rows as the anchors of the chain.

Exactly15 rows change and three E3-definition rows disappear. The deleted coordinates are362,410,458. The repurposed coordinates are355,403,451 and369,417,465. Every old and new use of a repurposed coordinate lies in the changed or deleted rows. Every old use of a deleted coordinate does too. All other residual objects, coordinate metadata and top-level metadata except the descriptive status are identical. The four detector sums, W products, norm equations and pole equations are literal unchanged consumers. In particular, no remaining evaluation expects E38 at a repurposed slot.

I independently normalized every rational residual by denominator and integer content, expanded the complete sum of squares and compared all5770 coefficients. All327 coordinates occur, there are297 quadratic residuals, the polynomial has degree four and integer content one. No changed row contains C. The unique C² coefficient remains16, C-linear coefficients have magnitude at most96, and C-independent coefficients have at most1520 bits. The maximum therefore remains16C².

CHECKS.json records these results. I also replayed the author's verifier with its only output redirected to this review directory. AUTHOR-UNMODIFIED.json records unchanged author-file hashes. No producer, source artifact, prior330 review or release file was edited.

## Scope

No new defect or arithmetic dependency was found. This exact chain replacement is accepted. The valuation classes, common-place proof, H-domain exceptions, Π^39 completeness progression, real/finite choice order and inherited theorem qualifications remain those of accepted330 because their required outputs and all outside equations are preserved exactly.

This is not a new audit of the underlying elliptic, height, pole, prime-pattern or published-source results. It adds no claim of full manuscript verification or publication approval. The strict below300 threshold remains unmet.

Reproduce the finite audit from the workspace root with `python -B work/quartic-optimization-20261107/resume-sol-review327-20261107/check.py` using a recorded compatible interpreter.
