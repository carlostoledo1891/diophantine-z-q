# Scalar depth 24 composed at 431 variables

The frozen candidate `combined431-ir.json` has SHA256 `180968baa12a26f0171eeeb337df61b293a3a122786929e28b9fc94c55ba5573`. Its polynomial SHA256 is `3f9ec023f0c850d0ef39b16f0832f49ce55dc4e5d009bcbd77fa69e1b72c5f50`. It has431 total variables,430 witnesses,408 quadratic residuals and6,456 quartic monomials. Content is one and the maximum coefficient remains16*3^(2^26).

The source432 composition is independently accepted in `inputs/composition432-review.md`. The new component is the accepted scalar-depth24 change copied to `inputs/scalar24-448-ir.json`, with non-author review `inputs/scalar24-review.md`. It removes the r^64 coordinate and changes the scalar expressions to

    B=(rho0^2+r*rho1^2)/r^32,
    W=(B^2+r*q^2)/r^32,
    q=Norm(f(H)).

The old B-square slot now stores q squared. All other scalar ratio, point and pole-input coordinates retain their meanings. This change gives scalar-index divisibility of order24. The independently reviewed exact anchor inequality proves that the unchanged height and order-ten contradiction still follow. This is a new arithmetic use and is not presented as an old-witness bijection.

The required hypotheses from the preceding composition are intact: the shifted beta gives r>0, its odd consumed contact valuations are positive, the small-prime correction is a unit at those contacts, the actual ratio coefficients are rho0 and rho1, and f(H) is a nonzero field element. The reviewed preparation supplies arbitrary finite coefficient depths, so it makes the new W integral on the support of cr. The new positive pole input c*r*W^2 therefore has the required square denominator and local squareclasses. Fresh pole witnesses are allowed.

`combine_depth431.py` records the exact component sequence from accepted435. `verify_combination.py 431` independently checks every source delta, renamed or removed coordinate, unchanged consumer and final coefficient. It passed. Agent01 is performing the final independent physical-interface and composition audit. The simpler432 interface replay is retained separately; it is not claimed to verify the changed431 formulas.

The new input-label/correction proposals and the primary charts admitting identity points are not included. No below400 publication milestone has been reached, and the published files remain unchanged.
