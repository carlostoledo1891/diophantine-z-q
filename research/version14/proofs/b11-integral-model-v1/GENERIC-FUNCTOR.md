# The generic full-three moduli curve and its actual forgetful map

Author: `/root/astra_quartic_opt05_anchor`. This is a new proposed connection, awaiting independent review. Root suggested passing through the full-five model and its three-marking cover. The author supplies the lattice, PEL, canonical-model and action comparisons below. Root is not proposed as the independent reviewer of that strategy. Arithmetic's earlier note reconstructed source boundaries and supplied no proof of this connection.

## 1. Exact assertion and incoming inputs

Let B=(2,-3), let O=Z[i,(1+j)/2] be the fixed maximal order, and put mu=2j+ij, so mu^2=-6. Use the actual principal datum

    E0(x,y)=Trd(mu^(-1) x bar(y)),    a^dagger=mu^(-1) bar(a) mu.

The accepted A001 application supplies its integrality, unimodularity, positive Riemann-form realization and its prescribed Rosati involution. In particular, this proof does not use Baba--Granath's printed six-times form as a principal polarization.

Write K0=Ohat^*, Kn=ker(K0 -> (O/nO)^*) and K35=K3 intersect K5. The existing B11 construction supplies the fine full-five scheme X5/Q, its universal polarized O-surface, the finite-etale full-three marking scheme X35 over X5, the free G5=(O/5O)^* action, and its quotient Y/Q. Those are the already constructed schemes, not curves inferred from the desired adelic identity. Their exact source interfaces remain incoming. All markings are isomorphisms of left O-modules; relabeling is precomposition by right multiplication.

The assertion is that X35 and Y are the canonical characteristic-zero PEL curves of levels K35 and K3 for this fixed quaternionic datum, on all their determinant components. The forgetful morphism from Y to the fixed A001 polarized coarse curve P1_j is the actual normalizer quotient map. The canonical finite-adelic action, the relabeling action and the coarse polarized forgetful relation agree. No degree estimate is assumed here, and no factor from the auxiliary five-marking remains after its quotient.

This is an assertion over Q and its extensions. It does not identify an integral coarse model with P1 over Z[1/30], and does not extend a characteristic-zero marking theorem to characteristic 3. Buzzard's full-M statement is used only at M=5, which is prime to the quaternion discriminant 6. The new level-three comparison uses the direct lattice argument and Deligne's general PEL construction.

The published PEL suppliers are Deligne, Travaux de Shimura, final Bourbaki expose 389, pp132,146--150,152,156--157: Proposition1.15, Theorem4.7, paragraphs4.9--4.12 and4.15--4.17, Theorem4.21, Corollaries5.5/5.7 and Example5.8. Paragraph4.9 permits a semisimple algebra with involution; Scholie4.11 permits every compact open subgroup. Neither imposes Buzzard's maximal-level restriction at division primes. The canonical-model conventions are compared with Deligne1979, pp268--270, particularly Definition2.2.5 and Criterion2.3.1. We keep the 1971 homological convention throughout the construction.

## 2. The actual rational representation, polarization and Hodge datum

Take V=B as a left B-module. Its B-linear automorphism group consists of right multiplications. Each right multiplication R_b scales E0 by nrd(b). Thus the algebraic group G of B-linear symplectic similitudes in Deligne4.9 is the right-multiplication group. To use an ordinary, rather than opposite, B^* coordinate, use the group isomorphism

    b |-> R_(b^(-1)).

Its similitude multiplier is nrd(b)^(-1). This inversion is retained in the comparison of level frames below. Inverting a congruence unit does not change any of K0, K3, K5 or K35.

The adjoint identity E0(ax,y)=E0(x,a^dagger y) verifies Deligne(4.9.1) for the prescribed involution. The real algebra is M2(R). For z=x+iy in the upper or lower half-plane set

    v_z=(z,1)^t,
    J_z=(1/y) [[x,-|z|^2],[1,-x]].

Then J_z^2=-1 and J_z v_z=i v_z. Right multiplication by J_z is the complex structure on B_R under the period map u |-> u v_z. Deligne4.6 uses the characters w^(-1), bar(w)^(-1) on homology. Accordingly set

    h_z(a+bi)=R_((a+bJ_z)^(-1)),

so h_z(i)=-R_(J_z). This is the homological convention, not its dual. On the positive half-plane E0(u,h_z(i)u)>0, precisely the principal Riemann-form positivity in the fixed A001 datum. On the other half-plane the effective positive form is -E0. Deligne4.8 and4.10 work with the homogeneous form before choosing the effective positive representative. Negative-norm elements exchange the two half-planes and reverse that representative; they do not turn a positive polarization into a negative one on the resulting abelian variety.

The complex Lie representation of the left algebra B has reduced trace Trd(a). Its characteristic polynomial is the reduced characteristic polynomial, with rational coefficients. Equivalently, after B_C=M2(C), the cocharacter of G_C has the two distinct weights of the standard rank-two representation and the same conjugacy class under every field automorphism. The reflex field is Q. This verifies the datum and reflex field required in Deligne4.9 and5.8; it is not inferred from the eventual rational j-coordinate.

Conversely, let A/C be any polarized O-surface with this Rosati action. H1(A,Q) is a faithful four-dimensional left B-module. Since B is a division algebra of dimension four, it is free of rank one. Its alternating form, in a B-linear rational frame, is a rational scalar multiple of E0. Indeed, write E'(x,y)=E0(x,T y). Equality of the prescribed adjoint identities forces T to commute with left B, so T=R_b. Its being self-adjoint for the alternating form forces b=bar(b), hence b is rational. The complex structure also commutes with left B, and so is R_J with J^2=-1; these structures are the two half-planes just displayed. Choosing the effective polarization fixes the positive representative. Thus Deligne(4.10.1), (4.10.2) and the trace-on-Lie condition (4.10.3) hold for every object of our actual functor. No extra determinant component has been selected in this argument.

## 3. Lattices, all components and the actual torsion local system

In such a rational frame put I=H1(A,Z) inside B. It is a full left O-stable lattice. At a division prime p=2 or3, the reviewed local-order input identifies O_p with the valuation ring for w=v_p(nrd)/2. Choose x in I_p of least valuation. For y in I_p, w(y x^(-1))>=0; hence I_p=O_p x. This is the left-module statement, with the quotient on the right.

At a split prime identify O_p with M2(Z_p). For an O_p-stable full lattice L, the matrix idempotents split L=e11 L direct-sum e22 L. The maps e21 and e12 identify the two summands; each is free of rank two over Z_p. If v1,v2 is a basis of e11 L, the map

    E_ab |-> e_a1 v_b

is an isomorphism of left O_p-modules O_p -> L. Extending it to B_p shows it is right multiplication by an invertible element. Consequently Ihat=Ohat g for some g in B(A_f)^*. Conversely, the intersection B intersect Ohat g is a full Z-lattice with exactly these completions. This last assertion follows by choosing one integer clearing the finitely many denominators, and applying the ordinary additive Chinese remainder theorem to the resulting sublattice of B. It uses no strong approximation for B^* and no ideal-class-number assertion.

There is no hidden polarization obstruction for these lattices. Choose a positive rational c with v_p(c)=v_p(nrd(g_p)) at every prime. On I the form c^(-1)E0 is integral and unimodular: in the local frame O_p -> I_p it is the standard form multiplied by the unit nrd(g_p)/c. The sign of its effective representative is chosen with the half-plane as in Section2. Deligne's Riemann equivalence4.7 produces the actual principally polarized complex surface. Its prescribed Rosati action is unchanged. The uniqueness of the principal polarization inducing this involution, used in the fixed Buzzard/A001 problem, identifies this with the polarization in that functor.

For fixed I, the analytic family is C^2/(I v_z). On a simply connected open subset of a half-plane its integral homology local system is literally the constant lattice I. If the rational frame changes by b in B^*, the pair (I,z) changes to (I b^(-1),b z). The identity b v_z=(c_b z+d_b) v_(b z) gives the actual holomorphic torus isomorphism and the induced right-multiplication map on homology. Its polarization scales as calculated in Section2. These are the transition maps of the universal local system, not a postulated monodromy representation.

The exponential sequence gives A[n]=(n^(-1)I)/I, O-linearly identified with I/nI. Thus a local generator of Ihat yields the actual finite-torsion marking. Replacing it by a unit u on the left changes this marking by precomposition with x |-> x u. The stabilizer of a full n-marking is precisely Kn. This proves the statement at n=3 directly, including the nonsemisimple ring O/3O.

Every unit modulo p^a lifts to O_p^*: lift it and a modular inverse; their product is 1+p^a t, which has a convergent geometric-series inverse. This argument works at both division primes. It follows that all finite O-linear markings lift to adelic O-linear frames. Such frames are symplectic similitudes, because every B_p-linear map is right multiplication and scales the form by its reduced norm. The pairing has its usual Tate-twist target; no trivialization of roots of unity and no fixed determinant of the marking is imposed. Deligne4.11 uses outward frames from the Tate module to V(A_f); our markings point into torsion, so one uses their inverses in that statement. The K-orbits and actual right-relabeling convention agree after this inversion.

For clarity, the finite coordinate in the standard double quotient is a=g^(-1), where Ihat=Ohat g. Changing the local generator and rational frame gives g -> u g b^(-1), hence (z,a) -> (b z,b a u^(-1)). In particular, left relabeling u dot alpha=alpha composed with r_u is the canonical right action by u^(-1). This explicitly identifies the variable and the left/right conversion; it does not change the datum or its level subgroups.

This describes all rational frames, all adelic lattices and both half-planes. It gives the complete, all-component double quotient

    B^* \ (H^+- times B(A_f)^*) / K,

with the foregoing group/level convention, for each of K35 and K3. It is not a description of only the component represented by O. The complex comparison is also a comparison of families and markings, by the explicit homology transitions and Deligne4.15, not only a bijection of geometric points.

## 4. Why this is the same curve over Q

We now check the descent of that comparison. We do not deduce a Q-isomorphism from an arbitrary isomorphism over C.

Embed G in GSp(V,E0) by its actual action. Deligne Proposition1.15, p132, supplies a compact open K' of GSp(A_f) containing K35 for which the map of complex PEL curves at levels K35 and K' is a closed immersion. We may intersect K' with the integral stabilizer of O and with principal Siegel level3; these groups contain the image of K35. Shrinking K' in this way preserves the closed-immersion conclusion: in the proof of1.15 the equivalence relations decrease, and the maps at the sufficiently small levels are finite and unramified. The Siegel level K' is therefore a fine level. It has a Q-model obtained from full principal level N, N>=3, by its finite level quotient, as in Deligne4.16--4.17.

There is a Q-defined morphism from the actual X35 to this Siegel moduli scheme: retain the actual principal polarization and forget the O action, carrying its frame to its K'-orbit. This description is algebraic. Choose N divisible by15 and large enough that full Siegel level N is contained in K'. Refine the O marking to level N on a finite-etale surjective cover. Nonemptiness follows from the local-lattice argument above on every geometric characteristic-zero fiber; representability and descent are the already stated finite-marking inputs. The resulting symplectic-similitude level structure, modulo K', is independent of the refinement, because two refinements agreeing at35 differ by K35, whose image is contained in K'. Thus the morphism descends over Q. The primitive integral lattice and the effective degree-one polarization recovered in Deligne4.12 are exactly O and the polarization used here, rather than a multiple or an isogenous substitute.

Over C this actual morphism is precisely the closed immersion in1.15, by Sections2--3 and Deligne4.11--4.12. By Theorem4.21 and Corollary5.7/Example5.8, its PEL image is a canonical closed subscheme Z over the reflex field Q of the same Siegel moduli scheme. Since the Q-defined morphism has image in Z after extension to C, its pullback of the defining ideal of Z is zero already over Q. It factors through Z. That factor becomes an isomorphism over C, so it is an isomorphism over Q by faithful-flat descent for isomorphisms. This uses the actual forgetful map to a published canonical moduli scheme and the exact closed-image theorem. It does not assume the missing generic identity as a descent premise.

The universal abelian scheme, polarization, O action and finite markings on X35 are consequently the actual ones in the PEL description. We have not had to assert that an arbitrary complex universal family automatically descends. The comparison over Q was obtained from the already Q-defined X35 and its actual algebraic map.

## 5. The five quotient, the center and the same coarse map

The projection at5 gives

    K3 / K35 = (O/5O)^*.

Indeed K3 has full O_5^* at5, and reduction there is onto by the unit-lifting argument. Its kernel is exactly K35. The conditions at3 and5 are independent finite-adelic factors. This is a local product statement; it does not require global strong approximation. On X35 the left relabeling action is exactly precomposition of the five-marking by right multiplication, as Section3 checked on the actual universal lattice. Under a=g^(-1), left relabeling by u equals the canonical right action by u^(-1). After this explicit conversion the actions are both Q-defined and agree over C, hence agree over Q. Their orbit quotients agree. The already constructed free G5 quotient Y is therefore the canonical K3 curve over Q. There is no further five-level cover in Y and no five-level multiplier in the generic degree.

In particular, the central element -1 does not introduce an extra copy: on a full-three object the change of marking alpha to -alpha is realized by the isomorphism [-1] of the abelian surface. On X35 it changes both markings at once; the element -1 acting on the five-marking alone is not a stabilizer of the three-marked object. This agrees with freeness of the existing G5 action. More generally, the arithmetic center calculation in the separately reviewed normalizer proof applies to this full adelic model: cancel the finite valuations of a central idele by a rational scalar, then choose its sign so that its remaining 3-adic residue is1. The residue field for central units is F3. All remaining central units lie in K3. A rational scalar acts trivially on the half-plane, since its quaternionic norm is its square. This is compatible with the marking isomorphism just described.

For the coarse comparison first forget the three-marking. This is the actual Q-defined moduli map to the unlevelled polarized O-curve. Its distinguished analytic component is H/Gamma for Gamma=O^1/{+1,-1}. It is the whole unlevelled curve: Buzzard's V1(5) is geometrically connected, and its actual forgetful map is surjective onto this unlevelled moduli problem, because every complex O-surface admits a V1(5) marking. That last assertion is the split-five matrix-module argument, not the full-three conclusion. Equivalently the all-component lattice description above has a connected K0 quotient. No class-number assertion is substituted for this argument.

The unlevelled analytic family is exactly A_z=C^2/(O v_z) with the corrected principal form E0. Therefore the accepted A001 application of Baba--Granath Theorem2.1 is to this same polarized family. It identifies its polarized forgetful coarse quotient with V/W, where W is the full positive-normalizer group. The arithmetic normalizer calculation supplies the four classes and the center quotient separately from its final degree statement. They are precisely the positive rational Atkin--Lehner classes: i and j normalize the displayed O; the unit 1+i has norm -1; thus i(1+i)=2+i has positive norm2, and j has positive norm3. They realize the independent local parity classes at2 and3. Hence the finite-adelic normalizer relation on the K0 quotient is the same full W relation, with no omitted sign class.

Baba--Granath's Q-defined coarse model and the A001 marked coordinate now identify this quotient with the fixed P1_j. The map from Y is the composition of the actual Q-defined forgetful moduli maps, so it is this same j-map, not a map differing by an unspecified fractional-linear coordinate. Canonical finite-adelic actions and level transitions are Q-defined for reflex field Q. Their agreement with the actual forgetful relation has been checked over C and descends since these are already Q-defined morphisms. No ramified-prime marking statement from Buzzard is used in this final comparison.

## 6. Boundaries and exact downstream consumption

This proves the proposed CURRENT-B11-GENERIC-FUNCTOR connection, subject to the named published PEL/Riemann/canonical-model statements and the separately reviewed principal datum, construction and coarse-quotient inputs. The integral construction, Tate faithfulness, finite polarized automorphism theorem, scheme quotient/descent and arithmetic local-normalizer computations remain their own inputs. In particular this proof consumes only the arithmetic normalizer classes/center calculation, not the final degree theorem that depends on the present generic identification. There is no circular use of degree324, quotient essential surjectivity, or the desired canonical-model identity.

Once this new connection is independently accepted, the existing direct arithmetic index proof can be applied to the same Y3 and same j. The resulting degree bound is that separate proof's conclusion. No claim is made here that the current ordinary graph, full proof inventory, source ancestry or manuscript incorporation has been accepted. The historical unreviewed local-constancy alternative at ed992 lines779--781 remains a separate deletion proposal; none of this argument uses it.

The published PEL inputs retain their published ancestors, including Riemann theory, the CM reciprocity theorem and the canonical-model existence/uniqueness arguments. The selected Deligne source is a final published scan, not an author retype. The present proof does not claim a recursive new audit of those ancestors. Third-party source PDFs and page images remain local-only.
