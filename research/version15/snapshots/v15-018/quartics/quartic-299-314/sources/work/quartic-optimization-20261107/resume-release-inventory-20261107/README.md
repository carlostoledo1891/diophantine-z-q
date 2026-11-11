# Preparatory application delta after Version 13

This directory prepares the inventory work for a future release. It compares published 394 with the accepted 320, three-anchor319 and exact319 packets, and the pending 318 composition. It creates no acceptance, changes no production inventory or manuscript, and supplies no new mathematical proof audit. The source reports and their non-author reviews remain the authorities for the recorded component status.

Prepared by `/root/astra_quartic_opt05_anchor`, November 7, 2026. The below 300 release threshold has not been reached by any candidate in this packet. No ordinary-coefficient companion for the current composition has been frozen here.

## Files

* `APPLICATION-DELTA.json` maps all 39 published application records to changed or retained uses. It preserves each original source and consumer object and supplies 19 proposed internal inventory entries with exact proof-section locations, author/reviewer identities and whole-file hashes.
* `CANDIDATES.json` pins 16 component or composition IRs, their reports and recorded reviews. It lists every changed, added and removed coordinate/residual ID in each stated comparison. These are source comparisons, not repeated SOS or arithmetic checks.
* `BASELINE-COVERAGE.md` is the short index of the 39 application mappings.
* `RETAINED-SOURCES.json` preserves the published source catalog metadata, inherited references, version and errata qualifications, and field/valuation conventions.
* `PRESERVED-ALTERNATIVES.json` records rejected, conditional, superseded and unselected routes that must not be counted as adopted reductions.
* `SOURCE-PINS.json` binds 66 input files. `STATUS-SNAPSHOT.json` preserves the navigation index read from agent 10. That index does not itself authorize an acceptance.
* `build_notes.py` reproduces these notes from the pinned source files. It imports no author verifier and executes no candidate code. A rerun rejects changed frozen inputs except the explicitly mutable navigation index.

The N01–N19 labels are working inventory keys, not existing manuscript theorem labels. The eventual author should give the corresponding statements actual labels and bind their construction and consumer passages in the final text. Component approval is not approval of that future exposition.

## Distinguish the candidate names

| Candidate | Exact IR SHA256 | Recorded status and proof route |
|---|---|---|
| published 394 | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` | Version 13 published symbolic construction; 394 variables, 364 residuals, 6338 monomials |
| combined320 | `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f` | Accepted 327 detector plus 359 anchor; 290 residuals, 5659 monomials; stronger Π³⁹ completeness |
| three-anchor319 | `61898500a23024afbf21aed5a35ee0b573beef0dcaa598caba07de884c4281f4` | Accepted 326 detector plus 359 anchor; 289 residuals, 5676 monomials; original Π¹⁹ completeness |
| exact319 | `847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676` | Accepted exact private unscaling of combined320; 289 residuals, 5659 monomials; inherits Π³⁹ |
| combined318 | `e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1` | **Pending composition review in this inventory**; exact private unscaling transported to three-anchor319; 288 residuals, 5676 actual monomials |

The three-anchor319 review is by `/root`, SHA `9aae015208f80bcf38b74b5d5271cbe56aed94e7a320272d265f9a2cf8a18c4d`. The exact319 review is by `/root/sol_protocol_final_review`, SHA `412d86d205d9914249823d86a89b89bbbc9c006d908a980d846328f6c0e13406`. These different reviews approve different IRs. Neither is relabeled as approval of 318.

The exact unscaling uses `T=2g0g1+Cq`. It does not use the separately accepted 358 alternative `T=g1²+Cq`. The latter needs additional arithmetic and is not an ingredient of 318.

## Changes that need explicit arithmetic statements

| Entries | Changed use and required statement | Source author and recorded non-author review |
|---|---|---|
| N02–N03 | Squared-H reconstruction on UQ!=0; classify U=0 and Q=0; exclude those branches by fixed-unit tests and the pre-H root-height contradiction | 01's squared-H390; 03's review390 |
| N04–N05 | Replace the contact parameter by R=F5(Aλ), use B=R/[T²(1+R)²], and prove both required-contact soundness and the new ordered real/local completeness estimates | 10's unweighted372; 01's review372 |
| N06 | Recover trace and B nonzero only at required contact primes after removing global guards; retain radical-free degenerate auxiliary cases | 10's369; 01's review369 |
| N07–N08 | Recover S oddness from the old anchor at 3 and restore its half-chart using the global sign map | 01's S-parity366; 03's review366 |
| N09 | Establish valuation classes before H has its later meaning, using the unconditional Kummer-to-curve identity and primary fourth-power identities; bind every cached power and affine normalization |Current application in 03's332, reviewed here; original valuation-only correction credited to the earlier 354 reviewer |
| N10 | Four-group mod16 unique-minimum proof and same-place recovery, with original Π¹⁹ completeness | 03's332; 05's review332 |
| N11 | Strong H slot in 330 forces f(H) depth 80 and requires Π³⁹ primary completeness | 03's330;Sol final reviewer. Used in 320/exact319, superseded in the three-group route |
| N13–N14 | Three groups in 326, all residue classes and zero leaves, strengthened U2 requirement, actual G2 precision 12, and completeness rebuilt with original Π¹⁹ | 03's326;Sol final reviewer |
| N15–N17 | Abscissa coefficient lemmas at 3 and 2; shifted quaternion parameter F_s/C+Qroots; root parity and half-chart restoration before H/height use | 01's359;BL horizontal reviewer |
| N19, unselected | Replace F_s by g1² using an orbit-specific valuation equality and 2-integrality of g1; apply the quaternion criterion to a different parameter | 10's358;BL horizontal reviewer; not used in 318 |

The exact source sections, their line ranges and whole-file hashes are in `APPLICATION-DELTA.json`. The19-entry list includes exact maps as well as arithmetic statements. It is not a claim that19 new external theorems are required.

The pre-H repair deserves explicit historical attribution. `12-independent-next/REVIEW354.md` records that `/root/astra_bl_synthesis` identified premature interpretation of the generic V0 leaf and supplied the valuation-only correction. The corrected author report and the later independent mixed348 application review are pinned separately. The current cache/three-group applications must be written anew, but the underlying repair must not be presented as an independent discovery in every later packet.

## Exact substitutions do not create new arithmetic applications

N01, the 392t Kummer presentation, has an exact affine substitution for the old slope and explicit rational inverse. It consumes the already proved source domain in one direction; its reverse only divides by the stated nonzero quantities. The subsequent squared-H step is different because it introduces exceptional branches requiring N03.

N12, the 327 power chain, changes only private helpers. The retained ER=1 gives every needed denominator, and the outputs are exactly E,E²,E⁴,E⁸,E¹⁹,E⁷⁹,E¹⁵⁸. In 326, E¹⁵⁷=R E¹⁵⁸ is an exact quadratic gate. These statements need finite identity/consumer bindings, not a new prime-pattern or height theorem.

N18, exact319 and its pending 318 transport, is a full guarded solution-set bijection. From Q=q and B=2g1+CQτ set

    u=g0U, v=g0V, w=g0W, T=g0B.

The inverse sets Q=q, B=τT, U=τu, V=τv, W=τw using the retained g0τ=1. The quaternion parameter remains exactly T/C=F_s/C+q. No additional Hasse–Minkowski application, local valuation lemma, square-root branch or real choice is introduced. The five unconditional identities in the exact319 review are the appropriate finite certificate.

By contrast, 359 changes the quaternion parameter, and 358 changes it again. Their existential selections of new private quaternion witnesses are genuine changed applications of the inherited universal criterion. They must not be described as the same exact map as N18.

## The soundness order must appear in the new exposition

For 318, first invert the exact private unscaling to obtain the three-anchor319 system. Its 359 proof starts with the square-abscissa charts and scalar subtraction, which give integral indices without first assuming them odd. The three disjoint 3-adic valuation classes recover root parity and the old scalar anchor. Then apply the A,T,Z sign actions and restore the reviewed 326 source.

Only on that restored source may the 326 proof invoke its inherited 366 S-sign normalization. The S involution should not be applied directly to the shifted B equation without a separate proof. The root signs and S sign are different transformations, used at different stages.

The detector then establishes the pre-H valuation classes, rules out its two fixed-unit branches and reconstructs H. The later log, ratio-integrality, Lucas, scalar24 and input arguments use their original formulas after receiving the renewed local hypotheses. A radical-free detector does not acquire an unproved global trace inverse.

For completeness, construct the 326 witnesses using Π¹⁹, with all finite and real bounds fixed before contact primes. The actual shallow G2 ratio has precision 12; this supplies the M0 margin in 326 even though the required middle order is10. Choose 359's private quaternion witnesses afterward, without changing points or congruences, and apply the exact private map last. The alternate320/exact319 route instead uses 330's explicitly stronger Π³⁹ construction. These branches must not be mixed in a single proof paragraph.

## Unchanged source qualifications and conventions

The published inventory is SHA `b7c4027a0f735906b4fdde129f08294871332e49f68b25d5e2fc32e9c42d9674`; the Version 13 manuscript is SHA `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. `RETAINED-SOURCES.json` preserves the inherited source catalog and all 47 compatibility references, rather than replacing them with fresh paraphrases.

In particular, keep Silverman's pinned second edition and its recorded errata limitations, and Voight's corrected online v1.0.7u of August 5, 2026, with that edition's theorem/page references. Keep the restricted-converse and prime-pattern qualifications of the inherited inventories. No packet here proves a stronger external result or eliminates those qualifications.

Keep K=Q(√2), D=(3-√2)², P=2R0, the rational-coefficient basis, and the precise field-valuation normalization. At 2, the new coefficient statements use an integral formal subgroup, not good reduction. Distinguish F_s, the √2 coefficient of f([s]P), from X_n, the √2 coefficient of x([n]P). The physical X values are 2v83, 2v87, 2v89. The scalar coefficient is F_s=2g0g1. These factors cannot be inferred from coordinate names.

## Finite and artifact obligations still ahead

The326 and 359 inputs reuse residual IDs 903 and 904 for different equations. The three-anchor composition relabels only the anchor residuals to 1903 and 1904. It leaves coordinates 903 and 904 unchanged. The pending 318 transform deletes anchor row 1904 and coordinate 904, replaces 1903, and retains both detector rows 903/904. A naive numeric-ID union would lose defining equations.

Exact319/318 introduce three ordinary-monomial collisions between constant and C² parts. For 318 there are5679 coefficient-power entries but 5676 monomials after fixing C; its maximum is 186624C²+64. The old 16C² maximum and no-collision claim cannot be carried forward.

The published 411 companion uses a 16-coordinate constant chain and a Cτ product. It does not automatically yield an ordinary companion for the new unscaled anchor, whose T equation contains Cq with q quadratic. The new circuit needs a separately stored q when C is quantified. Any eventual count, coefficient bound, table, compact numbering and manuscript claim require their own frozen finite checks. The independent 379 decimal component belongs to another positive-anchor branch and cannot be combined by adding its count.

After a below 300 candidate is selected, the release still needs its complete frozen dependency packet, the final composition review, actual manuscript statements and application contracts with nine explicit obligations, new source/construction/consumer spans, independent acceptance of that exposition, full finite/ordinary artifacts and the ordinary release checks. Nothing in this preparatory inventory marks those steps complete.
