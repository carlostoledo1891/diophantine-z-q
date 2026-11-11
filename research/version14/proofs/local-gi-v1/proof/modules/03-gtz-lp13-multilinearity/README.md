# Local Lemma 13.2 repair, draft 002

This successor makes the natural ultrapower interpretation explicit, citing Appendix A.2/A.3. The exact vertical identity quantifies over all limit points and all limit top-group elements. The proof does not infer that identity from standard-point-only equivariance. This is a definition-domain clarification requested in independent review; the algebraic construction is unchanged.

The b842 manuscript consumer pins now refer to the byte-identical frozen predecessor in `combined-source-revision-001/previous`, because the live manuscript has advanced. Their mathematical text and line ranges have not been approximated or rebound to the new manuscript. The eventual theorem assembly must map the new current version separately.

This is an author proposal for the unchanged multilinearity statement in GTZ Lemma 13.2. The proof constructs a descending rational filtration using all generators of weight at least the index. It normalizes the constant polynomial coefficient using a bounded representative, restricts the orbit to the positive-index group, and takes the central top-layer quotient. It proves the subgroup, lattice, polynomial, vertical-character and uniform Lipschitz claims used by this construction.

The proof also checks that the bounded normalization preserves the same standard vertical character. This matters when the polynomial coefficients are limit objects. Its conclusion is the exact lower-degree nilsequence representation required by the original symbol equality.

The source defect is independently recorded in `../../independent-sol-lemma13-2/REVIEW.md`, as pinned in the manifest. This draft proposes a repair; it does not close the finding or supply its own independent acceptance. Sol's earlier repair outline is acknowledged as input to authorship, so any independent acceptance must account for that participation. The parent should arrange non-author review of the resulting proof.

The local theorem supplies the multilinearity input to the Section 13 consumers. It does not establish the separate symbol-shift, multilinearization, Section 12 quotient, or Proposition 7.3 corrections, and it does not declare the complete inverse theorem verified modulo published theorems. The release manuscript and the frozen DK replacement packet remain unchanged.

`SOURCE-USES.json` records ten-field assertions and exact raw proof spans. `APPLICATION.json` records the composite application and nine unresolved review obligations. `CONSUMERS.json` lists the published and manuscript consumers with their remaining dependencies. `MANIFEST.json` freezes all authored files, the build output and source pins. A successful TeX build checks rendering only.
