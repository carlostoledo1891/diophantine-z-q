# CondZQ: hypothesis-to-manuscript ledger

`CondZQ.exists_bounded_integer_polynomial_defining_integers_of_eight_hypotheses` proves the statement of the frozen target `ZInQ.exists_bounded_integer_polynomial_defining_integers` from the eight hypotheses below. **None of the eight is proved here, so the theorem is conditional.** It is not a proof of the frozen target, and if any hypothesis is false it says nothing.

Each hypothesis is a `Prop` in `CondZQ/Hypotheses.lean`, and its docstring names its source. Each one is a reading of the manuscript, to be checked for fidelity; this ledger lists the readings, and a successful build does not certify them.

**TeX line numbers** refer to the November 5 manuscript `diophantine_zq.tex` at `97cec7fd`. Current `main` preserves it byte for byte as `docs/theorem-application-audit/source/audited-baseline.tex` (SHA-256 `cb1148cd6c7769d2af3f1636b60ff0ada4b40431978d1e98d0c339274b3d792b`), so the numbers are the same in both files. They were re-checked against that file at `036cebe4`. The frozen target is the original polynomial's statement, and that is the manuscript it formalizes; the quartic versions have no frozen Lean target.

Status words: **assumed** means a hypothesis of the theorem, not proved here. **Proved** means a theorem here with axioms `propext`, `Quot.sound` and `Classical.choice` only.

## The eight hypotheses (all assumed)

| Name | Statement (summary) | Manuscript source | Snapshot modules used |
| --- | --- | --- | --- |
| `HypM` | ∃ `P` over `Fin (15 + 35134)` with `SizeOK P 214` and `Sol P (A,B,C) ↔ ∃ a b, A = ι a ∧ B = ι b ∧ C = ι(ab)` for all rational 5-codes | premise M (TeX 96–97), `sec:mult` (TeX 1123–1758), `prop:box` (1225), `prop:fixed-prime-pattern` (1267); Green–Tao 2010, Green–Tao–Ziegler, Green–Tao (Möbius–nilsequences); template `multiply` (35,134 witnesses, height 214) | — |
| `HypH` | `∀ u ∉ 𝒞, h(u) ≤ H_6(S_ht)·M_{S_ht}(u)^24`, with `S_ht = {p ≤ 324}` and `R = max(D, 317, 10^12)` | premise H (TeX 98–99), `thm:height` (TeX 404–408), `sec:height` (377–972), De Rham appendix (10936–11007); Faltings 1983/1988, Scholze 2013, Pan 2022, Lin–Yang, Baba–Granath | `HeightConstantComparison.h6` (`H_6`), `rationalLogHeight` (`h`) |
| `HypPC` | `∀ B, IsSquare B.den ∧ 0 < B < 1/2 ∧ (∀ p ∈ {2,3,5,7,13}, v_p(B) ≥ 4) → Φ(B)` | premise PC (TeX 100–101), `hyp:PC` (TeX 1001–1004); from `hyp:RC` (1005) by `sec:pole` (Kato 2004, Gross–Zagier, Kolyvagin, Poonen–Stoll, BCDT) | `PolePolynomial.polePolynomial` (`Q_pole`, defining `Φ`) |
| `HypC` | ∃ `P` over `Fin (11 + 292890196199)` with `SizeOK P 235` and `Sol P (N,K,t) ↔ ∃ n κ a l j, N = ι n ∧ K = ι κ ∧ accept n κ a l j ∧ \|t − r(a,j)\| < ε_l` | premise C (TeX 102–104), `sec:compiler` (5745–6093), the `Close` relation (6103–6106); AFP `DPRM_Theorem`; recipe `close` (292,890,196,199 witnesses, height 235) | `HeightConstantComparison.h6` (in `accept`) |
| `HypLT` | ∃ `P` over `Fin (17 + 137)` with `SizeOK P 249`. Sound: `t ∉ 𝒞`, `κ ≠ 0`, `Sol P (ι n, ι κ, ι(κn), t, B)` and `Φ(B)` give `M_{S_ht}(t) ∣ κF(n)`. Complete: `n ∉ 𝒞` gives some `κ ≠ 0` and `B` with `PCInput B` and `Sol P (ι n, ι κ, ι(κn), n, B)` | `lem:test` (TeX 6151–6200), `lem:test-complete` (6202–6235); Silverman IV.5.5, IV.6.4, VII.6.3, IV.2.3(a); template `value.test` less `multiply` and `pole` (35,282 − 35,134 − 11 = 137 witnesses, height 249) | `PolePolynomial.polePolynomial` (in `Φ`) |
| `HypCC` | `∀ n κ, n ∉ 𝒞 → κ ≠ 0 → ∃ a l j, accept n κ a l j` | `eq:close-complete` (TeX 6114, in 6109–6127); compactness of `E(ℝ)×E(ℝ)`, Silverman IV.2.3(a) | `HeightConstantComparison.h6` (in `accept`) |
| `HypH1` | `H_max < 2^(W³)`, where `W = 4·∏_{p≤324} p` and `H_max` is the largest of the first 22 primes `> 324` in each unit class mod `W` | proof of `prop:cutoff` (TeX 6297–6308); Bennett–Martin–O'Bryant–Rechnitzer, Thm 1.2, (1.10)–(1.11), Cor. 6.17, `A = 1` | — |
| `HypH2` | `∃ m, 1 ≤ m ≤ N_s^10` with `1/x([m]P₀) = (a+bs)/c`, `c > 0`, `gcd(a,b,c) = 1`, `N_s⁴ ∣ a, b`, `gcd(c, N_s) = 1` (so `M_0 ≤ N_s^10`) | proof of `prop:cutoff` (TeX 6310–6349); Silverman VII.2.1, V.1.1 | — |

`SizeOK P h` is `totalDegree P ≤ (T+1)^(8h) ∧ ‖P‖₁ ≤ 2^((T+1)^(8h))`, the majorant of `sec:size` (TeX 6390–6418) with `T` the literal cutoff. The heights are those of `construction/ordinary-integer-polynomial-size-bounds.json`.

`HypM`, `HypC` and `HypLT` are existential. Each is implied by the manuscript's premise for that template together with premise B (TeX 105–107); none of them mentions the saved JSON. The assembled polynomial is not the saved `P_*`, which the frozen target, existential in `P`, allows. It has no `member` call, since the multiplication relation types its inputs. It has no `value.exceptions` template: a second factor evaluates the same sum of squares at `u = t + 1000 ∉ 𝒞`, sharing the witnesses. Its 292,890,231,498 witnesses are padded into the 292,890,231,904 slots. Premise B for `P_*` itself (that the saved expression denotes a polynomial of the stated size) is therefore not used.

## Premises that are proved, not assumed

| Piece | Statement | Manuscript source | Where |
| --- | --- | --- | --- |
| `prop:generator`, first clause | `addOrderOf P₀ = 0`: `P₀` has infinite order on `E` over `ℚ(s)` | TeX 268–270, premise G (93–95). The manuscript's proof uses reductions at `(17,s−6)`, `(23,s−5)` and torsion injection (293–295); the proof here is 2-adic, by the dyadic step of the proof of `prop:cutoff` (6335–6338) | `EllipticModel.P0_addOrderOf` (`EllipticModel/InfiniteOrder.lean`), used by `CondZQ.iota_injective` |
| `prop:generator`, second clause | `2E(K₀) = ℤP₀` is not stated. `HypM` and `HypC` state their zero sets on the codes `ι(n)` directly, which consumes it | TeX 268–270 | — |
| `hyp:RC` | not stated: it is used only to prove PC (TeX 1111) | TeX 1005 | — |

## What is proved between the hypotheses and the conclusion

| Piece | Statement | Manuscript source | Snapshot modules used |
| --- | --- | --- | --- |
| `Cutoff.T_eq_closed`, `T_lt_triplePower` | Under H1 and H2: `R = D`, `max(1, C_cm, Q_D^17) = Q_D^17`, and `T = (96·10^13)^13·D^(2210·G_0²·D³) < 2^(2^(2^9013))` | `prop:cutoff` (TeX 6285–6359), the quantitative part of premise B | `HeightConstantComparison` (`d`, `d0`, `g0`, `h6ForDegree`, `q0ForDegree`, `rForDegree`, `cCmForDegree`, `bCmForDegree`, `e0ForDegree`, `degreeFromBase`), `ExplicitCutoffBounds` (`t`, `d`, `g0`, `factorialBase`, `t_lt_triplePower`) |
| `Bridge.iota_injective` | `ι` is injective | TeX 263–266 | — (uses `EllipticModel.P0_addOrderOf`) |
| `Bridge.close_sound` | An accepting run with `\|t − r\| < ε_l` gives `\|t − n\| < e^{−B(n,κ)}` | `eq:close-sound` (TeX 6112, in 6109–6113) | — |
| `Bridge.eq_of_close_of_dvd` | An accepting run, the close window, `lem:test`'s divisibility and H give `t = n` | `sec:bridge`, the exact ordinary value (TeX 6237–6262) | `RationalSeparation.eq_int_of_real_abs_sub_lt_exp_neg_of_height_le` |
| `Assembly.assembled_iff` | The rational zero projection of the assembled polynomial is `ℤ` | `sec:bridge`, `sec:syntax` (sums of squares, products, private blocks; TeX 166–171) | `PolePolynomial.polePolynomial` |
| `Assembly.pole_bound` | `deg Q_pole ≤ 75`, `‖Q_pole‖₁ < 2^200` | TeX 975–987 | `PolePolynomial.polePolynomial`, `bitIndex` |
| `Assembly.bound_assembled` | Degree `≤ 6X` and ℓ¹ `≤ 2^(6X+7)` from components bounded at `X` | `sec:size` | — |
| `Main.tower_bounds` and the theorem | Padding into `Fin 292890231905`; `6(T+1)^1992 < 2↑↑7` and `2^(6(T+1)^1992+7) < 2↑↑8` | TeX 6431–6438 | `NumericalTowerBounds` (`degree_bound_of_cutoff_bound`, `coefficient_bound_of_cutoff_bound`, `triplePower_9014_lt_tower_seven`, `quadruplePower_9014_lt_tower_eight`, `tower_succ`) |

## Not discharged, and why

Every hypothesis above remains open in this development:

- `HypM`, `HypH` and `HypPC` rest on the arithmetic literature cited in their rows.
- `HypLT` and `HypCC` rest on the formal logarithm over the completions of `ℚ(s)`, the finite index of formal neighbourhoods and the topology of `E(ℝ)`. Mathlib v4.35.0 has none of these.
- `HypH1` and `HypH2` are the explicit inputs of the proof of `prop:cutoff`.
- `HypC` is finite and combinatorial. Discharging it needs four pieces: the precision machine as a Lean program over exact `ℚ(s)` arithmetic, its correctness against `accept`, a Diophantine compilation over `ℕ` with an explicit variable count, and the translation of naturals into point codes through the multiplication relation. The last piece would leave C discharged modulo M.
