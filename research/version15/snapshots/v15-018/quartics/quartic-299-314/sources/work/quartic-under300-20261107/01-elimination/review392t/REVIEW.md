# Independent acceptance of the 392t Kummer presentation

Accepted as a research transformation of the pinned, independently accepted 394 system. It has 392 total rational variables, 391 witnesses, 362 quadratic residuals and 6843 quartic monomials. The degree is four, integer content one and maximum coefficient 16*3^(2^26). This does not alter the frozen Version 13 release or reach the next below-300 publication threshold.

Reviewer: `/root/astra_quartic_opt01_elimination`. I authored neither this transformation nor its implementation. I read the frozen report, both source acceptance arguments, the actual old/new equations and all changed consumers. My independent checker imports no producer, project algebra helper or author checker.

## Frozen bindings

| Object | SHA-256 |
|---|---|
| Source under400 `10-combination/combined394-ir.json` | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` |
| Source acceptance `03-depth/integrated394/REVIEW.md` | `0d2be6af0bde35995ca0dfa6334aab1368ea298fd6974a4a231478f34c3c080f` |
| Under300 `03-depth/REPORT392t.md` | `b96a442d27a62189ef8c3ffdbe2b6ca368cc8b5e657a05cf5bf31735a19cfcfd` |
| `03-depth/candidate392t-ir.json` | `846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba` |
| `03-depth/polynomial392t.json` | `46d54b4c183911e195f56dda232a565d88fe5b2a6df56f591efedab56c15f26f` |

This review does not accept the different candidate392 IR `72cc3627...`, whose new zero branch required an additional global detector argument. The preliminary reading of that proposal is preserved separately in `ORIGINAL392-NOTES.md`.

## Actual equations and domains

Use K=Q(rho), rho squared=2, D=11-6rho, and the fixed P=(c,ab), with a=-1+7rho/4, b=39/8-9rho/2, c=a squared. Then b squared=c squared-D, and a,c are nonzero. These constants are checked exactly by the independent program, including 1/a=8/41+(14/41)rho.

Write f=fH, F=fV0 and v for the retained rescaled V0 parameter. The source equations are

    x*f=1,                    S^2=x-D*f,
    (c*x+D)*v=a*S-b,           v^2=f*F.

Their actual component normalization is checked: x is old coordinate90+2*coordinate91*rho, while f,F,S,v are the unscaled pairs 140/141,160/161,142/143,700/701.

The candidate removes 90/91, reuses 142/143 for t, and imposes

    K0=c*(f+F)+D*v^2+2*b*v-1=0,
    A0=v-f*t=0,               E0=F-v*t=0.

Every other old occurrence of S is replaced by

    Sback=(b+c*t+D*v)/a.

This is affine over K with fixed rational coefficients. It is not a new freely varying field parameter or a division by a witness.

If f=0, A0 forces v=0 and E0 then forces F=0, while K0 becomes -1. Hence f!=0 follows from these three field equations alone. No H point, logarithm ratio, scalar positivity, anchor or one-place detector is invoked. The argument uses equations over the field K and is valid for their exact rational component presentation.

## Reverse map and exact identities

Given a candidate solution, set x=1/f and S=Sback. Restore the physical old x slots by x0 and x1/2 when 1/f=x0+x1*rho. The independent checker verifies

    Aold=a*f*S-b*f-(c+D*f)*v=-c*A0,
    Eold=v^2-f*F=v*A0-f*E0.

Put d=c+D*f, B=b*f+d*v and H0=f*S squared+D*f squared-1. The full universal polynomial identity is

    c*f*H0=f*d*K0+c*d*Eold
             +(b^2-c^2+D)*f^2+Aold*(a*f*S+B).

I independently expanded it with a,b,D,f,F,S,v as indeterminates and c=a squared. The fixed P relation kills its third term. Since c*f is nonzero, H0=0, which restores S squared=x-D*f. Dividing Aold=0 by f restores the old difference equation. The other two old equations also hold.

All outside equations are satisfied because they are exactly the complete affine Sback substitutions. Thus every new solution reconstructs a full accepted394 solution before any of its arithmetic conclusions are used. This proves soundness without a new pre-H zero-branch argument. There is no division by d,t,v,S,F or a logarithm in this direction.

## Forward map and the inherited exceptional-H fact

For an old full394 solution, x*f=1 gives f!=0. Set t=v/f. The source difference equation also gives

    t=(a*S-b-D*v)/c,

so Sback recovers S exactly. The old v squared=f*F equation gives F=v*t. To obtain K0, apply the universal identity with H0=Aold=Eold=0. The remaining equation is f*d*K0=0.

Here one must justify d!=0; the local polynomial subsystem alone does not do so. The accepted source proof excludes c*x+D=0 using its pre-ratio exceptional-H argument. Such an abscissa is a translate of +P or -P by T0; its fH is a unit at every consumed place, forcing all three radicals to be 1 and contradicting the independent scalar anchor and root-height bound. The source394 review restores that anchor from its rescaled form without first using H, so this prior exclusion is not circular. Since d=f*(c*x+D), d is nonzero in every full source solution. Therefore K0=0.

This is an inherited consequence for full source witnesses, not a new arithmetic premise. Applying the forward map to every complete394 witness gives completeness with the same integer input and all previously chosen points, poles and local/real/CRT data. The reverse map then recovers x and S uniquely. The maps are inverse on full rational solution sets, fixing every other coordinate. No claim of equivalence for arbitrary assignments to only the old local subsystem is made.

## All consumers and zero cases

The union of old consumers of 90/91 is exactly the six component rows for x*f, the H curve and the V0 difference quotient. All are replaced as declared. Neither coordinate occurs in the new system.

The old S slots occur in the H/difference rows and exactly twelve outside rows: eight primary-ratio components, two V0-logarithm components and two scalar-ratio components. The independent checker reconstructs Sback and substitutes it into every old residual, matching all twelve complete new polynomials and their metadata. No other residual is changed. Coordinate records are preserved except for deletion of 90/91 and the explicit t renaming of 142/143. The fixed coefficient parameter and input are unchanged.

At the algebraic reconstruction stage t,v,F or S need not be nonzero. The maps do not divide by them. Any further forbidden zero or exceptional H is excluded only after the entire source system has been recovered and its accepted proof applies. This respects the source's general H domain, half-indices and two-torsion; it does not reimpose a square abscissa. The transformed logarithm and scalar-ratio equations regain precisely their old meanings, so their source nonvanishing arguments remain available in the original order.

The detector and anchor equations are unchanged, but no fresh use of their global implications is required for the new f!=0 argument. In particular the original392 conjugate-F detector proof is unnecessary for this candidate and is not silently imported.

## Independent finite result

`check.py` verifies source/report hashes, complete row and coordinate sets, unique identifiers, physical old and new equations, all outside substitutions, both immediate residual identities, the universal recovery identity and the algebraic zero-branch contradiction. It independently forms the primitive integer sum of squares and compares every coefficient with the frozen polynomial.

All 392 coordinates occur. The 6843 symbolic terms have distinct coordinate monomials after substituting fixed C, so the count does not conceal collisions between different C powers. The unique C-squared term remains 16*C squared*W_anchor squared*tau_anchor squared, with no constant or C-linear contribution to that same monomial. Other C-linear multipliers are at most 96, and all constant coefficients have at most 1520 bits. Thus the maximum remains exactly 16*3^(2^26), with degree four and content one.

Run `python -B check.py` in this directory to reproduce `CHECKS.json`. It writes only its local receipt. No released manuscript, frozen Version13 artifact, source candidate or author file was modified. A future composition or release still requires its own review and the below-300 release criterion.
