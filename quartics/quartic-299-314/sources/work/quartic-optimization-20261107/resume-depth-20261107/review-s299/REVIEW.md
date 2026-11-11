# Independent S auxiliary extension review

I accept the new S auxiliary extension in the corrected frozen299-r2 packet, within the precise scope below. The IR SHA256 is `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815`; the polynomial SHA256 is `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c`; the author report SHA256 is `ae5d127cb34de3b0f318f6faff3736738748286279012d3db3f9b46151b95b8b`. These files are in `work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2`. I read the frozen author report and checked these exact files. The initial299 candidate `ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd` was rejected for the wrong alternate-square cache. It is preserved in sibling `reciprocal299`, with its rejection notice. See my retained FINDING-S299-1.md.

## Scope and independence

Reviewer: agent03. The reviewed change is agent01's S-only extension of the reciprocal auxiliary chart, with the parent-proposed explicit orientation equation. I did not author that extension, its orientation equation, or the301 alternate-ordinate elimination. I have authored earlier detector and anchor arguments in the dependency chain. This is therefore a scoped non-author review of the new S extension, not independent acceptance of the whole quartic, earlier arithmetic, or a publication.

The predecessor is the301 IR `ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6`. Agent10 independently accepted that predecessor in `work/quartic-under300-20261107/10-combination/review-reciprocal301/REVIEW.md`, SHA256 `ab035cfec699f36adddff3792a0de89a30c6719e59deef3f4361198bac2bd6aa`. I read its reconstruction and nonzero-denominator argument. The S-extension conclusion is relative to that predecessor and its earlier arithmetic. The full source-to-target composition is separately assigned to agent10.

## Physical slots and the corrected cache

The new K-valued slots are

    a=v5+rho*v6, b=v7+rho*v8, c=v84+2rho*v85,
    f=v25+rho*v26, h=v27+rho*v28,
    F=v118+rho*v119, s=v120+rho*v121,
    Y=v257+2rho*v258, B=v196+2rho*v197,
    L=v236+rho*v237, z=v168+rho*v169.

The checker binds Y and B directly to predecessor rows209/210 and148/149. Those rows contain `D*c*Y+I^2-c` and `D*c*B+K^2-c`, respectively. It also binds the shared N=-1/z(H) affine expression to an unchanged primary A ratio row. This avoids inferring meanings from coordinate names.

The only old S-private consumers are rows120/121,148/149,188/189,209/210 and708-715. Exactly those rows are changed, and primary regular rows2220/2221 are added. Coordinates122/123 are removed. Every outside row and every other coordinate record is unchanged, apart from the eight declared S-slot names. In particular both root square conditions, all scalar equations including474/475 and513/514, the g0 inverse and every anchor row remain literal predecessor records.

No new coordinate is used. The corrected target has299 declared and active coordinates,279 quadratic residuals, and6630 quartic monomials. The independent checker expands every primitive integral residual square and matches the complete target polynomial.

## Reconstruction and orientation

The target retains Y=f squared, B=F squared and the primary curve. Put

    d=f-F,
    k=s*d-h,
    J=s^2-c+D(f+F),
    Q=2*s*h-c*d-1+D(2Y+fF).

The target imposes J=Q=0. With eY=Y-f squared and eB=B-F squared, direct polynomial expansion gives

    s(h-k)-1+D(Y+fF+B) = Q-J*d-D*eY+D*eB,

    k^2-F+D*F*B
      = h^2-f+D*f*Y + J*d^2-Q*d+D(f-2F)*eY+D*F*eB.

Thus the alternate curve and original divided-difference equation recover before any ratio is interpreted. The secant equation follows from the definition of k. These identities involve no division.

The reciprocal secant/tangent proof then gives the actual point difference with abscissa c and ordinate

    yR=D*h-s*(D*f+c).

The new equation is `a*b=yR`, not equality up to sign. Therefore U2-V2 is exactly the retained scalar root S=(c,a*b). The scalar point S-P and its label are unchanged. This closes the orientation issue that would remain if only the root abscissa were imposed.

The identity and tangent branches are included. If f=F, k=-h; h=0 would contradict the divided-difference equation and primary curve, so the recovered equation is the genuine tangent slope. If f=h=0, the primary point is O, and the group-law relation gives V=-S. The old-witness identity branch has s=-b/a and yR=-s*c=a*b. The other identity branch is symmetric. Both points cannot be O because Q would equal-1. The retained S square-abscissa/curve conditions exclude zero c; equivalently the source's unchanged nonzero-root argument applies.

## Ratio domains and order of soundness

Write A=1-D*B. The target alternate equation is `A*z=k`, with k reconstructed above. The identity

    A*(k*z-F)=k*(A*z-k)+(k^2-F+D*F*B)

recovers the old raw ratio once A is known nonzero. It does not license division on the finite two-torsion branch. The primary regular equation likewise forces L=0 at f=h=0 and agrees with the retained primary raw equation away from torsion.

The needed order is valid for this S extension. First recover the raw curves and exact oriented difference algebraically. All root and scalar data are already literal source data. The all-empty-contact-radical contradiction uses the unchanged root-height and scalar-anchor arguments, independently of auxiliary ratios. At a consumed successful place the raw curves imply even valuations of f and F, including negative valuations; zero leaves are simply omitted. Thus the same detector residue-class proof applies to the unchanged caches before logarithm or ratio meanings are used. Its positive low bounds make Y and B positive-valuation, so1-DY and1-DB are units at the corresponding places. They are consequently nonzero in K. Identity coordinates give the same conclusion directly. Raw alternate ratios may now be restored.

This ordering applies to all four auxiliary pairs in the assembled candidate. The unchanged A/T/Z replacements first recover their alternate ordinates and curves by the301 identities; the new S equations recover the fourth pair by the same polynomial identities and retain its explicit orientation. Hence all four curve/cache inputs are available together before applying the common successful-place argument. No pair uses a ratio conclusion to establish its curve, valuation period or root identity.

The new S auxiliary domain is E(K), except the missing reciprocal point T0, rather than2E(K). The accepted conditional auxiliary-domain proof covers all four indices, including this S index. Its doubled integral group identities kill both torsion terms and leave half-integral auxiliary free indices locally integral at every consumed odd prime. The oriented root label is still the old integer n2. Its depth-one integrality transfer and H bootstrap therefore apply to L2 along with L3,L4. The scalar depth24 argument is unchanged because its S-P point and its g variables were not altered.

This is an arithmetic extension preserving the intended input projection. It is not an assertion that every new auxiliary witness lifts to a predecessor square-root witness in2E(K).

## Completeness and signs

For a predecessor witness, recover r=V/a,J=I/a and the normalized alternate data t=Q/a,K=Kold/a from the old S biquadratic block. Use f=r squared,h=-J*r and F=t squared,k=-K*t. These are the actual old U2,V2 reciprocal coordinates. The genuine relation U2-V2=S supplies a finite secant or tangent slope s in K; a vertical slope would give the identity difference, contrary to the retained finite nonzero S. The new equations and oriented ordinate identity follow. The zero-safe regular ratios follow from the old unit-conic identities, including either identity sign. The scalar g is unchanged.

All outside witnesses stay fixed. No new real inequality, finite prime condition, H progression, or approximation choice is introduced. In particular the scalar preparation and its earlier ordering relative to the contacts remain unchanged.

The full literal sign check also passes. Negating exactly coordinates5,6,7,8,543,544,549 fixes S as a point, fixes its reciprocal auxiliary coordinates and its anchor value, and only negates complete residuals474/475 and513/514. All other residuals are fixed. Thus the old harmless root-square sign choice remains compatible with every consumer; no sign of the physical S point is silently changed.

## Sources read

The new reciprocal ordinate proof is `root-reciprocal307/PROOF.md`, SHA256 `9413e67fc1f54980932758304f561aaac418b037dd3406fcb0b87bbac929da0e`. The all-E auxiliary proposal is `resume-auxiliary-domain-20261107/PROPOSAL.md`, SHA256 `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`. I read its valuation, doubled-identity, depth and completeness argument, as well as the independent arithmetic review at `work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md`, SHA256 `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b`. The old exact S chart map is in `work/quartic-under400-20261107/10-combination/BIQUADRATIC_PROPOSAL.md`.

`check_algebra.py` and `ALGEBRA-CHECKS.json` record four universal polynomial identities. `check_slots.py` and `SLOT-CHECKS.json` record the corrected finite transport, source normalizations, complete sign action and full SOS equality. The earlier rejected-cache finding is retained separately.

The parent orientation note `work/quartic-optimization-20261107/root-ordinate299/PROOF.md`, SHA256 `69ddd3063b571c19a481272a31268ce093411c0c5519d62aef65878d52a4a7d0`, was also read. Its statements agree with the independently expanded identities and the literal orientation row. The only repair requested in this review was the alternate-cache binding described in FINDING-S299-1; no new arithmetic hypothesis or source-proof repair was supplied.
