# Source-side transport audit, working draft

Author: /root/v14_gi_selection_review. This is an authored proposal awaiting independent review. No canonical source is changed.

## Coefficient conjugation at main 14669–14679

Use Ramsey's section model, Definition 3.1 and Sections 3–4, with k=3 and a characteristic-zero coefficient field containing the character values and the chosen root of unity of order 4N. A field automorphism preserves the defining divisor and the cusp-vanishing condition, and sends the diamond character psi to tau(psi). This uses field base change only. It does not use the k>=5 vanishing theorem.

There is a cusp convention to account for. The q-expansion of the conjugated section at the conjugated Tate marking is the coefficientwise conjugate expansion. If tau(zeta)=zeta^a, the conjugated marking differs from the fixed marking by diamond a. Since the section is a diamond eigenvector, the two expansions differ by one nonzero constant. Rescale the conjugated section by that constant. Its classical expansion is then exactly coefficientwise conjugation of g. Theta at the standard Tate marking has rational coefficients, so the same conclusion holds after multiplication by theta^3 in Ramsey's q-expansion convention. This supplies coefficientwise conjugation without assuming that the chosen cyclotomic cusp is rational.

Ramsey Theorem 6.2, specialized to k=3, gives T(p^2) coefficients a(p^2 n)+psi(p)(-n/p)a(n)+p psi(p^2)a(n/p^2). All factors other than character values are rational. Conjugating this formula shows that the new good eigenvalues are tau(eta(p)) a_p(E), provided a_p(E) is the separately supplied rational elliptic-curve trace. Thus the claimed eta(p)^e a_p(E) follows.

## Still to bind

The finite-character twist at main 14680–14685 needs its own half-integral-weight transformation theorem, including cusp holomorphy and level support. A published lead is Shimura (1973), Lemma 3.6; no acceptance is asserted before the exact primary statement is read. The existing full-eigenspace proportionality result is a separate input for 14687–14698, with D0 coprime to the character conductor and a(D0)=1 retained.

For main 14420–14510, the general common-cover calculation at 15320–15401 is a candidate supplier for the normalized unit action. Its general Q0=three-squares specialization must be separated from the later B0-specific determinant cancellation. Finite order of the Weil-index multiplier and the global rational central-element product relation still require exact source bindings.

For main 14511–14524, Waldspurger's unramified normalized c_p^0 and local Whittaker factorization require their own exact source paragraphs. Nonzero packet existence alone does not supply them.

## Verified local-index source

Weil, Sur certains groupes d'operateurs unitaires, II.25 Proposition 3 and II.28 Proposition 4 with its consequence (28), printed pp.173–177, explicitly gives multiplicativity for orthogonal sums and gamma(f)^8=1. Applied to Q0 and uQ0, this makes r_Q0(u)=gamma(uQ0)/gamma(Q0) an eighth root of unity. The retained main calculation 15320–15401 derives its Hilbert-symbol cocycle and the diagonal/unipotent conjugation relation on the common double cover. Thus division by r_Q0 gives an honest action of the units; this inference does not require the B0 determinant to be a square. The dyadic relation M_Q(-1)^2=-id belongs to the unnormalized genuine action; after division by the theta-cubed scalar, the normalized unit action has square one at -1. This distinction must remain in the final binding.

## Alternative direct finite-translation proof, pending review

Let g have weight k/2 for odd k, level L divisible by 4, and character psi; let nu be primitive of conductor m. Set h(z)=G(bar(nu))^{-1} sum over t mod m of bar(nu)(t) g(z+t/m). The elementary Gauss identity gives h=sum nu(n)a(n)q^n. For gamma=(a,b;c,d) in Gamma0(L*m^2), choose t' congruent to d^2*t modulo m. Then n(t/m)*gamma=gamma_t*n(t'/m), where gamma_t is integral of determinant one, has lower-left entry c and lower-right d'=d-c*t'/m, and lies in Gamma0(L).

The theta multiplier in Ramsey p.600 is unchanged in this identity. Indeed d' is congruent to d modulo L and modulo 4, so psi(d')=psi(d) and epsilon(d')=epsilon(d). Also (c/d')=(c/d): writing c=s*r^2 with signed squarefree s, the symbol on odd denominators coprime to c is (s/d); its conductor divides 4*abs(s), and 4*abs(s) divides c/m when L is divisible by 4 and m^2 divides c/L. Thus the difference d'-d is divisible by this conductor. The case c=0 follows directly from integral translation invariance. The square-root argument is identical because c*(z+t'/m)+d'=cz+d.

Reindexing the sum by t' gives bar(nu)(d^{-2}t')=nu(d)^2*bar(nu)(t'). Therefore h transforms with character psi*nu^2 at level L*m^2. Each rational translation sends a rational cusp to a rational cusp. In a local cusp coordinate it rescales the imaginary variable by a positive rational number, so the vanishing expansion of g remains a vanishing expansion after taking a common cusp width. The finite sum is therefore cuspidal. The trivial character m=1 gives h=g directly. For an imprimitive presentation use its inducing primitive character; the needed coefficients at D and D0 are unchanged because these integers are prime to the original support. This preserves level prime support.

At primes p away from L*m, the k=3 Hecke coefficient formula shows the eigenvalue changes by nu(p)^2. Its middle term uses nu(p)^2*nu(n) when (n/p) is nonzero; its last term uses nu(n/p^2)=nu(n)/nu(p)^2. This proves the asserted eigenvalue relation without assuming twist modularity as an input.

## Global parity and the unramified factors, pending independent check

The selected packet is a genuine cuspidal automorphic representation with holomorphic archimedean lowest weight 3/2. The product of its local central actions on rational -I is one, by left invariance of automorphic forms under the rational splitting. The reference theta-cubed representation has the same archimedean central action. Weil II.30 Proposition 5, printed p.179, gives the product of the local indices equal to one for each rational quadratic form; applied to Q0 and -Q0 it gives the compatible rational product relation for the theta-cubed normalization. Taking the quotient of the two central product relations cancels the archimedean factor. The finite quotient character consequently has value one at -1. The locally chosen alpha(-1)=delta is precisely what retains this quotient action in the selected vector. This uses the actual holomorphic weight and rational automorphic splitting as inputs, not as conclusions of the finite projector calculation.

Waldspurger 1981 I.3(5), printed pp.377–378, applies at odd p away from both the automorphic conductor and the character conductor. It gives the unique normalized unramified coefficient function c_p^0 with value one when the argument has valuation zero or one. Since S0 contains 2 and those conductors, and the reference D0 is squarefree, these are exactly the needed valuations even at primes dividing D0. The existence of the initial nonzero reference functional is a separate retained packet input. For a fixed such functional, tensor factorization follows from local Whittaker uniqueness; Waldspurger explicitly uses this product decomposition in the proof of IV.4 Lemma 6, printed p.396. Thus replacing finitely many local vectors by ones with nonzero reference functional, and using the normalized spherical factors outside S0, preserves a nonzero reference coefficient. This is not a claim that every nonzero local vector has nonzero reference functional.
