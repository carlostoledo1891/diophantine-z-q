# Rational discrepancy and positive degree normalization

Author proposal. Independent review is pending. Exact published inputs and proposed manuscript insertions are recorded in SOURCE-ATTACHMENT.md. This note makes no claim that Item 2.9 or Version 14 is accepted.

## Precise algebraic statement

Let A be an abelian surface over an algebraic closure of a characteristic-zero field. Suppose quasi-isogenies mu_sigma: sigma A -> A satisfy

    mu_sigma o sigma(mu_tau) = c(sigma,tau) mu_sigma_tau,

where c(sigma,tau) belongs to Q*. The rationality of this discrepancy is an input. It does not follow from the dimension of A alone. In particular it must be checked against the actual endomorphism algebra and chosen equivariance condition.

Use the usual degree of a genuine isogeny. The external input is Milne, Abelian Varieties, Arithmetic Geometry, Springer, 1986, Theorem 8.2 and its preceding paragraph, printed p. 115, with proof on p. 116: deg([n]_A)=n^(2 dim A), hence n^4 here, and multiplicativity of degree. The degree is the rank of a finite locally free map, which is unchanged under field conjugation. For negative n use the degree-one automorphism [-1]. The actual published pages were visually checked; their exact image hashes are in SOURCE-ATTACHMENT.md.

For a quasi-isogeny u define D(u)=deg([m]u)/m^4, where m is any positive integer clearing its denominators. This is independent of m. Indeed, if m and n both clear the denominators, then

    deg([n]([m]u)) = n^4 deg([m]u)
    deg([m]([n]u)) = m^4 deg([n]u),

and the two maps coincide. Thus their degrees coincide and the two quotients agree. A common denominator proves D(uv)=D(u)D(v), and conjugating an integral representative proves D(sigma u)=D(u). Also D(id)=1, so D(u^-1)=D(u)^-1.

For c=a/b in Q*, with a a nonzero integer and b a positive integer, use a denominator divisible by b and the multiplication-degree theorem to obtain

    D(cu)=c^4 D(u).

No degree is being assigned directly to a nonexistent algebraic morphism [1/b]. This formula uses the preceding definition on rational quasi-isogenies.

Set d_sigma=D(mu_sigma)^(1/4), choosing the positive real fourth root. These are positive real algebraic numbers. The discrepancy identity gives

    d_sigma d_tau = |c(sigma,tau)| d_sigma_tau.

Consequently its normalized scalar cocycle is

    epsilon(sigma,tau)
      = c(sigma,tau) d_sigma_tau / (d_sigma d_tau)
      = c(sigma,tau)/|c(sigma,tau)| in {+1,-1}.

Equivalently nu_sigma=d_sigma^-1 mu_sigma satisfies nu_sigma sigma(nu_tau)=epsilon(sigma,tau)nu_sigma_tau after extending the rational Hom spaces by real algebraic scalar coefficients, with trivial Galois action on this auxiliary coefficient field. The normalized nu_sigma are formal scalar-extended homomorphisms; the argument does not assert that they remain algebraic quasi-isogenies. One can avoid this notation entirely and use the displayed scalar cocycle formula. The cocycle identity follows by multiplying the original cocycle by the coboundary of d^-1. Positivity removes the fourth-root ambiguity.

## Separate finite-cochain obligation

This calculation proves that epsilon is sign-valued. It does not prove that its class is zero, produce a splitting cochain, or imply that a splitting cochain has finite image. If a later construction requires such a cochain, its domain, continuity, coefficient action and splitting theorem must be supplied separately. Sign-valued cocycles need not be coboundaries on an arbitrary fixed finite quotient. Likewise continuity or finite image of d requires the corresponding property of the chosen mu_sigma family; it is not a consequence of pointwise degree normalization.

## Conductor bridge, conditional on the actual representations

Fix a rational prime p and choose an auxiliary prime ell different from p. Suppose the actual geometric and modular two-dimensional ell-adic representations in one specified family are isomorphic as G_Q representations. Restriction gives an isomorphism on a decomposition group at p and on every inertia and ramification subgroup. The dimensions of inertia-invariants agree, as do all terms defining the Swan conductor. Therefore their Artin conductor exponents agree. This argument works separately for each constructed family; an isomorphism or endomorphism calculation for the b-family does not supply the beta-family premise.

An independent local compatibility/conductor theorem must identify the modular representation exponent with v_p(N_f), where N_f is the primitive newform's level. That theorem must cover p dividing N_f and the actual coefficient embedding. The Tate-module identification alone does not supply this assertion. A fixed auxiliary prime ell=3 cannot be used for this argument at p=3. To state a product conductor formula for a larger Tate module, the direct-sum multiplicities and coefficient-field degrees must also be checked explicitly.

## Pending exact attachments

The published degree theorem and conductor provider have now been read. SOURCE-ATTACHMENT.md records exact locators and separates them from the family-specific premises. The current manuscript passage and its hash were supplied by root; this author's own full passage readback remains pending. Independent acceptance, final family-specific bindings, and final incorporated-manuscript review remain separate. No canonical manuscript was edited.
