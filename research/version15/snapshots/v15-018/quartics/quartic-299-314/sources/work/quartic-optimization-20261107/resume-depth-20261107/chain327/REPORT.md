# A two-auxiliary weight chain: 327 variables

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. This is a separately reviewable algebraic component on the pending330 construction. It removes three total rational coordinates and leaves every detector function, local order, pole, root and scalar predicate unchanged. The result has327 total variables,326 existential witnesses,297 quadratic residuals and5770 quartic monomials. Independent acceptance of the330 arithmetic and this exact component is still required. No release or prior frozen packet was edited.

## Exact bindings

| Object | SHA-256 |
|---|---|
| Source `../strong-h330/candidate330-ir.json` | `41602bf9d25d52ae6e461f958eb21e1d752190ef71a72c1cc7c444f4e0a9fff6` |
| Source `../strong-h330/REPORT.md` | `a90fe9b838dba89e77ee54672c42fbc60b669924032ccfc780bc2e531fef90b8` |
| `candidate327-ir.json` | `d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665` |
| `polynomial327.json` | `884e02a0d5b3c2bc8179e7911a77375ed3871c7f353adc14339549a95cf6fe49` |

## Why the earlier fixed-interface bound does not apply

The four-group detector already needs the scalar output E4=E^4 for its low-order terms. It no longer needs E38=E^38 as an evaluation weight. The older fixed-interface Laurent-chain searches did not have this pair of input/output conditions. This component uses those actual changed consumers; it is not a contradiction of their scoped lower bound.

Keep R*E=1, E2=E² and E4=E2². Replace the remaining chain by

    E8=E4²,
    E11*E=E8*E4,
    E19=E11*E8,
    E39*R=E19²,
    E79*R=E39²,
    E158=E79².

Every equation is quadratic because R is the same affine expression in the stored contact-polynomial coordinates. Only E11 and E39 are auxiliary scalar powers. The required detector outputs are E,E2,E4,E8,E19,E79,E158.

## Both maps and all nonzero domains

The retained equation R*E=1 forces both R and E nonzero for every rational solution, regardless of sign. Starting with E2 and E4, the new equations solve successively and uniquely to

    E8=E^8, E11=E^11, E19=E^19,
    E39=E^39, E79=E^79, E158=E^158.

At each division the divisor is E or R, already nonzero. This introduces no square-root branch, positivity premise, zero denominator, or restriction on the input.

From an old330 solution, keep every required output and every outside coordinate, assign E11=E^11 and E39=E^39, and forget E3. This gives a new solution. Conversely, from any new solution restore the old helpers E3=E³, c=R³, and E38=E^38. The old relations

    E*c=R², c*E8=E2*E3,
    c*E19=E8², c*E79=E38²

all follow by exponent arithmetic and R=E^-1. The old square equations hold too. This reconstructs an old330 solution while preserving every detector output and every outside coordinate. The two changes of helper values are explicit, not claims that repurposed source IDs keep their old meanings.

## Literal coordinate incidence

For detectors0,1,2 respectively, repurpose c at355/403/451 as E11 and the old E38 at369/417/465 as E39. Remove E3 at362/410/458. Keep E8 at356/404/452, E19 at359/407/455, E79 at360/408/456, E158 at374/422/470, and E4 at832/833/834. The retained E2 positions are361/409/457.

Exactly five rows per detector change, and the three E3 definition rows314/364/414 are deleted. The checker verifies that every old and new occurrence of the repurposed coordinates lies in those changed/deleted rows. In particular, no middle-product evaluation still consumes the old E38 value. All other rows remain byte-for-byte the corresponding source objects, including the four detector sums and both norm/pole equations. The complete coordinate count is330-3=327, not a saving added to an incompatible older detector.

## Verification and mathematical scope

Run `python -B verify327.py` here. The checker imports no producer. It derives R from each retained E*R=1 row, writes the five expected replacement equations independently, checks all deleted and repurposed incidences and metadata, verifies the sequential exact exponent identities, and expands every primitive residual square by an independent upper-triangular accumulation. All5770 coefficients match. The quartic has degree four and integer content one. No changed row contains the huge fixed constant C, and the unchanged anchor still supplies the maximum16C².

This component is a rational equivalence of complete solution sets after changing private helpers. It makes no new arithmetic application. The local/common-place proof, stronger Pi39 completeness choice, scalar24 bounds, root parity and inherited source qualifications remain exactly those of330. That arithmetic packet is still pending independent review; this finite equivalence cannot supply its missing acceptance. The strict below300 publication threshold is not yet reached.
