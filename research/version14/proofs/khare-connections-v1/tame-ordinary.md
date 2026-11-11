# The nonscalar tame ordinary connection for Khare5.3

Author proposal, not an independent source approval. The corrected Savitt source used below is the exact arXiv v3 of September2010, SHA e161ac6498c1a75fc8f981c25edd5e9390b19ceb40f174a25a1f6491390c115c. It is not relabelled as the final Duke2005 facsimile. The final-edition comparison remains unresolved.

## 1. Needed assertion and type reduction

Let p be odd, E/Q_p finite, V a two-dimensional continuous E-representation of G_Qp with a stable lattice T. Suppose V becomes Barsotti-Tate over F1=Q_p(mu_p) and (T/m_E T) has reducible semisimplification over an algebraic closure. The desired conclusion is that some finite Teichmuller twist of V has an unramified one-dimensional quotient and a one-dimensional subrepresentation with cyclotomic character times a finite tame and unramified character. In particular V is reducible. No global modularity conclusion is asserted.

The potentially crystalline inertia type factors through Gal(F1/Q_p), which is cyclic of order p-1. After a finite coefficient extension it is therefore a sum of two powers of the finite Teichmuller character. The scalar and nonscalar cases are distinct. This packet supplies the nonscalar connection conditional on the named Savitt inputs; the scalar case is reduced explicitly to the separate crystalline-weight-two interface below.

Normalize the nonscalar case by twisting V by one of those finite characters so that its type is 1+omega_tilde^j, with 1<=j<=p-2. Finite twisting preserves reducibility of the residual semisimplification, changes neither Hodge-Tate weight, and is available globally as a power of the Teichmuller lift of the mod-p cyclotomic character when needed by the caller.

## 2. Explicit source inputs and convention

The required Savitt inputs are Proposition2.17/2.20's filtered-module description, Proposition6.9's lattice, and Theorem6.11(3)'s reduction for interior slopes. They appear on corrected pages8-10,29-32,34-35. Corollary6.15(1) and Remark6.17 on38-39 explain their application to residual semisimplification without a trivial-endomorphism assumption. The endpoint cases excluded in Lemma6.8 are already reducible characteristic-zero representations; we do not apply the interior calculation to them.

The convention matters. On corrected page7, D_st,2(V)=D_st(V(-1)), a covariant functor. Example2.13 gives phi=p^(1-h)*a^(-1) on the character epsilon^h*omega_tilde^b*lambda_a, where lambda_a sends arithmetic Frobenius to a. Thus a unit phi eigenvalue with filtration degree0 corresponds to a character of cyclotomic weight1 in V, not weight0. We use this convention in the actual subrepresentation and quotient below.

In the indecomposable nonscalar case, the source gives D=E e1+E e2, phi(e_i)=x_i e_i, x1*x2=p*w with w a unit, and Fil1 generated over F1 by pi^j e1+e2. The two descent characters are1 and omega_tilde^j, respectively. Both x_i are integral and their valuations sum to1. We retain the potentially semistable equivalence with descent data and rank-one character identification as explicit inputs; a whole independent proof of those comparison theorems is not claimed.

## 3. Interior slopes cannot have the given reducible residual representation

If both x_i have valuation strictly between0 and1, Theorem6.11(3) supplies a stable lattice whose reduction has inertia characters omega_2^(1+j) and omega_2^(p(1+j)). Since 2<=1+j<=p-1, the exponent1+j is not divisible by p+1. The two characters are distinct of niveau two. Frobenius interchanges their eigenspaces, so that residual representation is absolutely irreducible.

The semisimplification of the reduction of a p-adic representation is independent of its stable lattice, after extending the residue field if necessary. Therefore this calculation contradicts the assumed reducibility for T. This is precisely a semisimplification argument, not an assertion that every integral lattice was classified. No assumption End(T/m_E T)=k_E is added. Remark6.17 explicitly separates these two scopes.

It follows that the valuations are(0,1) or(1,0).

## 4. The endpoint gives the actual ordinary quotient

Suppose first that x1 is a unit. The phi-stable descent line E e1 has zero Fil1, and equal Hodge and Newton numbers0. It is a weakly admissible subobject. Under the covariant D_st,2 equivalence it gives the subrepresentation epsilon*lambda_(x1^-1). The quotient has descent character omega_tilde^j, phi eigenvalue x2=p*w/x1 and filtration degree1. Its character is omega_tilde^j*lambda_(x1/w). Thus there is an exact sequence

    0 -> epsilon*lambda_(x1^-1) -> V_normalized
      -> omega_tilde^j*lambda_(x1/w) -> 0.

Twisting the whole sequence by omega_tilde^(-j) makes its quotient unramified. The subrepresentation then has character epsilon*omega_tilde^(-j)*lambda_(x1^-1).

If x2 is a unit, the same calculation using E e2 gives

    0 -> epsilon*omega_tilde^j*lambda_(x2^-1) -> V_normalized
      -> lambda_(x2/w) -> 0.

This quotient is already unramified. These formulas use the same finite twist on the entire representation, hence its determinant changes by the square of that twist. They do not exchange a subcharacter and quotient merely because the residual representation happens to split.

If V was decomposable at the outset, its two characters have weights0 and1. The weight0 character has finite tame inertia, trivial over F1; twisting by its inverse finite inertia character makes it an unramified quotient. This uses the same explicit rank-one potentially crystalline character classification. It needs no lattice enumeration.

## 5. Scalar branch and source correction history

If the type is scalar, a finite Teichmuller twist makes V crystalline over Q_p with weights0,1. To complete Khare5.3 one needs the separate assertion: a crystalline two-dimensional representation of these weights with reducible residual semisimplification is ordinary. Theta is authoring that local connection from the previously pinned BLZ small-weight results and the filtered-module equivalence. It is not assumed independently approved in this freeze. This packet therefore does not claim all of Khare5.3 closed.

The public Savitt corrigendum identifies the omitted niveau-two case in Theorem6.12(4), and adds the missing lattice and corresponding6.12(5),6.15(2),6.21 changes and the added surjectivity argument in6.24. The corrected arXiv v3 incorporates it. The selected nonscalar niveau-one argument uses6.9,6.11 and6.15(1), not that omitted family. This limited source-use separation does not certify every proof ancestor or final-edition equality. The author index's label 'published version' accompanies a43-page author-layout file, whereas the journal pagination is141-197; that label is recorded as provenance, not treated as a facsimile comparison.

## 6. Actual callers and remaining work

This connection addresses the P-local RETURN members that become Barsotti-Tate over Q_P(mu_P), and the same local condition in the prime-conductor argument. It does not assume that a FIRST member with two ramified primes is globally strict level one. Local residual reducibility must be supplied by its actual branch; the independent dihedral connection can supply it in the stated cyclotomic-degenerate cases.

The finite twist is the one described above. An application must retain the changed determinant and its square-twist factor, the residual distinguishedness test, the chosen embedding, and the later untwist. No modularity lifting theorem, global ordered entry, compatible-system construction, or full Serre result is proved here.

Before adoption the packet requires a non-author mathematical decision, qualification of the selected Savitt source against the demanded publication standard (or an explicit authorized corrected-source adoption), and the separate scalar-branch decision. The original Khare author-edition qualifier remains unchanged in the canonical records.
