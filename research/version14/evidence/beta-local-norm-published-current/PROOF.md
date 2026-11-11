# Local reciprocity and the norm

This note replaces the online-course-note input to ACTIVE-BETA-LOCAL-NORM. It proves only the local norm compatibility used there, from the published local class-formation statements below. It does not supply the separate logarithm, ramification or Tate-module estimates.

Let K be a nonarchimedean local field of characteristic zero and E/K a finite extension inside a fixed separable closure. Put G=G_K, H=G_E, d=[E:K], and C=(K^sep)^times, regarded as a discrete G-module. H need not be normal. Write i_ab:H^ab→G^ab for the map induced by inclusion. We prove rec_K(N_(E/K)u)=i_ab(rec_E(u)) for every u in E^times.

## Published inputs

Milne, Arithmetic Duality Theorems, second edition, BookSurge 2006, I(1.1b), printed17, states that the invariant isomorphisms H2(U,C)→Q/Z satisfy inv_H(res x)=d inv_G(x). Example1.6(b), printed19, supplies this class formation for the local field, not the global idele class formation. Remark1.5(a), printed18, characterizes reciprocity by chi(rec_K(c))=inv_G(c cup delta chi), where delta:H1(G,Q/Z)→H2(G,Z) is the connecting map. These three published pages were read directly. Their local class-formation and cup-pairing inputs are retained; no claim to reprove class field theory is made.

## Transfer calculation

Use a free group resolution and restrict it to the finite-index subgroup H. For an H-equivariant cochain f, corestriction is represented by Tr(f)(p)=sum_t t f(t^(-1)p), summing over left coset representatives for G/H. The sum is independent of the representatives, commutes with the differential and is G-equivariant. On G-equivariant cochains Tr(res f)=d f. The same construction with continuous cochains is valid for open H: there are finitely many cosets. Equivalently each cochain expression here descends to a sufficiently large finite Galois extension, and the identities persist on passage to continuous cohomology.

Choose the G-equivariant diagonal defining the cup product. If u is an H-invariant degree-zero element of C and z is a G-invariant Z-valued degree-two cocycle, equivariance of z shows term by term that Tr(u cup res z)=(sum_t t u) cup z. In multiplicative notation for C, sum_t t u is the product of all E/K embeddings of u, namely N_(E/K)u. Consequently cor(u cup res z)=N_(E/K)u cup z. This is the degree-zero projection formula needed here. No averaging or division by d is involved.

The restriction H2(G,C)→H2(H,C) is surjective, since under the two invariant isomorphisms it is multiplication by d on the divisible group Q/Z. Given y=res x, the transfer identity gives inv_G(cor y)=inv_G(d x)=d inv_G(x)=inv_H(y). Thus inv_G cor=inv_H. This does not cancel d in Q/Z; surjectivity supplies x before applying cor res=d.

For every continuous character chi:G→Q/Z, naturality of the connecting map and the preceding formulas give

    chi(rec_K(Nu)) = inv_G(Nu cup delta chi)
                    = inv_G cor(u cup res(delta chi))
                    = inv_H(u cup delta(res chi))
                    = (res chi)(rec_E(u)).

Continuous finite characters separate points of the profinite abelian group G^ab, proving the claimed identity. The calculation permits every open H, including nonnormal H. It therefore also gives the finite-quotient diagram after choosing a finite Galois compositum containing E and the character field. If both reciprocity maps are inverted to change the Frobenius convention, the same identity remains true; one must change both coherently.

## The actual beta caller

Apply this with K=Q2 and E=F=L_v. The norm of a unit is a unit: both u and u^(-1) are integral, so their norms and inverse norms are integral. The retained Dirichlet-character data say that the local chi has order at most two on Z2^times, while its non-2 factors are unramified. Composing the norm identity with chi gives chi restricted to G_F of order at most two on the reciprocity image of O_F^times. The retained relation beta squared=chi therefore gives beta to the fourth=1 on those units. This argument does not assume chi globally quadratic.

The existing beta proof then separately uses the multiplicative formal logarithm at depth e+1, the identity (U_F^(e+1))^4=U_F^(3e+1), and the ramification-unit rule. The present replacement supplies only the local norm step at beta proof43 and main1512–1519. The older online-note locator remains historical provenance, not the source of this replacement.
