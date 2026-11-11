# Ordinary companions of anchor-gamma313

These are exact ordinary-coefficient lifts of the independently accepted anchor-gamma313 candidate. They preserve its new completeness argument and do not impose another local or real condition. The new lift artifacts require their own independent composition review.

| Variables | Witnesses | Quadratic residuals | Quartic monomials | Constant gates | Maximum bits | Decimal digits | Text bytes |
|---|---|---|---|---|---|---|---|
|330|329|300|6121|16|1627|490|181845|
|329|328|299|6118|15|3250|979|189872|
|328|327|298|6115|14|6496|1956|210336|

All three polynomials have degree four and content one. The330-variable lift meets the released bound below2^3247. The329-variable lift exceeds that cap by three bits. The328-variable lift meets the8193-bit comparison cap. These totals come from complete expanded tables, not gate estimates. This does not reach the symbolic strict-under300 milestone.

## Inputs and maps

The source is `work/quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json`, SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`; its polynomial hash is `d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d`. The independent source review is `10-combination/review-anchor-gamma313/REVIEW.md`, SHA256 `981dff20bd980f2a040e8b31418cdd0c74e7bcf6e1356c6322fd01f9b42cca13`.

The reused weighted chains are the same separately accepted component as in `ordinary-sparse-shared314`. Their original review is `work/quartic-optimization-20261107/resume-sol-review-ordinary-chains-20261107/REVIEW.md`, SHA256 `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`. The earlier314 transport review is `resume-review-transports314-20261107/REVIEW.md`, SHA256 `abc780609bf1b9a65100608eac4bec936f8844ea9b91fdeed973b24241c0efa7`. Neither earlier review is asserted to approve the current files automatically.

For each lift add Q=48v83^2+48v87^2+432v89^2 in coordinate1000, and a uniquely determined constant chain c0=3^a0, c_j=3^a_j*c_(j-1)^2. The exponent lists are respectively

    [513]*9+[2]+[0]*6;
    [1025]*10+[2]+[0]*4;
    [2049]+[2048]*11+[0,0].

The exact recurrence e0=a0, e_j=2e_(j-1)+a_j ends at2^25, so each final coordinate equals C=3^(2^25). Only rows504 and1903 contain the source parameter. Replace them by

    u^2+6v^2-2w^2-4*C*w-3*T^2=0,
    T-2g0*g1-C*Q=0,

with C the final constant coordinate. This makes every residual quadratic in all quantified variables. Substituting the unique Q and C recovers both symbolic rows exactly. Forward extension is unique; the reverse map forgets only these new helpers.

All313 source coordinates and all other281 residual objects stay identical. New coordinate and residual IDs1000 through1016, or the shorter prefix, do not collide with the retained inverse-anchor chain1101 through1108. In particular u is unchanged, the inverse equation still excludes u=0, and gamma=1/u is unchanged. The constant C and the common detector scale are never identified.

## Exact tables

`build.py` emits each rational IR, complete decimal polynomial JSON, complete tab-separated text table and certificate. `verify.py` imports no producer, checks all unchanged objects and exact source-row recovery, reconstructs each chain, independently expands every primitive residual square, and parses each text table back into the exact polynomial. All checks pass.

`INHERITED-CONSTANT.json` contains the1514-bit integer K, the source polynomial's constant coefficient. The exact maxima are3^1026+K,3^2050+K and3^4098+K. Their full decimal values are in the certificates and tables. No enormous decimal expansion of C is performed. `SUMMARY.json`, `VERIFICATION.json` and `MANIFEST.json` bind all actual counts, bytes, coefficients and source pins.

All accepted symbolic and ordinary predecessors remain unchanged. No manuscript, release package or published repository is modified.
