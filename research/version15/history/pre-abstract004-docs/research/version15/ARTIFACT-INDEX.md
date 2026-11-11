# Version 15 artifact index

The selected new family has 222 total variables, 196 quadratic residuals and 2,277 nonzero coordinate monomials in its sparse presentation. The original huge construction and the 314-variable decimal quartic are retained.

| Artifact | File | Scope |
| --- | --- | --- |
| Manuscript PDF | [quartic_v15.pdf](snapshots/v15-222-001/manuscript/quartic_v15.pdf) | Current 222-variable draft |
| TeX source | [quartic_v15.tex](snapshots/v15-222-001/manuscript/quartic_v15.tex) | Matching source selection |
| 222-variable reproduction guide | [Package README](quartics/quartic-222/README.md) | Parameters, exact checks and review chain |
| Raw quadratic system | [raw222-ir.json](quartics/quartic-222/tables/raw222-ir.json) | 222 variables; 196 residuals |
| Raw quartic table | [raw222-polynomial.json](quartics/quartic-222/tables/raw222-polynomial.json) | 2,961 coordinate monomials |
| Selected sparse quadratic system | [sparse222-ir.json](quartics/quartic-222/tables/sparse222-ir.json) | Same witness dimension and residual count |
| Selected sparse quartic table | [sparse222-polynomial.json](quartics/quartic-222/tables/sparse222-polynomial.json) | 2,277 coordinate monomials; 2,278 parameter-separated terms |
| Finite verifier | [verify.py](quartics/quartic-222/verify.py) | Exact finite algebra and coefficient checks |
| Fixed-parameter generator | [generate.py](quartics/quartic-222/generate.py) | Coefficients for a chosen N; no effective N0 assertion |
| Retained 314 decimal table | [quartic-314-ordinary-coefficients.txt](snapshots/v15-018/quartics/quartic-299-314/quartic-314-ordinary-coefficients.txt) | 6,672 monomials; all coefficients written in decimal |
| Original huge specification | [ordinary-integer-definition.json](snapshots/v15-018/construction/ordinary-integer-definition.json) | Finite expression specification |

A_N = 149^(2N+1) is a fixed coefficient parameter and is not counted as a variable. The coefficient bound A_N² + 1 holds for N >= 53. The defining theorem has a separate ineffective threshold N0. See the [release notes](RELEASE-NOTES.md) and [cumulative handoff](CUMULATIVE-HANDOFF.md).

The final selection manifest must bind the exact manuscript/PDF hashes and release assets. Authenticated publication remains separate from this artifact index.
