# Scalar preparation zero after simultaneous real and finite-place preparation

This proposal saves three coordinates from the accepted442 system. It gives439 total variables,438 witnesses,417 quadratic residuals and6,658 quartic monomials. The degree remains four, content one and maximum coefficient16*3^(2^26), with unchanged fixed C=3^(2^25).

Source SHA256: `e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86`.
Candidate SHA256: `135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3`.
Polynomial SHA256: `0347a66d00cc80282c2cca559bbeba190550c676dfdb9c3f00002ff9a53adcb1`.

## Existing statements applied

Use the frozen v11 manuscript's `v5:preparation-zero-bridge` and `v5:real-progression-bridge`, with the same curve, point, real embeddings and scalar-pole convention as the accepted source. Exact manuscript hashes and line locators are recorded in `SOURCE-PINS.json`.

The first lemma permits the original scalar preparation U=b when the rational input b has square reduced denominator, is positive and square in Q2,Q3,Q17, and satisfies

    b<17,  v2(b)>=3,  v3(b)>=1,  v17(b)>=2.

Its conclusion is existence of the same remaining scalar pole witnesses. It permits their degenerate zero values; no new inverse condition on them is introduced.

The real-progression lemma defines G as the closure of the simultaneous real orbit of P and its conjugate, and G0 as its identity component. It states that if m=|G/G0| divides both L and h0, then the positive tail of h=h0 mod L is dense in G0 and meets every nonempty open subset infinitely often. Its proof also states that a progression with modulus divisible by m and residue divisible by m has closure G0. We use this exact open-set statement, not only the lemma's weaker boundedness statement.

## Scalar functions and their real behavior

Retain the accepted input label beta=51(2X+1)^2+2504, positive contact product r, and deterministic c=r+4896. Fix an integer input X, so c and r are now fixed positive integers. For a shared point H and scalar point R put

    q(H)=Norm(f(H)),
    z(R)/z(H)=z0+z1*sqrt(2),
    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q(H)^2)/r^32,
    b=c*r*W^2.

For every allowed H, q(H) is nonzero, so W>0 and b>0. At either real embedding the functions f=1/x and z=-x/y extend continuously to O with value zero. Consequently q(H) tends to zero when both real components of H tend to O. Once H0 is fixed and nonidentity, both real values of z(H0) are nonzero. Taking R sufficiently close to O at both real embeddings then makes both real values of z(R)/z(H0), and therefore both rational coefficients z0,z1, as small as desired.

It follows directly from the displayed formulas that H0 can first be chosen so that the term q(H0)^2/r^31 is arbitrarily small, and R can next be chosen so that the term B^2/r^32 is arbitrarily small. Thus b(H0,R) can be made strictly smaller than17, for example smaller than17/4. This possibility depends on the removed constant branch: the new W has no constant summand.

## Choosing the same rational points with all finite conditions

Let S0 be the finite prime support of cr, and enlarge the preparatory set to S*=S0 union {2,3,17}. In this construction2 and3 already lie in S0, whereas17 does not. Let m=|G/G0|, a fixed positive integer depending only on the real orbit of the original point P.

Choose a positive integer M divisible by64 and m and sufficiently divisible that every point [Mk]P meets the required finite lower valuation bounds for f(H) at all places over S*. This is possible because sufficiently deep formal subgroups have finite index, exactly as in the existing scalar preparation proof. At p dividing r with eta=v_p(r), use coefficient depth at least8eta for f(H); at17 require positive coefficient depth; at the other primes of S* use at least the depths in the accepted442 preparation.

The positive progression h0=0 mod M has dense real image in G0 by the existing real-progression lemma. A neighborhood of (O,O) in G0 is nonempty and open. Hence choose h0>0 in this progression so that H0=[h0]P has q(H0) as small as required above. H0 is not O in either real embedding: P has infinite order and h0 is nonzero. All finite bounds are automatic from the choice of M. In particular m divides h0.

With this H0 fixed, choose a positive integer N divisible by6 and m and sufficiently divisible that every [Nk]P meets the anchor and the required finite bounds for R and z(R)/z(H0). At p dividing r use coefficient depth at least24eta for the ratio; at17 require positive coefficient depth; at primes dividing c but not r use positive ratio coefficient depth. The existing scalar preparation permits all these bounds and arbitrary additional divisibility. The anchor is achieved by such divisibility, and its size bound is achieved by taking a sufficiently large positive multiple.

Apply the same real-progression lemma to s=0 mod N. Its positive tail is dense in G0. Choose s arbitrarily large in this progression with R=[s]P sufficiently close to O at both real embeddings to make b(H0,R)<17/4. Since H0 was fixed first, the real ratio denominators are fixed nonzero numbers. This simultaneously satisfies the finite conditions, the physical anchor, positivity of s and6 dividing s. Set a=s+1, as in the accepted construction.

Thus the real smallness and finite depth requirements hold at the same rational points H0 and R. They have not been produced separately and assumed to be compatible.

## Local hypotheses for preparation zero

At p dividing r, the accepted depth24 calculation gives v_p(W)>=0. At p dividing c but not r the positive coefficient bounds give the same integrality. Hence b has nonnegative valuation on S0 and even valuation outside S0; its reduced denominator is a square. Its local squareclasses at2,3,17 equal those of cr and remain squares.

For this input label and correction, v2(cr)=4 and v3(cr)=2. Since W is integral there,

    v2(b)>=4>=3,  v3(b)>=2>=1.

At17 both r and c are units. The separately imposed positive coefficient depths give v17(q)>=2 and v17(B)>=2. Therefore v17(W)>=4 and v17(b)>=8>=2. These bounds do not require17 to divide cr; it was included explicitly in S*.

The prepared value b(H0,R) is therefore positive, smaller than17, locally square at2,3,17, has square reduced denominator, and has all three required lower valuations.

## Preserving the strict real bound through the final CRT

Keep R fixed. By continuity there is a nonempty open neighborhood U of H0 in G0 on which the scalar expressions are defined and 0<b(H,R)<17. The finite lower valuation bounds persist when the integer shared index satisfies h=h0 modulo a sufficiently divisible integer L. Require64 and m to divide L as well.

Choose the two remaining Lucas labels, root points and height scales exactly as in the accepted source, before selecting any contact primes. The comparison functions are now fixed. Enlarge L if necessary to include their same finite local continuity requirements; this preserves all earlier scalar congruences and m dividing L. Their pole sets satisfy the finite-fiber hypotheses of `v5:real-progression-bridge`. By the proof of that lemma, a finite union of such pole sets has measure zero in G0, so it cannot cover U. Choose a nonempty open subset U' with compact closure inside U and avoiding every required pole. The same continuity argument bounds all real comparison functions on this compact closure by a constant fixed before the contact-prime choice. This supplies the real boundedness used by the existing asymptotic pole estimates while retaining the strict scalar bound b<17.

Now use the same simultaneous-prime theorem and the same separation lemma. The accepted CRT gives

    h=0 mod Pi^19*Mminus,
    h=1 mod Mplus,
    h=h0 mod L.

All previous coprimality conditions are unchanged: L was already an arbitrary fixed sufficiently divisible modulus chosen before the contact primes, and including m or extra17-depth only enlarges that fixed modulus. Let h=h1 modulo T be the resulting nonconstant integer progression. Since L divides T and h1=h0 modulo L, both T and h1 are divisible by m. Therefore this final progression has dense positive tail in G0. It meets U' at arbitrarily large positive indices.

Choose the final h in U'. Its finite scalar bounds are preserved by h=h0 mod L. Its strict real bound b<17 holds because U' lies in U. It has every required comparison domain and the same uniform real bounds used by the original prime argument. Thus this one final shared point simultaneously has all primary/opposite local depths, all scalar finite conditions and the strict real scalar bound.

Apply `v5:preparation-zero-bridge` to this final b. It supplies the remaining pole witnesses with preparation U=b. The accepted factored second-conic implementation still has its required positive input. If its factor parameter is zero, the same zero-branch lift applies. The local scalar soundness, heights, anchor, odd-label and input projection are otherwise unchanged.

## Concrete quadratic replacement and reverse map

In the current implementation the semantic pole input is b=-K*v526, with the positive fixed rational integer K recorded in `VERIFICATION.json`. The semantic preparation-square output is K^2*v531. The old preparation rows are

    U^2=K^2*v531,
    1+K*v526*J=0,
    K*v526+K^2*J*v531+V^2=0.

Coordinates U,J,V have IDs50,528,529. Replace these three rows by

    v531=v526^2.

Delete those three coordinates. The retained preparation-square output is now exactly b^2, so it is the preparation-zero value consumed by the rest of the pole block. Every other residual, including the factorized pole equations, is unchanged.

For soundness at an arbitrary new rational solution, the existing point domain gives q nonzero, r>0 and W>0; deterministic c>0 then gives b>0. Thus b is nonzero even though the explicit preparation inverse coordinate was deleted. Restore U=b, J=1/b and V=0. These satisfy all three old preparation rows, and the preparation-square output and every outside coordinate are unchanged. This proves that every new solution lifts to the accepted442 system. It includes all possible zero values of other pole witnesses.

Completeness is the real and finite-place construction above; no claim is made that every old preparation witness admits this specialization.

## Verification and scope

The independent finite checker reads the actual K and K^2 coefficients, checks the exact normalization, all removed-coordinate consumers, every unchanged row, fixed coefficient and every quartic coefficient. The semantic reverse map and the complete arithmetic specialization are given above. A computational pass is not a substitute for independent review of the real-progression and preparation-zero theorem applications.

The proposal is frozen for agent05's assigned non-author review. No prior packet or published manuscript is changed.
