# Five comparison guards give a 518-variable candidate

Status: explicit candidate, finite algebraic checks passed, independent arithmetic acceptance pending. No repository file was changed. The conclusion inherits the arithmetic dependencies and qualifications of the current 523-variable construction. This report does not independently validate those dependencies.

The candidate has 518 total rational coordinates, including the input, and 487 quadratic residuals. Clearing each residual's rational coefficient denominators and taking the sum of squares gives an integer quartic with 35,090 monomials. Its fixed coefficient parameter remains `S = 3^(2^26)`. The complete symbolic coefficient table is `quartic-518-symbolic.json`. No enormous decimal integer was expanded.

## Exact change

For each `V0,...,V4`, write the existing difference denominator as

    d_i = x(U_i) - x(Q_i) = A_i + B_i sqrt(2),

where `U_0 = H`, `Q_0 = P`, and the other four `Q_i` are the fixed root points. The current guard introduces `a_i,b_i` and imposes

    A_i a_i + 2 B_i b_i = 1,
    B_i a_i + A_i b_i = 0.

These two variables occur only in these two guard equations. Replace them with one rational coordinate `c_i` and the single equation

    A_i c_i = 1.

Every `A_i` is an affine expression in retained coordinates. The new residual is quadratic. The slope, difference abscissa and ordinate, local parameters, logarithms, odd-index equations, detector poles, scalar block, and height scales are untouched. In particular, no zero values of the pole witnesses are excluded by this change.

The source residuals have individually cleared coefficients and signs. The implementation deletes the terms containing `b_i` from the first old row and deletes the second row. Thus it retains the exact nonzero scalar multiple of the displayed new equation without relying on guessed normalization.

The removed coordinate IDs are `101,109,117,125,133`. The removed residual IDs are `53,61,69,77,85`. The first coordinates `100,108,116,124,132` are repurposed as the new rational inverses. The separate `scalar.shiftedS.dxInverse` guard is unchanged.

## Soundness and rational witness map

A new solution has `A_i != 0`, hence `d_i != 0`. Since 2 is not a rational square, `N_i = A_i^2 - 2 B_i^2` is nonzero whenever `d_i != 0`. Set

    a_i = A_i/N_i,  b_i = -B_i/N_i.

These rational values satisfy the two old equations. None of the downstream equations contains `a_i,b_i`, so replacing the five new inverses with these ten values gives an old 523-variable solution with exactly the same input and all the same other coordinates. The inherited 523-variable soundness theorem therefore applies.

This is a strengthening of five guards, not an equivalence on every old intermediate assignment. Old solutions with `A_i = 0` are deliberately not retained. The next argument proves that every integer input still has a solution, which is the required exact rational projection.

## Completeness

Fix an integer input and perform the existing Version 9 completeness construction. The four root points, scalar data, scales and continuity modulus are chosen before the contact primes. Add to the finite prime cutoff all rational primes below which one of `P,Q_1,...,Q_4` has a nonintegral abscissa. This is a finite set of fixed data, so taking all contact primes above its maximum uses the existing arbitrary lower-bound freedom. It changes neither the prescribed ray classes nor the later CRT argument.

Select any one contact prime `p`. The existing two-reduction lemma says that it splits in `K = Q(sqrt(2))`. Write its places as `v` and `bar(v)`, with `v` the primary place. The existing completeness congruences give:

* `U_i` is a nonidentity formal point at `v`, so `v(x(U_i)) < 0`. The asymmetric-depth version gives even more depth than needed here.
* `U_i` reduces to `Q_i` at `bar(v)`, because `h = 1` modulo the opposite doubling-image order, and both points are multiples of the globally doubled point `P`.
* The fixed `Q_i` has integral abscissa at both places by the enlarged cutoff. Its reduction is finite. Consequently `x(U_i)` is integral at `bar(v)` as well.

It follows for every `i = 0,...,4` that

    v(d_i) < 0,  bar(v)(d_i) >= 0.

Conjugation exchanges the two places. Therefore

    v(conj(d_i)) = bar(v)(d_i) >= 0.

The summands of `d_i + conj(d_i)` have unequal valuations, so their sum is nonzero. Since `2 A_i = d_i + conj(d_i)`, we have `A_i != 0`. Set `c_i = 1/A_i`. The old completeness witnesses then satisfy every new residual.

This argument works simultaneously for all five differences at the same selected prime. It does not need `n_i` to be a unit modulo `p`, does not impose an additional local condition on a pole witness, and does not use real approximation. The positivity and nonzero indices already supplied by completeness ensure that each `U_i` is a nonidentity global point. No claim is made that the same argument applies to the scalar difference `S-P`, so its guard was retained.

Together with soundness, the new quartic has precisely the same rational input projection as the old one. Subject to independent acceptance of this changed application and the inherited source theorem, that projection is `Z`.

## Source contract for independent review

1. **Source version.** `manuscripts/quartic_v11.tex`, SHA-256 `1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`. The 523-variable residual source is `quartics/quartic-523-540/final523_540/symbolic523/candidate-ir.json`, SHA-256 `48a8b8f9263a97d3a1c59f3f0f3553eae628b7aba342d44003e8da840ae84928`.
2. **Required input.** The two-reduction lemma `lem:v5-two-reductions`, near line 11138, supplies split places and their oriented reduced group orders. The construction `subsec:v9-deep-completeness`, near line 19712, supplies the primary and opposite CRT congruences. These source passages are read as mathematical arguments, not as status labels.
3. **Constructed input.** `U_0=[h]P`, `Q_0=P`, `U_i=[hn_i]P`, and `Q_i=[n_i]P` over the same `K`. All five are covered, including index zero in the comparison list. The root indices are fixed before selecting primes, as in `subsec:v9-completeness`, near line 19629.
4. **Domain coverage.** Completeness requires a witness for every integer input, not every old intermediate point assignment. The old constructor provides roots for every integer input, and the finite enlarged cutoff is available after those roots are fixed. Soundness covers every rational solution of the new equations by the explicit inverse map above.
5. **Maps and conventions.** Conjugation is the nontrivial automorphism of `Q(sqrt(2))`; it exchanges the two split places. `v(conj(d))=bar(v)(d)` holds with the same unramified normalization. The rational coefficient is the half-trace `A=(d+conj(d))/2`.
6. **Group-to-coordinate step.** The root has integral coordinates at the chosen good prime, hence finite reduction. Equality of opposite reductions therefore forces the moving point to have finite reduction and integral abscissa there. Primary formal reduction gives a negative abscissa valuation. This is exactly the identity-versus-finite distinction used in the existing local-parameter argument.
7. **Object consumed downstream.** The retained `d_i` is exactly the denominator of the unchanged subtraction slope. The inverse coordinates have no other consumers. The new guard proves that same denominator nonzero; it does not replace the slope or choose a different point.
8. **Exceptions.** Trace-zero old denominators are excluded, but the displayed unequal-valuation argument rules them out for the completeness witnesses. The scalar difference, all quotient guards outside these five, and all permitted zero pole witnesses remain unchanged. Contact primes are odd and split. No assertion for inert primes is needed in completeness.
9. **Affected claims and acceptance.** The changed application is the completeness realization of five subtraction-domain guards and the resulting variable count. The inherited arithmetic theorems remain dependencies, not newly verified results. The repository's `AGENTS.md` and `docs/audit-history/PROTOCOL.md` require someone other than the author to accept the changed route. No acceptance record has been authored here.

## Finite checks

Run `node build-candidate.cjs`, then `node verify-candidate.cjs` in this directory. The checker uses the pinned source independently of the candidate builder. It verifies the original field-inverse equations up to their actual rational row factors, verifies that all ten inverse coordinates have no other consumers, checks every unmodified row, checks that all retained variables occur, and expands the denominator-cleared sum of squares exactly using small BigInts and formal powers of `S`.

The verified counts are 518 coordinates, 517 witnesses, 487 residuals, residual degree at most 2, quartic degree exactly 4, and 35,090 distinct variable monomials. The output has at most `S^2`. The structural checker does not prove the split-place completeness argument. `verification.json` explicitly records independent arithmetic acceptance as pending.

## Other chart routes examined

The existing point module `x=h^2`, `j^2=x^2-D` uses three field coordinates and already omits the ordinate `hj`. Substituting away `x` raises the curve residual to degree four, which would make a direct sum of squares degree eight. Substituting away `j` through the odd chart has the same problem. Parametrizing the parity conic introduces products needed again by the curve and its consumers, so no certified net reduction was obtained that way.

Reciprocal point coordinates can reduce the apparent cost of `f` and `z`, but require new quadratic intermediates and nonzero conditions when the difference formulas and fixed height product are reconstructed. No claim of a lower bound on chart size is made. Those attempts were not accepted as candidates. The five guard replacements above are the only changes in the delivered 518-variable candidate.
