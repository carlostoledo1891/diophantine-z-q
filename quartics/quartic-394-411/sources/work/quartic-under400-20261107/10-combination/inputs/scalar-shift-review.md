# Independent review of the shifted label and five scalar corrections

Reviewer: agent03. Author: agent06. I accept the frozen 453-to-450 component on its stated inherited arithmetic inputs. This review found no hidden local, integrality, sign, or size assumption in the new application. It does not accept a later combined artifact without checking that composition, and it does not re-prove the inherited height or prime-selection theorems.

## Bound artifacts

The reviewed packet is ../06-product/scalar-redesign.

| Artifact | SHA-256 |
| --- | --- |
| Input rational453-ir.json | f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f |
| candidate450-ir.json | 31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6 |
| polynomial450.json | 24f024ca5db98e4fb9a8fa831b8fb4ced8e5baeb5a9724c0c6da3da80697b3c9 |
| REPORT.md | 3011bee6336dfd90828fa09e5d0c844c931dcb39fe98c736160a095f7ce20c13 |
| CONSUMERS.json | 30387007d4e6ce8aa3a92336fe1add87073774f5614c9027a3eabfe38024dd3c |
| MANIFEST.json | cc623e93eee15473c02b7c1d25c3163ee501edc83833ee02c02da86c86a73d18 |

All file pins in the manifest matched. I read the author proof, the nine obligations and source bindings in CONSUMERS.json, the builder and checker, and the actual source passages identified below. I wrote and ran check_scalar_shift_review.py, which imports no author implementation. It passes the exact translation of all fifteen changed input-square consumers, the unchanged input equation, every other row and coordinate, the five correction equations, all 32 joint local signatures, the two-adic residue calculation, and the complete sum of squares. The count is 450 total variables, 427 quadratic residuals and 6,593 quartic monomials. The fixed giant coefficient was not expanded.

## Label and contact domain

The new label is beta=2X^2+2403 for X in Q. It is at least 2403, so every factor of

    r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1)

is strictly positive. Thus r is never zero. For integral X it is a positive integer and beta is positive and odd. If X=u/v is reduced and beta is integral, then v^2 divides 2u^2, hence v^2 divides 2 and v=1. Conversely integral X plainly gives integral beta. At an odd prime, a negative valuation of beta equals 2v_p(X), since the constant 2403 is integral and 2 is a unit. It is therefore even. No such assertion is required at the exceptional prime 2.

These are the input-specific premises of the scalar bridge. I checked the bridge in the pinned manuscript quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9: the original scalar32 argument at lines 10428 onward, its explicit extension of the label premises at lines 19319-19325, and the later reduced scalar proof at lines 20263-20350. The height theorem at lines 8921 onward applies to every rational argument outside its contact set. It has no hypothesis beta>2500. The new label avoids the full contact set, so beta=2403 at X=0 is included, not omitted.

## Joint squareclass coverage

For X=2k, the factors beta-1 and beta-2401 each have two-adic valuation one. The other factors are odd. Dividing r by 4 and reducing modulo 8 gives the three odd factors 3,7,5, while the remaining product is (4k^2+1)^2=1 modulo 8. Thus v2(r)=2 and r/4=1 modulo 8.

For X odd, write X^2=1+8t. Then beta=2405+16t, both even factors have valuation two, and r/16 modulo 8 is 5*7*1 times (1+4t)^2. Thus v2(r)=4 and r/16=3 modulo 8. These computations exhaust every integral X, including zero and negative X. The period-64 check is corroborating finite evidence, not a substitute for this algebra.

Consequently the possible joint class lies in the five-dimensional space consisting of the Q2 unit class 1 or 3, and both valuation-parity and unit-squareclass bits at each of Q3 and Q17. In that order I independently checked the generator vectors

    3  : (1,1,0,0,1)
    11 : (1,0,1,0,1)
    17 : (0,0,1,1,0)
    35 : (1,0,1,0,0)
    91 : (1,0,0,0,1).

Their 32 subset products have all 32 distinct signatures. This is simultaneous surjectivity at the three fields, not merely three separate surjectivity statements. The author's explicit exponent formula was also checked on all 32 targets. Taking c with the same signature as r makes cr locally square at all three fields. Each c is a positive integer. The correction chain starts at 1 and each factor equation forces the next value to be either its predecessor or g times its predecessor; hence no zero or negative branch is present.

The norm criterion at an odd prime is even valuation plus square unit residue. At 2 it is even valuation plus unit 1 modulo 8. These are exactly the criteria used. The products can contain 7 twice, but this does not invalidate the argument: the actual integer c, including that square factor, is used throughout.

## Actual scalar completeness requirements

The original completeness proof at manuscript lines 10520-10559 consumes an integer correction c such that cr is positive and square in Q2, Q3 and Q17. It then uses the finite support of cr to choose successively a deep positive shared index and a still deeper positive scalar index. It does not use an upper bound on c or squarefreeness of c after these inputs have been supplied. The new c has precisely these required properties. All its prime divisors are at most 17.

At primes dividing r, the prepared normalized leaves are integral. At primes dividing c but not r, all nonconstant leaves can be made divisible by the prime. In the reduced scalar tree, this gives W=1 modulo every prime on the support of cr. Thus W is nonzero and is a unit there. At those primes v_p(crW^2)=v_p(cr)>=0. Outside that support, v_p(crW^2)=2v_p(W) is even. This proves square reduced denominator; positivity and the three local-square conditions also hold. These are exactly the sufficient conditions for the original pole predicate. The correction choice therefore supports fresh pole witnesses for the actual new value crW^2.

The order of choices is valid: fix integral X and its one simultaneous correction; choose the deep shared and scalar indices; form the four positive odd root indices; fix their scales; choose the continuity modulus; only then select the contact primes and solve the existing simultaneous congruences. Arbitrary finite support and arbitrary prescribed divisibility were already allowed. No new simultaneous-realization theorem is being presumed. The source's allowed degenerate private pole witnesses remain allowed.

## Soundness and quantitative thresholds

At every consumed prime p>76176, c is a unit. The unchanged contact polynomial and even negative-valuation property therefore give the same odd valuation eta of r and the same scalar pole obstruction. The reduced scalar proof still yields ratio coefficient valuations at least 32. It handles the branch where the scalar point is near (0,0) by doubling that point before applying the formal logarithm; the new proof does not silently assume the point itself is formal. It follows that M5(beta)^32 divides the scalar index s, and

    h(beta) <= H*|s|^(19/32),  H < 2^2093966.

Neither exponent nor constant depends on the additive constant in beta once the stated contact premises hold. The anchor is unchanged, with log2|s|>25165823.5 and |s|>(80H)^10. Therefore the same estimates h(beta)<|a|/40 and log(48H)<|a|/40 hold for a=s+1. The order-40 Lucas contradiction remains unchanged. The order-10 comparison gives the same bound log B<(29/40)|a|, contradicting log B>|a|-3 under the same anchor. Its conclusion is now n=2X^2+2403, and the denominator argument above recovers X in Z. There is no numerical gap between 2403 and any required lower bound.

## Every physical consumer

The retained coordinate 248 is literally Y=X^2. Its defining equation is unchanged. In every other equation containing Y, the substitution is Y -> Y+1200, which changes 2Y+3 to 2Y+2403. I verified all fifteen such rows, including the grouped low-order detector evaluations; the inventory lists sixteen direct consumers only because it also lists the unchanged defining equation. Every other non-correction residual is identical. The source construction uses Y outside that equation through beta and its contact expressions, so this is the intended label change, not the unintended equation Y=X^2+1200 or an assumed square root of X^2+1200.

Only the eight old correction rows are replaced by the five stated chain rows. Deleted coordinates 58,59,60 have no outside consumer. The internal correction coordinates 61,...,64 likewise have no outside consumer. The final correction coordinate 65 is retained in all its actual scalar uses. No logarithm order, local denominator guard, anchor, point coordinate, or quantified field changes.

The new route is substantive and was reviewed anew; historical acceptance of the original seven-prime correction does not by itself accept it. This report accepts the exact component hashes above. Any combined implementation must discover and translate its own current Y consumers rather than blindly replaying the source packet's list of fifteen row names.
