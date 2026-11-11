# The same modular form at coefficient primes five and three

Author proposal. This argument concerns the family in the current manuscript at lines 8100–8139 and its use at 8218–8222. It does not replace the controlled field, cochain, exceptional set, or representations of that construction.

## Inputs and conventions

Let A be the given abelian surface. Retain the actual locally constant isogenies mu_sigma from sigma A to A, defined over the original L, and the scalar t_sigma=a_sigma/b(sigma), where a_sigma=(deg mu_sigma)^(-1/4) is the chosen positive algebraic fourth root. Only b is asserted to be root-of-unity valued. Their cocycle identity makes rho_l(sigma)=t_sigma mu_sigma composed with sigma a representation commuting with B. After the fixed splitting, rho_l is the direct sum of two copies of r_l. The existing construction supplies absolute irreducibility of the original r_3 and identifies the original r_5 with the realization of the selected primitive weight-two form f.

The phrase sigma A uses the convention fixed by this composition. Applying sigma to point coordinates gives the semilinear map from A to sigma A. This source and target identification is required. It is not a consequence of a quaternion-algebra isomorphism alone.

Choose one finite Galois number field K defining A, the finitely many quasi-isogenies and their twists, and the finite choices in the scalar cochain. Choose a positive integer m clearing all their denominators. These are auxiliary comparison choices. Neither K nor the comparison exceptional set below replaces the manuscript's controlled L-prime or T.

## Reduction and the degree polynomial

After removing finitely many rational primes, these finite data spread to smooth proper abelian schemes, and every m mu_sigma is a homomorphism of the corresponding schemes. This follows by spreading their finite equations and morphism charts and removing the finitely many primes where the charts, group identities, smoothness, or proper models fail. Include the primes ramified in K. Call this finite comparison set S. Its size is not used in a conductor estimate.

For p outside S and a chosen place v of K above p, choose an arithmetic Frobenius lift sigma_p in the decomposition group. On the residue field it acts by x mapping to x^p, even when the residue degree is greater than one. Reduction identifies sigma_p A with the p-Frobenius twist of A_v. Thus

    e_p = reduction(m mu_sigma_p) composed with Fr_{p,A_v}

is an endomorphism of A_v. Here Fr_p is the relative p-Frobenius from A_v to its p-twist. It must not be replaced by the q-Frobenius for q equal to the residue-field cardinality, which would represent a different power of sigma_p.

Milne, *Abelian Varieties* (1986), printed page 125, Proposition 12.9 and the preceding definition, assign every rational endomorphism alpha of an abelian variety over any field a monic rational degree polynomial P_alpha. For every l different from the field characteristic, this is the characteristic polynomial on V_l. In particular, the characteristic polynomial of e_p is independent of l. Equivalently one may apply the same statement directly to e_p/m in End^0(A_v). Its trace q_p lies in Q and equals Tr(e_p)/m. This explicitly retains the denominator scaling.

For l different from p, multiplication by l^n on an abelian scheme has finite etale kernel. It is proper with finite geometric fibers, and its differential is the invertible scalar l^n, so it is etale. Over the strict henselization of the local base, a finite etale scheme is a disjoint union of sections. Reduction therefore gives the bijection on l-power torsion, compatibly with the transition maps and with the spread homomorphism m mu_sigma_p. Under this identification the action of sigma_p is the relative p-Frobenius with the twist just specified. Passing to rational Tate modules identifies mu_sigma_p composed with sigma_p with e_p/m. Consequently

    Tr(r_l(sigma_p)) = (1/2) iota_l(t_sigma_p) q_p.

The factor one half comes from rho_l = r_l direct-sum r_l, not from an identification of a single matrix corner with the whole Tate module.

## One algebraic trace and the prime-three realization

Let E contain the original scalar and splitting field and the coefficients of f. Choose iota_5:E to Qbar_5 extending the embedding used in the known identification at five. Independently choose iota_3:E to Qbar_3 extending the already fixed prime-three embedding of the original scalar and splitting field. The quantity tau_p=t_sigma_p q_p/2 is an element of E before any coefficient-prime embedding.

Let U_{f,3} be the two-dimensional classical realization with its stated good-prime traces; no separate semisimplicity hypothesis on this realization is required here. For p also away from 3, 5 and the level of f, equality r_5=U_{f,5} gives iota_5(tau_p)=iota_5(a_p(f)). Injectivity of this embedding gives equality in E. Applying iota_3 gives equality of the traces of r_3 and U_{f,3} at all primes outside a finite set. Semisimplification preserves every trace. Chebotarev density and Brauer–Nesbitt therefore identify the absolutely irreducible r_3 with the semisimplification of U_{f,3}. A finite-dimensional representation has the same composition factors as its semisimplification. Since that semisimplification is one simple two-dimensional factor, U_{f,3} has composition length one and is itself irreducible. Thus the conclusion is an isomorphism with U_{f,3} itself.

The finite exclusions in this comparison do not weaken the result to a restriction to a subgroup and do not enlarge T in the earlier ramification statements. The global representation isomorphism identifies their restrictions at 5. Thus the same f can be used with r_3 for its conductor at 5 and with r_5 at the other places, subject to the separately supplied conductor-realization theorem. This argument supplies no new numerical conductor bound.

## Remaining binding checks

The final ordinary projection must bind the actual normalizer/quasi-isogeny provider and its source-to-target convention, the common scalar field, the semisimplicity inputs, and the named Chebotarev/Brauer–Nesbitt providers. The original r_3/r_5 and a_sigma/b(sigma) are retained. The C6 Jacobian-placement application at 8140–8142 is separate.
