# Five scalar correction coordinates instead of eight

This research change saves three variables. Applied to the frozen 453-variable research system, it gives 450 total variables, 449 witnesses, 427 quadratic residuals, and 6,593 quartic monomials. The content is one and the maximum coefficient remains 16*3^(2^26), with fixed C=3^(2^25). The implementation and a separate finite checker pass. Non-author mathematical review is pending.

The source is `10-combination/rational453-ir.json`, SHA256 `f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f`. The candidate `candidate450-ir.json` has SHA256 `31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6`. Its polynomial has SHA256 `24f024ca5db98e4fb9a8fa831b8fb4ced8e5baeb5a9724c0c6da3da80697b3c9`.

## The changed input label

Replace beta=2X^2+3 everywhere by

    beta=2X^2+2403.

Keep the five-contact polynomial, including every sign and numerical coefficient,

    r(beta)=beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1).

For every rational X, beta>=2403. Every factor of r is strictly positive, so r>0. In particular no contact root or inverse exception remains. At an odd prime p, if v_p(beta)<0, then v_p(beta)=2v_p(X), since 2403 is integral and 2 is a unit. Thus the negative valuation is even, as required by the existing contact calculation. For integral X, beta is a positive odd integer. Conversely, if X=u/v is in lowest terms with v>0 and beta is integral, then v^2 divides 2u^2 and hence divides 2. Consequently v=1. The input projection remains exactly integrality of X once the existing argument proves beta integral.

This is an arithmetic replacement of the input label. It is not a rational substitution X -> sqrt(X^2+1200), and no such square root is required or used. The input-square equation stays Y=X^2. In every other residual, the old formal Y is replaced by Y+1200. All occurrences of Y outside its own equation are consumers of beta or of its five-contact polynomial. The certificate lists all fifteen affected rows, including the grouped order-ten detector rows. The exact checker compares every resulting residual to this formal translation.

## The smaller correction set

Use five successive rational coordinates c1,...,c5 and put c0=1. For

    (g1,g2,g3,g4,g5)=(3,11,17,35,91),

impose

    (ci-c(i-1))*(ci-gi*c(i-1))=0     for i=1,...,5.

The first equation is (c1-1)(c1-3)=0. Over Q, induction gives ci/c(i-1) in {1,gi}. All ci are positive and nonzero. The final correction c=c5 is supported on the same small primes {3,5,7,11,13,17}; repeated factors of 7 are permitted. In particular it is a p-unit at every consumed prime p>76176. This p-unit property, rather than squarefreeness, is exactly what the scalar soundness proof uses.

For completeness these five choices suffice to make cr a square in Q2, Q3 and Q17 for every integral X. Here is a complete squareclass calculation.

At 2, an element of Q2 is a square exactly when its valuation is even and its odd unit is 1 modulo 8. At an odd prime p, it is a square exactly when its valuation is even and its unit residue is a nonzero square modulo p. Necessity follows by squaring. For sufficiency at odd p, a nonzero square root modulo p lifts one digit at a time because its derivative 2u is a unit. At 2, start with an odd square root modulo 8; if u^2 agrees modulo 2^n, adding 2^(n-1) to u toggles the next square digit, since the square changes by u*2^n modulo 2^(n+1). This constructs compatible roots at all precisions. Removing the even valuation proves the assertions over the local fields. Thus no new external squareclass theorem is needed.

For X even, write X=2k. Then beta=8k^2+2403. Both beta-1 and beta-2401 have valuation one at 2; all other factors are odd. Dividing their product by 4 gives

    r/4 = beta*(4k^2+1201)*(4k^2+1)*(32beta+343)*(2beta-1).

Modulo 8, the middle product is (4k^2+1)^2=1, and the other three factors are 3,7,5. Hence v2(r)=2 and r/4=1 modulo 8.

For X odd, write X^2=1+8t. Then beta=2405+16t. Both beta-1 and beta-2401 have valuation two. Dividing by 16 gives

    r/16 = beta*(601+4t)*(1+4t)*(32beta+343)*(2beta-1).

Modulo 8 the middle product is (1+4t)^2=1, and the other factors are 5,7,1. Hence v2(r)=4 and r/16=3 modulo 8. In both cases v2(r) is even and its unit class is either 1 or 3.

There are therefore five independent binary coordinates to correct: the Q2 unit class 1 or 3; valuation parity and unit squareclass at 3; valuation parity and unit squareclass at 17. In that order, the five positive generators have the following vectors over F2. A unit bit is zero for a square and one for a nonsquare; the Q2 bit is zero for class 1 and one for class 3.

| Generator | Q2 unit | v3 parity | Q3 unit | v17 parity | Q17 unit |
| --- | --- | --- | --- | --- | --- |
| 3 | 1 | 1 | 0 | 0 | 1 |
| 11 | 1 | 0 | 1 | 0 | 1 |
| 17 | 0 | 0 | 1 | 1 | 0 |
| 35 | 1 | 0 | 1 | 0 | 0 |
| 91 | 1 | 0 | 0 | 0 | 1 |

These vectors form a basis. Indeed the sum of the vectors for 11 and 35 is the fifth standard vector. Adding that vector to the vector for 91 gives the first. Adding the first and fifth to the vector for 3 gives the second. Adding the first to the vector for 35 gives the third, and adding the third to the vector for 17 gives the fourth.

More explicitly, for a target signature (a,b,d,e,f), one may use exponents

    epsilon3=b,
    epsilon11=a+d+e+f,
    epsilon17=e,
    epsilon35=a+f,
    epsilon91=a+b+d+e,

where every sum is in F2. Multiplying these selected generators gives c with the same signature as r. Since every squareclass has order two, cr then has zero signature at all three fields. Also cr>0 because both factors are positive. The checker independently enumerates all 32 signatures and all correction products; it does not infer simultaneous coverage from separate surjectivity at the three primes.

## Soundness and retained quantitative bounds

The scalar pole input remains the actual b=crW^2 with the same nonzero condition and the same norm tree. Every root, point chart, ratio, physical anchor, and detector order remains as in the source453 system. The source's later rational-log and tangent extensions are not altered by this transformation.

For p>76176 in the same five-contact radical M5(beta), c is a p-unit. The contact calculation is unchanged because the polynomial in beta is unchanged; the only input-specific premise it needs is the even negative valuation just proved. Write eta=v_p(r). The scalar pole obstruction gives eta+2v_p(W)>0, and eta is odd. The exact scalar norm proof of v12, `lem:v12-scalar-sound`, applies with the same q=Norm(f(H)) and the same two coefficient tests of z(R)/z(H). It yields a place where H is formal and both ratio coefficients have depth at least 32. As in that proof, z(R) may be small either near O or near T0=(0,0). One doubles R, uses the exact duplication identity to preserve its positive parameter valuation, and applies [h](2R)=[2s]H. This yields v_p(s)>=32, not an unjustified assertion that R itself is formal. Hence M5(beta)^32 divides s and h(beta)<=H*abs(s)^(19/32), with the same exponent-nineteen constant H.

All following inequalities concern beta through h(beta), not through an upper or lower bound on X. The anchor still gives the same lower bound on abs(s), so the estimates h(beta)<abs(a)/40 and log(48H)<abs(a)/40 used by the order-ten comparison remain valid with the same constants. The group indices n,a,t,b, the positive product-height scales, and the estimate B^2-6<7H*abs(N)^(19/10) remain unchanged. The local comparisons still force n=beta. The final denominator argument for beta=2X^2+2403 was proved above. No requirement beta>2500 occurs in these applications, and no such bound is used here; the required conditions are positivity, exclusion of the five contact roots, oddness for integral inputs, and the height bounds obtained from the scalar certificate.

The repeated factor 7 allowed in c has no effect on these arguments. The obstruction uses c only at p>76176. All small-prime behavior is retained in the actual pole input, not discarded by replacing c with a squarefree representative.

## Simultaneous completeness

Fix an arbitrary integer X and set n=beta=2X^2+2403. First choose the single correction c from the five-coordinate chain by the simultaneous 32-signature calculation above. Set S0 to the finite prime support of cr. This choice precedes every later arithmetic choice.

Apply the actual preparation proof in `v5:scalar32-bridge`, with this positive integer cr square at Q2,Q3,Q17. That proof uses no upper bound on c and no squarefreeness premise. It first chooses a positive h0 divisible by 64 and sufficiently deep in the formal subgroups at every place over S0. It then chooses the positive scalar index s sufficiently divisible relative to h0, sufficiently large for the physical anchor, and divisible by 6. Its original six leaf bounds suffice for the reduced scalar tree by v12. At primes dividing r, those normalized leaves are integral; at primes dividing c but not r, the nonconstant leaves vanish modulo p. Thus W is a unit at every prime of S0. In particular W is nonzero. The resulting b=crW^2 is positive, has square reduced denominator, and is square at Q2,Q3,Q17. The same exact pole-completeness lemma supplies its pole witnesses, including the allowed zero values of private witnesses.

Now put a=s+1 and choose the positive odd Lucas labels t,b_index by the source's recurrence. Since n is positive and odd, all four odd-coset root charts exist. Fix their three height scales. The existing continuity argument chooses a common modulus L preserving the scalar preparation and the rational comparison functions. These choices all occur before the contact-prime selection. The unchanged prime theorem then supplies the same coprimality statements for M_minus,M_plus,Pi,L. The same simultaneous congruences

    h=0 mod Pi^19*M_minus,
    h=1 mod M_plus,
    h=h0 mod L

are compatible. The real-progression argument chooses a sufficiently large positive h and avoids the same finite exceptional point loci. The already accepted source453 rational approximants and grouped detector circuits then receive exactly their required point domains, local depths and positive pole inputs.

This is not a claim that independent local corrections can be combined into a global elliptic point without further work. The correction is one rational integer chosen simultaneously for all three local signatures. The later elliptic and prime-pattern choices follow the same ordered preparation, continuity and CRT arguments as the source. Changing the fixed value of n and the finite support S0 does not change those theorems' quantified domains. The correction's support remains within the original allowed small-prime set.

One further consequence may be useful in later work: for every rational solution, r>0 and A=1+q^2/r>=1. Therefore W=A^2+r*Bnode^2>=1. This global nonvanishing was not needed for the three-coordinate saving and no guard is deleted on its strength here.

## Finite transport and scope

The five chain coordinates use old IDs61,...,65; IDs58,59,60 are removed. Coordinate65 remains the correction consumed by the scalar input. No outside residual consumes the other correction coordinates. The eight old correction equations are replaced by five quadratics. All other changes are precisely Y -> Y+1200 outside `inputSquare.definition`. This includes the scalar r definitions, every r consumer, and every beta consumer in the grouped order-ten detector circuit. The input equation remains literal Y=X^2, and the fixed C remains unchanged.

`build.py` produces the candidate and its primitive-integer-residual sum of squares. `verify.py` imports no producer. It independently uses binomial translation to reconstruct every changed row, checks every unchanged row and deleted-coordinate consumer, verifies all 32 simultaneous local signatures and the 2-adic residue calculation, and recomputes every quartic coefficient. `VERIFICATION.json` records the result. No giant fixed integer is expanded.

This change is disjoint from the scalar ratio fusion at the level of mathematical interfaces: the fusion remains an identity in the formal contact variable r. To compose implementations, first apply the fusion and then apply the Y translation to every retained r/beta consumer. Do not apply the old list of fifteen shifted row names mechanically to a changed IR; discover all Y consumers again. A composition must receive its own exact transport check.

The public manuscript and earlier artifacts are unchanged. Acceptance of this research candidate requires a non-author review of the changed beta application and simultaneous squareclass correction, in addition to the finite checks.
