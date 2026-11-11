# Even-characteristic auxiliary primes over a general totally real field

## 1. Target and retained inputs

Let F be a totally real number field, with no assumption that it is unramified at 2. Let k be a finite field of characteristic 2 and let r:G_F→GL_2(k) be continuous with nonsolvable image. Let S contain every infinite place, every place above 2, and all ramification of r and of the fixed determinant lift used below. Put A=End_k(k^2), with conjugation action, and Z=k·id. Write h^i for dimension over k. Choose the determinant character and coefficient ring as in the definitions in Kisin 3.2.1, final pp.625–626. In particular all framed local factors, including the infinite ones, are retained.

We prove that for every positive integer n there is a finite Q disjoint from S satisfying all three conclusions of Kisin Proposition 3.2.2: (a) N(v)=1 mod 2^n and r(Frob_v) has distinct eigenvalues for every v in Q; (b) |Q|=h^1(G_{F,S},A)−2, and the globally variable-determinant, S-locally fixed-determinant framed deformation ring is topologically generated over the completed tensor product of the fixed-determinant framed local rings by 2|Q|+1 elements; (c) if Theta_Q is the maximal abelian 2-extension group unramified outside Q and split at S, then Theta_Q/2^nTheta_Q is free of rank 2−|S|+|Q| over Z/2^n.

The following are retained mathematical inputs, rather than new proofs in this packet:

* The finite-group assertions in final KWII Lemma 4.3(2),(4),(5), pp.537–538: the projective image is conjugate to G=SL_2(k_0), |k_0|>2; A^G=Z, H^1(G,A)=0, and every nonzero G-submodule of A contains Z. These are group assertions and have no number-field ramification hypothesis. KWII cites Dickinson Lemma 42 for the H^1 assertion. The injection H^1(G_F,Z)→H^1(G_F,A) follows from (A/Z)^G=0.
* Chebotarev, global class field theory, local Tate duality and the local Euler characteristic formula at places away from 2.
* The Selmer-size formula for a finite G_F-module M and mutually annihilating local conditions L,L-perp:
  |H^1_L(F,M)| / |H^1_Lperp(F,M^*(1))| = (|H^0(F,M)| / |H^0(F,M^*(1))|) product_v (|L_v| / |H^0(F_v,M)|).
  Almost all L_v are unramified; the exceptional set contains all primes dividing |M| and all infinite places. This is the general-number-field formula, not a version restricted to fields unramified at 2. KWII §4.1.6, final p.539, cites DDT Theorem 2.19. The university-hosted DDT text dated May 24, 2000 states that generality explicitly on printed p.62. Its edition is separately qualified in the source record; this packet does not authenticate that file as the final book edition.
* The ordinary representability and completeness of the deformation rings defined by Kisin 3.2.1. We calculate their relative cotangent dimension below; we do not require the dimension or regularity of a Barsotti–Tate quotient to construct Q.

All subsequent calculations are for this fixed F,r,S. Their constants and thresholds may depend on that data. No uniform assertion as F varies is made.

## 2. The even part of KWII Lemma 5.2 does not use unramifiedness

Let M_j=Q(mu_(2^j)) and M_j^+ its maximal real subfield. The fields M_j^+ form the real cyclotomic Z_2 tower. Its finite subfields are exactly this chain, since their Galois groups are cyclic 2-groups. Since F is finite and totally real, there is a largest j0≥2 with M_j0^+ contained in F, and F intersect union_j M_j equals M_j0^+. Consequently for j>j0,

Gal(F(mu_(2^j))/F) is C_2 × C_(2^(j-j0)).

This follows by identifying it with Gal(M_j/M_j0^+); the factor C_2 is complex conjugation. Thus its maximal elementary abelian quotient has rank 2. This conclusion is valid even when F is ramified above 2.

Let K be the field cut out by A; Gal(K/F)=G is simple and nonabelian. It is disjoint from the abelian cyclotomic extension F_j=F(mu_(2^j)). Inflation-restriction for K F_j/F, using A^G=Z and H^1(G,A)=0, gives

H^1(K F_j/F,A) = H^1(F_j/F,Z), of k-dimension 2 for j>j0.

This is exactly the p=2 argument printed in final KWII p.544. On that page the use of “F unramified at p” is in the preceding p>2 argument, not in this calculation. No odd-p conclusion is extended here.

## 3. The auxiliary Kummer extension and disjointness

Choose compatible primitive 2^j-th roots zeta_j with zeta_(j+1)^2=zeta_j, and write x_j=(zeta_j+zeta_j^(-1))/2. Then 2x_(j+1)^2=x_j+1. Set y=x_(j0+1)^2=(x_j0+1)/2 in M_j0^+, hence in F. For j>j0 put T_j=F_j(y^(1/2^j)). Let kappa_j be the Kummer class of y in H^1(F,mu_(2^j)).

We record the elementary Kummer fact used here. If a characteristic-zero field E contains mu_(p^j), and adjoining a p^m-th root of a has positive degree p^a, then adjoining a p^j-th root has degree p^(a+j-m). Indeed write z^(p^j)=a. The extension E(z)/E is Galois, and its group acts on z by a subgroup of mu_(p^j), of order p^b for some b. The induced action on z^(p^(j-m)) has order p^max(b-(j-m),0). That order is the assumed positive degree p^a, so b=a+j-m. This is final KWII Lemma 5.7; it is independent of local ramification.

The extension F(sqrt(y))=F M_(j0+1)^+ is quadratic and totally real, by maximality of j0. It is disjoint from F(i). Therefore P=F(i,y^(1/4)) has degree 8 over F. Complex conjugation fixes the real fourth root and inverts i, so Gal(P/F) is dihedral of order 8. In particular P/F is not abelian.

The field F_j contains sqrt(y), but cannot contain y^(1/4), since F_j/F is abelian and would then contain P. The Kummer fact gives [T_j:F_j]=2^(j−1); its unique quadratic subextension is F_j(y^(1/4)). The field T_j/F is Galois and solvable (its group is cyclic-by-abelian). Also y is a unit away from 2. To check this, set R_2(X)=X and R_j(X)=R_(j−1)(2X^2−1). For j≥3, R_j(x_j)=0, its leading coefficient is a power of 2, and its constant coefficient is −1 for j=3 and 1 thereafter. These assertions follow by induction, using R_j(1)=1 and evenness for j≥3. The reversed polynomial shows x_j^(-1) is an algebraic integer of norm a power of 2 (its degree is 2^(j−2), since x_j generates M_j^+). Hence x_j, and then y, are units away from 2. Kummer extensions at a residue characteristic different from 2 of a unit by a 2-power root are unramified: after the unramified extension adjoining residue roots, Hensel's lemma applies since the derivative is a unit. Thus kappa_j is unramified outside S and has order at least 2^(j−1), already after restriction to F_j.

Let L/K be the common splitting field of the restrictions to G_K of the finitely many classes in H^1(G_{F,S},A). These restrictions are homomorphisms to the additive group of A. Hence L/K is finite abelian of exponent 2, and L/F is Galois. The simple nonabelian extension K/F is disjoint from the solvable extension T_j/F. Over K F_j, the extension T_j K is cyclic of degree 2^(j−1), while L F_j/K F_j has exponent 2. If they intersect nontrivially, L F_j contains K F_j(y^(1/4)). But L F_j/K is abelian, whereas K F_j(y^(1/4))/K is not abelian: by disjointness from K it has the same nonabelian quotient Gal(P/F). This contradiction proves T_j and L F_j are disjoint over F_j. This spells out the field argument of final KWII Proposition 5.6 and Lemmas 5.8–5.9; no unramified-at-2 assumption occurs.

Restriction of H^1(G_{F,S},A) to G_(T_j) therefore has the same kernel as restriction to G_(F_j). More precisely, if a class restricts to zero on G_(T_j), it is zero on G_(K T_j). Disjointness over K F_j says that Gal(L F_j/K F_j) is still fully seen after passing to K T_j. Since the restricted cocycle is a homomorphism on G_K, it must then vanish on G_(K F_j). Inflation-restriction places the original class in H^1(K F_j/F,A), which equals the inflated H^1(F_j/F,Z) by Section 2. Conversely those inflated classes vanish on G_(T_j), since T_j contains F_j. All such cyclotomic classes are unramified outside S: the extension F_j/F is unramified away from 2. Thus the common kernel has exactly dimension 2.

## 4. Selecting exactly h^1−2 primes

Let V=H^1(G_{F,S},A), with the two-dimensional kernel B just found. Every nonzero class outside B can be detected at a finite place splitting in T_j with distinct residual Frobenius eigenvalues. Here is the needed group argument. Its restriction to G_(K T_j) has nonzero additive image. That image need only be an F_2-subspace; take its k-linear span W. Normality and the cocycle identity make W a nonzero G-submodule, so W contains Z. Choose a split semisimple g in G with distinct eigenvalues, and lift g to G_(T_j). The scalar subspace Z is not contained in (g−1)A: conjugation by g is semisimple and the scalar matrices are in its fixed eigenspace. Since (g−1)A is k-linear and does not contain W, the actual additive image also cannot be contained in (g−1)A. Choose tau in G_(K T_j) whose cocycle value is outside that image. Since K is cut out by the adjoint representation, r(tau) is a scalar, not necessarily the identity. Let e be its order in k^*, which is odd. Replace tau by tau^e. This remains in G_(K T_j), its residual matrix is now the identity, and its cocycle value is unchanged: tau acts trivially on A, so c(tau^e)=e c(tau)=c(tau) in characteristic 2. If the chosen lift of g already has nonzero cocycle value modulo (g−1)A, keep it; otherwise replace it by this adjusted tau times that lift. The cocycle identity gives a nonzero value modulo (g−1)A, and the residual matrix is unchanged. Chebotarev applied to the finite extension encoding this cocycle and r gives infinitely many such places, avoiding S and any already chosen finite list.

Starting with V/B, choose a place detecting a nonzero remaining class, then restrict to the kernel of that local evaluation, and repeat. Each step decreases dimension by at least one. After at most dim(V)−2 places the common kernel is exactly B. Every class in B vanishes at every chosen place because the places split in F_j. If fewer than dim(V)−2 were needed, pad with further distinct places splitting in T_j and having the same residual semisimplicity property; B still vanishes and the kernel stays B. The resulting Q has exactly q=dim(V)−2 elements.

For every v in Q, r is unramified, N(v)=1 mod 2^j and r(Frob_v) has distinct eigenvalues. Moreover

h^1_(Q-split)(S,A)=2 and h^0(F_v,A)=2.

The congruence follows because v splits in F_j. All these choices can be made anew for each j. Nested Q's are unnecessary.

## 5. Cohomology counts and the framed algebra

Use zero local condition at S and full local condition at Q, with unramified conditions elsewhere. The trace pairing identifies A with its dual, and the mod-2 cyclotomic character is trivial. Global invariants have dimension 1. At v in Q, local duality and Euler characteristic away from 2 give h^1(F_v,A)−h^0(F_v,A)=h^0(F_v,A)=2. The Selmer-size formula therefore gives

h^1_(S-split)(Q,A) = 2 − sum_(v in S) h^0(F_v,A) + 2q.

This uses no Euler characteristic at a place over 2: those places are in S and their local condition is zero. The dependence on their actual invariants has been retained, not replaced by an unramified-field formula.

For clarity, compute the relative tangent space rather than importing a field-restricted generator formula. A first-order global lift has cocycle in Z^1(G_(F,S union Q),A). Fixing its image at the local basepoint in each framed local factor means that its restriction at v in S is a coboundary, with the chosen local change of frame. Simultaneous global change of frame identifies equivalent tuples. This yields the exact sequence

0 → H^0(F,A) → direct_sum_(v in S) H^0(F_v,A) → T_rel → H^1_(S-split)(Q,A) → 0.

The determinant is fixed locally at S, since a coboundary has trace zero; no global fixed-determinant condition is imposed in this ring. Thus the calculation uses A, not A^0. Its dimension is

dim T_rel = sum_S h^0(F_v,A) − 1 + h^1_(S-split)(Q,A) = 2q+1.

For a map of complete Noetherian local coefficient algebras with common residue field k, lift a basis of this relative cotangent space to elements of the target. Successive approximation modulo powers of its maximal ideal (or the complete local form of Nakayama) gives a surjection from the base formal power-series algebra on those 2q+1 elements. This proves precisely the generator bound in Kisin 3.2.2(2), with its globally variable determinant and all S-frames. A subsequent quotient by any specified local deformation conditions preserves the bound; no smoothness of those quotients was used.

## 6. The full exponent quotient

The injection H^1(F,Z)→H^1(F,A) and the kernel description in Section 3 show that H^1_(Q-split)(S,k) also has dimension 2. Apply the Selmer-size formula to k. The global invariant dimensions cancel, each place of S contributes −1, and each place of Q contributes +1. Consequently

t:=h^1_(S-split)(Q,k)=2−|S|+q.

Now apply that formula to the constant module Z/2^j, whose dual twist is mu_(2^j). Since F is totally real, the latter has exactly two global invariants. The local constant invariants have order 2^j at every place in S. At each v in Q, local class field theory gives H^1(F_v,Z/2^j) of order 2^(2j), since N(v)=1 mod 2^j. Thus

|H^1_(S-split)(Q,Z/2^j)| = |H^1_(Q-split)(S,mu_(2^j))| · 2^(j−1+j(q−|S|)).

The second Selmer group contains kappa_j: it is unramified outside S and zero locally at Q because Q splits in T_j. Its order is at least 2^(j−1). Hence the first group has order at least 2^(jt−2).

By class field theory Theta_Q is finite: splitting at all 2-adic and real places removes wild and infinite ramification, and the allowed abelian ramification at the finitely many odd places Q is tame with bounded conductor. The first group above is Hom(Theta_Q,Z/2^j). The equality for t says its underlying finite 2-group has exactly t generators modulo 2. Write the invariant factors of Theta_Q/2^jTheta_Q as cyclic groups of orders 2^a_i, with 1≤a_i≤j and exactly t factors (with the trivial case t=0 allowed). The order bound says sum_i(j−a_i)≤2, so every a_i≥j−2. Therefore

Theta_Q/2^(j−2)Theta_Q is (Z/2^(j−2))^t.

For the requested n choose j≥max(n+2,j0+1). Quotienting once more gives Theta_Q/2^nTheta_Q=(Z/2^n)^t, while the stronger norm congruence implies the requested one. Cardinality and generator count are independent of the index. This completes the stated general-field auxiliary-prime conclusion relative to the retained inputs in Section 1.

## 7. Scope and source qualification

The only explicit use of F unramified at p in the proof of final KWII Lemma 5.2 is in its odd-p branch. The even branch is supplied in Section 2 here. The §5.5 Kummer construction, Chebotarev selection, local computations at Q, and the relative tangent calculation above likewise impose no such hypothesis. Ramification of the actual H field above 2 is therefore not an obstruction to this argument. No assertion concerning odd p, arbitrary local component support, or the later automorphic module is proved here.

The source-level gap in citing the globally worded KWII Lemma 5.2 without checking its field hypothesis has not been dismissed as an edition mismatch. It is addressed by this separately authored even-characteristic derivation. At author freeze it has no independent acceptance. The final Kisin Proposition 3.2.2 remains a retained published input until this proof and its exact incoming source assumptions are reviewed. In particular the general Selmer-size formula, finite-group H^1 vanishing and representability are named mathematical premises; this packet makes no claim that their whole source proofs or editions have been newly certified.
