# Full quaternion compatibility for the H5 normalizer maps

This is an author connection for independent review. It supplies the full B-intertwining and prime-to-11 properties required at the actual H5 callers. It does not assert a new compatible-system theorem, a coherent descent datum, bounded descent to Q, or any new conductor bound.

## 1. Exact objects and retained geometric input

Let B be the rational indefinite quaternion division algebra of discriminant210, O the fixed maximal order, and A/L an actual non-CM surface in the full-three fiber. Retain the already established all-component identification with the rational PEL moduli problem, its canonical right normalizer action and its compatibility with the maximal-level forgetful map. The full-cover proof sections6-7 supplies these inputs with the rational B-action retained. Retain also End^0(A_Qbar)=B and the simultaneous statement that every geometric homomorphism between these fiber surfaces is defined over the same L. These are separately accepted inputs, not consequences of the scalar calculation below.

The rational PEL group is the centralizer of the left B-action. Under a fixed complex embedding, a point represented by (h,a) has a rational left B-module V, Hodge structure h, and lattice Lambda=V intersect a(Ohat). Its right normalizer translate by n has the same V and h and lattice Lambda_n=V intersect a n(Ohat). The accepted integral-lattice equivalence identifies these objects with the actual fiber surfaces, including their O-labels. Thus this is not a comparison of unnamed isogenous tori. Opposite action conventions replace n by its inverse and do not change the argument; here n denotes the representative for the actual canonical right action.

## 2. B-linear maps on every component

The identity on V commutes with B and preserves h. Since Lambda and Lambda_n are commensurable, multiplication by a nonzero rational number c with c Lambda_n contained in Lambda gives a holomorphic homomorphism from the translated surface A_n to A. It is an isogeny because the two lattices have the same rank. The equivalence between complex abelian varieties and their polarized Hodge lattices makes this homomorphism algebraic. Its B-linearity is the identity c i_n(x)=i(x)c, first for x in O and then for x in B after rationalization. The previously accepted two-surface Hom descent places it over Qbar and then over L. Changing the full-three marking is an O-linear isomorphism and can be composed on either side without changing this conclusion.

This argument works on every component: the right finite-adelic action retains h and the rational B-module. It does not replace the two-half-plane PEL datum by an unexplained single-half-plane datum, nor does it require a new choice of a positive rational normalizer representative to prove existence.

For comparison with the formula already printed in H5, final Voight43.1.2 uses the upper half-plane and fixes a real embedding i_infinity. It defines Lambda_z=i_infinity(O)(z,1)^t and i_z=i_infinity as the labeled order action on A_z=C^2/Lambda_z. The rational normalizer quotient acting on the maximal-level curve is43.1.3. On a positive rational normalizer chart let b=(a,b';c,d), z'=bz and lambda=cz+d. Then lambda is nonzero and

    lambda (z',1)^t = b (z,1)^t.

If O b is contained in O, the scalar map lambda I therefore sends Lambda_z' to O b(z,1)^t contained in Lambda_z. It gives A_bz to A_z, the direction mu_sigma: sigma A to A required by H5. Both labeled actions are the same left matrix action i_infinity(x), so lambda I intertwines every x in B. There is no conjugation of the chosen quadratic subfield substituted for this full-algebra identity. Its degree is [O:O b]=Nrd(b)^2: after a real splitting, right multiplication by b on the four-dimensional matrix space has determinant det(b)^2. This chart calculation agrees with the rational B-linear lattice description above.

## 3. Prime-to-11 normalization without losing B-linearity

At11 the algebra is split and its maximal order is a matrix maximal order. Its normalizer is Q_11^* O_11^*. One elementary verification reduces to M_2(Z_11): if x normalizes that ring, x Z_11^2 is stable under its matrix units. The diagonal units split this lattice into two fractional ideals; the off-diagonal units force the ideals to coincide. Hence x Z_11^2=q Z_11^2 and x=q u with u in GL_2(Z_11).

Consequently Lambda_n,11=q Lambda_11. Multiply the rational identity map by r=11^(-v_11(q)); then r Lambda_n,11=Lambda_11. Relative to Z-bases of the two global lattices, the rational map r has matrix entries integral at11. Clearing their finitely many denominators therefore requires an integer m prime to11. For c=mr, one has c Lambda_n contained in Lambda and equality after tensoring with Z_11. Its finite lattice cokernel has order prime to11. Thus the resulting actual B-linear isogeny A_n to A has degree prime to11.

In the positive rational chart this is the same permitted operation on b: first multiply b by a rational power of11 so that b_11 lies in O_11^*, then clear remaining O-basis denominators by an integer prime to11. Central rational rescaling preserves the normalizer class, its action on z, positivity of its reduced norm, and scalar B-intertwining. The normalized norm is an11-adic unit, so its squared norm degree is prime to11. No arbitrary Skolem-Noether element is inserted. No claim is made that all other prime factors of the isogeny degree are bounded or belong to a smaller fixed set.

## 4. Actual finite choices and downstream boundary

For each element sigma of the finite group Gal(L/Q), use its actual normalizer translate and choose one such B-compatible isogeny mu_sigma: sigma A to A over L; choose mu_1=1. Inflating this finite choice gives exactly the family requested at H5's scalar-lift paragraph. For sigma,tau the map

    mu_sigma * sigma(mu_tau) * mu_sigma_tau^(-1)

is an invertible rational endomorphism of A commuting with B. Since End^0(A_Qbar)=B, it is in the center Q^*. Associativity gives the scalar two-cocycle identity. This does not assert that the discrepancies are already1 or that the isogenies form a descent datum.

Applying rational Tate modules to these same algebraic maps gives B-intertwiners for every coefficient prime, functorially and with the same composition identities. This is all-prime realization of fixed algebraic maps, not by itself equality of Frobenius polynomials for the subsequently corrected representations. The existing later paragraphs separately normalize degrees, construct and control the sign-splitting cochain, and compare traces through reduction of isogenies composed with Frobenius. Those arguments and their source obligations remain unchanged.

The prime-to-11 maps also give the actual isomorphisms on11-torsion used to compare the kernels for A and its conjugates. Thus the family serves both the normality-of-L(A[11]) caller and the full-B scalar-discrepancy caller, without replacing the controlled family by merely quadratic-field-linear isogenies.
