# Review of the compactified modular-level connection

Reviewer: `/root/astra_v14_baseline_theta`. Author: `/root/sol_protocol_final_review`.

The exact frozen target and any records-only successor are specified in TARGET.json. This review concerns LEVEL-CONNECTION.md, its selected level-geometry source uses, and the resulting input to QM-COHO-COMPACTIFIED-LEVELS. It does not approve the other mathematical providers or the whole ordinary-record packet.

## Independence and source reading

I previously authored related GL2 and Serre arguments, but did not author this level-geometry proof or the separate cohomology proof. Root initially assigned me a new geometry proof, then reassigned me to independent review after Sol identified the existing draft. I wrote no competing proof. The source-reviewer's requested domain, including the need for the actual rational level model, was a review requirement rather than a supplied derivation.

I read final Emerton Section 2.4, printed pages 293 and 294, and viewed the actual page 293 image. The PDF has SHA256 5b2042b8863162f06ba822c4e463bf4290163ad2b57baca05f5ecb71693243fb. It defines the rational open modular curve using orbits of full torsion identifications, gives surjective forgetful maps for subgroup inclusions, states the fine-level criterion, and gives the complex adelic description. I separately read the official Stacks entries 0H1F, 0BXX and 0CCL on 2026-11-08, including the hypotheses and proofs of the extension and finiteness statements. Their selected statements match LEVEL-STATEMENTS.md. This is a dated check of those online entries, not a claim about a different historical snapshot.

I read the entire level proof, the relevant nine-obligation application, the selected use and connection records, the cohomology proof's actual finite-map input at line 25, and current manuscript lines 595 through 599 in the ed992 revision. The manuscript needs geometry for the rational level carrying its given modular Jacobian. It does not need a degree prime to 5 or an etale compactified map.

## Required objects and actual construction

The first-vector stabilizer is the correct rational moduli convention in this proof. In Emerton's torsion-identification convention, two identifications have the same image of the standard point of exact order N precisely when their ratio fixes that point modulo N. Primitive vectors can be completed to bases over Z/N, and these bases lift locally to integral adelic bases. Thus the orbit records the order-N point itself. This identifies the rational moduli problem, not just its complex congruence subgroup.

The determinant is unrestricted: diag(1,u) belongs to this stabilizer for every integral adelic unit u. No Weil-pairing value or root of unity has been fixed. The intersection with SL2(Z) is Gamma1(N), but that analytic check is supplementary to the moduli identification. I do not identify the group here with the earlier note's lower-row convention by notation alone.

At 5 one takes the intersection of the existing 5-component with the principal congruence kernel. This keeps the tame factor fixed even when 5 divides N. The trace proof is valid: a finite-order determinant-one integral matrix has integral trace between -2 and 2, and only 2 in that range is 2 modulo 5. A finite-order matrix in characteristic zero is semisimple, so both eigenvalues equal to 1 force the identity. This supplies the published fine-level criterion. The initial level is not assumed fine.

The classical regular open-level construction remains a named input. Apply 0H1F to the finitely many integral components over Q of the regular open curve. Their disjoint union is a smooth projective Q-scheme containing the whole open level, with a finite reduced boundary. This retains components that become disconnected over Qbar. It makes no choice of a geometric component over a smaller field. The mutually inverse rational maps induced by the initial open identification extend uniquely by 53.2.2, so the initial compactification is the given X1(N).

For a subgroup inclusion the open forgetful map is the published Q-map. A fixed orbit has only finitely many refinements, bounded by the finite subgroup index; quotienting by automorphisms can only identify refinements. Hence no one-dimensional source component is contracted. On each component the existing open map is a rational map into a proper target, so 53.2.2 extends it uniquely over Q. Uniqueness also preserves composition in the tower. The compactified source is proper of dimension one, the target is separated, and every component has nonconstant image. These are exactly the hypotheses of 0CCL, which makes the extension finite.

Surjectivity on the open levels gives a source component over every target component. The finite compactified map is therefore dominant with positive degree there. After geometric base change the same componentwise reasoning applies. This is the precise finite-map input needed by the separately reviewed cohomology argument. Its DVR calculation and norm comparison supply the subsequent rational injection. Ramification at the boundary and a degree divisible by 5 do not invalidate that input.

The boundary here is the finite complement of the actual open modular level in its smooth projective completion. No integral compactification, good reduction at 5, etaleness at the cusps, or independent choice of a cyclotomic component is asserted. The proof does not need to infer properness of an open forgetful map merely from finite fibers; it proves finiteness only after extending to the proper compactifications.

## Nine application checks

| Obligation | Required and supplied comparison |
| --- | --- |
| Source hypotheses | The regular classical Q-level system is retained explicitly; Q is perfect, the compactifications are normal and proper, and the noncontraction hypothesis is proved from finite refinement fibers. |
| Constructed objects | The primitive-vector moduli interpretation identifies the actual Y1(N), and the whole componentwise compactification supplies its given X1(N) and the finer levels. |
| Index and domain | N need not be prime to 5. All finite refinements used in the tower are covered; no geometric component is discarded. |
| Transition maps | The extensions restrict to the published Q-defined forgetful maps, and uniqueness preserves their compositions. |
| Consumed identity | The finite dominant compactified maps have the source and target used at cohomology PROOF.md line 25 and manuscript 595 through 599. |
| Coefficients | The geometric construction is over Q. Inverting the positive degree belongs to rational Q5 cohomology, not integral cohomology. |
| Local conditions | The fine-at-5 trace argument is checked separately; the compactification theorems use regular curves over a perfect field. |
| Exceptional cases | Small initial levels may be coarse, finer levels may have several geometric components, and boundary maps may ramify. None is excluded by an unstated coprimality assumption. |
| Downstream use | The geometry supplies only the stated finite-map and boundary input. The curve/Jacobian, parabolic and norm arguments retain their separate proof and decision. |

## Record findings and limits

The initial ordinary packet bound QM-LEVEL-OPEN's derivation and consumer only to line 3, although the actual primitive-vector and fine-at-5 arguments occur at lines 5 and 7. I requested the exact sufficient span in a preserved successor. I also requested an explicit repeated use of 53.2.2 at line 9 for the mutually inverse initial-compactification identification. These are source-occurrence and evidence-location corrections; no mathematical change was requested. TARGET.json and CHECKS.json identify the final reviewed resolution.

The mathematical decision is bounded to this geometry and its selected source-to-consumer joins. It does not reapprove Emerton's entire article, the inherited GL2 theorem, the separate cohomology proof, the graph-descent provider, complete source coverage, a populated protected profile, live installation, or a release gate. Source files and the author packet were not modified by this review.
