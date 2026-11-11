# Independent preparatory inventory review

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Packet author `/root/astra_quartic_opt05_anchor`. This review concerns inventory accuracy and proposed integration. Mathematical component decisions remain those in their separately pinned reports.

## Decision

Corrections required before this packet becomes the authoritative integration inventory. The frozen manifest is `56a0e6a76318e56af6158ea1ccb325457b0c3a4772974c5849b935b52c9ba97d`. The outline is `43dd55c133812149952ea26dffcf2608d6451e85e41b411b08785787b5691a94`. Preserve these bytes as the reviewed revision.

## Required corrections

1. Reconcile the two application-to-entry relations. In APPLICATION-DELTA.json, application.newEntryIds and newInternalEntries.baselineApplications disagree for 23 of 39 applications. CHECKS.json in this review records every difference. For example, MODEL omits N08 in its application row although N08 names MODEL. FINAL-COMPLETENESS names N18 only on the application side, while N08, N10, N11, N17 and N19 occur only on the entry side. IDENTITY-CHARTS names N02 and N03 only on its application side. INTEGRATION-MAP.json is built from the entry-side relation, so a reader following an application record receives different coverage from a reader following the proposed proof map. Resolve each edge against its actual mathematical use, retaining selected versus alternative scope, and generate both directions from that reviewed relation. Add an equality check for every application. Taking the union automatically would conceal mistaken edges.

2. Update the current machine classification for V13-ORDINARY-GATE. It still says `new_artifact_required_not_accepted`, while its revision2Note and N21 correctly record accepted exact319 ordinary artifacts. Preserve that old classification in historical revision data and give the current field a source-specific classification that also records that combined315 has no ordinary lift within this cutoff.

## Checks completed

The independent check.py verifies every manifest byte hash and length, all 39 baseline record hashes, 180 raw source and consumer span hashes, preservation of the baseline source records and qualifications, and all coordinate/residual object differences for all 22 candidates against their recorded comparison sources. The author structural checker also passed for 107 nonmutable source pins, previous-packet preservation, outline labels and spans. The independent script imports no author checker or candidate code.

Full IR hashes distinguish exact319 from threeAnchor319 and the three ordinary companions. Author and reviewer identities differ in all 22 candidate records and all 23 proposed entries. Recorded identities are documentary provenance, without provider attestation. The retained source catalog preserves the corrected Voight edition, Silverman limitations, errata caveats and restricted-converse qualifications. Adverse and superseded routes remain classified, including the pre-H repair, conditional357, positive-anchor alternative and unsuccessful searches.

The text distinguishes exact substitutions N01/N02/N12/N18/N20/N21/N22 from changed local or arithmetic applications N03-N11/N13-N17/N19. The outline retains the zero/domain restrictions, same-place valuation requirement, root parity before H inference, selected Pi19 progression, separate Pi39 branch, nonadditive alternatives and optional restricted constant-chain bound. Its chain and unscaling formulas agree with the already reviewed sources. Component reports and their later independent reviews are distinguished by freeze time.

The explicit cutoff excluding sparse315 and ordinary-sparse315 is respected. Their later acceptances create no defect in this earlier snapshot. The document remains an outline with full exposition and application contracts outstanding. TeX compilation was not completed in the packet because of the recorded MiKTeX setup failure. This review checked lexical structure through the author checker and does not supply a PDF build or new mathematical theorem acceptance.

## Reproduction

Run this review's check.py with Python 3.14. The result is in CHECKS.json. It deliberately records relation differences instead of treating matching counts as sufficient coverage. Run the packet's check_revision.py separately to reproduce its narrower structural result. No candidate, published repository or author packet file was changed.
