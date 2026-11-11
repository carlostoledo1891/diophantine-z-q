# Fixed-witness characteristic-zero Kummer inputs

Reviewer: /root/v14_arithmetic_review. Accepted within the three stated input scopes. Target v14-rc-witness-kummer-inputs-001/MANIFEST.json SHA256 54c2c2a3688acaa75acc5ee78641a97a590bdbbb58049d3a9a8e05f8e1ee3535, current manuscript1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8.

I read the actual3335–3355 construction, the retained finite Kummer proof and the source profiles, and directly checked Silverman VIII Theorem4.1 at printed220. The actual point is rational on the fixed twist, so the theorem over Q suffices. Rational nontorsion remains supplied by3335–3342, not by Mordell–Weil.

A zero rational Tate Kummer class would become an integral coboundary after multiplying by one power of2. Reducing every level and using the finite Kummer injections puts that multiple of the point in every2^a E(Q). For a finitely generated abelian group the intersection is odd torsion. This contradicts the given nontorsion point. The argument does not need a limit-surjectivity assertion or finite Sha.

The retained Serre openness theorem applies to the actual non-CM twist. An open subgroup of GL2(Z2) contains a principal congruence subgroup; hence the rational representation is irreducible and there is a nonidentity central scalar. If the translation restriction vanished, the cocycle would descend to the Tate image. The displayed scalar identity then makes it a rational coboundary. Thus the translation subgroup is nonzero; its stable rational span is full by irreducibility. Its compact closed additive subgroup has full lattice rank, and intersection with a finite-index kernel preserves rank. These local deductions use the three inputs together; openness alone does not assert Kummer translation nonvanishing.

All manifest members and distinct source/current span bindings pass CHECKS.json. This accepts only the characteristic-zero portion of original residual3. Finite-field specialization, same-place reduction and the stated detection at3360–3373 remain separately required. The new rational Mordell–Weil statement card still requires installation/source-scope handling.
