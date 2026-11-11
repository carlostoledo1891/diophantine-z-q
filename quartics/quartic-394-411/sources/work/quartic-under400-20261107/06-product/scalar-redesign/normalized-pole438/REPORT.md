# Normalizing the scalar pole after preparation zero

This exact rational equivalence removes one further coordinate from the proposed439 system. The result has438 variables,437 witnesses,416 quadratic residuals and6,655 quartic monomials. Degree, content and maximum coefficient remain four, one and16*3^(2^26). Its arithmetic validity is conditional on the separate preparation-zero439 proof.

Source SHA256: `135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3`.
Candidate SHA256: `6867a2365bf3bc33225aba4d055d4e698f2fbcd67b958d6f528e477b0e697ea9`.
Polynomial SHA256: `e0684677d00d82b700d8442aa71d2c9226b6e000e46bfbfb2ad59bd55e6e253a`.

## Exact maps and domain

Let x be the retained stored scalar input, coordinate526. Its semantic value is b=-Kx with fixed K>0. The unchanged point and scalar-root rows imply r>0, c=r+4896>0, q=Norm(f(H)) nonzero, W>0 and therefore b=crW^2>0. Hence x is nonzero in both the old and new systems. This conclusion comes from rows outside the pole block; it does not depend on the removed preparation-square coordinate or a pole inverse witness.

After preparation zero, the old coordinate531 equals x^2. Rescale the private coordinates as follows, where the symbols on the right denote their new values:

    old v51  = x*v51,
    old v52  = x*v52,
    old v53  = x*v53,
    old v54  = x*v54,
    old v532 = x*v532,
    old v527 = x^2*v527,
    old v534 = x^2*v534,
    old v531 = x^2.

All other coordinates, including x and the input X, are fixed. This is the ordinary pole normalization, applied here to the scalar pole only after its preparation has become U=b. The factored second conic is retained.

Substitute these formulas into each of the five remaining scalar pole rows: the p-square row, first conic, factored h row, q-square row and second conic. Each result is x^2 times a quadratic polynomial in the new coordinates. Divide by that nonzero factor and keep the resulting five rows. The old equation v531=x^2 becomes an identity and is deleted together with coordinate531.

The p-square, q-square and second-conic rows have exactly the same coefficient lists after this normalization. In the first conic, the old e*x term becomes linear in the new e, and the old x^2 term becomes constant. The x*p-square term remains quadratic. In the factored h row,

    17*v51*x + K*v51*v531 -17*v52*v532=0

becomes

    17*v51 + K*x*v51 -17*v52*v532=0.

These are the only two nontrivial coefficient changes. The exact K and other first-conic coefficients are taken from the pinned source; the verifier checks their complete values.

From an old solution, divide each private coordinate by its indicated nonzero power of x and forget531. Conversely, reconstruct the old coordinates by the displayed multiplication formulas and set531=x^2. These maps are mutual inverses on all retained coordinates. They work when any of e,p,s,v,q or their square coordinates is zero. The fact that x is negative under the semantic normalization does not affect invertibility or any squared residual identity.

Every coordinate with a changed meaning has consumers only in these five rows. The deleted coordinate appears only in its old defining row and the factored h row. Thus the maps fix all outside equations and the actual scalar pole input. There is no new local or global arithmetic choice and no additional theorem application in this step.

## Evidence and limits

`build.py` performs the weighted substitutions. `verify.py` imports no producer, reconstructs the two changed rows directly, proves the five full polynomial substitution identities, checks every unchanged row and the complete incidence, and expands every quartic coefficient after primitive integer normalization. All checks pass.

The proof of the439 source's preparation specialization is a separate arithmetic dependency and must receive its own non-author review. This packet does not assert that the original arbitrary preparation can be normalized away before that specialization. All earlier files and the released manuscript remain unchanged.
