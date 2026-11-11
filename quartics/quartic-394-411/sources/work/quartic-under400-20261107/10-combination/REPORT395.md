# Frozen 395-variable composition

The final research candidate has 395 total variables, 394 existential witnesses, 365 quadratic residuals and 6,341 quartic monomials. Its degree is four, content one and largest integer coefficient 16*3^(2^26). All component changes have independent reviews and the complete finite chain has passed. Final non-author mathematical composition acceptance is pending.

| Artifact | SHA-256 |
|---|---|
| Accepted source combined417-ir.json | b7d124eb221df55d49131854b541a4c97c5689b18882dfa4a24cc6b8c2d1b6a9 |
| Final combined395-ir.json | 440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a |
| Final combined395-polynomial.json | 3d7c165ffb4171fe3dc11559b1a2bb29ff24dcb02289303d4544e8c5a5667d85 |
| Alternate combined397-ir.json | 964c1fe55b9ae5d4aba51005d8d2536b5f248b87f4ac840a4bae874b0fab3c1b |
| Alternate combined397-polynomial.json | 801ae87aa8616b0b958c6fc584b4c6d383c3129e7f363715777204b05dd47ae3 |

The 397-variable alternative retains the two original H square-root coordinates and equations. Apart from these, its coordinate and residual objects are identical to395. It has 367 residuals and 6,347 monomials. Its completeness uses the same new scalar preparation, while its soundness does not require the enlarged H-domain argument. It is also pending final composition acceptance.

## Exact chain and reproduction

The immutable main chain is 417 -> 401 -> 399 -> 396 -> 395. The alternate chain is 417 -> 401 -> 398 -> 397. Each step has a combinedCOUNT-certificate.json with exact predecessor, component source, component target and non-author review hashes. The 417 composition itself was independently accepted by agent01 in inputs/composition417-review.md, SHA f0242de339c9a659ecb447aeea6208da0c18cb7face4932b0595606524a3bf44.

Run verify_combination.py for 401,399,396,395 to replay every main-chain change and every coefficient without importing producers. The 398 and397 arguments replay the alternate branch. verify417_interfaces.py, verify399_interfaces.py and verify395_interfaces.py cover the physical input-label, scalar, H/V0 and normalization interfaces. REPORT399.md gives the full H-domain and scaled-chart argument; REPORT396.md adds the simultaneous scalar preparation and its compatibility. Both reports and their source files remain frozen.

## Last normalization and its domain

The final step is the independently reviewed component in inputs/normalized-pole438-ir.json, with review inputs/normalized-pole-review.md. Write x for stored scalar input coordinate526. The actual semantic input is b=-K*x for a fixed positive rational K. Outside the pole block, the unchanged scalar equations give r>0, c=r+4896>0, q=Norm(fH) nonzero, W=(B^2+r*q^2)/r^32>0 and b=crW^2>0. Therefore x is nonzero even when H is allowed outside 2E(K).

The exact substitution is old v_i=x*new v_i for i=51,52,53,54,532 and old v_i=x^2*new v_i for i=527,534. Set old v531=x^2 and remove531. All five pole equations become x^2 times their new equations. The private preparation-square equation becomes an identity. Division by x is justified entirely outside this pole block, and no private pole coordinate is divided by. Zero private witnesses remain permitted. The actual b and every outside coordinate stay fixed.

verify395_interfaces.py checks these five complete polynomial identities on the final composition, the full private-coordinate incidence and every unchanged row. It also checks the exact two-row/two-coordinate difference from the397 alternative. This verifies the specific final normalization, not just the abstract component argument.

## Final proof obligations

The complete mathematical review must retain the order established in REPORT399.md. Exclude fixed exceptional H points by the contact-height contradiction before interpreting logarithm ratios; use global nonvanishing of the actual rational approximation on K when the positive H component is unavailable; apply the torsion-killing integral group identities for both comparison and scalar transfers; and retain the exact squared-test values under the scaled biquadratic maps.

For completeness, REPORT396.md uses one simultaneous real and finite-place construction of H0 and the scalar point, then the same final shared H through the full CRT. It includes17 in the support and respects the order in which the correction support, continuity modulus, root scales and later primes are chosen. The enlarged H domain allows these original subgroup choices. The normalization then gives a rationally equivalent pole witness. It does not require choosing any new real or local data.

No release or manuscript edits were made. The 395 and397 candidates remain frozen for final review; later optimizations must use separate artifacts.
