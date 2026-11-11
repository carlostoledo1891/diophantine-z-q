# Independent review of positive weighted squares

I accept the frozen positive-integer weighting of the accepted313 residual system and its stated328-variable ordinary companion. It preserves the complete rational zero set of each source system, including every input fiber. The claimed monomial counts and coefficient bounds pass an independent full expansion. No repair was required.

Reviewer: `/root/astra_quartic_opt01_elimination`, November7,2026. The root agent authored this weighting and its search/verifier. I did not contribute to that construction. I authored or coauthored some earlier residual-system components; this review does not renew their mathematical acceptance. It reviews the new compiler transformation relative to the separately accepted exact source systems.

## Frozen scope

The author packet is `work/quartic-optimization-20261107/root-sparse313`, with manifest SHA256 `3bac94d0090ac9abe8c6fc5f432a9935259934cf760b64049bc2974b644f9f11` and report SHA256 `cbf15de62cfea96e08ae8ed7c09af348c643792a663db991aa4ac344290295bb`.

| Artifact | SHA256 |
| --- | --- |
| Source313 IR | `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a` |
| Source328 IR | `aabaf282330f1f7d8d00f0dfc529020504890fee427dcaf9b0537bf1f2d53748` |
| Integer weights | `e332d37d8461797173b038b1253fa5f16770ab637b5353dbe2dcafd0c4605550` |
| Weighted313 polynomial | `c7863b51f07115db9f5f0d9ecce4173921a40bb93d02d442eb0bb98b480c1101` |
| Weighted328 polynomial JSON | `25cac3ad2777b39e628795bc2ea598932228796b822f03df5bc3cc832b313337` |
| Weighted328 polynomial text | `1b80f192909c4c4a124e5a4446a82603ef8ac99b11f87eb6c762f49d1a9b8944` |

The inherited source acceptance is agent10's `review-anchor-gamma313/REVIEW.md`, SHA `981dff20bd980f2a040e8b31418cdd0c74e7bcf6e1356c6322fd01f9b42cca13`. The ordinary source is covered by agent05's `resume-review-ordinary313-20261107/REVIEW.md`, whose exact328 source hash matches the table above. I read that review's source-specific map and count scope. Neither acceptance alone was used to approve this new weighting.

## Zero-set equivalence

For every source residual f_i, the primitive integer residual r_i differs from f_i by a nonzero rational scalar. Every specified weight is a strictly positive integer, and omitted weights are exactly1. Therefore, at any rational assignment,

```
sum_i w_i*r_i^2 = 0  if and only if  every r_i=0
                     if and only if  every f_i=0.
```

This uses only the usual order on the rationals. No square root of a weight, new coordinate, denominator guard, branch choice or new arithmetic premise is needed. The witness maps in both directions are the identity. The42 weight overrides refer only to existing source row IDs. The source variables and residual equations are unchanged.

The number283 remains the number of source residuals. As the author correctly notes, it need not be the number of unweighted squares in a presentation of the expanded polynomial. The validity of the zero-set argument does not depend on that representation.

## Independent full finite checks

My `check.py` imports no author producer or verifier. It rejects duplicate JSON keys, checks the source and artifact hashes, independently clears every row's rational denominators and integer content, and expands the weighted square with ordered term pairs. It compares every resulting coefficient with each full frozen JSON table. It separately parses every line of the ordinary ASCII table and compares that complete table as well.

All coordinates occur, every source residual has degree at most two, and both resulting polynomials have degree exactly four. The symbolic polynomial has5985 coefficient-power entries representing5982 variable monomials. After specialization at the specified C, none disappears: each leading coefficient is a nonzero integer, while the sum of lower magnitudes plus1 is below2^7. The fixed C=3^(2^25) is much larger. A literal coefficient of magnitude1 verifies content one after specialization, not merely content one in a formal polynomial ring.

For every other monomial coefficient p(C), I checked both M(C)-p(C) and M(C)+p(C), where M(C)=186624*C^2+64. Each nonzero difference has positive leading coefficient; the lower-magnitude dominance bound is below2^1520. Consequently the exact maximum is M(C), uniquely at x89^4. This is an exact integer comparison, not floating-point evaluation or a bit-length proxy.

The ordinary source changes only rows504 and1903 and adds its already reviewed constant-chain rows. None of those changed or added rows receives a new weight. All other residual objects agree literally between the symbolic and ordinary source systems. Thus the existing unique-extension map for the constant chain and the new identity-map compiler transformation commute.

The weighted ordinary table has328 variables and6024 monomials. It has degree four and content one, and its maximum absolute coefficient has6496 bits. The ASCII table is209130 bytes and matches the frozen hash. These facts were computed from all coefficients, without assuming that the maximum integer equals the unweighted source maximum.

## Limits and preservation

This accepts only the integer-weight artifact identified above. The earlier rational-weight alternative is not included. The search need not be exhaustive for the equivalence proof, and no global sparsity optimum is claimed.

No new local, elliptic, approximation, height, prime-choice or restricted-converse argument is involved. Their hypotheses remain exactly those of the accepted source systems. There is no variable-count improvement and no below300 publication milestone. This review does not authorize manuscript integration or publication.

Every file in the author manifest was checked before and after the independent calculation; all remained unchanged. `CHECKS.json` and this directory's manifest record the independent results and pins. No unresolved defect was found in the reviewed transformation.
