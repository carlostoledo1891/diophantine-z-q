# Published-source comparisons for Version 14

Author: /root. Status: authored evidence, awaiting independent acceptance.

The reviewed manuscript is `manuscripts/quartic_v14.tex`, SHA-256 `b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d`. No release manuscript was changed. The proposed edits are separately bound to that source. This report closes neither the other source qualifications nor whole-proof review.

## Kolyvagin

The final article is V. A. Kolyvagin, *On the Mordell-Weil Group and the Shafarevich-Tate Group of Modular Elliptic Curves*, Proceedings of the International Congress of Mathematicians, Kyoto 1990, Mathematical Society of Japan, 1991, volume I, pp. 429–436. The International Mathematical Union supplies a scan of the published volume at <https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1990.1/ICM1990.1.ocr.pdf>. The volume is 85,534,904 bytes, SHA-256 `a86ae342133e8f051752bfd26009c38b9c755e8469c46235cef2d35e8c68f75d`. The article occupies PDF pages 517–524. Its first page carries the proceedings imprint and 1991 Mathematical Society of Japan copyright.

The inherited source is MPI/90-69, 380,826 bytes, SHA-256 `bacdf23d05d5120defe923c8dcccd7c5bc525fe7b32239552b04fd6567726f2f`. Its printed pp. 4–5 are PDF pages 6–7. This comparison concerns that article, not the different Festschrift chapter *Euler systems*.

I read the published theorem statements and surrounding conventions on pp. 429–431, compared them with the inherited source, and visually checked published pp. 430–431 because the OCR incorrectly reads some non-strict inequalities as strict. Published Theorem 1 on p. 430 has the hypothesis analytic rank at most one, and concludes equality of algebraic and analytic ranks and finiteness of the entire Shafarevich–Tate group. It includes analytic rank one, not just rank zero.

The source's ambient curve is an elliptic curve over Q. The paragraph preceding Theorem 1 assumes a modular parametrization from X_0(N), where N is the conductor. Its analytic rank is the order of the usual elliptic-curve L-function at s=1. Its group III is defined on p. 429 by the kernel of localization at all places. Those are the manuscript's objects. Modularity is a separate input from BCDT; its final-version qualification is not discharged here.

On published p. 431, Theorem 2 adds a nontorsion Heegner point over an imaginary quadratic field; Theorems 3 and 4 supply that condition when the analytic rank over Q is at most one; Theorem 5 gives rank one and finite III over the auxiliary field. These statements and their directions agree with the inherited pp. 4–5. The restrictions on the fundamental discriminant, its square residue modulo 4N, the exclusions -3 and -4, and the coprimality in Theorems 3 and 4 remain explicit. The descent paragraph bounds the restriction kernel by III(Q)[2]. Neither source asserts an identification of the full groups over the two fields.

Current uses are the forward-rank lemma at lines 1171–1193 and the dependency table at line 12214, inventoried as A020 and A082. The manuscript uses Theorem 1 directly, with the auxiliary chain as explanation. Its subsequent 2-primary Kummer corank computation consumes finiteness of the entire III and introduces no additional hypothesis on residual representations or the prime 2. The proposed edit changes the theorem locator and bibliography to the final article. It leaves the statement and argument unchanged. The author-level result is that this published theorem supplies the exact required forward implication. Independent acceptance is still required.

## The local-character input

Conrad's 2011 preprint is not claimed to have a final published version here. Its Appendix B, p. 32, explicitly refers the local-algebraicity implication to Tate's theorem in Serre's book. The refinement involving arbitrary local fields and detailed individual Hodge–Tate weights in the rest of that appendix is unnecessary for the manuscript's base field Q_5.

An accessible scan of the published 1989 Addison-Wesley edition of J.-P. Serre, *Abelian l-adic representations and elliptic curves*, is supplied for a McGill course at <https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf>. It is 5,563,667 bytes, SHA-256 `971dbfdd4414d99ea21d7d0af63dbb790d7b1188e9aec37f422181a2b543dec4`. The title and copyright pages identify the edition as the 1989 reprint of the 1968 book. This is not an asserted byte-equivalence with Conrad's cited 1998 edition.

The exact published supplier is Chapter III, section 1.2, p. III-7, repeated with proof in Appendix A.7, Theorem 3, pp. III-52–53. These are PDF pages 99 and 144–145. It characterizes local algebraicity of an abelian p-adic representation of a finite extension of Q_p by the Hodge–Tate condition together with semisimplicity on inertia. Chapter III, section 1.1, pp. III-1–4, defines local algebraicity and fixes the inverse in the reciprocity convention. I read these passages and visually checked the theorem on p. III-52. The theorem does not assert that all Hodge–Tate representations are locally algebraic without the abelian and semisimplicity conditions.

Here is the complete application needed at current manuscript lines 832–848, A011. Let E/Q_5 be a finite coefficient field containing the twisting character's values. The character is a one-dimensional E-representation, and the manuscript has already obtained its de Rham property as a subrepresentation of the relevant Hom representation. Hence its underlying Q_5-representation is Hodge–Tate. This last implication remains part of the manuscript's separately inventoried p-adic Hodge theory input.

After scalar extension to an algebraic closure of Q_5, multiplication by elements of E diagonalizes simultaneously under the embeddings of E. Thus the representation, including its restriction to inertia, is semisimple. It is abelian because it is a character. Tate's theorem therefore applies to the underlying Q_5-representation over the local base field Q_5.

Its algebraic map from G_m to GL_Q5(E) commutes with multiplication by E. Indeed it does so on a nonempty open subgroup of Q_5^*, and that subgroup is Zariski dense. The centralizer is Res_{E/Q5} G_m. By the defining adjunction of Weil restriction, every Q_5-map G_m to Res_{E/Q5} G_m comes from a character of G_m over E, hence an integral power. In Serre's reciprocity convention the map is evaluated at the inverse of a local unit; the cyclotomic character has the same inverse on units. Consequently the original character agrees on an open inertia subgroup with an integral cyclotomic power. This argument does not assume E=Q_5, nor an arbitrary equality between individual labeled weights.

Remove that power. The remaining character has finite inertia at 5. At every other finite prime, the pro-l subgroup of local units has finite image in E^*, since an open subgroup of E^* is pro-5. Only finitely many primes ramify by the existing hypothesis. Global class field theory over Q now factors the character through a finite ray-class group, with the real place included if necessary. It has finite image. This is the finite-character-times-cyclotomic-power conclusion consumed by the next paragraph. Comparing the two weight multisets proceeds as in the existing manuscript and is not a new assertion of this report.

The proposed edit inserts the inertia-semisimplicity justification, replaces the Conrad proof citation by this published Tate theorem, and supplies a bibliography entry for the edition actually inspected. Conrad's old source remains historical evidence. This is a proposed change of supplier and therefore requires fresh independent acceptance even though the resulting local-algebraicity assertion is the same.

## Lauter–Naehrig–Yang remains open

The current pin is an article-in-press proof with placeholder volume, pages and availability date. The publisher identifies the final article as Journal of Number Theory 161 (April 2016), pp. 146–174, DOI 10.1016/j.jnt.2015.02.020. This differs from the manuscript's shorthand publication year 2015. The current required use is section 2.2's coordinate normalization at manuscript lines 992–994, A017. Neither the title of the file `2015-LNYFinal-JNT.pdf` nor matching metadata proves that those formulas survived unchanged. The publisher page was located; full final formula text has not been retrieved. No final-equivalence conclusion is made.

## Jetchev–Kane remains open

The publisher identifies the final article as Mathematische Annalen 350 (2011), pp. 501–532, DOI 10.1007/s00208-010-0568-5. The direct PDF request redirected to an access page. The publicly linked HKU repository PDF is visibly arXiv:0908.3905v1 and has 23 pages; the repository's label `postprint` does not override the file itself. The author's publication list also links to that arXiv record. These are not a comparison with the final 32-page published article.

The required use is the geometric and adelic description at current manuscript lines 13998–14005, A052, especially cyclic levels including powers of 2. The record remains open. The publisher displayed a US$39.95 single-article price, but no purchase was made or authorized in this report. No access control was bypassed.

## Handling of source files and acceptance

Full PDFs, page images and text extractions are local audit material. They are excluded from the proposed public handoff. Authored analysis, source identities, stable URLs, exact locators and review records may be included. The two proposed source changes are ready for independent review; the two unavailable final texts remain unresolved. The complete inventory and other agents' source qualifications remain separate obligations.
