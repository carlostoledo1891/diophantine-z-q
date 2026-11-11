# Independent review of the isolated scalar guard replacement

Reviewer: `/root/astra_bl5_models`. Decision: accepted for the exact 443-to-442 change, with the 443 source and its established scalar-point interpretation as explicit dependencies. This is a research review, not a release approval.

I proposed the preceding 445-to-443 scalar-fusion identity and therefore do not claim independent acceptance of that step. The present guard replacement was authored separately by agent02. I reviewed its new arithmetic use, literal source and target equations, complete consumer incidence and coefficient table.

## Frozen files

- Source443: `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`.
- Candidate442: `7c8bcbb20289e92e790a0728a96428b451516842420454355731e64a950d7c3b`.
- Polynomial442: `8fdc5a0d7fcf0ed90a0028d9585dba23f02fbc59a1de52a257da5952502a4f90`.
- Certificate: `28d47602b24b282c4f3fc7ebbc6cca2b25922efbb277c6f5522fdb979ca0a4ab`.
- Author report: `37c7f07fe214497b2e2af381df4735e676fdb419d4ad71cb986fef43c440883c`.

`replay442.py` runs the producer-free checker with source writes suppressed and adds specialized coefficient checks and the exact leading-residue calculation. Its results and log are saved alongside this report.

## Literal change and reverse map

The old rows give `f0=g0^2+2*g1^2`, `f1=2*g0*g1`, and `f0*sigma=1`, in slots 504,505,543,544,549 as specified by the author. The new system deletes slot504 and its definition, keeps f1's definition, and replaces the inverse row by `f1*tau=1`, reusing slot549.

The checker proves that slot504 has exactly its definition and inverse as consumers, and slot549 has only the inverse row. Every outside residual object is unchanged, including its metadata; every outside coordinate object and fixed parameter is unchanged. In particular, the anchor continues to consume exactly the same slot505, and no scalar ratio, norm, height or detector value changes.

For any new rational solution, f1 is nonzero, so both rational g0 and g1 are nonzero. Define `f0=g0^2+2*g1^2>0` and `sigma=1/f0`. This reconstructs the old deleted definition and inverse row, without any group-theoretic argument. The old source's scalar-point interpretation therefore applies to that restored solution. No new zero branch survives this direction.

## Forward map and exact arithmetic dependency

For an old source solution, the retained scalar chart identifies the actual difference as `R=S-P=[s]P`, where S has odd index and the source f0 guard excludes S=P. Thus s is a nonzero even integer. This implication belongs to the source's proved point/odd-coset interpretation, including the reciprocal-chart exceptional cases; it is not deduced merely from arbitrary rational g0,g1.

I read the cited v12 Lemma `lem:v12-anchor-coefficient` and its proof at lines20115ff, and the scalar reciprocal-chart proof at lines20365–20445, in manuscript hash `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The coefficient lemma proves

`v_3(f1([s]P))=2+2*v_3(s)`.

The new use needs only its finite valuation, hence nonvanishing. The displayed exact z(2P) calculation reduces after division by3 to `2+sqrt(2)` in F9; I independently checked the two rational residues and that its square is sqrt(2). Writing `s=2*3^k*u`, the odd integral formal multiplication series preserves that leading residue under multiplication by3 and multiplies it by u modulo3. The error after division has valuation at least `2r-1>0` at depth r>=1. The curve relation `f=z^2*(1-D*f^2)` then gives the leading residue sqrt(2) for `f/3^(2k+2)`. Independence of 1 and sqrt(2) in F9 proves the exact irrational-coefficient valuation. Negative u causes no exception because u^2=1 in F3.

Consequently every full old source solution has f1 nonzero. Set tau=1/f1, forget f0 and the old inverse, and preserve everything else. This gives a new solution. The map would be false for a standalone arbitrary g with f0 nonzero and f1=0; the full-source nonzero-even-index condition is essential and is retained explicitly in this acceptance.

The extra reciprocal-chart case S=-P gives s=-2 and still has nonzero f1. The full anchor in fact excludes that shallow case, but the guard replacement does not need to discard it separately. There is no new assumption that the rational coefficient f0 alone controls the irrational coefficient.

## Composition and counts

The two maps preserve every retained value except the repurposed inverse slot, including the actual scalar ratio and f1. Their inverse values are uniquely determined. Hence they establish equality of the full rational solution sets projected onto the shared coordinates, and in particular equality of the rational input projections, once the source443 dependency is supplied.

The complete primitive sum-of-squares table agrees with the frozen polynomial:442 variables,441 witnesses,419 quadratic residuals,degree4 and6611 monomials. The fixed parameter remains C=3^(2^25). A coefficient exactly1 survives with no C contribution, and the unique C^2 term remains `16*C^2*x_57^2` with no lower-C term on that monomial. The checked ordinary and linear-C bounds therefore give specialized content1 and maximum absolute coefficient `16*3^(2^26)`.

No defect was found in this isolated guard change. This report does not replace the separate independent review of source443 or approve any later combination.
