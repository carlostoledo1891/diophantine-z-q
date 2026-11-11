# Reviewed H-coordinate and scalar-root changes at 432 variables

The frozen candidate `combined432-ir.json` has SHA256 `92418e21d6903cf5a80def3848c3c3da603ec03673c207cf7c40a1a2dec105a2`. It has432 total variables,431 witnesses,409 quadratic residuals and6,496 quartic monomials. Its polynomial SHA256 is `e622e2fb7574f18319b84595d230509f843a5789e14ebaeb26722d1f7101ac19`. Content is one and the maximum coefficient remains16*3^(2^26).

The independently accepted435 source first receives the independently accepted H.j elimination. This produces433, SHA256 `207218ebbcd15fa97f69580fce71629a50e34129549e80a9568dbed57ae28832`. The H change is described in `REPORT437.md`; its non-author mathematical review is copied to `inputs/primary437-review.md`. Parent acceptance of the actual433 composition is copied to `inputs/composition433-review.md`. It preserves every point and logarithm value through the exact maps j=hs and oldg=hv.

The additional one-coordinate scalar-root change is the reviewed450-to449 component copied to `inputs/scalar-root449-ir.json`. Its non-author review is `inputs/scalar-root-review.md`. It replaces the root by

    W=B^2+q^2/r,
    q=Norm(f(H)),
    B=(rho0^2+r*rho1^2)/r^64.

The label remains beta=2X^2+2403, so r is strictly positive. The new W is strictly positive. The reviewed valuation proof still obtains the required order32 scalar divisibility; the reviewed completeness proof requires integrality of W at the prepared primes, rather than the old unit assertion. It supplies fresh pole witnesses for the new positive input c*r*W^2. This is an arithmetic replacement of W, not a bijection preserving the old pole input.

The H change preserves f(H), and the earlier scalar fusion preserves rho=z(R)/z(H). Therefore the scalar-root component receives exactly the same semantic q and ratio coefficients in the composed system. `verify432_interfaces.py` replays the separately authored05 checker on the actual433-to432 files. It independently eliminates the contact intermediates to the precise five-factor r at the shifted beta, checks q squared through the retained test-square slots, checks all powers through r^64 and the actual B denominator, and checks the new root and every downstream corrected-r, W-square and pole-input row. It verifies the negative normalization of stored pole coordinate526 as well.

`combine_root432.py` applies both component deltas from435 with exact source-row and coordinate-semantic checks. `verify_combination.py 432` reconstructs the complete result independently and expands every coefficient. Both that check and the physical-interface replay passed. The authoritative accepted baseline is433; final review of the432 composition is pending. The separate depth24 proposal is not included.

The below400 publication threshold has not been reached. All prior candidate files and all published files remain unchanged.
