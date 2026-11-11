# Independent review of the scalar preparation conic

I accept the 494-to-493 scalar-preparation replacement in `02-squares`. I did not author it. The old and new systems have the same projection onto their exterior coordinates, including the retained squared preparation value. The exceptional branch is handled correctly. This acceptance covers only this replacement, not the earlier 498-to-494 pole changes or the full arithmetic construction.

The frozen source `candidate494-ir.json` has SHA-256 `fc6ae1c382688596b5434f2412700ac42f4b800e0a8d4f2ff28b5151f3c45ccf`. The target `candidate493-ir.json` has SHA-256 `c4298c8a7e147797e0ab8e1cc3e7e3d3f4431d29609fec394154345306441b2d`. Its polynomial hash is `63b56d3582ea1732f25b9b02e0f7ae0a2ba0a64b722d941915a31141ab41f2ea`.

## Literal normalization and equations

The source IDs are b=526, t=50, t2=528, T=529, W=530 and u2=531. Define the semantic quantities B=-K*b and N=K^2*u2, where the exact rational normalization constant is the positive integer

    K=80990493410131000784375977023646274345820490095244015289194989569855772668241364832628280392076492800000000000000.

I checked this scaling against the actual four source rows, not only their names. Rows 495–498 are exactly

    t^2-t2=0,
    1-B(T-t2)=0,
    2-TW=0,
    (W-B)^2-N=0.

Thus B is nonzero and T is nonzero in every source solution. The replacement reuses IDs 50,528,529 as U,J,Y and removes ID 530. Its three rows are exactly

    U^2-N=0,
    1-BJ=0,
    NJ+Y^2-B=0.

The replacement therefore also forces B nonzero. It does not rely on an external nonzero assumption or drop the source's domain restriction.

## Forward map

Given an old solution, set

    U=W-B,    J=T-t2=1/B,    Y=tW.

The first two new equations follow directly from the source equations. Since t2=t^2 and T=t^2+1/B, the relation TW=2 gives

    U^2+B Y^2
      =(W-B)^2+B t^2 W^2
      =W^2(1+B t^2)-2BW+B^2
      =B^2.

Division by the already proved nonzero B yields NJ+Y^2=B. The exterior quantities B and N are preserved.

## Reverse map, including the exceptional branch

Suppose a new solution is given. Then J=1/B and U^2+B Y^2=B^2. If d=B+U is nonzero, choose

    W=d,    t=Y/d,    t2=t^2,    T=t^2+J.

Using B Y^2=(B-U)(B+U), one obtains

    T*d = Y^2/d + d/B = (B-U)/B+(B+U)/B=2.

All four old equations now hold, including (W-B)^2=N because W-B=U.

If d=0, then U=-B and N=B^2. The conic equation gives B Y^2=0, so Y=0 over Q. Choose instead

    W=2B,    t=t2=0,    T=J=1/B.

These values satisfy all old equations and have (W-B)^2=B^2=N. The old unsquared preparation value is +B, whereas the new U is -B. This sign change is allowed because the exterior system consumes only N. Thus the result is equality of exterior projections, not a bijection preserving the private unsquared preparation value.

## Consumer coverage and verification

I independently enumerated the literal residual incidence. The old private coordinates 50,528,529,530 occur only in rows 495,496,497,498. The retained coordinate 531 occurs in the old squared-value definition and the downstream `scalar.Bh.definition` row 499. The latter uses only its normalized squared value N. In the new system the private coordinates U,J,Y occur only in the three new rows. Every exterior row is unchanged, so switching the exceptional branch's sign cannot affect another constraint.

I read `build493.py`, `verify493.py`, the exact certificate and both residual systems, then ran the read-only verifier. It checks the literal normalization above, polynomial identities, complete private-coordinate incidence, all exterior rows, and the full sum-of-squares table. It passed with 493 variables, 462 quadratic residuals, degree four and 24,645 monomials. Its invocation also checked the preceding 494-coordinate table, but this review does not independently accept that preceding arithmetic change.

The rational maps above prove the conic replacement for every rational exterior assignment. They invoke no number-theoretic theorem, sign restriction on B, or unproved assertion about rational points on conics. No missing branch or additional hypothesis was found. No shared source or released manuscript was edited.
