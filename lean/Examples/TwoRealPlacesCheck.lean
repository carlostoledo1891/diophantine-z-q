module

import Examples.TwoRealPlaces

/-! Exact consumers of the concrete two-place interface, including the zero and guarded loci. -/

open EllipticModel EllipticModel.TwoRealPlaces WeierstrassCurve

example : sigmaPlus (QuadraticAlgebra.omega : K0) = Real.sqrt 2 ∧
    sigmaMinus (QuadraticAlgebra.omega : K0) = -Real.sqrt 2 :=
  ⟨sigmaPlus_omega, sigmaMinus_omega⟩

example : EPlus = { a₁ := 0, a₂ := 0, a₃ := 0,
    a₄ := -((75 : ℝ) - 53 * Real.sqrt 2)^2, a₆ := 0 } := by
  ext <;> simp [E, WeierstrassCurve.map, dco, pow_two]

example : EMinus = { a₁ := 0, a₂ := 0, a₃ := 0,
    a₄ := -((75 : ℝ) + 53 * Real.sqrt 2)^2, a₆ := 0 } := by
  ext <;> simp [E, WeierstrassCurve.map, dco, pow_two]

example (σ : K0 →ₐ[ℚ] ℝ) :
    pointMap σ P0 = .some (σ P0x) (σ P0y)
      ((E.toAffine.map_nonsingular σ.injective P0x P0y).mpr P0_nonsingular) :=
  pointMap_some σ P0x P0y P0_nonsingular

example (P : Pt) (m : ℤ) : diagonal (m • P) = m • diagonal P :=
  diagonal_zsmul m P

example (m : ℤ) : diagonal (m • P0) =
    (m • pointMap sigmaPlus P0, m • pointMap sigmaMinus P0) := diagonal_P0_zsmul m

example : diagonal 0 = (0, 0) ∧
    realZ EPlus (diagonal 0).1 = 0 ∧ realZ EMinus (diagonal 0).2 = 0 := by
  simp [realZ]

example : Function.Injective diagonal := diagonal_injective

example (P : Pt) :
    (realZ EPlus (diagonal P).1, realZ EMinus (diagonal P).2) =
    (sigmaPlus (CondZQ.zcoord P), sigmaMinus (CondZQ.zcoord P)) := diagonal_zcoord P

example (x y : K0) (h : E.toAffine.Nonsingular x y) (hy : y ≠ 0) :
    (sigmaPlus y ≠ 0 ∧
      realZ EPlus (pointMap sigmaPlus (.some x y h)) = -sigmaPlus x / sigmaPlus y) ∧
    (sigmaMinus y ≠ 0 ∧
      realZ EMinus (pointMap sigmaMinus (.some x y h)) = -sigmaMinus x / sigmaMinus y) :=
  ⟨guarded_some sigmaPlus x y h hy, guarded_some sigmaMinus x y h hy⟩

example (a j : ℤ) (ha : CondZQ.zcoord (a • P0) ≠ 0) :
    realZ EPlus (diagonal (a • P0)).1 ≠ 0 ∧
    realZ EMinus (diagonal (a • P0)).2 ≠ 0 ∧
    (CondZQ.rval a j : ℝ) =
      (realZ EPlus (diagonal (j • P0)).1 / realZ EPlus (diagonal (a • P0)).1 +
       realZ EMinus (diagonal (j • P0)).2 / realZ EMinus (diagonal (a • P0)).2) / 2 :=
  rval_recovery a j ha
