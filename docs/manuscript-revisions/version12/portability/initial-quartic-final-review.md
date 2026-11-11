# Independent final review of the 498-variable quartic application

Reviewer: `/root/astra_bl5_models`. Decision: accepted. Date: 2026-11-07.

This acceptance binds `docs/manuscript-revisions/version12/quartic-application.json`, SHA-256 `8f83001397a23206b3af3c394db0408ac91060f3eea83675b59f5e61fb05f38a`, to `manuscripts/quartic_v12.tex`, SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

I authored none of the construction, manuscript addition or application contract. I read the full added proof, its component arguments, the relevant original manuscript inputs, and the final contract. My detailed mathematical review is `composition-review.md`, SHA-256 `3e67873e47eb463444dcb8844d5d03ae6c4cd45f71728223c695983a6a625d90`. My complete manuscript integration review is `integration-review.md`, SHA-256 `f808482fd53e4dc0d274663935ba6a9f670d3628fd0d0b9a4fa5f9ec5929092e`. Both are in this evidence directory and form part of this final decision.

## Contract and exact artifact checks

I independently checked every pinned evidence file, the full manuscript hash, all three manuscript span hashes, and the complete-object compact-JSON hashes of the three mathematical edits. The author inventory retains all 25 applications and their 225 obligation fields. I read its mathematical obligations and compared them with the added proof. The inventory's historical status as awaiting review is preserved; this separately authored record supplies acceptance.

The first supplied contract had construction and application span hashes computed after line-ending normalization. I reported that mismatch and withheld acceptance. The author corrected and refroze the contract. In the accepted hash above, both spans and the consumer span match the raw manuscript using the checker's `decode().splitlines(keepends=True)` convention. No manuscript text or mathematical argument changed to resolve this metadata error.

The exact candidate is `candidate498-ir.json`, SHA-256 `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`. Its sparse polynomial is `polynomial498.json`, SHA-256 `817fec936dee3b358fc8b5b0b9a5570694adf009b134432467ef0be914aeedc4`. The ordinary coefficient lift is `polynomial514.json`, SHA-256 `d247a27709afda5f2be626390cffa1a175c3dfcbee1a5c832a1c457b32629bd5`. The actual inserted TeX equals the reviewed addition, SHA-256 `d229ea5c501fd2b61a281172dc8b038b49c2a8838abe6ae7afc92b766cdee800`, apart from surrounding whitespace.

## Acceptance of the nine obligations

1. **Source hypotheses.** The applications use the literal integral formal group and normalized logarithm at their stated primes and depths. Silverman's integral multiplication and logarithm results supply the exact properties used; the new truncation orders are checked from the manuscript recurrence and its tail estimate. The quaternion predicate includes both the quadratic-field embedding case and the split-algebra exception. The detailed review records the primary passages read. The exact source editions and existing errata qualifications remain those in the inventory.

2. **Constructed objects.** The selected chain is mixed orders 12/40, three normalized poles, five half-trace guards, the single-coefficient anchor, the shorter scalar norm tree, the scalar-only reciprocal chart, the mixed toric circuits retaining both outputs, squared-denominator cancellation and norm reuse. The alternative factored-pole and order-10 candidates are outside this decision. The proof correctly separates rational witness equivalences from arithmetic replacements that require separate completeness arguments.

3. **Index and domain coverage.** Soundness treats every rational solution of the final system. Completeness treats every integer input with one compatible sequence of choices. The root points and scales are fixed before the finite denominator exclusions and contact-prime selection. The same CRT output supplies the primary depth, alternate comparisons and half-trace guards. No presumed rational lift or generic-domain assumption replaces an actual witness construction.

4. **Transition maps.** Pole scalings have inverse rational maps on the proved nonzero pole domain. Half-trace guards restore the old field inverse in soundness. The reciprocal chart preserves the actual scalar difference; the toric equations determine both retained outputs successively. The cancellation identity uses proved nonzero constants and denominator. The reused norm square is `t^2-8u^2`, with `u` the product of coefficients. The exact finite checks account for every deleted coordinate's consumers.

5. **Identity of the consumed object.** There is no new analytic limit in this revision. The pertinent identity is between the proved arithmetic predicate, the pinned quadratic residual system, and its full sum-of-squares expansion. I reran the independent verifier chain through 505, 504, 501, 499 and 498 variables. It reconstructs the selected transformations and checks the final expansion. The unique coefficient-lift chain supplies the stated ordinary quartic. This obligation is accepted in that explicit sense, not omitted as inapplicable.

6. **Coefficient conventions.** The field basis is `(1,rho)` and unramified local valuations have `v(p)=1`. The parameter `C=3^(2^25)` is fixed. There are 498 total coordinates and 497 witnesses, or 514 total coordinates and 513 witnesses after the lift. The symbolic expansion has 24,669 monomials, content one and maximum absolute coefficient `16*3^(2^26)`. The ordinary expansion has 24,716 monomials, content one and maximum `3^2048+1005072314676622`, of bit length 3247. I also parsed the public ordinary text table and verified its 690,922-byte count. These agree with the theorem and abstract.

7. **Local conditions.** The scalar norm argument supplies a suitable formal place for `H` and coefficient valuation bounds for `z(R)`. It does not incorrectly infer that `R` itself is formal. The duplication formula makes `[2]R` formal when necessary, and the logarithm of `[h]([2]R)=[2s]H` yields the required order-32 divisibility. The primary/opposite valuations separately establish the five nonzero half-traces in completeness.

8. **Exceptional cases.** The positive reciprocal denominator cannot vanish. The guard excludes `S=P`. The other exceptional chart branch is the genuine point `R=-2P`; its explicitly computed anchor valuation excludes it before any large-index bound is used. Zero pole witnesses remain permitted. Inert-place conjugation, the zero ternary input, the split quadratic-algebra case and the nonzero inputs used by the toric circuit are covered. The proof does not assume an old private witness survives a changed arithmetic predicate.

9. **Downstream consumption.** The unchanged height theorem with exponent 19 receives scalar order 32, Lucas order 40 and input order 12. The displayed numerical margins suffice for both height contradictions. They force the Lucas equation and then `n=2X^2+3` integral, which forces the rational input `X` integral. The simultaneous completeness construction proves the converse. The actual consumers in the abstract, theorem and coefficient specifications match these conclusions.

## Scope retained

This is internal independent model review of the new composition and its exact manuscript integration. It is not a fresh independent proof of every inherited arithmetic input. The restricted converse, height theorem, point-group identification, prime-pattern theorem and other unchanged source dependencies retain the qualifications recorded in Version 11 and its source inventory. The Kato interface has a separate fresh rebind and acceptance in this directory. The nine historical Issue 2 dispositions are not upgraded to new whole-proof validation by this record.

Finite verifier and metadata results support exact algebra, counts and bindings. They do not establish the truth of the external theorems. My mathematical acceptance rests on the source-to-application and application-to-consumer comparisons described above and in the detailed review, within the stated inherited scope. No further correction to the accepted contract or bound manuscript is requested.
