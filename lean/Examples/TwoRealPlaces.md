# The actual two-real-place algebraic bridge

`Examples/TwoRealPlaces.lean` applies the pinned Mathlib APIs to PR6's actual
`EllipticModel.K0`, `E`, `Pt`, `P0` and `CondZQ.zcoord` from `CondZQ.Model`. This is a library
application, with no new mathematical-content or open-problem claim.
`Examples/TwoRealPlacesCheck.lean` consumes the interface, and
`Checks/TwoRealPlacesAxioms.lean` audits both modules and their project imports.

## Objects and exact correspondence

The source is `conditional-eight-hypotheses`, commit
`7663a19635390053716f02bfcbd16b97c42bd26a`. Its base snapshot and all 48 accepted
modules, hashes, dependency pins and quarantined target remain unchanged.
Mathlib is `56a005855ea17e0b0958f73ec801ae140b0a1679` (Lean 4.35.0).

For `K0 = QuadraticAlgebra ℚ 2 0`, the two `ℚ`-algebra homomorphisms are

```text
sigmaPlus  (u + v s) = u + v sqrt(2)
sigmaMinus (u + v s) = u - v sqrt(2).
```

They are constructed by `QuadraticAlgebra.lift`; the generator images are checked.
The real curves are literally `E.map sigmaPlus.toRingHom` and
`E.map sigmaMinus.toRingHom`. The tests identify their five coefficients with
`y² = x³ - (75 ∓ 53 sqrt(2))² x`, respectively. No curve identification between
the factors is used.

For one selected embedding `σ`, `pointMap` installs only
`σ.toRingHom.toAlgebra : Algebra K0 ℝ`, inside its definition, and applies
`WeierstrassCurve.Affine.Point.map` to `Algebra.ofId K0 ℝ`. The source
self-base-change and the explicit target are definitionally equal to the required
curves. The local instance does not escape into the product type. `diagonal`
pairs these two homomorphisms, so for every `P : Pt` and **every signed** `m : ℤ`,

```text
diagonal (m • P) = m • diagonal P.
diagonal (m • P0) = (m • pointMap sigmaPlus P0, m • pointMap sigmaMinus P0).
```

The test of `P0` consumes the original `P0x`, `P0y` and `P0_nonsingular`; no new
point or orbit is chosen. Zero maps to `(0,0)`, and injectivity is inherited from
either field point map, using `Point.map_injective`.

## Coordinates and denominator guards

`realZ` uses exactly the total convention `O ↦ 0`, `some x y h ↦ -x/y`.
`realZ_pointMap` and `diagonal_zcoord` identify it with the embedded value of
`CondZQ.zcoord` for every point, including the identity and zero ordinates.
`pointMap_some` retains the transported nonsingularity proof.
`guarded_some` takes the additional premise `y ≠ 0` and exports `σ y ≠ 0`
together with the coordinate equation. Totalized division also sends a zero
ordinate to zero, as explicitly tested; it asserts neither nonvanishing nor an
analytic chart.

For the **same** element `w : K0`, `rationalPart` gives
`(w.re : ℝ) = (sigmaPlus w + sigmaMinus w)/2`. The consumer `rval_recovery`
uses exactly `w = zcoord (j • P0) / zcoord (a • P0)`, with signed `a,j : ℤ`.
It requires `zcoord (a • P0) ≠ 0`, exports both real denominator guards, and
identifies `(CondZQ.rval a j : ℝ)` with the average of the two real quotients.
It does not establish the premise for any orbit index.

## Supplier applications

| Supplier and requirements | Actual input and consumer |
| --- | --- |
| `QuadraticAlgebra.lift`: a root of `u*u = 2 • 1 + 0 • u` in a `ℚ`-algebra | `±Real.sqrt 2` in `ℝ`; `sigmaPlus`, `sigmaMinus` and their evaluation/generator tests. |
| `Point.map`: one base curve, field extensions, compatible algebra towers | `R=S=F=K0`, target field `ℝ`, `W'=E.toAffine`, one scope-local action at a time; `pointMap`. The field premise and original point proofs come from `Curve.lean`. |
| `Point.map_injective` | The same selected field homomorphism; `pointMap_injective`, then `diagonal_injective`. |
| `AddMonoidHom.prod`, `map_zsmul`, `map_zero` | The two maps from the same `Pt`, one signed integer and one point; `diagonal`, its signed law and actual `P0` consumer. |
| `Affine.map_nonsingular`, point-map constructor computation | The original `x,y,h`; `pointMap_some` and the `P0` test. |
| `map_div₀`, `map_neg`, `map_ne_zero` | The same point coordinates and explicit nonzero premise; total compatibility and `guarded_some`. |
| Lift evaluation and field normalization | One `w` and then the exact guarded `CondZQ` quotient; `rationalPart`, `rval_recovery`. |

All indices and exceptional cases of these algebraic APIs are retained: arbitrary
points, signed integers, identity, and zero denominators for total compatibility.
The nonzero-denominator conclusion is conditional on its stated guard. There is
no limit, index-set extension, analytic normalization or independently optimized
orbit in this application. The downstream object is the original `rval`, not a
related independently defined ratio.

## Focused reproduction

From `lean/`, with the pinned dependencies already built, use a new output
directory and compile only this import closure in the following order:

```text
EllipticModel.Curve
ZInQ.PrecisionArithmetic
ZInQ.PrecisionAlgorithms
ZInQ.HeightConstantAlgorithm
ZInQ.HeightConstantComparison
ZInQ.PoleValuation
ZInQ.PolePolynomial
ZInQ.RationalSeparation
CondZQ.Model
Examples.TwoRealPlaces
Examples.TwoRealPlacesCheck
Checks.TwoRealPlacesAxioms
```

For each dotted module `M`, run under `lake env`, with `LEAN_PATH` prefixed by
the fresh output directory (and retaining the pinned dependency library paths):

```sh
lean -j1 -Ddebug.skipKernelTC=false -DwarningAsError=true \
  --root=. -o "$output/${M//.//}.olean" "${M//.//}.lean"
```

Create each output parent directory first. The unchanged accepted
`ZInQ.PoleValuation` reports its unused `hp2` parameter; compile that supplier
with the upstream default `-DwarningAsError=false`. Every new module uses
warnings-as-errors. No linter is disabled and no accepted source is edited.
The audit rejects any project declaration whose complete axiom closure contains
anything beyond `propext`, `Quot.sound`, `Classical.choice`, and rejects any
import of the quarantined `Frozen` target. The audit directly uses `import all`
for both example modules and all nine project suppliers listed above, asserts
full private import visibility for each module, and enumerates its complete
`constNames` inventory, including private, compiler-generated and test roots.
It checks representative private helpers from all five suppliers with explicit
private theorems. Per-module and total counts are computed dynamically;
`private` uses `Lean.isPrivateName`, and `generated_internal` uses
`Name.isInternalDetail` after removing the private prefix. These categories can
overlap and do not restrict the audit: every enumerated declaration is checked.
Each module's reported axioms are the union of its roots' transitive closures.

From the repository root, the existing narrow source and historical audit checks
are `python3 -B scripts/check_lean.py`,
`python3 -B scripts/check_lean_contrib.py`, and
`python3 -B scripts/check_audit_history.py --self-test`. The first two retain their
original accepted/contributed scope; they do not themselves compile these new
examples. No expected hash is refreshed.

## Scope and outstanding work

This non-release application does not alter the manuscript, release profile,
archived artifacts or existing audit acceptance. Independent review and upstream
Protocol acceptance remain pending. Codex CLI authored the application and ran
the scoped compiler and axiom checks; this is author verification.

Real point topology, compact topological group instances, continuity of the
identity extension of `z`, admissible orbit denominator guards, positive and
arbitrarily small `eps`, the derivative of signed `[n]`, the punctured `rval`
limit and both exact strict inequalities in `accept` remain unproved here.
In particular the full target remains
`∀ n κ : ℤ, n ∉ Cset → κ ≠ 0 → ∃ a l j : ℤ, accept n κ a l j`, with
`j = n*a`, `1 ≤ a`, `1 ≤ l`, and signed `n,κ` unchanged. No `HypCC`, main theorem,
geometric isomorphism or external open-problem solution follows from this
algebraic interface alone.
