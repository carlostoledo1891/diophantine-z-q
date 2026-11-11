# A common scale determined by a private anchor witness

This candidate has313 total variables,283 quadratic residuals and6073 quartic monomials. It saves one variable from accepted sparse-shared314. The new step is a completeness construction that couples the common detector scale to a private anchor witness. It is not an exact equivalence on arbitrary old witness fibers. Independent arithmetic and structural review are required.

Circuit and original coupling proposal: `/root/astra_quartic_opt05_anchor`. The constructive approximation proof is contributed by `/root/astra_quartic_opt03_depth`, so that contribution is not independent acceptance. The original exploratory note is preserved in the parent directory.

## Frozen algebraic candidate

The source is `work/quartic-under300-20261107/10-combination/sparse-shared314/candidate314-ir.json`, SHA256 `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382`. Its exact-transport review is `resume-review-transports314-20261107/REVIEW.md`, SHA256 `abc780609bf1b9a65100608eac4bec936f8844ea9b91fdeed973b24241c0efa7`. The underlying shared314 arithmetic and compiler reviews remain separate dependencies.

The new IR is `candidate313-ir.json`, SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`. The complete polynomial is `polynomial313.json`, SHA256 `d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d`. Only rows919,930,941,2000,2005 change. Coordinate1100 is removed; coordinates1101 through1105 acquire the meanings specified below. Every other coordinate and row object is retained, except for those five coordinate names and the top-level status.

The source private anchor has u=v55, v=v56, w=v57, T=v903 and fixed C=3^(2^25). Its unchanged equations are

    u^2+6v^2-2w^2-4Cw-3T^2=0,
    T=2g0*g1+Cq,
    q=48v83^2+48v87^2+432v89^2.

Here g0=v543 and g1=v544. Put gamma=1/u. Replace the nine common-scale coordinates with eight coordinates having these forced values:

| Coordinate | Value |
| --- | --- |
|1101|u^2|
|1102|u^4|
|1103|u^8|
|1104|u^16|
|1105|u^-16=gamma^16|
|1106|u^-40=gamma^40|
|1107|u^-80=gamma^80|
|1108|u^-160=gamma^160|

The first four are successive squares. The remaining equations are

    v1104*v1105=1,
    v1103*v1106=v1105^2,
    v1107=v1106^2,
    v1108=v1107^2.

The three G0 guard terms use1105 in place of1104. No other consumer changes. In particular the scaled high/middle/P2/P3/P4 values, promoted P1 input, local R/E powers, product, norm, trace, pole and scalar equations remain identical.

## Soundness and exceptional cases

The inverse equation forces u nonzero, since v1104=u^16. All eight helpers are then uniquely determined by u. Reconstruct the source gamma as1/u, its powers2,4,8,16 in old1101 through1104, and its inverse sixteenth power in old1105. Keep1106 through1108 and all non-chain coordinates fixed. The reconstructed source guard is exactly the new guard, because old gamma^16 equals new1105. Every source equation follows.

`verify.py` checks this statement on every row after substituting the old and new chain coordinates as Laurent monomials in u. It also checks the literal chain equations that justify those substitutions, the complete incidence of removed1100 and repurposed1101 through1105, and the unchanged objects. Thus a new rational solution maps to an accepted sparse-shared314 solution with the same input, without assuming any group-law, valuation or index interpretation first. In particular the old soundness proof supplies all original root-parity, height and integrality conclusions. The new system does not contain a u=0 branch.

## Completeness construction to be independently reviewed

The remaining obligation is to select private anchor witnesses jointly with the common scale. Write t=T/C, z=w+C and N=3T^2-2C^2. The unchanged anchor is

    u^2+6v^2-2z^2=N.

N is nonzero because t is rational and t^2 cannot equal2/3. The accepted quaternion criterion supplies a rational point once t is integral at2 and3. The previously selected scalar and odd-root data have that property.

Require the scalar coefficient Fs=2g0*g1 to lie in8Z2 when selecting the original scalar point. Version13 lines21430 through21439 explicitly allow arbitrary further finite depths before choosing that scalar point in the same dense positive real progression. No extra congruence is imposed after selecting the contact primes. The accepted odd-root coefficient lemma gives v2(X_i)=-1, with X_A=2v83, X_T=2v87, X_Z=2v89. Hence q=3(2X_A)^2+3(2X_T)^2+27(2X_Z)^2 is1 modulo8. Since C is odd, t is odd.

At the three small primes select exact u valuations nu_p, with nu2 and nu17 at least1 and nu3>2^25, enlarged further to meet the old uniform small-prime estimates. Explicit local points for u=p^nu are:

    p=2:  v=T/2, z=(C/2)*sqrt(4-3t^2+2(u/C)^2);
    p=3:  v=0,   z=C*sqrt(1-3t^2/2+(u/C)^2/2);
    p=17: v=T/sqrt(2), z=C*sqrt(1+u^2/(2C^2)).

The first radicand is1 modulo8. The other two are1 modulo their odd prime;2 is a square in Q17. These are local points on the exact displayed quadric, with nonzero z. Each desired valuation condition describes an open subset.

Choose contact primes beyond the denominators of the already fixed T, as well as every original finite exclusion. At each such p put u=p^-1. For V=pv and Z=pz the remaining equation is

    6V^2-2Z^2=p^2N-1.

Modulo p its right side is-1. The nondegenerate binary form represents every nonzero residue: it is either a split product or a nonzero scalar multiple of the norm from Fp^2. A nonzero solution is nonsingular, so it lifts. Thus every contact prime has an open set of local quadric points with v_p(u)=-1. A repeated contact prime gives the same requirement once.

At the real place require1/(2lambda)<u<1/lambda. Any u in this interval admits a real point by taking v sufficiently large and solving for z. Consequently gamma/lambda lies in(1,2).

The complete constructive proof is `work/quartic-optimization-20261107/resume-depth-20261107/anchor313/PROOF.md`, SHA256 `ba0b08bf1d155d22d152e1dd2ec23f1b264951663cb53e90f1ed3da214b271a1`. I read that exact note before binding it here. Its argument uses a fixed rational anchor point P supplied by the accepted quaternion criterion and the rational map

    Phi(d)=P-2B(P,d)d/Q(d),

where B is the polar form of Q and Q(d) is nonzero. The note proves that every nonempty local target open set meets the complement of the tangent section, hence is reached by this one map. At a tangent-section point X it uses an explicit curve sqrt(1-s^2Q(h)/N)X+sh to leave that section while staying in the chosen open set. It then gives a coordinatewise integer CRT construction with a large denominator congruent to1 modulo the finite precision modulus, proving simultaneous finite approximation and real density. No general weak-approximation theorem for quadrics is assumed. The direction parameters occur only in the existence proof and are not additional quartic coordinates.

The order is fixed scalar preparation with extra2-adic depth; fixed scalar, roots, T and a rational anchor basepoint; fixed finite neighborhoods, denominator depths and uniform real bounds; contact primes avoiding the fixed T denominators; the original lambda; the new private anchor point; then the final H in the old Pi19/continuity progression and real neighborhood. The scalar and root coordinates, hence T and q, do not depend on the final H. All previously required estimates are uniform for gamma/lambda in(1,2) and the specified exact finite valuations. The newly selected private anchor values do not enter those bounds. Extra denominator primes are covered by the unchanged even-parity pole-support argument of shared314.

After selecting this point, set the eight helpers to their unique rational values and all other coordinates by the shared314 completeness construction using gamma=1/u. This proves existence for each integer input. Together with the preceding reverse map it proves equality of input projections, while making no claim that every old choice of private anchor and gamma can be transported unchanged.

## Finite table and scope

The producer writes the exact rational IR and the full primitive-residual sum of squares with C kept symbolic. The separate verifier imports no producer. It reconstructs every coefficient, verifies all313 coordinates occur and every residual is quadratic, and checks degree four and content one. The table has6076 coefficient-power entries and6073 monomials after specialization. The maximum remains186624C^2+64. The coefficient bounds used for the accepted source still hold literally: all other C^2 leading coefficients are smaller, C-linear coefficients are at most1728 in absolute value, and C-independent coefficients have fewer than2048 bits.

The old u^4 monomial receives the square contribution of the new first chain equation, while the removed gamma coordinate no longer contributes its own monomials. These collisions are included in the actual count. No ordinary companion is asserted. No production file or accepted predecessor was edited, and313 remains above the publication threshold.
