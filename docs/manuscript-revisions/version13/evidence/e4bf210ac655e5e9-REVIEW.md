# Independent review of the frozen 470-variable lineage

Reviewer: `/root/astra_bl5_models`. Decision: accepted as a research candidate, with the inherited arithmetic hypotheses unchanged. This is not a release approval and does not meet the requested fewer-than-400 threshold.

I authored neither the candidate nor its transformations. I read the actual hybrid producer, semantic checker, elimination verifier and certificate operations, and used agent 10's review only as a guide. I reran the exact 498-to-486 transport, the hybrid semantic verification, and the final nine-step elimination and full coefficient expansion. My wrapper suppresses every attempted source-file write, compares generated artifacts with the frozen artifacts, and writes only in this review directory. `replay.py`, `replay.log`, and `replay-result.json` record the check.

## Frozen lineage

| Artifact | SHA-256 |
| --- | --- |
| released498 input | `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a` |
| combined486 / triple-cubic baseline486 | `55043867418ca00c68add72560b11055c71d082747d6bea61522168885875787` |
| candidate479 | `e8aea4b56037c0be0a8e9906e377bceea8c7bebd8fc3bf3314366032cfeae1f7` |
| candidate470 | `eff9369864da6bd2ed46fa300f51f5a0cc9217d3b790380713644ee31f512b72` |
| elimination470 certificate | `561d709106bc7e580b8ee237645204b4aeb038ea5ffa4cffb678c9ba247a4744` |
| polynomial470 | `80a23d972ee8bc4d04a2cb002b480395cada31b6580ee2bb765df52f9e7bf74c` |

The semantic reference is the released depth519 IR, hash `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`. Its historical order12 names are explicitly translated to the order10 source names. This is a naming translation for the retained test values, not a claim that order12 weights survive the order10 change.

## 498 to 486: inherited review and current transport

My complete prior mathematical review is `../10-combination/reviews/bl5/REVIEW.md`, hash `5958f35b2fba747c91d6afdf33d4c61567b40357aae9379113968b6f3cee3153`. I reread it for this composition. Its accepted chain is the order10 arithmetic/toric replacement, four factored poles, scalar reciprocal elimination, scalar preparation conic, and forward scalar powers. The current replay verifies all source/target/review pins and exact patch application to the accumulated system, including renamed-coordinate meanings and every modified consumer.

The distinctions in that mathematical proof remain necessary. Factored-pole completeness uses positive semantic pole inputs, including the scalar sign normalization; it is not an unrestricted bijection on arbitrary old pole tuples. The preparation conic has a separate `U=-B` reverse branch preserving the externally consumed square. Reciprocal reconstruction divides only by the proved nonzero chart denominator. The contact polynomial is nonzero for every rational input, so replacing inverse powers by forward powers preserves the scalar node. The order10 change needs the revised source-level height argument and recomputed detector witnesses. The present hybrid and elimination changes do not weaken or bypass these obligations.

## 486 to 479: products and all consumers

Each order output is a product of `1+q*Y_i` over the same retained squared field tests in `Q(sqrt(2))`. Multiplication is implemented componentwise as `(a0*b0+2*a1*b1, a0*b1+a1*b0)`. The order1 grouping is `[V0,U1,U2]`, `[V1,U3,U4]`, `[V2,V3,V4]`, with permutation `[4,0,1,5,2,3,6,7,8]`; the other groups are the order10 pair and the order40 pair/triple.

The checker does more than compare labels or sample values. It solves both old and new private circuits by nonzero constant pivots. Retained powers are replaced by their actual powers of `q`, and their defining equations are checked as well. Each of the nine old outputs and nine new outputs expands to its full common product. It then treats those nine established outputs as independent inputs and verifies each final `W` multiplication network. The replay checked 119 old circuit rows and 94 new circuit rows.

The six old stored `W` coordinates are affine-normalized values rather than literal components. For each one, the checker obtains its nonzero constant coefficient `a` and reconstructs the old coordinate as `(newW-rest)/a`. It substitutes these maps into every retained outside row, checks equality with the actual new row, and verifies that no deleted private coordinate remains. It also checks the complete row-set difference and coordinate-set difference. Thus no norm, inverse, pole, or height consumer is silently left in the old normalization.

Both rational projections follow. Starting with an old solution, keep shared values, reconstruct the new private circuit by its polynomial assignments, and set literal `W` to the proved product. Starting with a new solution, reconstruct the old private circuit and inverse affine `W` coordinates. The full retained-row identities give the outside equations in each direction. All divisions in this stage are by fixed nonzero rational constants. Zero factors, zero intermediate products and repeated factors require no extra branch. Both maps fix the input.

## 479 to 470: nine exact eliminations

The first six eliminations remove the two components of a private pair product from each order1 triple. Conceptually, for a triple `a,b,c`, the stored relations are `d=bc`, `e2=a(b+c)+d`, `e3=ad`. Substitution gives `e3=a*e2-a^2*(b+c)`. The available logarithm rows express the required squared field value in retained variables; the component certificate includes all affine normalizations and correction terms, so the result is still quadratic.

Concretely, the removed coordinate pairs are `(619,618)`, `(613,612)`, and `(607,606)`. Their first steps use retained rows `150/151/581`, `144/145/575`, and `132/133/569`, respectively; their second steps need no correction rows. The operation list in `replay-result.json` records all consumers, including the intermediate coefficient-definition rows, rather than only the final cubic coefficient.

The last three removals are coordinates `460`, `412`, and `364`, the retained `q1^5` values. Their pivots define them as the product of the retained `q1^2` and `q1^3`. Each has one remaining consumer, respectively rows `557`, `551`, and `545`. Direct substitution remains quadratic.

For every step I checked the verifier's mathematical invariant: the pivot coefficient of the eliminated variable is a nonzero rational constant; the replacement contains no eliminated variable; the changed-row list equals the full affected-row set minus the pivot; and each new row is the old substituted row plus explicit polynomial multiples of unchanged retained rows. Those multipliers contain no eliminated variable. Hence forgetting the variable maps old solutions to new ones, and inserting the pivot replacement recovers every old equation. The argument works in reverse step order and has no exceptional denominator or open-domain restriction. Final coordinate and residual dictionaries agree exactly with the published candidate.

## Quartic and statistics

The final candidate has 470 total rational variables, including the unchanged input, hence 469 witnesses. It has 439 residuals of degree at most two. Primitive integer normalization followed by the full sum of their squares gives degree four and 6,646 distinct coordinate monomials. The regenerated polynomial agrees with the frozen table, not merely its reported count.

The fixed coefficient parameter remains `C=3^(2^25)` and is not a quantified coordinate. The only `C^2` term is `16*C^2*x_57^2`, and that monomial has no lower-C contribution. All ordinary coefficients have bit length below 2048, and all linear-C coefficients have absolute value at most 48. Therefore every other specialized coefficient is smaller in absolute value than `16*C^2=16*3^(2^26)`. I separately checked a monomial with coefficient exactly 1 and no other C power, namely `x_1^4`, so primitive content 1 also holds after specializing C. No enormous decimal expansion is needed for these comparisons.

Over the rationals a sum of integer-residual squares vanishes exactly when each residual vanishes. The two new stages preserve the rational input projection in both directions. Combined with the separately reviewed 498-to-486 arithmetic construction, this establishes the claimed 470-variable research presentation with precisely the inherited arithmetic qualifications.

No defect was found in these frozen artifacts. Acceptance does not extend to later rational-log, complete-chart, reciprocal-V0 or other optimization candidates until their actual composition and source obligations are reviewed.
