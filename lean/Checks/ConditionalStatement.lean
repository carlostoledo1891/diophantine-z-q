module

public import CondZQ
public import Frozen.BoundedIntegerPolynomial
import Lean.Util.CollectAxioms

/-!
The statement check of the conditional theorem against the frozen target. The frozen file is
compiled only for this check, into the check's own output directory, so that its theorem's type
can be named; its value (the `sorry`) is never used. Compiled by
`scripts/check_lean_contrib.py --build`.

1. `CondZQChecks.statement_is_the_frozen_target` has as its type
   `type_of% @ZInQ.exists_bounded_integer_polynomial_defining_integers`, taken from the frozen
   file, never retyped, and is proved by the conditional theorem applied to the eight
   hypotheses: it elaborates only if the two statements agree up to definitional unfolding.
2. The `run_cmd` below checks the stronger, syntactic fact: the conditional theorem's type is
   exactly `HypM → HypH → HypPC → HypC → HypLT → HypCC → HypH1 → HypH2 → τ`, where `τ` is the
   frozen theorem's type, equal as a Lean expression (`Expr.equal`, binder names included), and
   each of the eight is a `Prop`. Neither theorem may use an axiom outside `propext`,
   `Quot.sound` and `Classical.choice`.
-/

public theorem CondZQChecks.statement_is_the_frozen_target
    (hM : CondZQ.HypM) (hH : CondZQ.HypH) (hPC : CondZQ.HypPC) (hC : CondZQ.HypC)
    (hLT : CondZQ.HypLT) (hCC : CondZQ.HypCC) (hH1 : CondZQ.HypH1) (hH2 : CondZQ.HypH2) :
    type_of% @ZInQ.exists_bounded_integer_polynomial_defining_integers :=
  CondZQ.exists_bounded_integer_polynomial_defining_integers_of_eight_hypotheses
    hM hH hPC hC hLT hCC hH1 hH2

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let thm := ``CondZQ.exists_bounded_integer_polynomial_defining_integers_of_eight_hypotheses
  let frozen := ``ZInQ.exists_bounded_integer_polynomial_defining_integers
  let hyps : List Name := [``CondZQ.HypM, ``CondZQ.HypH, ``CondZQ.HypPC, ``CondZQ.HypC,
    ``CondZQ.HypLT, ``CondZQ.HypCC, ``CondZQ.HypH1, ``CondZQ.HypH2]
  let some ti := env.find? thm | throwError "missing {thm}"
  let some fi := env.find? frozen | throwError "missing {frozen}"
  let mut ty := ti.type
  for h in hyps do
    match ty with
    | .forallE _ dom body _ =>
      unless dom.equal (.const h []) do throwError "found hypothesis {dom} where {h} was expected"
      if body.hasLooseBVars then throwError "the conclusion depends on hypothesis {h}"
      ty := body
    | _ => throwError "fewer than eight hypotheses"
  unless ty.equal fi.type do throwError "the conclusion is not the frozen theorem's type"
  for h in hyps do
    let some ci := env.find? h | throwError "missing {h}"
    unless ci.type.equal (.sort 0) && ci.levelParams.isEmpty do throwError "{h} is not a Prop"
  for n in [thm, ``CondZQChecks.statement_is_the_frozen_target] do
    for ax in ← collectAxioms n do
      unless ax == ``propext || ax == ``Quot.sound || ax == ``Classical.choice do
        throwError "Unexpected axiom {ax} in {n}"
  let names := ",".intercalate (hyps.map toString)
  logInfo m!"STATEMENT_CHECK_PASS theorem={thm} hypotheses={names} conclusion=type_of% {frozen}"

#print axioms CondZQChecks.statement_is_the_frozen_target
