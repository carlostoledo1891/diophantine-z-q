# A shorter exact scalar chain: 323 variables

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. Independent review of this component is pending. The candidate has 323 total rational variables, 322 witnesses, 293 quadratic residuals and 5840 quartic monomials. It removes one private scalar coordinate from each detector of accepted326. This is an exact equivalence after changing private helpers; it changes no arithmetic predicate, valuation class, completeness choice, point, label, or detector output.

## Frozen source and result

| File | SHA-256 |
|---|---|
| `../three326/candidate326-ir.json` | `48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84` |
| `../three326/REPORT.md` | `766427b1e75cf10823b0119b9d3a415a8460b49cbebb31c1b2b8483502f3baf8` |
| `work/quartic-optimization-20261107/resume-sol-review326-20261107/REVIEW.md` | `9bc208d22884b33a2777446ddd826017db173aa30b50830f944bbd941a08482c` |
| `candidate323-ir.json` | `dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd` |
| `polynomial323.json` | `0a08b05ce9924038009013f9f3628e19a4a8ee6566676178aeb57554fffb9571` |

All paths not beginning with `work/` are relative to this directory. Earlier frozen packets and the released manuscript remain unchanged.

## Exact equations and domains

For each of the three detectors retain the existing equation RE=1. R is the same affine expression in the stored contact-polynomial coordinates, and E is unchanged. Therefore R and E are nonzero in every rational solution, without any positivity or arithmetic conclusion.

Keep the existing output coordinates for E4,E8,E19,E39,E79,E157,E158. Replace the old E11 helper by r3 and remove E2. The full chain is

    E*r3 = R^2,
    E4*r3 = E,
    E8 = E4^2,
    E19*r3 = E8^2,
    E39*R = E19^2,
    E79*R = E39^2,
    E158 = E79^2,
    E157 = R*E158.

These equations successively and uniquely give

    r3=R^3=E^(-3), E4=E^4, E8=E^8, E19=E^19,
    E39=E^39, E79=E^79, E158=E^158, E157=E^157.

The first equation forces r3 nonzero because R and E are nonzero. Hence every division in this sequential verification is justified. There is no square-root choice: the square equations assign a new value from an already known value, and no reverse use of a square equation is required. R^2 is quadratic in the stored coordinates, so its direct expansion requires no new witness.

## Both witness maps

Given any326 solution, retain all coordinates except the private E2 and E11 helpers. Discard E2 and assign the repurposed E11 slot to R^3. The old chain has already forced all outputs to their stated powers of E, so every displayed new equation holds.

Given any323 solution, the sequential argument above determines every retained output. Restore E2=E^2 and change the r3 slot back to E11=E^11. Then the old equations

    E2=E^2, E4=E2^2,
    E11*E=E8*E4, E19=E11*E8

hold, as do the unchanged remainder of the old chain. No other coordinate changes. In particular, all three group values, W, the trace/pole coordinate, every point coordinate, the input and all scalar/anchor witnesses remain the same. This proves equality of full projections onto all outside coordinates, stronger than just equality of input projections.

## Literal incidence and count

Delete E2 coordinates361,409,457 and their defining rows313,363,413. Repurpose the former E11 coordinates355,403,451 as r3. Exactly three rows per detector change:

| Detector | r3 definition | E4 definition | E19 definition |
|---|---:|---:|---:|
| 0 | 544 | 745 | 546 |
| 1 | 550 | 760 | 552 |
| 2 | 556 | 775 | 558 |

The r3 definition is E*r3-R^2=0. The E4 definition is E4*r3-E=0, and the E19 definition is E19*r3-E8^2=0. The remaining coordinates keep their identities, including E39 at369,417,465 and E157 at843,844,845. The reused names of historical q10/q40 slots do not alter their exact meanings established above.

The complete incidence check confirms that all occurrences of the deleted or repurposed helpers lie in these changed or deleted rows. Every other residual object is identical to its326 source. Thus the count is326-3=323; there is no compensating helper or hidden change in the quantified domain.

## Verification and arithmetic scope

`verify323.py` imports no producer. It extracts R independently from each unchanged RE=1 row, constructs R^2 by an upper-triangular expansion, and compares the exact nine changed equations. It checks the complete deleted/repurposed incidence, active coordinate inventory, unchanged outside rows and metadata, and the successive exponent identities. It then recomputes every primitive residual square independently and matches all5840 quartic coefficients. Degree is four and integer content is one. C-independent coefficients have at most1520 bits; the five C-dependent terms are unchanged, so the exact maximum coefficient remains16C^2 for C=3^(2^25).

The existing326 common-place proof and its original Pi^19 completeness progression apply without modification because every consumed output is unchanged. This includes the pre-H exceptional-branch argument, actual G2 precision12, high comparison accuracy40, scalar conditions and order of real/local/CRT choices. No new external theorem application is introduced by this rational coordinate equivalence.

The search in `../post326/two_aux_search.py` suggested the chain by removing the formerly fixed E2 intermediate. It enumerated22307 two-helper Laurent exponent pairs and found only(-3,19) with full relation rank. That finite search is not needed for the proof of equivalence and does not establish global optimality among general quadratic circuits. The explicit equations, maps and literal verification above are the proposed result. Independent acceptance is still required before composition.
