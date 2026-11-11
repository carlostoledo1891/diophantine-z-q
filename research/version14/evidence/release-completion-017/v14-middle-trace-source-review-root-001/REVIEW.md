# Independent review of three trace applications

Reviewer: /root. Author: /root/v14_gi_constructors. Date: 2026-11-09T08:45:38.775Z.

Decision: accept the three exact source applications in manifest 0d2801e2493288bd3639937b4e40e3f55cac17a195ea83ab1eea9ffb183cb242. This is an internal mathematical review of those applications, not complete manuscript approval.

## Material actually read

Current manuscript lines 9090–9172 and 10708–10750, whole-file SHA256 1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8. Read the final published Koenigsmann PDF, printed pages 75–78, including Definition 4, Observation 5, Proposition 6, its local Facts (a), (b), (c), (e), and the displayed U2 and U3 computations. PDF SHA256 f26c2e155d025978045a0c68073505631677624ef4d6f9b461640c6fbe1d3c93. The primary PDF was read directly, not inferred from the author's extracted text or verdict.

## Trace sum and conventions

The source's reduced trace is twice the scalar coordinate, and its norm for parameters (2,3) is x0²−2x1²−3x2²+6x3². Definition 4 uses T=S+S with no finite additive offset. Substituting the second scalar coordinate (t−2u0)/2 and multiplying its norm equation by four gives exactly the second equation at lines9103–9104 and9142–9144. Division by two is legal in Q; the formula has exactly seven independent witnesses.

Observation 5 explicitly lists (2,3) as ramified at2. At3, the odd valuation of3 and the nonsquare residue2 give ramification. At every other odd prime both parameters are units, and the positive real parameters give splitting. Proposition 6 therefore yields exactly Z_(2) intersection Z_(3). The real interval in its general statement imposes no restriction here. Both repeated applications use the same conventions.

## Single trace and the four-witness anchor

This step needs Facts (a), (b), (c), (e), rather than the trace-sum proposition alone. At a ramified place, a trace is integral. If m=min(v_p(a),v_p(b))<0, the square sum has valuation2m at3: equal leading valuations cannot cancel because −1 is nonsquare modulo3. At2, unequal valuations give2m; equal finite valuations give2m+1 because two odd squares sum to2 modulo8. Thus 3(a²+b²) has negative valuation at the offending place and cannot cancel9. This proves necessity, including a zero coordinate via infinite valuation.

Conversely integral a,b give h=9+3(a²+b²) congruent0 modulo3. At2, square residues show that h is odd or divisible by4. The odd case belongs to the inverse image of U2={1}; the3-adic value belongs to the inverse image of U3={0}. For h in4Z2, put x0=h/2. If x0 is2 modulo4, then (x0²−1)/3 is1 modulo8, and a square root v gives x0²−3v²=1. If x0 is0 modulo4, then x0²/6 lies in8Z2; a square root w of1−x0²/6 gives x0²−2−3+6w²=1. The elementary square criterion for2-adic units supplies these roots. All other places split. Fact (e) supplies a rational norm-one element with trace h.

For the displayed homogeneous anchor, C is a fixed nonzero integer. Dividing its first equation by C² gives H/C=9+3((f0/C)²+(f1/C)²). Dividing the second by4C² is the norm equation with scalar H/(2C), and other coordinates U/C,V/C,Wa/C. Conversely multiply rational witnesses by C. This establishes equality of existential projections without asserting a rational witness-selection function.

## Scope

Accepted rows: MIDDLE-TRACE-SUM-DEFINITION, MIDDLE-TRACE-SUM-CONVENTION, MIDDLE-FOUR-WITNESS-SINGLE-TRACE. The surrounding group, height, subgroup and anchor-size claims are not reviewed here. No manuscript repair is needed for these three applications. The source's cited quadratic-form input is being used as part of its published local facts, not claimed newly proved in this review.
