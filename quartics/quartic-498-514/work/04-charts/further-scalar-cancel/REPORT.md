# Cancel the scalar reciprocal denominator square

The current 504-variable system has a redundant pair of scalar chart coordinates. Removing them gives a 502-variable system with 471 quadratic residuals and a quartic sum of squares with 24,670 monomials. The change preserves the projection onto every retained coordinate, with a unique rational lift in the reverse direction. It requires no new arithmetic input or exceptional-point argument.

The source is `10-combination/candidate504-ir.json`, SHA-256 `7c17debaff9a726562be6b7ef843dbc6ca6a0a9d17556158c54ffe5c49ddb0cd`. Its scalar chart and source qualifications are described in `10-combination/REPORT504.md`. The new artifact is `candidate502-ir.json`, SHA-256 `83a38c1ae10534721afd6e254d31783e65d94bf9a42b61e2f26b6bd1c4779c09`.

This saves two variables independently of the three-variable mixed-depth toric change. Applying both changes to the 504-variable source would give 499 total variables, but that composition needs its own exact check. No manuscript or earlier candidate was edited here. Independent acceptance of this cancellation is pending.

## Equations

Use the exact source constants in `K=Q(sqrt(2))`:

    a = -1+(7/4)sqrt(2),
    b = 39/8-(9/2)sqrt(2),
    c = a^2, D = 11-6sqrt(2), b^2=c^2-D.

For the incoming scalar point use the unchanged chart `x=h^2`, `j^2=x^2-D`. Write

    d = cx+D,
    N = aj-bh,
    M = -2aDh(x+c)-bj(cx-D).

The 504-variable source has

    dg=N,
    d2=d^2,
    d2 k=M.

Delete the two rational coordinates of `d2` and their two defining residuals. Replace the last field equation by

    a d k + 2D h + ab j - 2Db g = 0.

This replacement still gives two rational quadratic residuals. Here `d` is affine in the already stored `x`, and all of `a,b,c,D` are fixed constants. No new coordinate is introduced. The two deleted coordinate IDs are 545 and 546, named `scalar.shiftedS.reciprocal.d2.0` and `.1`. Only the two `scalar.shiftedS.reciprocal.k.definition.*` rows change.

Equivalently, the new equation is

    d k = -(2D/a)h-bj+(2Db/a)g.

The implementation uses the version multiplied by `a`, so it does not need to encode a field-constant inverse.

## Exact identity and rational witness maps

Define field residuals

    G=dg-N,
    K=d^2 k-M,
    L=a d k+2D h+ab j-2Db g.

Then the polynomial identity

    d L = a K - 2Db G

holds. Expansion reduces it to `a^2=c` and `b^2=c^2-D`. It does not require division or use `j^2=x^2-D` to establish the identity. The checker verifies both rational components exactly.

The fixed `a` is nonzero; its rational norm is `-41/8`. The varying `d` is also nonzero on every incoming source chart. At both real embeddings, `c=a^2>0`, `D=(3-sqrt(2))^2>0`, and `x=h^2>=0`. Thus `d=cx+D>0` at both embeddings. This is exactly the nonzero denominator already used by the source reciprocal chart, not a new guard.

Forward map: start with a 504-variable solution and forget `d2`. Its old equations give `G=K=0`, so the displayed identity gives `dL=0`. Since `d!=0`, the new residual `L` vanishes. All other coordinates and equations remain unchanged.

Reverse map: start with a 502-variable solution and set `d2=d^2`, using its two rational coefficients. The unchanged equation gives `G=0`, and the new equation gives `L=0`. The identity gives `aK=0`, so `K=0` because `a!=0`. The old chart equations hold. The lift is unique because `d2` had its defining equation.

These maps preserve `g,k,f(R),z(R)`, the scalar ratio and norm tree, the anchor, all five comparison guards, every detector coordinate, and the input. They preserve all exceptional branches already handled in the source504 argument. In particular, this cancellation neither adds nor removes the `S=+/-P` cases; it leaves the source504 nonzero guard and anchor unchanged.

## Checks and scope

`build.py` reads only the frozen source504 and the frozen mixed-depth semantic-value file. It constructs the new residual system and its full symbolic sum of squares. The fixed parameter remains `C=3^(2^25)`.

`verify.py` imports no producer. It independently checks:

* The exact field constants and `b^2=c^2-D`.
* The two-component residual identity `dL=aK-2DbG`.
* The actual source `g` and `k` equations, including their row normalization factors.
* That the deleted coordinates occur only in the deleted `d2` equations and replaced `k` equations.
* Every unchanged residual, all remaining coordinate incidences, and every coefficient of the new sum of squares.

The checks passed. `VERIFICATION.json` records 502 variables, 501 witnesses, 471 residuals, degree four, 24,670 monomials, content one, and largest coefficient `16*3^(2^26)`. `polynomial502.json` contains the complete sparse symbolic coefficient table. No giant fixed integer was expanded.

The correctness of the cancellation is an exact equivalence of the two residual systems on their unchanged incoming point chart. It does not independently approve the source504 arithmetic construction or the future toric composition. A reviewer other than this author must accept the change before it is used as an independently accepted optimization.

Run `python -B build.py` and `python -B verify.py` with the supplied Python runtime from this directory. Both scripts write only here.
