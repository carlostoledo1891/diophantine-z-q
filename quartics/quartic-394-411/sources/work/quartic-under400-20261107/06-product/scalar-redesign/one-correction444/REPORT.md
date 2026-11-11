# Implementation of the one-correction label

This packet implements root's frozen arithmetic proposal `00-root/one-correction/PROPOSAL.md`, SHA256 `495ffb791c149bb6b2ee6fa1f4988aa8583fea383efd0e4197436fe6bab2b9a6`. Root authored that proposal; agent06 authored this implementation. Non-author arithmetic and implementation review is assigned to agent03.

The source is the independently reviewed depth24-448 candidate, SHA256 `e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609`. The output has444 total variables,443 witnesses,421 quadratic residuals and6,668 quartic monomials. Its degree is four, content one and maximum coefficient16*3^(2^26), with unchanged fixed C=3^(2^25).

Candidate SHA256: `c2c60a1bed5c929eb633b654e76d401dc96fc0edd1f09eee44324740c4cde837`.
Polynomial SHA256: `aaa5dfeec88403654211b4c1b5fb9284dc1d87908fc6987d4864ea015b1951f2`.

## Literal implementation

Keep the input coordinate X=0, square coordinate Y=248, and the literal equation Y=X^2. In every other residual substitute

    Y -> 102Y+102X+76.

The source expression beta=2Y+2403 becomes204X^2+204X+2555=51(2X+1)^2+2504. All fourteen affected residuals and their original IDs, original terms and new terms are recorded in `CONSUMERS.json`. The transformation includes the two direct beta-test rows, all grouped order-ten beta consumers, all definitions of the contact product, and every later direct use of its affine expression. The input-square equation is explicitly exempted. No other residual changes except the correction block.

Delete correction coordinates61,62,63,64. Retain final correction coordinate65 and impose just

    v65^2-33066*v65+1090089=0,

which is exactly (v65-33)(v65-33033)=0. The final correction still has its unscaled semantic meaning c. Its corrected-product row and pole-input row are preserved after the input substitution. No rescaled-correction optimization is included in this packet.

## Arithmetic binding

The frozen proposal proves r>0 for all rational X, squareclass sufficiency of these two corrections at2,3,17, and that the same depth24 scalar and order-ten height arguments apply. Its even negative-valuation assertion is explicitly restricted to consumed primes p>76176, where51 is a unit. The special primes3 and17 are handled by the exact local calculations, not by that assertion.

The final input implication now uses the retained odd integer label n. From n=beta, the squarefree factor51 forces t=2X+1 to be an integer, and odd n forces odd t, hence integral X. The four actual A odd-chart residuals are unchanged; the checker verifies this separately. This binding is essential: beta integral by itself would not justify the final implication without oddness.

For completeness the frozen proposal chooses one of33 and33033 before the scalar support, prepared indices, continuity modulus and contact primes. Thus the output feeds exactly the same positive scalar pole interface. No assertion is made that old448 witness assignments keep their values after the input-label change.

## Verification

`build.py` produces the candidate. `verify.py` imports no producer and independently reconstructs the affine substitution by a multinomial formula. It checks the deleted-coordinate incidence, every changed and unchanged row, the untouched input equation and A odd-chart rows, the local arithmetic formulas on a complete relevant residue cross-check, and every final coefficient of the primitive integer sum of squares. The local cross-check supports the formulas in the frozen proof; it is not substituted for that proof.

All checks passed. The packet is frozen for the assigned non-author review and makes no publication claim. No older packet or manuscript is changed.
