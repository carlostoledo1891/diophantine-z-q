# Current-consumer interface for the proposed Lin--Yang normalization route

Author connection draft, pending review. This file does not approve Gaussian's new source derivation. It binds the intended use to combined004 TeX SHA256 ed992fd5876ad89383dc58848bab378045820cf411535dbd6045e3bea0b3a68f and keeps the abstract A001 geometry separate.

## Required and available objects

Current lines724--739 fix B=(2,-3), O=Z[i,(1+j)/2], mu=2j+ij, and the positive principal form Trd(mu^{-1}x bar(y)). The separate A001 connection matches this corrected principal form to the abstract polarized moduli definition in final Baba--Granath section2.1 and Theorem2.1. Its sixfold printed-form discrepancy remains recorded. That connection supplies the full four-element normalizer quotient and its three rational marked points; it does not need Proposition3.7, Proposition3.8 or the explicit conic map in Theorem3.10.

Final Lin--Yang Examples29--30, pp795--797, concern the unique component X6 of the quaternionic locus Q6 in the moduli space of principally polarized abelian surfaces. Thus the actual fixed principal object is on this X6; the statement is not being applied to an arbitrary polarization on the same rational quaternion module. Its Hauptmodul j6 is defined by the values 0,infinity,-16/27 at the CM points of discriminants -4,-3,-24. These are exactly the ordered points in current740--741 and1206--1207. The rational coordinate agrees by uniqueness, not by an unspecified fractional-linear change.

The new Gaussian proof retains the divisor identities, the Y1 product intersection, the Y'_5 parameterization and its CM(-24) eta value as precise published inputs, then determines the three remaining constants by substituting x^2+12x+144=0. It does not import the printed last step that assumes j6(CM(-19))=81/64. Compiler's independent decision in ly-example30-review-compiler-001 accepts that exact source/application connection under its six stated inputs. The receipt is bound in INPUTS.json. This new current-consumer record still requires its own incorporation review; the component decision does not supply whole A001/B11 or source-ancestor approval.

## Exact weighted conversion

The desired supplier output is

    s3^2/s2^3=j,  s5/(s2*s3)=1,  s6/s2^3=j+1,

with the fixed definitions in final equation(14): s2=psi4, s3=psi6, s5=2^12*3^5*chi10 and s6=2^12*3^6*chi12. On the actual finite-nonzero j-locus, the stated divisors make s2 and s3 nonzero. Choosing the weight-one scale lambda=j*s2/s3 gives the representative

    [s2,s3,s5,s6]=[j,j^2,j^3,j^3(j+1)]

in weights2,3,5,6: lambda^2*s2=j and lambda^3*s3=j^2 follow from the first ratio, and the other two entries then follow from the other ratios. No root choice or change of point is hidden in this normalization.

Final equation(13) gives

    J2=-3 chi12/chi10,
    J4=(J2^2-psi4)/24,
    J6=(-J2^3+36J2*J4+psi6)/216,
    J10=-4chi10.

Consequently the provisional tuple is

    [-(j+1), (j^2+j+1)/24, -(j^3-2j^2+1)/432,
     -j^3/(2^10*3^5)].

Rescale this tuple by -12 in weights1,2,3,5. It becomes exactly

    [12(j+1),6(j^2+j+1),4(j^3-2j^2+1),j^3].

This is the weighted representative in current857--858 and1211. The equivalent convention with weights2,4,6,10 allows a square root of -12 over C and gives the same weighted-projective point. No rational model for the genus-two curve is asserted from this geometric tuple.

Substituting this tuple into equation(13) gives psi4=144j and chi10=-j^3/4 in that common representative. Both terms of chi10^2/psi4^5 have weight20, so the normalization cancels and

    j=16*144^5*chi10^2/psi4^5.

The already independently reviewed Igusa half-characteristic substitution then supplies exactly the degree40 theta ratio and coefficient3779136 in current1230--1236. It is not used to prove the new Lin--Yang constant determination, so there is no circular use of the target j formula.

## Actual current uses and exclusions

* Lines724--741: the fixed principal datum, coarse quotient, three marked values and branch indices. The abstract geometry comes from A001; the new supplier is needed only for compatibility with the explicit weighted invariants.
* Lines821--827: the integral quotient coordinate is identified by the same ordered three sections. The new argument changes none of the tame-integral construction or branch reasoning.
* Lines829--841: J(u)=-57600F(u)^2/G(u)^6 is a chosen rational pullback to that coordinate. Its polynomial identity and contact indices are separate algebraic inputs. No explicit equation for V as a conic is used here.
* Lines851--861: the arithmetic point with j=J(u) has the exact displayed weighted invariants. Rational j and the coarse polarized quotient give the same geometric polarized point for conjugates; no fine universal object is asserted on the coarse quotient.
* Lines1206--1239: the same weighted invariants yield the theta identity and unchanged height coefficient40 and additive22. The theta/Pazuki and other height inputs remain separate.
* Bibliography23131--23135 currently still lists BG Proposition3.9. Any adopted replacement should remove that selected dependency or qualify it explicitly and cite the new local connecting proof plus final Lin--Yang Examples29--30/equations(13)--(14). No live bibliography edit is made here.

The complete main-source search for BG citations, its explicit conic expressions, h4/h6/h12, sqrt(j), -27j-16 and81/64 found no active use of Theorem3.10. The conic references elsewhere in the manuscript concern unrelated quartic constructions. The selected B11 root assembly likewise does not import that explicit conic map: its canonical generic moduli/forgetful-map input remains separate. Historical reports and unselected payloads are not retired by this bounded search.

The observed kernel in the displayed BG Proposition3.7 map, the analogous proof invocation in Proposition3.8 and their use in3.9/3.10 remain in the adverse-finding ledger. The new proposed route supplies only the required normalization; it does not assert those propositions false or silently approve their proofs.
