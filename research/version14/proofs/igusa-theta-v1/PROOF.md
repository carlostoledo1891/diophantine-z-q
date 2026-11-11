# Igusa's theta identities at the actual genus-two point

This is an authored source substitution and connecting proof, pending independent
review. It replaces the LNY publisher-proof citation for the two theta identities.
It does not authenticate a final LNY edition or replace the other height inputs.

## 1. Fixed objects and coordinate conventions

Let (A,L) be the principally polarized abelian surface in the current manuscript,
with its already chosen principal polarization, and choose a compatible symplectic
homology basis. Write its complex period point as tau in the genus-two Siegel
upper half-space. For a,b in {0,1}^2 put m=(a/2,b/2) and define

    z_m = theta_m(tau,0)
        = sum over n in Z^2 of exp(pi*i*(n+a/2)^t*tau*(n+a/2)
                                    + pi*i*(n+a/2)^t*b).

The positive definite imaginary part gives absolute convergence. These are
Igusa's theta constants: his printed p833 defines theta_m(tau,z) by the series
with e(u)=exp(2*pi*i*u), first term (n+m')^t*tau*(n+m')/2 and second term
(n+m')^t*(z+m''); p834 sets z=0. In particular his characteristic is the
half-integral vector m, whereas LNY p4 labels the same series by the integral
vector (a,b) and puts its halves into the exponent. This is a reindexing, not
a rescaling of tau or the constants. We fix the representatives 0 and1/2 used
by Igusa on p848, so no choice of integer lift remains.

Igusa p834 gives parity (-1)^(a dot b). It can also be checked directly by
reindexing n as -n-a: z_m=(-1)^(a dot b) z_m. Thus the six odd constants vanish.
There are ten even characteristics: a=0 permits all four b, and each of the
three nonzero a permits two b. No assertion that every even constant is
nonzero at every genus-two point is used.

## 2. The exact published identities

Igusa, Modular forms and projective invariants, American Journal of Mathematics
89(3),1967,817-855, p848, gives in this genus-two convention

    2^2 psi_4 = sum over even m of z_m^8,
    -2^14 chi_10 = product over even m of z_m^2.

The minus sign and exponents are visible in the final journal scan. These are
the same two formulas stated in LNY's proof p4, which itself cites this exact
page of Igusa. The parity convention is on pp833-834; the count is also given
in general on p819. The discussion on p850 explicitly identifies the product
of all even theta constants and notes that its square is required at genus2.
We do not apply the genus-at-least-three conclusion of Lemma10 to genus2.

The psi_4 and chi_10 names match the Igusa forms in the current Lin-Yang
application. Final Lin-Yang p793, equation(13), cites this same Igusa1967 paper
as reference20 and states J4=(J2^2-psi4)/24 and J10=-4chi10. Thus there is no
unverified conversion between independently scaled cusp forms in this join.

## 3. The unchanged rational coordinate

For the same quaternionic moduli point the separately retained Lin-Yang
parameterization supplies, in one common weighted representative,

    J2=12(j+1), J4=6(j^2+j+1), J10=j^3.

Consequently psi4=144j and chi10=-j^3/4. On the actual open set j finite and
nonzero, psi4 is nonzero and

    j = 16*144^5 * chi10^2/psi4^5
      = 3779136 * (product over even m of z_m)^4
                  / (sum over even m of z_m^8)^5.

Indeed 16*144^5*2^(-28+10)=2^6*3^10=3779136. Both numerator and denominator
in the first ratio have modular weight20. In the last ratio both homogeneous
polynomials have degree40. Common projective rescaling cancels in either
description. The published Lin-Yang pullback factor for weight k therefore
also cancels. All identities use the same point and same period matrix.

## 4. Connection to the theta height

The final published Pazuki paper, Theta height and Faltings height, p25, defines
theta_(m1,m2)(tau,z) by exactly the same exponential series. Its Section2.3.4,
Definition2.6 and following discussion on pp30-31 identify the coordinates
of Theta(0) as theta_(m1,m2)(tau,0) for m1,m2 in
{0,1/r,...,(r-1)/r}^g. For r=2 and g=2 these are exactly our sixteen half-
characteristics. They are not the alternative theta_(m,0)(r^2 tau,0) coordinates
mentioned there, and we do not silently identify the two coordinate systems.

Pazuki's coordinates are the raw complex theta values as projective coordinates,
not the individual analytic norms printed on p25. The common analytic factor
at zero would cancel in a projective point, but no such factor is needed here.
The six odd entries are zero by Section1. Appending them to the ten even entries
does not change the local maximum norm or Euclidean norm. The nonzero projective
point and algebraicity of its coordinate ratios are the published Pazuki input
on p30. Its Euclidean projective height dominates the maximum-norm projective
height used in the manuscript. This source substitution does not reprove the
later comparison with Faltings height or its constants.

For clarity, the elementary polynomial estimate is also unchanged. The numerator
has coefficient norm3779136, the denominator has coefficient norm10^5. At every
archimedean place each evaluated polynomial is bounded by its coefficient norm
times the fortieth power of the maximum coordinate norm; the corresponding
nonarchimedean bound has coefficient norm at most1. Summing the local inequalities
gives h(j)<=40h([z_m])+log(3779136), hence the displayed weaker bound with +22.
Nonvanishing of the denominator follows from psi4=144j, not from a blanket claim
about even theta constants.

## 5. Scope and required adoption

The actual replaced use is the LNY citation at current925967 lines1154-1156 and
its inherited normalization in A017. The Lin-Yang inputs, the principal-polarized
surface, and Pazuki's theta-height theorem remain separate premises. The proposed
manuscript edit supplies the half-characteristic convention and cites Igusa
directly. A companion bibliography edit removes the sole active LNY citation
and supplies Igusa plus a link to this connecting proof. Historical LNY evidence
and its unresolved final-edition comparison remain preserved. The available
published input now supplies exactly the two needed identities; no final LNY
authentication, full Igusa proof audit or release acceptance is claimed.
