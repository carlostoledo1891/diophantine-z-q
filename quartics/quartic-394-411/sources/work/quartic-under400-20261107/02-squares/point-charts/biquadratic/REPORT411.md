# Scaled biquadratic charts save sixteen coordinates

The candidate has 411 total rational coordinates, 410 witnesses, 380 quadratic residuals and 6,350 quartic monomials. It removes sixteen coordinates from the accepted427 source. This replaces the separate eight-coordinate inverse-addition reduction; the savings are not additive. The previous427 and419 packets remain unchanged. Independent review is pending.

Agent10 proposed the scaled equations and wrote `10-combination/BIQUADRATIC_PROPOSAL.md`, SHA256 `ef84fd9b994bc1891fc89a9be090114f55736f2008e93c7b079414310fad8f9b`. This packet implements them against the actual source and checks every affected field normalization and consumer. The change is an exact rational equivalence of witness spaces after the specified coordinate change, including the identity branches already accepted in427. It requires no new arithmetic argument.

## Frozen inputs and outputs

- Source `../primary-reciprocal/candidate427-ir.json`: `6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4`.
- Candidate `candidate411-ir.json`: `21757b59bbd9b9a8f1edfd31f02c5115e1f52ed7a7338c746878764c55437662`.
- Polynomial `polynomial411.json`: `9c32c88f6567fdd9f88acc307d0ee867ce76745d18db1f8bdd97e7705c9b4ada`.
- Published semantic source `quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json`: `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.

## Equations and exact maps

Work over K=Q(sqrt(2)), with D=(3-sqrt(2))². Retain each root a,b,c with c=a² and b²=c²-D. The original block uses seven K-valued coordinates r,J,f,g,k,u,F, satisfying

    f=r²,                J²+D*f²=1,
    (c+D*f)*g=a*J-b*r,  u=c*r+b*g,
    (c+D*f)*k=b*J-2*a*u,
    F=g²,                k*z=-g,        J*L=r*s.

The retained test outputs are YU=f² and YV=F². Here s is the unchanged common primary reciprocal. All other uses of f and F in the actual source are within these displayed equations or the definitions of YU,YV.

Replace the seven field pairs by five field pairs

    V=a*r, Q=a*g, I=a*J, K=a*k, W=r*g.

The new block is

    V*Q=c*W,
    V²+Q²+D*W²+2*b*W=1,
    a*I=b*V+c*Q+D*V*W,
    a*K=-b*Q-c*V-D*Q*W,
    I*L=V*s,             K*z=-Q,
    D*c*YU+I²=c,         D*c*YV+K²=c.

Every equation is quadratic. In particular c is an existing coordinate, so c*YU and c*YV are quadratic products. The old coordinate pairs r,J,g,k,u are repurposed respectively as V,I,Q,K,W. The old f,F pairs are deleted. All roots, the input, L,z,YU,YV and every outside coordinate retain their meanings and values.

For reverse recovery set

    r=V/a, g=Q/a, J=I/a, k=K/a,
    f=r², F=g², u=c*r+b*g.

The retained root equations force a nonzero, since a=0 would give b²=-D, impossible at a real embedding. Thus c=a² is positive at both real embeddings. The elements d=c+D*r² and e=c+D*g² are also positive, including when r or g is zero. Every division below has therefore been justified before use.

## Proof of both directions

Define

    B=c*(r²+g²)+D*r²*g²+2*b*r*g-1,
    G=d*g-a*J+b*r,
    E=a*k+b*g+e*r,
    H=d*k-b*J+2*a*(c*r+b*g).

Modulo only the two retained root equations, the following identities hold:

    a²*(J²+D*r⁴-1) = d*B-G*(d*g+b*r+a*J),
    a²*(k²+D*g⁴-1) = e*B+E*(a*k-b*g-e*r),
    d*E = a*H+D*r*B-b*G.

The checker verifies stronger unconditional versions, including the explicit multiples of c-a² and b²-c²+D, rather than assuming the root equations during expansion.

From an old solution, the first identity and G=0 imply B=0 since d is nonzero. The third identity and H=0 then imply E=0. The second identity gives k²+D*g⁴=1. Substituting the displayed forward map now verifies all eight new equations, including the two retained squared outputs.

Conversely, V*Q=c*W and c=a² imply W=r*g under the reverse map. The next three new equations give B=G=E=0. The first two identities yield J²+D*r⁴=1 and k²+D*g⁴=1. The third yields H=0 since a is nonzero. These recover all old structural equations. Comparing D*c*YU+I²=c with the reconstructed J curve gives D*c*(YU-r⁴)=0. Since D and c are nonzero, YU=r⁴=f². The identical argument gives YV=g⁴=F². Dividing the two retained ratio equations by a restores J*L=r*s and k*z=-g.

The forward and reverse maps are inverse on all coordinates. They never divide by r,g,J,k,W,L or z. The r=0 primary identity branch, g=0 difference identity branch and every sign choice are included. No different curve point or squared-test value is introduced at zero.

## Exact physical consumers

The verifier independently reconstructs the old root, primary, difference, ratio and squared-output equations from their literal source rows. It checks each new component, allowing only nonzero rational normalization. It explicitly checks all occurrences of every repurposed or deleted coordinate and compares every outside row and coordinate object literally.

For primary Ui, the retained YU is `testSquare.1.(i-1)` with its exact stored normalization. For Vi, YV is `logVi.fSquare`, also with its exact stored normalization. These are the field squares of the actual old f-values, not componentwise squares and not a substitute test family. The complete old consumer lists of each removed f component are recorded in `verification411.json` under `removedFConsumers`. No removed f-value has an outside consumer. All later polynomial/logarithm factors and detector test products continue to use the identical retained YU,YV values.

H, V0, scalar, root odd charts, height scales and all detector rows are unchanged. The inherited427 identity-domain arithmetic remains the same. A future composition still needs exact transport checking against its chosen source.

## Reproduction

Run `python -B build_biquadratic.py` and `python -B verify_biquadratic.py`. The verifier imports no producer and uses only Python's standard library. It checks the three unconditional recovery identities, all old/new equations and incidences, fixed metadata, degree bounds, surviving-coordinate coverage, and every coefficient of the complete primitive sum of squares. All checks passed. The degree is four and the content one. Independent review of the frozen packet is required before acceptance.
