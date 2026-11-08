module

import all Examples.TwoRealPlaces
import all Examples.TwoRealPlacesCheck
import Lean.Util.CollectAxioms

/-! Audit every declaration in the new application, its tests, and its project import closure. -/

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let mut checked := 0
  let mut modules := 0
  for idx in [:env.header.modules.size] do
    let modName := env.header.modules[idx]!.module
    if Name.isPrefixOf `Frozen modName then
      throwError "Quarantined module imported: {modName}"
    if [`EllipticModel, `CondZQ, `ZInQ, `Examples].any (·.isPrefixOf modName) then
      modules := modules + 1
      let names := env.header.moduleData[idx]!.constNames
      for name in names do
        let axioms ← collectAxioms name
        for ax in axioms do
          unless ax == ``propext || ax == ``Quot.sound || ax == ``Classical.choice do
            throwError "Unexpected axiom {ax} in {name} from {modName}"
        checked := checked + 1
      logInfo m!"TWO_REAL_PLACES_MODULE {modName}: {names.size} declarations"
  unless modules == 11 do
    throwError "Expected exactly 11 project modules, found {modules}"
  logInfo m!"TWO_REAL_PLACES_AXIOM_AUDIT_PASS declarations={checked} modules={modules}"

#print axioms EllipticModel.TwoRealPlaces.diagonal
#print axioms EllipticModel.TwoRealPlaces.diagonal_injective
#print axioms EllipticModel.TwoRealPlaces.diagonal_P0_zsmul
#print axioms EllipticModel.TwoRealPlaces.diagonal_zcoord
#print axioms EllipticModel.TwoRealPlaces.guarded_some
#print axioms EllipticModel.TwoRealPlaces.rval_recovery
