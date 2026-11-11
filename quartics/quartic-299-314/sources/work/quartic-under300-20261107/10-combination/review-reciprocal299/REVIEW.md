# Independent review of reciprocal299-r2

I accept the corrected, frozen299-variable construction below, under the independently accepted source arithmetic inputs. This review covers the literal S conversion, its orientation and scalar coupling, the joint four-auxiliary soundness argument, completeness, the complete variable inventory and the entire polynomial. The earlier miswired candidate remains rejected.

Reviewer: `/root/astra_quartic_opt10_combination`. Agent01 authored the new compiler and the preceding301 elimination; the root agent proposed the S extension. I contributed parts of the earlier307 algebra and independently reviewed agent05's auxiliary-domain proof. Those earlier contributions remain inherited dependencies. I did not author the new301 elimination or the new S-oriented299 application reviewed here. This acceptance does not claim a rational bijection between all299 and301 witnesses.

## Exact objects and correction history

All paths below are relative to `work`.

| Object | SHA256 |
|---|---|
| `quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json` | `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815` |
| Same directory, `polynomial299.json` | `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c` |
| Same directory, `REPORT.md` | `ae5d127cb34de3b0f318f6faff3736738748286279012d3db3f9b46151b95b8b` |
| Source `reciprocal301/candidate301-ir.json` | `ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6` |
| `quartic-under300-20261107/10-combination/review-reciprocal301/REVIEW.md` | `ab035cfec699f36adddff3792a0de89a30c6719e59deef3f4361198bac2bd6aa` |
| `quartic-optimization-20261107/root-ordinate299/PROOF.md` | `69ddd3063b571c19a481272a31268ce093411c0c5519d62aef65878d52a4a7d0` |
| `quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md` | `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750` |
| Its earlier conditional review, `quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md` | `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b` |

I read the actual frozen author report and root proof note, together with the earlier domain argument and the successful-place/H-bootstrap passages it consumes. The original candidate `ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd` incorrectly used undeclared202/203 for the alternate cache. Agent03 and the author checker detected that error; I independently confirmed it against source rows148/149. The correct cache is196+2*rho*197. The corrected bytes above pass. My checker also deliberately substitutes the wrong slots and confirms that the active inventory detects202/203. This is a resolved implementation error, not a change of the mathematical argument or an acceptance of the earlier bytes.

## Physical equations and orientation

The checker independently reconstructs all old S biquadratic, cache and ratio equations from their coefficients. It then reconstructs every new field equation using rho^2=2 and D=11-6*rho. The actual retained root is

    a=x5+rho*x6, b=x7+rho*x8, c=x84+2*rho*x85.

Both a^2=c and b^2=c^2-D remain literal source rows. The new private pairs are f at25, h at27, F at118 and s at120. The actual caches are Y=x257+2*rho*x258 and B=x196+2*rho*x197. L at236, z at168 and the affine H normalizer N are unchanged. The new rows assert Y=f^2, B=F^2, the primary curve, the reduced divided difference, the root abscissa, both primary ratio equations and the regular alternate equation.

In particular the new orientation is exactly

    a*b = D*h-s*(D*f+c).

It is quadratic, uses the same b that the scalar subsystem consumes, and removes the otherwise uncontrolled sign of the recovered root ordinate. No S root coordinate is deleted. All scalar, H/V0, anchor, common-scale, logarithm and detector rows remain identical to301. The checker verifies the full S sign action: negating5,6,7,8,543,544,549 fixes every new equation; only the old scalar rows474,475,513,514 change by an overall minus sign. This preserves the inherited sign-restoration freedom without changing the scalar point.

Define k=s*(f-F)-h. The independently expanded301 identities recover the alternate curve and both full slope equations from the retained caches, primary curve and new reduced equation, without division. They are valid for S as well as A/T/Z. The accepted reciprocal closure therefore supplies genuine points U,V with U-V=(c,D*h-s*(D*f+c)). The orientation row identifies this with the retained scalar root S=(c,a*b).

The closure includes f=F,k=-h: its divided difference forces the genuine tangent and excludes h=0 there. If U=O it gives F*c=1 and U-V=-V; if V=O it gives f*c=1 and U-V=U. Both identities are impossible simultaneously. The retained product/height inverse excludes c=0 before a root division is needed. These are actual closure cases, not assumptions of generic distinct abscissae.

## Joint soundness before the raw ratios

The S conversion admits auxiliary points in E(K) that need not lie in2E(K). Accordingly I reapply the previously reviewed all-four auxiliary-domain argument to the literal new interfaces. I do not first invoke the301 theorem with an unstated old S square-root lift.

First reconstruct all four alternate ordinates and point curves polynomially. This yields all four oriented differences; S agrees with its retained scalar root, and the other roots recover their old ordinate charts. Root nonvanishing, parity and height conditions can then be used before auxiliary logarithms. Their physical inputs and the scalar anchor are unchanged. The all-empty-contact-radical branch is excluded by the same root-height/anchor contradiction.

At a required contact, a raw reciprocal curve h^2=f(1-D*f^2) gives even valuation of every nonzero f: positive valuation comes from h^2 with a unit factor, negative valuation from the leading cubic term, and valuation zero is immediate. Zero f is the identity. This applies to S as well as the other three pairs and to the conjugated alternate place. The exact cached powers therefore retain the required fourth/eighth/sixteenth valuation classes before any ratio interpretation. All group, norm, trace, pole and common-scale equations are unchanged. The successful-place argument gives positive valuation of every relevant nonzero alternate F, including S, and the required primary bounds.

Thus A=1-D*F^2 is a local unit at that place; if F=0 it equals1. For every pair,

    A*(k*z-F)=k*(A*z-k)+(k^2-F+D*F^3).

This recovers the omitted raw alternate equations only after A is known to be nonzero. Finite alternate two-torsion is excluded by the positive low bound; it is not divided away beforehand. The regular primary equation likewise gives the correct zero value at O and, after the same unit conclusion, the exact primary ratio. H/V0 have their unchanged pre-ratio exclusions.

Now write H=m*R0+T_H and U_i=k_i*R0+T_i. The unchanged integer roots are n_i*P, with P=2R0. The identities with coefficients2m and2k_i kill both torsion terms, so the formal-logarithm ratios have free indices k_i/2 and m/2. Their only possible denominator is2, a unit at the consumed primes. This proves the same initial ratio integrality, then the unit-L H-depth bootstrap, then the original order40/order10 congruences to the integer root labels. The scalar argument sees precisely the old S orientation. Global rational-approximant nonvanishing still uses the modulo71/modulo7 certificates, not a real-positivity assumption for the enlarged auxiliary domain.

This is the same conditional domain theorem previously reviewed, with its formerly conditional S point, cache, ratio and orientation inputs now checked against actual299 equations. No new precision, prime-selection hypothesis or scalar subgroup assumption is introduced.

## Completeness and scope of equivalence

Use the old complete301 witnesses. With the old normalized S chart r=V_old/a, J=I_old/a, g=Q_old/a, K=K_old/a, set f=r^2, h=-J*r, F=g^2 and k=-K*g. The old source equations supply J^2+D*r^4=1, its alternate counterpart and the exact old ratios. They imply both new primary ratios and the regular alternate equation, including r=0 or g=0. The cached values stay Y=r^4 and B=g^4, in their original physical slots.

The actual old relation U-V=S supplies the complete reciprocal slope. Equivalently one can use s=(D*h-a*b)/(D*f+c): for these old doubled-point witnesses f is nonnegative at both real embeddings and c=a^2 is strictly positive, so its denominator is nonzero. This slope has the required orientation and satisfies the closure. All other witnesses are kept. There is no new real neighborhood, finite congruence, approximation choice, or change to the final H progression.

The resulting equivalence is of the rational input projection, using the inherited arithmetic theorem for soundness and old completeness in the other direction. It is not a claim that every new S auxiliary point has a rational old square root. The stronger full-witness bijection established for301 is not silently extended to299.

## Complete finite result

The reviewer-owned `check.py` and `algebra.py` import no author module. They check all16 changed old rows, both added rows2220/2221, deletion of exactly122/123, every old/new consumer of all ten affected private coordinates, all remaining objects, the actual cache and normalizer scaling, retained root curves, S sign action and the negative cache fixture. Every active coordinate is declared and every declared coordinate occurs.

The checker expands every primitive integral residual square and matches the complete frozen polynomial:299 total variables,298 witnesses,279 quadratic residuals,6630 quartic monomials, degree4, content1. The exact maximum is186624*C^2 with C=3^(2^25), attained at x89^4. Dominance is proved without expanding the enormous fixed C. The universal identities are separately checked in the frozen301 review program.

No author artifact was edited. This accepts the pinned299-r2 construction and its inherited input characterization. It does not approve an unbuilt ordinary companion, alter the rejected history, or authorize a publication step by itself.
