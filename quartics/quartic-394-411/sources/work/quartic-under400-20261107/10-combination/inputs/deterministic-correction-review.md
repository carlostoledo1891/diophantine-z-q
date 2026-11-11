# Independent review of the deterministic correction

Reviewer: agent03. Author: agent06. I accept the frozen 444-to-442 component on its inherited arithmetic inputs. The change removes two coordinates by replacing the correction choice with c=r+4896 and consuming r*c directly. It is an arithmetic replacement, not a bijection to old witnesses satisfying c in {33,33033}.

## Bound artifacts and checks

The reviewed packet is ../06-product/scalar-redesign/deterministic442.

| Artifact | SHA-256 |
| --- | --- |
| Parent one-correction444/candidate444-ir.json | c2c60a1bed5c929eb633b654e76d401dc96fc0edd1f09eee44324740c4cde837 |
| candidate442-ir.json | e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86 |
| polynomial442.json | c65f1049d1af0ab5a438de3c7b73a34b6ac43cd822763adf41679102182f2bc3 |
| REPORT.md | 76b2181c4618d0a208910de652a21a64c89ecaff6c4609ad2fb98007a0e0c211 |
| MANIFEST.json | 2f5aff25a5dd761954e284858dcff95547686b5eb9f99b3360d5fe28f8a9636d |

All manifest pins matched. I read the frozen author argument and implementation, the predecessor correction and depth24 proofs, and the underlying scalar preparation, pole and continuity passages. The underlying manuscript remains quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9. In particular the arbitrary finite support and subsequent continuity argument are stated at lines 10520-10559, and the concrete scalar pole interface appears in the scalar section at lines 20222-20362.

My read-only check_deterministic_correction.py imports no author implementation. It independently derives the affine r from the old corrected-product equation, checks its square against coordinate600, proves the normalized pole-input identity, checks every unchanged row and coordinate and all deleted-coordinate incidences, and expands the complete sum of squares. It also cross-checks the local residue formulas. All checks passed: 442 total variables, 419 quadratic residuals, 6,666 quartic monomials, with the same fixed coefficient and degree. The receipt is deterministic-correction-checks.json.

## Soundness uses a restricted unit assertion

The input label remains beta=51(2X+1)^2+2504. Thus r is strictly positive and nonzero for every rational X. At a scalar contact prime p>76176 in M5(beta), the established contact calculation says eta=v_p(r) is odd. If beta is p-integral, each contact factor is integral. If beta is not p-integral, 51 is a unit and v_p(beta)=2v_p(2X+1); all five factors have that valuation, making eta even. Consequently the odd eta is positive, independently of c or the pole equation.

Now 4896=2^5*3^2*17 is a p-unit. Since r has positive valuation, c=r+4896 is a p-unit. The pole equation therefore has valuation eta+2v_p(W), exactly as required by the accepted depth24 argument. That argument proves M5(beta)^24 divides the scalar index, including both possible branches of the scalar point near O and near (0,0).

This reasoning does not assert that c is a unit at every prime above the fixed cutoff. Such an assertion would be false and is unnecessary. The only occurrence of this correction is in the scalar pole input, and its soundness proof needs the unit condition only on M5(beta). The other contact-detector pole modules do not consume this correction. Positivity of eta was proved first, so there is no circular use of the new unit assertion.

All later height and anchor bounds remain unchanged: h(beta)<=H*|s|^(19/24), h(beta)<|a|/40 and log(48H)<|a|/40. Hence the same order40 Lucas and order10 input arguments force n=beta. The already reviewed odd-label bridge for the coefficient51 then gives X in Z. No old finite-choice equation is used in these deductions.

## Local correction for every integer input

For integral X, the parent calculation gives v2(r)=2 with odd part 1 modulo8, v3(r)=1, and v17(r)=0 with square unit residue15. These properties are for every odd 2X+1, with no restriction on its residue at3.

At2, v2(4896/r)=3, so c/r=1+4896/r is a unit congruent to1 modulo8 and is a square in Q2. At3, v3(4896/r)=1, so c/r is a unit congruent to1 modulo3 and is a square in Q3. At17, v17(4896/r)=1, giving the same conclusion in Q17. Therefore cr=r^2*(c/r) is a square in all three fields. Also c and r are positive integers. These are the exact local and real hypotheses used by scalar completeness.

## Enlarged support and the global choice order

The support of c may contain new large primes. The source preparation proof permits arbitrary fixed finite support, not merely primes at most17: already the input contact product r can have arbitrary prime factors. Its proof uses the finite-index property of sufficiently deep local formal subgroups at every place in that support, then chooses a deeper scalar point. Nothing in that step relies on a bound for the correction or on its squarefreeness.

For a fixed integer X, both r and c are determined before any elliptic or contact-prime choice. Take the full finite support S of cr. At p dividing r, impose the depth24 coefficient bounds 8v_p(r) on f(H) and 24v_p(r) on the scalar ratio. At p dividing c but not r, impose positive coefficient valuations. The accepted scalar formulas then give W integral on S. Since q=Norm(f(H)) is nonzero and r>0, W is positive and nonzero. Thus crW^2 is positive, has nonnegative valuation on S and even valuation outside S, and has the three required local squareclasses. Its reduced denominator is a square. The original pole-completeness theorem supplies witnesses for this actual input.

The finite support is fixed before the continuity modulus L. Only after that modulus and the root scales have been fixed are the later contact primes selected. The source permits the resulting arbitrary finite odd support in L and exclusion of any additional finite set of primes. Hence new prime factors of c do not change the quantified domain of the prime-selection theorem or reverse the choice order. They are fully accounted for; they are not silently discarded as exceptional primes.

## Actual normalized scalar input

Let F denote old coordinate524, let V=coordinate525 be the retained normalized W-square, and let b0=coordinate526 be the retained normalized pole input. The old product row is

    c*s0-20619812*F=0,

and its old input row is

    (7895415*c+20619812*F)*V-20619812*b0=0.

The actual affine contact expression satisfies r=-4*(s0+7895415). Multiplying the first row by V, adding the second, and multiplying by -4 gives

    r*c*V+82479248*b0=0.

Coordinate600 is exactly r^2 by its retained definition. The replacement row is therefore

    (coordinate600+4896*r)*V+82479248*b0=0,

which has exactly the intended semantic input r(r+4896)W^2, including the old sign and rational normalization. The independent checker derives r from the old product row rather than trusting its name or copying it from the new row.

Only the old correction-choice and corrected-product rows are removed. Their coordinates65 and524 occur nowhere else except the old scalar-input row just replaced. Every other row, coordinate and parameter is unchanged. In particular the scalar powers, norm square, ratios, root labels, input equation and all other pole modules are untouched. The new row is quadratic because coordinate600 and the expression r are affine in retained coordinates.

This acceptance covers the frozen component above. It does not restore the removed finite-choice equation, and it does not accept a later combined artifact without checking the corresponding physical transport.
