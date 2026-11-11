# Selected dihedral interfaces of Khare Lemma 5.1

Author: /root/astra_quartic_opt05_anchor. This is a new bounded connecting proof, awaiting independent review. Khare's final Duke edition has not been compared. The argument below replaces only the conclusions explicitly stated here, not his class-number existence assertion, Lemma 5.3, Lemma 5.4, or compatible-system construction.

## 1. Objects and inputs

Let p be an odd prime and let r: G_Q -> GL_2(k) be continuous, odd and absolutely irreducible, where k is an algebraic closure of F_p. Its image is finite; a sufficiently large finite coefficient field contains every matrix used. Dihedral means that the projective image H is a noncyclic dihedral group D_{2t}, with cyclic rotation subgroup C_t and t>1. All assertions of splitting below are after a finite coefficient extension, not over an arbitrary nonsplitting field.

The elementary local inputs are that wild inertia is pro-p, finite prime-to-p inertia is cyclic, and decomposition normalizes inertia. The elementary global input is the quadratic-field discriminant formula: for odd p there is exactly one nontrivial quadratic field unramified at all finite primes other than p, namely Q(sqrt((-1)^((p-1)/2)*p)). There is no nontrivial quadratic field unramified at every finite prime. These are named background facts, not new modularity or class-number inputs.

For weights we use the actual final Serre1987, printed183-184. In the niveau-two case its digits satisfy 0<=a<b<=p-1, inertial characters psi^(a+pb), psi^(b+pa), and weight 1+pa+b. In the split niveau-one case the digits satisfy 0<=a<=b<=p-2, and the weight is 1+pa+b unless a=b=0. We use these definitions, not Serre's modularity conjecture as a theorem. The inertia convention for the mod-p cyclotomic character chi is psi^(p+1).

## 2. Prime-to-p image

A finite-order element of PGL_2(k) is either semisimple of order prime to p or nontrivial unipotent of order p. This follows by putting a lift in Jordan normal form and taking the ratio of its eigenvalues. If p divided t, the cyclic rotation subgroup would therefore have order p, and would have a unique fixed point of P^1(k). Its normalizer preserves that point. The dihedral group H normalizes its rotation subgroup, so all of r(G_Q) would preserve the associated line, contrary to absolute irreducibility. Thus p does not divide 2t.

The scalar kernel of r(G_Q) -> H is a finite subgroup of k^times, also of order prime to p. Consequently the entire linear image has order prime to p. In particular r is tamely ramified at p, and every restriction to a finite-image subgroup is semisimple.

If r is semistable in Khare's residual sense, meaning that inertia away from p acts unipotently, that inertia is trivial: a nontrivial unipotent has order p and cannot lie in this image. Thus this semistable hypothesis implies that r is unramified outside p. The argument below may instead start directly with this latter hypothesis.

## 3. Strict level one forces local splitting and distinguished inertia

Assume r is unramified at every finite prime other than p. If t were even, D_{2t} would have a quotient C_2 x C_2. Its distinct quadratic characters would give distinct quadratic extensions of Q unramified outside p, contradicting the quadratic discriminant formula. Hence t is odd.

Write eta: H -> C_2 for the rotation quotient. Its field K is the unique quadratic field described above, and is ramified at p. Complex conjugation has eigenvalues 1,-1 because r is odd and p is odd, so its projective image is a nonidentity involution. Every involution in D_{2t} with t odd is a reflection. Therefore eta(c)=-1, K is imaginary, p is 3 modulo 4, and K=Q(sqrt(-p)). No class-number claim is needed.

The image I of inertia at p in H is cyclic and maps onto C_2 under eta. A cyclic subgroup containing a reflection in D_{2t} with t odd is exactly that order-two reflection subgroup: its generator outside C_t has order two. Thus I=C_2. The image D of decomposition normalizes I, hence centralizes its unique nonidentity element. The centralizer of a reflection in an odd dihedral group is that same C_2. Therefore D=I.

The inverse image of a cyclic projective subgroup of order two in GL_2(k) is abelian: choose a lift g of its generator; every matrix in the inverse image is a scalar times either 1 or g. Since the actual finite image has order prime to p, it diagonalizes. Thus r restricted to G_Qp is a direct sum of two characters. Their ratio on inertia is the unique nontrivial quadratic tame character, chi^((p-1)/2). In particular the two inertial characters are distinct.

Each finite character of G_Qp has tame inertia a power of chi: the Frobenius relation forces that power's order to divide p-1. Twisting r by a global power of chi therefore makes one local character unramified. The other has inertia chi^((p-1)/2). This is the precise residual ordinary/distinguished conclusion needed by the selected strict-level-one callers. Serre's split digit rule then gives weight (p+1)/2 for this twist. We do not infer ordinarity of a characteristic-zero lift; that is a separate input, including Khare5.3 where applicable.

## 4. Cyclotomic-induced local irreducibility fixes the small weight

Now allow arbitrary ramification away from p. Assume instead that r is induced from a character of the quadratic field K_p=Q(sqrt((-1)^((p-1)/2)*p)), and is locally irreducible at p. The inducing character and its conjugate are distinct; in the induced basis the projective image has cyclic diagonal subgroup and an off-diagonal reflection. This gives the dihedral description of Section2, including the case t=2. Its rotation quotient is the inducing quadratic character.

Because K_p is ramified at p, the cyclic projective image of inertia contains an element outside the rotation subgroup. Such an element is a reflection of order two. Hence projective inertia again has order two. This step does not require t odd, strict level one, or the preceding global argument.

The two inertia eigencharacters must be of niveau two. If both were of niveau one, Frobenius would preserve their distinct eigenspaces, since the pth power fixes a niveau-one character. Wild inertia is already trivial, so the local representation would split, contrary to the hypothesis. In the notation of Serre's definition their ratio has order

    (p+1) / gcd(p+1,b-a).

Indeed its exponent in a fundamental niveau-two character is (p-1)(b-a), up to sign. This order equals two by the preceding paragraph.

If the actual Serre weight is at most p+1, the formula 1+pa+b forces a=0: a>=1 and b>a would give weight at least p+3. Therefore b=k-1, and 1<=b<=p-1. Order two forces b=(p+1)/2, hence k=(p+3)/2. The assertion concerns this specified small Serre weight; it does not replace an arbitrary weight by a smaller one without recording the twist.

In particular a cyclotomic-induced residual representation with Serre weight2 cannot be locally irreducible for any odd p. This supplies only the residual local reducibility used in the first auxiliary calls. Characteristic-zero ordinary lifting and its distinguished ordering remain their separate stated inputs.

## 5. Exact caller partition and retained boundaries

The strict-level-one portion of LEVEL1-WEIGHT-TRANSFER and the W8/W10-W12/W14-W20/W22-W30/W32/GENERAL RETURN rows can consume Section3 only after their recorded outside-p unramified and globally absolutely irreducible dihedral hypotheses hold. Section4 supplies the weight2 exclusion in the cyclotomic-induced FIRST branch. It is not legitimate to apply Section3 to those FIRST members: they can have nontrivial finite type at a second prime. GENERAL-LINK-BACK reuses its actual FIRST partition; it does not turn shared residual representations into equality of characteristic-zero systems.

Globally reducible residual representations, nondegenerate lifting theorems, solvable-image modularity, the ordinary characteristic-zero line and the compatible-system embeddings are not proved here. In particular this packet does not retire the BM/Savitt source interface of Khare5.3 or the full weight-transfer inference of Khare5.4. It proves neither existence of the dihedral representations nor the stated list of class-number-one exceptions in Khare5.1(i).

The proof was developed after reading Khare's author proof and the caller records; it is not a source-first independent reconstruction of Khare's paper. No final-Khare equivalence is asserted. Its new bounded assertions require a non-author decision before adoption.
