# Classical local realization and exclusion of weight one

Status: AUTHORED FOR INDEPENDENT REVIEW. No manuscript or historical review is changed. This is not an acceptance of the full modularity ancestry.

## Exact input and normalization

This supplies the classical local input missing from Section 5 of `pan-calegari-direct-author-001/PUBLIC-PROOF.md`. The preceding argument constructs the same absolutely irreducible r=r5, de Rham at 5 with weights {0,-1}. Its published modularity input supplies r = U_g tensor delta after finite coefficient extension, with g a nonzero classical cuspidal eigenform of positive integral weight k. Section 0 supplies the normalized primitive representative f. We do not attribute that extra normalization step to an unquoted stronger modularity statement.

Use the arithmetic-Frobenius normalization of U_f: its good-prime characteristic polynomial is X^2-a_ell(f)X+epsilon_f(ell)ell^(k-1). Let kappa be the 5-adic cyclotomic character, with HT(kappa)=-1. All coefficient extensions respect the fixed embedding of the eigenvalue field into Qbar_5. We may enlarge the coefficient field finitely. Weights are relative to this embedding.

## 0. Choose a primitive representative before knowing the weight

Deligne–Serre Section 1.9, printed p.510, decomposes a form of type (k,epsilon) into an Eisenstein part and oldforms f_j(d_j z), with primitive cusp forms f_j at levels dividing N and d_j dividing the corresponding level quotient. The decomposition is unique in its stated sense. Since g is cuspidal, its Eisenstein part is zero. Group terms by normalized primitive form and degeneracy index and discard zero coefficients.

For ell not dividing N, the coefficient formula for T_ell in Section 1.6, p.509, shows that it commutes with h(z) -> h(d_j z), since ell and d_j are coprime. The primitive constituents are eigenforms by Section 1.7, p.509. Apply T_ell-a_ell(g) to the unique decomposition. Each nonzero component must have eigenvalue a_ell(g). Choose one to obtain a primitive f with the same good-prime eigenvalues, weight k and induced nebentype. Section 1.7 normalizes it by a_1(f)=1. There is no weight-two restriction on these statements.

The good-prime polynomials of U_f and U_g agree. Deligne–Serre Lemma 3.2, p.513, identifies their semisimple representations after compatible coefficient extension. Thus r = U_f tensor delta with the same delta. The later Li theorem is used only for weight-two finite-twist extraction after k=2 is established.

## 1. Exclude weight one first

If k=1, the nonzero form's transformation under -I gives epsilon_f(-1)=-1. Deligne–Serre Theorem 4.1, printed pp.513–514, therefore applies. It supplies a complex representation with trace a_ell and determinant epsilon_f(ell) for ell not dividing the level, irreducible because f is cuspidal. Section 3.1, p.513, uses the discrete topology on C and explicitly states that the representation has finite image. The footnote on that page specifies arithmetic Frobenius.

The proof itself realizes this representation over a number field. Section 8.2, p.525, chooses K containing the eigenvalues and nebentype values. Section 8.5 enlarges K by finitely many roots of unity. Section 8.6, p.526, constructs the finite-image lift and explicitly compares the resulting representations in GL_2(K), before viewing them as complex representations. Extend the given eigenvalue-field embedding to K and then to a finite extension of Q_5. This gives the finite-image 5-adic representation W_f with the required polynomials. No separate finite-group realization theorem is needed.

Its good-prime polynomials equal those of U_f. W_f is semisimple in characteristic zero, and U_f is irreducible because r is. Deligne–Serre Lemma 3.2, p.513, in its finite-extension-of-Q_ell case identifies them. Choose a finite extension L/Q_5 killing W_f on the local Galois group. Then r|G_L is the direct sum of two copies of delta|G_L. De Rhamness is preserved by restriction and by subrepresentations, so delta|G_L is de Rham. The two summands have equal weights. On the other hand finite-extension compatibility preserves the distinct weights {0,-1} of r at each embedding above the fixed embedding. Contradiction. Thus k>=2.

Kato Section 9.2, p.187, explicitly supplies tensor/dual/subquotient closure and finite-extension compatibility for de Rham representations. The parent proof also retains its published Fontaine admissibility input. No crystallinity or good reduction at 5 is assumed.

## 2. Identify the precise Kato dual

For k>=2 take V=V_{F_lambda}(f) in Kato, with lambda above 5. Section 6.3, pp.161–162, gives dimension two for this exact Hecke quotient and dimension one for S(f). Section 9.4, p.188, makes V de Rham and states that its decreasing filtration is all of D_dR(V) for i<=0, is S(f) tensor_F F_lambda for 1<=i<=k-1, and is zero for i>=k. Its jumps are 0,k-1. The dual has jumps 0,1-k, which are its weights with HT(kappa)=-1.

The original newform level is any N>=1, and p may divide N. Sections 5.4, p.155, and 8.3, p.181, handle the small levels by invariants at fine level. The lower bound on an auxiliary fine level does not restrict the original level. Section 9.4 has no non-CM condition.

Equation (14.10.2), p.240, gives det V = kappa^(1-k)epsilon_f^(-1). Equation (14.10.3) gives the Euler polynomial on inverse arithmetic Frobenius in V. Consequently at good primes the arithmetic-Frobenius polynomial on V^vee is precisely the one defining U_f. Hence

    U_f = V^vee,
    det U_f = epsilon_f kappa^(k-1),
    HT(U_f) = {0,1-k}.

Here is the semisimplicity justification without assuming anything about an entire cohomology group. The semisimplification of V^vee has the same good-prime polynomials as U_f, so Deligne–Serre Lemma 3.2 identifies them. Since U_f is irreducible of dimension two, V^vee is itself irreducible and thus isomorphic to U_f. No conjugate-form relabeling or additional Tate twist is used. Equation (14.10.1) about f* does not require inserting such a twist in this identification.

## 3. Determine the weight and the twist

The isomorphism r = U_f tensor delta gives a stable line of character delta inside Hom(U_f,r), namely the identity line in Hom(U_f,U_f) tensored with delta. Both ambient representations are now known to be de Rham. Tensor, dual and subobject closure make delta de Rham. If its weight is m, tensor compatibility gives

    {m,m+1-k} = {0,-1}.

Since k>=2, the first entry is strictly larger. Thus m=0 and k=2. Weight one was excluded before using Kato's k>=2 statement.

Retain the parent argument's finite character alpha=det(r)/kappa. At k=2 the determinant identity is det(U_f)=epsilon_f kappa. Taking determinants gives delta^2=alpha/epsilon_f. The right-hand side has finite image. Each nonzero scalar has at most two square roots in characteristic zero, so delta itself has finite image. This does not deduce finiteness from weight zero alone. The cyclotomic exponent in det(U_f) is k-1, not 1-k.

The existing finite-character absorption proof now applies unchanged. Neither controlled extension field is replaced, and delta is not identified with either caller's controlled auxiliary character.

## Evidence and authorship

Final Kato PDF: `work/kato-2004.pdf`, SHA256 `3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.

Final Deligne–Serre PDF: `work/source-risk-review-20261107/sw01-p3-entry-review-compiler-001/local-only/deligne-serre1974-final.pdf`, SHA256 `65b390f6d33e827e30c6c66bbc15421eca51db3180bdf5996dcee19047be97fc`.

Root authored this connector after directly reading the parent proof, Deligne–Serre through Section 4 and Sections 8.2–8.7, and final Kato images pp.187,188,240. SourceReview supplied the Kato locations, proposed the dual-normalization match and located the Deligne–Serre number-field construction. Sol flagged the scope of the earlier Li citation. Picard is assigned the noncontributing mathematical review; the intended primitive-selection route was communicated before his source-first supplement, and that exposure must be disclosed. Exact incorporation into both current consumers and ordinary-inventory adoption require separate checks after acceptance.
