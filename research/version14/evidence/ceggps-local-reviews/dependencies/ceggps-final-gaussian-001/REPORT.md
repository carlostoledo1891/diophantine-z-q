# CEGGPS final-edition access and source-interface record

Author: /root/astra_v14_baseline_gaussian. Date: 2026-11-08. This is an authored source qualification record, not independent acceptance of the proposed mathematical replacement. Final-edition qualification remains open.

The target is Caraiani, Emerton, Gee, Geraghty, Paskunas and Shin, *Patching and the p-adic Langlands program for GL2(Qp)*, Compositio Mathematica 154 (2018), 503–548, DOI [10.1112/S0010437X17007606](https://doi.org/10.1112/S0010437X17007606). The current consumer proposal is the separately authored `independent-source-review/ceggps-route-001/PROPOSAL.md`. Its hash at inspection is in SOURCE-PINS.json. This record does not adopt that proposal.

## 1. Actual access outcome

The ordinary public [Cambridge article endpoint](https://www.cambridge.org/core/journals/compositio-mathematica/article/patching-and-the-p-adic-langlands-program-for-operatornamegl2mathbbqp/1B076A22D923C604561A010C0A5BFF0E) returned an abstract/access page. Both its short PDF endpoint and the complete PDF URL advertised by its own `citation_pdf_url` metadata returned HTML, not PDF. The exact URLs, local response hashes and content signatures are preserved in ACCESS.json. One response initially had a `.pdf` filename; before freezing this packet it was renamed `.html`. No response is relabelled as a journal paper.

The [Imperial repository](https://spiral.imperial.ac.uk/entities/publication/badb3229-6155-4545-8c4d-b7e413551f13) explicitly identifies `1609.06902v2.pdf` as the accepted version and says it precedes possible editorial changes. Official author-hosted copies and the author publication pages did not supply an authenticated final typesetting. The Caraiani copy has the arXiv v2 heading and author pagination. Emerton's official copy also has author pagination. Shin's publication entry links to arXiv. Publication metadata does not establish equality of editions.

The visible official option was **Get access**. No exact purchase price or priced product was visible in the fetched page or returned public text. The stored HTML was searched for purchase-price fields; generic currency configuration and purchase-modal feature flags are not price quotes. No checkout, account change, payment or authentication bypass was attempted. A purchase is not requested by this record. It should be considered only if the mathematical replacement survives independent review and the final text remains necessary.

## 2. What was actually read

The substantive checks below use the pinned accepted arXiv v2, not an unseen final edition. Its source pagination is used throughout. The official author copy is separately pinned and its pages 2 and 8 support the same normalization warning; no whole-document equality claim is made. The inspected accepted passages include pages 2–3, 7–8, 11–12, 15–17 and 32–41. The exact relevant source interfaces are itemized in INTERFACES.json. Reading these passages identifies required comparisons, not a completed proof audit of every cited source.

### Normalization

Section 1.12.1, page 7, assigns cyclotomic character epsilon the Hodge–Tate label -1 and sends a uniformizer to geometric Frobenius under local reciprocity. Sections 1.12.2–3 separately fix the local Langlands normalization and the meanings of the different duals. These are part of the input, not disposable notation.

Body Section 2.1, page 8, associates `det^A Sym^B` with labels `(1-A,-A-B)`. For increasing labels `u<v`, solving gives `B=v-u-1` and `A=1-v`. Thus the algebraic factor is `Sym^(v-u-1) det^(1-v)`. Its central exponent is `1-u-v`, agreeing with the algebraic exponent of `det(r) epsilon` in this convention.

The introductory Example 1.2 on page 2 and its AA3 restatement on page 3 instead print exponent `1-a` for increasing labels `a<b`. That conflicts with the body definition. This is an observed inconsistency in the accepted/author text. It is not a claim that the final edition contains the same inconsistency. The proposed route must use a declared convention and verify the final text before making any edition-equivalence claim.

Page 35 also explicitly adjusts the modified Colmez functor by inverse cyclotomic twist relative to Paskunas. For the same Banach representation, the proposed identification `r=V tensor epsilon^(-1)` must retain that twist. It preserves inertial type but can change the unramified Weil parameter. Equality of full Frobenius parameters cannot be inferred merely from equality of algebraic factors or inertial types.

### Residual and crystalline scope

Assumption 2.2 on page 8 requires scalar endomorphisms and excludes twists of the extension with subcharacter omega and quotient 1. The opposite nonsplit orientation is not the displayed exclusion. A selected lattice of one irreducible characteristic-zero representation does not identify an entire projective-envelope family with another one. Section 6.27 on pages 37–38 treats scalar semisimplification speculatively, not as an established extension of the theorem.

Sections 3.1 and 3.3 on page 15 give the arithmetic-action and pointwise Hecke conditions on crystalline algebraic-weight support. Section 3.4 on pages 16–17 constructs an arithmetic action from the earlier patching paper and chooses trivial inertial type in this argument. It does not alone assert an arbitrary-supercuspidal-type auxiliary global point.

For the Section 6 route, Proposition 6.14 invokes Paskunas's results for the weight modules, including his Proposition 4.14. Proposition 6.17 verifies the Hecke action on crystalline points using the explicit crystalline comparison. Theorem 6.18 then constructs the arithmetic action on the twisted envelope, and Corollary 6.19 identifies the Galois functor at a point. A proof avoiding the unresolved general supercuspidal comparison must justify the restricted uses of the cited results; the word 'patching' does not itself establish independence from that comparison. This packet does not decide that dependency question.

### Minimal-level global comparison

Sections 7.1–7.4, pages 38–40, require an odd absolutely irreducible global residual representation, irreducibility after restriction to Q(zeta_p), the local Assumption 2.2, p>3 in Theorem 7.4, and no vexing primes. The tame level is exactly the minimal conductor level Gamma_1(N). The accepted text describes the relevant local minimal-deformation smoothness and cites CHT08 Lemma 2.4.19. Remark 7.1 warns that arbitrary tame level does not inherit the same assertion.

Equation (7.2) identifies completed homology through the patched quotient and the **R-linear dual** of the universal global representation. Theorem 7.4 identifies the resulting completed homology with the envelope tensored over the local deformation ring with that dual. Corollary 7.5 gives the residual cohomological consequence. Passage from this homology statement to a continuous cohomological weak map must handle the stated duals and topologies. The displayed tensor identity is not already the desired cohomological map with all factors unchanged.

The proposed auxiliary route uses an irreducible local residual representation and invokes Lemma 2.15 and Proposition 6.21(i) for the residual weight input. Those are distinct suppliers from the characteristic-zero type lift. A Jordan–Holder constituent of a lattice does not lift by this theorem alone; the proposed cohomology/injectivity argument needs its own review. The unchecked quaternion generalization of Remark 7.8 is unnecessary and is not used.

## 3. Bounded corrections check

Public searches for the exact title with 'erratum correction' and the DOI found the article, accepted repository record and author copies, but no correction addressing this article. Shin's official two-page errata file was downloaded and read in full; it contains no entry for CEGGPS. This is a bounded negative observation, not a proof that no correction exists. The accepted-text determinant inconsistency remains an explicit issue despite that negative search.

## 4. Remaining work and boundaries

The final paper has not been obtained. The exact final definitions, theorem hypotheses, determinant formulas, proof dependencies and corrections therefore remain unverified. The needed comparison must cover Sections 1.12, 2.1–2.2, 3.4, 6.14/6.17–6.21 and 7.1–7.5, with the residual weight passages used by the actual route. Journal page numbers must be read from the final paper; this packet does not manufacture them by an offset.

The separate mathematical proposal still needs independent review of its auxiliary residual construction, fixed-level type lift, cohomological dualization, classical local-global supplier and the restricted dependencies in Section 6. This record grants no new mathematical acceptance and changes no manuscript. All downloaded full texts and access responses remain local-only; portable evidence consists of hashes, URLs, locators and these comparison notes.
