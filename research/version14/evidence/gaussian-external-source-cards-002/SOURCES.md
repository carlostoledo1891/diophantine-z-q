# Gaussian external source cards

These are project paraphrases of the stated published inputs. They are not copies of the source publications and do not approve every downstream application. Historical records and exact source-version qualifications are retained in SOURCES.json.

## V5-SUN-BL-CONGRUENCES

Published input, project paraphrase: For an isotropic nondegenerate integral quadratic form F in n>=5 variables and a nonnegative smooth compactly supported weight away from the gradient-zero locus, the weighted count of all integral zeros satisfying nonempty admissible sets of local zeros that are nonzero modulo each relevant prime has the product-density main term and error O_(epsilon,F,w)(B^(n/2+epsilon) M^(n/2+epsilon)), uniformly in M and allowed subsets when M is coprime to twice the discriminant.

Retained published locator: Theorem 4.1; accepted manuscript p.17; BL-v2.tex:1278–1326

Application objects: Same theorem label and hypotheses in v2 and institutional accepted text; final typeset numbering not independently observed.

Application hypotheses: n=5 is permitted (n≥5, not n>5). Qκ has κ≠0, rank5 and rational isotropic point (1,0,1,0,0). Modulus squarefree, coprime to2κ, hence to2ΔQ; each residue subset is in nonzero zeros. Smooth compact support away from origin, so gradient bounded away from0. Error B^(n/2+ε)m^(n/2+ε) uniform in modulus/subsets; derivatives may depend on fixedτ.

Conventions: BL counts all integral zeros; appendix imposes global primitivity by Möbius inversion. Hessian/determinant discriminant conventions differ only by powers of2 here. Primitive local density is1−p^-4; conditioning denominator p^4−1.

Connecting argument retained from the scoped application: Rescale by h in Möbius sum. For (h,m)=1, h^-1Ω has same size; otherwise no contribution. Sum errors absolutely and calculate local densities.

Version qualification: Only the consumed nonprimitive uniform count interface; Mobius inversion, local positivity and downstream sieve remain separate.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V5-SUN-WILLIAMS-MERTENS

Published input, project paraphrase: For a fixed arithmetic progression with coprime residue and modulus, the Mertens product has a positive constant and the prescribed reciprocal-logarithm exponent. In particular the two unit classes modulo4 have exponent1/2; removing finitely many fixed primes changes only the positive constant.

Retained published locator: Theorem1, p.356; ordinary formula(1.1), p.353

Application objects: Published theorem; author-hosted scan of journal pages.

Application hypotheses: Fixed modulus4 with coprime residues1,3; also modulus1, or product of the two modulus4 formulas. Only finitely many fixed exceptional primes removed.

Conventions: Positive constants in product asymptotics; χ4(p)=±1. Taking logarithms loses only convergent∑p^-2 terms.

Connecting argument retained from the scoped application: Gives∑g(p)=kloglogy+O(1), and ∏(1−4/(ℓ−1))^k≫(logL)^(-4k).

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-AUDIT-BHB-BOX

Published input, project paraphrase: For integer polynomials of bounded degree and height at most H with no common factor in Z[X_1,...,X_n], and rectangular side parameters, H and M at least2, the number of box points for which some prime greater than M divides all polynomial values is O_(d,n)(V log(VH)/(M log M)+V log(VH)/B_min). The constant is independent of the number of polynomials.

Retained published locator: Lemma 2.1; accepted manuscript p.6; BHB-v1.tex:559–599

Application objects: Inhomogeneous adjacent norms on Q_kappa=0; two fixed-coordinate charts, then a short-basis substitution into the ternary congruence lattices. See the source-pinned tail report.

Application hypotheses: Rectangular side parameters and L,H at least2. Fixed dimension3, polynomial degrees≤4; coefficient heights polynomial inB. No common factor in Z[x,z,w], including common prime content. After lattice substitution detE=±q²; primes outside2t stay invertible; remove only common content supported on2t.

Conventions: Height=max absolute coefficient. All nonhomogeneous chart pairs explicitly checked; homogeneity of sieve polynomials is not required.

Connecting argument retained from the scoped application: Apply to P,T or P′,K in short-basis coordinates; volume O(B³/q²), smallest side≫B/T. Also apply to a,b²+1 for self tail.

Version qualification: Retain R for the local form, divisor sum over d|q, and largest minimum lambda_m as explicit proof-supported interpretations of printed slips. No publisher correction is claimed.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-AUDIT-BHB-LATTICES

Published input, project paraphrase: For a quadratic form R of rank at least3 and a squarefree product q of odd rank-preserving primes, all zeros modulo q are covered by at most (3m)^omega(q) q^(m-2) rank-m lattices of determinant q^(m-1), containing qZ^m. The number with largest Euclidean successive minimum greater than T is O_m((3m)^omega(q)q^(2m-3)T^(-m)); the stated short-basis and inverse-coordinate bounds also hold.

Retained published locator: Lemma 4.1; accepted manuscript pp.13–14; BHB-v1.tex:949–983

Application objects: Inhomogeneous adjacent norms on Q_kappa=0; two fixed-coordinate charts, then a short-basis substitution into the ternary congruence lattices. See the source-pinned tail report.

Application hypotheses: R=κw²−xz has rank3. q is squarefree and every p|q is odd and p∤κ. Good primes preserve rank3. Euclidean successive minima; count with largest minimum>T.

Conventions: Explicit repair: S_R contains every divisor of2κ, not merely rank-drop primes. For m=3: number lattices≤9^ω(q)q, determinantq²; large-minimum count≪9^ω(q)q³T^-3.

Connecting argument retained from the scoped application: Cover t|R by q|R, bound multiplicity of t for eachq, separate largest minimum atT=B^(3/4), use box sieve on remaining lattices.

Version qualification: Retain R for the local form, divisor sum over d|q, and largest minimum lambda_m as explicit proof-supported interpretations of printed slips. No publisher correction is claimed.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## FT-REPLACEMENT-MITSUI-GAUSSIAN

Published input, project paraphrase: For a fixed number field and finite-order ray characters of logarithmically bounded modulus norm, the weighted prime-ideal sum has main term X exactly for the character induced from the trivial primitive character and error X exp(-c sqrt(log X)), uniformly in the permitted characters and moduli, with ineffective fixed-data constants.

Retained published locator: Section 1, Lemma 15, p.12 (weighted prime-ideal sum); Lemma 14 and proof, pp.11–12 (smoothed sum). Character conventions and principal indicator p.2; explicit uniformity paragraph immediately before Lemma14 p.11.

Application objects: E=Q(i); fixed finite-order ray character chi of modulus m; rational Dirichlet rho modulo q; theta(a)=chi(a)rho(Na), a ray character modulo m(q), whose finite modulus norm is at most Nm*q^2.

Application hypotheses: For q<=(log X)^B and sqrtX<=Y<=X, Nm*q^2<=(log Y)^(2B+1) for sufficiently large X depending only on m,B. Mitsui applies with fixed K=E and A=2B+1, uniformly over rho,q. SmallY<sqrtX handled by elementary ideal von Mangoldt sum bound. Fixed bounded X absorbed. Principal indicator checked by inducing character.

Conventions: Normalized ideal norm; Lambda_K(p^j)=log Np for j>=1; finite-order ray characters extended by zero at excluded primes; all residue degrees included; principal means induced by the trivial primitive character. Fixed field and logarithmic exponent. Constants ineffective.

Connecting argument retained from the scoped application: Subtract the smoothed prime sums at x*exp(h) and x to prove unsmoothing for complex characters; bound prime powers of exponent>=2 by O_E(sqrtY log^2(2Y)); replace error atY by Xexp(-c sqrtlogX). Optional primitive-to-imprimitive restoration costs O_chi(log(q+2)log(Y+2)). Any fixed log-power saving follows. No extra Fogels external application is consumed by this proof.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## FT-REPLACEMENT-MITSUI-RATIONAL

Published input, project paraphrase: The same fixed-number-field ray-character prime-ideal estimate applies to Q, including a real infinite place in the ray modulus when required by an odd Dirichlet character.

Retained published locator: Section 1, Lemma 15, p.12 (weighted prime-ideal sum); Lemma 14 and proof, pp.11–12 (smoothed sum). Character conventions and principal indicator p.2; explicit uniformity paragraph immediately before Lemma14 p.11.

Application objects: K=Q; Dirichlet character rho modulo q viewed as a ray character with finite modulus q and, for odd parity, the real infinite place.

Application hypotheses: Mitsui allows arbitrary fixed number field including Q and ray moduli containing infinite places. For q<=(log X)^B and sqrtX<=Y<=X use A=B+1; finite modulus norm is q. SmallY and boundedX handled elementarily. Principal character is exactly rho principal moduloq.

Conventions: Normalized ideal norm; Lambda_K(p^j)=log Np for j>=1; finite-order ray characters extended by zero at excluded primes; all residue degrees included; principal means induced by the trivial primitive character. Fixed field and logarithmic exponent. Constants ineffective.

Connecting argument retained from the scoped application: Apply the same weighted-prime estimate over Q; restore rational prime powers with O(sqrtY log^2(2Y)); obtain uniform allY<=X and q<=log^B X with Xexp(-c_B sqrtlogX) error and its fixed log-power consequences.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GN-LEIBMAN

Published input, project paraphrase: For a one-parameter polynomial orbit on a rational filtered nilmanifold that fails ordinary epsilon-equidistribution, the quantitative Leibman theorem gives a nonzero horizontal character with epsilon-power bounds on its magnitude and binomial C-infinity smoothness norm.

Retained published locator: Theorem 2.9, printed p.480, one-parameter case

Application objects: Apply to t -> g(P(t)) Gamma on [L], with P an integer quadratic from a horizontal Gaussian-norm row. Target discrepancy epsilon=delta^kappa; dimension m and filtration degree at most 2d.

Application hypotheses: Q<=delta^(-kappa)=epsilon^(-1); the stretched filtration and unchanged basis are supplied by V6-GN-COORDINATES. Failure of ordinary epsilon-equidistribution gives a nonzero horizontal character with epsilon-power size and smoothness bounds. L>=sqrt(X)/B0, B0<=delta^(-5kappa).

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Internal integer coefficient extrapolation returns k*eta on the original orbit. Choose C_* first, then 6*C_*kappa<c0/2, sigma<sigma0 and 2*kappa*sigma<1/4. The internal horizontal-character obstruction contradicts total delta-equidistribution. Only ordinary distribution is deduced for each row pullback.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GN-COORDINATES

Published input, project paraphrase: The one-parameter Malcev-coordinate characterization of polynomial sequences gives the coordinate degree constraints associated to a filtration. Composing with an integer quadratic produces a polynomial sequence for the filtration stretched by a factor of two.

Retained published locator: Lemma 6.7, printed pp.501–502, t=1

Application objects: Second-kind Malcev coordinates of g(P(t)); replace G_j by G_ceil(j/2).

Application hypotheses: P has degree two. Each coordinate degree at most j becomes at most 2j; the stretched groups still form a closed connected rational filtration and retain the adapted basis.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Provides polynomiality and degree 2d for the one-parameter Leibman invocation, without a multiparameter theorem or any inference from pointwise fractional arguments.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GN-HORIZONTAL-METRIC

Published input, project paraphrase: The horizontal-character definitions and rational Malcev metric comparisons bound the Lipschitz norm of a fixed circle test function composed with a horizontal character by a fixed power of the rationality and character-height bounds.

Retained published locator: Definitions 2.2 and 2.6 and Appendix A metric comparisons

Application objects: Compose a fixed mean-zero circle bump with a nonzero horizontal character eta of magnitude at most T.

Application hypotheses: T-rational adapted basis and character smoothness at most T. Character pushes Haar probability to circle Haar probability; the initial interval of length floor(X/(100dT)) is long when T<=delta^(-c0).

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Metric comparison bounds the test Lip norm by T^C. Choose C*c0<1/4 and c0<1/4, then small sigma0 handles floors. The obstruction itself is proved internally; no external converse-equidistribution theorem is assumed.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GI-LEIBMAN-I

Published input, project paraphrase: The one-parameter quantitative Leibman theorem supplies a nonzero horizontal character with power bounds when a polynomial orbit in dimension m fails ordinary equidistribution on an interval.

Retained published locator: Theorem 2.9, printed p.480, dimension m

Application objects: For many integer dilations r, restrict n -> g(rn) to a progression a+q[ell] witnessing failure of total eta-equidistribution.

Application hypotheses: ell>=eta*M, q<=2/eta, |a|<=2M, eta^(-1)-rational basis; polynomial degree d. Fixed factors are absorbed by reducing eta0.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Internal d! and q^d clearing removes the possibly O(M) shift; character-lattice pigeonholing fixes one nonzero character on eta-power density of r. No bounded-height assumption on the shift is made.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GI-LEIBMAN-II

Published input, project paraphrase: The same one-parameter quantitative Leibman theorem applies to the product nilmanifold in dimension2m with its product filtration and concatenated rational basis. A nonzero horizontal character is a nonzero pair of factor characters.

Retained published locator: Theorem 2.9, printed p.480, dimension 2m

Application objects: For many pairs r,r-prime, restrict n -> (g(rn),g(r-prime*n)) in (G/Gamma)^2 to a bad progression.

Application hypotheses: Use the product filtration, product lattice and concatenated adapted basis. Product orbit failure is obtained by contraposition of norm transfer; equidistribution of separate factors is never asserted to imply product equidistribution.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Obtain a nonzero pair of horizontal characters, clear shift denominators and pigeonhole. Interchange coordinates if needed to ensure the first character is nonzero; fix one r-prime with many partners.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GI-RECURRENCE-I

Published input, project paraphrase: If a polynomial phase takes values in a sufficiently short arc on a positive-density subset of an interval, the recurrence lemma gives a bounded nonzero integer multiple with a C-infinity bound retaining the arc-length factor and a power loss in the density.

Retained published locator: Lemma 4.5, printed p.490

Application objects: Polynomial r -> d!*beta_j*r^j modulo one on [ceil(R)] for each 1<=j<=d.

Application hypotheses: Selected r have eta-power density. Values lie in an arc of length <=2*eta^(-C5)*(R/N)^j. R<=2*N^(2/3), sufficiently large K_rec, and the large-R branch ensure arc length at most half density. Small R is treated internally by multiplying by r^d.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Retain the arc-length factor in the published smoothness conclusion; the leading coefficient then has N^(-j), not merely R^(-j), accuracy. Additional factorial and product of nonzero bounded integers yield one character.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GI-RECURRENCE-II

Published input, project paraphrase: The polynomial-phase recurrence lemma permits an arbitrary arc center. Its smoothness conclusion retains the short-arc length factor, with a bounded integer multiplier and density-power losses.

Retained published locator: Lemma 4.5, printed p.490, arbitrary interval centre

Application objects: After fixing r-prime, apply to r -> d!*beta_j*r^j in the arc centred at -d!*beta-prime_j*(r-prime)^j.

Application hypotheses: N^(1/3)/4<=R<=2*N^(2/3); many partners supply eta-power density and the same short-arc inequality. The first horizontal character is nonzero.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Gives the same N^(-j) coefficient control as Type I. Does not replace r^j-r0^j by (r-r0)^j, and does not require the arc to be centred at zero.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GI-HORIZONTAL-METRIC

Published input, project paraphrase: Rational Malcev metric comparisons control the Lipschitz norm of a circle bump composed with a nonzero horizontal character by a fixed power of the basis and character bounds; the character pushes Haar probability onto circle Haar probability.

Retained published locator: Definitions 2.2 and 2.6; Appendix A metric comparisons

Application objects: Mean-zero circle bump composed with the recombined nonzero character Psi.

Application hypotheses: Character magnitude and C-infinity[N] norm are bounded by eta^(-C9); on an initial interval c*eta^(2C9+4)*N its phase stays in a fixed short arc.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Lip norm is an eta-power and Haar mean is zero. Choose C_rec beyond length and Lip losses, then K_rec for floors, to contradict total eta^C_rec-equidistribution.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-COORDINATES

Published input, project paraphrase: The one-parameter coordinate characterization allows polynomial extension of the Malcev coordinates to real arguments; affine precomposition preserves their filtration degree constraints.

Retained published locator: Lemma 6.7, printed pp.501–502, t=1

Application objects: Extend the coordinate polynomials of g(n) to real t, form g_R(t), then tilde-g(t)=g_R((t-b)/W).

Application hypotheses: W>=1 and b are fixed integers, 0<=b<W. Affine composition preserves every coordinate degree constraint for the original filtration; real exponential coordinates exist in connected simply connected nilpotent G.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: tilde-g is a polynomial sequence on the same nilmanifold and tilde-g(Wn+b)=g(n). This is an algebraic interpolation statement, not assumed fractional-argument equidistribution.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-LEIBMAN

Published input, project paraphrase: The one-parameter quantitative Leibman theorem applies to a polynomial orbit restricted to an integer progression, with rationality and discrepancy bounds for that restricted orbit.

Retained published locator: Theorem 2.9, printed p.480, one-parameter case

Application objects: Restrict tilde-g to a bad progression u+v[L] in [X], X=WN+b, epsilon=delta^a.

Application hypotheses: Q<=delta^(-a)=epsilon^(-1); u,v integers, 1<=v<=2/epsilon, |u|<=2X, L>=epsilon*X. Same rational filtration and dimension m.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Internal linear extrapolation and forward composition with integer Wn+b give a small nonzero character on g. a<C0/(2*C_aff) with C0=c0 and sigma<min(sigma0,1/(2a)) permit the norm-section obstruction. Total delta on [N] implies total delta^a on the full expanded interval, for fixed W.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GF-FACTORIZATION

Published input, project paraphrase: The quantitative polynomial-orbit factorization theorem gives g=epsilon g-prime gamma, where epsilon is (M,N)-smooth, g-prime is totally M^(-B)-equidistributed on a rational subgroup, and gamma has rational coset period at most M, for M between M0 and a fixed power of M0 depending on the chosen B.

Retained published locator: Theorem 1.19, printed p.476

Application objects: Initial polynomial g on G/Gamma, M0=log(2N)^max(1,C_init), external exponent A renamed B; g=epsilon*g-prime*gamma.

Application hypotheses: Initial basis is log(2N)^C_init-rational, hence M0-rational; fixed dimension m, degree d. Output M0<=M<=C*M0^E(B), rational subgroup G-prime and Gamma-prime=G-prime intersect Gamma.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: epsilon is (M,N)-smooth, g-prime totally M^(-B)-equidistributed, gamma rational with coset period q<=M. B is chosen using lower M>=log(2N) before E(B) is used for the later progression threshold; no circular comparison B>E(B).

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GF-CONJUGATED-QUOTIENT

Published input, project paraphrase: The published quantitative conjugation claim transfers a rational subgroup orbit to the conjugated quotient with the actual intersection lattice, controlling rationality, equidistribution and Lipschitz losses by fixed powers of the height bound.

Retained published locator: Quantitative Claim and proof on printed p.547, within Section 2

Application objects: H_j=gamma_j^(-1)*G-prime*gamma_j; Lambda_j=H_j intersect Gamma; h_j=gamma_j^(-1)*g-prime*gamma_j. F_jk(x Lambda_j)=F(a_jk*gamma_j*x Gamma).

Application hypotheses: Reduced gamma_j has rational coordinates of height M^O(1); a_jk=epsilon(n_jk) has bounded M-power coordinates. The output subgroup basis and lattice satisfy the published claim.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Obtain basis rationality M^C2, total M^(-aB+C2)-equidistribution and Lip norm M^C2. Account for commensurable lattices and finite-index losses; conjugation is not an isometry of the original quotients. Subtract each new quotient Haar mean, including the dimension-zero case. The claim is used for a general weight through separate mean/minor-arc hypotheses, not by extending the Möbius theorem.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GF-RATIONAL-METRIC-SUPPORT

Published input, project paraphrase: The specified AppendixA rational subgroup, lattice and metric comparisons supply the power bounds used in the published conjugation claim, including commensurability and finite-index losses.

Retained published locator: Appendix A: Proposition A.9, Lemmas A.13, A.5 and A.17, as explicitly used in the published p.547 Claim

Application objects: Rational conjugation of G-prime, an adapted basis on H_j/Lambda_j, and translated test functions F_jk.

Application hypotheses: All rational coordinate heights and translation coordinates are M-power bounded. Use the changed lattice Lambda_j=H_j intersect Gamma rather than silently identifying quotients.

Conventions: G connected, simply connected and nilpotent; Gamma discrete cocompact; filtration by closed connected rational subgroups; adapted rational Malcev basis; C-infinity norm in the binomial basis modulo one; Lipschitz norm includes supremum norm. Nontrivial horizontal characters are integer-lattice characters annihilating commutators and Gamma.

Connecting argument retained from the scoped application: Supports the p.547 Claim with exponents depending only on m,d and not B. Records the scoped support chain; does not declare every Appendix A result independently applied.

Version qualification: Application inventory and cited independent reviews; not a proof-assistant certificate or an independent truth decision for the complete manuscript.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-BOUNDARY-MOMENTS

Published input, project paraphrase: The polynomial-forms estimate for the normalized divisor-sum majorant gives the stated asymptotic for a fixed family whose pairwise shift differences are nonconstant, over the full cyclic base variable and permitted parameter boxes, with cutoff-then-size errors.

Retained published locator: Theorem15, AppendixA, published p57.

Application objects: In a fixed enlarged ambient interval without wrap, isolate at most one constant-shift factor nu0. Set F(x)=E_m product_i nu_i(x+P_i(m)). Apply to nu0*F, nu0*F^2, nu0.

Application hypotheses: In F^2 use independent m and mprime; every pairwise difference of the nonconstant shifts, including across the two copies, is nonconstant. All degrees and counts are fixed, coefficients fall within A^C, and the parameter box lengths exceed the required logarithmic lower bound. The sieve exponent is chosen small enough for this enlarged moment family.

Conventions: The source theorem averages x over the whole cyclic group; no x-subinterval conclusion is quoted. Errors retain cutoff-then-size order, o_(v to infinity)(1)+o_v(1).

Connecting argument retained from the scoped application: The three moments give E nu0*(F-1)^2=o(1). Weighted Cauchy-Schwarz reduces any interval-strip mass to E1_I*nu0; V6-GA-GT-INTERVAL-MEAN supplies that mean.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-GT-INTERVAL-MEAN

Published input, project paraphrase: The normalized divisor-sum convex-body estimate gives the mean of a single unit-residue affine majorant over a fixed relative-length interval, with the stated iterated cutoff and size errors. This is a singleton specialization of the source estimate.

Retained published locator: GT TheoremD.3 (Goldston-Yildirim), p1829, and normalized convex-body estimate preceding (D.24), p1840; TZ normalized divisor-sum definition (36), p29.

Application objects: Take one affine divisor-sum factor W*x+b and a fixed relative-length interval I in the enlarged ambient domain; nu0=1 is immediate if no anchor is present.

Application hypotheses: Freeze v and epsilon before the size limit. b is a unit modulo W, the smooth cutoff is fixed and the sieve exponent is sufficiently small. Singleton convex-body specialization has no pairwise degeneracy condition to check. Use the same cutoff normalization as in nu0; its total-mass normalization is one. At primes dividing W, normalization cancels the unit local factor.

Conventions: This is a specialization of a proved divisor-sum/convex-body estimate, not a separately named interval-prime theorem. No claim that global L1 or global Gowers smallness alone implies the interval mean.

Connecting argument retained from the scoped application: Obtain E1_I*nu0=|I|/n plus the stated iterated errors. Together with weighted L2 this gives O(epsilon)+cutoff error+size error for boundary strips.

Version qualification: Exact p1829/p1840 source locator checked during inventory conversion. The standalone bridge reviewers accepted the generic interval-mean specialization; this new locator annotation is not a new independent review of the source proof.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-GT-MAJORANT

Published input, project paraphrase: The Green-Tao divisor-sum construction provides a nonnegative normalized prime-cyclic majorant with any requested fixed finite pseudorandom complexity and domination of the appropriately rescaled prime weight, under its stated cutoff and size hypotheses.

Retained published locator: Proposition6.4, pp1780-1781; Definition6.2; AppendixD construction pp1839-1842.

Application objects: V_z=D*product(p<=z,p not dividing D)=E*primorial(z) for fixed E. Common ordinary-prime majorant nu on prime cyclic group Z/Lprime Z, Lprime in[C L,2C L].

Historical application hypotheses, retained only as old-route metadata: Fix a finite number of unit residues and norm/GN complexity before construction; request at least max(4^s,4s,D_GN) complexity. Take C>=20 and the source construction threshold. On [L^(3/5),L] a fixed positive rescaling of each real centered weight is dominated by nu. Added prime powers in fixed E do not affect any divisor condition because residues are units. This is an explicitly justified adaptation, not a literal additional clause in Proposition6.4. Current application: choose the full pseudorandom order S at least every order required by the present argument, in particular S>=(k+2)2^(k+1) for GT Proposition10.1, as in GA-MAJORANT-FIXED-E and GA-RELATIVE-INVERSE. The old max(4^s,4s,D_GN) request is not asserted sufficient for that current theorem.

Conventions: Nu is nonnegative on the whole cyclic group, not a zero extension. The fixed-z limiting error is made small by choosing z first; it is not asserted to vanish with L for each fixed z.

Current connecting argument: use the smooth truncated-divisor construction with fixed extra modulus E and unit residues. Prime powers in E impose no new divisor condition on those residues. Request the full finite pseudorandom order required by the current GT Proposition10.1 application, and keep cutoff-then-size errors. The former U^(2s)-for-DK translation is retained only in the historical JSON record; it is not the current inverse argument.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-GT-NORMALFORM

Published input, project paraphrase: A finite-complexity system of nonzero pairwise nonproportional affine-linear forms can be extended to the stated normal form by adjoining variables and using the given invertible integer change of variables.

Retained published locator: Lemma4.4 p1773 and normal-form reduction pp1774-1775.

Application objects: For each i!=j select fixed integer v_ij with dot(psi_j)(v_ij)=0 and dot(psi_i)(v_ij)!=0; substitute m=x+sum y_ij*v_ij.

Application hypotheses: All linear parts are nonzero, fixed, and pairwise nonproportional. New y variables range over a full box of side comparable to N/V_z. For t=1 choose v with dot(psi_1)(v)!=0. The extended convex region is defined by original constraints on x+Vy together with the full y box.

Conventions: The integer map (x,y)->(x+Vy,y) is bijective; the sum is multiplied by the exact box cardinality. No restriction to a zero section is used.

Connecting argument retained from the scoped application: Each i has a block of active variables absent from each competing form. Apply normal-form GN, then divide by the added box cardinality.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-GT-RELATIVE-GN

Published input, project paraphrase: The relative generalized von Neumann bound controls a multilinear average in normal form by a small Gowers norm of one factor when all factors are dominated by the requisite common pseudorandom majorant.

Retained published locator: Proposition7.1 pp1781-1782; AppendixC pp1818-1827.

Application objects: Telescope the product after V_z refinement; each term has one centered h and the other factors bounded by ordinary lambda_(V_z,b).

Application hypotheses: One common D-pseudorandom majorant dominates fixed rescalings of all t weights. The extended system is in normal form with fixed coefficients and bounded normalized offsets. The centered factor has small Gowers norm at inner scale L comparable to N/V_z, including all fixed enlargement constants. Choose physical stage thresholds N_j so all inner scales exceed the required L_j.

Conventions: Errors are uniform in residue vectors and convex domains. The positive normalization (phi(V_z)/V_z)^t must be undone.

Connecting argument retained from the scoped application: An o((N/V_z)^d) normalized error per residue becomes o(N^d), because normalized admissible mass is product beta_p=O_Psi(1).

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-BIENVENU-CUBE

Published input, project paraphrase: The fixed finite-complexity affine-linear prime-pattern asymptotic applies to nonconstant forms with pairwise nonproportional gradients, uniformly over the permitted convex domains and bounded normalized affine constants.

Retained published locator: Theorem1.1, published pp79-80.

Application objects: For each centered-cube subproduct and each wrap region, use affine forms W*(x+q*sum omega_r*(h_r-hprime_r)-m_omega*n)+b.

Application hypotheses: Freeze v and therefore W,A and finitely many q first. Forms are nonconstant with pairwise nonproportional gradients, and coefficients are fixed at that v. Offsets are O_v(n); all wrap regions are convex, and the source theorem is uniform over those regions and bounded normalized constants. J/n lies in a fixed positive interval at frozen v.

Conventions: Source uses ordinary von Mangoldt; prime-power weight is O_v(sqrt(n)*log(n)^2), negligible by fixed linear-fiber bounds. This application concerns ordinary primes only.

Connecting argument retained from the scoped application: The linear asymptotic supplies each ordinary subproduct; normalization by n*J^(2a) gives o_v(1), without multiplying a persistent cutoff error by q.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-LOCAL-CUBE

Published input, project paraphrase: The ordinary-prime local-cube estimate and its local-factor calculation control the centered cube with difference-multiset increments in the stated ranges. The proof distinguishes primes dividing the step from other primes.

Retained published locator: Proposition6 and its proof, published pp39-40.

Application objects: Centered ordinary-prime cube on Z/nZ with increments q*(h-hprime), 1<=h,hprime<=J; then multiply by mu_C(b)^(2^a).

Application hypotheses: Fixed a>=2, C1<C2<C3 and q<=A^C1, n*A^-C3<=J<=n*A^-C2. For p not dividing W*q the cube gradients give 1+O_a(p^-2). For p>v dividing q use 1+O_a(p^-1); log q=O(v) gives O(v/log v) such primes.

Conventions: Difference-multiset local norm convention. First n tends to infinity at fixed v, then v increases.

Connecting argument retained from the scoped application: Reproduce the source local-factor calculation explicitly: centered common term cancels and the remaining cutoff error is O(1/log v); this is a proof adaptation, not an Artin conclusion quoted from Proposition6.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-MODEL

Published input, project paraphrase: The dense-model theorem supplies a bounded model for an arbitrary function dominated by the prescribed prime majorant, with the stated norm-testing accuracy. The special model1 for the prime weight is not the arbitrary-function conclusion.

Retained published locator: Theorem11, published p28.

Application objects: Bounded model of arbitrary f_(j,b) dominated by the normalized ordinary prime weight.

Application hypotheses: 0<=Lambda_jprime<=Lambda_prime. Set rho_star=rho/B0 and Acal=A^B0; the model majorant cutoff n^rho_star is no larger than the input truncation n^rho. Choose fixed complexities before rho and v.

Conventions: Use the arbitrary-function assertion, not the special model 1 for the ordinary prime weight. A single model must be accurate for both global and local norm tests.

Connecting argument retained from the scoped application: Transfer eq:gaussian-global-gowers to the bounded model minus mu_j(b). Published numbering replaces arXiv-v1 Theorem3.1.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-MODEL-COROLLARY

Published input, project paraphrase: The model approximation corollary supplies simultaneous approximation for the permitted global and polynomial local norm tests using the same bounded model, with the stated scale and coefficient restrictions.

Retained published locator: Corollary3, published p38.

Application objects: Apply simultaneous model approximation with M1=floor(floor(T/W)/A), q<=A^(B0*a), J=floor(A^(-2B0*a)*M1^2).

Application hypotheses: A^-3*sqrt(n)<=M1<=sqrt(n); slow v ensures the required logarithmic lower bound. Local step polynomials have degree1 and coefficients O(A^C), within the Acal allowance. B0>C+2 is chosen before a and small rho.

Conventions: The same bounded model is used in all norm comparisons.

Connecting argument retained from the scoped application: Approximation covers the global q[J] tests and polynomial local box norms together; after concatenation transfer smallness back to the unbounded centered weight.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-CONCAT

Published input, project paraphrase: For a bounded function satisfying the required small global norms over the permitted steps and scales, the concatenation theorem gives small averaged local polynomial box norms, with the stated complexity-dependent order and thresholds.

Retained published locator: Theorem9, published p21.

Application objects: Apply to the bounded model minus mu_j(b), using global order a chosen from the desired local order.

Application hypotheses: Global q[J] norms are small at all required q,J. n>Acal^-1*M1^2, with Acal=A^B0. Parameter order fixes local complexity, B0, a and rho before v.

Conventions: The local smallness threshold is independent of Acal. Bounded rescaling if needed is fixed.

Connecting argument retained from the scoped application: Small global Gowers norms give small averaged local polynomial box norms. Published numbering replaces arXiv-v1 Theorem2.5.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-POLYNOMIAL-GN

Published input, project paraphrase: The polynomial generalized von Neumann estimate makes the stated multilinear average small when one factor has the required small local box norm and all factors meet the ordinary-majorant domination and polynomial nondegeneracy hypotheses.

Retained published locator: Theorem13 and equation(57), published p41.

Application objects: After u=W*x+b,w=W*m+c, use integer shifts P_j(m)=c_j*W*m^2+2*c_j*c*m+(b+c_j*c^2-b_j)/W.

Application hypotheses: Distinct c_j yield nonzero leading-coefficient differences. Coefficients O(W) satisfy fixed chosen coefficient allowances. Each non-main expansion term has one centered factor with vanishing local norm; all other factors satisfy the ordinary-majorant domination.

Conventions: Boundary localization is handled separately, not discarded using a pointwise logarithmic bound. Admissible residue mass is bounded uniformly in v.

Connecting argument retained from the scoped application: All centered polynomial products are negligible, leaving the explicit singular series. Published numbering replaces arXiv-v1 Theorem4.1.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-GA-TZ-MAJORANT

Published input, project paraphrase: The normalized ordinary-prime divisor-sum construction supplies the model and polynomial-forms majorant with the specified domination and moment estimates for a fixed family and sufficiently small sieve exponent.

Retained published locator: Equation(36) p29, Proposition2 p30, and AppendixA polynomial-forms verification.

Application objects: Ordinary polynomial majorant nu_b for W=E*primorial(v), fixed E, and unit b modulo W.

Application hypotheses: Unit residues exclude every divisor condition at primes dividing W, regardless of their exponents. Remaining local factors are unchanged; fixed E is absorbed into coefficient bounds. Choose small sieve exponent after all fixed polynomial complexities.

Conventions: This is an explicit fixed-E adaptation of the source construction. Nu concerns ordinary primes and does not itself imply ray-prime equidistribution.

Connecting argument retained from the scoped application: Provides the model/GN majorants and the polynomial moments used for the boundary argument.

Version qualification: Retain the exact source versions and source inspection scope in SOURCES.json.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

## V6-AUDIT-KL-RAYS

Published input, project paraphrase: The published ray-class existence, exact sequence and reciprocity theorems identify the ray class field and its Artin map. For the maximal Gaussian order with no real places, the residue-unit quotient by global units gives the ray group, with arithmetic Frobenius convention.

Retained published locator: Theorems1.1 (p.4),1.3 (p.5),6.5 (p.42),7.2 (pp.47–48), Remark7.3 (p.48)

Application objects: Published theorem labels used directly. Milne course-note citation replaced.

Application hypotheses: Base field Q(i), maximal order Z[i], finite nonzero modulusHZ[i], no real places. Class number1 gives ray quotient of residue units by four Gaussian units. Stable modulus under conjugation gives ray extension Galois overQ. H0 divisible16 makes unit embedding injective; added primes avoid2H0.

Conventions: Arithmetic Frobenius x↦x^Norm(p) is explicit in publishedTheorem7.2. Ideal Artin class of(r), not inverse class, defines residue h_r. Cyclotomic restriction is exponentNorm(r). No division by four in new residue kernel oncebase representative fixed.

Connecting argument retained from the scoped application: Derive exact kernel∏Bℓ, commutators∏kerNorm, abelian quotient, and surviving norm-fibre proportions at least1−4/(ℓ−1). The product quotient is established by the unramified-intersection and degree argument, not by trivial conjugation alone.

Version qualification: Source versions and scope are qualified in the 2026-11-06 reports; not formal verification or full-manuscript validation.

This card supplies the stated external input. Its application hypotheses, current consumer identity and any further local deductions remain separate obligations.

