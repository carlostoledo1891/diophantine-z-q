# Bounded decimal companions for the positive scalar anchor

Author: agent05. These are new candidates requiring non-author review. They define the same integer input projection using the arithmetic inputs of accepted positive365. They are alternatives to the separate 362-variable anchor search, not additive reductions to it. The best constructed decimal table here has379 total rational variables,349 quadratic residuals,6566 quartic monomials, degree4, content1 and maximum coefficient exactly `2^8192`.

## Frozen source and candidates

The source is `work/quartic-under300-20261107/11-anchor-next/candidate365-ir.json`, SHA256 `2a2823f355ac95ac935202f295b009c18bb957ba399513d0139ac07c53348a98`. Its report SHA256 is `fa1376463fd92282a1d63cc17b42f4758a51a123f275ac02759ef2a27a49ed19`; its non-author acceptance `01-elimination/review-positive365/REVIEW.md` has SHA256 `d5c7453f95f6adf2df6e9529f542d442bdfbc7a3a854641d65b48a0de1831f54`. These paths are relative to the workspace. The published394/411 package is an ancestor, but the exact numerical source here is accepted365.

| Candidate | Added threshold coordinates | Residuals | Quartic monomials | Exact maximum coefficient |
|---|---:|---:|---:|---|
|379|14|349|6566|2^8192|
|380|15|350|6569|2^4096|
|381|16|351|6572|2^2048|

Candidate379 IR SHA256 is `c634365eb706a732da17e1d7e381c7656dfceff540fb5143af300af63d8885a7`; its full polynomial table SHA256 is `ae7687c6dda97a10c8fcd8ff539385adf62541fb514cc737686a38a3f25a8cdd`. `DYADIC-CHECKS.json` gives the other exact hashes. All coefficients are ordinary decimal integers in the generated tables. No integer remotely as large as3^(2^24) is expanded.

## Literal replacement

Let L=2^24. Replace the source's threshold `3^L/(6*3^L+1)` by

    delta=(3/4)^L.

The source fixed parameter occurs only in row504. Preserve every other source row and all365 source coordinates. Replace row504 by

    U^2+V^2+6W^2-3*g1^2+d_last^2=0,

where U,V,W,g1 are the actual coordinates55,56,57,544. For a chain of length m in{14,15,16}, put k=2^(25-m), assign IDs800 through799+m, and append

    4^k*d0-3^k=0,
    d_j-d_(j-1)^2=0       for 1<=j<m.

Every appended row and the new anchor row has degree at most two. The first equation has the unique rational solution d0=(3/4)^k; induction gives the unique values d_j=(3/4)^(k*2^j). Since k*2^(m-1)=2^24, d_last=delta. There are no free chain branches, inverse guards or new arithmetic assumptions. The chain is independent of the input and every other witness.

The full defining polynomial is the sum of squares of the primitive integer normalizations of these residuals and all unchanged source residuals. A rational zero is equivalent to simultaneous vanishing of every residual, since rational squares are nonnegative. The original input remains coordinate0 in the IR and x1 in the compact decimal text table.

## Arithmetic proof for both input directions

Only two numerical properties of the source threshold enter its soundness and representation arguments:

    v3(delta)=L,       0<delta<1/6.

The first holds because4 is a3-adic unit. The second follows from L>=8 and `(3/4)^8=6561/65536<1/6`. All other scalar, point, logarithm, detector, height and preparation rows are literally preserved.

For soundness take any full new rational solution. Its positive ternary equation is

    U^2+V^2+6W^2=3*g1^2-delta^2.                  (1)

Thus g1 is nonzero. The right side is strictly positive: equality would give the rational square `(delta/g1)^2=3`, which is impossible. This excludes the scalar identity before any height or logarithm conclusion. The unchanged S chart gives an integral index S=[a]P, and the unchanged reciprocal subtraction identity gives R=S-P=[a-1]P with f(R)=g^2. Its denominator is positive at both real embeddings. At S=P, g=0 contradicts (1); S=-P is covered by the unchanged explicit duplication identity. These are exactly the domain arguments in the accepted365 proof and do not use the chain beyond delta>0.

If v3(g1)<L, the right side of(1) has odd valuation and leading3-adic unit1. On its left U^2+V^2, when nonzero, has even valuation since-1 is nonsquare modulo3;6W^2 has odd valuation and leading unit2. Those valuations cannot tie. Therefore a left side of odd valuation has leading unit2, a contradiction. Zero summands and negative valuations are included. Hence v3(g1)>=L.

The accepted365 parity argument now applies verbatim. Odd scalar difference index would give f(R)=2*rho modulo3 and a square root g with g1 a unit, contradicting this depth. The difference index s=a-1 is nonzero and even. The accepted coefficient lemma gives v3(f1([s]P))=2+2v3(s), and the unramified square-root calculation gives v3(g0)=v3(g1)=1+v3(s). Hence g0 is nonzero and v3(s)>=L-1. In particular f1/3^(2L) is3-integral; the retained coefficient lemma supplies its2-integrality. The same quaternion criterion as accepted365 restores the old366 indefinite anchor and its g0 inverse. Every other old366 row is unchanged. The old366 soundness theorem therefore implies that the original input is an integer. No changed detector, H-domain or height inference is needed.

For completeness fix an arbitrary integer input. Use the actual simultaneous finite/real construction in Sections3–4 of the accepted365 report. It chooses the same S,R,H and remaining root points with v3(g1)>=L, |g1|>1/10, every scalar finite depth, and0<b<17. That construction does not choose anchor witnesses until these values are fixed. In particular its open-set argument near a real point with |g1|>1/10 and its bound b<=8450*r^-60<17 remain unchanged. There is no independent replacement of a p-adic point by an unrelated real point.

Set A=3*g1^2-delta^2. It is positive because3/100>1/36. At3, A has even valuation2L and unit part-1; the same Hensel argument represents it by U^2+V^2. At2 the ternary form<1,1,6> is isotropic using(sqrt(-7),1,1). At every odd prime other than3 it is isotropic by the same finite-field square-set intersection and Hensel argument from accepted365. A nondegenerate isotropic ternary form represents every scalar at those places. At the real place positivity represents A. Thus the accepted application of Hasse–Minkowski to<1,1,6,-A> supplies a nonzero rational isotropic vector. Its last coordinate cannot vanish because the first three terms form a positive definite real form. Dividing by that coordinate supplies(1). This uses the same published Voight Theorem14.6.9 input and local hypotheses; a future application inventory must record the changed A.

Append the unique rational chain values. All new equations hold and all original non-anchor witnesses are preserved. This proves that every integer input has new witnesses. Together the two arguments prove equality of rational input projections. They do not claim a witness-preserving equivalence with positive365 at arbitrary old or new fibers: the smaller real threshold can admit additional g1 values, and the soundness route deliberately restores366.

## Exact coefficient bound and reproducible checks

For379, k=2048. The largest seed residual coefficient is4^2048=2^4096. Squaring that residual contributes2^8192 to monomial d0^2. The next chain residual contains d0^2, so its square contributes d0^4 and d0^2*d1, not d0^2. No other residual contains d0. Thus the maximum monomial has only row1000 as a contributor. The complete independent expansion in `verify_dyadic.py` checks every monomial and confirms that no other combined coefficient exceeds2^8192. The same reasoning and full checks give2^4096 and2^2048 for the other two variants. This distinguishes the residual coefficient from the quartic coefficient.

Run `build_dyadic.py` followed by `verify_dyadic.py` using Python's standard library. The latter imports no producer code. It checks exact source hash, all unchanged objects, sole original fixed-parameter incidence, literal chain and anchor equations, complete coordinate incidence, full primitive SOS expansion, degree, content and the unique maximum-contributor row. Negative controls change the seed, anchor sign and an outside row; all are rejected. `quartic-379-decimal.txt` is the complete table with compact1-based indices. The computation is bounded and finishes in seconds.

The381 alternative has the same coordinate count as the previous unbuilt ordinary prescription in the365 report, with a smaller maximum coefficient. The379 and380 alternatives trade a larger but still modest decimal coefficient for fewer variables. None claims to cross the below300 target.

## Preserved unsuccessful direction

Deleting W and replacing<1,1,6> by the binary sum of two squares does not preserve the representation lemma. For this exact delta take g1=5*3^L. Modulo121, 3^L=3 and delta=119. Then A=3*g1^2-delta^2 is66 modulo121, so v11(A)=1. Since-1 is nonsquare modulo11, any nonzero rational sum of two squares has even11-adic valuation. Thus A is not represented by U^2+V^2, despite satisfying v3(g1)>=L and |g1|>1/10. This is an obstruction to that blanket local representation argument, not a claim that this particular g1 occurs on the elliptic curve. A binary-anchor reduction would need an additional proved property of the actual scalar values.
