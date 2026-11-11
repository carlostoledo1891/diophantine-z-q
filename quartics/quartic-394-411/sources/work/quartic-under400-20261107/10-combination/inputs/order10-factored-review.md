# Independent review of order ten and four factored poles

I accept the order-ten detector change and all four pole factorizations, including the scalar pole, in the exact 491-variable composition identified below. This is an independent internal model review of these transformations and their interaction. It is not a fresh verification of the inherited global arithmetic theorem or an approval of a later composition with additional changes.

The exact inputs are the frozen 498-variable source and the 495/491 artifacts from `10-combination`. `REVIEW-order10-poles-checks.json` records every input hash. In particular:

- Source498: `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.
- Order10-495: `7977c821c1b21d934a4ce1ea107d93e6fda7af729afaf8b43670b2cf8959de66`.
- Combined491: `ad387a34c8fdba8d6ac4463356c46ae9ae8f178ddf9523cde0593e15454be20f`.
- Combined polynomial: `6f02c4dd5b647bcf0d887a1fada7e076a90922cd073da0e75a3dbabee284c57a`.

I read the actual lower-precision proof, the current Version 12 local-comparison, scalar, soundness and completeness arguments, the earlier detector and scalar factorization proofs, and the actual transported equations. I wrote `review_order10_poles.py` independently of the producer. It imports no producer or verifier helper. Its complete row reconstructions and full sum-of-squares comparison passed: 491 variables, 460 quadratic residuals, and 24,641 monomials.

## Order-ten arithmetic

Only the tests L1-L1' and L1-beta are weakened from order12 to order10. Their functions remain the same. In particular the alternate numerator is still ell12=z*G2 and the common alternate denominator remains ell40=z*G9. All primary logarithms remain z. The three other cross tests and the Lucas residual remain order40.

At a consumed unramified place over p>76176, the retained formal-membership tests and f(H) order40 give H depth at least20. Before inferring improved depth for U1, the logarithm/truncation unit factors preserve the valuations of the exact ratios u1/h and (u1-n)/(h-1). One of h,h-1 is a p-unit. A cross congruence of any positive order, including10, transfers integrality to both approximate ratios. Only then does L1 integral imply U1 depth at least20. The primary error has order80 and the alternate G2/G9 error has order12. The order10 cross test therefore gives L1 congruent to n modulo p^10. The beta test gives the same order for n-beta. This argument covers split and inert places with the original valuation normalization. It adds no logarithm denominator and does not strengthen an unproved approximation statement.

The order40 Lucas contradiction is unchanged. It gives F=0 and log B>|a|-3. If N is the nonzero reduced numerator of n-beta, the inherited product-height estimate gives

```
B^2-6 < 7 H |N|^(19/10),
|N| <= 2 exp(h(beta)) B.
```

For B>4, B^2-6>(5/8)B^2, and 2^(19/10)<4. Hence

```
B^(1/10) < 48 H exp((19/10) h(beta)),
log B < 10 log(48H) + 19 h(beta).
```

The exact old anchor gives c=|a-1|>(80H)^10 and h(beta)<|a|/40. It also gives log(48H)<|a|/40: set y=80H>=80, use log(48H)<y, c/80>y^10/80>y, and c/80<=|a|/40. Therefore log B<(29/40)|a|. Since the same anchor gives |a|>11, this is smaller than |a|-3, a contradiction. Thus the changed order still forces n=beta and the input remains integral.

For completeness, the same preparation and primary/opposite CRT construction provides order12 approximation, hence order10. The detector weights and pole values are recomputed for order10; one does not claim that an arbitrary old order12 pole witness remains valid. The inherited pole-realization estimates apply to fixed positive order10: the real error remains O(lambda^-3), and the small-prime bound has coefficient 10m-8=92>0. The same choice order, finite continuity conditions, prime exclusions, and sufficiently large real parameter work simultaneously. No new prime theorem or unpublished arithmetic hypothesis is used.

## Exact order-ten weight circuit and its domains

For one detector write E=eWeight, q=q1, Q=q^5, and R=q10^2. The retained power rows define Q and R. The new six equations are

```
E a = q,
E b = a^2,
q c = b^2,
c d = Q,
c q10 = d^2,
c q40 = R^2.
```

The unchanged norm/trace guards prove E is nonzero. If E were zero, its eDelta row would force eDelta=0, the B row would force the norm quotient n=0, and the norm equation would give w0^2=2w1^2. Rationality would force w0=w1=0, contradicting the retained inverse of w0. The unchanged q-definition specialized at q=0 gives E=0, so q is also nonzero.

The equations determine a=q/E, b=q^2/E^3, c=q^3/E^6, d=q^2*E^6, q10=q*E^18, and q40=q*E^78. In particular c is nonzero before either last division. These are exactly the required order10 and order40 weights. The order10 coordinate is consumed by the former order12 degree-two evaluation, with its coefficients and test functions unchanged. The retained R equation reads its new square; it is not assumed independently. My checker reconstructs all six equations, checks the actual nonzero guards, verifies their Laurent exponents, and compares every other row after the explicit E12-to-E10 name change.

## Four pole factorizations

For each normalized detector the old private rows are

```
17E-Eb-17F=0,
t2=t^2,
q2=q^2,
17b q2+867F^2-34F t2-t2^2=0.
```

The new coordinates satisfy F=t*v, q=t*Q, q2=t^2*Q2, and t2=t^2. The Bh row becomes 17E-Eb-17t*v=0. The two remaining rows are Q2=Q^2 and

```
17b Q2+867v^2-34t*v-t^2=0.
```

This reconstructs every old rational solution row from every new solution, including t=0: the old square and conic rows are t^2 times the new rows. This soundness direction does not assume positivity or divide by t.

For completeness take the source's positive detector inputs. If t is nonzero, divide F and q by t and q2 by t^2. If t=0, the old equation is 17b*q^2+867F^2=0; since b>0, it forces F=q=0. Choosing v=Q=Q2=0 gives a valid lift. All three blocks have private coordinates, so their lifts do not interact.

The scalar factorization has the same polynomial reconstruction, but a different literal sign and scale. The frozen source's actual values are

```
B_semantic = -K*b_stored,
H_semantic = -17K*f_stored,
```

where K is the positive integer recorded exactly in the check JSON. These equalities were checked against the pinned semantic values of the mixed-depth source, not inferred from variable names. At t=0 the actual scalar second-conic row is

```
17K*b_stored*q^2 - 867K^2*f_stored^2
 = -17*B_semantic*q^2 - 3*H_semantic^2.
```

The scalar completeness construction has B_semantic=c*r*W^2>0: c*r is chosen positive and the new scalar norm root W is a nonzero unit at the prescribed places. Thus this zero-branch equation also forces q=f_stored=0. Choose the new scalar factor witnesses zero. This is valid even though the stored b coordinate is negative, not positive. The Bh row, preparation equations and first conic are all preserved by the polynomial reconstruction. My checker applies the simultaneous reconstruction to every row of the complete 491-variable system, so no outside consumer is omitted.

## Simultaneous completeness and review scope

Version 12's scalar preparation proves positivity of the actual scalar input before constructing scalar pole witnesses. Its large-real-parameter argument gives positive detector inputs after the roots, scales and continuity modulus have been fixed. The order10 modification retains these conclusions by the same estimates. Apply the four factorizations only after choosing those positive-input pole witnesses. Consequently all zero-branch lifts work in the same complete witness set. No incompatible set of prime choices or moduli is combined.

The relevant inherited consumers are `lem:v12-mixed-local`, `lem:v12-scalar-sound`, `subsec:v12-soundness`, and `subsec:v12-completeness` in the published Version 12 addition. The original detector positivity estimate is also stated in Version 11 around the expansion B_r~1/(4*A_r^6*lambda). The new transformations do not change the curve, coefficient basis, normalization, root labels, scalar anchor, or global arithmetic assumptions. Their dependence on those inherited results remains explicit.

This accepts the exact order10 and four-pole transformations in the pinned491 composition. A later composition with the scalar forward-power rewrite, the guarded preparation conic, or hybrid grouped products needs its own interface and coefficient checks. No release, manuscript edit, or below-400 claim is made here.
