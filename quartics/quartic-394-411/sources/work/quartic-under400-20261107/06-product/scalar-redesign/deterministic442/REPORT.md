# A deterministic correction from the retained contact square

This arithmetic replacement removes the last correction coordinate and its separate product coordinate. The resulting research system has442 total variables,441 witnesses,419 quadratic residuals and6,666 quartic monomials. The degree remains four, content one, and maximum coefficient16*3^(2^26), with unchanged fixed C=3^(2^25).

The source is the independently reviewed one-correction444 system, SHA256 `c2c60a1bed5c929eb633b654e76d401dc96fc0edd1f09eee44324740c4cde837`. The candidate SHA256 is `e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86`. Its polynomial SHA256 is `c65f1049d1af0ab5a438de3c7b73a34b6ac43cd822763adf41679102182f2bc3`.

## Replacement and domain

Keep exactly the source label and contact product

    t=2X+1,
    beta=51*t^2+2504,
    r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1).

For rational X, beta>=2504 and r>0. Replace the old choice c in {33,33033} by the explicit rational function, in fact an integer polynomial in X,

    c=r+M,  where M=4896=2^5*3^2*17.

Then c>0 and the desired scalar pole input is still b=c*r*W^2. The value of c is no longer confined to a finite set, and its prime support need not be small. The exact scope of the new p-unit assertion is proved below. No stronger assertion about all large primes is used.

The existing power coordinate600 equals r^2. Therefore

    c*r=r^2+4896*r

is affine in retained coordinates. This eliminates both the correction coordinate65 and its old normalized product slot524. The correction equation and the old product equation are deleted. Only the scalar-input definition changes.

## Unit property at every consumed contact prime

Let p>76176 lie in the same contact radical M5(beta). The fixed five-contact calculation gives odd eta=v_p(r). Its positivity is established before using c: if beta is p-integral, all five factors are integral and eta>=0. Otherwise p does not divide2*51 and

    v_p(beta)=2v_p(t),
    eta=5v_p(beta),

which is even. Hence an odd eta is positive. Since p does not divide M=4896, reduction modulo p gives

    c=r+M=M mod p,

so v_p(c)=0 at this consumed prime. The pole obstruction therefore still gives eta+2v_p(W)>0, exactly the inequality used in the reviewed depth24 proof. All its norm inequalities, the O/T0 branch analysis, the doubled-point logarithm comparison and M5(beta)^24 divisibility conclusion remain valid.

It is not asserted that c is a unit at every prime p>76176. New prime factors of c are allowed. They are disjoint from the relevant prime factors of r, because any common prime factor divides M. Extra primes in the pole predicate impose extra conditions, which completeness handles by including them in its finite preparation support. The scalar soundness conclusion only needs the contact primes just considered.

## Exact local squareclasses for integer inputs

For integral X, t is odd. The independently reviewed source calculation gives

    v2(r)=2 and r/4=1 mod8,
    v3(r)=1,
    v17(r)=0 and r=15 mod17.

For clarity, these assertions follow directly as well. At2, beta=3 modulo8, and the two even factors beta-1 and beta-2401 each have valuation one; after division by4 their product with the three odd factors is1 modulo8. At3, beta=2 modulo3, the first four contact factors are units whose product is1 modulo3, and (2beta-1)/3=34t^2+1669=1+t^2 modulo3 is nonzero. At17, beta=5, and the five residues multiply to15. The residue15 is a nonzero square modulo17.

Now c=r+4896 has exactly the same local squareclass as r at each of these fields. At2, v2(M)=5>2, and after division by4 the added term is divisible by8. Thus v2(c)=2 and c/4 has the same odd residue as r/4 modulo8. At3, v3(M)=2>1, so v3(c)=1 and c/3=r/3 modulo3. At17, v17(M)=1>0, so c is a unit with c=r modulo17. The elementary local square criteria therefore show that c/r is a square in each of Q2,Q3,Q17. Equivalently, cr is a square in all three fields.

This argument corrects every integral input with one explicit value c; it does not select independent local values. Since c,r are positive integers at such an input, cr is a positive integer as required by the scalar preparation.

## Simultaneous completeness with the enlarged support

Fix any integer X. Compute its fixed positive integers r and c=r+4896 first, then let S0 be the finite prime support of cr. S0 may contain new primes larger than76176; no bound on its cardinality or largest element is imposed.

The actual preparation argument in the frozen v11 lemma `v5:scalar32-bridge` chooses H0=[h0]P arbitrarily deep at all places over a prescribed finite support, and then R=[s]P sufficiently deep relative to H0. Its support was already allowed to contain arbitrary prime factors of the input contact product. The argument uses finiteness and fixed data before the later prime choice, not that every support prime is small. The same proof therefore applies to this S0.

Use the explicit depth24 bounds from the accepted scalar construction: for p dividing r with eta=v_p(r), make the coefficients of f(H0) have valuation at least8eta and the coefficients of z(R)/z(H0) have valuation at least24eta. For p dividing c but not r, make these coefficients have positive valuation. The preparation theorem allows these finitely many bounds simultaneously, including ramified and bad primes, as well as64 dividing h0 and the retained anchor and divisibility conditions on s.

The reviewed formulas B=(z0^2+r*z1^2)/r^32 and W=(B^2+r*q^2)/r^32 then give v_p(W)>=0 throughout S0. Also W>0 globally because r>0 and q=Norm(f(H0)) is nonzero. Thus b=crW^2 is positive and nonzero. At S0 it has nonnegative valuation; outside S0 it has even valuation. Its reduced denominator is a square. Its local squareclasses at2,3,17 are those of cr, which were proved square above. These are the exact hypotheses of the existing scalar pole-completeness lemma, so fresh pole witnesses exist.

After the scalar preparation, choose the other root labels and their height scales, and then a continuity modulus L preserving all the finitely many scalar bounds and comparison domains. Only after all this fixed data is chosen are the contact primes selected. The same simultaneous-prime theorem, coprimality assertions and primary/opposite CRT apply to the enlarged fixed L and support. The resulting shared point still satisfies the scalar integrality bounds. Hence the new primes of c do not require a new prime-pattern theorem or an exchange of quantifiers.

The scalar height exponent19/24, the retained physical anchor and order-ten height contradiction are unchanged. They yield n=beta, and the same odd-root argument then gives X integral. No point chart or input relation changes in this step.

## Actual quadratic input row

Write U=v600=r^2 and V=v525 for the retained normalized W-square coordinate. The source's actual normalized scalar input is v526. Its two old defining rows imply

    c*r*V+82479248*v526=0.

Replace them by the single row

    (U+4896*r)*V+82479248*v526=0.

The affine expression for r, including its normalization and signs, is recorded in `CERTIFICATE.json`. The new row is quadratic. The checker compares U=r^2 against the retained power row and verifies the scalar normalization from the actual old product and input equations.

For a direct algebraic check, temporarily set oldc=r+4896 and reconstruct the old normalized product slot as

    oldF=-(U+4896*r+31581660*oldc)/82479248.

The old product residual becomes (U-r^2)/4, and its old scalar-input residual becomes minus one quarter of the new input residual. These identities identify the actual semantic pole input without claiming the old finite-choice row still holds. The deletion of that row is the arithmetic replacement proved above.

## Source and evidence boundaries

The one-correction source and its arithmetic proposal are pinned in the preceding packet. The unchanged local point and logarithm domains, height theorem, anchor and simultaneous-prime statements keep the versions and qualifications recorded in the parent `CONSUMERS.json`. The new applications are the restricted unit assertion at contact primes, the explicit local correction, and extending the already arbitrary finite preparation support to include primes of c. Each is proved above. The pole-completeness hypothesis list is checked explicitly rather than inferred from a finite computation.

`verify.py` imports no producer. It checks every unchanged row, the exact deleted-coordinate consumers, the actual r and r-square definitions, the normalization identities just displayed, the new quadratic row, and every final quartic coefficient. It also cross-checks the elementary local formulas on residues. The finite pass is evidence for these identities and coefficients, not a substitute for non-author mathematical review.

All previous packets remain frozen. This candidate is a research improvement and makes no publication claim.
