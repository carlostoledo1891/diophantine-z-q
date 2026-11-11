# Independent review of the one-correction quadratic input

Reviewer: agent03. Arithmetic author: root. Implementation author: agent06. I accept the frozen arithmetic proposal and its 448-to-444 implementation on the inherited source inputs. I found no missing parity, local-squareclass, denominator, size, or global-choice premise. This is a non-author review; neither the root author's calculations nor the implementation author's finite checks are used as substitutes for the argument below.

## Frozen scope

| Artifact | SHA-256 |
| --- | --- |
| 00-root/one-correction/PROPOSAL.md | 495ffb791c149bb6b2ee6fa1f4988aa8583fea383efd0e4197436fe6bab2b9a6 |
| 06-product/scalar-redesign/depth24-448/candidate448-ir.json | e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609 |
| one-correction444/candidate444-ir.json | c2c60a1bed5c929eb633b654e76d401dc96fc0edd1f09eee44324740c4cde837 |
| one-correction444/polynomial444.json | aaa5dfeec88403654211b4c1b5fb9284dc1d87908fc6987d4864ea015b1951f2 |
| one-correction444/REPORT.md | 1a5568d11183cdaf56191a11d0343559820acc521b405040a4b23268487dc3ae |
| one-correction444/MANIFEST.json | 1547b0f0d3c62b8757c0c96e450bc266fc29cef4df4d7e8485f566779225c251 |

The last four paths are under 06-product/scalar-redesign. All manifest file pins matched. I read the frozen proposal, implementation report and source, consumer inventory, relevant predecessor proofs, and actual retained-source passages. The source manuscript is quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9. Relevant applications are the odd chart at lines 19527-19581; the label identification and height/Lucas conclusions around 19626-19645 and 20556-20596; scalar preparation at 10520-10559; and the reduced scalar proof and pole application at 20263-20362. The scalar depth-24 replacement was separately reviewed in review-scalar24.md and its exact source hash is the input above.

My independent scripts check_one_correction_local.py and check_one_correction_transport.py passed. The latter checks every changed and unchanged row and coordinate, the full consumer incidence, and every coefficient of the sum of squares. It records 444 total rational variables, 421 quadratic residuals and 6,668 quartic monomials in one-correction-transport-checks.json. The fixed C=3^(2^25), degree four, content one and maximum coefficient 16*C^2 are retained. No giant integer was expanded.

## Input bridge and retained oddness

Write tau=2X+1 for the proposal's input expression, to distinguish it from the Lucas label also traditionally called t. The new label is

    beta=51*tau^2+2504=204X^2+204X+2555.

For every rational X, beta>=2504. It lies strictly beyond all five real contact roots 0,1,2401,-343/32,1/2. Therefore the unchanged contact polynomial r is positive and nonzero. If X is integral, tau is odd and beta is positive and odd. In particular beta supplies an allowed odd root index; no restriction on the sign of tau is imposed.

For the reverse implication one must use the retained conclusion that n is odd, not just that beta is integral. Suppose n=beta with n an odd integer. Write tau=u/v in lowest terms, v>0. Then v^2 divides 51u^2, hence divides 51. As 51=3*17 is squarefree, v=1. Now 51*tau^2=n-2504 is odd, so tau is odd and X=(tau-1)/2 is integral. This covers negative tau and excludes tau=0. Integrality alone would fail: X=-1/2 gives beta=2504, an even integer. The proposal explicitly uses oddness at the correct final step.

The implementation leaves all A odd-chart equations unchanged. The source identifies A=[n]P and its augmentation supplies odd n by the existing squareclass proof. The new code changes no point equation, root designation, or quantified field. Thus the parity premise used by the bridge is actually available.

At any consumed prime p>76176, 51 is a unit. If v_p(beta)<0, then v_p(beta)=2v_p(tau) is even. This assertion need not hold at 3 or 17 and is not used there. The contact-valuation argument only consumes it above the stated cutoff. This checks the exact prime domain rather than incorrectly extending the old coefficient-2 assertion to every odd prime.

## Exact simultaneous local correction

Assume X is integral, so tau is odd. Then tau^2=1 modulo 8 and beta=3 modulo 8. Write beta=8k+3. Both beta-1 and beta-2401 have valuation one at 2. Their odd parts are 4k+1 and 4k-1199, congruent modulo 8; their product is an odd square, hence 1 modulo 8. The other factors have residues 3,7,5 with product 1 modulo 8. Thus v2(r)=2 and r/4=1 modulo 8. The contact product is a square in Q2.

At 3, beta=2 modulo 3. The residues of its first four contact factors are 2,1,1,2, whose product is 1. The remaining factor satisfies

    (2beta-1)/3=34*tau^2+1669=1+tau^2 modulo 3.

This is 1 when 3 divides tau and 2 otherwise, so it never vanishes. Consequently v3(r)=1 exactly, with the stated two possible unit classes. This computation does not assume that beta has a fixed residue modulo 9.

At 17, beta=5 and the contact residues are 5,4,1,10,9. Their product is 15, which equals 7^2 modulo 17. No factor vanishes. Hence r is a square unit in Q17.

Both candidate corrections are 1 modulo 8, hence square units at 2. At 17, 33 has residue 16 and 33033 has residue 2, both nonzero squares. At 3, both have valuation one; the unit parts are 11=2 and 11011=1 modulo 3. Choose c=33033 when 3 divides tau and c=33 otherwise. Then v3(cr)=2 and its unit is a square. This one rational integer c therefore makes cr square at all three local fields simultaneously. The argument covers all integral X; the finite residue checks only corroborate these formulas.

The binary equation (c-33)(c-33033)=0 over Q has exactly these two roots. Both are positive, nonzero, and supported on primes 3,7,11,13. Thus c is a unit at every consumed prime. No extra sign selector or local witness is being suppressed.

## Scalar, height, and completeness applications

The scalar soundness proof uses positive nonzero r, odd positive contact valuation at consumed primes, and a unit correction there. These premises were checked above. It still proves M5(beta)^24 divides the scalar index s and h(beta)<=H*|s|^(19/24), with the same H. The doubled-R step still treats both the formal branch and the branch near (0,0); no part of that argument depends on the coefficient 2 in the old label. The field, norm map, ratio functions, and point domains are unchanged.

The actual anchor inequality (5/24)*25165823.5>2093966+7 is unchanged. Thus h(beta)<|a|/40 and log(48H)<|a|/40 still hold. The high-order Lucas proof gives F=0 and log B>|a|-3, while the order-10 input comparison gives the contradictory bound log B<29|a|/40 unless n=beta. Applying the parity-sensitive bridge above completes soundness. The height theorem is applied directly to the new rational beta outside its contact set; no extra factor or height constant is needed for its expression in X.

For completeness, fix any integer X and choose c as above before making the elliptic choices. The integer cr is positive and square at 2,3,17. The inherited preparation allows arbitrary finite support and arbitrary finite depth bounds there. It requires these properties of cr, not the former five-generator representation of c. Choose the shared index sufficiently deep, then the scalar index deeper with the same anchor and congruence conditions. The depth24 proof makes its new root W positive and integral at every prime on the support of cr. Hence crW^2 is positive, has square reduced denominator, and has the required three local squareclasses. The existing pole theorem supplies fresh witnesses for this actual input.

The four root labels are then positive and odd, with n=beta. The scales and continuity modulus are fixed before the contact primes, and the same prime-selection, CRT, and real-progression arguments apply. Changing the finite value of n or the finite support of cr does not change their quantified domains. No new local-global or simultaneous-realization assumption is needed.

## Literal implementation and outside consumers

The source input appears only in Y=X^2, with IDs X=0 and Y=248. All other dependence is through Y. The new code leaves that equation unchanged and substitutes Y -> 102Y+102X+76 in every other Y consumer. Therefore the old beta=2Y+2403 becomes exactly the desired quadratic label. The substitution is affine in stored coordinates, so every residual remains quadratic.

I independently reconstructed this substitution with a multinomial expansion. It matches all fourteen changed rows, including the two direct beta-test components, the scalar contact expressions, the retained power-chain and norm rows, and all grouped low-order detector consumers. Every other non-correction residual object is identical. The inventory's fifteen Y consumers include the unchanged input equation.

Correction coordinates 61 through 64 are deleted; they have no outside consumer. Coordinate 65 retains the unscaled semantic value c and now obeys c^2-33066c+1090089=0. Its actual corrected-product and scalar pole-input consumers remain attached to that value after the beta substitution. Every other retained coordinate object is unchanged. No rescaled-correction optimization is included or accepted by this report.

The new input map is a substantive replacement, not a rational bijection of old input labels or a claimed square root of an old expression. Acceptance is for the exact arithmetic and implementation hashes above. A later combined candidate must repeat the consumer transport check against its own current equations.
