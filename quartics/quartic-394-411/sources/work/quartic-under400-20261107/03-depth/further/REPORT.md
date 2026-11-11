# Eight more coordinates removed by reversing the common primary parameter

The frozen 453-variable candidate becomes a 445-variable candidate. There are 422 quadratic residuals, and their primitive integer sum of squares has degree four and 6,568 monomials. This is an exact change of rational witnesses. It preserves every point, every primary ratio, and every test, so it requires no new approximation estimate. Independent acceptance of this new implementation is pending.

## Exact change

Let the five primary chart points be H, UA, US, UT, UZ, indexed by i=0,...,4. Write their existing chart coordinates as h_i,j_i. The old equations are

    j_i z_i + h_i = 0                    (0 <= i <= 4),
    z_0 L_i - z_i = 0                    (1 <= i <= 4).

Each is an equation in K=Q(sqrt(2)), hence two rational component equations. Keep the two physical coordinates 142,143, formerly z_0, but give them the new value

    s = -1/z_0 = j_0/h_0.

Replace the equations above by

    h_0 s - j_0 = 0,
    j_i L_i - h_i s = 0                  (1 <= i <= 4).

Delete the eight rational coordinates 146,147,150,151,154,155,158,159 that formerly represented z_1,...,z_4. All equations remain quadratic. No auxiliary coordinate is added.

## Domain, forward map, and reverse map

The retained chart has x_i=h_i^2 and j_i^2=x_i^2-D, where D=(3-sqrt(2))^2. Both h_i and j_i are nonzero for every rational component solution, not merely for the points selected during completeness. Indeed, h_i=0 would imply j_i^2=-D, impossible under a real embedding. If j_i=0 then h_i^2=+(3-sqrt(2)) or -(3-sqrt(2)). Taking field norms would give Norm(h_i)^2=7, impossible for a rational number Norm(h_i). This is the same nonvanishing proof already present in Proposition v9chart:prop:chart of the frozen manuscript, lines 19358-19376. It is not a new assertion that needs an additional inverse guard.

Forward: from an old witness, keep every retained coordinate other than 142,143 unchanged, and set s=-1/z_0. The old chart and parameter equations give z_0=-h_0/j_0, so this is a defined element of K. Then h_0 s=j_0. From z_0 L_i=z_i=-h_i/j_i, we obtain j_i L_i=h_i s.

Reverse: from a new witness, keep all other retained coordinates unchanged, reconstruct old z_i=-h_i/j_i for i=0,...,4, and put these values into the old slots. The new first equation forces s=j_0/h_0=-1/z_0. Each other new equation forces L_i=h_i s/j_i=z_i/z_0. Thus all old equations hold. Both compositions recover the starting witness, and both fix the input X. The witness maps use field division in K; their rational component formulas divide by nonzero norms of h_0,j_0,...,j_4. These norms cannot vanish for nonzero elements of Q(sqrt(2)). No extension of the quantified field occurs.

There is no added local integrality condition on s. For example, at a place where v(z_0)>=20, s can have valuation at most -20. That is permitted because the circuit variables range over Q, not over a valuation ring. No test consumes s directly. The original ratios L_i have exactly their original values, so their local valuation estimates, the primary/alternate comparison, the scalar height argument, and all real inequalities remain unchanged. The scalar preparation rows do not consume any of the changed or deleted slots.

## Literal row and consumer audit

The builder first matches every old component equation against the actual frozen rows, allowing only a nonzero rational scalar multiple. This avoids relying on stale semantic-value metadata. The old z variables occur in exactly eighteen rows: ten parameter component definitions and eight L_i component definitions. Eight rows are removed and ten are replaced. All other residual objects are identical, including their coefficients, row IDs, and metadata. In particular primary f_i, the root charts, the alternate logarithms, every detector, and the scalar constraints are untouched.

The two retained coordinates are renamed primary.negativeReciprocalZ0.0 and .1. Their coordinate IDs stay 142 and 143. Every other retained coordinate object is identical. The standalone checker verifies the entire old-variable incidence, these exact field identities, every outside row and coordinate, the absence of deleted variables, and the complete primitive sum of squares. It is a separate implementation and does not import or execute the builder.

The tempting analogous deletion of alternate z_i variables is not claimed. The actual compiled alternate rows already contain ell_0 L'_i-z_i G_i, rather than a separate ell_i. Substituting z_i=-x_i/y_i directly would introduce cubic products. That initial lead was rejected after checking the literal row bindings.

## Frozen artifacts and verification

Source: ../../10-combination/rational453-ir.json.

    source SHA256     f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f
    candidate445      173e0e79a5eb9404917e952117666f3de7920ca876eae2163ac0d20981414e3e
    polynomial445     83ac2963bc5dc2e6f0b5b8165da6c9af1f36a264b474e466e74bcc200e035844

The complete machine-readable record is certificate445.json. The builder is primary_reciprocal.py. Run the read-only verifier with the available Python runtime and the argument verify_primary.py. Its observed result was PASS for 445 variables, 422 residuals, and 6,568 monomials.

The arithmetic source is manuscripts/quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9. Relevant passages are the chart and domain proof at lines 19331-19408 and the primary ratio definition at lines 19912-19920. This proposal changes the compiled representation of those exact primary ratios. The earlier rational logarithm proposal and all frozen files remain untouched. This finite check and author proof are evidence for an independent reviewer; they are not an independent acceptance record.
