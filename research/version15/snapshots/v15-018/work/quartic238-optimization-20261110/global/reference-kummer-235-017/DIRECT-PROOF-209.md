# Direct proof for the 235-variable, 209-residual system

This is an author proof for the final selected presentation. It compares directly with the accepted original raw237 parity-core system, SHA64649e6f06b3d8dc1f592805610f550b9500a7a44d4ed13796af0f83544e3c9b. The intermediate236 and235/211 constructions are historical research artifacts, not assumed accepted premises. Full finite construction and independent review are separate obligations.

## Exact replacement

Work over K=Q(r), r²=2. In raw237 coordinates put

    D=11−6r, f=x19+r*x20, S=x21+r*x22,
    v=x23+r*x24, g=x139+r*x140,
    chi=x17+2r*x18,
    a=57−28r, b=8−14r, c=88−48r, d=39−36r.

Delete coordinates17 and18. Delete old rational rows1–4 and88–89, and insert the four rational components of

    F=(a+c*f)*g+b*f*S+d*f=0,
    E=(b*S−d)*g−a*f+8=0.

Retain every other parent row and coordinate meaning, including g²=f*v, both v-square output definitions, the original scalar parity core, both detectors, all root charts and every Lucas equation. Coordinates17 and18 have no other consumers. There are235 rational variables and209 quadratic residuals. Both new field equations have degree at most two. No new auxiliary variable or nonzero guard is used.

## Polynomial identity

Let A=a+c*f and H=f*S²−1+D*f². Exact arithmetic in K gives

    A*(a*f−8)=b²*D*f²+d²*f−b²,
    F*(b*S−d)−A*E=b²*H.

The second identity follows by expanding: the terms A*g*(b*S−d) cancel, leaving A*(a*f−8)+f*(b²*S²−d²). The first identity then gives b²*H. The constant b is nonzero.

## New solution to old solution

From F=E=0, the polynomial identity gives H=0. In particular f cannot vanish, since at f=0 one has H=−1. Recover chi=1/f. Then H=0 gives S²=chi−D*f, and F/f=0 gives (a*chi+c)*g+b*S+d=0. Thus all six deleted parent rows hold. Every other parent row is retained. This implication makes no division by A,g,S,v, or a root coordinate, and applies to every zero stratum those variables can have.

## Old solution to new solution

The old equations give chi*f=1 and H=0. Multiplication of the old reference equation by f gives F=0. The polynomial identity therefore gives A*E=0.

The only value at which A could vanish is

    f*=−a/c=−291/392−(17/196)r,
    Norm(f*)=(41/56)².

On the admitted family A_N=149^(2N+1), with inherited sufficiently large N, the unchanged positive scalar normalizer gives nu=v149(Rscalar)>0 odd. The original parity scalar equations force v149(Norm(f))>7nu/4>0. The exceptional norm has valuation zero, so A cannot vanish. Consequently E=0.

For completeness, that scalar implication is noncircular. The old equation chi*f=1 already gives f!=0. Since149 is inert in K, v149(Norm(f)) is even. The unchanged scalar formula is

    W=Z0^4/Rscalar^10+Z1²/Rscalar^5+Norm(f)²/Rscalar^4,
    B=Rscalar*(Rscalar+9792)*W².

The three summand valuations have distinct residues modulo4:2, odd, and0. Zero Z components can be omitted. Rscalar>0 and Norm(f)!=0 imply W>0. The retained scalar pole excludes a negative odd valuation of B, so v149(W)>−nu/2. Hence2*v149(Norm(f))−4nu>−nu/2, yielding the required norm bound. This uses no new reference equation or division by A. It is the original parity237 core, not a later asymmetric or relative-norm proposal. The existing scalar proof and its independent review are pinned in the manifest.

## Both witness maps

Forward, forget old17 and old18, keep every other coordinate, and apply the finite constructor's index renumbering. Backward, keep all retained coordinates and restore

    old17=f0/Norm(f), old18=−f1/(2*Norm(f)).

The preceding argument proves Norm(f)!=0 on every new solution. These maps are inverse on the full rational solution sets in the admitted parameter family, with the input and A_N unchanged. No arbitrary-symbolic-A equivalence is asserted, because the old-to-new exceptional-factor exclusion uses that family.

The original input projection, arithmetic premises and sufficiently-large-family conclusion transfer. N0 remains ineffective. The constructor must separately verify exact row transport, all235 coordinates, the quartic expansion and coefficient profile. A sparse affine presentation may be selected only with its own exact inverse maps. This document claims no completed independent acceptance.
