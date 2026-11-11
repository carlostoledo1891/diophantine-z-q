# Item 1/4: conditional Khare caller connections

I accept KC-FIRST-LIFTING and KC-LINK-BACK in their stated conditional scopes, together with the source-precision correction and the separation of the nine caller obligations. This decision binds audit13 manifest `c80772ee38beffbb0153c1d20de267c086eecbdcb0bd47f285239ff521d154d5` with the four overrides in source-precision-001 manifest `ed08df51c33aab0c695008ea8dd879e1cab67a302f079585c5399ef8aa534b8d`. The effective proof is `01883e8587ee75d1fedc3700d1ebb63d1fb28a930c2dc672f539d5845c0b4755`. No author file or manuscript was changed.

I previously supplied source locations and reviewed neighboring source interfaces. I did not author these two connections, the local ordinary lemma, or the dihedral argument used here. I read the effective proof and cards, then the actual source passages and component proofs. This is an independent review of the new connections; it is not an independent reapproval of my earlier trace or local-base-change contributions.

## Source and exact-version check

I read Khare's pinned author text, pages 11-13, 16-19, 21 and 23-28; final early Khare-Wintenberger, pages 230, 237, 239, 244 and 246; and final Kisin, pages 1122 and 1172-1173. I visually checked Khare pages 19 and 24, KW page 246, and Kisin page 1173. The three PDF identities and the exact excerpts are bound in CHECKS.json. Khare remains the author version, not an authenticated final Duke comparison.

KW page 230 includes odd geometrically reducible residual representations in its definition of modular. Theorem 5.1 on page 246 allows finite ramification away from the coefficient prime; its hypotheses are not restricted to level one. Definition 3.1 supplies the integral ordinary condition. Kisin's Corollary 3.5.8 is the Q-corollary actually invoked. The proof does not remove conditions from the separate Hilbert theorem 3.5.7. Kisin's weight-zero/one crystalline-to-Barsotti-Tate interface on page 1122 retains its cited Breuil input.

The check verified 72 distinct file pins and 11 raw spans. Sections 1-3 are byte-identical across the successor. The two NEW-CONNECTIONS cards remain the original pinned bytes. The only proof change is exactly the declared Section 4 tail replacement. CALLER-OBLIGATIONS changes only the available assertion and missing-work description of KC-RETURN-WEIGHT. FINDINGS changes its corresponding wording. PROOF-LOCATIONS changes the file metadata, removes headings, and updates the Section 4 hash; all four new spans verify. These mechanical checks supplement the mathematical reading below.

## KC-FIRST-LIFTING

The domain is a finitely ramified, absolutely irreducible rank-two representation over a finite extension of Q_l, with l odd, crystalline weights (0,1) in the KW convention, finite-times-cyclotomic determinant with the finite character unramified at l, and modular semisimplified reduction. The statement does not establish these hypotheses for a newly constructed family.

If the residual restriction to the specified quadratic field K_l remains absolutely irreducible, Kisin's Q-corollary applies directly. Crystalline weights (0,1) give the required Barsotti-Tate condition, and the weights fix the resulting form's weight as two.

For geometrically reducible residual representation, the local ordinary lemma applies. Its saturation argument gives a free rank-one integral submodule and free unramified quotient, as required by KW, rather than merely a reducible residual representation.

In the remaining branch, Clifford theory for the index-two normal subgroup in odd characteristic gives induction of a character of K_l. The finite diagonal character image has order prime to l, as does the index two. Wild inertia therefore acts trivially and the inertia image is cyclic. Since K_l is ramified at l, projective inertia contains a reflection. A cyclic subgroup containing a reflection is of order two, including the projective Klein-four case. This calculation needs no restriction on ramification at the other primes and no uniqueness of inducing fields.

If the local residual representation were absolutely irreducible, a saturated characteristic-zero line would contradict that irreducibility. The characteristic-zero local representation would therefore also be absolutely irreducible. The retained h=1 BLZ calculation then gives inertia ratio of order l+1, contradicting order two, also when l=3. Thus the residual local representation is reducible, and the same ordinary lemma applies. This is a valid use of the general induced calculation, not the earlier strict-level-one argument.

In the two ordinary branches the residual determinant on inertia is omega_l, an odd exponent. The original absolute irreducibility, finite ramification, weights, modular reduction and integral ordinarity give all the stated hypotheses of final KW Theorem 5.1. Its conclusion is a weight-two newform. KW's Skinner-Wiles ancestry and the local lemma's BLZ and crystalline-category inputs remain retained inputs with their existing version qualifications.

## KC-LINK-BACK

The two systems have fixed coefficient embeddings and the same absolutely irreducible nonsolvable residual representation at l. Modularity of B gives residual modularity of that representation. A representation induced from a character of a quadratic field has solvable projective image and abelian scalar kernel, hence solvable linear image. The nonsolvable hypothesis thus ensures the residual restriction required by Kisin for A_l. The specified crystalline, determinant, irreducibility and ramification conditions of A_l remain essential hypotheses. No equality A_l=B_l is used or proved.

After modularity of A_l, the coefficient-field compositum places its Frobenius identities and those of the newform in the same number field. Extending the originally fixed P-embedding and using compatibility transports these characteristic-zero identities to A_P. Chebotarev and Brauer-Nesbitt compare semisimplifications; absolute irreducibility of A_P identifies the actual representation. Its fixed residual reduction gives modularity of the original residual representation. This argument is not a transport of characteristic-zero identity from a residual congruence. The final prescribed level/weight refinement remains a separate input.

Khare page 28 expressly identifies the two nonsolvable residual l-representations at the fixed embedding; page 24 has the same link-back pattern. The proposed connection matches that step once the systems and modularity of B have been supplied. It does not supply them.

## The retained caller boundary

The nine-row separation is accurate. KC-NORMALIZE retains the weight/twist and induction-range argument. KC-INITIAL-LIFT retains the particular ordinary weight-two lift, including the semistable endpoint at the original prime. KC-INITIAL-SYSTEM retains a system with the specified original member and the required crystalline member at l. KC-TYPE-CHANGE retains the prescribed nonminimal type at P. KC-RETURN-SYSTEM retains the actual returned P-member, its ramification and its potential Barsotti-Tate property. KC-RETURN-WEIGHT retains the residual weight conversion and endpoints. KC-RESIDUAL-MODULARITY keeps the easy exits apart from the unknown nonsolvable branch. Only the last two conditional lifting/link-back implications are discharged here.

In particular early KW Theorem 3.3 and Theorem 4.2(i) do not by their stated outputs replace those weight-two/type-changing constructions. Khare's pages 26-28 use the second system and the lower-weight induction before link-back in the surviving branch. Treating residual modularity there as already known would be circular; the packet does not do so.

The corrected Section 4 is source-faithful. Page 19 identifies the principal-series type and invokes Breuil-Mézard Proposition 6.1.1 and Savitt Theorem 6.11. Page 24 gives the broader 6.11/6.12 reference. The latter alone establishes no use of the corrected exceptional 6.12 case in this principal-series argument. This decision does not prove the remaining residual-weight conversion or authenticate the final Savitt or Khare editions.

The seven current ed992 locations verify. The main lemma still invokes the published ICM GL2 result directly at lines 590-610; lines 700-715 explicitly describe the subsidiary source route. Those locations are evidence of the present role, not adoption of this new author packet or approval of all caller hypotheses. The current inventory, full seventeen-caller closure, compatible-system construction, final-edition qualifications and release remain outside this decision.
