module

public import CondZQ.Model
public import Mathlib.Analysis.Real.Sqrt
public import Mathlib.Algebra.Group.Prod

/-!
# The two real places of the fixed elliptic model

An algebraic application of Mathlib's quadratic-algebra lift and point-map APIs.
Both factors are images of the same point of `EllipticModel.E`.
The coordinate below is total field division; no analytic chart is asserted.
-/

@[expose] public section

namespace EllipticModel.TwoRealPlaces

open WeierstrassCurve

noncomputable def sigmaPlus : K0 →ₐ[ℚ] ℝ :=
  QuadraticAlgebra.lift ⟨Real.sqrt 2, by
    simpa [smul_eq_mul, pow_two] using Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2)⟩

noncomputable def sigmaMinus : K0 →ₐ[ℚ] ℝ :=
  QuadraticAlgebra.lift ⟨-Real.sqrt 2, by
    simpa [smul_eq_mul, pow_two] using Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2)⟩

@[simp] theorem sigmaPlus_apply (w : K0) :
    sigmaPlus w = (w.re : ℝ) + (w.im : ℝ) * Real.sqrt 2 := by
  simp [sigmaPlus, QuadraticAlgebra.lift, smul_eq_mul]

@[simp] theorem sigmaMinus_apply (w : K0) :
    sigmaMinus w = (w.re : ℝ) - (w.im : ℝ) * Real.sqrt 2 := by
  simp [sigmaMinus, QuadraticAlgebra.lift, smul_eq_mul, sub_eq_add_neg]

@[simp] theorem sigmaPlus_omega :
    sigmaPlus (QuadraticAlgebra.omega : K0) = Real.sqrt 2 := by simp

@[simp] theorem sigmaMinus_omega :
    sigmaMinus (QuadraticAlgebra.omega : K0) = -Real.sqrt 2 := by simp

abbrev EPlus := E.map sigmaPlus.toRingHom
abbrev EMinus := E.map sigmaMinus.toRingHom

/-- Each call installs only the algebra action belonging to its selected place. -/
noncomputable def pointMap (σ : K0 →ₐ[ℚ] ℝ) :
    Pt →+ (E.map σ.toRingHom).toAffine.Point := by
  letI : Algebra K0 ℝ := σ.toRingHom.toAlgebra
  exact Affine.Point.map (W' := E.toAffine) (Algebra.ofId K0 ℝ)

/-- One homomorphism, with two explicit and generally different target curves. -/
noncomputable def diagonal : Pt →+ EPlus.toAffine.Point × EMinus.toAffine.Point :=
  (pointMap sigmaPlus).prod (pointMap sigmaMinus)

theorem pointMap_injective (σ : K0 →ₐ[ℚ] ℝ) : Function.Injective (pointMap σ) := by
  letI : Algebra K0 ℝ := σ.toRingHom.toAlgebra
  exact Affine.Point.map_injective (W' := E.toAffine) (Algebra.ofId K0 ℝ)

theorem diagonal_injective : Function.Injective diagonal := by
  intro P Q h
  exact pointMap_injective sigmaPlus (congrArg Prod.fst h)

@[simp] theorem diagonal_zero : diagonal 0 = (0, 0) := map_zero diagonal

/-- The integer index, including its sign, is shared by both factors. -/
theorem diagonal_zsmul (m : ℤ) (P : Pt) : diagonal (m • P) = m • diagonal P :=
  map_zsmul diagonal P m

theorem diagonal_P0_zsmul (m : ℤ) :
    diagonal (m • P0) = (m • pointMap sigmaPlus P0, m • pointMap sigmaMinus P0) := by
  rw [diagonal_zsmul]
  rfl

/-- The same total convention as `CondZQ.zcoord`: `O ↦ 0`, `(x,y) ↦ -x/y`. -/
noncomputable def realZ (W : WeierstrassCurve ℝ) : W.toAffine.Point → ℝ
  | .zero => 0
  | .some x y _ => -x / y

theorem pointMap_some (σ : K0 →ₐ[ℚ] ℝ) (x y : K0)
    (h : E.toAffine.Nonsingular x y) :
    pointMap σ (.some x y h) =
      .some (σ x) (σ y) ((E.toAffine.map_nonsingular σ.injective x y).mpr h) := by
  rfl

theorem realZ_pointMap (σ : K0 →ₐ[ℚ] ℝ) (P : Pt) :
    realZ (E.map σ.toRingHom) (pointMap σ P) = σ (CondZQ.zcoord P) := by
  cases P with
  | zero => exact (map_zero σ).symm
  | some x y h =>
    change -σ x / σ y = σ (-x / y)
    rw [map_div₀, map_neg]

/-- A chart denominator guard is transported, never inferred from total division. -/
theorem guarded_some (σ : K0 →ₐ[ℚ] ℝ) (x y : K0)
    (h : E.toAffine.Nonsingular x y) (hy : y ≠ 0) :
    σ y ≠ 0 ∧ realZ (E.map σ.toRingHom) (pointMap σ (.some x y h)) = -σ x / σ y := by
  exact ⟨map_ne_zero σ |>.mpr hy, rfl⟩

theorem diagonal_zcoord (P : Pt) :
    (realZ EPlus (diagonal P).1, realZ EMinus (diagonal P).2) =
      (sigmaPlus (CondZQ.zcoord P), sigmaMinus (CondZQ.zcoord P)) := by
  exact Prod.ext (realZ_pointMap sigmaPlus P) (realZ_pointMap sigmaMinus P)

/-- Recover the rational part of one element, before taking any quotient images. -/
theorem rationalPart (w : K0) :
    (w.re : ℝ) = (sigmaPlus w + sigmaMinus w) / 2 := by
  rw [sigmaPlus_apply, sigmaMinus_apply]
  ring

/-- Both denominators and both quotients come from the same signed orbit. -/
theorem rval_recovery (a j : ℤ) (ha : CondZQ.zcoord (a • P0) ≠ 0) :
    realZ EPlus (diagonal (a • P0)).1 ≠ 0 ∧
    realZ EMinus (diagonal (a • P0)).2 ≠ 0 ∧
    (CondZQ.rval a j : ℝ) =
      (realZ EPlus (diagonal (j • P0)).1 / realZ EPlus (diagonal (a • P0)).1 +
       realZ EMinus (diagonal (j • P0)).2 / realZ EMinus (diagonal (a • P0)).2) / 2 := by
  change realZ EPlus (pointMap sigmaPlus (a • P0)) ≠ 0 ∧
    realZ EMinus (pointMap sigmaMinus (a • P0)) ≠ 0 ∧ _
  simp only [realZ_pointMap]
  refine ⟨(map_ne_zero sigmaPlus).mpr ha, (map_ne_zero sigmaMinus).mpr ha, ?_⟩
  simpa only [CondZQ.rval, map_div₀] using
    rationalPart (CondZQ.zcoord (j • P0) / CondZQ.zcoord (a • P0))

end EllipticModel.TwoRealPlaces
