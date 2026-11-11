# A common decay scale across the three detectors

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. No variable reduction is established in this packet. It records an explicit obstruction to the unguarded product and a mathematically viable guarded construction whose direct quadratic implementation is larger. Accepted323 and all released files are unchanged.

The frozen source is `../chain323/candidate323-ir.json`, SHA `dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd`. Its report has SHA `828cd7cfb7649b1e93cb3fbe22d1d5dc50f7d8ed1b71c20242b3634029417b15`. The inherited three-group arithmetic is `../three326/REPORT.md`, SHA `766427b1e75cf10823b0119b9d3a415a8460b49cbebb31c1b2b8483502f3baf8`, with independent review SHA `9bc208d22884b33a2777446ddd826017db173aa30b50830f944bbd941a08482c`.

Write R_j=F5(A_j*lambda), E_j=1/R_j for the three unchanged positive rational square scales. At a prime consumed by detector j, alpha=v_p(R_j) is positive and odd. This says nothing by itself about the signs of v_p(R_k) at the other two scales.

## A counterexample in the actual odd-point scale domain

`check_obstruction.py` uses the literal curve D=11-6rho, rho^2=2 and

    P=((57-28rho)/8,(-660+417rho)/32).

At p=76249 the selected split reduction has group order76064, and P has odd order2377. The script checks the opposite reduction and computes [2377]P modulo p^3 in Jacobian coordinates. The resulting x-coordinate has valuation-2 at the first place and0 at the opposite place. The opposite point is (62278,58484) modulo p. The recorded Jacobian coordinates satisfy the curve equation modulo p^3, their X is a unit, and their Z has valuation exactly1. Thus the valuation assertion is exact and does not require constructing the enormous rational point.

Take all four source root points equal to this actual odd multiple. Their product abscissa x has valuations(-8,0). Therefore both rational components x0,x1 have valuation-8: the sums and differences of the two conjugates cannot cancel their unequal valuations. The scale definitions in the323 source, up to fixed powers of2 that are units at p, give

    v(A0)=0, v(A1)=-16, v(A2)=-32.

Set lambda=p. The scaled arguments then have valuations1,-15,-31. Since the five contact constants and their nonzero differences are p-units, F5 has valuation v(t) for positive v(t), and5v(t) for negative v(t). Hence

    v(R0)=1, v(R1)=-75, v(R2)=-155,
    v(R0*R1*R2)=-229.

The prime is a required odd zero-contact prime for detector0. A proposed common inverse product has positive valuation229 there, while the old E0 has negative valuation-1. Its large powers therefore weaken, rather than enforce, the desired local comparisons. The analogous three-root product gives valuations1,-55,-115 and total-169.

This is a counterexample to an inference from the actual odd-point/scale domain. It is not asserted to satisfy the later anchor, scalar or detector rows, and is not a counterexample to the accepted quartic. A repair would have to prove an earlier additional restriction excluding this phenomenon; one cannot assume that restriction from the final integer-label conclusions.

Even a positive product valuation need not preserve each individual odd support when several R_j have odd valuation at the same prime. Repeated contact forms are allowed in the inherited completeness theorem, so pairwise-disjoint odd supports cannot be presumed either.

## A guarded common scale that does preserve the proof

Let C be a new nonzero rational parameter, write D0=1/C, and keep each E_j=1/R_j. This D0 is unrelated to the elliptic-curve constant D. Starting with the three326 sums, make the following replacements in each detector:

    E_j^158 -> D0^156 E_j^2,
    E_j^157 -> D0^156 E_j,
    E_j^39  -> D0^36 E_j^3,
    E_j^79  -> D0^76 E_j^3.

Leave every low-order weight unchanged. Add the rational term C^16*E_j^12 to G0. The old G0 occupied classes2 mod4,3 mod4,1 mod4,8 mod16,12 mod16. The new guard occupies its unused class4 mod16. Thus the unique-minimum proof remains valid for arbitrary valuations of C, without first assuming the guard's conclusion. All large common exponents above are divisible by4, so they preserve the relevant high/middle residue classes.

At a consumed prime, let c=v_p(C), alpha=v_p(R_j)>0 odd, and let lambda_p be the maximum valuation of the product W over its places. The unchanged pole equation and trace argument give lambda_p>-alpha/2, with every term in every group above this bound at one common place. The added rational term therefore gives

    16c-12alpha > -alpha/2,
    c > 23alpha/32 >= 23/32,

so c>=1. The modified high terms at that same place then yield, for example,

    4v(H1) > 156c+1.5alpha >=157.5,
    4v(H4) > 156c+0.5alpha >=156.5,
    4v(M0) > 36c+2.5alpha >=38.5,
    2v(H0) > 76c+2.5alpha >=78.5.

These force the same high order40, middle order10 and H0 order40, using its already justified even valuation. P2 has the same stronger order as in326. All low-order tests are literally unchanged. In particular, the fixed-unit T0 test still excludes the pre-H exceptional branches before any height conclusion. Every downstream arithmetic application is therefore restored in the same order as326. This construction does not use any valuation of R_k for k different from j.

For completeness use the original Pi^19 progression and all original test-depth bounds. After the finite contact-prime set is fixed, choose C with valuation exactly1 at every selected contact prime, valuation0 at2,3,17, and real value in(1,2). This choice exists by elementary CRT: take a sufficiently large positive denominator N congruent1 modulo the product of the required prime-square moduli, then choose a numerator in(N,2N) in the prescribed residue class. The interval eventually contains such an integer. This gives the desired exact valuations and a uniform compact real interval without enlarging any point index or requiring disjoint contact supports.

At a successful selected place c=alpha=1, all four new weights have exactly the old valuations158,157,39,79, and the guard term has valuation4. Thus the old positive margins and trace residue1 or2 remain valid. At the other place the same residue argument applies. At2,3,17, C and D0 are units, while every E_j exponent is positive, so increasing the old preparatory divisibility again sends all nonconstant terms to zero. At real embeddings C in(1,2) gives uniformly bounded positive common factors. Every remaining E_j exponent is positive, so the old large-lambda argument sends the groups to1 and the poles to0 through positive values. These uniform bounds can be fixed before prime selection, and C can be chosen afterward in the prescribed interval. New primes in the numerator or denominator of C cause no odd-denominator problem where v(R_j) is even, since the pole's other factors remain squares.

This proves a viable guarded source-level construction, but does not show it is economical.

## The direct quadratic count is336, not a saving

The four high/middle expressions above cannot simply be inserted as products of a common power, a local power and a field leaf; that would be cubic. Their combined scalar weights must be stored or an equivalent extra multiplication introduced.

A ten-coordinate common chain suffices. Its coordinates are

    D0, D0^2, Q=D0^4, Q2=Q^2, Q4=Q^4,
    J=Q^-1, G=Q^-4, A=Q^9, B=Q^19, H=Q^39.

Use successive square equations, Q*J=1, Q4*G=1,

    A*J=Q4^2, B*J=A^2, H*J=B^2.

The outputs are G=C^16, A=D0^36, B=D0^76, H=D0^156. The inverse equations force the required nonzero domain. Each definition is quadratic.

Each detector needs E_j and the five local powers E_j^2,E_j^3,E_j^4,E_j^8,E_j^12, plus four stored combined weights. This is ten scalar coordinates instead of the nine used in323. The guard product G*E_j^12 is directly quadratic in the real component of G0 and needs no extra field coordinate. Thus this direct realization costs

    323 + 10 common coordinates + 3*(10-9) = 336.

This is an explicit circuit upper count, not a compiled/independently accepted336 artifact. It is included to expose the cost that a purely symbolic common-factor count misses. No reduction is claimed.

## A cheaper-looking pole guard fails to preserve the low tests

One can replace the pole by B_new=B_old*C^2/R_j^2. At a consumed prime its valuation is2c-alpha-2v(T). The unique-minimum bound lambda_p<=0 would then force c>alpha/2, without adding the guard leaf. But its common-place conclusion is only lambda_p>alpha/2-c. If c is large, unchanged low terms may have negative valuation and still satisfy this bound. For alpha=1,c=100, a unit T0 gives its term valuation-8, compatible with lambda_p>-99.5. Hence the old low-formality and pre-H exclusion do not follow from that argument.

All low terms would need a separate redesign. Reweighting them with C can restore valuation inequalities, but changes their residue classes, completeness margins and quadratic multiplication cost. No smaller complete circuit from this alternative has been established here.

The conclusion is scoped: unguarded product sharing fails in the actual point-scale domain; guarded sharing is arithmetically possible, but the explicit quadratic construction above is larger. More economical guards or a different simultaneous common-place argument remain open. The accepted323 packet is unchanged.
