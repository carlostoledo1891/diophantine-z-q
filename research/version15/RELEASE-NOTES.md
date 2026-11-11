# Version 15 release notes

Version 15 adds a quartic family in **222 total rational variables**, including the input variable. The selected sparse presentation has **196 quadratic residuals** and **2,277 nonzero coordinate monomials**. Its table has 2,278 parameter-separated terms: terms with the same coordinate monomial are combined after substituting the fixed integer parameter.

The family uses A_N = 149^(2N+1) as a coefficient parameter, not an additional variable. For N >= 53, the maximum absolute coefficient is A_N² + 1. The theorem identifies the integers for sufficiently large N, with an **ineffective defining threshold N0**. The coefficient estimate N >= 53 does not establish that defining threshold. A generator can print the coefficients for a chosen N without certifying that N is large enough for the defining theorem.

The original huge-polynomial construction and the 314-variable quartic with fully written decimal coefficients remain available. Earlier 233-, 224- and 223-variable presentations, their source maps and scoped reviews remain research history. The variable and monomial counts are not claimed minimal.

## What changed

The accepted reduction replaces two trace helpers by one quotient coordinate. The existing proof that q1 is nonzero justifies the quotient. All other coordinates and constraints retain their roles. Separate reviews check the rational witness maps and domain conditions, and the exact finite residual transport and complete polynomial expansion.

The selected sparse table also retains previously reviewed coordinate and row transformations and positive residual weights. Positive weights preserve the common zero set over the rationals. No new non-diagonal Gram-block candidate is included.

## Reproduction and review scope

Use the [222-variable package](quartics/quartic-222/README.md) for the raw and sparse tables, parameter substitution and finite verification. The portable verifier checks the complete residual expansion and coefficient statistics. Preserved exact-map checks and their scoped reviews address the algebraic transformations; they are not all rerun by the portable verifier. The mathematical source argument and its separate reviews supply the arithmetic characterization.

The [Version 15 release](https://github.com/elliotglazer/diophantine-z-q/releases/tag/quartic-222-version-15) is published from public merge `2b34f7175aa258f331fa451c03336a0cec051890`, following [PR 26](https://github.com/elliotglazer/diophantine-z-q/pull/26) and its successful [protocol evaluation](https://github.com/elliotglazer/diophantine-z-q/pull/26/checks). Historical reviews retain their original qualifications and authorship corrections.
