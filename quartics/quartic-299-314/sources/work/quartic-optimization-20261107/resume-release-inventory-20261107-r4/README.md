# Preparatory research inventory revision 4

This revision records the accepted shared314 arithmetic and construction, its sparse-Lucas transport, three ordinary companions of sparse314, and the new anchor-gamma313 construction. It preserves revision3 and its independent review unchanged. It is an author-prepared inventory awaiting its own independent review. No mathematical acceptance, production inventory change, manuscript revision or publication approval is created here.

The selected candidate is `anchorGamma313`, IR SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`, with313 variables. Agent10 independently accepted its proof and literal artifact in `review-anchor-gamma313/REVIEW.md`, SHA256 `981dff20bd980f2a040e8b31418cdd0c74e7bcf6e1356c6322fd01f9b42cca13`. Inventory author agent05 authored the coupling/compiler, and agent03 contributed the constructive approximation proof. Those contributions are not independent reviews. The inventory records agent10's existing acceptance rather than self-certifying the proof.

All candidates remain above the strict below300 publication threshold.

## Scope and identities

`CANDIDATES.json` now contains28 exact IR identities. Display names and variable counts do not identify a candidate. The selected continuation after combined315 is shared314, sparseShared314, anchorGamma313. The ordinaryShared314_331/330/329 branch starts at sparseShared314. It does not start at anchorGamma313.

The accepted ordinary families in this cutoff are the earlier exact319 lifts and the new sparseShared314 lifts. The current machine classification says that no ordinary lift of the selected313 is included. Other later transports outside this cutoff are not declared unreviewed merely because they are absent. Inherited soundness/completeness records explicitly named for315 remain historical; the catalog adds separate313 ordering records.

For compact new records, aliases01,03,05,10 refer respectively to `/root/astra_quartic_opt01_elimination`, `/root/astra_quartic_opt03_depth`, `/root/astra_quartic_opt05_anchor`, and `/root/astra_quartic_opt10_combination`. The mapping is also machine-readable. Multiple author aliases denote contributors, not additional independent acceptances.

## New application entries

The inventory retains all23 earlier entries and adds ten:

| Entry | Recorded change |
| --- | --- |
| N24 | Common-scale local residue classes, guard forcing and same-place bounds, including pre-H branches |
| N25 | H-depth bootstrap from initial formality, integral ratios, F(0)=-1 and a unit Li |
| N26 | Common-scale completeness with original Pi19, uniform finite/real bounds and denominator parity |
| N27 | Exact sparse-Lucas coordinate map on shared314, preserving the physical F/F+1 interface |
| N28 | Exact ordinary constant-chain lifts of sparse314, with actual source-specific coefficient bounds |
| N29 | Eight-coordinate anchor-gamma chain and unconditional reverse reconstruction to314 |
| N30 | Extra allowed scalar finite depth and explicit local anchor targets at2,3,17 |
| N31 | Contact-prime anchor targets by a binary norm equation and nonsingular local lifting |
| N32 | One rational reflection map, local density and constructive simultaneous rational approximation |
| N33 | Complete ordering of fixed scalar/root data, bounds, contacts, lambda, anchor and final H |

Each entry records old/new objects, the exact internal lemma or substitution, author and non-author review, source sections, actual residual or proof consumers, and direct links to the original Version13 applications. These are direct application/restoration links, not an exhaustive transitive dependency graph.

`NEW-INPUT-CLASSIFICATION.json` separates the newly proved internal statements from retained arithmetic inputs and standard external facts invoked without reproof. For example, the reflection identity and coordinatewise approximation construction are internal proofs. The old quaternion criterion supplies their basepoint. Hensel's lemma, unit-square criteria, finite-field multiplicative cyclicity and integer CRT are standard invoked results, not newly proved theorems. No general weak-approximation theorem for quadrics, stronger prime-pattern input or stronger Pi progression is used.

The retained arithmetic application records pin exact Version13 spans for the depth-one unit identity, scalar finite preparation, quaternion criterion, real-progression lemma and simultaneous-prime theorem. New uses preserve their stated field, curve, normalization, order and domain qualifications.

## One relation and all derived views

`spec.py` explicitly specifies the ten new entries and their direct baseline targets. The117 reviewed r3 edges remain present. `CANONICAL-RELATION.json` has169 edges. Both directions in `APPLICATION-DELTA.json` and every integration-map consumer are generated from that relation. New scope fields use `selectedCandidateDependency`; the old315-specific values are preserved under an explicitly historical name.

The39 baseline source records, consumer spans and canonical record hashes are unchanged. The builder computes full coordinate/residual deltas for all six new candidate IRs. The checker independently recomputes these and the inherited deltas. It also checks exact source hashes, proof-section line spans, normalized retained-source span hashes, outline labels, candidate lineage and source-specific ordinary status.

Sixteen negative fixtures reject missing or extra edges, duplicate or unknown endpoints, scope changes, baseline and actual consumer drift, stale ordinary status, falsely included313 lifts, a wrong ordinary parent, an omitted H-bootstrap entry, author self-review, invented acceptance and changed proof bindings. `CHECKS.json` records the structural result. These checks do not prove the underlying mathematics or grant an independent inventory acceptance.

An initial checker run treated the inherited source descriptor `Whole report` as a literal Markdown heading. It failed on N22. The checker now handles that existing descriptor only by requiring the complete line range; all actual heading descriptors still require an exact match. No source span or mathematical record was changed to pass that check.

## Preservation and proposed exposition

`PREVIOUS-REVISION.json` pins every r3 file and its independent acceptance. Mutable historical STATUS references are not revalidated as immutable evidence; their earlier snapshots remain in the pinned r3 packet. No current candidate status is inferred from a live mutable status file.

The rejected original common-scale156 proof, its erratum and the narrower reciprocal-variant review are added to the adverse-history list. The original exploratory anchor note is also preserved. None is silently promoted to the final313 proof.

`PROOF-INTEGRATION-OUTLINE.tex` retains the r3 outline as explicitly historical text and appends separate labeled sections for N24 through N33. The new integration map binds all labels and consumers. It remains a proof-integration outline, not a production manuscript or fully reviewed exposition. No PDF build is claimed.

Reproduce with the supplied Python runtime, from the workspace root:

```text
python -B work/quartic-optimization-20261107/resume-release-inventory-20261107-r4/build_revision.py
python -B work/quartic-optimization-20261107/resume-release-inventory-20261107-r4/check_revision.py
```

The scripts execute no candidate code. All output is confined to r4. Once frozen for independent review, verify without overwriting it, or redirect generated check results to the reviewer's own directory.
