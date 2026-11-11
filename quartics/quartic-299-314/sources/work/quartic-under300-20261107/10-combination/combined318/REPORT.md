# Three-group detector with exact unscaled anchor: 318 variables

Author: `/root/astra_quartic_opt10_combination`. This is a provisional composition with318 total variables,317 witnesses,288 quadratic residuals and5676 quartic monomials. There are5679 coefficient-power entries because three ordinary monomials have both constant and C-squared coefficients. The exact maximum coefficient is186624*3^(2^26)+64. All earlier artifacts are preserved. The next publication threshold remains strictly below300 variables.

## Source and review boundaries

The immediate source is `../three-anchor319/candidate319-ir.json`, SHA61898500a23024afbf21aed5a35ee0b573beef0dcaa598caba07de884c4281f4. Its report SHA isb7e0d302925dc9f9313d57ff6ced152cb683bde13e05b721c414f2b9d02b42ee. That packet combines independently accepted detector326 and anchor359; its whole-composition review is pending at this freeze. Read its full source and review pins and its Pi^19/root-restoration argument as part of this packet.

The transported component is `work/quartic-optimization-20261107/resume-elimination-20261107/exact319/candidate319-ir.json`, SHA847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676. Its report SHA is2cd2a61828a8d3dd34a73ff00079d192bb2619856fdcfba34373a95302bbc2a8. It descends from accepted320, SHAd1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f. Independent component review was pending at this freeze. Neither this report nor the finite checks claim that pending reviews have occurred.

The new exact component is an alternative to the independently accepted squared-g1 anchor358. Only the exact component is used here. No squared-g1 substitution, new local valuation lemma, or exact scalar-index valuation is used.

## Exact physical map and residual labels

Write g0=v543, g1=v544, tau=v549 and q=48*v83^2+48*v87^2+432*v89^2. The source's only private-anchor equations are Q=q, B=2*g1+C*Q*tau and U^2+6V^2-2W^2-4C*tau*W-3B^2=0. They are residuals1903,1904,504 in the immediate source. The retained guard is residual732, g0*tau=1.

Replace them by T=2*g0*g1+C*q and u^2+6v^2-2w^2-4C*w-3T^2=0. Store T at coordinate903 and u,v,w at55,56,57; delete coordinate904. Keep residual1903 for the T definition and504 for the anchor; delete residual1904.

The source326 detector also has residuals903 and904. Those are shared-square definitions and remain byte-identical. The administrative map from component row903 to1903 and904 to1904 acts only on residual labels. It never changes coordinate903 in a monomial. The constructor verifies the entire old source object at every transported destination before replacing it. The checker reconstructs every final object independently and checks every residual appears once. The certificate records all component-to-destination labels explicitly.

From an old solution set u=g0*U, v=g0*V, w=g0*W, T=g0*B. Conversely set Q=q, B=tau*T, U=tau*u, V=tau*v, W=tau*w. Keep every nonprivate variable. These maps are mutual inverses using only the retained guard. With G=g0*tau-1, RQ,RB,RA the old residual polynomials, and NT,NA the new ones, the checker proves all five unconditional polynomial identities:

    forward(NT)=g0*RB+C*RQ+C*Q*G
    forward(NA)=g0^2*RA+4*C*g0*W*G
    reverse(RQ)=0
    reverse(RB)=tau*NT+2*g1*G
    reverse(RA)=tau^2*NA.

The complete private-consumer scan finds exactly rows504/1903/1904 before and504/1903 after. Thus no hidden detector, logarithm, point, power or scalar consumer changes. The maps remain valid for all zero values of private witnesses; only g0 is divided by, and its existing inverse remains present.

## Whole proof interface and completeness

The previous319 composition restores odd root charts before invoking the three-group detector's pre-H height argument. Its checker verifies the three complete root-sign actions on every residual. This checker repeats those actions on the final318 system. The exact unscaling fixes all actual roots and scalar data. It therefore carries that restoration and the same old quaternion parameter through the new coordinates.

Every detector group, E-power cache, norm/pole equation, primary and alternate log consumer is byte-identical to the immediate source. The pre-H even-valuation proof and exceptional-branch exclusion retain all their hypotheses. The three-group326 proof supplies the original Pi^19 completeness progression, the actual G2 precision12 and all required positive contact margins. It chooses its finite and real neighborhoods before contact primes. Anchor359 then chooses only private quaternion witnesses. The present forward map is applied last and changes no nonprivate quantity at all. It adds no congruence, sign, local divisibility or real-size condition. Thus the entire ordered completeness construction is unchanged.

## Finite result and coefficient bound

`verify.py` imports neither producer nor component verifier. It pins the three IR inputs and final table, checks every transported/unchanged object, all private consumers, the five exact map identities, the root-sign actions and all288 primitive residual squares. All318 variables occur. Degree is four and a coefficient1 remains, so content is one.

The coefficient of v89^4 is186624*C^2+64. The v83^4 andv87^4 coefficients are2304*C^2+64. Every other C-squared leading coefficient has strictly smaller absolute value than186624, every C-linear coefficient is at most1728 in absolute value, and C-independent coefficients have fewer than2048 bits. Since C=3^(2^25)>2^2048, the displayed coefficient is the exact maximum. The checker groups equal ordinary monomials before counting; it does not mistake5679 power entries for5679 monomials. No giant decimal expansion is performed.

No ordinary companion or independent whole-composition acceptance is claimed. Final review should bind these frozen files and the earlier319 composition, including the residual-label collision resolution.

candidate318-ir.json: `e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1`.

polynomial318.json: `664a1c0460a2b01c5b5162f3af3c9dfbd2afc6a90ed3e9d2a88d95eae5561fac`.

build.py: `b0a69ea37588bbd5f82cd3bc73a3792ea90655596339dc3dd2841172b71482ad`.

verify.py: `28686a04df1382ccba610215ca56e941d6813f40f3d2fecb0bcef822171557eb`.

CERTIFICATE.json: `29d33828a13a71122f790a103e8195361c6b6429fcacca274fc9ff97e4631067`.

VERIFICATION.json: `a4280a80c5504fb2e5fb5aefb1fe91074784fd9a07ba9d8959084af4a3705212`.
