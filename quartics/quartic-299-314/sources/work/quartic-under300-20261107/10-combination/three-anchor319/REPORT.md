# Three-group detector and abscissa anchor: 319 variables

Author: `/root/astra_quartic_opt10_combination`. Both component inputs have independent reviews. This composition is provisional until a non-author reviews the interfaces below. It has319 total variables,318 witnesses,289 quadratic residuals and5676 quartic monomials. Degree four, content one, maximum coefficient16*3^(2^26). No released file was changed.

## Frozen inputs

Paths below start at `work/`.

* Common366: `quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json`, SHA0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56.
* Detector326: `quartic-optimization-20261107/resume-depth-20261107/three326/candidate326-ir.json`, SHA48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84. Report SHA766427b1e75cf10823b0119b9d3a415a8460b49cbebb31c1b2b8483502f3baf8. Independent review `quartic-optimization-20261107/resume-sol-review326-20261107/REVIEW.md`, SHA9bc208d22884b33a2777446ddd826017db173aa30b50830f944bbd941a08482c.
* Anchor359: `quartic-optimization-20261107/resume-elimination-20261107/abscissa359/candidate359-ir.json`, SHA282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1. Independent review `quartic-optimization-20261107/resume-review359-20261107/REVIEW.md`, SHA6956155cc4878f0c36f5e1159330f043d473cc8fd4ba421f2ec484dc4083655c.

## Residual-label collision and exact transport

The raw components both use residual IDs903 and904. In326 those are two shared H-square definitions; in359 those define Q and B. Blind union would lose equations. The constructor first relabels only the anchor residual903 to1903 and904 to1904. Their names, kinds, blocks and terms remain identical. Coordinate IDs903 and904 are NOT relabeled; they still mean Q and B. The new residual labels are absent from both inputs.

After this explicit injective relabeling, all changed coordinate and residual objects relative to366 are disjoint. The checker supplies each final object from exactly one pinned input, checks ID uniqueness and all metadata, and checks every deleted coordinate has no final consumer. Both detector rows903/904 and both anchor rows1903/1904 survive. The certificate records the map separately from coordinate changes.

## Whole arithmetic interface

Anchor359 uses only the retained root square-abscissa charts, the unchanged scalar point/g0 inverse, and its private quaternion rows. Its parity argument therefore precedes the detector's pre-H height contradiction. It forces the three root indices odd and restores the old scalar anchor. The required half-chart sign choices are precisely the A,T,Z actions in the359 review. Our checker applies each action to every final residual, including all new three-group shared squares, sums and products. Each residual is invariant or changes by an overall sign. Actual root points, all abscissae, Q, B and the detector outputs remain fixed.

Consequently326 may use the restored root domain and anchor when excluding its pre-H exceptional branches. The326 review establishes the generic squared-H valuation class without first using a later index interpretation, and the exceptional branches have unit T0. Its three group inequalities then supply all high/middle/primary/alternate tests at one common place. All scalar, logarithm and input-bridge equations retain their pinned meanings. This composition does not infer a global trace inverse at a radical-free detector.

For completeness, use the independently reviewed326 construction with the original Pi^19 progression. It supplies primary formal depth20 and reciprocal depth40, including the stronger U2 term. The G2 ratio retains precision12, while the other rational-log ratios have precision40; these give the actual positive margins recorded in326. The newly used E-weighted terms require only enlarging the freely chosen preparatory small-prime divisibility before selecting contact primes. The reviewed326 construction already does so.

After all those choices, apply359's forward construction of its private Q, B and quaternion witnesses to the same roots and scalar point. Q depends only on already fixed root abscissae, and the new private representation requires only the already satisfied integrality at2 and3. It imposes no new congruence on h, no real condition, and no new contact-prime restriction. All nonprivate326 values stay fixed. Thus its Pi^19 choice order survives unchanged. No Pi^39 requirement from the superseded327 presentation is imported.

## Checks and scope

`build.py` produces the exact composition; `verify.py` imports no producer and checks source pins, injective residual relabeling, all object suppliers, full active-coordinate/consumer coverage, all three sign actions, and every coefficient of the primitive-residual sum of squares. All checks pass. C-dependent terms remain those of359: maximum16C^2, no ordinary-monomial collision between different C powers, constant coefficients below2048 bits.

This is not the separate exact-anchor319 candidate authored by01. They share only a variable count. No ordinary coefficient companion is asserted. No publication is authorized; the next threshold remains fewer than300 total variables.

candidate319-ir.json: `61898500a23024afbf21aed5a35ee0b573beef0dcaa598caba07de884c4281f4`.

polynomial319.json: `2ea15f952e6e38d2aa49aa1ef849b854696dc99f8af8dcfa23d686b4ebd3af37`.

build.py: `4726676c32b9674899ec5010a4667ddae966b9db984f4832b39b5f3062698c98`.

verify.py: `e95ee8987f0e2a772704b5a6a0af25435ec336f089666c2ee7a19de347795c8c`.

CERTIFICATE.json: `ea191eb479e51da315429641a3d69cce586e64c89e975f95fa2d1643c397037a`.

VERIFICATION.json: `c6c3030effd5ffc150d18d0b6da10adfed5a936f7d0dec789135cca0f4fdeb8e`.
