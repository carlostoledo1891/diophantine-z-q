# Independent full-composition review: 453 variables

Reviewer: `/root/astra_bl5_models`. Decision: accepted for the exact research candidate below, under the unchanged inherited arithmetic qualifications. No manuscript or publication approval is given; 453 is above the requested release threshold.

## Artifacts and review boundary

- Reviewed 470 source: `eff9369864da6bd2ed46fa300f51f5a0cc9217d3b790380713644ee31f512b72`.
- Intermediate `combined461-ir.json`: `73d16931a8e6fb9c50927b2d059899eb77157ef76ab6d9e38fb6536a5601c99a`.
- Final `rational453-ir.json`: `f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f`.
- Final polynomial: `b297f9ee23af09293433620cdcd77959e464c1e5125754d610f97eacd50ea422`.
- 461 transport certificate: `f638a1952ac37b7028d36a54dc9069feb6b2db549e7ddd62ad3bbef3877362f5`.
- Rational-log certificate: `d0243417626465651a2e54ef3e482cf4e1e8e35b3f5157bbe5a8dbfa6ec8ada1`.
- Corrected author report `REPORT453.md`: `b725de7010dd9c10c0dac846aefb16b50db4e48e4586a9021c93de6673d2b87b`.

The preceding 498-to-470 review is `REVIEW.md` in this directory. For the new changes I read the actual V0, tangent and rational-log arguments, their separate non-author reviews, the relevant checker implementations, and the final transport and physical-consumer checks. I reran six checks through `replay453.py`, with all source writes suppressed. The output is saved as `453-replay.log` and `453-replay-result.json`. The existing independent checkers are not presented as newly authored by me.

The author corrected one wording issue I reported: an abscissa difference with zero rational component in `Q(sqrt(2))` is not purely imaginary. No candidate equation changed for that correction.

## Reciprocal V0 and its two exceptional cases

Use `D=(3-sqrt(2))^2`, `a=-1+7sqrt(2)/4`, `b=39/8-9sqrt(2)/2`, `c=a^2`, and the retained H coordinates `x=h^2`, `j^2=h^4-D`. Define

`d=c*x+D`, `N=a*j-b*h`, `d*g=N`, `T=-2D*h-a*b*j+2D*b*g`, `k=T/(a*d)`.

Both real embeddings make `d=(a*h)^2+D` positive. Thus division by `a*d` is legitimate. The exact identities give `k^2+D*g^4=1` and identify `(1/g^2,k/g^3)` with `H-P` on the unequal-abscissa locus. The checker verifies the ordinate sign as well as the abscissa. Direct calculations at all four choices `h=±a,j=±b` show that the two H=P cases have g=0, while the two H=-P cases give the actual point -2P, including `z=-g/k`.

The zero branches must be handled in the composed system, not by invoking the removed inverse. If g=0, then N=0 and k^2=1, so T is nonzero. The final logarithm equation forces ell0=0. But the actual retained equation is

`ell0*LP1 = z(V1)*G2(D*f(V1)^2)`.

As checked below, the completed V1 chart still gives a nonidentity doubled point. Its z is nonzero and its w lies in (0,1) in both real embeddings. On that interval `G2(w)=1-2w/5-2w^2/15 >= 7/15`. The displayed equation contradicts ell0=0; no assumption on LP1 is needed. This proof is independent of the rational approximation R0 and therefore introduces no circular use of V0's identification.

Also k cannot be zero: `D*g^4=1` would imply `(3-sqrt(2))*g^2=1` by positivity in the real embeddings, and norms would give `7*Norm(g)^2=1`, impossible in Q. Thus every final solution has the actual finite nonidentity V0=H-P, with f=g^2 and z=-g/k.

## Four completed comparison charts

Only V1 through V4 receive the tangent equations. The subset checker verifies that this is exactly the four-block restriction of the separately reviewed five-chart proposal; V0 does not simultaneously retain that alternative chart.

For incoming points with coordinates `(x1,y1),(x2,y2)`, write `d=x1-x2`, `q=m^2`, `xR=q-x1-x2`, `yR=m*(x1-xR)-y1`. The retained slope relation and added equation are

`m*d=y1+y2`,

`q*(x1+x2-2*xR)-2*m*yR=x1^2+x1*x2+x2^2-D`.

The exact identity reducing the added equation to the curve and slope equations holds when d is nonzero. When d=0, the slope equation forces y2=-y1, and the added equation becomes the actual tangent relation `2*m*y1=3*x1^2-D`. The retained point-domain lemma gives y1 nonzero. Thus the equal-abscissa branch represents doubling of the first point, not an arbitrary slope. The identity difference is excluded by the same nonzero-y fact. In either case the output is the actual nonidentity difference in 2E(K), so its x,y,z are nonzero and its abscissa is a square in K.

This supplies precisely the V1 property used to exclude g=0 above, even after its half-trace inverse has been removed. The integer indices are unchanged: V0 has index h-1 and Vi has index ui-ni. No proof here divides by h+1 or ui+ni. The new opposite-point cases therefore remain within the original local ratio argument.

## Rational logarithms, global and local domains

The four changed blocks are exactly indices 0,2,3,4. The polynomial numerator N8 and quadratic denominator Q2 satisfy the displayed exact identity

`Q2*G9-N8=(2970726/254443709)*w^10-(41697666/6361092725)*w^11`.

The independent rational checker reconstructs these coefficients by convolution, verifies the zero coefficients at degrees 7 and 9, and checks all Bernstein coefficients of N8. On [0,1], Q2 is decreasing and at least 60/1073; the positive Bernstein coefficients give N8 at least 83904/10113025. All actual Vi are nonidentity doubled points by the two chart arguments above. Their square positive abscissas and nonzero ordinates give `0<D/x(Vi)^2<1` in both real embeddings. Hence both polynomials and R=N8/Q2 are nonzero on the complete admitted K-point domain. This is not a claim about arbitrary complex elliptic points.

At the consumed unramified places over p>76176, coefficient denominators have no prime factor above 37. If r=v(z)>=1, then v(w)=4r; Q2 and N8 are units, and the exact identity gives v(R-G9)>=40r. Combined with the retained full-tail estimate, v(log_E(V)-zR)>=41r. Thus zR has the logarithm's valuation and relative precision at least 40 at split and inert places alike.

For LP2,LP3,LP4, both numerator and denominator have precision 40. LP1 keeps its G2 numerator of precision 12 and receives a denominator of precision 40, so its relative precision remains 12. The order10 tests in the current source therefore still have enough precision. As before, integrality of the full ratios is transferred before relative congruences are treated as absolute congruences. The primary depth and order80 estimate, the order40 label tests, and the order10 height contradiction are unchanged.

## Actual final consumers and composition order

The final physical equations, checked in both rational components, are

`T*ell0+a*N*R0=0`,

`ell0*LP1=z(V1)*G2(w1)`,

`ell0*LPi=z(Vi)*Ri` for i=2,3,4.

They use the literal new R outputs. There is no reliance on a historical semantic entry for a separately eliminated ell_i. The checker also compares every retained outside row after the fixed affine recentering of the old polynomial slots. Reused cube slots are now fourth powers; no unintended consumer remains. The six square rows used by the 470 triple eliminations—132/133,144/145,150/151—are unchanged as actual polynomials. Hence the earlier detector equivalence remains valid with the new point and logarithm values.

The chart changes alone extend each old complete witness while preserving its actual point outputs, and their soundness uses the enlarged-domain arguments above. The rational-log change instead requires recomputing comparison values and detector/pole witnesses. For completeness, choose the same kind of prepared points and scalar data, then the scales and continuity neighborhoods for the new nonzero rational functions, then the contact primes and shared-index CRT. The new local precision supplies the unchanged tests. The existing real pole construction still yields positive semantic pole inputs, as required for the factored-pole completeness step. Nothing requires an old G9 value to equal R, or an arbitrary old pole tuple to be retained. No additional arithmetic hypothesis or rational lifting premise is introduced.

In the reverse direction, the final equations give actual points, legitimate R values and the required approximate ratios, so the inherited arithmetic soundness proof applies. These are equalities of the rational input projections, not a claimed bijection between all old and new witness spaces.

## Counts and verdict

The exact transport and full primitive-row sum-of-squares replay give 453 total coordinates, 452 witnesses, 430 quadratic residuals and a degree-four polynomial with 6,584 monomials. The fixed parameter remains C=3^(2^25). The x_1^4 coefficient is exactly 1 with no C term, while the unique C^2 contribution is `16*C^2*x_57^2` with no lower-C contribution on that monomial. The verified ordinary and linear-C coefficient bounds establish content 1 and maximum absolute coefficient `16*3^(2^26)` after specialization.

No unresolved defect was found in this exact composition. Acceptance is confined to the candidate and hashes above and the unchanged inherited arithmetic dependencies. It does not approve a future optimization or release.
