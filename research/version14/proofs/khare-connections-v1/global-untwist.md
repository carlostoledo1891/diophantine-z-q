# A global cyclotomic untwist for the lower-weight normalization callers

Authored proposal. Independent review and adoption are pending. This supplies only the global twisting input of normalization18. It does not re-prove that packet's local weight calculation or its lower-weight modularity inputs.

## 1. Objects, coefficients and conclusion

Fix embeddings i_infinity: Qbar -> C and i_P: Qbar -> Qbar_P. Let P be an odd prime and let r be an absolutely irreducible two-dimensional representation of G_Q over a finite field of characteristic P. Let omega_P be the mod-P cyclotomic character. Assume that r' = r tensor omega_P^e is modular: after a finite coefficient extension it is the reduction of a stable lattice T_f in the P-adic representation rho_f of a normalized primitive cuspidal eigenform f of weight w >= 2, some level N, and nebentype epsilon. A definition using semisimplified reduction gives the same input here, since r' is absolutely irreducible. All coefficient and residue-field identifications below use the fixed embeddings.

The conclusion is that r is modular, realized by a stable lattice in a primitive cuspidal eigenform H of the same weight w at some finite level. If e is zero modulo P-1, then r'=r and the conclusion is already the input. In the construction below assume e is nonzero modulo P-1. No least level, least weight, local ordinary filtration or U_P eigenvalue is asserted. In the actual nonordinary callers of normalization18,

    8 <= k <= P-1,  e = P+1-k,  w = P+3-k,

so P >= 11, e is even with 2 <= e <= P-7, and w is even and at least 4. These inequalities imply that the character used below is nontrivial. The ordinary and k=P+1 branches do not use this connection.

For each a in F_P^*, choose the algebraic root of unity eta(a) of order dividing P-1 whose image under i_P reduces to a^(-e). These choices define the finite Dirichlet character eta modulo P. It is primitive of conductor P because e is nonzero modulo P-1. Write eta also for its complex realization under i_infinity. Its Galois realization eta_G is defined explicitly through Gal(Q(zeta_P)/Q): an element sending zeta_P to zeta_P^a has value i_P(eta(a)). Thus at an arithmetic Frobenius at ell != P its value is i_P(eta(ell)), and its residual character is omega_P^(-e). There is no reciprocity-inverse ambiguity in this definition. In our callers eta(-1)=1. Enlarge the algebraic coefficient field to include the coefficients and nebentype of f, the values of eta, and zeta_P; subsequently enlarge it again if needed for H. All these extensions are finite.

## 2. The translated cusp form

Use the weight-w right slash action of GL_2^+(Q), including the factor det(g)^(w/2), as in final Li1975, p.285. Set u_a = [[1,a/P],[0,1]] and

    tau = sum_(a in F_P^*) eta(a)^(-1) zeta_P^a,
    F = tau^(-1) sum_(a in F_P^*) eta(a)^(-1) (f |_w u_a).

Here zeta_P in the analytic formula is exp(2 pi i/P), chosen within the fixed complex algebraic closure. The value tau is nonzero: substitution shows that the finite Fourier transform of the nonzero function a |-> eta(a)^(-1) (extended by zero at 0) has value eta(n) tau at every n != 0, and value zero at n=0. If tau vanished, all its Fourier coefficients would vanish, contradicting invertibility of the finite Fourier matrix. Consequently the Fourier series of F is

    F(q) = sum_(n>=1) eta(n) a_n(f) q^n,

where eta(n)=0 when P divides n. In particular a_1(F)=1. This also shows directly that its coefficients belong to a number field. No assertion that tau is a P-adic unit is used.

Put M = N P^2 and Psi = epsilon eta^2, regarded as a Dirichlet character modulo M. We prove F belongs to S_w(Gamma_0(M),Psi), including the character, without assuming P is prime to N. Let gamma = [[A,B],[C,D]] lie in Gamma_0(M). For each a in F_P^*, choose b in F_P^* with

    b = a D A^(-1) = a D^2 (mod P).

The matrix gamma_a = u_a gamma u_b^(-1) has entries

    A+aC/P,  B+(aD-Ab)/P-abC/P^2,
    C,        D-Cb/P.

They are integers, its determinant is one, and its lower-left entry is divisible by N. Its lower-right entry is congruent to D modulo N. Hence gamma_a is in Gamma_0(N) and

    f |_w u_a gamma = epsilon(D) f |_w u_b.

Relabeling a by b in the finite sum uses eta(a)^(-1) = eta(b)^(-1) eta(D)^2. It follows that F |_w gamma = Psi(D) F. The parity is correct: Psi(-1)=epsilon(-1)=(-1)^w; the stronger evenness of eta is available for our actual callers but is not needed for this equality.

Each rational translate is cuspidal at every rational cusp. Indeed, for sigma in SL_2(Z), choose gamma' in SL_2(Z) with gamma'(infinity)=u_a sigma(infinity). Then gamma'^(-1) u_a sigma is upper triangular with positive determinant. The expansion of f|gamma' has zero constant term, and the upper triangular change scales the imaginary part by a positive rational number. Its value therefore tends to zero at infinity. Holomorphy follows from the same rational change of variable and the finite-index cusp stabilizer. The finite sum F is a cusp form. This proves the stated membership and nonvanishing by elementary translation, not by an extension of a weight-two twisting theorem.

## 3. Good Hecke operators and a primitive form

For the good Hecke operator on an arbitrary G in S_w(Gamma0(L),chi), the standard double-coset normalization is

    (T_ell G)(z) = ell^(w-1) chi(ell) G(ell z)
                    + ell^(-1) sum_(a=0)^(ell-1) G((z+a)/ell),

when ell does not divide L. Expanding the finite sum gives coefficient b_(ell n)+chi(ell)ell^(w-1)b_(n/ell). This calculation does not assume G is new or is already an eigenvector. Final Li1975 p.287 explicitly gives this general-form coefficient expansion; p.294 uses its newform specialization, with the nebentype spaces defined on p.285. For our primitive input f and a prime ell not dividing NP it gives

    a_(ell n)(f) + epsilon(ell) ell^(w-1) a_(n/ell)(f)
      = a_ell(f) a_n(f),

where a_(n/ell)=0 if ell does not divide n. Apply the same formula with nebentype Psi to F. If P does not divide n, multiplicativity of eta, including eta(n/ell)=eta(n)/eta(ell), yields

    T_ell F = eta(ell) a_ell(f) F.

If P divides n, each coefficient in that identity is zero, so the identity still holds. The factor eta(ell)^2 in Psi is essential. No assertion about U_P is needed.

We now use the general-weight new/old decomposition on Li1975 p.294, with its notation C_epsilon(M,N) specialized to second level parameter 1. The new and old spaces are invariant under good Hecke operators; the good operators admit simultaneous eigenvectors, newforms have nonzero first coefficient, and an old common eigenform has a primitive newform at divisor level with the same good eigenvalues. Project F to the new and old summands. If its new projection is nonzero, it supplies the required normalized newform; equivalently one can take a simultaneous eigenvector in that projection. If it vanishes, use the stated oldform conclusion. In either case there is a normalized primitive cusp form H of weight w, at a divisor of M, with descended nebentype and

    a_ell(H) = eta(ell) a_ell(f)  for all primes ell not dividing NP.

The nebentype at those primes is Psi(ell). The finite-dimensional primitive-form and coefficient-field statements are used as published inputs; their ancestors are not reconstructed here. This step makes no claim of optimal conductor and does not require uniqueness of H.

## 4. Galois representation and the actual lattice

Use the published attachment recalled at the start of final Ghate--Vatsal2004, pp.2143-2144: for a normalized cuspidal eigenform of any integral weight at least two, the coefficient field is a number field, and the attached representation at a chosen prime has good Frobenius trace a_ell and determinant nebentype(ell) ell^(w-1). We use this recalled attachment statement only, before the ordinary hypothesis and equation (1.1); neither the main splitting theorem nor the ordinary theorem is needed. Use the arithmetic Frobenius convention, so the cyclotomic character takes value ell.

After embedding the finite coefficient fields into a common finite extension E of Q_P, rho_H and rho_f tensor eta_G have the same characteristic polynomials at every prime outside NP. Chebotarev density and continuity give equality of their traces on G_Q. Characteristic-zero Brauer--Nesbitt gives an isomorphism of their semisimplifications. These two standard inputs are retained through the exact trace-only source records identified in SOURCES.json; they do not require a compatible system or any ramified local comparison.

The residual absolute irreducibility of T_f implies absolute irreducibility of rho_f: an invariant proper line after finite scalar extension would intersect the extended lattice in a saturated rank-one submodule, yielding a proper invariant line in its residual representation. Thus rho_f tensor eta_G is absolutely irreducible. Equality of semisimplifications makes rho_H itself irreducible and gives an actual representation isomorphism after a finite coefficient extension, not only an equality of residual traces. Such an extension is finite because the intertwiner uses finitely many algebraic P-adic entries.

Twist T_f by the rank-one lattice with Galois character eta_G, and transport this lattice through that isomorphism to rho_H. Finite-order character values are units. The resulting stable lattice has reduction

    r' tensor bar(eta_G) = (r tensor omega_P^e) tensor omega_P^(-e) = r

over the same extended finite residue field. This identifies the actual residual representation. If the starting modularity assertion was phrased using semisimplification, absolute irreducibility already identifies the starting reduction with r'. No local ordering or chosen ordinary quotient is imported into this argument.

## 5. Exact use and retained boundaries

This supplies the global twisting sentence in normalization18, Sections 1, 4 and 6, when its nonordinary branch has already been proved modular in the previous weight range. The result returns modularity of the original r, so that branch stops. It is not used to construct the ordinary characteristic-zero lift in the other branch. For the finite callers it applies to P=11,k=10; P=19,k=14,16,18; and P=29,k=22,24,26,28. The P=7,k=8 and P=31,k=32 endpoint-only callers have no use. In the general caller it applies only to the nonordinary k<=P-1 branch, under the independently supplied lower-range modularity assertion; the normalization proof supplies w=P+3-k in that range.

The conclusion is modularity at some finite level and the same weight w as the modular input f. It does not by itself establish the minimal Serre level or weight of r, ordinary lifting, compatible systems, prime selection, or the full Serre theorem. Any later refined level/weight theorem remains its own input. Final Li's general-weight Hecke/newform input, final Ghate--Vatsal's recalled attachment, and Chebotarev/Brauer--Nesbitt are named imports; this packet neither re-proves all their ancestors nor claims independent acceptance. The weight-two Shimura1973 source is not used.
