# Original multiplication connections

Author: /root. Pending independent review.

The three records cover current manuscript lines1886–2030. They do not replace the original template implementation, generator theorem, pole-soundness lemma, or six-contact height theorem. Those are explicit incoming dependencies. No original frozen source or assertion is changed.

## Direct checks

For the displayed equation, eliminating x from z=-x/y gives the integral invariant differential dz/sqrt(1+4d²z⁴). The binomial expansion and termwise formal integration give the coefficients in lines1907–1909. The seven fixed coefficients of16575 times the degree25 truncation are recomputed in CHECKS.json. For omitted exponent r>=29 and p>324, r-1-v_p(r)>=28. For r<p this is immediate; for r>=p, v_p(r)<=r-p+1 gives r-1-v_p(r)>=p-2>=323. The integral coefficients and v(z)>=1 therefore give the claimed relative error. The logarithm isometry used here is the separately retained formal-group theorem.

In the passing group, full-log ratios equal the rational index quotients. This follows without applying log to P0 itself: [h]U_i=[z_i]H gives h log(U_i)=z_i log(H), and H is nonidentity by its denominator guard. The analogous identity holds for the primed points and their conjugates. Thus whichever of h and h-c* is a p-unit supplies integrality. The difference test transfers it to the other truncated ratio; its unit relative-error factor transfers it to the other full-log ratio. Only then are the modulo p^28 errors absolute. Subtracting the two modulo p^25 index congruences gives c*(n_i-A_i)=0 mod p^25; c* is a unit by the separately retained support condition.

For the trace contradiction, alpha and delta are odd, each factor has valuation min(0,alpha+2v(C)), and a failed threshold gives <=alpha-2delta. If all groups fail at both places, the trace sum has valuation>=2delta-alpha. Since Theta is rational and nonzero, alpha-2v_p(Theta) is odd and <=-delta. Pole soundness rules this out. The argument requires a common passing group/place, not that all its factors are units.

For the box bound, each product of odd contact primes has its25th power dividing the nonzero integer f. Apply the height theorem to each of27 slopes. The sum/quotient and K0 coordinate-height bounds, followed by the generator and duplication inequalities, give N²<24 A_ht N^(48/25)+10. For N>=5, absorb10<N²/2, obtaining N^(2/25)<48 A_ht and hence N<(48 A_ht)^(25/2)<=(48 A_ht)^13. The N<=4 case and identity code convention remain explicit.

The exact correspondence between the literal S03 recipe and these displayed constraints is a separate compiler/template obligation. These mathematical records cannot certify that correspondence by themselves.
