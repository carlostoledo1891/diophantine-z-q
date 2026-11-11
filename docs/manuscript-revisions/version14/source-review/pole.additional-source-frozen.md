# Independent refutation-first review of pole completeness

4 November 2026. Reviewer: astra_moving_filter_audit.

## 1. Finding, target, and boundary

I found no new gap in the conditional implication RC => PC for the exact saved pole template. The proof covers every rational B in the stated PC domain, allows d=1 and theta=1, retains the actual nonzero cross-symbols, and uses the same finite multiplier m in both curve constructions. The full Selmer corank is proved to equal one before either application of RC. Finiteness of Sha is used only after RC and the forward analytic-rank-one theorem.

This conclusion does not prove RC, PC unconditionally, the height and prime-selection inputs to the multiplication predicate, or the global ordinary-integer theorem. In particular, it is not a new acceptance of the raw broad pointwise-converse claim. That claim at `work/parity-frozen-4eaee875.tex` lines 457-494 is excluded. The narrower replacement at current V4d02 lines 265-289 is sufficient, for the reasons below.

The reviewed producer report is `work/astra-final-pole-completeness-review-001/REPORT.txt`, SHA256 `7f496b180185b48490b691f8c9a113fafbe298c76647d6a227869ca3ebc9e582`. I read it completely and verified all 17 of its source pins. Its verdict and computational successes are not premises here. I directly read the current mathematical text, the raw local and simultaneous-matrix proofs, the saved template's complete 107-node array, and the primary statements identified in section 8. I wrote and ran a separate data-only checker without importing the producer's checker or a production builder.

Notation: V02 is `review-v4d/02-height-pole-multiplication.tex`, V03 is `review-v4d/03-restricted-converse.tex`, and P is the raw parity file just named. The current V02 and V03 bytes match their V4b versions. All exact paths, roles, read ranges, sizes, and hashes are in SOURCE_PINS.json. The algebraic parameter theta in this report is the positive squarefree representative of H; it is different from the multiplication predicate's rational trace Theta.

## 2. Literal polynomial and the one multiplier

V02:168-181 and `outputs/multiplication-certificate.js`:22-33 define the eleven-witness expression

    m=(1-2b0)(1+b1)(1+2b2)(1+4b3)(1+6b4)(1+12b5),
    A=mB, H=A(A-B^2)=A^2(1-B/m),
    T1=A(A-e)(A+3e), T2=A(Az^2-eH)(Az^2+3eH),
    Q=B[sum_i (b_i^2-b_i)^2+(eHzw-1)^2+(r1^2-T1)^2+(r2^2-T2)^2].

The actual saved `outputs/ordinary-integer-definition.json` template `library.templates[5]` has parameterCount=1, witnessCount=11, root=106. The direct node trace gives m at 35, A at 36, H at 40, Az^2 at 42, T1 at 49, T2 at 56, Q at 102, zero at 103, and the square of Q-0 at 106. Thus the actual root is Q^2. Squaring preserves the rational zero set; it does not preserve the displayed degree 75, which becomes 150. No polynomial-equality or degree-75 claim about the saved root is needed here.

Because PC assumes B>0, Q^2=0 is equivalent to each rational square inside Q vanishing. The bits must be in {0,1}; they choose precisely a signed divisor of 2730. The guard forces e,H,z nonzero. The two other equations give points (A,r1) on E_e and (Az^2,zr2) on E_{eH}. The leading factor in T2 is A, not Az^2: multiplying its equation by z^2 is what gives the curve equation for the second point. Both this factor and the second ordinate are essential in the witness construction below.

The signed divisors represent all real, Q_2, and Q_3 squareclass signatures. After choosing -1,2,3 for sign and the two valuation parities, the unit bits of 5,7,13 are respectively (0,1,1),(1,0,0),(0,1,0) in the two Q_2 unit coordinates and the Q_3 unit coordinate. These three vectors form a basis. Their corrections change neither sign nor valuation parity. This proves the asserted simultaneous choice, and the separate checker also finds all 64 signatures distinctly.

For every admissible B choose m with A positive, square in Q_2, and in the nonsquare unit class in Q_3. Since B>0, m is positive and at least 1. Since 0<B<1/2, 0<B/m<1/2. For each p in S0={2,3,5,7,13}, v_p(m)<=1 and v_p(B)>=4, hence v_p(B/m)>=3. Thus 1-B/m is positive and a local square at S0; the bound three supplies the needed 1 mod 8 at two. H is positive and locally square at all S0. These choices use no elliptic-curve theorem.

Let beta and theta be the positive squarefree representatives of A and H. Local squareclasses now give beta=1 mod 8, beta=2 mod 3, and theta=1 mod 8, theta=1 mod 3. Therefore beta=17 mod 24, theta=1 mod 24, neither is divisible by 2 or 3, and beta>1. Theta=1 remains possible.

Here is the full cross-square argument, which is needed for the matrices. If q divides beta and q is in S0, H is already locally square there. Otherwise m is a q-unit and v_q(B) is odd. The square reduced denominator excludes a negative odd valuation, so v_q(B)>0. Then 1-B/m is a square unit, hence H is locally square at q. This proves disjointness of beta and theta and one direction of the cross condition.

Conversely, if q divides theta then q is outside S0. Put k=v_q(B)=v_q(A). If k>0, H=A^2(1-B/m) has valuation 2k. If k<0, it has valuation 3k, which is even because every negative valuation of B is even. Both contradict q dividing theta. Thus k=0; the odd valuation of H comes from cancellation in 1-B/m. Hence B/m=1 mod q, and A=m^2(B/m) is a local square at q. These are the exact mutual-square statements needed from P:170-216, now proved for the present B and H rather than for an unrelated preparation parameter.

## 3. The local descent and its normalization

Take l>0 squarefree, prime to 6, l=3 mod 4 and l=2 mod 3. Use Kummer coordinates (x+3l,x-l). Silverman X.1.4, printed page 315, directly supplies the split-cubic Kummer map with root replacements. Set e1=-3l,e2=l,e3=0 there. The replacement at l has squareclasses (l,1), and that at -3l has (3,-l); the source's quotient and product formulas differ by squares. Denote these torsion images tau1 and tau2. They are independent, since l is nonsquare and the second coordinate of tau2 is negative. The other two torsion images are the identity and their product.

The local claims in P:328-374 can be proved without imposing a reduction type. At an odd q choose an open formal subgroup on which multiplication by 2 is invertible. The finite quotient G then gives E(Q_q)/2 of the same cardinality as E(Q_q)[2], namely four: lifting a 2-torsion element of G can be corrected inside the formal subgroup. At q not dividing 3l, the roots are distinct modulo q. A negative x-valuation is even by the three-factor equation; for integral x at most one factor has positive valuation, and its valuation is even. Root replacements are units. Thus the four-element Kummer image is exactly the four unramified squareclass pairs. At q|l, tau1 and tau2 have independent valuation pairs (1,0),(0,1), so they generate the whole local image. At 3, their first coordinates span Q_3^*/Q_3^{*2} while their second coordinates are squares, giving exactly that product with {1}.

At two, only a necessary valuation condition is used. For negative v_2(x), the cubic equation makes it even. If x is even integral, the selected factors are units. If x-l=2u with u odd, division by four gives (y/2)^2=(l+2u)u(u+2l), whose odd residue modulo eight is l, either 3 or 7; impossible. Otherwise the two selected factors have valuations at least two, their difference is 4l, and their even sum forces both valuations even. Root replacements satisfy the same condition. No claim that this necessary condition characterizes the full dyadic Kummer image is used.

At infinity the first Kummer coordinate is positive. The sign of the second coordinate is onto because of tau2. Thus the positive-second-coordinate subgroup of Sel_2 has index two, and all its members have unique representatives

    (U,V)=(3^delta product_i q_i^{u_i}, product_i q_i^{v_i}).

Here q_i run over supp(l). Good-prime and dyadic restrictions exclude all other prime factors, and the local condition at three excludes 3 from V. With s_i=[-1/q_i], lambda_i=[3/q_i], and

    (Ku)_i=sum_{j!=i}[q_j/q_i](u_j+u_i),

comparison at q_i with tau1^{u_i}tau2^{v_i} gives exactly

    Ku+diag(lambda)v=delta lambda, (K+diag(s))v=0,
    (lambda+s)^t v=0.

For example, the first unit quotient has bit (Ku)_i+(delta+v_i)lambda_i, and the second has bit (Kv)_i+s_i v_i. The last displayed equation uses [q_i/3]=lambda_i+s_i. This directly checks the direction of the Legendre symbols and the normalization in V02:251-263 and P:392-410.

Quadratic reciprocity gives K+K^t=ss^t+diag(s). When sum s=1, K1=K^t1=0 and N=K+diag(s)=K^t+ss^t. Suppose ker K=<1,1_B>, lambda is outside im K, and sum lambda=0. Then ker N=ker K^t intersect s-perp is one-dimensional: ker K^t has dimension two and s^t1=1. Lambda vanishes on 1 but is a nonzero functional on ker K^t, hence is nonzero on that other line. The equation at three forces v=0. Next Ku=delta lambda forces delta=0 and u in ker K. There are at most four positive-second-coordinate classes, hence at most eight Selmer classes in total. This is an upper bound from necessary conditions, not yet a local-solubility assertion.

## 4. Simultaneous matrices, retaining the cross-symbols

Write Bset=supp(beta), J=supp(theta), d=|Bset|>=1. The congruences give sum_B s=0, sum_B lambda=1, sum_J s=0, sum_J lambda=0. The mutual-square conclusions give zero cross-row sums in BOTH directions:

    sum_{j in J}[q_j/q_b]=0 for b in Bset,
    sum_{b in Bset}[q_b/q_j]=0 for j in J.

Individual cross-symbols can be nonzero. They remain unchanged throughout the construction.

Introduce d-1 I-slots of type (s,lambda)=(0,0) and one q0-slot of type (1,1). Both Q0=Bset union I union {q0} and Q1=Q0 union J then have total s=1 and total lambda=0. Let C have columns e_i+e_d. Put the Bset-to-I symbols equal to C, all other I-incident symbols zero, and [q0/q_b] equal to the b-th row sum of C. Set the reverse symbol by reciprocity, so [q_b/q0]=[q0/q_b]+s_b. Keep q0-J symbols free.

Now K1_B=0 on both supports. In Bset rows the I and q0 terms cancel and the added J sum is zero. In an I row the C column sum is zero. At q0 the sum is the total of C plus sum_B s, both zero. In J rows the reverse cross-row sum is zero. This is P:627-649, and it uses the exact allowed cross sums rather than replacing the entire cross block by zero.

Choose b_* in Bset and a=e_{b_*}+e_{q0}. Then a^t1=0 and a^t1_B=1. Put Ksharp=K+lambda a^t and T=I-1_B a^t. Ksharp kills 1 on both sides, Ksharp1_B=lambda, T projects onto a-perp along 1_B and fixes 1, and K=Ksharp T. If deleting row and column q0 from Ksharp gives an invertible matrix, its kernel is precisely <1>. It follows that ker K=<1,1_B>. Moreover Kx=lambda would give Ksharp(Tx-1_B)=0; applying a^t to Tx-1_B=c1 gives 1=0. Thus lambda is not in im K. This checks the rank-one correction and its direction directly.

On Q0 the deleted matrix is M0=[[D,C],[C^t,0]], with 1^t D1=1. If M0(x,y)=0, then C^t x=0 implies x=c1. Left multiplication of the first equation by 1^t forces c=0, and injectivity of C forces y=0. D is not assumed symmetric. When d=1, C is empty and D=(1); the argument remains valid. It does not secretly require an auxiliary I-prime.

On Q1 the Bset,I principal block remains M0 because the cross-row sums are zero. Toggling [q0/q_j] changes its reverse too, with a fixed reciprocity discrepancy. Once q0 is deleted, the only surviving change is the j-th diagonal entry. The enlarged determinant is multilinear in those |J| bits, and its full-product coefficient is det M0=1. Therefore it is a nonzero Boolean function: the elementary induction f=f0+X f1 proves this over F_2. At least one assignment is invertible. It leaves M0 unchanged, so the same assignment solves both supports simultaneously. If J is empty, no new assignment is required. These are P:650-703; the argument is for arbitrary d and |J|, independently of the finite checker.

Realize the I-primes successively and q0 last. Their required types are respectively 1 and 7 modulo 12. At every previously fixed prime >=5 a prescribed Legendre sign admits a nonzero residue. CRT therefore gives a reduced residue class modulo 12 times the finite old prime product, and Dirichlet gives infinitely many primes in it. Exclude the finitely many used primes. Reverse symbols agree by the imposed reciprocity rule. The free q0-J bits are chosen in the matrix argument before this final CRT step. There is no incompatible independent-Frobenius prescription hidden here.

## 5. Exact Selmer dimension and both RC parameters

Let n be the product of Q0. All auxiliary primes are distinct and outside 6 beta theta, so n and n theta are positive squarefree and prime to 6. The total s=1 gives 3 mod 4. Since total lambda=0, total (lambda+s)=1 gives 2 mod 3. Both are therefore 11 mod 12, the exact domain of V02:200-205 and V03:1-16. The additional q0 outside Bset ensures n>1. Theta=1 makes these two parameters equal, which is allowed. Neither the rational e ultimately used in the circuit nor the generally nonsquarefree nH is an RC input.

For each l=n,n theta, gamma=(beta,1) is actually locally Kummer. At two and infinity it is the identity; at three it equals tau1 since beta and l are both nonsquare units. At support primes, u=1_B,v=0 and K1_B=0 give square unit quotients relative to tau1^{u_i}. At every remaining odd prime gamma is unramified, and the local Kummer image is exactly the unramified four-element subgroup. This includes all places, not only those used for the upper bound.

Gamma differs from the identity because beta>1 is squarefree, from tau1 because q0 divides l but not beta, and from tau2 and tau1 tau2 because their second coordinates are negative. Thus it supplies a third independent class besides the two rational 2-torsion classes. Combined with the upper bound in section 3, this proves dim_F2 Sel_2(E_l/Q)=3 for both l. It is the full multiplication-by-two Selmer group, not a 2-isogeny Selmer group and not a torsion-quotiented group.

## 6. Full corank one without finite Sha

The finite Kummer exact sequence gives

    0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0.

Mordell-Weil and full rational two-torsion give dim E(Q)/2E(Q)=r+2, even if higher two-power torsion is present. Thus dim Sel_2=3 implies r+dim Sha[2]=1. Finite Selmer groups imply finite Sha[2^a] at every finite a. The structure statement in Poonen's section 12 therefore gives

    Sha[2^infinity] = (Q_2/Z_2)^t direct-sum F,

with F a finite two-group. It does not assert t=0. The divisible subgroup splits as an abstract abelian group, so dim Sha[2]=t+dim F[2].

Poonen-Stoll's primary introductory statement says the Cassels-Tate pairing becomes nondegenerate after quotient by the maximal divisible subgroup and is alternating for elliptic curves. The elliptic principal polarization is induced by the rational divisor (O); the weaker antisymmetry applicable to an arbitrary principally polarized abelian variety is not being substituted. Distinct primary components pair trivially because a pairing value is killed by both relatively prime orders. Consequently the finite two-primary quotient F itself has a nondegenerate alternating pairing.

The needed consequence is stronger than square cardinality. Choose x in F of maximal order 2^a. The pairing identifies finite F with its character dual, so its character from x has order 2^a and some y pairs with x to exact order 2^a. Alternation makes <x,y> a perfect summand isomorphic to (Z/2^a)^2: pairing a relation with x and y proves independence, and subtracting suitable x,y multiples splits every element into this summand and its orthogonal complement. Induction pairs all cyclic factors. Therefore dim F[2] is even.

Now 1=r+t+dim F[2] forces dim F[2]=0, hence F=0, and r+t=1. Passing to the direct-limit Kummer sequence gives corank_Z2 Sel_{2^infinity}(E/Q)=r+t=1. This proves the exact RC antecedent, not only an upper bound. No finiteness of the entire Sha group has been assumed. In particular r=0,t=1 remains a possibility at this point; the following application of RC, not the matrix computation alone, removes it.

Apply RC to each of the two parameters certified in section 5. It gives analytic rank one. The modularity theorem applies to each nonsingular E_l/Q. Kolyvagin's forward theorem for modular elliptic curves then gives algebraic rank one and finite Sha. Returning to r+dim Sha[2]=1 yields Sha[2]=0. This order is V02:265-281. The broader assertion P:457-494 about all curves with corank in {0,1} is unnecessary and is not imported. Nor is square order alone used to prove dim F[2] even: Z/4 is a counterexample to that shortcut. Restriction of the pairing to F[2] is not used either; that restriction is zero on (Z/4)^2 with the standard pairing divided by four.

## 7. Actual rational witnesses with the same m

Since Sha[2]=0, gamma lifts through the finite Kummer sequence to an actual rational point on each E_l. It is outside all four rational 2-torsion images, so the representatives are neither infinity nor any cubic root point. Write them as (x1,y1) on E_n and (x2,y2) on E_{n theta}. Their ordinates and abscissas are nonzero. Multiplying their two Kummer coordinates and using the cubic equation gives squareclass [x_i]=beta=[A]. Thus x1=A q1^2 and x2=A q2^2 for q1,q2 in Q^*.

Choose c in Q^* with H=theta c^2. Scale the second point by (x,y)->(c^2 x,c^3 y), obtaining a point on E_{nH}. Now divide both curve parameters by q1^2, and both sets of point coordinates by q1^2,q1^3. Define

    e=n/q1^2, z=c q2/q1,
    r1=y1/q1^3, r2=c^3 y2/(q1^3 z), w=(eHz)^(-1).

The first point is exactly (A,r1) on E_e. The second point is exactly (Az^2,zr2) on E_{eH}. Dividing its equation by z^2 gives r2^2=A(Az^2-eH)(Az^2+3eH), with the saved leading factor A. All denominators are nonzero. The bits already chosen for the original m, together with these five rational numbers, make the original Q^2 node zero. B, m, A and H are never replaced by data from a second independent choice. When theta=1 one may reuse one rational point and q2=q1, giving z=c!=0. This covers that case without any additional nonvanishing assertion.

The exact saved node array and builder therefore consume precisely the points supplied by the descent and RC argument. Soluble local coverings alone would not suffice; section 6 is what turns the extra Selmer class into the required rational points.

## 8. Direct primary checks and immediate multiplication interface

I independently extracted and read the following actual primary pages and rendered the formula-sensitive pages in this directory:

- Silverman, Arithmetic of Elliptic Curves, second edition, X.1.4, printed 315/PDF 328: split-cubic Kummer map and its root replacements. Render: silverman-315.png.
- Poonen-Stoll, The Cassels-Tate pairing on polarized abelian varieties, author paper PDF pages 1-2: nondegeneracy modulo maximal divisible subgroup and elliptic-curve alternation. Render: poonen-stoll-2.png. Its general-abelian-variety qualification is retained.
- Poonen, The Selmer group, the Shafarevich-Tate group, and the weak Mordell-Weil theorem, sections 8-9, the defining sequence and finiteness statements (PDF 6-7), and section 12 (PDF 10-11): finite Kummer sequence, finiteness, primary decomposition, and rational-divisor alternation. Render: poonen-10.png; the continuation concerning the divisor (O) on page 11 was read in the actual extracted text.
- Kolyvagin, On the Mordell-Weil group and the Shafarevich-Tate group of modular elliptic curves, printed 3-5/PDF 5-7: modular hypothesis, forward Theorem 1, and the explanation removing the auxiliary Heegner nonvanishing condition. Render: kolyvagin-4.png. This is a forward rank theorem, not a converse theorem.
- Breuil-Conrad-Diamond-Taylor, On the modularity of elliptic curves over Q: wild 3-adic exercises, Theorem A, PDF 1: every elliptic curve over Q is modular. Render: bcdt-1.png.

These are direct checks of applicable classical statements, not new proofs of their published theories. Standard local squareclass descriptions, Hensel lifting, formal groups at odd residue characteristic, quadratic reciprocity, CRT, Dirichlet and Mordell-Weil are also explicit inputs.

The production slope builder, lines 68-92, passes B=R/Theta^2 through its guarded equation, with R=ell^2 a^2 R0 and Theta the rational trace of six inverse products. It does not pass an elliptic abscissa or an independently unrelated B. The guards make R0,ell,a,Theta nonzero. At V02:430-457, accepting the separately produced local/height bounds, the arithmetic is consistent: with D_p=51C_p and E_p=52C_p+v_p(12)+4,

    2E_p-C_p-2D_p=C_p+2v_p(12)+8>v_p(12),
    2E_p-C_p-2v_p(12)=103C_p+8>=4.

Thus Theta has valuation v_p(12) and B has the needed five old-prime valuations. Selected odd-contact primes have valuation one in B because their trace sum is a unit; at all other non-old primes B has even valuation. This gives the square reduced denominator. The real approximation makes R positive and small while Theta tends to 12, giving 0<B<1/2. These are immediate interface calculations only; this review does not re-prove the separately assigned six-contact, private-group, or simultaneous approximation producers.

## 9. Separate finite checks and final boundary

`check_independent.py` imports only the Python standard library and reads the saved JSON as data. Its checks are not a substitute for the all-size matrix proof or the classical theorems. CHECKS.json records:

- 96 exact rational evaluations matching the parsed saved root to the independently written Q^2 formula, in addition to the complete direct node read;
- all 64 distinct multiplier signatures;
- exhaustive small abstract matrix data for d=1,2 and |J|=0,1,2, allowing every permitted s/lambda vector, internal symbol choice and even-row/even-column cross block;
- 100 further matrix cases with d=3 through 6 and |J|=2 through 6;
- 254 matrix instances total, testing 3,071 q0-J assignments, with 164 instances having genuinely nonzero cross blocks;
- direct rank tests for both kernel targets and for the complete necessary local system, rather than only a deleted determinant;
- an exact theta=1 rational witness tuple evaluated through the saved node array, and rejection after perturbing its second ordinate witness.

For that last test, u=2730^2, s=2u/(1+17u^2), c=(1-17u^2)/(1+17u^2), B=17s^2 and 1-B=c^2. The script checks PC's size, denominator, and all five valuation conditions exactly. It uses n=323 and the point x=17(23297/2444)^2, y=17(23297/2444)(85425/2444)(29719/2444); the two differences x-323 and x+969 are checked as the required squares/squareclass. This supplies only a regression example; the general witnesses are proved in section 7.

The two exact RC antecedents, the finite-quotient pairing step, the single shared multiplier, and the saved squared root all withstand these checks. No correction to the producer report or current V4d text is requested. RC remains unproved by this review, and the upstream multiplication producers remain separate obligations. No manuscript, production source, original review, or runtime file was edited.
