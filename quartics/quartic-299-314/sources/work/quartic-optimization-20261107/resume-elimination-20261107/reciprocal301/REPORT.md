# Alternate-ordinate elimination: proposed301

Author: agent01. This is an unreviewed exact elimination from accepted307. It removes six rational coordinates, giving301 total variables,300 witnesses,277 quadratic residuals and6423 quartic monomials. The primitive sum of squares has degree4, content1 and maximum coefficient186624*C^2, C=3^(2^25). No ordinary companion or publication is claimed.

The source is `../../reciprocal307-20261107/candidate307-ir.json`, SHA256 `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`. Its independent review is `../../resume-review-reciprocal307-01/REVIEW.md`, SHA256 `055f82695b4757c534f5d8a915afe2ede778730f3291fd2b1da6d69564d472e8`. That review was by the present author; it is evidence for the source and is not independent acceptance of this new elimination.

The targetIR SHA256 is `ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6`; the polynomial SHA256 is `738893f68014f1b92852585fcda5e32946cdcdb702fe37f6f7c584d4f97be76f`.

## Exact local substitution

Use the accepted307 negative reciprocal convention and its stored Y=f^2, B=F^2. For each A/T/Z chart remove k, the alternate reciprocal ordinate, and reconstruct it by

    k=s*(f-F)-h.

This is a polynomial map, with no denominator or sign choice. Retain the primary curve, both square caches and s^2=c-D(f+F). Replace the divided-difference equation by

    2*s*h-c*(f-F)-1+D*(2*Y+f*F)=0.

Retain the alternate regular ratio in the form

    (1-D*B)*z-s*(f-F)+h=0.

All these equations have degree at most2. Remove the alternate curve, the secant equation used to define k, and the alternate raw ratio k*z=F. All primary ratio equations remain unchanged. No other coordinate is reinterpreted.

For a direct certificate let eY=f^2-Y, eB=F^2-B, eS=s^2-c+D(f+F), let q denote the new divided-difference residual, and reconstruct k as above. The old divided-difference residual r2 satisfies

    r2=q-eS*(f-F)+D*(eY-eB).

Writing ch=h^2-f+D*f*Y and ck=k^2-F+D*F*B, one has

    ck=ch-(f-F)*r2+D*F*eY-D*f*eB.

Thus the secant, divided-difference and alternate curve all recover polynomially, including the identity and tangent branches. `verify.py` checks these as universal polynomial identities with independent D. The resulting actual point difference and root restoration are exactly those of307, without any new root-domain assertion.

## Removed raw ratio and the order of the argument

Put A=1-D*B and reg=A*z-k. Then

    A*(k*z-F)=k*reg+ck.

Consequently the only remaining restoration obligation is A!=0. It must not be assumed from the old raw ratio. Here is the noncircular order.

First restore k and its curve by the polynomial identities. This restores the accepted307 oriented point relation and all root square charts, before any auxiliary ratios. The unchanged height/scalar-anchor argument excludes the all-empty-radical branch. It uses roots, H/V0 and scalar data, not the alternate raw auxiliary ratios. The inherited shared314 low-test argument then applies to the literal cached powers. Its valuation periods need only the now-restored raw point curves, not k*z=F and not an interpreted logarithm. At a required successful place it gives positive valuation of each nonzero alternate F, with F=0 allowed as the identity case. Thus B=F^2 gives A a unit there; if F=0 then A=1 directly. Hence A is nonzero in K. The displayed identity now restores k*z=F. Every original307 residual holds.

The required prior arithmetic is the regular-ratio domain proposal `../../resume-auxiliary-domain-20261107/PROPOSAL.md`, SHA256 `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`, especially its pre-logarithm valuation periods and successful-place argument. Its independent review is `work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md`, SHA256 `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b`. That proof was designed for regular ratios alone. The accepted307 artifact happens to include the additional raw ratios; this elimination uses their established global redundancy. This is a new application to301, requiring its own review.

Forward mapping merely deletes the three k pairs. The identities imply all new residuals. Reverse mapping restores those pairs by the polynomial formula and the argument above verifies all old residuals. Since the old secant equations fix k uniquely, these maps are inverse on the full rational zero sets. They preserve every outside witness and the input, not just integer existence. There is no new simultaneous approximation choice and no new arithmetic premise. Local subsystems without the low tests need not have this equivalence: finite alternate two-torsion is an explicitly excluded global branch.

## Literal construction

Deleted coordinate IDs are114,115,130,131,138,139. A/T/Z row triples removed are respectively700/702/116,716/718/124,724/726/128, each together with its following imaginary component. Changed pairs are704,720,728 and2202,2206,2210. Every other residual and every remaining coordinate record is unchanged. The certificate records all IDs. The S-root, scalar equations, H/V0, anchors, common scale, tests and all logarithm consumers are unchanged.

`verify.py` imports no builder. It independently builds the changed field equations, checks complete old/new consumer incidence, proves the universal identities, expands every primitive integral residual square and compares the full table. It also checks degree, content, active-variable count and the exact specialized maximum by coefficient dominance without expanding C. These author checks pass; independent acceptance remains required.
