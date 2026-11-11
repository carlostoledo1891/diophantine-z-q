# Pan's local-ring use of Thorne 2015 and the published 2020 correction

Author proposal, 8 November 2026. This packet has not received independent acceptance. It concerns Pan's author text, Lemma 4.2.10 and Proposition 4.2.4, under the actual prime 5 specialization. It does not certify Pan's proof or identify an adopted replacement for its main theorem. The current manuscript remains the 63db4260 source pinned in SOURCES.json.

## Source-only finding

Allen, Newton and Thorne, *Automorphy lifting for residually reducible l-adic Galois representations, II*, Compositio Mathematica 156 (2020), 2399–2422, DOI 10.1112/S0010437X20007484, is available as the final publisher PDF. Section 3.1, pp. 2406–2407, corrects Thorne 2015, Proposition 3.15(1). The special fiber of the entire unreduced trivial-character lifting ring need not be generically reduced, including in dimension two. Proposition 3.1 instead proves generic reducedness after first taking the nilreduction of the lifting ring. The correction also supplies the needed changes to Thorne's Proposition 3.17 and Lemma 3.40(2). These are exact published corrections, not an inference from a later theorem with a similar conclusion.

The original Thorne article is *Automorphy lifting for residually reducible l-adic Galois representations*, JAMS 28 (2015), 785–870, DOI 10.1090/S0894-0347-2014-00812-2. The local copy read here is the 16 April 2014 author version, not an authenticated final journal PDF. The correction authenticates the defective final assertion it explicitly identifies; it does not authenticate every other sentence of the author version. The final AMS PDF request returned 403. Final-version comparison of the other imported Thorne results remains qualified.

Pan's local copy is the 3 September 2021 arXiv v2 author text. Its final JAMS comparison is still open. In that actual text the following branches are distinct.

* If xi_v is trivial, Lemma 4.2.10(1) requires componentwise O-flatness, dimension four, generic reducedness of each component's special fiber, and uniqueness of the characteristic-zero component above a special-fiber generic point. Pan cites Taylor 2008. The precise final finite-type supplier is **Taylor Lemma 3.2(1), pp. 197–199**, supplemented by Lemma 2.7, pp. 193–194, for completion. Pan's phrase identifying the first part of Proposition 3.1 is not the precise locator for the finite-type statement.
* If xi_v is nontrivial and the residual local representation is trivial, Pan cites Thorne Propositions 3.15 and 3.16. Here the applicable assertion is 3.15(2), for pairwise-distinct inertial characters, and 3.16. Section 4.1.1 of Pan, p. 38, makes xi_v a character of p-power order. At p=5 a nontrivial xi_v differs from its inverse. The corrected all-trivial-character clause 3.15(1) is not the premise used in this branch.
* If the residual local representation is nontrivial, Pan uses the explicit Shotton descriptions on p. 46. That branch is not justified here by Thorne's residual-trivial result and has not been independently re-audited in this packet.

At p. 47, Pan explicitly replaces the finite-type factors for trivial xi_v by their reductions before the tensor-product component argument. Thus the published correction does **not** on its own establish a failure of Pan's argument. Section 3 of PROOF.md explains exactly which information survives this replacement. It does not transfer generic reducedness of the original special fiber.

There is a separate source-to-use difference. Pan 4.2.10(2) asserts O-flatness of the actual nontrivial-character lifting ring. The read statement of Thorne 3.15(2) gives irreducibility, dimension, a characteristic-zero generic point, and generic-fiber smoothness; 3.16 gives a connectedness statement. Those statements alone do not imply O-flatness of an unreduced ring. PROOF.md Section 4 supplies a new, elementary two-dimensional matrix proof for the actual fixed-determinant ring. This authored proof needs independent review. It is not attributed to the published correction, and the source-only finding leaves the extra inference unproved.

## Connecting arguments proposed for review

PROOF.md distinguishes three maps that must not be conflated. The determinant comparison is a degree-two etale cover of the finite-type matrix scheme, and becomes an exact one-variable formal product at the specified residual point. Nilreduction is a nilpotent quotient with the same prime spectrum; it is not an equality of special-fiber scheme structures. Finally, the explicit rank-one determinantal calculation proves O-flatness of the nontrivial-xi ring itself, before nilreduction.

The determinant argument uses 2 invertible and the fixed determinant congruent to the residual determinant. These hold at p=5 by Pan 4.1.1. The proof keeps the same ordered matrix pair and changes only the scalar multiplying Frobenius. For the unordered pair of inertia eigencharacters {xi_v,xi_v^-1}, the reciprocal local reciprocity convention in Thorne's author statement merely interchanges the pair. No arbitrary change of inertial type is allowed.

## Related-use audit

The immediate downstream object is the completed localization of R_loc^{xi} at q_loc^{xi}, in Pan Proposition 4.2.4. The trivial-character factors enter its component statement through Lemma 4.2.7. The nontrivial-character factors enter geometric connectedness and normality, and the flatness and dimension assertions of the intermediate ring S_1. At the current project level, the retained Pan route is explicitly invoked at manuscript lines 830–863 and 7393–7409. The route has not been replaced by the separately proposed CEGGPS/Hu–Tan construction.

Other actual Thorne 2015 imports identified on Pan pp. 41–43 are Lemmas 1.3 and 1.5, for completed tensor products and completion/localization, and a comparison with Lemma 1.6 alongside Pan's own proof. This packet does not claim that the 2020 correction changes or independently proves those inputs. Thorne's 2016 residually dihedral paper is a different article and a different conditional route.

The bounded historical text search covered the existing pan-route-author Markdown/JSON and PAN-prefixed independent-source-review Markdown. It found no explicit Tho15/3.15/generic-reducedness treatment. Root's independent search likewise found no correction treatment in the checked protected proof text. This is a newly documented comparison; absence from those records is not evidence that the earlier mathematical theorem was false. HISTORICAL-SEARCH.json records the exact local search scope and output without claiming a whole-repository coverage audit.

## Limits and disposition requested

Independent review is requested separately for the source-only branch comparison, the determinant and nilpotent-quotient connections, and the new matrix flatness proof. Final Pan and final Thorne 2015 equivalence remain open. The published Taylor and Allen–Newton–Thorne texts are read at their exact pins. No whole modularity route, Shotton branch, completed-tensor-product foundation, or live inventory transport is accepted by this author packet. No manuscript or historical decision was modified. Third-party PDFs, extracted text, and page renderings stay in local-only; the candidate public mathematical content is REPORT.md, PROOF.md, CONTRACTS.json, and source/passage hashes without full source text.
