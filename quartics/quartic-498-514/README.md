# Frozen 498- and 514-variable quartics

This package reproduces the frozen498 construction and its ordinary-coefficient514 lift. It needs Python3.10 or later, Node.js, and the existing reference repository's `quartics/quartic-523-540` files. No external Python package or network access is used.

```
python -B verify_portable.py --repo /path/to/reference/repository
```

When this directory is installed under that repository, `--repo` is optional. The checker discovers the repository among its parent directories. Nothing outside this package is written. Regenerated artifacts and logs appear in `build/` and `work/10-combination/`.

The checker first validates every pinned package input and every used repository input. It reconstructs the exact mixed-depth source builder from the original builder's seven declared edits, regenerates its raw equations, and compares them to the pinned raw source. It then replays the independent gate and compiler checks, every subsequent composition, and every full sum of squares. Finally it requires the regenerated498 and514 residual systems and coefficient tables to match the frozen root files byte for byte. Both consecutively numbered JSON tables and every row of the text tables are checked against those frozen polynomials.

| Construction | Total variables | Witnesses | Residuals | Degree | Monomials | Largest coefficient magnitude |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Symbolic | 498 | 497 | 467 | 4 | 24,669 | `16*3^(2^26)` |
| Ordinary | 514 | 513 | 483 | 4 | 24,716 | `3^2048+1005072314676622 < 2^3247` |

Both polynomials have primitive content one. The symbolic fixed integer is C=3^(2^25), which is not an extra variable. Sixteen uniquely determined constant coordinates give the ordinary version.

The `candidate*.json` and `polynomial*.json` root files preserve the reviewed source IDs and exact bytes. The `quartic-*-coefficients.json` and `.txt` files use consecutive variable IDs beginning at input x0. Every JSON coordinate records its original source ID. Text rows use `coefficient | C exponent | comma-separated variable indices`; an empty index list denotes a constant.

`proofs/REPORT498.md` gives the complete construction chain and the final two algebraic reductions. Earlier reports explain the arithmetic changes. `reviews/` contains copies of separately authored internal review reports with their original scope limitations. Their mathematical acceptance is not inferred from the finite checker. The package does not claim a formal Lean proof or a fresh independent validation of all inherited global arithmetic and external literature.

`MANIFEST.json` pins every shipped immutable input, tool, proof, review, and table. `repository-pins.json` pins the exact external reference files. `input-origins.json` identifies original optimizer files and the original hashes of copied or path-adapted scripts. The only adaptation to those scripts is reference-repository discovery; their computational code is retained.
