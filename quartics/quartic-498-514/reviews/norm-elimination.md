# Independent acceptance of the final norm-coordinate elimination

I accept the norm-coordinate elimination authored in `01-elimination/sub500/from501/RESULT.md`, as transported to the exact final mixed-order-12 construction in `10-combination/candidate498-ir.json`. I did not author this elimination. The change is an unconditional polynomial identity over Q with an explicit unique inverse; it requires no new arithmetic hypothesis.

This review concerns the final 498-variable file with SHA-256 `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`. It does not concern the separate order-10 candidate in `07-toric/further` and does not accept the other mathematical components of the final construction.

## Exact source and target

| File | SHA-256 |
| --- | --- |
| `10-combination/candidate499-ir.json` | `8be28d88a5c37567a965288d39e11d69267ae309e5a7e61526311983f3ee17fc` |
| `10-combination/candidate498-ir.json` | `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a` |
| `10-combination/certificate498.json` | `217c34f9fbfc521090cf41d3522e3253be52b939ce4a30269ba8e9cd7e434704` |
| `10-combination/polynomial498.json` | `817fec936dee3b358fc8b5b0b9a5570694adf009b134432467ef0be914aeedc4` |

I read the actual proposal, the exact source and target residuals, the transported certificate, and `10-combination/verify498.py`. The earlier 501-to-500 result alone was not used to approve this later transport.

## Coordinate meanings and retained identities

The source has the following literal coordinates:

| Symbol | ID | Name |
| --- | ---: | --- |
| a | 140 | `U0.f.0` |
| b | 141 | `U0.f.1` |
| t | 311 | `testSquare.40.0.0.quadratic` |
| u | 312 | `testSquare.40.0.1.quadratic` |
| q | 535 | `reduced_scalar.norm_fH` |

The actual rows are

    row 263: a^2+2b^2-t=0,
    row 264: ab-u=0,
    row 505: q-a^2+2b^2=0.

Thus t is the rational component of (a+b sqrt(2))^2, while u is ab. The full sqrt(2)-component is 2u. This factor of two is accounted for: the correct replacement is q^2=t^2-8u^2, not t^2-2u^2.

Rows 263 and 264 remain present and unchanged in the target. Direct enumeration of every source residual shows q occurs only in row 505 and row 506. In row 506 it occurs only as -q^2. The target contains no occurrence of coordinate 535. There is no hidden consumer of the omitted coordinate.

## Exact residual identity

Write K for the part of row 506 not containing q. Its exact source form is K-q^2. Its exact target form is

    K-t^2+8u^2.

The polynomial part K is identical term for term, including every rational scalar and sign. Let

    P=a^2-2b^2,
    R263=a^2+2b^2-t,
    R264=ab-u.

The identity checked in the actual certificate is

    K-t^2+8u^2
      = (K-P^2)
        +(a^2+2b^2+t) R263
        -8(ab+u) R264.

The two factors in the transported certificate are exactly a^2+2b^2+t and -8ab-8u. They multiply unchanged rows 263 and 264, neither of which contains q. The apparent quartic terms cancel, leaving precisely the displayed quadratic target row.

Row 505 has coefficient +1 on q and no other occurrence of q. Its replacement q=P is therefore a valid constant-pivot elimination. All rows other than 505 and 506, and all coordinates other than 535, are exactly unchanged. The input coordinate and fixed parameter C=3^(2^25) are unchanged.

## Forward and reverse witness maps

For a rational source solution, rows 263, 264 and 505 give t=a^2+2b^2, u=ab and q=a^2-2b^2. Hence q^2=t^2-8u^2. Forgetting q gives a target solution because the new row 506 then equals the old row 506.

For a rational target solution, insert the unique rational value q=a^2-2b^2. Row 505 holds by definition. The retained rows 263 and 264 give q^2=t^2-8u^2, so the old row 506 holds. No other row can change because no other row contains q.

These maps are inverse and fix every other coordinate. No square root is chosen. The cases q=0, a=0, b=0 or a=b=0 require no exception. There is no division by q, a, b or another variable, and no change in the quantified domain.

## Independent check and scope

`03-depth/check_norm_elimination.py` was written for this review and imports neither the elimination search nor a producer. It verifies the source and target hashes, literal coordinate names, all four actual row bindings, complete q-incidence, both retained identity rows, the exact certificate multipliers, the unchanged exterior system, and the final count of 498 coordinates and 467 residuals. It passes.

The final `verify498.py` also contains a complete constant-pivot/certificate replay and a full sum-of-squares comparison. I inspected that checker but did not treat its prior output as the proof of the norm identity. The independent local check and displayed all-rational witness maps establish this component directly.

No additional primary arithmetic source is needed for this elimination. It is a polynomial identity in a,b,t,u and a constant-pivot substitution. Its acceptance does not depend on whether a,b are later interpreted as elliptic coordinates. The source interpretation was nevertheless checked to ensure the retained t,u rows are the actual objects consumed by the new scalar row.

No error or missing case was found. No shared file was changed. This acceptance is limited to the bound 499-to-498 norm-coordinate step and does not independently certify the entire Diophantine construction or authorize publication.
