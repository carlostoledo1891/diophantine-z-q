# Root-domain requirements for reciprocal charts

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. This note investigates the proposed enlargement of root charts from the accepted anchor-gamma313 construction. It does not approve a changed compiler, a297-variable count, or a complete construction with unrestricted roots. All frozen files remain unchanged.

The baseline IR is `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`. The arithmetic source is Version13 `manuscripts/quartic_v13.tex`, SHA256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`, including the squareclass description and odd-product height lemma around lines19444-19580. The exact anchor-root restoration is the accepted abscissa359 report in `resume-elimination-20261107/abscissa359/REPORT.md`. The later exact unscaling and gamma reuse preserve its parameter t=Fs/C+q.

## Removing b while retaining a

There is an exact conditional recovery statement. Suppose the new addition geometry has reconstructed a genuine finite point R=(c,delta) on

    delta^2=c(c^2-D), D=11-6rho, rho^2=2,

and the retained root equation is c=a^2 with a nonzero in K. Then set b=delta/a. This is a rational K-value, and b^2=c^2-D. Thus (a,b) recovers the old root chart with exactly the same point and sign. No square root is chosen in the reverse direction.

The subgroup argument is also exact. Write R=mR0+eT0+fTd, where P=2R0 and the three squareclasses epsilon=1+rho, -1, d=3-rho are independent. Since c is a nonzero square,

    [c]=[epsilon]^m[-1]^e[d]^f=1.

Its rational norm first forces m even and f=0; the real embeddings then force e=0. Hence R=nP. The point is finite, so n is nonzero. The existing3-adic anchor argument now applies to these exact integral indices and restores oddness before the product-height lemma, just as in313. Reconstructing b therefore causes no new root-label, input, parity or height obligation.

Two hypotheses in this statement are essential. The addition equations must yield an actual K-rational ordinate delta, not just an abscissa satisfying a Kummer relation on an unspecified twist. Also a=0 must be excluded: the point T0=(0,0) satisfies c=a^2=0 but cannot lift to the old b equation, because b^2=-D is impossible at the real embeddings. The geometric reviewers must check these facts on every identity, tangent and zero branch. This note alone does not certify the proposed eight-coordinate saving.

## The current anchor does not repair arbitrary roots

If a is removed too, the old product-height implication fails even for finite non-torsion roots whose free indices are already odd integers. This is more than the possibility of half-integral indices.

For each positive odd n put

    Q_n=[n]P,
    A=Q_n, T=Q_n+T0, Z=P+T0,

and keep S any fixed old prepared odd root. All four points are finite and non-torsion, their ordinates and abscissae are nonzero, and their free indices relative to P are n,n,1 and index(S). Translation by T0 gives the exact formulas

    x(Q+T0)=-D/x(Q), y(Q+T0)=D*y(Q)/x(Q)^2.

Consequently

    x(A)x(T)x(Z)x(S)=-D*x(P+T0)*x(S),

which is independent of n. Its two real values are positive: A,S have positive abscissae and T,Z have negative abscissae. Meanwhile h(x(A)) grows at least quadratically in n by the retained canonical-height bound. Thus no uniform additive constant can restore the old lower bound for the height of this product. Rescaling the free indices or proving them odd does not remove this example.

The same family obeys the existing root part of the anchor. Write X(Q) for the rho coefficient of x(Q). At3, every odd Q_n reduces to the nonzero two-torsion point with x=rho. Since D=2 modulo3, Q_n+T0 has x=2rho modulo3. Therefore both X-values are3-adic units. At2 the retained odd-multiplication calculation gives

    v2(x(Q_n)_0)=-3, v2(X(Q_n))=-1.

For x=x0+x1*rho, the rho coefficient of -D/x is

    (6x0+11x1)/(x0^2-2x1^2).

The numerator has valuation-2 and denominator-6, so v2(X(Q_n+T0))=4. Thus

    q=12(X(A)^2+X(T)^2)+108X(Z)^2

is integral at2 and3, and q=3 modulo8. Choose the old scalar preparation with Fs divisible by8 at2 and Fs/C integral at3, as allowed in the accepted gamma-anchor proof. Then t=Fs/C+q is3-integral and odd at2. The existing quaternion criterion supplies anchor witnesses. In fact the local small-u targets in the gamma reuse proof still exist, since their2-adic argument requires only odd t, not t=1 modulo8.

For n=1 the translated point is exactly

    x(P+T0)=(-2328+272rho)/1681,
    y(P+T0)=(-220080+98742rho)/68921.

The product of the three displayed A,T,Z abscissae is

    (28872-16960rho)/1681.

`check.py` verifies these identities, the curve equations, the constant product and anchor valuations for n=1,3,5,7 using rational arithmetic. The all-odd-n proof is the valuation argument above. These are genuine root and anchor-domain examples, not asserted rational zeros of the proposed enlarged full circuit. They show that the old height theorem cannot be applied to arbitrary E(K) roots on the basis of the current anchor.

## A conditional input bridge without odd free indices

There is a simple way to remove the input arithmetic's dependence on an odd label, if a future root construction supplies the other missing arguments. Replace the current input expression by

    beta=51X^2+2504.

If beta lies even in (1/2)Z, write X=a/b in lowest terms. Then b^2 divides102. Since102 is squarefree, b=1 and X is an integer. Thus equality of beta with a half-integral free index would suffice for the input conclusion. This expression is not being substituted into313, whose current root completeness still requires an odd input label.

The deterministic scalar correction can be changed at no additional gate count to c=r+9792, where

    r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1).

For integer X, beta>=2504 and r>0. At3 all factors except2beta-1 are units, and

    (2beta-1)/3=34X^2+1669 = X^2+1 modulo3,

so v3(r)=1. At17, beta=5 and r=15 modulo17, so v17(r)=0. For odd X, beta=3 modulo8 and v2(r)=2. For X=2k, only beta is even among the five factors; beta=4(51k^2+626) has valuation2 if k is odd and3 if k is even. Thus v2(r) is always2 or3.

Since9792=2^6*3^2*17, the quotient c/r=1+9792/r is a local square at2,3,17. The product cr is positive and has square local classes there. At any consumed contact prime p>76176 dividing r, the correction c is a p-unit, because it is congruent to9792. For arbitrary rational X, a negative valuation of beta at such a p is even, since51 is a unit; thus the old proof that an odd contact valuation of r is positive remains valid. These are the same scalar premises used by the accepted deterministic correction, with the2-adic lower bound on cr unchanged or stronger. Extra primes of c can be included in the original finite preparation support.

This is a conditional arithmetic replacement, requiring its own independent review before use. It does not repair the product-height failure or the possible zero free index of a torsion root.

## What remains open

Requiring positive root abscissae at both real embeddings would restrict a genuine root to ZP+{0,Td}, excluding half-index and T0 components. A restricted product-height extension may then be possible: at places with D a unit, formal roots and roots reducing to T0 cannot coexist in the allowed cyclic reduction patterns; at the bad place above7, Td translation has a bounded valuation defect. But positivity must be enforced economically, pure torsion roots must be excluded where a nonzero free label is required, and the primary/opposite completeness construction must handle the remaining Td translations. In particular, the old choices U_i=[hn_i]P,V_i=[(h-1)n_i]P have difference n_iP, not n_iP+Td. These are new obligations, not automatic consequences of the auxiliary-point enlargement.

Other possible repairs replace x by the T0-invariant x-D/x=(y/x)^2 or by x(2Q). Either changes the actual product and scale inputs and needs a fresh height proof and full gate count. Merely noting that these values exist on the curve does not make them free compiler coordinates.

The current conclusions are therefore precise: removing b is arithmetically reversible under a genuine finite lift and a nonzero a; removing a as well is not justified by the old root/anchor/height proof. No297-variable construction is accepted by this note.
