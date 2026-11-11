# Independent review of the 433-variable composition

Reviewer: `/root`. Decision: accepted for the frozen research composition.

The source435 has SHA256 `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859` and independent parent acceptance in `REVIEW435.md`. The separately reviewed H.j elimination is the439-to437 component, SHA256 `e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e`. Its non-author review is `../00-independent470/REVIEW437.md`, SHA256 `ae596f97982b2c02bed099b00713457aa5e58ef6153de573577c42b425691d2f`.

The resulting candidate `../10-combination/combined433-ir.json` has SHA256 `207218ebbcd15fa97f69580fce71629a50e34129549e80a9568dbed57ae28832`. The full polynomial has SHA256 `9583374b2e7cd636739a62608906a76592606fdcca76304b2836c1154ce569d0`.

I read the full component argument and its independent review. Its maps are j=h*s and g=h*v in the reverse direction, and v=g/h in the forward direction. The retained equations x=h² and xf=1 prove h and x nonzero before these divisions. The new equations are exactly the old H curve, reciprocal V0 equation, V0 square, and physical logarithm equation after canceling the proved nonzero h or x. The maps preserve every other coordinate, including the actual rational logarithm output. They introduce no additional arithmetic premise.

The guard and shifted-label changes that produced435 have not altered any of those source equations, the retained H.x and f(H) relations, or the interpretation of the primary reciprocal s. They also have not added any consumer of H.j or the reinterpreted V0 g pair. This is verified against the literal full source rather than inferred from the names of the earlier changes.

The independent script `check_component_transport.py` derives the component delta from the pinned439 and437 files, checks its exact preimages and changed-coordinate incidence in435, and reproduces every coordinate and residual of433. It compares all non-ID row data and forbids duplicate row IDs. The complete coefficient table is then checked by a separately implemented triangular expansion of the primitive integer residual squares.

All checks passed. The construction has433 total variables,432 witnesses,410 quadratic residuals and6,507 quartic monomials. After specializing the fixed C=3^(2^25), its content is one and its largest coefficient magnitude remains16*C²=16*3^(2^26). These facts use the checked isolated coefficient-one monomial and the unique quadratic-C coefficient, together with bounds on every other coefficient.

The receipt is `transport433-receipt.json`. Acceptance is limited to this frozen composition, with its separately reviewed source and component dependencies. Proposed norm-tree and identity-domain changes are not included. No release is justified until the total variable count is strictly below400 and the corresponding release review is complete.
