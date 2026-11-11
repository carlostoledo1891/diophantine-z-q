# Preferred Kummer presentation with an affine slope parameter

This variant saves the same two rational coordinates as392 and excludes fH=0 algebraically. It requires no new zero-branch contact argument. The candidate has392 total variables,391 witnesses,362 quadratic residuals and6843 quartic monomials. Independent acceptance is pending. Both earlier392 files and all released files remain unchanged.

## Frozen files

| File | SHA256 |
| --- | --- |
| Source under400 `10-combination/combined394-ir.json` | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` |
| `candidate392t-ir.json` | `846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba` |
| `polynomial392t.json` | `46d54b4c183911e195f56dda232a565d88fe5b2a6df56f591efedab56c15f26f` |

`build392t.py` constructs this variant directly from frozen394. `verify392t.py` checks all field equations, every affine substitution consumer, the recovery identities, and every SOS coefficient. The checker is this author's evidence, not an independent review. The same source arithmetic and accepted394 H-domain proof identified in REPORT392.md are retained.

## Equations and meanings

Use K=Q(rho), rho^2=2, D=(3-rho)^2 and the fixed P=(c,ab), where a=-1+7rho/4, b=39/8-9rho/2, c=a^2=(57-28rho)/8, b^2=c^2-D. All are fixed nonzero constants.

The old394 H/V0 subsystem is

    x*f=1, S^2=x-D*f,
    (c*x+D)*v=a*S-b, v^2=f*F.

The existing slots are f=(140,141), F=(160,161), v=(700,701), S=(142,143). The x pair90,91 has physical value90+2*91*rho.

Delete the x pair and repurpose the old S slots as t. Impose

    K0 := c*(f+F)+D*v^2+2*b*v-1=0,
    A0 := v-f*t=0,
    E0 := F-v*t=0.

Every equation is quadratic. Define the old S in every other consumer by the fixed affine expression

    Sback=(b+c*t+D*v)/a.

Its constant coefficients are

    b/a=-87/41+(129/164)*rho,
    c/a=a=-1+(7/4)*rho,
    D/a=-80/41+(106/41)*rho.

Thus substituting Sback preserves quadratic degree. The denominators are fixed nonzero rationals; they require no new quantified variable or domain restriction. The only affected outside rows are the eight primary ratio component equations, the two V0 logarithm component equations, and the two scalar ratio component equations. The checker compares all twelve complete substitutions and every other row and coordinate record. Every semantic ratio and logarithm value is preserved.

## Nonzero f is now algebraic

If f=0, A0=0 gives v=0 and E0=0 gives F=0. Then K0=-1, a contradiction. Hence f is nonzero for every new solution, before any root, anchor, height or logarithm argument is used. This applies over K directly, not componentwise.

The candidate does not assert that f is a square in K. It asserts the same relative squareclass relation as the old v^2=fF equation: after f!=0, t=v/f and F/f=t^2. Neither t nor F is required to be nonzero at this algebraic stage. Their exceptional points are handled by the inherited full-system proof after reconstruction.

## Exact reverse reconstruction

Given a new solution, put x=1/f, and interpret S as Sback. Then

    Aold := a*f*S-b*f-(c+D*f)*v = -c*A0,
    Eold := v^2-f*F = v*A0-f*E0.

Both are zero. Let d=c+D*f, B=b*f+d*v, H0=f*S^2+D*f^2-1. The unconditional identity, with c=a^2, is

    c*f*H0 = f*d*K0+c*d*Eold
              +(b^2-c^2+D)*f^2+Aold*(a*f*S+B).

The fixed root relation makes the third term zero. Since c and f are nonzero, H0=0. This restores S^2=x-Df. Dividing Aold=0 by f gives the old difference equation. The old reciprocal equation and v^2=fF are also restored. No division by d, t, v, S, F, or any logarithm is used in this direction.

For the physical x slots, write 1/f=x0+x1*rho and set old90=x0, old91=x1/2. All other old coordinates are unchanged except the explicit Sback substitution. The checker accounts for this physical normalization in its source interface.

The restored values satisfy the entire accepted394 system. Its H-domain exclusion, half-index and torsion argument, actual scalar positivity, normalized pole, anchor restoration, and local/global soundness can therefore be applied in their already accepted order. No new arithmetic application is needed to exclude a pre-H zero branch.

## Forward map and completeness

In an old full394 solution, f!=0 follows from x*f=1. Set

    t=v/f=(a*S-b-D*v)/c.

The equality follows from the old difference equation. This also shows that the change between S and t, with v fixed, is invertible affine over K. The old v^2=fF equation gives E0=0 and the definition gives A0=0.

The accepted394 exceptional-H argument excludes c*x+D=0 before using logarithm ratios. Consequently d=f*(c*x+D) is nonzero in every old full solution. In the displayed unconditional identity H0=Aold=Eold=0, so division by f*d gives K0=0. Thus the old full witness maps to a new witness. This invocation of an already proved old-domain fact is the only nonzero d requirement; the reverse map above does not need it.

All outside old values are exactly restored by Sback. In particular the ordinary source completeness construction works unchanged, and the new map introduces no real or finite-place choice, no new CRT condition, and no strengthened point domain. The two maps are inverse on full solution sets. They fix the input, all root points, fH, fV0, every ratio and logarithm, scalar values and private pole/anchor witnesses. They replace only the redundant H abscissa coordinates and the representation of S.

## Evidence and review boundary

The exact checker passes the source incidence for90,91, all twelve Sback consumers, the other untouched residuals and coordinate records, the two identities Aold=-c*A0 and Eold=v*A0-f*E0, the generic recovery identity, and the full primitive sum of squares. It also confirms the unchanged conjugate fV0 leaf in all three height detectors, although that leaf is no longer needed for a new zero-branch argument.

All392 coordinates occur. There are362 residuals and6843 monomials. The fixed C remains3^(2^25), with maximum coefficient16*C^2 on the unchanged W_anchor^2*tau_anchor^2 monomial. All new coefficients are fixed small rationals before primitive normalization, and the old1520-bit constant coefficients dominate their size. No C-dependent coordinate is added.

This is the preferred version for review: it trades more expanded monomials for an algebraic nonzero domain and the same coordinate saving. The whole-polynomial count remains far above the under300 target. No further saving is claimed here.
