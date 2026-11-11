# Accepted reciprocal primary charts without a new guard

The independently reviewed candidate has 427 total rational coordinates, 426 witnesses, 396 quadratic residuals and 6,288 quartic monomials. It saves eight coordinates from the frozen 435-variable source. Both this packet and the guarded 428-variable packet were accepted by the non-author reviewer in `05-anchor/review-identity-extension.md`, SHA256 `481788e54903f897e61882603576e13bfbf0af45f0a4947b5fb09bae100f8911`.

The source is `10-combination/combined435-ir.json`, SHA256 `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859`. The accepted output is `candidate427-ir.json`, SHA256 `6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4`. Its polynomial is `polynomial427.json`, SHA256 `256721badc6296a154da5d43fb9c1f67bfd2146bbb96b4b2d174113ffd9c2e84`.

The mathematical chart equations, exact coordinate maps and identity branches are those in the preserved `REPORT.md`, SHA256 `47b935a66d73ee6e691b8010488ab41f517dd0d2d6028c703f5db060e9672918`. That report described the guarded variant before review. This addendum records acceptance and the additional reason its V0 guard can be omitted. Neither earlier report nor candidate was changed.

The new primary charts include U_i=O and the difference charts include V_i=O, for i=1,...,4. Their outputs are the regular values f=z=ell=0 at O. This preserves the original rational input projection by the refreshed arithmetic soundness proof, together with the old finite-point completeness witnesses. It is not an equivalence of all intermediate witness spaces with the old affine charts.

## Why V0 remains nonidentity without the guard

This argument was proposed by bl5 in `00-independent470/IDENTITY_EXTENSION.md`, SHA256 `d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32`, and independently checked by05 against the actual manuscript and numeric interfaces.

If V0=O, the unchanged H/V0 equations give H=P. Its value f(H)=8(57+28*sqrt(2))/1681 is a unit at every place over every consumed prime p>76176: its numerator and inverse have denominators supported only at 2 and 41. At any prime in one of the three contact radicals, the unchanged zero-tolerant one-place forcing lemma requires positive valuation of the order-forty f(H) test. This is impossible. Hence all three contact radicals equal one.

Apply the unchanged root-scale height implication with N=1, before using any logarithm ratios. It gives B²-6<7*Hcal. The independent scalar anchor and retained margins give B>=(40*Hcal)^10 with Hcal>=1, a contradiction. The root heights, scales and scalar anchor are unchanged, and none of these steps requires division by the possibly zero V0 logarithm. Thus V0=O is impossible without circularly assuming the comparison ratios are already meaningful. Its actual logarithm denominator is then nonzero by the existing reciprocal norm and approximation-unit proofs.

The remaining local proof uses identities of unit power series, with value one at O, rather than the undefined quotient ell(O)/z(O). The zero numerator cases make the corresponding ratios and errors exactly zero. The revised argument therefore applies when U_i or V_i is O. The independent review checked all eight actual zero-numerator LP consumers and 217 unchanged protected rows as well as the source height and completeness uses.

## Reproduction and compatibility

Run `build_primary.py` and `verify_primary.py` for the complete guarded chart transformation and its exact source checks. Then run `build_unguarded.py` and `verify_unguarded.py` for this variant. The latter verifies that427 is literally428 with only the global guard coordinate702 and row705 omitted, and independently expands the full primitive sum of squares. The non-author checker is `05-anchor/review_identity_extension_check.py`, with its saved checks beside it. All finite checks passed; the degree remains four and the content one.

Only the four primary charts UA,US,UT,UZ and their V1,...,V4 structural rows change. Root chart values, their odd augmentations, all height and scalar circuits, H, V0 and all retained downstream f/z values keep their meanings. This is disjoint from the separate H.j elimination and from the scalar f1 inverse change, subject to checking the actual source when composing. A new combined artifact still needs its own exact transport checks; the count427 applies to the pinned435 source only.
