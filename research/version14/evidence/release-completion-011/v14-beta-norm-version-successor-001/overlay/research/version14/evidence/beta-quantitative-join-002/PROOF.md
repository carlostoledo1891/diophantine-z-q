# Quantitative descent and level for the original beta family

Author: `/root/v14_arithmetic_author`. This is a new connecting-proof proposal, not an independent acceptance. It concerns the first, discriminant-six beta family only. It supplies the two quantitative inputs consumed by H6-A014-JACOBIAN-HEIGHT and H6-A015-REVERSE-ISOGENY. The D210 b-family is not used.

## Inputs and their identities

Retain the original surface A/K and its base change to L from the first height proof. The normalized-cover construction supplies K/Q normal of degree at most F0, T=S union supp(M), and good reduction of A outside places over S. Here M=M_S(u) is the positive squarefree product in the manuscript; the empty product is one. The full-endomorphism-field construction supplies L/Q normal, d=[L:Q]<=D, unramified outside T. These are genuine incoming geometric inputs, not consequences of this quantitative argument.

Retain the actual normalized maps a_sigma mu_sigma, the sign cochain beta, and the original matrix-unit factors r_ell. The current A007 construction gives beta squared equal to chi, its prescribed sign coboundary, and after the quadratic correction a conjugation-invariant character beta|G_L. Its kernel defines the actual L-prime. On G_L the inflated maps and positive normalization scalars are identities. The original family is unramified outside T union {ell}. The accepted beta all-prime comparison identifies these same r_ell with the realizations of the same final primitive weight-two form f; direct Carayol then identifies their local Artin conductor with the primitive-level exponent when ell differs from the residue characteristic.

Use exactly the manuscript constants

    G0 = 116064000000,
    E0 = 10(D G0)^2,
    U0 = 4(D G0)^2,
    Q = R^(R E0),
    R >= max(D, max(S), 10^12).

No auxiliary comparison field replaces L or L-prime, and no degree of such a field enters these constants.

## The actual kernel degree

The selected local characters give m=order(chi)<=2 R^R M. Indeed their order divides the least common multiple of the selected orders, hence at most twice the product of p-1 over the selected odd primes in T. The factors at p<=R contribute at most R^R; those at p>R contribute at most M, because every such prime of T lies in supp(M).

The corrected beta still takes values in mu_(2m), so

    d-prime = [L-prime:Q] <= 2m d <= 4 R^(R+1) M <= Q M.

For the final inequality, R>=10^12 implies 4<=R, and E0>=10 implies R+2<=R E0. Thus 4 R^(R+1)<=R^(R+2)<=R^(R E0). This uses the actual kernel field and preserves the first family's m bound. It is not the separate b-family bound 2304R. Also Q>=10^12 and M>=1.

## The retained local ramification calculation

The detailed derivative and subgroup calculation is already independently checked in the A012 section of the 2026-11-05 galois-height REPORT and in the independent A012-SECOND-REVIEW. Those reports identify the inspected source as Serre, Local Class Field Theory, Chapter VI in Cassels--Frohlich, sections4.1--4.3, printed155--159, not the uninspected Local Fields book. Their substantive calculation is retained here.

For an extension of Q_p of degree at most a, its normal closure has degree at most a!. Over the maximal unramified subfield of that closure, an Eisenstein polynomial f of degree e for a uniformizer has derivative terms with distinct valuations modulo e. Consequently there is no cancellation at the minimum and v(f'(pi))<=e-1+e v_p(e). The derivative product over inertia conjugates and the lower-group definition give d_diff=sum_(i>=0)(|G_i|-1). Changing variables with the Herbrand function gives

    d_diff/e = 1-1/e + integral_(u>0)(1-1/|G^u|) du.

Before the last positive upper break the integrand is at least one half. The last break is therefore at most 2(1+log_2(a!))<=4a^2. The unramified and tame cases satisfy the same bound. For a Galois subfield F/Q_p, the exact subgroup rule is G_Qp^u intersect G_F = G_F^(psi_F/Qp(u)), with psi(u)>=u for u>=0. The inverse Herbrand function, not phi, is used. The two cited independent reports give the derivative proof of this indexing identity and the normal-closure justification.

At any p put F=L_v. Adjoin A[3], except at p=3 adjoin A[5]. The degree over Q_p is at most D G0: G0=|GL4(F5)| dominates |GL4(F3)|. Silverberg--Zarhin1995 Theorem3.5, printed406, has n>=3 and n prime to p; over F(A[n]) its required unramified torsion premise is satisfied by the identity extension. The A013 acceptance checks this exact scan and the semistability hypothesis. Pass to a normal closure if necessary. For ell different from p, semistability makes inertia unipotent. A stable ell-adic lattice shows that the pro-p wild image is finite, since the congruence kernel is pro-ell; a finite unipotent subgroup in characteristic zero is trivial. Thus absolute upper groups with u>U0 act trivially on V_ell(A) and lie in G_L.

On those groups the a_sigma mu_sigma factor is one. For odd p, chi is tame; beta squared is chi, so beta on wild pro-p inertia has order dividing two and is trivial. At p=2 the non-2 Dirichlet factors of chi are unramified and its possible factor modulo4 has order at most two on Q_2-units. Local reciprocity's norm compatibility gives chi|G_F(x)=chi(N_F/Q2(x)); apply it to the finite cyclic character field cut out by local chi. The local norm-functoriality locator is Milne, Class Field Theory, v4.03, III Lemma3.2, printed107, first diagram; the earlier V Proposition3.3 locator is the global ideal diagram. Norms of units are units. Hence beta^4=chi^2=1 on O_F^*. This uses the finite-abelian norm functoriality itself, not only a quadratic example of it.

Write e=v_F(2)<=D. Logarithm and exponential are inverse on U_F^(e+1) and the ideal m_F^(e+1); the nonlinear series terms have strictly larger valuation there. Multiplication by four gives

    (U_F^(e+1))^4 = U_F^(3e+1).

Thus beta is trivial on U_F^(3e+1), its relative last upper break is at most 3e, and the subgroup rule makes it trivial on absolute upper groups above max(4D^2,3e)<=U0. This is the actual beta character over F, not a bound obtained from [L-prime:Q].

The two-dimensional r_ell therefore has tame invariant codimension at most two and Swan conductor at most 2U0. Possible infinite tame unipotent monodromy does not alter this wild integral. For every p and ell different from p,

    a_p(r_ell) <= 2+2U0 <= E0.

## Large primes and the primitive level

If p>R, then p is outside S, so the original A has good reduction at each place of L above p by base change from the supplied good-reduction model over K. Also [L_v:Q_p]<=D<p, so L_v/Q_p is tame. Absolute wild inertia lies in G_L, acts trivially on the good-reduction Tate module, and is killed by the odd-prime beta argument. Hence a_p(r_ell)<=2. Outside T the original normalized family is unramified, so its exponent is zero.

For each residue prime choose ell different from it. The accepted same-beta all-prime isomorphism and the separate direct Carayol theorem give a_p(r_ell)=v_p(N) for the same final primitive form f. This includes dyadic and bad primes. Since T=S union supp(M) and every prime in S is at most R,

    N <= product_(p<=R) p^E0 * product_(p>R,p|M) p^2
      <= R^(R E0) M^2 = Q M^2.

The bound for small primes uses at most R primes, each at most R. Including the small prime factors of M again in M squared only weakens the inequality. The auxiliary choice of ell and the finite set used for trace comparison do not enlarge T.

## Exact output and boundary

The output is d-prime<=Q M and N<=Q M^2, together with Q>=10^12 and M>=1, for the same beta A, L-prime and primitive f. H6-A015 uses the kernel-field degree bound and H6-A014 uses the primitive-level bound. The ordinary Tate restriction, the A063 Hom/complement construction, the direction of its isogeny and all height inequalities remain separate inputs or consumers. This proof supplies none of them by inference from the two numerical bounds.
