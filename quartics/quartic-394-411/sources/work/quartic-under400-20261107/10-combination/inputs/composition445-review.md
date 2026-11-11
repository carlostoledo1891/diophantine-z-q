# Independent review of the 445-variable primary-parameter change

Reviewer: `/root/astra_bl5_models`. Decision: accepted for this frozen research candidate. No repository or manuscript change is authorized by this review, and 445 does not meet the fewer-than-400 milestone.

## Frozen inputs and outputs

- Source453: `f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f`.
- Candidate445: `173e0e79a5eb9404917e952117666f3de7920ca876eae2163ac0d20981414e3e`.
- Polynomial445: `83ac2963bc5dc2e6f0b5b8165da6c9af1f36a264b474e466e74bcc200e035844`.
- Certificate445: `255ffe0eba53508ad27bd22d8438332546f7312b583bb66b7ec609894847aa0d`.
- Author report: `d7543f7af19c485b8f5420d14df630d95a56cfc13c047b61108310c49672b326`.

I read the author report and standalone verifier, inspected the exact old and new component equations and consumer checks, and reran the verifier. I then added checks of all five physical retained chart relations, coordinate and row coverage, fixed-parameter/input preservation, degree, specialized content and coefficient maximum. The records are `replay445.py`, `445-replay.log`, and `445-replay-result.json`; no source artifact was written.

## Source and nonzero denominators

The relevant source is the frozen v12 manuscript, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. I read its chart equations and proof at lines 19331–19408 and its primary-ratio definition at lines 19912–19920. The point chart is `x=h^2`, `j^2=x^2-D`, with `D=(3-sqrt(2))^2`, and its parameter is `z=-h/j`. The primary ratios are exactly `L_i=z(U_i)/z(H)`.

The nonzero fact used here follows directly from these retained equations over K=Q(sqrt(2)). If h=0 then j^2=-D, impossible at a real embedding. If j=0 then h^4=D, so h^2 is plus or minus `3-sqrt(2)`. Taking norms gives `Norm(h)^2=7`, impossible for rational Norm(h). Thus every h_i and j_i is nonzero for every rational component solution of the retained chart, not only for chosen complete witnesses. Their field norms are nonzero, so division has rational component formulas. No additional guard, rank claim, or valuation-ring requirement is introduced.

## Exact maps and consumers

The old equations are `j_i*z_i+h_i=0` for i=0,...,4 and `z_0*L_i-z_i=0` for i=1,...,4. The new system retains the two slots of z_0 but assigns them `s=j_0/h_0=-1/z_0`, with equations

`h_0*s-j_0=0`,

`j_i*L_i-h_i*s=0` for i=1,...,4.

Starting with an old solution, set s=-1/z_0, keep all other retained values, and forget z_1,...,z_4. The old equations imply every new equation. Conversely, reconstruct all five old values as `z_i=-h_i/j_i`. The first new equation gives s=j_0/h_0, and the others give `L_i=h_i*s/j_i=z_i/z_0`. These assignments recover all old equations and are mutual inverses after accounting for the changed slots. They preserve every point and every L_i, as well as the input.

The actual incidence check matters: the ten old parameter coordinates occur only in the ten parameter component definitions and eight primary-ratio definitions. The verifier matches those equations against literal frozen rows, up to nonzero constant normalization. It removes precisely eight rows and coordinates, replaces precisely ten rows, and compares every outside residual object unchanged, including IDs, coefficients and metadata. Only slots 142 and 143 are renamed; the deleted slots are 146/147,150/151,154/155,158/159. All other retained coordinate objects are identical. No scalar, alternate logarithm, detector or point-chart consumer receives s in place of an old z value.

Although s has negative valuation whenever z_0 has positive valuation, the witness domain is rational points, not integral local points. Nothing tests s directly. The old z values reconstructed for the arithmetic proof and the retained L_i have their exact old values. Thus no primary-depth, integrality-transfer, height, or completeness estimate changes. In particular this local equivalence composes with the preceding rational-log and expanded comparison charts without changing their actual objects or order of arithmetic choices.

## Polynomial verification and conclusion

Full primitive-row sum-of-squares expansion agrees with the frozen polynomial: 445 total variables, 444 witnesses, 422 quadratic residuals, degree four and 6,568 monomials. The fixed coefficient is still C=3^(2^25). The coefficient of x_1^4 is exactly 1, with no other C power on that monomial, and the only C^2 contribution is `16*C^2*x_57^2`, with no lower-C contribution there. Ordinary coefficients have bit length below 2048 and linear-C coefficients are bounded by 48, proving content 1 and maximum absolute coefficient `16*3^(2^26)` after specialization.

This is an exact rational witness equivalence on the whole retained chart domain. Both rational input projections therefore agree with the independently reviewed source453. No defect or new arithmetic qualification was found. Acceptance covers only the frozen files above and does not extend to subsequent optimizations.
