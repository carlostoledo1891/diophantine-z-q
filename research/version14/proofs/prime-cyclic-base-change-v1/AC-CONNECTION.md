# Published prime-degree base change for H-D4

Author: /root/astra_quartic_opt05_anchor. This is an authored source substitution and connecting argument for independent review. It is not an independent acceptance of itself or a new approval of all of H.

## 1. Result and exact scope

The final published Arthur–Clozel volume supplies the cyclic prime-degree automorphic inputs used in the already reviewed H-D4 argument. The proposed substitution uses Chapter III Theorem 4.2(a,d), pp.202–207; the split-place part of Theorem 5.1, pp.212–213; and the strong multiplicity-one statement (2.4), p.200. Chapter III Definitions 1.1–1.2, p.199, specify the weak and strong lifting conventions. Chapter I Section 5, pp.48–50, specifies split places and the unramified Hecke map.

The conclusion is the same restricted theorem as H-D4: for a fixed two-dimensional l-adic representation r over a totally real field F, with a stable lattice and nonsolvable residual image, modularity of parallel weight two ascends and descends along a finite totally real solvable Galois extension. The prime l may be 2. Finite coefficient extensions are allowed. All statements refer to the same r, not merely its projectivization or determinant.

This replaces the need to authenticate the original 1980 Langlands edition for these particular global inputs. It does not authenticate that edition, replace the Hilbert Galois attachment input, or supply general ramified local base change. The latter has a separate proposed connection using both modular Galois attachments and Skinner's local compatibility theorem.

## 2. Publication identity and inspected material

The file arthur-clozel-toronto.pdf has SHA256 3033d863634f5a1e8c26e48ba5b5ec9d8f95fb411b2a6d21c1580db80bc01737 and 17,549,338 bytes. It was downloaded from Arthur's institutional page, https://www.math.utoronto.ca/arthur/pdf/30.pdf. It is a facsimile of James Arthur and Laurent Clozel, Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula, Annals of Mathematics Studies 120, Princeton University Press, 1989.

The actual title and copyright images were read. They identify Princeton University Press, Princeton, New Jersey, 1989; copyright 1989; and ISBNs 0-691-08517-X and 0-691-08518-8. The 248 PDF pages include front matter. Printed page n is PDF page n+16. The scan's contents agree with the publisher-distributed JSTOR record: Chapter I pp.3–74, Chapter II pp.75–198, Chapter III pp.199–224 and bibliography pp.225–233. Clay's collected-works index independently identifies item 30 as this 1989 Princeton book and links its copy. No byte equality with a second download is claimed.

Publication records are https://www.claymath.org/online-resources/arthur/arranged-by-year-of-publication/ and https://www.jstor.org/stable/j.ctt1bd6kj6. The saved JSTOR HTTP response is not relied on as full book content. The human-readable web record and the scan's own front matter supply the identity comparison. The scan is not being rejected merely because it is hosted by an author, and it is not being relabelled from a preprint.

Direct inspection covered III pp.199–213 and pp.217–219, I pp.48–52 and pp.65–74, and front matter. Critical statement and normalization pages were also rendered. This is an inspection of the imported theorem statements and their immediate proof structure, not a fresh proof audit of the entire trace formula or all its ancestors.

## 3. Available theorem and necessary hypotheses

Let L/K be cyclic of prime degree q and let eta be a generating character of K* Norm(A_L*)\A_K*. In III4.2(a), a unitary cuspidal pi of GL(n,A_K) with pi not isomorphic to pi tensor eta has a unique sigma-stable cuspidal weak lift Pi. In III4.2(d), a sigma-stable cuspidal Pi over L has a cuspidal descendant pi over K; its descendants are the q eta-twists, and pi is not isomorphic to pi tensor eta. The definition of weak lift raises unramified Satake matrices to the residue degree. These are prime-degree assertions as printed, not applications of the later arbitrary-degree descent lemma.

H-D4 uses n=2 and the unitary normalization of a weight-two cuspidal representation. Its arithmetic roots at v are alpha_v,beta_v, with alpha_v beta_v=q_v s_v. The unitary roots are alpha_v/q_v^(1/2), beta_v/q_v^(1/2). Raising them to the residue degree f and multiplying by q_w^(1/2), where q_w=q_v^f, gives alpha_v^f,beta_v^f. This agrees with arithmetic Frobenius on the restricted l-adic representation. This calculation makes no claim about a ramified local parameter.

Every restriction of r to an intermediate field has absolutely irreducible residual representation. Indeed its image contains the nonsolvable normal image over the top field; the quotient is solvable. A two-dimensional reducible finite image over the algebraic closure is triangular and solvable. A characteristic-zero invariant line would, after a finite coefficient extension, intersect the stable lattice in a saturated line and reduce to a residual invariant line. Thus every characteristic-zero restriction is also absolutely irreducible.

## 4. Ascent and the exact no-self-twist condition

Suppose r restricted to G_K is attached to pi, and L/K is one prime step. If pi were isomorphic to pi tensor eta, its unramified polynomials and the retained attachment, Chebotarev and Brauer–Nesbitt inputs would give r isomorphic to r tensor eta_l. Taking determinants gives eta_l squared equal to 1. Since eta_l has exact prime order q, this is impossible for odd q.

For q=2 choose an invertible intertwiner A satisfying A r(g)=eta_l(g) r(g) A. Its square commutes with r and is scalar by absolute irreducibility. After a finite coefficient extension and rescaling, A squared is 1. It cannot be scalar, since eta_l is nontrivial. In characteristic zero its two distinct eigenspaces are lines stable under G_L. This contradicts irreducibility over L. The argument concerns characteristic-zero matrices even when l=2, so it does not divide by 2 in a residual coefficient ring.

Consequently III4.2(a) applies and gives a cuspidal lift. Section 5 below gives its weight at real places. Its attached Galois representation agrees with r restricted to G_L by the arithmetic-root calculation and Chebotarev. Equality is an actual two-dimensional isomorphism, not merely equality of semisimplifications with an unspecified extra constituent: the common semisimplification is irreducible of dimension two.

## 5. Why the real-place assertion is available

Weak lifting alone does not state the infinity type. The source for this part is III5.1, which assumes the same prime-degree setting as III4.2 and upgrades weak to strong lifting. All real places of a totally real extension are split: L tensor_K K_v is a product of copies of R. At a split place local lifting repeats the representation without change. Thus ascent and descent preserve the parallel-weight-two real discrete-series components.

Here is the immediate split-place proof check, so this use does not silently appeal to the later composite-degree descent. In the no-self-twist case, III5.1 on p.212 starts from the prime-degree global trace identity already used for III4.2. It separates Hecke eigenvalues and obtains the local twisted character identity up to a nonzero scalar. Chapter I Section 5, pp.48–49, identifies the transfer of a tensor of test functions at a split place with their convolution. The Galois action cycles the factors. For a tensor product of equal local representations, the trace of the tensor operators followed by that cyclic permutation is the trace of their product. This is the finite-rank tensor trace identity, extended to the smoothing test operators in the character identity. Consequently the local character in the descended representation is proportional to the character of any split lifted factor. Independence of irreducible admissible characters makes the representations isomorphic. No non-split local parameter classification is needed for this split conclusion.

The full printed proof of III5.1 also handles non-split places using local results in Chapter I and Langlands classification. Its reference to Lemma I.6.3 on p.213 is a local twisted-character independence lemma on p.52. It is not the erroneous composite-degree Lemma III.6.3 on p.217. This packet consumes only the split conclusion. It retains the prime-degree trace identity and character theory as published proof inputs; it does not newly prove the trace formula.

The descended unitary central character has trivial restriction to each positive real multiplicative group, since its real components are the weight-two ones. At finite places it is smooth with an open conductor. Quotienting by that conductor and the connected real factors leaves a finite ray class group. Its central character therefore has finite order. The descendant lies in the weight-two Hilbert attachment scope retained by H-D4. No unrestricted nonalgebraic automorphic representation is fed to that attachment theorem.

## 6. Descent, twist and prime-step iteration

Suppose Pi over L is cuspidal of weight two and attached to r restricted to G_L. For a generator sigma of Gal(L/K), the conjugate Galois representation is isomorphic to r restricted to G_L, since r is already defined over K. Unramified arithmetic polynomials therefore agree for Pi and Pi^sigma. Statement III(2.4), p.200, gives Pi isomorphic to Pi^sigma. This verifies the hypothesis of III4.2(d); invariance is not presumed from the existence of a lift.

Choose its cuspidal descendant pi. By Section 5 it has the required real components and finite-order central character. Attach R=r_pi using the retained Hilbert-form theorem. The restrictions of R and r to G_L are isomorphic and absolutely irreducible. Identify them once. For g in G_K, C(g)=R(g)r(g)^(-1) commutes with the common restriction, because both matrices implement conjugation on G_L. Thus C(g) is scalar. These scalars multiply, are trivial on G_L and define a finite character chi of Gal(L/K), with R=r tensor chi. Twisting pi by the inverse Hecke character gives the exact r over K. Under arithmetic reciprocity the Hecke value at an unramified uniformizer is chi(Frob_v); this fixes the inverse direction of the corrective twist. The character is trivial at real decomposition groups because those places split.

Take a prime cyclic tower inside the given solvable totally real Galois extension. At each downward step use the restriction of the original r as the target, correct the finite twist, and prove invariance again at the next step from that r. The proof never assumes that an arbitrary choice of descendant is invariant under the next Galois action. It need not combine the corrective characters into one character of the possibly nonabelian full Galois group.

## 7. Public correction history and bounded related-use check

Clozel's public seminar abstract at https://www.math.columbia.edu/~urban/SeminaireAFA/Clozel.html identifies a mistake in III Lemma6.3, p.217, and describes later work with Rajan on solvable descent. The exact downloaded notice is pinned. It is evidence about the source's history, not the theorem supplying this application.

The printed III6.3 proof first invokes prime descent to obtain an intermediate representation and then invokes descent again. The missing justification is the invariance needed for that intermediate descent. This packet does not use III6.3, III6.4 or III6.6, nor claim that the printed arbitrary cyclic descent proof is correct. It does not import the later Clozel–Rajan correction as a replacement theorem. The field tower here carries an independently given global r, which supplies the missing invariance at every step by Section 6.

The immediate proof of III4.2(a,d), pp.203–207, uses the trace identity III(4.1), Chapter II17.8, lower-rank prime-degree cases, and the Rankin–Selberg facts in III2. Its induction is on the representation rank, not on a composite extension degree. The proof of III4.2(d) proves cuspidality using lower-rank lifts and poles, then obtains the twist fiber using III3.1. Neither proof invokes III6.3. The split part of III5.1 examined in Section 5 starts from the same prime trace identity and also does not invoke it. This establishes the stated immediate dependency separation, not a new audit of every ancestor of the trace formula.

Related occurrences in the frozen H-D4 proof are its named-source paragraph, normalization at split and unramified places, ascent paragraph, invariance/descendant paragraph, and final prime-step iteration. CONSUMERS.json binds each exact old passage and states its proposed replacement. The old Section 6 warning about the limited IAS local statement remains valid history. It must not be changed into a claim that this AC packet supplies arbitrary ramified local compatibility.

## 8. Retained inputs and status

The following remain theorem inputs rather than consequences proved here: the published AC prime-degree trace-formula results; the Rankin–Selberg/strong-multiplicity-one input identified on p.200; Hilbert Galois attachment for the actual weight-two forms; arithmetic class field theory for finite twists; and characteristic-zero Chebotarev/Brauer–Nesbitt. H-D4's finite field construction, local p-adic Hodge statements and modularity-lifting arguments are outside this source substitution.

The original Langlands edition remains un-compared, but would no longer be needed for these selected global statements after independent acceptance of this packet. The original DDT source obstacle is separately closed by the compiler's accepted final Theorem2.19 connection. The general local-BC connection proposed by source_review is separately pending and is not presumed accepted here. No whole-Duke, whole-KW, whole-AC or whole-H source closure is asserted.

The local-only scan, extracted text, page images and downloaded web records are inspection evidence. They are not proposed for redistribution with the public project. This packet has no live manuscript edits, no purchase, no private correspondence and no optimization result.
