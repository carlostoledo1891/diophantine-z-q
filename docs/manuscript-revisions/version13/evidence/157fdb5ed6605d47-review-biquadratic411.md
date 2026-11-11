# Independent review of the scaled biquadratic charts

Reviewer: agent03. Mathematical proposer: agent10. Implementer: agent02. I accept the frozen 427-to-411 component. The two systems have exactly the same rational witnesses after the stated invertible change of private coordinates and reconstruction of the deleted coordinates. All outside coordinates, including the actual squared tests and ratios, are fixed. This is not a new extension of the point domain.

## Frozen scope and evidence

| Artifact | SHA-256 |
| --- | --- |
| 02-squares/point-charts/primary-reciprocal/candidate427-ir.json | 6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4 |
| 10-combination/BIQUADRATIC_PROPOSAL.md | ef84fd9b994bc1891fc89a9be090114f55736f2008e93c7b079414310fad8f9b |
| 02-squares/point-charts/biquadratic/REPORT411.md | d620690da4009267de230dbe65b465a6f0efda70306adfced8637e20895aad9f |
| biquadratic/candidate411-ir.json | 21757b59bbd9b9a8f1edfd31f02c5115e1f52ed7a7338c746878764c55437662 |
| biquadratic/polynomial411.json | 9c32c88f6567fdd9f88acc307d0ee867ce76745d18db1f8bdd97e7705c9b4ada |

The last two paths share the preceding point-charts parent. I read both frozen proofs, the actual source equations, producer and verifier, and the accepted reciprocal-chart and identity-extension descriptions. My separate check_biquadratic_review.py imports no author producer or checker. It independently derives the normalized root abscissae and squared outputs from the physical source rows, matches all old and new equations, checks the complete private incidence and all outside objects, verifies three unconditional polynomial identities, and recomputes the entire sum of squares. It passes 411 variables, 380 quadratic residuals and 6,350 quartic monomials, with the same fixed coefficient and maximum coefficient 16*C^2.

The source427 identity-domain acceptance is the existing dependency, including its argument that the shared V0 logarithm denominator remains nonzero. This component fixes H, V0 and every outside test or ratio. It therefore transports that accepted argument without an additional arithmetic assumption. Its saving of sixteen replaces, and is not additive to, the separate eight-coordinate inverse-addition saving from the same427 source.

## Algebra and domains

All field variables lie in K=Q(sqrt(2)), with D=(3-sqrt(2))^2. The unchanged root satisfies c=a^2 and b^2=c^2-D. It forces a!=0: otherwise c=0 and b^2=-D, impossible under a real embedding. Hence c is positive under both embeddings. For every r,g in K, the elements d=c+D*r^2 and e=c+D*g^2 are positive under both embeddings and nonzero. These facts are established before division.

Write the old primary and difference values as r,J,f,g,k,u,F, with f=r^2, F=g^2. The source rows are exactly

    J^2+D*r^4=1,
    d*g=a*J-b*r,
    u=c*r+b*g,
    d*k=b*J-2*a*u,
    J*L=r*s,
    k*z=-g.

The old squared outputs are YU=f^2 and YV=F^2. These are field squares, not the separate squares of their rational components.

The new private values are V=a*r, Q=a*g, I=a*J, K=a*k, W=r*g. Define

    T=c*(r^2+g^2)+D*r^2*g^2+2*b*r*g-1,
    A=b*r+d*g,
    E=b*g+e*r,
    B0=b^2-c^2+D.

I independently checked the unconditional polynomial identities

    A^2+c*D*r^4-c-d*T = r^2*B0,
    E^2+c*D*g^4-c-e*T = g^2*B0,
    -d*E-b*A+2*c*(c*r+b*g)+D*r*T+r*B0 = 0.

These identities give the two curve recoveries and the sign of the orientation equation. They do not rely on numerical samples or on generic nonzero values of r or g.

## Forward map

In an old witness, A=a*J and B0=0. The first identity and the primary curve give d*T=0, hence T=0. Multiplying the old k equation by a, substituting a*J=A and u=c*r+b*g, and using the third identity gives d*(a*k+E)=0. Thus a*k=-E. The second identity now gives k^2+D*g^4=1.

Substitute V=a*r, Q=a*g, I=a*J, K=a*k and W=r*g. The product equation V*Q=c*W, the biquadratic equation, and the two new I and K equations follow. The two ratio equations are the old equations multiplied by a. Finally D*c*YU+I^2=c and D*c*YV+K^2=c follow from YU=r^4, YV=g^4 and the two curve identities. Every outside coordinate is kept fixed.

## Reverse map and exact output identity

Given a new witness, define

    r=V/a, g=Q/a, J=I/a, k=K/a,
    f=r^2, F=g^2, u=c*r+b*g.

The first new equation and c=a^2 force W=r*g. The next three equations then say T=0, A=a*J, and E=-a*k. The first two checked identities give J^2+D*r^4=1 and k^2+D*g^4=1. The third gives the old orientation equation after division by the nonzero a. The old g equation, f and F definitions, and u definition follow directly.

The output equation D*c*YU+I^2=c now compares with c*(J^2+D*r^4)=c to give D*c*(YU-r^4)=0. Since D and c are nonzero, YU=r^4=f^2. The same argument gives YV=g^4=F^2. Thus the new outputs are the actual old squared parameters, not arbitrary surrogates with similar local behavior. Dividing the new ratio rows by a restores the old L and z equations. All old rows therefore hold with exactly the retained outside values.

The two maps are inverse: the cross equation uniquely restores W=r*g; the four scaled variables recover through division by a; and the deleted f,F and repurposed old u are uniquely reconstructed. Division in K has rational component denominators Norm(a)!=0, so the maps stay in the same rational quantified domain.

## Identity branches and zero cases

Neither map divides by r,g,J,k,W,L,z or any test value. The only divisions needed are by a, d in the forward proof, and the fixed nonzero D and c when identifying outputs. Their nonvanishing was proved above. Therefore r=0, which represents a primary identity point, and g=0, which represents a difference identity point, are included.

More explicitly, when r=0, W=0 and the biquadratic relation gives Q^2=1, so g is nonzero and the recovered primary curve has J^2=1. The retained equation forces L=0. When g=0, W=0 and V^2=1; the recovered difference curve has k^2=1 and the retained equation forces z=0. These are the source's accepted regular values at the identity. Both r and g cannot vanish because that would make the biquadratic equation read 0=1. No branch sign is discarded, and the recovered source witness determines the same points. The argument includes arbitrary allowed signs of the root a and of the reciprocal chart coordinates.

## Physical consumer audit

For each of A,S,T,Z, the seven old field pairs become five. Deleted rational IDs are (144,145,162,163), (148,149,166,167), (152,153,170,171), and (156,157,174,175). All five other pairs are repurposed by the specified scaling, including the old u slot becoming W. The complete incidence check includes every repurposed coordinate, not only the deleted f-values.

The retained YU values are the exact outputs of testSquare.1.(i-1); the retained YV values are the exact outputs of logVi.fSquare. My checker derives each as the affine remainder of its old field-square equation, allowing the actual component scaling, and then tests the new equations against those derived expressions. It also independently derives each root c from the retained a-square rows and matches the b curve, including the unusual T-chart scaling.

Every old or new equation within each private block matches its stated field equation. Every outside row and coordinate object is identical, and all other top-level metadata and fixed parameters are identical. Consequently no later logarithm, detector product, scalar expression, height scale, root odd chart, H or V0 consumer has changed meaning. All four transformations apply simultaneously and independently.

This accepts the frozen component. Combining it with other reductions requires a fresh transport check on the exact combined source, especially because the prior inverse-addition419 packet overlaps these same private blocks.
