# Independent review of the 443-variable scalar-ratio fusion

Reviewer: the parent agent, `/root`. Decision: accepted for the exact research candidate below. The suggestion came from `astra_bl5_models` and the implementation from `astra_quartic_opt10_combination`. This review was derived and implemented separately from both agents' checks. It does not establish a new review of the inherited arithmetic proof, nor does this count reach the below-400 publication threshold.

## Frozen files

- Source445 SHA256: `173e0e79a5eb9404917e952117666f3de7920ca876eae2163ac0d20981414e3e`.
- Candidate443 SHA256: `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`.
- Polynomial443 SHA256: `b2d2600ff4d088e3ff2d5ec398218c5f255770d17767948173ce2fd3c5eb7d68`.
- Author report SHA256: `97d9095a6d61615fbb029e4f3d76733f988183edc273b67a5065f7cd05bdeb88`.

The candidate, polynomial, and author report are `scalar443-ir.json`, `scalar443-polynomial.json`, and `REPORT443.md` under `../10-combination`. The source is `../03-depth/further/candidate445-ir.json`. The independent executable check is `review_scalar_fusion.py`, and its output is `scalar-fusion-receipt.json`. It imports no producer or previous verifier.

## Equations, conventions, and domain

All field equations are in K=Q(sqrt(2)), with multiplication `(a,b)(c,d)=(ac+2bd,ad+bc)`. The retained chart for H is x=h² and j²=x²-D, where D=11-6sqrt(2)=(3-sqrt(2))². The physical x coordinates have the convention x=x90+2*x91*sqrt(2). The checker verifies the actual four chart rows with that factor of two. It also verifies the retained equation hs=j against its literal two component rows.

Both h and j are nonzero on every rational solution of these chart equations. If h=0, then j²=-D, impossible under either real embedding. If j=0, then h⁴=D, hence h²=±(3-sqrt(2)). Applying the field norm gives Norm(h)²=7, impossible for a rational number Norm(h). Therefore s=j/h is defined and nonzero. These are algebraic consequences of retained rows, not restrictions on the specially chosen completeness witnesses. I also read the corresponding chart proof and scalar-ratio convention in the pinned v12 manuscript, lines 19331–19408, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

Write z for the old scalar parameter pair and rho for the retained scalar ratio pair. The actual scalar equations have the form

    T z + B = 0,
    h rho + j z = 0,
    h s - j = 0.

T and B are affine field expressions in retained coordinates. The checker extracts their coefficients from the literal old scalar rows, verifies both components of Tz+B, and checks the old ratio equation separately. Thus it does not infer the expressions from potentially stale semantic metadata.

The new equation is

    T rho - B s = 0.

Its rational components are quadratic. The sign in front of Bs is negative; rho=-s*z. The checker establishes the full polynomial identity

    h(T rho-Bs) = T(h rho+jz) - j(Tz+B) - B(hs-j).

Since h is nonzero, every old solution gives a new solution by forgetting z. Conversely, define z=-rho/s. The new equation implies Tz+B=0, and hs=j implies h*rho+j*z=0. The old ratio equation forces this same value of z, so these maps are mutual inverses and fix every retained coordinate. No division by T, B, rho, or z is needed. In particular this proof does not introduce an exceptional branch when any of those values is zero.

## Complete consumer and polynomial checks

The deleted coordinate IDs are exactly 506 and 507. Their only occurrences in the source are the four old component rows for `Sscalar.z` and `scalar.zRatio`. Exactly those four rows are replaced by the two new component rows. Every outside row object, including its coefficients and metadata, is identical. Every retained coordinate object and the fixed-parameter record is identical. The retained ratio coordinates 508 and 509 therefore have their old values in all downstream norm, height, and pole consumers.

The checker independently expands the primitive integer residual squares using a triangular product loop and compares every coefficient against the supplied polynomial table. The result has 443 total variables, 442 witnesses, 420 quadratic residuals, degree four, and 6,616 nonzero monomials. After specializing C=3^(2^25), its content is one: the x1^4 coefficient is exactly one with no other C contribution. Its unique quadratic-C contribution is 16*C²*x57², with no lower-C term there. Ordinary coefficients have bit length below 2048, and linear-C coefficients have multiplier at most 48. Thus the largest coefficient magnitude remains exactly 16*3^(2^26).

This is an exact equivalence of rational witness sets over the full retained chart domain. It changes no approximation estimate, local integrality premise, prime choice, or order of completeness choices. Acceptance is limited to the frozen transformation and files identified above.
