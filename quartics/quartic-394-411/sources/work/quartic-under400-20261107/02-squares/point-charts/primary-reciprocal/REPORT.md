# Four reciprocal primary charts

This packet changes the 435-variable source into a 428-variable candidate, with 427 witnesses, 397 quadratic residuals and 6,290 monomials in its primitive sum of squares. It saves two coordinates at each of four primary charts and adds one global guard for V0. The input, four root points and their height product remain fixed. All files are isolated research artifacts; no published file was changed.

This is a controlled enlargement of the intermediate point domain, not an equivalence with the old finite-chart solution set. The new system permits U1 through U4 or V1 through V4 to be the elliptic identity O. The arithmetic proof must be extended at these branches. The inherited proof alone cannot be cited as if nothing changed. Independent source-level review of this extension is supplied by `00-independent470/IDENTITY_EXTENSION.md`, SHA256 `d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32`; a further review is pending. H and V0 remain nonidentity in the candidate.

## Exact source and artifacts

- Source `10-combination/combined435-ir.json`, SHA256 `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859`.
- Candidate `candidate428-ir.json`, SHA256 `236e837094097aef4596a225f541347f314f7596511b75cbae09b722fa4a184d`.
- Semantic normalization source: published repository `quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json`, SHA256 `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.
- Exact polynomial hash, operation IDs and counts are in `certificate428.json`.
- `verify_primary.py` independently checks actual old/new equations, outside consumers, the generic norm and orientation identities and every coefficient of the full sum of squares. `verification428.json` records a pass.

The earlier `candidate427-ir.json` is an unguarded exploratory variant. It is not the candidate claimed by this report. Removing the V0 guard requires the additional boundary argument described in the independent arithmetic review and its separate acceptance.

## Equations and unchanged meanings

Write K=Q(sqrt(2)), D=(3-sqrt(2))². For each pair retain the root chart

    c=a²,  b²=c²-D,  Q=(c,ab).

The source proves a and b nonzero; c is positive in both real embeddings. In the primary chart replace the old h,j,x,f by r,J,f, using

    f=r²,
    J²+D f²=1.

When r is nonzero its represented point is

    U=(1/f, J/r³),   h=1/r, j=J/f, x=1/f.

When r=0 the equations force f=0 and J=±1, and the represented point is U=O. Thus both rational chart branches have a precise interpretation. The old duplicated point-coordinate pair x is deleted; the old h,j pairs are renamed r,J. The primary f pair keeps its exact former meaning on the finite branch and extends f(O)=0.

Let s be the unchanged common primary reciprocal, s=j_H/h_H=-1/z_H. The primary ratio equation becomes

    J*L_i = r*s.

J is always nonzero. If J=0, then D f²=1. Writing d0=3-sqrt(2), this gives d0*f=±1, impossible because f=r² and taking rational norms gives 7*Norm(r)²=1. Consequently the equation determines L_i. On the finite branch it is the original ratio z(U_i)/z(H); at r=0 it forces L_i=0, the correct extended ratio.

For the difference put d=c+D f and replace the three old field gates (slope, slope square, ordinate product) by g,u,k with

    d*g = a*J-b*r,
    u = c*r+b*g,
    d*k = b*J-2*a*u.

These are all quadratic. Keep the original difference fV,zV coordinates, with

    fV=g²,
    k*zV=-g.

No extra private field gate is introduced. The useful identity in the last difference equation was found independently by agent01.

## Denominators, orientation and identity branches

The field element d=c+D*r² is positive in both real embeddings, hence nonzero even when r=0. Thus g,u,k are uniquely specified by the incoming chart values. Put N=aJ-br and

    Knum=bJ*d-2a*(c*r*d+b*N).

Then g=N/d and k=Knum/d². Modulo c=a², b²=c²-D and J²=1-D*r⁴, the exact checked identity is

    Knum²+D*N⁴=d⁴.

It proves k²+D*g⁴=1. The same norm argument proves k nonzero: k=0 would imply (d0*g²)²=1, giving 7*Norm(g)²=1. Therefore zV=-g/k is uniquely determined in every branch.

For r nonzero the displayed g,k are exactly the reciprocal difference formulas in the inherited fixed-reference proof, with a,b,c now treated as variable root-chart values satisfying the same equations. Indeed the source formula becomes

    k = [-bJ(c-Df)-2D*a*r(c*f+1)]/d².

The verifier checks this numerator against Knum modulo the root equation. The ordinary subtraction formula, including the coincident-abscissa doubling branch, gives V=U-Q with f(V)=g² and z(V)=-g/k. This specialization uses no additional assumption that a,b,c be constant rationals.

The new cases have fully determined outputs:

- If r=0, then J=±1, g=J/a, u=bJ/a, k=-bJ/c and zV=a/b. Thus U=O and V=-Q. Both signs of J describe the same pair of points and the same retained f/z outputs.
- If r is nonzero and g=0, the relation aJ=br and the two curve equations imply c*f=1: subtracting gives `(1-c*f)*(c+D*f)=0`, and d is nonzero. It follows that U=Q, k=-a*r=±1 and zV=0. Thus V=O, fV=0 and its formal logarithm is zero.
- The r=0 and g=0 branches cannot occur together because a and J are nonzero.
- If neither is zero, the inverse chart formulas recover the genuine finite primary and difference points, including U=-Q, where V=-2Q. No rational real-component nonvanishing assumption is used.

## Global V0 domain and downstream arithmetic

The new rational coordinate sigma has exactly one equation

    f(V0)_0 * sigma = 1.

The source literally has f(V0)_0=g0²+2g1². Thus the guard is equivalent to its K-valued g being nonzero. The existing k norm proof and logarithm-approximation unit proof then keep V0 and its logarithm denominator nonzero. This guard is necessary for the proof route claimed here: the previous indirect exclusion of V0=O used V1 nonidentity, which is no longer available. Old source solutions already had V0 nonidentity, so they all extend by sigma=1/f(V0)_0.

All formal-log approximation and ratio rows outside the primary L_i equations are literally unchanged. At O, define f=z=ell=0 and the approximation factor to be one; do not form the undefined written quotient ell/z. Its regular unit-series identity is the object used in the extension. The physical difference-log rows then force zero difference ratios since their common V0 logarithm denominator stays nonzero. The one-place forcing lemma already permits zero test values. The height targets are the unchanged nonidentity root points Q, and their height products are unchanged. The independent arithmetic report binds these facts to the actual consuming proof, including the local-transfer and height steps. This packet does not infer them merely from finite polynomial checks.

Completeness follows by mapping every old finite source solution through the rational formulas above and adjoining the V0 inverse. Soundness is through the enlarged, reviewed arithmetic point interpretation; a new identity-branch solution need not lift to an old finite-chart witness. Both directions preserve the original rational input and the intended integer predicate, conditional on acceptance of that arithmetic extension.

## Actual source checking

The builder reads exact field normalizations from the pinned semantic source, including the nonunit normalizations of root abscissae and old slope/ordinate auxiliaries. For each of the four pairs the verifier independently matches every old primary, primary-ratio, slope, slope-square, ordinate, f, z and complete-tangent row, and matches every new equation above. It checks that removed and repurposed coordinates have no consumer outside the stated changed rows. Every outside row and every untouched coordinate is the exact source object. This includes H, all root odd charts, the scalar point, all height scales and all detector equations.

Eight coordinates and sixteen rows are removed across the four pairs. One coordinate and one guard row are added. The full primitive sum of squares has degree four and content one. Run `python -B build_primary.py` followed by `python -B verify_primary.py` to regenerate and check the finite certificate. Independent arithmetic and composed-source review remain separate requirements.

