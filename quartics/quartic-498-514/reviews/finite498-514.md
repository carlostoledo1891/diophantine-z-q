# Finite review of the frozen 498-variable composition

The frozen candidate passes the finite composition audit. It has 498 total
rational variables, including the input, 497 witnesses, 467 quadratic
residuals, and a quartic sum of squares with 24,669 monomials. This meets the
user's numerical threshold of fewer than 500 total variables.

No finite correction is requested. I accept the coordinate transport,
certificate composition, and coefficient table in the scope below. I authored
the final one-coordinate norm elimination, so this report does not count as
independent acceptance of that individual identity. A different reviewer must
accept it. I did not author the other transformations or the combination.

## Exact target

The input packet is `10-combination`, copied into `snapshot/`. The principal
SHA-256 bindings are:

| Artifact | SHA-256 |
| --- | --- |
| `candidate498-ir.json` | `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a` |
| `certificate498.json` | `217c34f9fbfc521090cf41d3522e3253be52b939ce4a30269ba8e9cd7e434704` |
| `polynomial498.json` | `817fec936dee3b358fc8b5b0b9a5570694adf009b134432467ef0be914aeedc4` |
| `candidate514-ir.json` | `5d7ed675b3ee255d9c09dec4ee4f80ea94d6dac747c8f255bac68e81b73484ba` |
| `polynomial514.json` | `d247a27709afda5f2be626390cffa1a175c3dfcbee1a5c832a1c457b32629bd5` |

The accepted finite 505-variable starting point and its prior review are
unchanged. That candidate has hash
`bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966`.
The current chain is exactly

```text
505 -> 504 scalar reciprocal chart
504 -> 501 mixed-depth toric circuit
501 -> 499 scalar denominator-square cancellation
499 -> 498 norm-coordinate elimination
```

The factored-detector and order-10 proposals are not in this target.

I also read the final `REPORT498.md`, hash
`d84f4f4fd8ab05ce221313609baf7b65ef7c7d2842f3719d0185cfd6d85ed558`.
Its counts, formulas, exclusions, and separation of contributor review from
composition acceptance agree with the frozen artifacts. The final version
of `verify498.py`, hash
`b8f8cabbe0aa87616eeea8bc219b68e581816fa36516b2410652a656b6023ce0`,
also includes the ordinary-lift checks. I reran this final version after
copying it into the snapshot. No candidate or polynomial data changed.

## Checks performed

`audit_final.py` is an independently written composition auditor. It reads the
frozen files, checks all intermediate and proposal hashes, verifies that IDs
and names are unique, and requires complete declared-coordinate support.
The protected input is preserved. It derives the full deleted, added,
changed, and renamed sets at each step and compares them to the certificates.

It then reruns the four standalone verifiers for 504, 501, 499, and 498.
The copies of the 504 and 499 drivers have only their repository and depth
source paths relocated. The equation and assertion bodies are unchanged.
The 501 and 498 drivers are unchanged. These runs are recorded in
`replay504.log`, `replay501.log`, `replay499.log`, and `replay498.log`.

All exact row checks, field identities, certificate replays, and full
sum-of-squares comparisons passed. `FINAL-FINITE-REVIEW.json` records the
complete change sets and verifier hashes. `SNAPSHOT-SHA256.json` binds all
copied artifacts.

The 498 table has content one, degree exactly four, and maximum coefficient
magnitude `16*C^2 = 16*3^(2^26)`, where `C=3^(2^25)` is fixed. The sole
C-squared term has no lower-C contribution at the same coordinate monomial;
the fixed coefficients have fewer than 2,048 bits, and all linear-C
multipliers have magnitude at most 48. No decimal expansion of C was used.

I also independently checked the 514-coordinate ordinary lift, using full
polynomial multiplication rather than the producer's triangular expansion.
Every original residual is its exact substitution at the last constant-chain
coordinate. The sixteen added equations start with `c0=3^1024` and perform
fifteen squarings, ending uniquely at `3^(2^25)`. The result has 483 residuals,
24,716 monomials, degree four, content one, and maximum coefficient
`3^2048+1005072314676622`, of bit length 3,247.

## Coverage of the four new steps

For the scalar reciprocal chart, the auditor checks the eight deleted old
coordinates, seven new coordinates, eight deleted rows, seven new rows, and
four changed f/z output equations. All other residuals are identical. The
deleted coordinates have no consumers outside those changed/deleted rows.
The standalone verifier checks the four reciprocal identities on the literal
curve and uses the depth source's actual semantic values. This preserves the
private ordinate-product normalization factor discussed in `REPORT504.md`.

The reverse interpretation of that chart at the exceptional branch remains
a mathematical obligation. `REPORT504.md` uses the retained anchor to exclude
S=-P after evaluating its genuine R=-2P output. This finite audit checks the
algebraic formulas and unchanged anchor but is not a fresh independent audit
of the complete anchor arithmetic theorem.

For the mixed-depth toric circuit, exactly 24 old chain equations are replaced
by 21 new equations, exactly three private coordinates disappear, and exactly
15 retained private coordinates are renamed. Every other row is identical.
Both q12 and q40 remain, so the restored order-12 detector is not silently
discarded. The original six private weight coordinates have no consumers
outside the replaced chain. The unchanged power identities used by the new
chain are checked literally.

The new equations force, with E and q denoting the retained outputs,

```text
a=E^-1, b=E^-3, u=E^4*q, v=E^11*q^2,
q12=E^22*q, t=E^45*q, q40=E^78*q.
```

The retained equation E*a=1 forces E nonzero. Setting q=0 in the unchanged
q-definition would force E=0, so q is nonzero as well. Thus all divisions in
this sequential derivation are legitimate, and the old and new chains have
the same retained outputs with unique private lifts. The exact coefficient
checker verifies the monomial identities and all outside consumers.

For the denominator-square cancellation, the only removed coordinates are
the two d2 components. Only their two defining rows are deleted; only the two
k rows change. The exact field identity

```text
d*L = a*K - 2*D*b*G
```

is checked against the source equations. The old and new equations have
equivalent solutions because a is a nonzero field constant and d=c*x+D is
nonzero on the retained chart: c=a^2 and D=(3-sqrt(2))^2 are positive at both
real embeddings, while x=h^2 is nonnegative. Reinserting d2=d^2 gives the
unique reverse lift. There is no extra exceptional branch introduced by this
cancellation. Every unchanged chart and scalar consumer is retained exactly.

For the norm elimination, the transported certificate is exactly the
contributor certificate from `01-elimination/sub500/from501`. Its source
rows and retained identity rows are unchanged by the previous scalar-chart
cancellation. The pivot, sole consumer, and two retained test-square
equations receive a complete exact replay. No other row consumes the removed
coordinate. The identity is

```text
(f0^2-2*f1^2)^2 = (f0^2+2*f1^2)^2 - 8*(f0*f1)^2.
```

I verified its transport and the resulting full table, but, as its author,
do not independently accept this identity here. This limitation does not
apply to the independent audit of the combination producer's transport.

## Scope and reproduction

This review checks the new finite chain from the already reviewed 505
snapshot. The earlier `combined-review/REPORT.md` contains the 505 source
rebuild, depth gate checks, and complete earlier composition audit. Its
arithmetic limitations remain in force. The current review does not refresh
or expand acceptance of the inherited global number-theoretic theorem.

Run from this directory:

```text
python -B audit_final.py
```

The script uses standard-library Python and reads the pinned source/proposal
files at their recorded locations. It writes only in this review directory
and its copied snapshot. The usable Python executable here was
`C:/Users/glaze/.local/bin/python3.14.exe`.

Disposition: finite composition and tables accepted for the hashes above;
independent acceptance of the reviewer's own norm step excluded; broader
arithmetic acceptance remains a separate review. No manuscript, repository,
contributor source, or previously accepted review was changed.
