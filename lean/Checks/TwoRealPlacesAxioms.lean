module

import all EllipticModel.Curve
import all ZInQ.PrecisionArithmetic
import all ZInQ.PrecisionAlgorithms
import all ZInQ.HeightConstantAlgorithm
import all ZInQ.HeightConstantComparison
import all ZInQ.PoleValuation
import all ZInQ.PolePolynomial
import all ZInQ.RationalSeparation
import all CondZQ.Model
import all Examples.TwoRealPlaces
import all Examples.TwoRealPlacesCheck
import Lean.Util.CollectAxioms

/-! Audit every declaration in the new application, its tests, and its project import closure. -/

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let mut checked : Nat := 0
  let mut modules : Nat := 0
  let mut privateTotal : Nat := 0
  let mut generatedTotal : Nat := 0
  let mut privateNames : Array Name := #[]
  for idx in [:env.header.modules.size] do
    let modName := env.header.modules[idx]!.module
    if Name.isPrefixOf `Frozen modName then
      throwError "Quarantined module imported: {modName}"
    if [`EllipticModel, `CondZQ, `ZInQ, `Examples].any (·.isPrefixOf modName) then
      unless env.header.modules[idx]!.importAll && env.header.modules[idx]!.hasData do
        throwError "Full private inventory not loaded: {modName}"
      modules := modules + 1
      let mut privateCount : Nat := 0
      let mut generatedCount : Nat := 0
      let mut axiomNames : Array Name := #[]
      let names := env.header.moduleData[idx]!.constNames
      for name in names do
        unless ((env.setExporting false).find? name).isSome do
          throwError "Missing declaration: {name} from {modName}"
        if isPrivateName name then
          privateCount := privateCount + 1
          privateNames := privateNames.push (privateToUserName name)
        -- Count internal/generated names independently of their private prefix.
        if (privateToUserName name).isInternalDetail then
          generatedCount := generatedCount + 1
        let axioms ← collectAxioms name
        for ax in axioms do
          unless axiomNames.contains ax do
            axiomNames := axiomNames.push ax
          unless ax == ``propext || ax == ``Quot.sound || ax == ``Classical.choice do
            throwError "Unexpected axiom {ax} in {name} from {modName}"
        checked := checked + 1
      privateTotal := privateTotal + privateCount
      generatedTotal := generatedTotal + generatedCount
      logInfo m!"TWO_REAL_PLACES_MODULE {modName}: declarations={names.size} private={privateCount} generated_internal={generatedCount} importAll=true axioms={axiomNames}"
  for witness in #[`ZInQ.PrecisionArithmetic.saturate_mul_left,
      `ZInQ.PrecisionAlgorithms.advance_correct,
      `ZInQ.HeightConstantAlgorithm.ascFactorial_front,
      `ZInQ.PolePolynomial.coordinates_bit,
      `ZInQ.sub_int_eq_num_sub_mul_den_div] do
    unless privateNames.contains witness do
      throwError "Private supplier helper missing: {witness}"
  unless modules == 11 do
    throwError "Expected exactly 11 project modules, found {modules}"
  logInfo m!"TWO_REAL_PLACES_AXIOM_AUDIT_PASS declarations={checked} modules={modules} private={privateTotal} generated_internal={generatedTotal}"

#print axioms EllipticModel.TwoRealPlaces.diagonal
#print axioms EllipticModel.TwoRealPlaces.diagonal_injective
#print axioms EllipticModel.TwoRealPlaces.diagonal_P0_zsmul
#print axioms EllipticModel.TwoRealPlaces.diagonal_zcoord
#print axioms EllipticModel.TwoRealPlaces.guarded_some
#print axioms EllipticModel.TwoRealPlaces.rval_recovery
