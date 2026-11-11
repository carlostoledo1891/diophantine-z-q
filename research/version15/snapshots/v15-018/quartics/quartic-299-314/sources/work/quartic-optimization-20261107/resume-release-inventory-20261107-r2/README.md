# Preparatory inventory revision 2

This revision records the accepted **combined315** construction and its exact lineage. It preserves the preceding inventory packet unchanged. It introduces no new mathematical acceptance, production application record, manuscript version or publication approval. The selected construction still has 315 total variables, above the strict threshold of fewer than 300.

The source reports were read alongside their independent reviews. Some frozen author reports still say that review is pending. Those statements describe their freeze times. The later, separately pinned reviews establish the statuses recorded here; the author reports have not been rewritten.

## What changed since revision 1

The complete application delta still covers all 39 published Version 13 records. It now has 23 proposed internal entries and 22 canonical candidate records. N01 through N19 retain their earlier source bindings. Four new entries cover the shorter Laurent chain, ordinary constant lifts, sparse Lucas recentering, and the optional restricted constant-chain lower bound.

| Candidate | Source and transformation | Current recorded scope |
|---|---|---|
| threeAnchor319 | three326 plus the abscissa359 anchor | Root's accepted composition; original Pi19 completeness |
| exact319 | combined320 plus exact private anchor unscaling | Accepted component; the separate strong-H/Pi39 branch |
| combined318 | threeAnchor319 plus the exact319 transformation | Accepted whole composition; original Pi19 |
| chain323 | three326 with one private helper removed per detector | Accepted exact solution-set equivalence |
| combined315 | combined318 plus chain323 | Accepted whole composition; original Pi19 |
| sparseLucas320 | combined320 with an affine Lucas recentering | Accepted separate term-count variant; zero variable saving |
| ordinaryExact319_334, _335, _336 | exact319 plus a root-sum gate and weighted constant chain | Three accepted ordinary artifacts on exact319 only |

The full IR SHA-256 is the canonical candidate ID. `CANONICAL-INDEX.md` gives the hashes, counts and immediate sources. `CANDIDATES.json` also records component-transport edges, author and reviewer identities, exact source comparisons and all added, changed and removed coordinate and residual IDs. Its reviewed monomial counts are source claims bound to the reviews, not newly recomputed SOS results.

The new recorded review hashes are:

* combined318: `b1282b2283b940df8b61c04d67eaf3b2e89906fa0ec41c07af006e073003ceaf`.
* chain323: `ab7a9e1c126823950c76e6fa9ae8523fb166c89e46f0ac3202d6b06752c2ece4`.
* combined315: `4585097b153c7bcb534eb209bd1bcea504a4f894d48fbdfa41dea5522007ca5c`.
* ordinary lifts: `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`.
* sparseLucas320: `fef1d4cc3fad17ee386d7a2999128efab23deb3a825258ae653cfbad4de5cbd2`.

## Proof integration

`PROOF-INTEGRATION-OUTLINE.tex` is a separate draft outline. It gives the proposed order for chart reconstruction, exceptional branches, changed contact predicates, root parity and the shifted quaternion application, three-group valuation packing, exact unscaling, and the shortened chain. It also separates the optional ordinary and sparse variants.

`INTEGRATION-MAP.json` connects all 23 working entries to exact outline labels and line numbers, source-report spans, non-author reviews, and the retained Version 13 consumer spans. It distinguishes the selected construction's uses from separate variants. These proposed labels are not production theorem labels. The eventual manuscript needs complete statements, proofs, construction and consumer bindings, the protocol's nine application obligations, and independent review of that exact exposition.

The proof order for 315 starts by inverting the new chain map to obtain an actual 318 solution. Invert private unscaling next. Then use the shifted anchor to recover root parity and restore the 326 source before its S-sign and pre-H arguments. Completeness starts with the original Pi19 construction, selects private quaternion witnesses afterward, then applies unscaling and assigns the unique new chain helpers. No additional local or real choice is introduced by the last two maps.

The selected chain retains ER=1 and forces J=R cubed before dividing by J. It preserves every consumed power through E158, all root and scalar data, detector group values, pole values and private anchor witnesses. Its equations work for either sign of R and introduce no square-root branch. The accepted composition checks their actual affine normalizations and complete consumers.

## Ordinary and sparse scope

The ordinary lifts now have full accepted decimal artifacts, but their exact source is **exact319**, not threeAnchor319 or combined315. They have 334, 335 and 336 total variables. Their maximum coefficients have 6496, 3250 and 1627 bits respectively, including the inherited constant contribution K. The 334 artifact meets the 8193-bit cap; the 336 artifact meets the tighter 3247-bit cap; the 335 artifact exceeds the latter by three bits. The gate lower bound is limited to the expressly isolated acyclic monomial-chain model with counted seeds and a separate root-sum gate. It is not a universal minimum.

SparseLucas320 changes only the two private product coordinates by subtracting twice Z, preserving the physical output components v253 and 2*v254. It reduces the quartic table by 61 monomials while keeping 320 variables. Its accepted maximum is the source-specific 16C squared. The selected combined315 instead has maximum 186624C squared plus 64; these coefficient claims must not be interchanged.

Separate transports named sparse315 and ordinary-sparse315 are outside this revision. This revision grants them no status, count or approval. Their literal equations and full polynomial tables require separate reviews.

## Preserved evidence and checks

`PREVIOUS-REVISION.json` pins every file of revision 1. Its historical pending318 status remains intact. `PRESERVED-ALTERNATIVES.json` retains the adverse and unsuccessful routes, including the pre-H repair history, conditional exact-valuation route, positive-anchor branch and unsuccessful logarithm searches. `RETAINED-SOURCES.json` preserves all published source editions, errata and theorem qualifications.

`SOURCE-PINS.json` binds the input files read for this revision. It includes every file of the ordinary packet's manifest. The status index is only a navigation aid and is captured in `STATUS-SNAPSHOT.json`; independent reviews supply acceptance evidence.

`build_revision.py` reads and hashes sources without importing or executing candidate code. It validates all inherited frozen pins, reads the exact new candidate IRs, compares the full coordinate and residual objects, checks the ordinary manifest, and builds the consumer map. `CHECKS.json` records structural consistency checks. Those checks are not a repeat mathematical audit. No production inventory, manuscript, repository, controller or frozen author file was changed.

`check_revision.py` repeats the source-pin, prior-packet, canonical-ID, proof-span and consumer-link checks without rebuilding any notes. It also checks TeX braces, environment nesting and label uniqueness. A compilation attempt stopped before reading the source because the local MiKTeX setup could not create its configuration directory. No compiled PDF or successful TeX build is claimed.
