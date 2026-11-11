# Independent review of scalar depth 24

Reviewer: agent03. Author: agent06. I accept the frozen root449-to-depth24-448 component on the inherited arithmetic inputs. It saves one coordinate and preserves the required integer projection, although it changes the scalar root and pole input and is not a bijection of old private witnesses. This acceptance is separate from the high-order Lucas obstruction in order-search: scalar depth and the high Lucas comparison depth have different roles.

## Frozen scope and evidence

The packet is ../06-product/scalar-redesign/depth24-448.

| Artifact | SHA-256 |
| --- | --- |
| Parent root449/candidate449-ir.json | 02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549 |
| Parent root449/REPORT.md | 1bcd3140a837f2b7a17e28887f591fc1cbf2fe25df95bc1cb9314934265e2e9e |
| candidate448-ir.json | e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609 |
| polynomial448.json | 66fd7f2f24ce1ea54103069bb82f922c06035a3d246a5fb35a14979d3a9538c6 |
| REPORT.md | c4d3093fb58cb4911a4fd018bec53287a91db819e2f1609ea575865284f1dd87 |

I read the new report, producer, verifier, parent root formulas, and agent05's non-author root review. I also revisited the actual scalar preparation, pole, norm-valuation and doubled-point arguments in the pinned quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9. Relevant passages are the pole statement around lines 7720-7748, scalar preparation and continuity around 10520-10559, the scalar proof around 20263-20362, and the anchor/Lucas consumers around 20532-20596. The depth change is a new application checked here, not covered merely by the parent acceptance.

My read-only check_scalar24_review.py uses this reviewer's polynomial arithmetic and imports no author producer or checker. It passed the exact power-chain and norm-square meanings, all changed equations and outside consumers, full sum of squares, local threshold arithmetic and anchor margin. The result is 448 total rational variables, 425 quadratic residuals, and 6,542 quartic monomials.

## Local soundness, including both branches

The parent label beta=2X^2+2403 and positive r and c retain their reviewed meanings. At a consumed prime p>76176, c is a unit and an odd eta=v_p(r) is positive: if beta had negative valuation, all five factors would have that same valuation and eta=5v_p(beta)=10v_p(X) would be even; otherwise all factors are integral.

Put q=Norm(f(H)), z(R)/z(H)=z0+z1*rho. The new equations give

    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q^2)/r^32.

The retained nonzero pole input c*r*W^2 yields eta+2v_p(W)>0. Terms of each numerator have distinct valuation parity because eta is odd; zero terms may be assigned infinite valuation. Therefore

    v_p(B) > 63eta/4,
    v_p(q) > 61eta/4 > 0,
    v_p(z0) > 191eta/8,
    v_p(z1) > 187eta/8.

Since eta is a positive integer and rational coefficient valuations are integers, both last valuations are at least 24. This conclusion is not stated as 24eta, which the lower bounds do not uniformly imply and which is unnecessary.

The positive norm valuation supplies at least one place of K above p with positive valuation of f(H): the norm valuation is the sum at a split prime and twice the valuation at an inert prime. At that place H is formal. The two rational coefficient bounds imply v(z(R)/z(H))>=24, hence v(z(R))>0.

The latter condition permits R to be near O or near T0=(0,0). It is not replaced by an assumption that R itself is formal. With D a unit and p odd, the unchanged identities z(R)^2=x/(x^2-D) and x(2R)=(x^2+D)^2/[4x(x^2-D)] show in both cases that 2R is formal and v(z(2R))=v(z(R)). The case v(x)=0 cannot give v(z(R))>0. All denominators are nonzero on the retained nontorsion point domain. Applying the formal logarithm isometry to [h](2R)=[2s]H gives v_p(s/h)>=24; h is a nonzero integer, so v_p(s)>=24. The same radical M5(beta) is therefore proved to divide s to power 24.

## Height and actual anchor

The exponent-nineteen theorem now yields h(beta)<=H*|s|^(19/24), with exactly the same H<2^2093966. Write kappa=|s|. The retained anchor gives log2(kappa)>25165823.5. The exact rational check

    (5/24)*25165823.5 > 2093966+7

implies kappa^(5/24)>80H. Thus h(beta)<kappa/80<=|a|/40 for a=s+1, including negative s, since |a|>=kappa-1>=kappa/2. The independent retained inequality kappa>(80H)^10 still gives log(48H)<|a|/40.

Nothing changes in the order-40 argument forcing the Lucas polynomial to vanish. Its lower bound log Bmax>|a|-3 remains available. The order-10 input argument consequently still gives log Bmax<10log(48H)+19h(beta)<29|a|/40, a contradiction. The final beta-integrality argument remains valid. There is no increase in the anchor coefficient, exceptional prime set, or other test order.

## Global completeness and pole input

For an arbitrary integral X the parent simultaneous correction supplies positive integral cr, square at Q2,Q3,Q17. Let its finite prime support be S. The actual preparation theorem permits arbitrary finite coefficient-depth bounds over S, with a sufficiently deep positive shared index chosen first and the scalar index chosen deeper afterward, subject to the retained divisibility and anchor requirements.

At p dividing r, with eta=v_p(r)>0, require the coefficients of f(H) to have valuation at least 8eta and those of z(R)/z(H) at least 24eta. Then v_p(q)>=16eta, v_p(B)>=16eta, and v_p(W)>=0. At p dividing c but not r, positive valuations of these coefficients also make W integral because r is a unit. This holds at ramified and bad primes too: it uses the preparation's arbitrary-depth conclusion there, not the good-prime logarithm estimate used for soundness.

The norm q is nonzero because f(H) is a nonzero field element. Since r>0, the new W is strictly positive. Thus c*r*W^2 is nonzero and positive. Its valuation on S is nonnegative, and its valuation outside S is even. Its reduced denominator is a square, and its local squareclasses at 2,3,17 agree with cr. These are precisely the existing pole-completeness hypotheses. No claim that W is a unit is needed. The new rational functions are continuous on the existing nonzero domains; the required finite bounds therefore persist in a congruence class of the shared index. Choosing that modulus before the contact primes retains the original order of global choices.

## Physical circuit and consumers

The literal remaining power equations give coordinates 600,...,604 the values r^2,r^4,r^8,r^16,r^32. The independent check expands the actual affine expression for r and matches the first square, then checks each further square. Coordinate 605 and the r^64 equation are removed.

The shared coordinates 311 and 312 have the exact meanings t=f0^2+2f1^2 and u=f0*f1 for f(H)=f0+f1*rho. Their stored normalization was checked directly. Hence t^2-8u^2=(f0^2-2f1^2)^2=q^2. Coordinate 541 is changed from B^2 to this Q=q^2. The three new rows literally give Q=t^2-8u^2, r32*B=z0^2+r*z1^2, and r32*W=B^2+r*Q. The existing z1-square row remains.

Only the declared old rows consume the deleted 605 or the old meaning of 541. Every other residual object is identical; every other retained coordinate object is identical. In particular the actual scalar pole input still consumes coordinate 542 as W, so the proof above analyzes the new value that is truly used downstream. This review accepts the frozen component, not an unverified composition onto a later count.
