# B11 Tate and polarized-automorphism review

Accepted within the four bounded source/application scopes below. The exact target is b11-tate-polarized-author-003/MANIFEST.json, SHA256 d848b6b4f8e2685f4b11bf75832a8b9d9815e829ae6716d81753a1c542ba7b16. This metadata overlay explicitly inherits the original001 proof and source packet, manifest a642be5bb8aeab975f5a8264575a9eb3e355703676e9be4f1b7a678e1ce8c656. The proof remains SHA256 595c1953b79d8b1df869a9915c8325bb4ed50e38ca5faa0fbc1850015bc3b3fe. Both metadata wording occurrences are corrected.

## Scope and independence

This review concerns the four bounded applications B11-TATE-RANK, B11-TATE-FAITHFUL, B11-END-LATTICE-CORRECTED and B11-POLARIZED-AUT-FINITE. I did not author these applications or the endomorphism-lattice repair. My clarification request changes only the erroneous phrase finite subgroups to finitely generated subgroups in the objects metadata. The proof already uses the correct hypothesis.

The field is algebraically closed, of characteristic different from3. All automorphisms are group automorphisms fixing the identity and preserving the polarization morphism. The argument includes positive characteristic. It does not use complex uniformization, a lift to characteristic zero, an ordinary or supersingular restriction, or a Tate-conjecture surjectivity assertion.

## Primary source reading

I directly inspected the published1986 scan at printed115–116,122–125 and137–139. The scan is SHA256 86259344a576e4ef75a9d81e9bf43143f872a72b14cf8fcc2703f3aea6349136. The source is Milne's Chapter V, Abelian Varieties, in Arithmetic Geometry, Springer1986, pages103–150. The author's publication page identifies that scan separately from his corrected notes.

The source statements used are Theorem8.2 and Remark8.4 for prime-to-characteristic torsion and Tate rank; Proposition12.1 and its simple-factor consequence; Lemma12.2 for the injection on actual Hom groups; Proposition12.4 for the polynomial degree function; Lemma12.6 for divisibility of an actual homomorphism; the trace definition on125; Theorem17.3 for Rosati positivity; and Proposition17.5(a) for the stated finiteness conclusion. The reverse-isogeny construction is also present immediately before Theorem8.2 on115.

The official errata explicitly flags the proof of12.5 on124. It also limits the printed proof of12.1 over imperfect fields. I read the errata and the corrected12.5 discussion on page22 of the2022 notes, keeping that version distinct from the published chapter. The proposed argument supplies its own final finite-generation deduction; the new inference is assessed below rather than being certified merely because a corrected source exists. The perfect-field issue does not occur over an algebraically closed field. Other source corrections are not silently declared absent or irrelevant to the whole chapter.

## Tate rank and the actual module

Theorem8.2 makes multiplication by3^n finite etale of degree3^(2ng). Over the algebraically closed field, Remark8.4 supplies the rank2g Tate module with transition multiplication by3. For g=2, T3 has rank4 and V3 has dimension4. The first projection is onto A[3](k), since successive division points exist. If x1=0 for a compatible sequence x, the sequence yn=x_(n+1) lies in A[3^n](k), is compatible and satisfies3y=x. This proves the exact kernel3T3 and hence the asserted quotient. The projection and this equality are compatible with the given order action by functoriality.

The unital order action extends to its3-adic completion on the finite free Tate module and then to B3 on V3. A unital representation of a division algebra on a nonzero module is faithful because its kernel is a proper two-sided ideal. A finite-dimensional module over that division ring is free, and the Q3 dimension formula makes its B3 rank one. This step does not need the general End(A)-faithfulness theorem. It does retain the given unital order action and the assertion that B3 is a four-dimensional division algebra. Principality of the integral order lattice is a different argument.

## Integral faithfulness

Lemma12.2 is an injection of actual Hom groups, not a surjectivity statement about linear maps. If an endomorphism has zero Tate action, it kills every geometric3-power torsion point. On a simple positive-dimensional abelian subvariety, a nonzero restriction has finite kernel, whereas the3-power torsion cardinalities are unbounded. The restriction is therefore zero. The isogeny decomposition of12.1 then gives zero on A. Equivalently, one may compose with the simple factors of an isogeny onto A and use surjectivity. Applying this to alpha-1 gives the exact implication needed by the stabilizer argument.

This reasoning is independent of the flawed finite-generation sentence in the printed proof of12.5. It uses prime-to-characteristic torsion and the simple-factor decomposition over the permitted perfect field.

## Endomorphism-lattice repair

The repair is valid. Let S be simple, M a finitely generated free subgroup of End(S), V=QM and D=V intersect End(S). Torsion-freeness follows from12.2. Proposition12.4 is defined by restriction to every finite-dimensional subspace, so it does not presuppose that all of End(S) has finite rational dimension. Its restriction extends to a real polynomial on V tensor R and is zero at zero. Every nonzero element of D is an isogeny, hence has positive integral degree. An open ball sufficiently close to zero is therefore disjoint from D minus zero. Additivity makes D uniformly discrete. Its intersection with a compact fundamental parallelepiped of M is finite, and every D/M class has a representative there. Thus D/M is finite and a denominator N_M exists. It may depend on M.

For a putative nonzero Z3 relation among the Tate images of a basis e_i of M, approximate its coefficients a_i by integers n_i modulo3^m. The resulting actual endomorphism has Tate matrix divisible by3^m. Lemma12.6 applies: etaleness detects its vanishing on the3^m-torsion subgroup scheme and allows factorization through multiplication by3^m. Hence3^(-m) sum n_i e_i belongs to D. Multiplying by N_M implies every coefficient N_M n_i/3^m is integral. Choose a nonzero a_j and m>v3(N_M)+v3(a_j). Then v3(n_j)=v3(a_j), contradicting that integrality. The Tate images are therefore Z3-independent, so rank(M) is at most(2 dim S)^2.

Because this bound holds for every finite independent set, End(S) has finite rational rank. Choose M spanning that rational vector space and apply the same discreteness argument again. Now D=End(S), so finite generation follows. This second use of discreteness is precisely what cannot be replaced by the assertion that a torsion-free finite-rank group is finitely generated.

For arbitrary A, an isogeny with a product of simple factors and a reverse isogeny give an additive injection of End(A) into the endomorphisms of that product. The matrix-entry Hom groups vanish between nonisogenous simple factors; between isogenous factors, composition with a fixed isogeny injects the Hom group into the already finitely generated endomorphism group of a simple factor. These injections use connectedness of the image to rule out a nonzero map into a finite kernel, and do not require an isogeny to be an isomorphism. Subgroups of finite free abelian groups are finite free. Thus End(A) is a lattice in its finite-dimensional real span.

No uniform N_M, nonsimple degree-positivity assertion, or arbitrary finite-rank finite-generation principle has entered this argument.

## Polarized automorphisms and the callers

For alpha preserving lambda, alpha^vee lambda alpha=lambda implies alpha^dagger alpha=1. Theorem17.3 supplies the positive definite Rosati trace form. The trace convention gives Tr(1)=2 dim A=4. The real level set q=4 is compact, and the repaired End(A) lattice intersects it in finitely many points. This proves finiteness of the polarized group automorphisms and hence finite order of each such automorphism. It supplies no bound on their number and does not include arbitrary translations. Proposition17.5(b), including its separate level argument, is not used.

I read the exact historical925967 consumer at708–721 and723–731. For THREE-MARKING the packet supplies Tate rank, the natural mod3 identification and the rank-one rational B3 module. It does not itself prove the finite-etale Isom sheaf, the local maximal-order lattice assertion, or its nonempty geometric fibers. For FIVE-ACTION-FREE it supplies finite order and integral Tate faithfulness. The independent odd-prime congruence argument, followed by the full-five marking, is still required. Finiteness of geometric automorphisms is not silently upgraded to a statement about an arbitrary automorphism group scheme.

The four ten-field assertions and their36 obligation entries match these bounded scopes after the metadata correction. The earlier925967-to040646 transport is separately pinned. This decision does not rebind the consumers to a later source, approve an entire B11 construction, or settle the other marking, quotient, descent or degree arguments.


## Exact successor and verification

The003 overlay changes only the two JSON field values identified above: the End-lattice assertion objects and its constructed_objects obligation now say finitely generated subgroups. All other field values match001 exactly. The overlay pins001 for its unchanged proof and sources and preserves the intermediate002 manifest. It does not duplicate the full source directory. The initial reviewer checker assumed a standalone copy and stopped; CHECKER-CORRECTION.md records that corrected assumption. No author defect or mathematical acceptance was inferred from that checker failure.

The independent corrected check verified 3 overlay members, 41 original members, the preserved002 members, 50 distinct referenced files and 7 distinct exact spans. It performed 347 pin/span checks and verified the exact two-value metadata delta. These checks bind the independently read mathematics; their success is not itself mathematical validation.

The lattice proof does not use Rosati positivity or polarized-automorphism finiteness, so the later compactness argument is not circular. The trace value needed there also follows directly from the characteristic-polynomial convention at the identity. The accepted scope is not the stronger completed-Hom or cokernel assertion, nor all of Milne Chapter V.

This is not final B11, source-inventory, all-proof, protocol or release acceptance. The bounded records still require faithful ordinary-schema/current-consumer integration where requested. Full source PDFs, rendered pages and extracted correction text remain local-only.
