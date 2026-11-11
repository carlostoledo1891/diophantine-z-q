# Independent review of the H-D4 automorphic connection

Reviewer: /root, a distinct model agent from author /root/astra_v14_baseline_theta. The runtime does not expose a verified serving-model identifier. This is an informal mathematical review, not formal verification. I read the author's proof before its source-use cards, so this is not a blind inventory reconstruction.

Target: h-d4-automorphic-descent-theta-001, manifest SHA256 d9ec9e65f96fc1f8ba5282dac6518d482418037b96f8ffc96ae5a16c655c45ae; PROOF.md SHA256 116442a0bf2f5c99b1006da791f1920c9bad9c500f4522cb8102ff586ba38c2e.

## Decision and boundaries

Accept the new conditional connection in PROOF.md Sections 2-5 and its stated application order in Section 6. It proves ascent and descent for the given representation, under the named automorphic and Galois-attachment inputs. It does not close the original-edition qualification for Langlands, the full Hilbert-form attachment source check, or the ramified local compatibility used by H-D5. Those are retained obligations, not consequences of this acceptance. This decision does not accept all of H, all of Serre's theorem, the manuscript, or a release.

The distinction is mathematical as well as documentary. A number-field existence theorem does not supply an automorphic descent theorem. An unramified Hecke comparison does not supply a theorem at every ramified place. The packet keeps both distinctions in its assertion and source-use records.

## Source comparison

I read the supplied IAS text at printed pages 2, 9-10, 13, 15, 133, 136-137 and 142. I also inspected the rendered pages 133 and 142. Lemma 11.3(b) supplies a cuspidal quasi-lift outside the specified quadratic induction exception, and Proposition 11.4 turns that quasi-lift into a lift. Lemma 11.6(b), on page 142, is the global invariant cuspidal descent statement. Proposition 11.5 is a local statement and cannot replace it. Lemma 3.1 supplies strong multiplicity one without an extra archimedean matching premise.

Chapter 2(e), on page 10, expressly restricts its Weil-parameter assertion to reducible or dihedral parameters. The following paragraph even discusses the difficulty of enlarging that scope. Thus the packet correctly refuses to use this passage as arbitrary ramified local-global compatibility. Chapter 2's principal-series definition and the split-place description on page 2 support the two elementary local comparisons actually used here.

These checks concern the inspected IAS retypesetting. They do not establish identity with the 1980 printed edition. Under Protocol 1.4's final-source requirement that edition comparison remains open. The retained class-field-theory, Chebotarev, Brauer-Nesbitt and full Hilbert attachment inputs also need their existing or forthcoming exact source records; this review does not fabricate those records from citations in Kisin.

## Reconstructed connecting argument

Let N be the residual image over the solvable Galois extension M. It is normal in the original residual image G, and G/N is solvable. If N were solvable then G would be solvable. The same nonsolvable N lies in the image over every intermediate field. A reducible two-dimensional representation over the algebraic closure has triangular, hence solvable, image. Every residual restriction is therefore absolutely irreducible. An invariant characteristic-zero line would intersect an extended stable lattice in a saturated rank-one submodule and reduce to an invariant line. This proves the needed characteristic-zero absolute irreducibility, including at coefficient prime 2.

For one cyclic step L/K, the excluded automorphic induction case gives the quadratic self-twist of the representation over K. If A implements that self-twist, A squared is scalar by Schur's lemma. After coefficient extension A has distinct eigenvalues 1 and -1. A cannot be scalar because the quadratic character is nontrivial. Its two eigenspaces are invariant under G_L, contradicting the absolute irreducibility just proved. This is a characteristic-zero argument even when the residual characteristic is 2. It does not import the omitted proof of Langlands Lemma 11.7.

The Satake calculation is consistent: after dividing arithmetic roots by the square root of the residue cardinality, unramified base change raises the unitary roots to the residue-degree power. Multiplying back by the square root of the new cardinality gives exactly the powers of the arithmetic roots. All exceptional finite places may be excluded in the Chebotarev comparison. A two-dimensional representation whose semisimplification is irreducible is itself irreducible, so the conclusion gives the actual restriction, not just an unexamined semisimplification.

For descent, the representation already defined on G_K proves the conjugation invariance of its restriction. This gives equality of almost all Hecke polynomials of Pi and its conjugate, and strong multiplicity one supplies the invariance required by Lemma 11.6(b). The descendant has weight two because every real place splits in this totally real extension. Its central character is trivial on the positive connected real factors; with its open finite conductor it factors through a finite ray class group. Thus it meets the stated attachment interface.

After identifying the restrictions of R and r to G_L, the discrepancy R(g)r(g)^{-1} commutes with that common irreducible restriction. It is scalar, multiplicative and trivial on G_L. It is therefore a finite quotient character chi of Gal(L/K), with R=r tensor chi. Twisting the descendant by the inverse Hecke character gives exactly r. This establishes the direction of the twist and avoids substituting determinant equality for representation equality. The finite character is trivial at real decomposition groups, so weight is preserved.

Iterate along a cyclic-prime tower for M/F. For an intermediate K which is not normal over F, the claimed converse still follows: first ascend from F to M, then descend from M to K. The extension M/K is Galois with solvable group, so its own cyclic-prime tower applies. No unsupported claim that every intermediate K/F has a cyclic Galois tower is necessary.

## Actual application and related uses

I read H003 Section 6 and the existing independent field-construction review. The latter accepts a solvable totally real normal closure with the prescribed completions under its explicitly Galois local-target premise. The new packet applies ascent to the modular comparison form through the preparation fields. It applies descent to the target only after the final modularity argument. It preserves the early split Q2 places until the ordinary local lemma has been applied. It does not infer modularity of the target from descent of a different comparison form.

The comparisons in RELATED-USES.json cover the relevant mechanisms in this bounded application: loss of cuspidality on ascent, failure to establish invariance before descent, a finite twist after descent, and overextension of unramified compatibility to ramified places. The conditional argument addresses the first three at every cyclic step. It retains the fourth as H-D5 rather than claiming to have proved it. Principal-series inertia must actually be killed; nonzero Steinberg monodromy stays nonzero after finite restriction. Barsotti-Tate properties are not asserted to descend through arbitrary ramified extensions.

No whole-manuscript source-coverage decision is made here. The packet's eight source-use entries and nine comparisons describe this connection, including its open inputs; their presence does not establish coverage of the rest of the proof. Old decisions and manuscripts remain unchanged.
