# Composition of accepted327 and accepted359

Author: `/root/astra_quartic_opt10_combination`. This combines independently accepted components. The resulting composition still requires a non-author review. It has **320 total variables**, **319 witnesses**, **290 quadratic residuals**, and **5,659 quartic monomials**. Degree is four, content is one, and maximum coefficient is `16*3^(2^26)`. Earlier candidates and all released files are unchanged.

## Exact dependencies

Component and review paths below start at `work/quartic-optimization-20261107`. The common366 source is under `work/quartic-under300-20261107/01-elimination/s-odd366`.

| Artifact | SHA256 |
|---|---|
| Common source366 IR | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| `resume-depth-20261107/chain327/candidate327-ir.json` | `d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665` |
| `resume-sol-review327-20261107/REVIEW.md` | `f007b843603b9c15c52f0c3f6aad3e8b203f26e596679f9a255c4fcecc17f57b` |
| `resume-sol-review330-20261107/REVIEW.md` | `0a2774c9debd513a5ee7f9591c1eb8e2c6ad83ee23e04d84307b47e42d0043c1` |
| `resume-elimination-20261107/abscissa359/candidate359-ir.json` | `282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1` |
| `resume-review359-20261107/REVIEW.md` | `6956155cc4878f0c36f5e1159330f043d473cc8fd4ba421f2ec484dc4083655c` |
| `candidate320-ir.json` | `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f` |
| `polynomial320.json` | `64510d25d7cd7daacf811bca59a5c4147d9f1f780f579c6be89034ff99f5d676` |

The reviewed327 chain preserves the detector functions of accepted330 by a rational change of private helpers. The reviewed359 anchor uses actual root abscissa coefficients, replacing362's inverse-coefficient gates. Those are the selected versions. Neither an old E38 value nor an old inverse-root value is silently retained under a repurposed name.

## Complete finite transport

For every coordinate and residual object, the checker computes the exact changes from common366. The327 and359 changed-object sets are disjoint. New IDs820..834 and903..904 do not collide. The constructor uses the changed object from its one component and otherwise preserves the source object. It rejects overlapping modifications, unexpected metadata changes, or mismatched source hashes.

The anchor changes row504, adds903/904, and removes the nine private A/T/Z odd-chart rows and variables. The detector does not consume any of those removed variables. The new Q is exactly `48*v83^2+48*v87^2+432*v89^2`, using the actual abscissa rho coefficients twice those slots. B is exactly `2*g1+C*Q*tau`. All scalar subtraction and g0 inverse rows remain unchanged.

The detector's private E11/E39 coordinates and deleted E3 slots retain their327 meanings. Every old/new consumer is accounted for by the complete map. All shared test powers, four sums, multiplication outputs, norm and bounded-B rows are unchanged from327. `verify.py` imports no producer and checks every resulting coordinate occurrence and every SOS coefficient.

## Root restoration precedes detector use

The359 local parity proof starts with the root square-abscissa charts and scalar point, independently of H, a detector inequality or a root-height conclusion. These inputs remain literal359 rows here. The quaternion criterion makes `F_s/C+Q` integral at3. The three summands have valuations in disjoint classes `2Z`, `1+4Z`, `3+4Z`, so none can hide a negative valuation by cancellation. The abscissa coefficient lemma then forces A,T,Z to have odd labels, and the scalar term restores the old anchor condition. The2-adic hypothesis needed for that restoration follows from the unchanged scalar source.

Half-chart restoration may require the A,T,Z sign involutions from359. The checker applies each complete sign set to every monomial of every combined row. Each row is invariant or changes by an overall minus sign. These actions fix actual root points, their abscissa coefficients, Q, B, input, all newly shared powers and the detector outputs. Thus the restored root domain and anchor coexist with the new detector.

The accepted330 argument, transported through327's exact chain, can now use the root-height/anchor contradiction to exclude pre-H exceptional branches. Its strong H slot has valuation multiplicity four before those exclusions through the separately reviewed Kummer-to-curve identity and fixed-unit branch analysis. The four groups provide the required tests at one common place. Their original high and middle orders, all logarithm consumers, the scalar24 estimate and the final input bridge are unchanged. This order avoids using a height theorem to prove a parity condition required by that theorem.

## Completeness and simultaneous choices

Take the accepted327 completeness witness. Its strong H slot uses the reviewed Pi^39 primary progression. The new chain has exactly the same E2/E4/E8/E19/E79/E158 outputs as330, including the real and local domains. The finite and real construction already supplies all scalar and detector pole witnesses for one H.

The359 forward map is applied afterward. The odd roots have3-adic-unit abscissa rho coefficients and2-adic valuation minus one. Hence Q is integral at2 and3, and the new quaternion parameter is integral there. Choose its private anchor witnesses, set Q and B, and forget the old odd-chart coordinates. Every nonprivate327 value remains fixed.

Q depends only on the already fixed roots. The private quaternion representation adds no congruence on h or h-1, no condition on the selected contact primes, and no bound on the real position of H. It preserves the Pi^39 progression, all cached powers, every trace and bounded B value, and the scalar preparation. Thus the order of all existing completeness choices is unchanged.

## Verification and scope

Full transport, all three sign actions, no dangling variables, quadratic degree and the entire primitive SOS pass. The two C-squared coefficients are16 and1; C-linear coefficients are bounded by96, and constant coefficients have fewer than2048 bits. Distinct C powers cause no monomial collision. No giant decimal expansion is used.

Independent component approvals are inputs to this report, not automatic approval of its composition. A non-author must review these actual interfaces and frozen320 files. There is no ordinary companion or publication claim. The next publication threshold remains strictly below300 total variables.
