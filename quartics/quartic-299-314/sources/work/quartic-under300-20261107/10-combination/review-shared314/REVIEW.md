# Independent construction review of shared314

I accept the finite construction of the frozen shared314 candidate and its implementation of the displayed arithmetic interface. I found no missing equation, coordinate-count discrepancy, private-consumer leak, or coefficient error. This review does not independently prove the new arithmetic argument. Agent05's separate arithmetic review, cited below, supplies that scope; neither review alone substitutes for the other.

Reviewer: `/root/astra_quartic_opt10_combination`, November 7, 2026. The candidate compiler was authored by agent01 and the new arithmetic argument by agent03. I authored neither. My earlier authorship of some inherited source315 compositions is disclosed; this review concerns their replacement detector construction, not a fresh independent certification of all inherited mathematics. No candidate or author file was changed.

## Frozen objects

Paths below are relative to the workspace's `work` directory.

| Object | Path | SHA256 |
|---|---|---|
| Accepted source315 | `quartic-under300-20261107/10-combination/combined315/candidate315-ir.json` | `d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8` |
| Candidate314 | `quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json` | `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5` |
| Full polynomial | same directory, `polynomial314.json` | `82f10a736855acba8c12a09406a5c954ddefa22825dbffa2d773005a6b6b05e8` |
| Author report | same directory, `REPORT.md` | `ea67fce0404236d1e5d7b9018536a040d07d75591cd83c5c4ca84385523a3f3e` |
| Arithmetic proof | `quartic-optimization-20261107/resume-depth-20261107/shared314/PROOF.md` | `a8b3adc8ed7103aea1fc65cff5654632534fe151ec5ba157ad4413f79cceb4eb` |
| Independent arithmetic review | `quartic-optimization-20261107/resume-review-shared314-20261107/REVIEW.md` | `99630a50aac94071d7001d04afd1dcf5fa68209b34bbebff092db926720a5e33` |
| My checker | this directory, `check.py` | `f723090ab7db662ff35f81ee3df794bca44825451a2aee4d6ce17f3e34dae4c8` |
| My results | this directory, `CHECKS.json` | `5cde7543440bd5dd1de6e0089bb4a01b8ade70a79d798a21a36a433b7c20ba82` |

The checker imports no author producer, verifier, or polynomial utility. It implements exact rational sparse-polynomial arithmetic, checks every entry of the author's frozen manifest before and after execution, and writes only its own result file.

## Complete equation and consumer accounting

The source has 315 coordinates and 285 residuals. The candidate removes exactly twelve coordinates and adds exactly eleven, with no duplicated IDs. It removes exactly 24 residuals, replaces the 18 shared-square and 18 group-component residuals, and adds exactly 22 residuals. Every one of the remaining 225 residual objects is identical, including metadata. Thus the candidate has 314 coordinates and 283 residuals. All 314 coordinates occur in the equations.

I checked every old and new consumer of all deleted, repurposed and scaled coordinates. The nine private field pairs have no uses outside their defining squares and the replaced groups. The six repurposed local helpers have no surviving old consumers. Other coordinate objects are unchanged; the 24 renamed helper/scale objects differ only in their names. All other top-level inherited data is unchanged except the explicit status field.

Each of the nine field squares is reconstructed from its actual affine source input, including the nontrivial M1 and H4 normalizations. Its two old equations are checked before checking the new equations obtained by multiplying the output by gamma40, gamma80 or gamma160. The forward/reverse maps for these private helpers are division/multiplication by a nonzero rational power of gamma. They are not claimed to preserve the old detector product.

The common gamma chain has nine coordinates and eight equations. The literal equation gamma16*J=1 is retained as row2004. It excludes gamma=0 and makes all powers unique: gamma2, gamma4, gamma8, gamma16, gamma^-16, gamma40, gamma80 and gamma160. The extra field pair is exactly P1 squared, with P1=(v255,2*v256); it adds two coordinates and two equations.

For each detector I extract R directly from its unchanged E*R=1 row and check that it is affine. The four new equations are R2=R^2, R3=R*R2, E4*R3=E and E8=E4^2. Since E*R=1, these give precisely the powers used in the proof, with no zero branch. Every coefficient of all 18 new group components is reconstructed independently from these powers and the displayed three groups. This includes the rational gamma16*E8 guard, the low E*U term and the E8*T0 term.

The alternate leaves retain their field conjugation. I derive the eighth-power cache matrix using D=11-6*sqrt(2), D^4=72097-50952*sqrt(2), and Norm(D^4)=5764801. The two Z1 cache equations are independently inverted to recover the conjugated fourth power. In particular, a stored second component is not silently interpreted with the wrong factor of two.

## Interfaces needed by the arithmetic review

I check each complete A, T and Z half-chart sign action against every candidate residual. Each residual is fixed or negated as a whole. The new common powers, scaled pairs and all groups remain fixed. Thus the root restoration preceding H interpretation is still permitted by the literal system. `CHECKS.json` lists the sign sets and every negated row.

The actual retained Lucas gates are reconstructed with A=L2, T=L3 and B=L4. Substituting their products gives

    F(A,T,B)+1 = T^2-A(A-2)*T*B+(A-2)^2*B^2.

The stored pair (v253,2*v254) is F+1, not F. The actual H4-square input is (v319-2*v253+1,4*v320-4*v254), and the retained test-square rows make it exactly F^2. The new pair is therefore F^4/gamma160. This distinction is necessary for the arithmetic use of F(0,0,0)=-1.

For all four primary charts I independently reconstruct the retained relation I_i*L_i=V_i*S_H, including the full physical affine expression S_H in coordinates142,143,700,701. On the inherited point domains this is the same exact z(U_i)=L_i*z(H) relation used by the bootstrap. I also bind the P1 source pair to I_1^2+D*c_A*P1=c_A with the actual c_A=(v82,2*v83). All these rows, the root/scalar/anchor equations, and the product/norm/trace/pole rows remain unchanged. The product values themselves change with the new groups; this is not an old-fiber equivalence claim.

I read agent05's separate review. Its accepted interface matches these literal equations: nonzero gamma, the one-place group inequalities, initial formality before the unit-ratio bootstrap, precision40 after H reaches depth10, and the original Pi19 completeness choices. My acceptance does not extend to changing any of those hypotheses, weights, conjugations, or choices.

## Full polynomial

I separately clear denominators and divide coefficient content in each residual, square every resulting primitive integral residual, and combine all coefficients. The result equals every entry of the frozen polynomial table.

The verified totals are 314 rational variables including the input, 313 witnesses, 283 quadratic residuals, 6138 entries separated by powers of C, and 6135 distinct variable monomials after specializing C=3^(2^25). The degree is exactly four and coefficient content is one. The largest absolute coefficient is exactly

    186624*C^2+64 = 186624*3^(2^26)+64,

on v89^4. All stored integer coefficients have at most 1520 bits. Since C>2^1522, the leading nonzero C coefficient dominates the lower powers, so no monomial vanishes under specialization. The same bound and the strict one-unit gap in every other C^2 coefficient establish the maximum without expanding C in decimal.

Run `python check.py` from any directory to reproduce this finite review. No publication or manuscript change is authorized by this report; the next publication threshold remains strictly below 300 total variables.
