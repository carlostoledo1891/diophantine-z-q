# Shorter power chains in the combined construction

Author: `/root/astra_quartic_opt10_combination`. This frozen candidate has 315 total variables, 314 witnesses, 285 quadratic residuals and 5729 quartic monomials. Its 5732 coefficient-power entries include three collisions after fixing C. The exact maximum coefficient is 186624*3^(2^26)+64. This packet is provisional. At freeze, the immediate318 composition and the323 chain component await their respective independent reviews. No released file is changed.

## Exact sources

The immediate source is `../combined318/candidate318-ir.json`, SHA e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1. Its report is SHA f2d8941c6a18369b956ab63e96328217e684590e1b2dfb8df557fcf1cba0fe19. That report records the complete route through accepted326 and359, the residual-label collision, and the exact private-anchor unscaling. Its count and coefficient corrections remain relevant here.

The new component is `work/quartic-optimization-20261107/resume-depth-20261107/chain323/candidate323-ir.json`, SHA dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd. Its report SHA is 828cd7cfb7649b1e93cb3fbe22d1d5dc50f7d8ed1b71c20242b3634029417b15. The certificate pins its source326, SHA 48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84.

## Changed coordinates and equations

The constructor computes all changes between326 and323 and checks that each changed source object is identical in the immediate318 candidate before transplanting it. Delete E2 coordinates361,409,457 and defining rows313,363,413. Repurpose coordinates355,403,451 from E11 to R cubed. Only rows544,546,550,552,556,558,745,760,775 change. All other coordinate and residual objects are byte-equivalent apart from the final status text.

For each detector, the retained RE=1 gives nonzero R and E. The new sequence is

    E*J=R^2, A*J=E, B=A^2, Q*J=B^2,
    L*R=Q^2, M*R=L^2, N=M^2, P=R*N.

It uniquely forces J=R^3, A=E^4, B=E^8, Q=E^19, L=E^39, M=E^79, N=E^158 and P=E^157. Every division is by R, E or J, each already proved nonzero. These are assignments from known values; no square-root branch is introduced.

In the forward map, discard the old E2 and replace E11 by R^3. All other coordinates stay fixed. In the reverse map, restore E2=E^2 and E11=E^11. The sequential equations prove that the retained outputs then satisfy the old chain. Hence both maps preserve every point, label, cached test, group value, W, trace/pole value and scalar witness, not just the input.

The checker derives each physical affine R independently from the literal retained RE=1 equation and expands R^2 itself. It compares all nine changed residuals to the displayed identities. It checks every occurrence of the repurposed J slots and the absence of every deleted E2 slot. There is no free cached power or silent use of the historical E38 meaning.

## Composition interfaces

The anchor remains exactly the unscaled318 anchor with T=2*g0*g1+C*q. Its residual1903, quaternion residual504 and guard732 are unchanged. The detector's unrelated shared-square residuals903 and904 also remain unchanged. Thus the previous residual-label collision cannot delete or replace an equation during this step. The coordinate named903 remains the anchor T, as before.

Every arithmetic function consumed by the three-group proof is fixed by these maps. The pre-H valuation cases, exceptional-branch height contradiction, root parity restoration, common successful place and scalar24 argument therefore receive identical values. Completeness uses the same original Pi^19 progression and the same ordered finite and real choices. The new helper values are assigned afterward and require no new congruence, sign or bound.

All three root restoration sign actions are checked again on every final residual. They fix R and its powers, so they commute with the chain replacement. The exact private-anchor map also fixes R and its powers. No interaction between the two private changes is assumed merely from disjoint names; their complete consumer sets and unchanged arithmetic outputs are checked.

## Finite verification and limits

`verify.py` imports no producer or component verifier. It checks the complete source delta, every final object, all repurposed consumers, the physical R equations, successive exponent recovery and all primitive residual squares. It finds all315 variables active, quadratic residual degree, quartic final degree and integer content one. The three collided coefficients are counted as three monomials rather than six power entries.

The coefficient of v89^4 remains 186624*C^2+64. Every other C-squared leading coefficient is smaller, every C-linear coefficient has absolute value at most1728, and C-independent coefficients have fewer than2048 bits. Since C=3^(2^25)>2^2048, the maximum stated above follows without expanding C.

Independent acceptance of the immediate318 composition, the standalone323 component, and this final transport must remain separately recorded. This report claims no ordinary companion, no global circuit optimality and no publication. The next publication threshold is strictly fewer than300 variables.

candidate315-ir.json: `d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8`.

polynomial315.json: `2e8879814484a8c838c700215d21c7c625f9b0569a5fa4d2e5e23d5c05055fd1`.

build.py: `09f6cbb04977669f87a4c759793f64cd3333f870c03cbbb2d869da4b9909d612`.

verify.py: `79f4cc64f70bed24d548d3bb62eca7b97a1efbd6ba86524e109afb0b10540742`.

CERTIFICATE.json: `8ad061eeab957355a94607e910513ed73b4ca66bc0c90e4a00f0a05c6f0d8b01`.

VERIFICATION.json: `7816dda6e8b54030c50172997e64601ec1bf5d753468960e54bfecb3731dddd6`.
