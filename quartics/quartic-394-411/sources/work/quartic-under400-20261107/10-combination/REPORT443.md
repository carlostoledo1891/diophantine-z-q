# Shared reciprocal removes the scalar z pair

The frozen candidate `scalar443-ir.json`, SHA256 `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`, has 443 total variables, 442 witnesses, 420 quadratic residuals and 6,616 quartic monomials. The source `inputs/accepted445-ir.json` has SHA256 `173e0e79a5eb9404917e952117666f3de7920ca876eae2163ac0d20981414e3e`. This exact reduction was suggested by agent bl5 and implemented by the combination agent. Fresh non-author acceptance from the parent is pending.

Use the already accepted common primary reciprocal s=j_H/h_H=-1/z_H. The retained H chart proves h_H and j_H nonzero, hence s nonzero, for every rational solution. The scalar reciprocal chart has the previously defined affine expressions T and B=aN, and its physical equation is T*z_S+B=0. Its ratio equation is h_H*rho+j_H*z_S=0. Eliminate the two rational coordinates of z_S and replace both field equations by

    T*rho-B*s=0.

This is quadratic because T and B are affine expressions in retained scalar-chart coordinates. The field elements s and rho use their existing pairs of coordinates. No coordinate is added or redefined.

For the forward direction, the old equations and h_H*s=j_H imply the displayed equation. One exact identity checked by `verify_scalar443.py` is

    h_H*(T*rho-B*s)
      = T*(h_H*rho+j_H*z_S)
        - h_H*s*(T*z_S+B)
        + T*z_S*(h_H*s-j_H).

Since h_H is nonzero, every old witness yields a new witness by forgetting z_S. For the reverse direction put z_S=-rho/s. The new equation gives T*z_S+B=0, and h_H*s=j_H gives h_H*rho+j_H*z_S=0. The old ratio equation already forces this z_S, so the maps are mutually inverse. No nonzero condition on T, B, rho or z_S is used. All retained scalar values and all point values are unchanged.

The removed coordinate IDs are exactly506 and507. Their complete consumer set is exactly the four component rows472 through475. The two Sscalar.z rows are deleted and the two scalar.zRatio rows are replaced. The retained ratio coordinates508 and509, including their squared consumers in the scalar norm tree, are unchanged.

`build_scalar443.py` constructs the candidate. The separate `verify_scalar443.py` imports no producer, matches every literal source equation, checks the polynomial identity and complete incidence, compares every unaffected row and coordinate, and expands the full primitive sum of squares. It passed. The degree is four, content is one, and the largest coefficient remains exactly16*3^(2^26). The polynomial SHA256 is `b2d2600ff4d088e3ff2d5ec398218c5f255770d17767948173ce2fd3c5eb7d68`.

This reduction changes no arithmetic approximation, prime choice, positivity argument or quantified field. It does not reach the below400 publication threshold. All earlier accepted files remain frozen.
