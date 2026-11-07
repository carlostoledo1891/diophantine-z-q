module

public import Mathlib.Algebra.Order.Ring.Star
public import Mathlib.Algebra.Order.Star.Int
public import Mathlib.Algebra.QuadraticAlgebra.Defs
public import Mathlib.AlgebraicGeometry.EllipticCurve.Affine.Point
public import Mathlib.Analysis.Normed.Field.Lemmas

/-!
# The curve `E` and the point `P₀` of the elliptic model (definitions)

The objects of `sec:model` in the November 5 manuscript (`diophantine_zq.tex` at `97cec7fd`,
preserved byte for byte as `docs/theorem-application-audit/source/audited-baseline.tex`,
TeX lines 254–262), stated on Mathlib objects:

* `K₀ = ℚ(s)`, `s² = 2`: Mathlib's `QuadraticAlgebra ℚ 2 0`, a field because `2` is not a
  square in `ℚ`; an element `⟨x₀, x₁⟩` is `x₀ + x₁ s`;
* `d = 75 − 53s` and `E : y² = x³ − d²x`, a `WeierstrassCurve` over `K₀`, its points with
  Mathlib's group law;
* `P₀ = ((1641 − 1160s)/8, (−123720 + 87483s)/32)`, proved to lie on `E` and to be
  nonsingular.

This file contains definitions and the two facts needed to form `P₀`; the infinite order of
`P₀` is in `EllipticModel.InfiniteOrder`.
-/

@[expose] public section

namespace EllipticModel

open WeierstrassCurve

theorem not_isSquare_two_rat : ¬ IsSquare (2 : ℚ) := by
  rw [Rat.isSquare_iff]
  rintro ⟨h, -⟩
  have h2 : ((2 : ℚ).num) = 2 := rfl
  rw [h2] at h
  obtain ⟨r, hr⟩ := h
  have hlo : -1 ≤ r := by nlinarith
  have hhi : r ≤ 1 := by nlinarith
  interval_cases r <;> simp_all

instance fact_not_isSquare_two : Fact (¬ IsSquare (2 : ℚ)) := ⟨not_isSquare_two_rat⟩

/-- `K₀ = ℚ(s)`, elements `x₀ + x₁ s` with `s² = 2` (TeX 257). -/
abbrev K0 := QuadraticAlgebra ℚ 2 0

/-- `d = 75 − 53 s` (TeX 257). -/
def dco : K0 := ⟨75, -53⟩

/-- The curve `E : y² = x³ − d² x` over `K₀` (TeX 257). -/
def E : WeierstrassCurve K0 := { a₁ := 0, a₂ := 0, a₃ := 0, a₄ := -(dco * dco), a₆ := 0 }

/-- The points of `E` over `K₀`, with Mathlib's group law. -/
abbrev Pt := E.toAffine.Point

/-- `x(P₀) = (1641 − 1160 s)/8` (TeX 261). -/
def P0x : K0 := ⟨1641 / 8, -145⟩

/-- `y(P₀) = (−123720 + 87483 s)/32` (TeX 261). -/
def P0y : K0 := ⟨-15465 / 4, 87483 / 32⟩

theorem P0_equation : E.toAffine.Equation P0x P0y := by
  rw [WeierstrassCurve.Affine.equation_iff]
  ext <;> simp [E, P0x, P0y, dco, pow_succ] <;> norm_num

theorem P0_nonsingular : E.toAffine.Nonsingular P0x P0y := by
  rw [WeierstrassCurve.Affine.nonsingular_iff']
  refine ⟨P0_equation, Or.inr ?_⟩
  intro h
  have := congrArg QuadraticAlgebra.re h
  simp [E, P0x, P0y, QuadraticAlgebra.re_ofNat, QuadraticAlgebra.im_ofNat] at this

/-- The fixed point `P₀` (TeX 259–262). -/
noncomputable def P0 : Pt := .some P0x P0y P0_nonsingular

end EllipticModel
