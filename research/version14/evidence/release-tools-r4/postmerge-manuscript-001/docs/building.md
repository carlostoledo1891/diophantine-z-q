# Building and checking the research package

Run these commands from the repository root. Python scripts use the standard library. The current quartic and the original large construction have separate checks. The Version 7 handoffs contain their own build instructions under `current/`; Version 9 adds the [odd-product constructions](quartic-523-540/README.md). See the [handoff guide](../handoff/README.md) for the archive layout and verification procedure.

## Current 299- and 314-variable quartics

Run the exact replay and inventory commands in the [Version 14 guide](manuscript-revisions/version14/GUIDE.md). Its finite checks, manuscript review and inherited arithmetic inputs have separate scopes.

## Historical 394- and 411-variable quartics

```sh
python -B scripts/check_quartic394_portable.py
python -B docs/manuscript-revisions/version13/validate-applications.py --repo . --self-test
python -B scripts/check_audit_history.py --self-test
```

The Version 13 replay uses only Python's standard library. It checks the immutable packet before and after all 27 source and certificate stages, both complete coefficient tables, the compact coordinate maps and the three public download copies. It writes its receipt to `build/quartic-394/verification.json`. The inventory validator checks 39 applications and 351 obligations, with negative controls; it does not decide their mathematical truth. Read the [Version 13 guide](manuscript-revisions/version13/GUIDE.md) for the review boundaries.

## Historical 523- and 540-variable quartics

```sh
python -B scripts/check_odd_product.py
python -B docs/quartic-523-540/inventory.py validate
```

These offline checks require only Python and Node.js. They write into `build/odd-product/` and leave pinned source data unchanged. Both final verifiers run twice; every text coefficient is compared with its JSON value.

## Historical 962-variable quartic

The [Version 7 guide](quartic-962/README.md) describes the complete coefficient table, its fixed integer parameter, and the separate scopes of the finite checks and arithmetic proof. Run:

```sh
python -E -B scripts/check_quartic962.py --out build/quartic-962-reproduction
```

Use a new output directory outside the frozen package. Python 3.10 or later and Node.js 18 or later suffice; no third-party packages or network access are needed. Fourteen checks rebuild the source, replay 904 gates and 894 compiler operations, verify the rational coordinate identities, and compare seven artifacts byte for byte. They also check the 962-variable, degree-four, 55,409-monomial statistics. The program does not expand the huge fixed integer coefficients digit by digit.

## Historical 1,272-variable baseline

The [Version 5 package](../quartics/quartic-1272/README.md) contains its portable reproduction command and independent checks. Its complete table encodes the fixed integer coefficients using exact powers; reproduction does not expand those integers digit by digit. Use a fresh output directory as specified there.

```sh
python -E -B scripts/check_quartic1272.py --out build/quartic-1272-reproduction
```

This requires Python 3.10 or later and Node.js 18 or later, with no third-party packages or network access. It checks the package inventory, rebuilds the complete source and coefficient table, runs the independent checks, and requires byte identity with the released polynomial. The output directory must be new and outside `quartics/quartic-1272/`.

## Retained 4,973-variable quartic

To replay the frozen certificate and reproduce the complete 4,973-variable construction:

```sh
python3 -E -B quartics/quartic-4973/reproducibility/run.py --output build/quartic-reproduction --stage-seconds 180
```

Use a fresh output directory outside the package. The runner reads the package without changing it and writes generated files, logs and reports to that directory. It requires Linux process groups and resource controls; the reference environment is CPython 3.12.14 with zlib 1.3. It requires at least 8 GiB available memory to start, stops if available memory falls below 4 GiB, and runs bounded stages sequentially with a 2 GiB child address-space limit. Standard public GitHub Linux runners satisfy the memory requirement; standard private runners may not. Mandatory reproduction rebuilds the source and base pipeline, then replays the exact selected certificate. Optional timed heuristic rediscovery is not a deterministic reproduction claim. See the [reproduction instructions](../quartics/quartic-4973/reproducibility/README.md) for its stages and failure conditions. The fresh receipt is `SUMMARY.json` in the output directory.

For the frozen artifact's algebraic replay alone, copy `quartics/quartic-4973/` to a writable directory and run:

```sh
python -E -B /path/to/writable-copy/verify_certificate.py /path/to/writable-copy
```

This portable checker writes `verification.json` in the supplied directory. Use the copy to keep the released package's exact file inventory unchanged. The packaged original receipt is [evidence/final-verification.json](../quartics/quartic-4973/evidence/final-verification.json). The checker verifies exact projection-preserving equivalence to the pinned source and the complete integer expansion, including the variable count, degree and coefficient bound. These checks do not prove the source system's arithmetic characterization of the integers. The [Version 4 evidence](quartic-4973/README.md) records that separate argument and its review scope.

## Version 14 manuscript

Run `python scripts/build_paper.py` to build the current Version 14 TeX with the pinned Tectonic engine and bundle. The build writes `quartic_v14.pdf`, its logs and the build receipt under `build/paper/`; it does not replace the checked-in PDF. Review the exact rendered pages and total page count recorded in the Version 14 PDF QA receipt and reviewed workflow. Historical Version 13 receipts retain their original scope.

## Manuscript inventories

The [Version 7 inventory](quartic-962/README.md) binds the unchanged proof body to its source applications, exact reviewed fragments, and historical predecessors:

```sh
python -E -B docs/quartic-962/inventory.py validate --repo . --manuscript manuscripts/quartic_v7.tex
python -E -B docs/quartic-962/test_inventory.py
python -E -B scripts/check_manuscript_revision.py
```

The Version 7 inventory keeps its frozen logical filename `manuscripts/quartic_v7.tex`; the validator reads the unchanged source from `manuscripts/archive/quartic_v7.tex`.

The following checks remain required for the historical baselines. Their older publication-status records describe those versions, not the replacement proof in Version 7. The adapter resolves the original logical filenames to `manuscripts/archive/` while retaining the frozen validators and all accepted hashes.

```sh
python -E -B scripts/check_historical_inventory.py 5 validate --repo . --manuscript quartic_1272.tex
python -E -B scripts/check_historical_inventory.py 5 test
```


```sh
python docs/theorem-application-audit/validate.py
python -E -B scripts/check_historical_inventory.py 4 validate --repo . --docs docs/quartic-4973 --acceptance-sha256 TRUSTED_SHA256
```

For the Pheidas attribution update, the current digest is `06dd04ceb4bdcb40875e70293bf68abba61fd17052a5e90a70ade61af649d88b`, recorded in [the update evidence](quartic-4973-validation/pheidas-20261106/UPDATE.json).

Replace `TRUSTED_SHA256` with the independently recorded acceptance digest in the release evidence.

The first command validates the [historical theorem-application inventory](theorem-application-audit/README.md) against its archived baseline. The second checks the [Version 4 inventory and manuscript bindings](quartic-4973/README.md). Read those instructions for the exact scopes. These structural checks do not prove mathematical statements. Primary-source verification for the historical inventory additionally requires its separately restored research workspace.

## Original large construction

This check uses Python 3.11 or later and Node.js 22 or later. CI pins Python 3.12.14 and Node.js 24.22.1.

```sh
python scripts/check_construction.py --report build/construction-checks.json
```

It regenerates the original rational expression from its pinned natural-polynomial input, checks hashes and wiring, recalculates syntactic bounds, and runs the supplied finite arithmetic checks. See the [original construction README](../construction/README.md) for each check's scope. This is separate from the quartic reproduction above.

## Lean helpers

Install [elan](https://github.com/leanprover/elan), then run:

```sh
cd lean
lake exe cache get
cd ..
python scripts/check_lean.py --build --output build/lean-local
```

The output directory must not already exist. The checked-in toolchain and Lake manifest pin Lean and Mathlib. The checker validates source hashes and dependency revisions, compiles the 48 accepted helper modules and their root into fresh project artifacts, and runs the axiom audit. Dependency binaries come from the pinned Mathlib cache and are not rebuilt by this command.

For the quick source and quarantine checks without compiling:

```sh
python scripts/check_lean.py
```

Read the [Lean README](../lean/README.md) for the trust boundary and allowed axioms. The main theorem remains unproved; its frozen `sorry` is excluded from the default imports and accepted-helper audit.

## Continuous integration

The [manuscript workflow](../.github/workflows/manuscript-integration.yml) reproduces the quartic, validates the historical and current manuscript inventories, and compiles the current manuscript. Run it by manual dispatch; the research workflow also runs on pushes. The [research workflow](../.github/workflows/research-checks.yml) checks the original construction, the historical inventory, manuscript compilation and the accepted Lean helpers.

GitHub Actions dependencies are pinned to commit hashes; the elan installer and Tectonic archives are pinned by SHA-256. Workflows upload their reports and logs. A green run means the named checks passed on that commit. It does not certify the global arithmetic inputs or complete the main Lean proof.

The earlier Version 4 release digest remains in its historical evidence; use the Pheidas-update digest above for the retained current Version 4 source.

The historical Version 10 revision and its inherited application bindings are checked with `python -B docs/manuscript-revisions/version10/check.py`. The bounded valuation regression is `python -B docs/manuscript-revisions/version10/check_valuation.py`. Neither is a decision procedure for the mathematical proof.

The current application contracts, exact revision and independent acceptance records are checked with `python -B scripts/check_audit_history.py --self-test`. Version 10 checks remain historical. Neither script proves the mathematics.

For the retained Version 12 baseline, run `python -B scripts/check_quartic498.py` for the complete portable reconstruction and coefficient checks. This requires Python and Node. The new application inventory has its separate validator under `docs/manuscript-revisions/version12/inventory/`.
