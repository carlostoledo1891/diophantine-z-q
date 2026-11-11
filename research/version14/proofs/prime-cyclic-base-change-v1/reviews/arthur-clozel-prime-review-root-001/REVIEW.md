# Review of the prime-degree Arthur--Clozel substitution

Reviewer: `/root`, internal model review. Author: `/root/astra_quartic_opt05_anchor`.

Target: author manifest `fee2fcc6ad7ec745cc796a4b772ba379a4c7eebf5da392349cdb9a9ce0de64e7`, report `a1c9929d511ca357848d293bd041e0074662a61a2ef4694f3ccd8508ec24e02b`, and connections `823b56b9d82335d031c421b6e6810c2e440182297ff9c4e9075525502b073c21`.

Decision: accepted bounded published-source substitution and its four exact application cards. No mathematical repair requested. This accepts the prime-degree global inputs and the stated connecting argument, not the whole H theorem or current release.

## Review scope and source identity

Root reviewed the full report, all four application cards, all 36 comparisons and all seven identified sections of the prior H-D4 argument. Root independently read the actual source at Chapter III pp.199--207, 212--213, 217--218 and Chapter I pp.48--50, and visually inspected the copyright page and Theorem III.4.2. The pinned scan is a facsimile of the 1989 Princeton volume, Annals of Mathematics Studies 120, not merely an author preprint. Its copyright, ISBNs, title, contents and printed pagination establish which text was inspected.

Root previously reviewed the H-D4 connecting argument and therefore is not blind to it. Root did not author the new source substitution or its prime-degree no-self-twist addition. This review independently checks those applications, while preserving the scope of the earlier H-D4 and separate Hilbert-attachment reviews. No full trace-formula proof review is claimed.

## The actual prime-degree source

III.4.2 explicitly assumes a cyclic extension of prime degree and representations induced from unitary cuspidal representations. Cuspidal weight-two Hilbert representations, put in the unitary normalization, lie in that category. Part (a) requires absence of a self-twist by a generating norm character and returns a cuspidal lift. Part (d) requires invariance of the cuspidal representation above and returns a cuspidal descendant. These hypotheses differ, and the report supplies each before its use.

The weak-lift convention is exactly III.1.1: unramified Satake matrices are raised to the residue degree. If the arithmetic roots are alpha and beta, the unitary roots are obtained by dividing by the positive square root of the residue cardinality. Raising to the residue degree f and restoring the normalization multiplies by the square root of `q_v^f=q_w`; the resulting arithmetic roots are alpha^f and beta^f. Thus the Galois comparison is with restriction of the original representation, without a hidden dual or Tate twist.

## Ascent and the characteristic-zero self-twist test

The normal subgroup argument in H-D4 shows that restriction to every field in the solvable tower still has nonsolvable residual image. In dimension two, a reducible finite image over the algebraic closure is solvable. Saturating the intersection of a putative characteristic-zero invariant line with a stable lattice would give a residual invariant line. This verifies the actual absolute irreducibility required throughout the argument.

Suppose a self-twist by the prime-order norm character existed. Attachment and equality of the unramified polynomials give a characteristic-zero isomorphism `r = r tensor eta`. Equality of determinants implies eta squared is trivial, excluding every odd prime degree. In degree two, an intertwiner A has scalar square by Schur's lemma and can be scaled after finite coefficient extension to satisfy A squared equal to one. It cannot be scalar. Its two eigenspaces are therefore one-dimensional and stable on the kernel of eta. This contradicts the irreducibility already proved. This uses characteristic zero even when the coefficient prime is two.

Part III.4.2(a) now gives the required cuspidal lift. The real-place argument below supplies its weight, and the unramified comparison identifies its attached Galois representation with the restriction of the same r. The rank-two irreducible common semisimplification is already the whole rank-two representation, so no unnoticed extension or constituent remains.

## Split real places and the known error boundary

Theorem III.5.1 carries the same prime-degree hypotheses and upgrades weak to strong lifting. Only its split-real consequence is used here. Every real place splits in a totally real extension. The source's Chapter I pp.48--49 computes split transfer as convolution of component test functions. For a sigma-stable representation on the product of the split factors, identify its factors; the cyclic permutation intertwiner has twisted trace equal, up to its scalar normalization, to the trace of their product. The prime-degree global identity in III.5.1 then equates this character with the downstairs character. Taking the other convolution factors to an approximate identity, or restricting first to finite-rank admissible test operators, identifies the two irreducible characters and hence their representations. This gives equality of the weight-two real components with no absolute-value twist.

This direct split-place computation matters for the dependency boundary. The full printed treatment also uses non-split local character theory. The present application does not import that full local theorem or its backward references to later arbitrary-degree results. The local Lemma I.6.3 mentioned in III.5.1 and the defective global Lemma III.6.3 are different statements. Neither a claim that their numbers agree nor a general assertion that all of Chapter I is independent would justify the application. The direct convolution argument supplies the needed split case using the prime trace identity.

The author's central-character argument then applies: the unitary weight-two character is trivial on positive real factors and is trivial on an open finite conductor subgroup. A ray class quotient, allowing real sign conditions, is finite. This puts the descendant in the finite-central-character domain of the separately retained Hilbert attachment theorem. The exact finite ray-group source is Kopp--Lagarias, Essential Number Theory 4 (2025), Theorem 6.9, pp.44--45, with Definitions 5.2--5.4, p.33. Root read and visually checked the final publisher text in the separate TW source review. It includes arbitrary real-place sign conditions. Here take the modulus given by the open finite conductor and allow every real sign: triviality on connected positive factors is essential. The resulting finite ray-class quotient shows that this actual central character, rather than an arbitrary unitary character, has finite image.

## Descent and the same representation at every step

Because r exists downstairs, conjugation by a lift of a generator gives an isomorphism of its restriction upstairs. The attached form and its conjugate consequently have equal unramified Hecke classes outside a finite set of all primes, not merely at primes split over the downstairs field. III.(2.4), with both Levi groups equal to GL2, gives the required invariance. Part III.4.2(d) therefore applies.

Let R be the representation attached to a chosen descendant. After identifying the absolutely irreducible restrictions of R and r, the matrix `R(g) r(g)^(-1)` commutes with the common restriction. Schur's lemma makes it scalar; the representation laws make the scalars a character trivial upstairs. This character has finite order dividing the prime degree. Twisting the form by its inverse, using the report's arithmetic reciprocity convention, gives precisely r downstairs. The correcting character is trivial at every real decomposition group, so the weight is preserved.

At the next step, invariance is re-established from the original r. It is not inferred for an arbitrary descendant from the invariance of its base change. This is exactly the assertion missing from the unchecked iteration in the printed composite-degree Lemma III.6.3.

## Correction history and related uses

Root read both the printed composite-degree argument on pp.217--218 and Clozel's public seminar notice identifying the error. The selected prime-degree theorem proof on pp.203--207 instead uses the prime-degree trace identity, lower-rank prime-degree induction and the Rankin--Selberg facts in III.2. It does not invoke III.6.3. The present proof uses a tower of prime steps with separately verified invariance; it neither adopts the defective arbitrary-degree lemma nor requires the later Clozel--Rajan repair.

The seven exact H-D4 sections in the consumer map cover the selected source declarations, normalizations, irreducibility, ascent, descent, local-scope warning and historical qualification. The restriction to these sections is justified because this substitution concerns the global automorphic input. H-D4's warning about arbitrary ramified local comparison remains valid. The separately reviewed modular local-base-change bridge supplies that different input, and is not a consequence asserted for this AC packet.

## Retained inputs and limits

The published prime-degree trace-formula and strong-multiplicity-one results remain theorem inputs. So do the separately identified Hilbert Galois attachment, class field theory, Chebotarev and Brauer--Nesbitt results. This review does not prove them from first principles, authenticate the uninspected 1980 Langlands edition, establish general composite-degree descent, or approve the whole H argument.

When this accepted substitution is adopted, the original-edition Langlands comparison is no longer necessary for these selected global applications. Its historical unresolved status should remain visible. Current manuscript integration and its affected dependency records need their own exact binding; this report alone changes neither.
