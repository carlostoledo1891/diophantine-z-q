# Scalar correction composition at 417 variables

The frozen candidate has 417 total variables, 416 existential witnesses, 386 quadratic residuals and 6,296 monomials in its squared residual polynomial. Its degree is four, its integer content is one, and its largest coefficient is 16*3^(2^26). This is a research candidate awaiting independent whole-composition acceptance.

| Artifact | SHA-256 |
|---|---|
| Accepted source combined423-ir.json | 3c19ce0d46ae80732e76fd243b7fd1c91599f4274e1c67b9a4ac6c5bd86899bf |
| Candidate combined417-ir.json | b7d124eb221df55d49131854b541a4c97c5689b18882dfa4a24cc6b8c2d1b6a9 |
| Polynomial combined417-polynomial.json | 8272326ab3ea2e7b6996221cee758658dc1a4266e68ada3748af75b5ef289ae6 |

The certificate binds both component sources, their exact targets and their independent reviews. The first component changes beta=2X^2+2403 to beta=51(2X+1)^2+2504 and replaces five correction choices with one. The second component uses c=r+4896 and removes the remaining choice and corrected-product coordinates. Both component reviews are copied into inputs. They establish arithmetic replacements, not equality of the old correction witness fibers.

The composer checks every touched coordinate name and every old residual before applying the two deltas. The producer-free verify_combination.py 417 independently replays those deltas and expands the full polynomial. The separate read-only verify417_interfaces.py rediscovers every current consumer of the input-square coordinate. There are thirteen retained consumers, all transformed by Y -> 102Y+102X+76. The two additional source consumers in the older fifteen-row list belong to the removed corrected-product equation and replaced scalar-input equation. The checker verifies the replacement input from the actual current r, rather than requiring a stale consumer count. The equation Y=X^2 is unchanged.

The final scalar-input row is

```
(rSquared+4896*r)*storedWSquared+82479248*storedB=0.
```

The checker extracts the affine r from the physical depth24 norm-root equation, verifies rSquared=r^2 from its retained defining row, and checks this complete input row including sign and normalization. The same physical norm-root and scalar-input expressions occur in the independently accepted deterministic component.

## Arithmetic interfaces requiring final review

The integer-input bridge now uses the retained odd integer n. Once the unchanged contact argument proves n=beta, squarefreeness of 51 first makes 2X+1 an integer and oddness makes it odd; hence X is integral. Conversely every integral X gives the reviewed positive label and local correction classes.

The scalar depth24 argument consumes the same r powers, norm square, ratio coordinates, W and pole input normalization. Only c changes. At consumed scalar contact primes, odd valuation of r is positive before the unit assertion is invoked. Then r+4896 is a unit. At the fixed primes 2,3,17, c/r is a square. Extra prime factors of c enter the finite preparation support before the continuity modulus and prime choices. No bound on those prime factors is assumed.

The primary identity extension and H rescaling remain untouched. Its pre-ratio V0 exclusion still uses the fixed value f(H) at H=P, the three contact radicals, the root-height estimate and the scalar index anchor. The label replacement keeps the accepted scalar depth24 height estimate and all anchor constants; the deterministic correction changes no root, logarithm or anchor equation. This compatibility must be included in independent final acceptance, rather than inferred from matching polynomials alone.

All other equations and coordinates are preserved under the declared input substitution. The squared-output interfaces used by the hybrid detector circuit, the rational-log denominators and the odd-root charts are unchanged. The complete polynomial checks establish every variable occurs and the coefficient bound. They do not replace the separate arithmetic arguments or the final composition review.

No manuscript or released repository file was changed.
