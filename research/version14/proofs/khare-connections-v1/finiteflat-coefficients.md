# Finite coefficient fields in the finite-flat weight-two criterion

Author proposal by /root/astra_quartic_opt05_anchor. The target is the missing general-coefficient connection in second-family15, not a new statement about characteristic2 or arbitrary ramified base fields. SourceReview identified the scope mismatch with the prime-field formulation of Serre Proposition4; the proof below is authored separately for independent review.

## 1. Statement and exact source roles

Let p>2, let k be any finite extension of F_p, and let V be a two-dimensional k-representation of G_Qp with finite image. Suppose its underlying F_p-representation is the generic fiber of a finite flat commutative group scheme G over Z_p killed by p. Suppose det_k(V)|I_p=omega_p. Then the Serre weight of V is2, with the original representation and no cyclotomic twist.

Serre1987, printed189, explicitly restricts the displayed formulation of Proposition4 to GL2(F_p), pointing to vector schemes for the general case. We do not apply that displayed formulation directly to a group of order p^(2[k:F_p]). Instead use final Raynaud1974: Section2.1,259-260 gives flat schematic closures and finite quotients; Theorem3.3.3 and Corollary3.3.6 on268 give uniqueness, extension of all generic morphisms, flat kernels/cokernels and injectivity on Ext when e<p-1. Corollary3.4.4 on270 bounds the tame exponents of every generic Jordan-Hoelder factor of a finite-flat group by0<=n_i<=e. Proposition3.3.2 alone only treats the rank-q vector-scheme case and is not the full-faithfulness assertion used here.

Use these results with e=1, hence e<p-1 even when p=3. The action of every element of k on the generic fiber extends uniquely by Corollary3.3.6. The field-action identities extend by uniqueness. This equips G with its required k-action, but does not assert that G is a rank-q one-dimensional Raynaud vector scheme. The tame bound is applied to all underlying F_p Jordan-Hoelder factors via Corollary3.4.4.

Extending the coefficient field causes no difficulty: a finite scalar extension of V is, on underlying F_p-vector spaces, a finite direct sum of copies of V, so has a finite-flat model; the extended coefficient action again extends uniquely. We may therefore choose a finite coefficient extension that splits all characters under consideration. Serre's weight is computed over F_p-bar and does not change in this process.

## 2. Tame possibilities

For the moment suppose wild inertia acts trivially on V. The finite tame inertia image is cyclic of order prime to p and is semisimple. Frobenius conjugation raises a tame generator to its p-th power. Thus its two character eigenvalues form Frobenius orbits of length at most2. Raynaud3.4.4 with e=1 says that, at their minimal niveau, the base-p digits of each character exponent are0 or1.

If both characters have niveau1, each is1 or omega_p. Their determinant is omega_p, and p>2, so they must be the pair(1,omega_p). Serre2.3,184-185 then gives weight2. If they form a genuine niveau2 orbit, the only possibilities with digits0/1 are the two fundamental characters psi and psi^p: digit pairs(0,0) and(1,1) have niveau1, while(1,0) and(0,1) give psi and psi^p. Serre2.2,183-184 gives weight2 for that pair. This uses the minimal coefficient field of the inertia character, not the possibly much larger field k.

## 3. Wild case and the extension orientation

Suppose wild inertia acts nontrivially. Its image is a finite p-group acting on a two-dimensional vector space in characteristic p. It has a nonzero fixed vector, and nontriviality makes its fixed space a line. Since wild inertia is normal in G_Qp, this line is stable under the full decomposition group. The two characters on the line and quotient are therefore G_Qp-characters; their restrictions to tame inertia have niveau1. Take schematic closure of the line and the finite-flat quotient, using Raynaud2.1/3.3.6. Raynaud's bound and the determinant again give the pair1,omega_p. The extension itself is not discarded.

Pass to R=Z_p^sh, with fraction field K0=Q_p^nr as in Serre2.4; this is a strictly henselian DVR with e=1. Unramified character factors disappear. Uniqueness from Raynaud3.3.3 identifies the finite-flat models of a trivial k-character and a cyclotomic k-character with the constant additive group k and with mu_p tensor_Fp k, respectively.

First consider the opposite orientation: an extension of the multiplicative group mu_p tensor k by the constant etale group k. The quotient map is a torsor under a constant etale group. On the special fiber its target is connected and local with algebraically closed residue field, so the torsor is a disjoint union of copies of that target. The identity component of the whole group has the same rank as the multiplicative target and maps isomorphically to it on the special fiber. Over the henselian base, that component is an open-and-closed finite-flat subgroup; its map to the target is an isomorphism by Nakayama on the finite free coordinate algebras. This gives a group section and splits the extension. Thus its wild inertia would be trivial. In the genuinely wild case the only remaining orientation is therefore

0 -> mu_p tensor_Fp k -> G_R -> constant k ->0.

This is the general-coefficient form of the connected-etale observation in Serre's proof on190. It does not assume that every finite-flat extension splits.

## 4. All Kummer coordinates are units

Choose an F_p-basis of k and its coordinate functionals lambda_i:k->F_p. Pull the preceding finite-flat extension back along the map constant F_p -> constant k sending1 to1, and push out its multiplicative subgroup by lambda_i. These are morphisms of underlying F_p-group schemes, not incorrectly claimed to be k-linear. Corollary3.3.6 ensures that the resulting kernels/cokernels, hence these pullbacks and pushouts, are finite flat. Each resulting group G_i has order p^2 and is an extension of constant Z/p by mu_p, still killed by p.

The fiber of G_i over1 is a mu_p-torsor over R. The fppf Kummer sequence and Pic(R)=0 identify its class with a unit u_i in R^*/R^(*)p. On the generic fiber this is exactly the coordinate lambda_i(c) of the original k-valued extension cocycle c. Thus all coordinates of c are represented by units; this conclusion is about the full extension, not only its semisimplification.

After adjoining mu_p, the inertia splitting field of V is contained in the compositum obtained by adjoining the p-th roots of these units. Every Kummer class in the resulting subextension is again a product of powers of units. Serre's definition2.4.6-2.4.7 on186 explicitly allows an elementary abelian group of rank m and declares this unit condition to be peu ramifie. It is not restricted there to m=1 or to coefficient field F_p. Therefore V is peu ramifie. With subcharacter omega_p and quotient1, the ordered exponents are beta=1 and alpha=0; the peu-ramifie weight rule in2.4 gives weight2. This completes the wild case and the lemma.

## 5. Apply to the actual auxiliary lattice in second-family15

The actual A_l in that packet is crystalline of weights(0,1) over Q_l, with l odd. As a Q_l-representation after restriction of coefficients, it still has only those weights. The argument printed in final Kisin, proof of Lemma2.3.8 on1122, uses Breuil5.3.1 to obtain a Barsotti-Tate lattice and then realizes any chosen stable lattice's reductions as subquotients of its finite-flat reductions. This is the exact retained crystalline/finite-flat input; we do not re-prove Breuil's theorem here.

Let T be the original stable coefficient lattice and varpi its coefficient uniformizer. Since l belongs to(varpi), T/varpi T is a quotient of T/lT, not generally equal to it. Schematic closure and finite-flat quotient produce the finite-flat generic model for this actual reduction. Raynaud3.3.6 over Z_l extends its finite residue-field action. The determinant on inertia is omega_l because the finite determinant factor of A_l is unramified at l. The lemma just proved therefore gives k(rbar_l)=2 for this same residual representation and embedding. It neither selects a different lattice nor replaces a nonsplit local extension by its semisimplification.

## 6. Scope and disclosures

The new proof is the coefficient-field extension of the finite-flat weight-two criterion and its exact application. It retains the published Raynaud classification, finite-flat group operations, finite separable coefficient extensions, the fppf Kummer sequence, Serre's definitions, and the Kisin/Breuil lattice input. It does not claim that the printed prime-field Proposition4 already states this lemma, nor prove all of those published ancestors anew.

The original second-family15 and its orientation-only successor remain unchanged. A new finiteflat-successor-002 selects this lemma explicitly and corrects the full-faithfulness citation to Raynaud3.3.6. The independent reviewer identified the need for this connection and the separate orientation explanation; no independent approval of this new proof is claimed. The orientation paragraph remains assigned to root's separate review. No characteristic2 or ramified-base extension is included.
