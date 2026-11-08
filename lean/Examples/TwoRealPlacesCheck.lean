module

import Examples.TwoRealPlaces

/-! Exact consumers of the concrete two-place interface, including the zero and guarded loci. -/

open EllipticModel EllipticModel.TwoRealPlaces WeierstrassCurve

namespace EllipticModel.TwoRealPlaces.Tests

theorem generator_images : sigmaPlus (QuadraticAlgebra.omega : K0) = Real.sqrt 2 ∧
    sigmaMinus (QuadraticAlgebra.omega : K0) = -Real.sqrt 2 :=
  ⟨sigmaPlus_omega, sigmaMinus_omega⟩

theorem curvePlus_coefficients : EPlus = { a₁ := 0, a₂ := 0, a₃ := 0, a₄ := -((75 : ℝ) - 53 * Real.sqrt 2)^2, a₆ := 0 } := by
  ext <;> simp only [E, WeierstrassCurve.map, map_zero, map_neg, map_mul]
  change -(sigmaPlus dco * sigmaPlus dco) = _
  rw [sigmaPlus_apply]
  norm_num [dco, pow_two, sub_eq_add_neg]

theorem curveMinus_coefficients : EMinus = { a₁ := 0, a₂ := 0, a₃ := 0, a₄ := -((75 : ℝ) + 53 * Real.sqrt 2)^2, a₆ := 0 } := by
  ext <;> simp only [E, WeierstrassCurve.map, map_zero, map_neg, map_mul]
  change -(sigmaMinus dco * sigmaMinus dco) = _
  rw [sigmaMinus_apply]
  norm_num [dco, pow_two]

theorem P0_image (σ : K0 →ₐ[ℚ] ℝ) :
    pointMap σ P0 = .some (σ P0x) (σ P0y)
      ((E.toAffine.map_nonsingular σ.injective P0x P0y).mpr P0_nonsingular) :=
  pointMap_some σ P0x P0y P0_nonsingular

theorem signed_multiples (P : Pt) (m : ℤ) : diagonal (m • P) = m • diagonal P :=
  diagonal_zsmul m P

theorem signed_P0_multiples (m : ℤ) : diagonal (m • P0) =
    (m • pointMap sigmaPlus P0, m • pointMap sigmaMinus P0) := diagonal_P0_zsmul m

theorem identity_coordinates : diagonal 0 = (0, 0) ∧
    realZ EPlus (diagonal 0).1 = 0 ∧ realZ EMinus (diagonal 0).2 = 0 := by
  simp [realZ]

theorem injectivity : Function.Injective diagonal := diagonal_injective

theorem total_coordinates (P : Pt) :
    (realZ EPlus (diagonal P).1, realZ EMinus (diagonal P).2) =
    (sigmaPlus (CondZQ.zcoord P), sigmaMinus (CondZQ.zcoord P)) := diagonal_zcoord P

theorem guarded_coordinates (x y : K0) (h : E.toAffine.Nonsingular x y) (hy : y ≠ 0) :
    (sigmaPlus y ≠ 0 ∧
      realZ EPlus (pointMap sigmaPlus (.some x y h)) = -sigmaPlus x / sigmaPlus y) ∧
    (sigmaMinus y ≠ 0 ∧
      realZ EMinus (pointMap sigmaMinus (.some x y h)) = -sigmaMinus x / sigmaMinus y) :=
  ⟨guarded_some sigmaPlus x y h hy, guarded_some sigmaMinus x y h hy⟩

theorem quotient_coordinates (a j : ℤ) (ha : CondZQ.zcoord (a • P0) ≠ 0) :
    realZ EPlus (diagonal (a • P0)).1 ≠ 0 ∧
    realZ EMinus (diagonal (a • P0)).2 ≠ 0 ∧
    (CondZQ.rval a j : ℝ) =
      (realZ EPlus (diagonal (j • P0)).1 / realZ EPlus (diagonal (a • P0)).1 +
       realZ EMinus (diagonal (j • P0)).2 / realZ EMinus (diagonal (a • P0)).2) / 2 :=
  rval_recovery a j ha

/-- The nonzero-index application combines the strict epsilon and guarded quotient interfaces. -/
theorem nonzero_index_bridge (a j : ℤ) (ha : a ≠ 0) :
    CondZQ.zcoord (a • P0) ≠ 0 ∧
    0 < CondZQ.eps a ∧
    realZ EPlus (diagonal (a • P0)).1 ≠ 0 ∧
    realZ EMinus (diagonal (a • P0)).2 ≠ 0 ∧
    (CondZQ.rval a j : ℝ) =
      (realZ EPlus (diagonal (j • P0)).1 / realZ EPlus (diagonal (a • P0)).1 +
       realZ EMinus (diagonal (j • P0)).2 / realZ EMinus (diagonal (a • P0)).2) / 2 := by
  have hz := zcoord_smul_P0_ne_zero a ha
  have hrec := rval_recovery a j hz
  exact ⟨hz, eps_pos_of_ne_zero_index a ha, hrec.1, hrec.2.1, hrec.2.2⟩

/-- Total division sends a zero ordinate to zero; it supplies no nonvanishing claim. -/
theorem zero_ordinate_totalized (x : K0) (h : E.toAffine.Nonsingular x 0) :
    CondZQ.zcoord (.some x 0 h) = 0 ∧
    realZ EPlus (pointMap sigmaPlus (.some x 0 h)) = 0 ∧
    realZ EMinus (pointMap sigmaMinus (.some x 0 h)) = 0 := by
  rw [realZ_pointMap, realZ_pointMap]
  simp [CondZQ.zcoord]

end EllipticModel.TwoRealPlaces.Tests
