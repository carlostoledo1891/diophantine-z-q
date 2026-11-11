# Consolidating the scalar denominator saves two variables

The frozen 498-variable system admits an exact rewrite with 496 total variables, 495 witnesses, and 465 quadratic residuals. Its primitive integer sum of squares has degree four, 24,699 monomials, content one, and maximum coefficient `16*3^(2^26)`. The fixed parameter remains `C=3^(2^25)`.

This is a local rational equivalence on the existing input domain. It introduces no new arithmetic hypothesis and does not change the scalar norm node consumed by the rest of the construction. The author's independent implementation checks passed; non-author acceptance is pending.

## Equations and maps

Write the retained scalar ratio as `z0+z1*sqrt(2)` and retain the existing contact polynomial

```
beta = 2*X^2+3
r = beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1).
```

The old subsystem has six coordinates for `r^-1,r^-2,r^-4,r^-8,r^-16,r^-32`, two leaves `U=z0*r^-32,V=z1*r^-32`, a coordinate `V2=V^2`, and the node `B=U^2+r*V2`. The last node is consumed through the unchanged equations for its square and the scalar root.

Replace the six inverse powers by six forward powers

```
p2=r^2, p4=p2^2, p8=p4^2, p16=p8^2, p32=p16^2, p64=p32^2.
```

Delete U and V. Repurpose the old V2 coordinate as `S=z1^2` and replace the node equation by

```
p64*B = z0^2+r*S.
```

Every equation is quadratic, because r is already an affine expression in retained coordinates. No other consumer of the repurposed square exists.

For every rational X, r is nonzero. Indeed beta>=3, so the first, second, fourth and fifth factors are nonzero. The third could vanish only if X^2=1199. A rational square which is an integer is an integer square, whereas 34^2<1199<35^2. The exact checker reconstructs the actual stored r from its defining rows and verifies this five-factor polynomial identity in beta, as well as the retained input-square equation. Thus this argument applies to all rational solutions of the unchanged surrounding rows, not merely intended witnesses.

Forward: from an old solution, assign the six positive powers and S=z1^2, and retain the old B. Then

```
r^64*B = r^64*((z0/r^32)^2+r*(z1/r^32)^2)
       = z0^2+r*z1^2.
```

Backward: a new solution has p64=r^64!=0. Restore the six inverse powers uniquely, set U=z0/r^32 and V=z1/r^32, and restore the old V2 as V^2. The new equation gives exactly B=U^2+r*V^2. Both maps preserve B and every outside coordinate, including the scalar root, scalar pole input, anchor, detector products, and original input. The maps are mutual inverses after accounting for the changed meaning of the private square coordinate.

Since every surrounding coordinate is preserved, all previous soundness and simultaneous-completeness arguments apply without any new choice of primes, points, or pole witnesses. In particular this is independent of the order-12 versus order-10 detector choice and of changes to private pole encodings.

## Exact transport details

Source: `quartics/quartic-498-514/candidate498-ir.json`.
Source SHA-256: `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.

Remove coordinate IDs 490-495 and 537-538. Add IDs 600-605 for the forward powers. Repurpose coordinate539 as the unscaled z1 square. Remove residual IDs456-461 and507-508. Change only residuals509 and510; add residuals600-605. Node B is coordinate540 and remains unchanged. The source ratio coordinates are508 and509; coordinate IDs and residual IDs have independent namespaces.

Candidate SHA-256: `780dbfb2cf04383062912a6ac68b780a025cf0eb94b2d567a05927c732356e48`.
Polynomial SHA-256: `5f294535464f2d3db05be9492ef73fe9045ef4578a6c44a7d04a0621eb6a875d`.

`build.py` produces `candidate496-ir.json` and `polynomial496.json`. `verify.py` imports neither the producer nor its polynomial functions. It checks all unchanged rows and coordinate incidences, reconstructs all old and new equations, proves the contact polynomial identity, and independently expands the sum of primitive integer residual squares by upper-triangular collection. `VERIFICATION.json` records the result.

Run `python -B build.py` and `python -B verify.py` from this directory. Both use only the standard library. The polynomial keeps C symbolic, so no enormous integer expansion occurs. No released artifact, previous work file, or manuscript was modified.
