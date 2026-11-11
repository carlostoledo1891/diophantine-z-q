# Unary theta and finite Chebotarev: source-bound audit

Scope: the two external inputs left open by the sealed T3 reconciliation. This report supplies an independent unary-theta derivation and checks finite Chebotarev against the actual simultaneous trace tests. It does not re-approve T1/T2/T3 as a whole, the construction of the moving Kummer target, or the claimed Diophantine conclusion. No manuscript or runtime files were changed.

Current source: review-v4b/08-odd-source.tex, SHA256 a521b79a36bce021a97cf868ca3221799f19c15077cc68294747bf75fdc4cb3e. Its new lines 342-348 impose the finite odd-stage cap. Sections 03 and 09 are separately pinned in SOURCE_PINS.json. The prior T3 report and consumer addendum remain byte-identical.

Finding: the exact unary series at current08:356-363 is a cusp form with the stated character and an available level 4 C^2 J, for C supported entirely at the old support. This proves the required exponent-one upper bound at every fresh prime dividing J. Finite Chebotarev supplies all the trace approximations at current08:378-409 and 435-446, including their joint compatibility, and the fresh prime in current09:212-214. It also supplies the prime class used at current09:225-230 and the cyclotomic instance of the graph realization at current09:320-330. No new mathematical correction was found for these two inputs. The exact scope and derivations follow.

## 1. Primary sources actually read

1. Andre Weil, Sur certains groupes d'operateurs unitaires, Acta Math. 111 (1964), 143-211. Local PDF: work/astra-weighted-theta-audit-001/primary/weil-1964.pdf, SHA256 22df47cb98307aa77c46028cf5575eeb1d3524950dbdadb9c0c21890966039d2. Source URL: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/weil2.pdf . I rendered and read printed 160, 168-169, 193-194, which are PDF pages 18, 26-27, 51-52. Section I.19, Theorem 4, printed 168, gives Poisson invariance for Schwartz functions. I.20, printed 169, identifies its discrete-lattice case as classical Poisson summation. I.13, printed 160, gives the Fourier and scaling operators. III.41, printed 193-194, gives the global theta construction and its convergence/invariance. The proof below only needs the classical Poisson specialization and its Gaussian calculation.

2. Nick Ramsey, Geometric and p-adic Modular Forms of Half-Integral Weight, Ann. Inst. Fourier 56 (2006), 599-624. Local PDF: work/ramsey-2006.pdf, SHA256 c4dbde444169f075dc77dadb67a18f0348a450a9df32d16ef049e40e348ed0f4. Source URL: https://www.numdam.org/item/10.5802/aif.2195.pdf . Printed 600, PDF page 3, was rendered and read. It states the classical theta transformation and the square-root convention in (1.1). I use that explicit normalization, not Ramsey's integral geometric theory at primes dividing the level.

3. Jean-Pierre Serre, Quelques applications du theoreme de densite de Chebotarev, Publ. Math. IHES 54 (1981), 123-201. Local PDF: this directory/primary/serre-chebotarev-1981.pdf, SHA256 bfcda9821742b02801e4f1264750aebeb656141fbd53fb61b8662333e1491830. Source URL: https://www.numdam.org/article/PMIHES_1981__54__123_0.pdf . Printed 131-132, PDF pages 10-11, were rendered and read. Section 2.1, Theorem 1, printed 131, is the qualitative theorem used here: for finite Galois E/K and a conjugation-stable subset C of its group G, the unramified prime ideals whose Frobenius lies in C have natural density |C|/|G|. Serre defines arithmetic Frobenius by a -> a^(Nv) modulo the prime. Section 2.2 gives an unconditional effective refinement, which is unnecessary here. No GRH result is invoked. This is an original Serre research paper stating the classical Chebotarev theorem, not a claim to have read Chebotarev's original proof.

I did not obtain or read an original Shimura proof of this unary-theta statement. The following is a derivation from the primary Poisson input and the explicitly read theta multiplier. No appeal to an inaccessible Shimura theorem is counted as evidence.

## 2. Exact unary statement, including sieves

Let S be the finite old support in current08:297-299. It contains 2, the conductors of eta and the old characters, and every late sieve prime, including the current theta prime ell_0. Let lambda_0 = eta chi_{-4}^i, where i is chosen so that lambda_0(-1) = -1. Choose an integer C divisible by its conductor and by every prime in S, and having no prime factors outside S. Induce lambda_0 to a Dirichlet character lambda modulo C, extended by zero off (Z/CZ)^*. Thus

lambda(m) = eta(m) chi_{-4}(m)^i if gcd(m,S)=1, and lambda(m)=0 otherwise.

The resulting character can be imprimitive. Every step below allows this. Put e(x)=exp(2 pi i x) and

F_lambda(z) = sum_{m>0} lambda(m) m e(m^2 z),   Im(z)>0.

Then

F_lambda in S_{3/2}(Gamma_0(4 C^2), lambda chi_{-4})

in the classical theta-multiplier convention of Ramsey (1.1). For squarefree positive J with gcd(J,S)=1,

Theta_J(z) = F_lambda(Jz)

belongs to S_{3/2}(Gamma_0(4 C^2 J), lambda chi_{-4} (J/.)); its character on units is eta chi_{-4}^i (-J/.), exactly current08:362. The assertion about level is an available level, not an assertion that this is the minimal conductor. In particular, the available level has exponent one at each p|J and omits every fresh prime outside J. This is exactly what current08:436-438 needs on omission.

## 3. Transformation proof, with the character rather than its inverse

Write

Theta(z,w) = sum_{n in Z} e(n^2 z+n w),

and j(gamma,z) = epsilon_d^{-1} (c/d) (cz+d)^(1/2) for gamma=(a b;c d) in Gamma_0(4), with Ramsey's branch. Thus Theta(gamma z,0)=j(gamma,z)Theta(z,0) and j(gamma,z)^2=chi_{-4}(d)(cz+d).

Poisson applied to a Gaussian gives the standard Jacobi identity

vartheta(-1/tau,u/tau) = (-i tau)^(1/2) exp(pi i u^2/tau) vartheta(tau,u),

where vartheta(tau,u)=sum_n exp(pi i n^2 tau+2 pi i n u). Also vartheta(tau+2,u)=vartheta(tau,u), by direct substitution. These identities imply, for gamma in Gamma_0(4),

Theta(gamma z,w/(cz+d)) = j(gamma,z) exp(pi i c w^2/(2(cz+d))) Theta(z,w).                    (U1)

For completeness, the associated matrix on (tau,u) with tau=2z is (a,2b;c/2,d), which lies in Gamma(2). This group is generated by T^2, S T^2 S^{-1}, and -I, as follows by the Euclidean algorithm on its first column using additions of even multiples of a row. The Gaussian S identity and the T^2 identity therefore give (U1) by composition. The scalar factor, independent of w, is fixed at w=0 by the displayed Ramsey formula. This avoids guessing a metaplectic sign or a character inverse.

For gamma in Gamma_0(4C^2), set D=cz+d. Differentiating (U1) with respect to w, then setting w=Dv, gives

Theta_w(gamma z,v) = D j(gamma,z) exp(pi i c D v^2/2) [Theta_w(z,Dv)+pi i c v Theta(z,Dv)].

The directly verified quasiperiod relation and its derivative are

Theta(z,w+2mz)=e(-m^2 z-mw)Theta(z,w),
Theta_w(z,w+2mz)=e(-m^2 z-mw)[Theta_w(z,w)-2 pi i m Theta(z,w)].

Take v=r/C and m=cr/(2C), an integer. Then Dv=2mz+dr/C. The derivative correction -2 pi i m cancels +pi i c v. The remaining exponential is

exp(pi i c D r^2/(2C^2)) e(-m^2 z-mdr/C) = e(-cdr^2/(4C^2)) = 1.

The last equality uses 4C^2|c, including its full dyadic part. Hence

Theta_w(gamma z,r/C)=D j(gamma,z) Theta_w(z,dr/C).                                      (U2)

Define the finite Fourier transform lambda_hat(r)=C^{-1} sum_{a mod C}lambda(a)e(-ar/C). Fourier inversion and the oddness of lambda give

F_lambda(z) = (4 pi i)^{-1} sum_{r mod C} lambda_hat(r) Theta_w(z,r/C).

After (U2), the sum on the right has coefficient lambda(dn)=lambda(d)lambda(n), since d is a unit modulo C. It follows that

F_lambda(gamma z)=lambda(d) D j(gamma,z) F_lambda(z)
                  =lambda(d) chi_{-4}(d) j(gamma,z)^3 F_lambda(z).                    (U3)

This proves the stated character, not lambda^{-1}. The argument includes imprimitive lambda and arbitrary dyadic conductor. The finite Fourier transform is used only in this complex-analytic proof. It neither defines a new 2-adic normalization nor divides the original q-coefficients by C. The coefficients of F_lambda remain lambda(m)m, in the original finite character field and integral over Z.

## 4. Holomorphy at every cusp

Normal convergence on the upper half-plane follows from the Gaussian decay of n exp(-2 pi n^2 Im(z)). To check the cusps without importing a separate unary theorem, take gamma=(a b;c d) in SL_2(Z), first c>0, and D=cz+d. Use gamma z=a/c-1/(cD). For the full sum F_full=2F_lambda, put L=cC and A=2i/(cD). Then Re(A)>0 and

F_full(gamma z)=sum_{r mod L} lambda(r)e(a r^2/c) sum_{n congruent r mod L} n exp(-pi A n^2).

The outer coefficient is L-periodic because L is divisible by C and c. For f(x)=x exp(-pi A x^2), its Fourier transform in the convention exp(-2 pi i x xi) is

f_hat(xi)=-i xi A^(-3/2) exp(-pi xi^2/A).

Poisson on the coset r+LZ gives L^{-1} sum_k e(kr/L) f_hat(k/L). Therefore, with a nonzero constant beta depending only on c,L and consistent square-root branches,

D^(-3/2)F_full(gamma z)
 = beta sum_{k in Z} k S(k) e(cd k^2/(4L^2)) e(c^2 k^2 z/(4L^2)),

where S(k)=sum_{r mod L}lambda(r)e(a r^2/c+kr/L) is bounded independently of k.

Since L=cC, the exponents of e(z) are k^2/(4C^2). All are nonnegative; the k=0 coefficient is zero. The series converges normally and tends to zero as Im(z) tends to infinity. This proves holomorphy and vanishing at that cusp. The cusp at infinity follows from the original series; c<0 reduces to c>0 by replacing gamma by -gamma, which only changes the scalar in the chosen slash operation. Thus F_lambda is cuspidal, including for imprimitive lambda.

For dilation by J, take gamma in Gamma_0(4C^2J) and gamma_J=(a,bJ;c/J,d). Then J gamma z=gamma_J(Jz). In (U3),

j(gamma_J,Jz)/j(gamma,z) = (J/d).

The cube of this quadratic ratio is again (J/d), proving the displayed character and level for Theta_J. Dilation takes rational cusps to rational cusps, so cusp holomorphy is preserved. No primitive-character hypothesis was used.

This also explains two nearby consumers. Multiplication by ordinary theta gives a genuine weight-two form because j^4=(cz+d)^2; its character is the same even character. And every prime p omitted from U is absent from 4C^2J for every J subset U, since C uses only S. The proof creates no hidden fresh-prime conductor. The exact character ratio in current08:387 is quadratic on units, as required for integer-two divisibility of diamond translates.

## 5. The finite joint quotient for trace approximation

Fix one actual theta stage and one finite collection of operators and omissions. The coefficient field L is a finite extension of Q_2 large enough for all the finitely many characteristic-zero constituents, their characters, and the matrices used to decompose the finite space. Let O be its DVR, pi a uniformizer. For each cuspidal constituent use the continuous two-dimensional representation rho_j established at the previous primary-input step. For Eisenstein constituents use the two continuous characters. Retain all old multiplicities; good-prime Hecke operators act by the same scalar on each copy.

Each rho_j admits a stable O-lattice. Indeed its image is compact. The O-span of the orbit of any lattice is bounded and contains that lattice, so it is a finitely generated full O-lattice and is stable. Fix these lattices. For m>=1 form the intersection H_m of the kernels of every reduction rho_j modulo pi^m and of every finite character needed in this test. Include all fixed rational labels, K if a split prime is needed, and any extra finite congruence conditions actually prescribed. One can also include the cyclotomic character modulo a sufficiently high power of 2 explicitly; it is already present in the determinants in the standard normalization.

H_m is open and normal in G_Q, because it is a finite intersection of kernels of continuous maps to finite groups. Its fixed field E_m/Q is a finite Galois extension. Its group is the ACTUAL JOINT IMAGE. It need not be the product of the separate images. Let g be the actual Galois element whose scalar operators are wanted. The image sigma_m of g is an element of that joint image, so its conjugacy class is nonempty and compatible with every included character.

Serre 2.1, Theorem 1 gives infinitely many unramified rational primes q whose Frobenius class in Gal(E_m/Q) is that class. Discard the finite set consisting of 2, all level/support primes of this fixed collection, the prime factors of the current Fourier index, earlier chosen auxiliary primes, and any other explicitly fixed exclusions. Infinitely many remain. Their traces and determinants agree with those of g modulo pi^m in every constituent, and their finite abelian characters agree exactly. Arithmetic Frobenius is used both here and in the good-prime polynomial X^2-T_q X+q<q>.

Only conjugation-invariant data are inferred: traces, determinants and abelian characters. No assertion that chosen Frobenius representatives converge to g in G_Q is required. If one needs an actual representative in the conjugacy class for a separate finite construction, a prime of E_m above q can be chosen accordingly. That extra observation does not enter the scalar-operator limit.

As m tends to infinity, the scalar tuples converge. Passing from a scalar tuple to its operator on the fixed finite-dimensional space is continuous, even if the change of basis has denominators. For any requested operator precision one can take a larger m to pay those fixed denominators. These denominators may depend on the stage. No uniform bound over stages is asserted or needed. The sizes of q likewise have no relevance to the graph weight budget.

## 6. Integral module and all Fourier-index tests

Let M be the O-module generated by the relevant vector and its integral Hecke/diamond translates in the fixed finite-dimensional space. Good Hecke and diamond actions preserve q-integrality by the explicit formula current08:389-391 and the character-ratio argument. Choose finitely many Fourier coordinates that inject this vector space into L^r. Then M injects into O^r. Since O is Noetherian, M is finite; since O is complete with finite residue field, its finite modules are compact and their images in the Hausdorff finite-dimensional L-space are closed.

Thus the Hecke/diamond operator limits preserve M. This is the argument at current08:392-397. It requires no integral eigenprojector and makes no claim that M is saturated in the full q-integral lattice. For d(g), use q<q> in the same finite quotient; q is an O-unit and the scalar tuple is the determinant tuple.

For a coefficient test at a fixed n and a finite product of s traces, choose distinct fresh primes q_1,...,q_s, each avoiding n and all earlier chosen primes. The coefficient of T_{q_1}...T_{q_s}v at n is then v[n q_1...q_s], because every second term in the good-Hecke formula vanishes. At higher precision repeat this finite construction. Different n may use different primes. This proves the coefficient identity or divisibility for every n, not the existence of one finite prime set serving all n simultaneously.

For a reduced coefficientwise trace orbit, one further closure point matters. If a q-integral vector v has every coefficient in the maximal ideal, fix n and approximate t(g) by a fresh q avoiding n. Then (T_qv)[n]=v[nq] is in that closed ideal; passing to the limit proves (t(g)v)[n] lies there. Hence scalar traces preserve the coefficientwise-zero reduction kernel. No identification with M/pi M, and no saturation hypothesis, is needed.

At current08:399 a fresh trace kills a unary correction modulo the maximal ideal because theta is 1 modulo 2 and Theta_J has support J times a square. For q avoiding Jn, the exponent of q in nq is odd, so nq is outside that support. At current08:406 two distinct fresh primes add weight at least two in the full-two-torsion application. The cap R>=2 imposed at lines 342-348 pays this before the single unary division. Further traces preserve the resulting coefficientwise-zero kernel by the preceding paragraph.

The order is: finite operator budget and precision cap, one actual stage satisfying the global truncated bound, its finite coefficient field and representations, one coefficient index, then the auxiliary primes used to test that index. The stage is common to all indices. The auxiliary primes need not be common to all indices. This is compatible with current09:158-168 and 320-326; it interchanges no infinite intersection with an existence quantifier.

## 7. Contraction and omission use compatible targets

At current08:427-440 the targets g tau_p phi_p, g phi_p, g tau_p and g are actual elements of G_Q. Put representations from U and from all needed omissions into the same H_m above. Each target has an image in that same actual finite joint group. Therefore all comparisons are simultaneously approximable as scalar tests. There is no assumption that separately chosen conjugacy classes in several extensions can be prescribed arbitrarily.

Old rational label characters are unramified at the fresh p. Hence they are 1 on tau_p, and their value on phi_p is their value at p. In particular the two targets differing only by tau_p have identical old labels. In the omitted family the entire p is absent from the level, so its representation is unramified and the two traces are equal there. In the retained new constituent the ramified quadratic character changes sign. This is the exact setting for the first-shell difference before division by two. Chebotarev does not supply or replace the local matrix identity; it realizes its already defined class-function tests.

If K-splitting is also imposed and p splits in K, the whole local decomposition group at p acts trivially on K. Thus multiplying by tau_p or phi_p does not change K's label. If the contraction uses a previously chosen K-split target g, all four relevant targets remain K-split. These conditions must be included jointly, not added as independent classes after selecting q.

## 8. The nonempty-seed fresh prime and the contradiction prime

Current09:203-224 fixes a fresh K-split p and an arithmetic Frobenius lift phi_p in its decomposition group. Include K and every fixed rational character in H_m. The image of phi_p on K is 1, since p splits. The fixed characters are unramified at p and evaluate on phi_p as they do at p. Chebotarev therefore gives a fresh K-split p' matching the required finite trace precision and ALL those characters at once, while avoiding the full level, p, and the coefficient index p^2.

For each fixed quadratic filter character chi, chi(pp')=chi(p)^2=1. Thus pp' satisfies the square filter even if p alone does not. This is exactly the compatibility needed at current09:212-215. The approximation precision can be made sufficient for the coefficient comparison after the already fixed division by four. It is not necessary to force exact equality of characteristic-zero traces at p'.

The final prime at current09:225-230 is a different application. Here ell is positive, squarefree and congruent to 11 modulo 12, so ell is not a square and Q(i,sqrt(ell)) is biquadratic. Current03:415-434 chooses K with a ramified prime outside the old fields, in particular outside the ramification support of Q(i,sqrt(ell)). Therefore K is not contained in that biquadratic field and their intersection is Q. In the compositum there is an automorphism acting +1 on i, -1 on sqrt(ell), and +1 on K. This is a nonempty class in an abelian finite Galois group. Chebotarev gives infinitely many good primes with p=1 mod 4, (ell/p)=-1 and (k/p)=1, after every finite avoidance. These are the simultaneous conditions used in the two-primary reduction contradiction. No unproved independence of arbitrary label coordinates is used.

## 9. Numerical prime realization of the finite graph

Current09:320-330 invokes CRT and Dirichlet after the finite graph, its alphabet, and one actual stage have been fixed. The needed Dirichlet instance also follows from the same qualitative Chebotarev theorem applied to Q(zeta_M)/Q. For a unit residue class a modulo M the corresponding automorphism is a nonempty singleton; primes in that class have positive density.

Every rational elementary quadratic character unramified outside the finite support is a Kronecker character of a squareclass supported there and is determined by a residue class modulo an integer supported there, with a sufficiently large power of 2. Enlarge M by the conductors of any further finite rational characters actually used. A label admitted to the ACTUAL common alphabet already has a representative unit residue class a modulo M. This step does not claim that every tuple of signs is admitted. In particular it respects the relations from K and the stationary tests emphasized at current09:187-190 and 247-249.

Inductively, previously selected variable primes p_1,...,p_t are distinct and outside M. Fix the new prime's allowed class modulo M. Its desired forward Legendre bit against each p_j can be enforced by a nonzero residue class modulo p_j. If the forward convention is (p_j/q), quadratic reciprocity translates it to the required class of (q/p_j), because q modulo 4 is already fixed. The moduli M,p_1,...,p_t are coprime, so CRT gives a unit class modulo their product. The cyclotomic Chebotarev instance gives infinitely many primes in it, and one discards all already used or otherwise forbidden primes. Reciprocity supplies the reverse bits, rather than imposing them independently.

There are finitely many vertices at the chosen b, so this induction terminates. The moving ell_0 and all primes of k are among the exclusions when required. Every final address retains the graph's already proved zero-total label; finite prime realization does not alter that combinatorial property. In particular the moving support (D/ell_0)=1 remains satisfied at every address. This uses the prior zero-label-packet argument, not a new claim that arbitrary graph addresses have the right support automatically.

## 10. Scope boundaries and suggested source note

The two inputs left open in the sealed T3 report are now supplied at their actual scopes. The unary proof handles imprimitive sieves, the dyadic conductor, the scalar character, every cusp, and the absence of omitted fresh primes from the level. The finite Chebotarev proof handles joint quotients, conjugacy, continuity, finite avoidance, K-split matching, the contradiction prime and finite graph residue realization.

This report does not prove the existence or local compatibility of the modular Galois representations again; the sealed T3 primary Carayol/Casselman pass supplies that separate input. It does not construct the affine Kummer element used to produce the moving theta stage in current03:315-325. Once that element exists, the same finite-quotient theorem applies, but its existence and compatibility belong to the independent Kummer audit. It does not prove the minimum-depth, graph-program, or arithmetic Selmer arguments again. The cap R in current08:342-348 remains essential.

For an author who wants explicit citations without adding a new hypothesis, a source note can say: induce the odd character lambda=eta chi_{-4}^i to a modulus C supported on S; Poisson summation gives F_lambda in S_{3/2}(4C^2,lambda chi_{-4}), and dilation by J gives the displayed Theta_J at level 4C^2J. Cite Weil I.19-I.20 and Ramsey (1.1), with the derivation here available. For scalar trace limits cite Serre 2.1, Theorem 1, and state that all constituents and prescribed finite characters are placed in their joint finite quotient before choosing a fresh prime. These are source clarifications, not a requested change in mathematical scope.

All primary page images, fresh extracts and source hashes are recorded in SOURCE_PINS.json and RECEIPT.json. The exact final report hash is in the receipt. No conclusion about the overall claimed theorem is drawn.
