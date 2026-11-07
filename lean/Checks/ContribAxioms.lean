module

import all EllipticModel
import all CondZQ
import Lean.Util.CollectAxioms

/-!
Axiom audit of the contributed libraries (not of the accepted `ZInQ` snapshot, which
`Checks/Axioms.lean` audits). Every declaration of every module under a contributed root,
compiler-generated ones included, must depend on no axiom outside `propext`, `Quot.sound`
and `Classical.choice`; a `sorry` would appear here as `sorryAx` and fail the audit.
Compiled by `scripts/check_lean_contrib.py --build`.
-/

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let roots : List Name := [`EllipticModel, `CondZQ]
  let mut checked : Nat := 0
  let mut modules : Array Name := #[]
  for idx in [:env.header.modules.size] do
    let modName := env.header.modules[idx]!.module
    if roots.any (·.isPrefixOf modName) then
      modules := modules.push modName
      let names := env.header.moduleData[idx]!.constNames.qsort (·.toString < ·.toString)
      for name in names do
        let axioms ← collectAxioms name
        for ax in axioms do
          unless ax == ``propext || ax == ``Quot.sound || ax == ``Classical.choice do
            throwError "Unexpected axiom {ax} in {name} from {modName}"
        checked := checked + 1
        logInfo m!"AXIOM_CHECK {name}: {axioms.toList}"
  logInfo m!"CONTRIB_AXIOM_AUDIT_PASS declarations={checked} modules={modules.size}"

#print axioms EllipticModel.P0_addOrderOf
#print axioms EllipticModel.P0_not_isOfFinAddOrder
#print axioms CondZQ.exists_bounded_integer_polynomial_defining_integers_of_eight_hypotheses
