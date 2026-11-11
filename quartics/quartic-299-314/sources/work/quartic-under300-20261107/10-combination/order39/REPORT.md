# Order 39 alternative: algebra and numerical margin

This is a proposal, not an accepted candidate or a whole-system verification. It is an alternative to the cached-eighth-power packing that preserves order 40. The two three-coordinate savings are not additive with the circuits presently known.

Start from the provisional mixed348 circuit. For each detector retain E, R=E^-1, E2, E3, E4, E7 and the square of q10. Delete the old auxiliary R3, and repurpose the old E8 coordinate as E9. Replace the four old chain equations by

    E9 = E7*E2,
    R*q10 = E9^2,
    q10Square = q10^2,
    R*q39 = q10Square^2.

The third equation was already retained. Since ER=1, these force E9=E^9, q10=E^19 and q39=E^77. Retained q40 square/cube slots can be renamed q39 square/cube and then have exponents 154 and 231. Every high-order coefficient/evaluation consumer must be relabeled and semantically rechecked; its polynomial form is unchanged. Low groups still use E4 and E7. This deletes one rational auxiliary coordinate and its defining row per detector. The proposed total is 345, before any other unrelated component.

The mixed348 source has q10=E^19 and q40=E^79. Its old R3 appears only in four old chain equations (its own definition, E8, q10 and q40), and E8 appears only in two of those equations. Those four rows are replaced by the three new defining rows above; q10Square is retained. This finite incidence claim is checked against the pinned source by check.py. No global division other than the already retained ER=1 is used in the replacement chain.

The order-40 rational-log error continues to suffice for an order-39 comparison. At a consumed contact prime, the new high factor has weight E^77=R^(1-2*39); the same trace/pole bound forces test valuation at least 39. The two order-10 tests, the low formality tests, scalar order24, the root-height theorem, and the pre-H exceptional-branch exclusion keep their existing interfaces. Completeness can keep the stronger old order-40 point neighborhoods.

The first Lucas height contradiction needs a larger anchor. With |F|<5B^4 and all radicals dividing F to order39, the existing root-height inequality gives

    B^(2/39) < 7*H*5^(19/39)+6 < 24*H.

The last inequality follows from H>=1, 5^(19/39)<sqrt(5)<16/7, and 16+6<24. Hence a nonzero F would imply

    log2 B < (39/2)*(5+2093966) = 40832434.5.

For the current ternary anchor, increasing its fixed coefficient C from 3^(2^25) to 3^(2^26) gives v3(s)>=2^25-1. Since s is nonzero even and log2(3)>3/2,

    log2 |s| > 1+(3/2)*(2^25-1) = 50331647.5.

As B>=|a|>=|s|/2, log2 B>50331646.5, contradicting the preceding bound. The scalar order24 margin also holds, more strongly:

    (5/24)*50331647.5 > 2093966+7.

Thus h(beta)<|a|/40 and the final order10 comparison retain their prior numerical bounds. Changing this fixed C adds no symbolic coordinate but changes the symbolic coefficient bound and adds one squaring to the current ordinary constant-chain realization. This proposed anchor adjustment has not been composed with the pending positive-anchor365; that alternative would need its own depth/count calculation.

Source: mixed348 IR SHA256 4782ed265f5d3c2d2241ea73445af5b1465f28a7580d634b825bd9d11710f22c. Mathematical source passages: manuscript quartic_v13.tex equations (v13-height), (v13-anchor), Version9 first Lucas height contradiction, and the scalar24 margin. The proof above is not a claim that a frozen order39 IR has been generated or independently reviewed.
