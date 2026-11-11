# Voight chapter 14: independent final-source comparison

Reviewer: `/root`. Author: `/root/astra_v14_baseline_compiler`. This is a model review. I did not author the source comparison, application cards or proposed edits. I read the source pages and the actual manuscript passages; earlier packet reports provided locations, not the mathematical justification below.

I accept the three bounded source applications and two citation edits in `voight-final-ch14-compiler-001` against manuscript `301e051afc8690d51a1fe6a6f8e0db3bb646d9a6deb7971400f6838691abbba5`. The exact inputs, edit replay and resulting candidate are bound in CHECKS.json. This accepts the replacement of the corrected online locators with the final published chapter. It does not accept the whole manuscript or independently reprove the neighboring arithmetic arguments.

## Sources and conventions

I visually read final printed pages 231–232 and corrected online pages 223–224. The statements of Main Theorem 14.6.1 and Proposition 14.6.7, together with the split quadratic algebra extension in 14.6.8, agree in the respects used here. I read the final chapter title/copyright and Definition 14.5.1 on page 230 from their extracted text. The final chapter is the 2021 Springer publication, not the older file whose PDF extension concealed an HTML response.

The source base field F is Q in these applications. Its quadratic extension K is the manuscript's quadratic field denoted F in the embedding application. Ramification means that the completed quaternion algebra is a division algebra; the ramification set includes the real place. The ideal discriminant alone does not encode infinity. A quadratic extension need not be unramified at a ramified place of the quaternion algebra: the criterion requires that the quadratic algebra there be a field.

I read the errata title/date and visually checked pages 3 and 13, which contain the chapter 14 corrections. They correct the proof of 14.3.4, the proof of 14.7.5, and Example 14.2.13. They do not change the selected statements or the displayed proof of 14.6.7. A full-text search of the pinned errata is also recorded. This is a bounded comparison with that public errata document, not a claim that every theorem or ancestor in the book has been reverified.

## Actual source-to-consumer connections

At manuscript lines 14343–14347, the required assertion is the existence of a quaternion Q-algebra ramified at the prescribed finite prime ell_0 and infinity. These are two distinct noncomplex places, giving a finite even set. Main Theorem 14.6.1 therefore gives exactly the required algebra, up to Q-isomorphism. The subsequent Eichler order and enhanced supersingular curve assertions have separate suppliers; this theorem does not establish them.

At lines 15050–15055, the supplied local hypotheses say that the actual quadratic field Q(sqrt(D h_*)) remains a field at ell_0 and infinity, the two ramified places of B. In characteristic zero the quadratic field is separable. These are condition (v) of Proposition 14.6.7, which implies the rational algebra embedding in condition (iii). This is the same B as in the construction. Choosing optimal integral embeddings, their orientations and the adelic representative z_0 is a subsequent argument; none of those stronger assertions is attributed to this field-embedding criterion.

At lines 20595–20616, the scalar test uses B=(2,3) and the nonzero rational radicand a=1-2/(3t^2) for t nonzero. Nonzero follows because 2/3 is not a rational square. If a is not a global square, Q(sqrt(a)) is a separable quadratic field and Proposition 14.6.7 applies to the nonsplitting conditions at 2 and 3. If a is a global square, the relevant quadratic algebra is Q times Q, rather than a quadratic field. The adjacent 14.6.8 explicitly supplies the same embedding equivalences for that algebra; it cannot embed into a quaternion algebra ramified at 2 and 3. Thus the source has precisely the field/split-algebra distinction required by this application. The zero input is handled separately by the manuscript's explicit witnesses. The existing local square tests, norm-form rewriting and preceding polynomial lemma remain separate reviewed arguments; this final-version substitution does not newly certify their complete chain.

No limit, uniformity or change of base field is introduced by these two citation edits. The unchanged neighboring proof text retains its prior dependencies. The edits update one proposition page reference and the chapter bibliography, and preserve the separate chapter 43 bibliography.

## Decision

The published hypotheses, objects, embedding direction and ramification convention match the bounded application cards. Accept the exact source substitution and edit replay. Current ordinary inventory adoption, transport into a later combined candidate, all other Voight applications, whole-proof coverage and release approval remain outside this decision. Source PDFs and rendered pages remain local-only.
