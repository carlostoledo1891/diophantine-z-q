# A positive scalar anchor with one fewer coordinate

Author: `/root/astra_bl5_models`. This is a new research component requiring independent review. It preserves the integer input projection of the accepted366 construction, rather than every old solution. In particular its completeness proof makes a new simultaneous real choice. It is not an accepted release.

The exact candidate is `candidate365-ir.json`, SHA256 `2a2823f355ac95ac935202f295b009c18bb957ba399513d0139ac07c53348a98`. Its source is `../01-elimination/s-odd366/candidate366-ir.json`, SHA256 `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56`. The source's independent review is `../03-depth/review366/REVIEW.md`, SHA256 `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2`.

The candidate has365 total variables,364 witnesses,335 quadratic residuals and6523 quartic monomials. Its coefficient table has6573 terms when powers of the fixed parameter are kept separate. Degree is four, integer content one, and maximum coefficient is `36*(6*3^(2^24)+1)^4`. The polynomial table is `polynomial365.json`, SHA256 `547c358dd679cd274aefacb983ab10b76cb0d02a0f0cd555a0405f30940261ee`.

## 1. Literal change and consumer boundary

Put L=2^24, C=3^L and delta=C/(6C+1). The old fixed parameter was C_old=3^(2^25)=C^2. Delete coordinate549, the rational inverse tau of the scalar reciprocal coefficient g0, and delete row732, `g0*tau-1=0`. Replace row504 by

    (6C+1)^2*(U^2+V^2+6W^2-3g1^2)+C^2=0.                 (A)

The private coordinates are U=55,V=56,W=57. The retained scalar reciprocal coefficients are g0=543,g1=544. Renaming the three private coordinates changes no equation. Every other coordinate object and every other residual object is unchanged. The only occurrence of the fixed parameter in the source is row504. The complete incidence of tau is rows504,732. Thus the change of fixed parameter has no hidden consumer.

The source rows513,514 still say `(c*x+D)*g=aP*j-bP*h` in K=Q(rho), rho^2=2. Here D=(3-rho)^2, P=(c,aP*bP), aP=-1+7rho/4, bP=39/8-9rho/2 and c=aP^2. The S chart still says x=h^2, j^2=x^2-D, with physical x=coordinate84+2*coordinate85*rho. No scalar logarithm, ratio, input, norm, preparation, primary, detector or height equation is changed.

Equation(A) is equivalent over Q to

    U^2+V^2+6W^2 = 3g1^2-delta^2.                        (B)

It does not encode a rational inverse of g1. Positivity will exclude its zero value, and the local argument will recover the stronger old anchor condition.

## 2. Soundness before any later arithmetic conclusion

We use the accepted366 integral-index argument, which precedes its oddness argument. The group decomposition and independent squareclasses imply S=[a]P for a nonzero integer a from the retained square-abscissa S chart alone. No Lucas, detector, height or oddness conclusion is used.

The positive left side of(B) and delta>0 imply g1 is nonzero. In fact the right side is positive: equality would imply the rational square (delta/g1)^2=3. Therefore g is nonzero. The scalar reciprocal identity identifies

    R=S-P=[s]P,  s=a-1,  f(R)=g^2,

and R is nonidentity. For x!=c this is ordinary subtraction. At S=P its numerator vanishes, which contradicts g1!=0. At S=-P it is the duplication identity g^2=f(-2P), as in the source review. The denominator c*x+D is positive at both real embeddings. Thus this argument does not use the deleted g0 guard.

Write k=v3(g1). Since v3(delta)=L, if k<L, the right side of(B) has valuation1+2k and leading unit1 modulo3. On the left, a nonzero U^2+V^2 has even3-adic valuation, because -1 is nonsquare modulo3. A nonzero6W^2 has odd valuation and leading unit2 modulo3. These two valuations cannot coincide. Hence a left side of odd valuation has leading unit2, a contradiction. The same argument includes zero summands and negative valuations. Consequently

    v3(g1)>=L.                                          (C)

At3 the curve has good reduction over F9, and P reduces to the nonzero point of order two with x=rho,y=0. If s were odd, f([s]P) would be integral with residue2rho. Since g^2=f([s]P), g is integral. The two solutions of `(g0+g1*rho)^2=2rho` in F9 have (g0,g1)=(1,1) or(2,2); in particular g1 is a unit. This contradicts(C). Hence s is even and a is odd.

For a nonzero even integer s, the already proved source lemma `lem:v12-anchor-coefficient` gives

    v3(f1([s]P))=2+2v3(s),  v3(f0([s]P))>=3+2v3(s).

Its proof also gives v3(f([s]P))=2+2v3(s). The extension at3 is unramified with integral basis1,rho, so

    min(v3(g0),v3(g1))=1+v3(s).

Since f1=2g0g1, the sum of these two valuations is2+2v3(s). Both must equal1+v3(s). In particular g0 is nonzero, and(C) gives v3(s)>=L-1. Both f coefficients are2-integral by the same source lemma. Thus

    f1/C_old belongs to Z_(2) intersect Z_(3).

The source quaternion criterion supplies rational u,v,w satisfying

    u^2+6v^2-2w^2-4C_old*w-3f1^2=0.

Set the old private witnesses to U_old=u/g0,V_old=v/g0,W_old=w/g0 and restore tau=1/g0. This is exactly the old row504, because f1=2g0g1. All other old366 rows are unchanged. We have constructed a full old366 solution with the same input. Its accepted soundness then applies, including both global height contradictions. We have not used either contradiction to establish(C), parity or the restoration map.

## 3. The new rational representation theorem application

Let g1 be rational with v3(g1)>=L and |g1|>1/10. Then A=3g1^2-delta^2 is positive, since delta<1/6 and3/100>1/36. We claim A is represented over Q by q=<1,1,6>.

At3 the two summands of A have valuations at least2L+1 and exactly2L respectively. Thus A has even valuation2L and leading unit-1. Every3-adic unit is represented by x^2+y^2: a unit congruent1 is itself a square, while for a unit congruent2 its difference from1 is a square. Hensel's lemma proves these square assertions. Scaling by3^L represents A at3.

At2, q has a nonzero isotropic vector(sqrt(-7),1,1), because -7 is1 modulo8 and hence a square in Q2. At an odd p other than3, the two subsets of Fp given by squares and -6 minus squares have sizes(p+1)/2 and therefore intersect. This gives x^2+y^2+6=0 modulo p. Its gradient has nonzero third component12, so Hensel lifts a nonzero isotropic vector. Over a field of characteristic zero a nondegenerate isotropic quadratic form contains a hyperbolic plane and represents every scalar. Thus q represents A at every p other than3. It represents A at the real place by positivity.

Apply Voight, *Quaternion algebras*, corrected published version1.0.7u, Theorem14.6.9, printed p224, to the four-variable rational quadratic form

    Q_A(U,V,W,T)=U^2+V^2+6W^2-A*T^2.

The theorem says that a quadratic form over a global field is isotropic if and only if it is isotropic at every completion. Here the global field is Q, A>0 ensures nondegeneracy, and the preceding local representations give local vectors with T=1 at every completion. A nonzero rational isotropic vector cannot have T=0, because q is positive definite over R. Dividing by T gives(B). This is a new application to a new form and consumer, not an automatic reuse of the old indefinite-anchor citation.

The inspected primary PDF is `work/theorem-application-audit-20261105/parallel-009/sieve-bounds/voight-quaternion.pdf`, SHA256 `a9316b834dbd500c52cd3a981c3205c9f4145b217042b213d23f696aee84b0f0`. The extraction `voight-223-225.txt` records printed pp223-225, including the theorem and its conventions. A future publication inventory must contain a distinct application row for Q_A, its local hypotheses and the T!=0 affine conclusion.

## 4. Completeness with the actual preparation inequalities

The new real condition on g1 is substantive. We do not claim that every old366 solution can be transformed while retaining R. Instead fix an integer input X and perform the accepted completeness construction with the following revised initial real choices. All finite-place requirements are retained.

Let G be the closure of the paired real orbit of P, let G0 be its identity component and let m=|G/G0|. The source `v5:real-progression-bridge` proves that each projection G0 to a real elliptic identity circle is onto, and that every positive progression with residue and modulus divisible by m is dense in G0. We use its open-set conclusion, with the same group and point.

Write d+=3-sqrt(2), d-=3+sqrt(2). On each identity circle, f is between0 and1/d, with maximum at the nonzero endpoint of order two. Therefore for any real square root g of f(R),

    |g+|<=1/sqrt(d+),  |g-|<=1/sqrt(d-).

The strict inequality

    1/sqrt(d+) - 1/sqrt(d-) > sqrt(2)/5

holds: after squaring it reduces to136/175>2/sqrt(7), whose squares differ by the positive integer comparison129472>122500. Surjectivity of the first projection gives a nonempty open subset of G0 on which |g+|-|g-|>sqrt(2)/5. On this subset, for either allowable signs of the two roots,

    |g1|=|g+-g-|/(2sqrt(2))>1/10.                         (D)

Exclude the inverse images of O and the nonzero points of order two at both real embeddings. These sets have measure zero by the same source proof. Choose a point T in the remaining open set, so both z-coordinates at T are finite and nonzero. The functions involved below are continuous near T.

As in the accepted preparation-zero component, fix

    beta=51(2X+1)^2+2504,
    r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1),
    c=r+4896.

For integer X, r>=4896, hence c<=2r. Let S0 contain the prime support of cr, together with2,3,17. First choose a positive h0 divisible by64,m and sufficiently divisible to meet every accepted finite preparation depth for H0=[h0]P. At p|r these include coefficient depth8*v_p(r) for f(H0); at17 they include positive coefficient depth. Among this progression choose H0 in a small real neighborhood of T.

Next choose a positive s divisible by6,m,3^(L-1), and all additional finite factors needed for the scalar ratio z(R)/z(H0). At p|r the ratio coefficient depth is at least24*v_p(r); the separate positive depths at17 and primes of c are unchanged. The source formal-subgroup argument permits any further divisibility after H0 is fixed. Among this progression choose s arbitrarily large with R=[s]P close to H0 inside the neighborhood where(D) holds. Put a=s+1. Thus both finite-depth conditions and(D) hold at these same rational points.

Choose the neighborhood small enough that the rational coefficients z0,z1 of z(R)/z(H0) have absolute values less than2. Put q=Norm(f(H0)). Since H0 is an even multiple and each real f lies in[0,1/d], we have0<q<=1/7. For the actual preparation expressions

    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q^2)/r^32,
    b=crW^2,

we obtain B<=8*r^-31, W<=65*r^-31, and

    0<b<=8450*r^-60<17.                                 (E)

This quantitative estimate replaces the old choice of both points near O. In particular there is no conflict between the lower bound(D) and the upper bound(E).

The finite preparation proof is unchanged: b has square reduced denominator, is locally square at2,3,17 and has the required lower valuations there. The accepted depth24 calculation and the separately imposed17-depth still apply. Hence the same preparation-zero lemma supplies the remaining pole witnesses.

Keep R fixed. By continuity shrink to an open neighborhood U of H0 in G0 on which all scalar functions are defined and0<b(H,R)<17. Choose the shared-index modulus sufficiently divisible to preserve the finite conditions, including m and64. Choose the remaining labels, roots and height scales before the contact primes, as in the source. Remove the finitely many comparison pole sets from U and choose a nonempty smaller open subset with compact closure. The source real-progression proof gives uniform real comparison bounds there. After the contact primes and CRT progression are chosen, its modulus and residue remain divisible by m; its positive tail meets this smaller open set. Choose the final H there. This preserves the actual preparation domain and every accepted later local and global construction.

Since s is even and v3(s)>=L-1, the coefficient calculation from Section2 gives v3(g1)>=L. Condition(D) supplies the required real inequality. Section3 now supplies the private positive-anchor witnesses. They affect no other row. All other completeness witnesses are constructed as in the source. This proves that each integer input has a full candidate365 solution, subject to independent acceptance of this new proof.

## 5. Ordinary coefficient companion

One can replace the fixed C by a15-coordinate squaring chain: c0=3^1024 and cj=c(j-1)^2 for1<=j<=14, so c14=C. Add one coordinate delta with equation(6c14+1)*delta=c14, and use(B) as the anchor row. Both equations are quadratic. The chain and delta are uniquely determined over Q, because6C+1 is nonzero. This gives381 variables, rather than the source366 companion's383. This paragraph is an exact circuit prescription; a separately frozen ordinary table would still require its own numerical check.

A dyadic alternative delta=(3/4)^L could shorten the ordinary companion by another coordinate but would require different fixed-coefficient encoding for the symbolic artifact. It is not part of this candidate.

## 6. Verification and scope

`build_positive.py` constructs the candidate from the frozen366 source. `verify_positive.py` independently checks the literal change, every outside row and coordinate, complete deleted-variable and fixed-parameter incidence, the new anchor polynomial, and the full primitive-residual sum of squares against the frozen table. Its finite residue checks supplement the valuation proof; they do not replace it. The new real construction and the Hasse-Minkowski application require mathematical review.

All inherited source qualifications remain unchanged. No new conclusion about the original Diophantine or arithmetic hypotheses is asserted. The candidate remains above the current below300 release target.
