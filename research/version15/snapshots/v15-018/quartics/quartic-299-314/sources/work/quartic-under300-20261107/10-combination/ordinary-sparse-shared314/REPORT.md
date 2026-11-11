# Ordinary-coefficient companions of sparse shared314

These three frozen candidates transport the independently reviewed weighted constant chains to the exact sparse-shared314 source. All coefficients are written as ordinary decimal integers in the complete JSON and text polynomial tables. The new compositions await independent review; no prior acceptance is promoted automatically.

| Total variables | Witnesses | Residuals | Monomials | Constant gates | Maximum bits | Maximum digits | Text bytes |
|---|---|---|---|---|---|---|---|
|331|330|300|6122|16|1627|490|181869|
|330|329|299|6119|15|3250|979|189896|
|329|328|298|6116|14|6496|1956|210360|

Every residual has degree at most two, and every final polynomial has degree four and content one. The 331-variable companion meets the released coefficient bound below 2^3247. The 330-variable companion exceeds that bound by three bits. The 329-variable companion meets the alternative bound below 2^8193. These are actual expanded counts, not counts inferred by adding gate budgets.

## Pinned inputs

The symbolic source is `../sparse-shared314/candidate314-ir.json`, SHA256 `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382`; its polynomial is `1fc9ba1e03e5134bd3173f22d80ecc5c29838996c1cb58839264844f6358d77e`. Its report records the separate shared314 arithmetic/construction acceptances and the earlier sparse-Lucas acceptance. The present symbolic transport still requires its own independent review.

The constant-chain component is `work/quartic-optimization-20261107/resume-elimination-20261107/ordinary-chains`. Its independent review is `resume-sol-review-ordinary-chains-20261107/REVIEW.md`, SHA256 `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`. The exact approved336/335/334 input IRs are separately pinned by `build.py`, each candidate certificate, and the manifest. Only their constant/anchor delta is used here.

## Exact lifting and inverse

Introduce Q in coordinate1000 with

    Q=48*v83^2+48*v87^2+432*v89^2.

For each chain let c0=3^a0, c_j=3^a_j*c_(j-1)^2. The three exponent lists are

    16 gates: [513]*9+[2]+[0]*6
    15 gates: [1025]*10+[2]+[0]*4
    14 gates: [2049]+[2048]*11+[0,0].

In every case the integer recurrence e0=a0, e_j=2e_(j-1)+a_j ends at 2^25. Hence the last coordinate is uniquely C=3^(2^25), without sign or zero branches. The other new coordinates are also uniquely determined. The inverse projection simply forgets Q and the constant chain.

The only source residuals consuming C are504 and1903. They become

    u^2+6v^2-2w^2-4*C*w-3*T^2=0,
    T-2*g0*g1-C*Q=0.

Here C is now the final chain coordinate. Substituting the unique Q and C recovers the two symbolic source rows exactly. The C*Q gate is quadratic; direct substitution of the quadratic Q expression after making C a variable would be cubic, which is why Q is explicitly counted.

All source coordinates, including gamma1100 through gamma1601108 and the promoted P1 pair1109/1110, remain identical. New coordinate and row IDs1000 through1016 (or the shorter prefix) are disjoint from every source coordinate and residual. No source row other than504/1903 changes. In particular the common gamma parameter is unrelated to the fixed C chain and retains its separate guard and arithmetic proof.

## Coefficients and reproducibility

`INHERITED-CONSTANT.json` stores the complete ordinary integer K, the symbolic source polynomial's C-independent constant coefficient. The exact maximum coefficients are respectively 3^1026+K, 3^2050+K and 3^4098+K. Each full decimal value is also present in its candidate certificate. K has1514 bits. The large fixed C itself is never expanded in decimal.

`build.py` generates each IR, complete JSON polynomial, complete tab-separated decimal text table and certificate. `verify.py` imports no producer, reconstructs all chains from the exponent lists, proves the exact final exponents, checks every unchanged object and both source-row reconstructions, independently expands every primitive residual square, and parses the text table back into the exact polynomial. `SUMMARY.json` and `VERIFICATION.json` record the actual counts and maxima. The manifest pins every artifact and the reused accepted components.

There is no new arithmetic premise or changed completeness order. These are exact lifts of the symbolic candidate, conditional on its separate acceptance. No accepted artifact, manuscript or published repository is modified.
