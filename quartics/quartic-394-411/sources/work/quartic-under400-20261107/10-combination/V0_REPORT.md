# Reciprocal V0 chart

Research candidate, requiring independent mathematical review. The frozen input is the published 498-variable IR with SHA256 `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`. The candidate `v0-493-ir.json` has SHA256 `09a3b7255cc50441945b5bcfd4eb1fdcb5def3fff95d06cd4255d364c41c29b9`.

## Formulas and domain

Work in K=Q(sqrt(2)), with D=11-6sqrt(2), a=-1+7sqrt(2)/4, b=39/8-9sqrt(2)/2, and c=a^2. Thus b^2=c^2-D. The retained incoming H coordinates satisfy x=h^2 and j^2=h^4-D. Put d=cx+D, N=aj-bh and T=-2Dh-abj+2Db g. Replace the old slope circuit for V0=H-P by

    d g = N,
    f = g^2,
    T ell0 + a N G0 = 0.

Each displayed equation is a field equation with two rational component rows. G0 is the retained logarithm polynomial output. The third equation is quadratic because T,N,G0 are affine in stored coordinates. Remove seven old private coordinates and add two g coordinates, saving five.

The constant a is nonzero. In both real embeddings, d=(ah)^2+(3-sqrt(2))^2 is strictly positive. Define k=T/(ad). Substituting dg=N gives

    k = M/d^2,
    M = -2aDh(x+c)-bj(cx-D).

The generic identities checked by `verify_v0.py` prove k^2+Dg^4=1 and the usual reciprocal addition formulas for H-P whenever x differs from c. The same formulas at H=-P give the actual doubling -2P. The potentially invalid identity branch H=P has g=0. More generally g=0 forces k^2=1, so T is nonzero and the new logarithm equation forces ell0=0.

That branch is excluded by the retained V1 logarithm ratio. V1 is unchanged, hence is a genuine nonidentity doubled point under the inherited chart hypotheses. Its z coordinate is nonzero, and its w=D f^2 lies strictly between zero and one in both real embeddings. The retained equation is

    ell0 LP1 = z(V1) G2(w),
    G2(w)=1-2w/5-2w^2/15.

On this interval G2 is at least 7/15. The right side is therefore nonzero, so ell0 is nonzero. This excludes g=0 and makes V0 a genuine nonidentity difference point. Since k is also nonzero for a genuine affine point on this chart, the new logarithm equation gives ell0=-(g/k)G0, the required value.

The proof uses the retained V1 chart and its degree-two logarithm. It does not assume a new nonzero guard on g, T, or ell0. The inherited source-level real-chart and doubled-point facts are essential inputs, not consequences of finite polynomial expansion alone.

## Completeness and projection

Every original witness provides the actual H-P reciprocal coordinates g,k. These satisfy the new rows and preserve f, G0 and ell0. This gives old-to-new completeness. Conversely, the argument above assigns actual V0=H-P to every new witness and preserves all downstream semantic values. The new system may admit H=-P, where the old unequal-x slope chart was unavailable. Accordingly this is an arithmetic chart extension with unchanged downstream point semantics; it is not a bijection of old private slope witnesses.

The only deleted-coordinate consumers are the seven deleted private rows and the four replaced component rows for f and ell0. No other row changes. The source values are read from the pinned mixed-depth 519 IR, whose coordinate semantics are unchanged at H, f(V0), ell0 and G0.

## Finite verification

`verify_v0.py` imports no producer. It checks all changed and unchanged rows, private incidence, the exact retained V1 ratio and G2 output, four generic reciprocal identities in K[h,j]/(j^2-h^4+D), the compressed numerator identity, and every coefficient of the full sum of squares. The candidate has 493 total variables, 492 witnesses, 462 quadratic residuals and 24,567 quartic monomials. Its content is one and its maximum coefficient is exactly 16*3^(2^26). The fixed parameter remains C=3^(2^25).

The pending rational-log replacement changes only G0's evaluation, so the final logarithm equation can consume that output unchanged. The nonzero branch argument depends on the unchanged G2 at V1. The five comparison-guard proposal overlaps this change at V0; only its V1 through V4 changes should be combined with this candidate.
