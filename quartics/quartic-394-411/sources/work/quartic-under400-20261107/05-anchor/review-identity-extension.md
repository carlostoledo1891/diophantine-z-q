# Independent review of identity-inclusive comparison points

Accepted at the bindings below. The arithmetic extension permits U_i=O or
V_i=O for i=1,...,4 while preserving the integer input projection. The
guarded 428-variable packet is valid. The separately checked 427-variable
packet is also valid, because the proposed global exclusion of V0=O works
without a new guard. The latter saves eight variables from its 435-variable
source.

This is an independent review of the changed chart domains, their source
applications and their exact numeric interfaces. The inherited global
arithmetic inputs remain dependencies. It is not a proof that every new
identity-branch witness lifts to the old affine chart. Soundness uses the
extended point interpretation; completeness may use the old finite points.

## Frozen bindings

| Object | SHA-256 |
|---|---|
| bl5 `00-independent470/IDENTITY_EXTENSION.md` | `d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32` |
| 02 `point-charts/primary-reciprocal/REPORT.md` | `47b935a66d73ee6e691b8010488ab41f517dd0d2d6028c703f5db060e9672918` |
| Source `10-combination/combined435-ir.json` | `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859` |
| Guarded `candidate428-ir.json` | `236e837094097aef4596a225f541347f314f7596511b75cbae09b722fa4a184d` |
| Guarded `polynomial428.json` | `e2f652a2be9c0ae1f45495a93c313cde2d4a1d70e29c2cc48061d7cac90deb24` |
| Unguarded `candidate427-ir.json` | `6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4` |
| Unguarded `polynomial427.json` | `256721badc6296a154da5d43fb9c1f67bfd2146bbb96b4b2d174113ffd9c2e84` |

The actual manuscript read was `manuscripts/quartic_v12.tex`, SHA-256
`5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.
I read the source formal-log identities and mixed-local argument, the
one-place proof at lines 11038–11068, the product-height lemma and
three-scale corollary at lines 19457–19525, and the scalar margins and
completeness passages identified by the frozen bl5 note. I also read the
actual Version 12 addition containing `lem:v12-mixed-local`, its list of
tests, and its final height consumers. The order-ten and rational-log
refinements remain those of the 435 source, not the earlier order-twelve
printed circuit. The earlier rational-log extension was independently
reviewed in this directory's `review-rational-log.md`.

Historical disposition: the source relative-quotient statement explicitly
uses nonidentity points. It cannot simply be cited unchanged at O. The
source supplies the requisite series, local bounds, detector statement
and height argument; the zero-tolerant connecting identities and the
guard-free V0 exclusion are the new arguments accepted here. No published
source was modified.

## Exact point domains and boundary values

Write K=Q(rho), rho^2=2, d0=3-rho and D=d0^2. Each unchanged odd root point
has Q=(c,ab), c=a^2, b^2=c^2-D, with a and b nonzero. The primary chart

    f=r^2,                       J^2+D*f^2=1

represents U=(1/r^2,J/r^3) if r is nonzero, and U=O if r=0. For r nonzero,
h=1/r and j=J/r^2 reconstruct the old chart. Thus the source's particular
field identification gives U in 2E(K), hence an integer label u. At r=0
the two solutions J=1 and J=-1 represent O, also in 2E(K), with u=0.

J cannot vanish. Otherwise (d0*r^2)^2=1, and taking norms after choosing
either sign would give 7*Norm(r)^2=1. That has no rational solution.

For the difference, the exact equations are

    d=c+D*r^2,
    d*g=a*J-b*r,
    u_aux=c*r+b*g,
    d*k=b*J-2*a*u_aux,
    fV=g^2,                      k*zV=-g.

At both real embeddings d>0, including at r=0. The checked polynomial
identity k^2+D*g^4=1 proves that k is also nonzero by the same norm
argument. There is therefore no exceptional undefined value of zV.

The numerator identities in bl5's standard-library checker agree with
ordinary subtraction on its open domain. They determine the same
group-law map on the smooth primary curve. The two new boundaries also
have a direct calculation:

* For r=0, g=J/a, k=-bJ/c and zV=a/b. Hence V=-Q for both signs of J.
* For g=0, aJ=br, and the two curve equations imply
  (c*r^2-1)(c+D*r^2)=0. Since the second factor is nonzero,
  r^2=1/c and U=Q. Here k=-ar=1 or -1, fV=zV=0 and V=O.

The boundaries cannot occur together. The finite equal-abscissa case
U=-Q gives the actual doubling -2Q, as supplied by the same regular
subtraction map. Thus V is always U-Q, not an independently chosen point.

The retained shared primary reciprocal is s_H=j_H/h_H=-1/z(H), and H
remains a finite nonidentity point. The changed equation

    J*L_i=r*s_H

therefore gives the actual L_i=z(U_i)/z(H), including L_i=0 at U_i=O.
Only the integer comparison labels u_i are enlarged to include zero.
The four root labels n_i remain odd and nonzero.

## The exact logarithm identities at zero

Extend the regular functions f and z at O by f(O)=z(O)=0. Set
log_E(O)=0. The formal relation f=z^2*(1-D*f^2) holds there as an identity.
The order-one f-tests therefore say that each indicated point is in the
formal group, allowing O. They do not demand an affine coordinate x(O).

Define A(Q) by the formal power series identity

    log_E(Q)=z(Q)*A(Q),           A(O)=1.

This defines A without dividing by z(O). At nonzero formal depth e>=1,
A lies in 1+p^(4e)O. At O its difference from 1 is exactly zero. Define

    T_2(Q)=G2(D*f(Q)^2)/A(Q),
    T_R(Q)=R(D*f(Q)^2)/A(Q),

where R is the already accepted rational order-40 approximation. These
are units, equal to 1 at O. Their deviations from 1 have orders at least
12 and 40 at positive-depth nonidentity points, respectively; they vanish
at O. R has numerator and denominator equal to 1 at w=0. Thus the
previous local denominator and relative-error proof includes the new
endpoint directly, with no division by a zero logarithm.

After V0 has been shown nonidentity as below, write

    H=[h]P, V0=[h-1]P,
    U_i=[u_i]P, V_i=[u_i-n_i]P.

Here h!=0,1. The formal homomorphism identity
[h]U_i=[u_i]H yields log(U_i)/log(H)=u_i/h even at U_i=O, since only
the nonzero denominator log(H) is divided out. The alternate identity is
obtained in the same way at the conjugate place, with denominator V0.
Consequently the actual approximate ratios satisfy

    L_i=(u_i/h)*A(H)/A(U_i),
    L'_i=((u_i-n_i)/(h-1))*conj(T_i(V_i)/T_R(V0)).

Every factor divided out here is a unit. These are identities with a zero
factor when u_i=0 or u_i=n_i, rather than shorthand for a quotient 0/0.
In particular V_i=O forces L'_i=0, and U_i=O forces L_i=0.

## Integrality before improved depth

At a consumed place above p>76176, at least one of the integers h,h-1
is a p-unit. Thus one of u_i/h and (u_i-n_i)/(h-1) is integral. Its
approximate ratio is integral by the exact unit identity, also if it is
zero. A positive-order cross-test then makes the other approximate
ratio integral; dividing by its unit makes the other full ratio integral.
Equivalently all valuation comparisons hold with v(0)=infinity. No
step divides by a numerator or assumes its valuation finite.

The retained f(H) order-40 test gives depth(H)>=20. If U_i is nonidentity,
integrality of L_i implies depth(U_i)>=depth(H), so the primary relative
error has order at least 80. If U_i=O, its primary error is exactly zero.
The alternate error has order 12 for i=1 and 40 for i=2,3,4, including
zero error when V_i=O. Since the full ratios are now integral, these
relative bounds are valid absolute congruences.

The current cross-test orders are 10 and 40. They therefore yield

    L_i congruent to u_i/h and to (u_i-n_i)/(h-1)

to precisely the orders consumed downstream. Multiplication by the two
integers and subtraction gives L_i congruent to n_i, without division by
either integer. This proves the required label congruences even on every
new boundary. Conjugation changes the chosen split place but not the
rational label ratios; at an inert prime it preserves the single
valuation. Both local cases are covered.

## Independent acceptance of the guard-free V0 exclusion

The former proof from a nonzero V1 numerator is unavailable once V1=O
is permitted. I do not carry that proof forward.

The guarded packet instead adds f(V0)_0*sigma=1. Its retained equation is
f(V0)_0=g0^2+2g1^2, so the guard forces g!=0 and hence V0!=O. The
following separate argument validates the unguarded packet.

Suppose V0=O in a full unguarded solution. The retained reciprocal V0
chart identifies the actual difference H-P at its boundary too, so H=P.
Explicitly, its g=0 relation a_*j_H=b_*h_H, together with the old H
curve equation, gives

    (x(H)-c_*)*(c_*x(H)+D)=0.

The second factor is positive at both real embeddings. Hence x(H)=c_*
and its ordinate is a_*b_*, so the orientation is H=P, not H=-P.

Its actual inverse abscissa is then

    f(H)=f(P)=8*(57+28rho)/1681,
    Norm(f(P))=64/1681.

Both f(P) and its inverse have coefficients integral away from 2 and 41.
Thus f(P) is a unit at every place above every consumed p>76176.

For any prime in any of the three contact radicals, the unchanged
one-place detector lemma forces all sixteen field tests at one place,
including the order-40 f(H) test. The source proof explicitly permits a
zero test D_j: its factor is 1 and its requested depth is automatic.
The lemma requires the same nonzero detector R,W,T and pole domains,
all retained. Therefore it applies even if arbitrary LP slots at a zero
denominator have not yet been interpreted. The unit f(H) cannot satisfy
its requested positive valuation. No contact radical can have a prime
factor, so all three radicals equal 1.

Apply the unchanged three-scale height corollary with N=1. This argument
uses only the four actual odd root points and the three scales, together
with the contact height theorem. It uses no comparison logarithm or
local ratio congruence. It gives

    B^2-6 < 7Hcal,

where B is the largest absolute root label. Independently the unchanged
scalar anchor and its numerical margin give

    B >= |a| > (40Hcal)^10,       Hcal>=1.

These inequalities contradict one another: 40^20 Hcal^20 is greater
than 13Hcal, which is at least 7Hcal+6. The checked source margin
10*(7+2093966)<25165823.5 is untouched by this comparison-chart change.

This proves V0!=O before using the ratio argument. Its chart and its
nonzero rational approximation then give the actual
ell0=z(V0)*R(D*f(V0)^2)!=0. For a nonidentity doubled point the argument
w lies in (0,1) at both real embeddings, where the accepted numerator
and denominator are positive. Thus every LP slot regains its unique
ratio meaning. There is no circular use of local ratio soundness in
the exclusion of its own zero denominator.

## Height targets and completeness

The product-height inputs remain Q1,...,Q4, their nonzero odd integer
labels, and their finite abscissae. Neither x(U_i) nor x(V_i) is a height
target. No x(O) enters a height expression. In particular Q4 remains
nonidentity, so the b!=0 hypothesis of the Lucas argument survives.
The scalar point S-P, its coefficient guard, its anchor, beta, and the
three scales are unchanged. After the local label congruences above,
the same order-40 Lucas contradiction and order-ten input contradiction
apply with their existing constants.

For every integer input, the established completeness construction may
still choose large h avoiding 0 and 1, and nonzero odd root labels n_i.
Then U_i=[hn_i]P and V_i=[(h-1)n_i]P are nonidentity. Their old affine
coordinates give the reciprocal chart coordinates and preserve f,z,
the approximate logarithms, and all detector inputs. The guarded packet
also gets sigma=1/f(V0)_0. Thus no new completeness or simultaneous-prime
existence input is needed. The identity points enlarge soundness's
domain; completeness does not have to use them.

## Numeric interface and reproducible checks

`review_identity_extension_check.py` binds the two reports, both candidates
and their common source. It replays the inspected physical-equation,
consumer-incidence and sum-of-squares section of 02's checker without
writing to its packet. The runtime used here has no SymPy, so it replaces
that checker's generic symbolic section with bl5's inspected and pinned
standard-library polynomial-identity checker. All checks pass.

The replay matches every old and new primary, ratio and difference
equation in the actual rational-component normalization. It checks every
removed and repurposed coordinate for outside consumers. I additionally
checked that 217 scalar, anchor, correction, height-product and detector
rows are literally unchanged, independently recomputed the full 427
sum of squares, and verified that the two numeric packets differ only
by coordinate 702 and guard row 705.

For the eight actual fused alternate-log rows, I substituted z(V_i)=0
and checked that each becomes the corresponding component of ell0*LP_i=0.
This checks the live consumers rather than obsolete standalone
logarithm-slot metadata. Since ell0 is proved nonzero, a zero numerator
cannot leave a free alternate-ratio field element. The primary zero
ratios are likewise forced by the checked J*L_i=r*s_H equations and
J!=0.

The guarded packet has 428 variables, 397 quadratic residuals and 6,290
quartic monomials. The unguarded packet has 427 variables, 396 quadratic
residuals and 6,288 quartic monomials. Both retain the same input and
fixed coefficient parameter. The unguarded table can be reproduced
exactly from the guarded table by deleting only coordinate 702 and
row 705 and recomputing the primitive sum of squares. The reports'
status wording is not used as evidence for mathematical acceptance.

Run `python -B review_identity_extension_check.py` from this directory.
The resulting `review-identity-extension-checks.json` records hashes,
counts and the actual zero-numerator consumer names. No candidate,
source, earlier report or published file was edited during this review.
