# Independent review of the final DDT source connection

Reviewer: `/root/astra_v14_baseline_compiler`. Connection author: `/root/astra_quartic_opt05_anchor`. The exact reviewed author manifest and its file pins are bound in `DECISION.json` and `INPUTS.json`.

The source connection `DDT-FINAL-GENERAL-SELMER` is accepted for the three finite-module applications it states. This closes the author-version limitation for that input by using the actual published theorem. It is not acceptance of the entire general-field Taylor-Wiles proof or of the other inputs of that proof.

## Source and statement

I independently read the publisher scan's title page and printed pp.54–58 before reviewing the author's conclusion. The final PDF is Darmon, Diamond and Taylor, *Fermat's Last Theorem*, Current Developments in Mathematics 1995, pp.1–154, DOI 10.4310/CDM.1995.v1995.n1.a1, SHA256 `2b45bf258d078924f008ff178a49d78e033c83541af5f9c95fa1aeab215e235d`. The source record identifies the International Press archive URL and publication metadata. The scanned pages were read visually because the PDF has no usable extracted text on these pages.

Theorem 2.19 on p.57 explicitly applies to a number field F and a finite discrete G_F-module M. The local subgroups of ordinary H1 are unramified at almost all places. It states finiteness of the dual Selmer groups and the cardinality ratio with the global invariant ratio and the product of local-condition sizes divided by ordinary local H0 sizes. It imposes neither an odd-primary restriction nor an unramified-at-2 field hypothesis. The odd-prime assumption printed below it starts Section 2.4 and does not qualify Theorem 2.19.

The dual is the cyclotomic additive dual Hom_Z(M,mu_n), with the contragredient action and n annihilating M. I checked the corresponding Theorem 2.19 text in the later author version on p.62. The required statement and formula agree. This comparison makes no claim about the whole author version, the 2000 file or the 1997 reprint.

## Real places

Theorem 2.18's proof on p.56 includes the quotient by the real-place norm image (1+c)M in the Poitou-Tate sequence. The Euler-characteristic factor cancels this correction and yields ordinary H0 in the final product. The following paragraph explicitly extends the argument to number fields before stating Theorem 2.19.

The author's warning about Theorem 2.17(c) is necessary and correct. Its degree-zero pairing at a real place cannot be read as a perfect pairing on unrestricted ordinary H0. That intermediate degree requires Tate H0. The present connection uses the perfect ordinary H1 pairing, where this distinction does not change the group, and the stated final Selmer ratio. It does not assert H1(R,M)=0 for 2-primary modules. It also does not replace the final ordinary-H0 denominator by Tate H0. The definitions and proof therefore support exactly the convention needed by the consumer.

## Application to the actual modules

All three substitutions, End_k(k^2), k and Z/2^j, are finite continuous additive modules. In the consumer, S contains the infinite places, the 2-adic places and all ramification. Q is disjoint from S. Zero local conditions at S, full conditions at Q and unramified conditions elsewhere meet the theorem's hypotheses. Under local H1 duality, the zero and full subgroups have the stated full and zero annihilators. The theorem itself quantifies over every place, so there is no omitted real-place factor.

For the full matrix module, the connection uses Tr_(k/F2)(tr(XY)). This is Galois invariant under conjugation. If X has a nonzero entry, a corresponding matrix unit in Y detects it; scaling that unit permits a nonzero finite-field trace. Thus the pairing is nondegenerate in characteristic two. Scalar trace-zero matrices do not create a kernel in the full matrix algebra. This identifies the additive Tate dual used by DDT with the required twisted linear dual. The mod-two cyclotomic twist is trivial. For Z/2^j, the twist remains mu_(2^j), exactly as the consumer uses.

Taking logarithms to base |k| in the vector-space cases is valid; for Z/2^j the proof uses cardinalities. There is no passage to infinite coefficient modules. The connection supplies the finite global ratio. It does not by itself compute local dimensions, global invariant sizes, Kummer orders or the class-field quotient; those are distinct steps in the consumer's proof.

## Consumer binding and scope

The author binds theta001 Sections 1, 5 and 6. I checked their raw slices and compared the corresponding ranges with theta003, proof SHA256 `69d535145031e224f2eec621a243de6d492facc17bf85a5c27dbe8c3a89907fd`. All three slices are byte-identical, so this source application also binds to those same ranges in theta003. Its separate changed line 50 is outside this review.

My earlier conditional review of the Taylor-Wiles calculation did not author the present source connection, finite-field trace explanation or final-edition comparison. I supplied no repair to this packet. The accepted input is the explicit published Theorem 2.19, not an inference that every cited theorem in DDT has been independently reproved. The cited Milne duality, finiteness and Euler-characteristic results remain named ancestors. NSW electronic-to-print equivalence is unnecessary for this accepted DDT substitution and is not decided here. No live source or prior review was modified.
