# Contributed Lean libraries

These libraries sit beside the accepted 48-module `ZInQ` snapshot and leave it unchanged: `ZInQ.lean`, `lakefile.toml`, `SOURCE_MANIFEST.json`, `Checks/Axioms.lean` and `Frozen/BoundedIntegerPolynomial.lean` are not edited, and `scripts/check_lean.py` passes as before. They are not part of the snapshot and are not a proof of the main theorem.

| Library | Declaration | Hypotheses |
| --- | --- | --- |
| `EllipticModel` | `EllipticModel.P0_addOrderOf : addOrderOf P0 = 0` (and `P0_not_isOfFinAddOrder : ¬ IsOfFinAddOrder P0`): the first clause of `prop:generator`, the point `P₀` has infinite order on `E : y² = x³ − d²x`, `d = 75 − 53s`, over `ℚ(s)`, `s² = 2` | none |

`EllipticModel/Curve.lean` holds the definitions (`K0`, `dco`, `E`, `P0x`, `P0y`, `P0`), transcribed from `sec:model` of the November 5 manuscript (TeX 254–262 of `diophantine_zq.tex` at `97cec7fd`, preserved byte for byte as `docs/theorem-application-audit/source/audited-baseline.tex`). `EllipticModel/InfiniteOrder.lean` holds the proof. The proof is 2-adic, not the manuscript's reduction-and-torsion argument, which needs results Mathlib v4.35.0 lacks. It uses the dyadic step from the proof of `prop:cutoff` (TeX 6335–6338): with `μ(z) = |N(z)|₂`, one doubling multiplies `μ(x)` by 16 once `μ(x) > 1`, and `μ(x(P₀)) = 64`, so the points `2^k P₀` are pairwise distinct.

## Check

From the repository root, after `lake exe cache get` in `lean/`:

```sh
python scripts/check_lean_contrib.py --build
```

The script first runs `scripts/check_lean.py` (the snapshot's source check) and checks the frozen target's SHA-256. It then lints every contributed file: it must have a `module` header and no `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, `implemented_by` or `opaque`. Next it compiles each contributed module, and each snapshot module it imports, in a new output directory. Every compile is one `lean -j1 -Ddebug.skipKernelTC=false` call against the pinned dependency libraries, as `scripts/check_lean.py --build` does. Last it compiles `Checks/ContribAxioms.lean`, which fails on any declaration of a contributed module whose axioms leave `propext`, `Quot.sound` and `Classical.choice`, and prints `#print axioms` for the named theorems. `CONTRIB_EXPECTED.json` also pins the SHA-256 of every contributed Lean file and check file, as `SOURCE_MANIFEST.json` pins the snapshot; the source check refuses any other bytes, so a changed statement shows up as a change to that file. The printed facts must equal `CONTRIB_EXPECTED.json`; the output directory receives `FACTS.json`, `RESULT.json`, `commands.json` and one log per target.

`lakefile.toml` is pinned by `SOURCE_MANIFEST.json`, so the libraries have no `lean_lib` entry and the script is their build. For interactive work, a local `[[lean_lib]] name = "EllipticModel"` entry lets `lake build EllipticModel` and the editor find them.
