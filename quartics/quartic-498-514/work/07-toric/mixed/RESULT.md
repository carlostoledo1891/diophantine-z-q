# Mixed-depth toric reduction to 516 coordinates

The 519-coordinate mixed-depth candidate from `03-depth/beta12/final/candidate-ir.json` admits an exact replacement with 516 coordinates, 515 witnesses, and 485 quadratic residuals. Its primitive integer sum of squares has degree four and 24,977 monomials. The source SHA-256 is `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.

This reduction preserves both q12 and q40 and all their consumers. It uses the existing `E1.power3` and `E12.power2` coordinates. It changes no arithmetic assertion of the mixed-depth source. Its arithmetic qualifications therefore remain those of `03-depth/REPORT.md`.

## Exact equations

For each of the three detectors write E for eWeight, q for q1, Q for the retained E1.power3=q^3, and R for the retained E12.power2=q12^2. Replace the six old pure-power coordinates by five coordinates a,b,u,v,t, and retain both output coordinates q12 and q40. Impose

```
E a = 1
E b = a^2
b u = E q
b v = u^2
Q q12 = v^2
q t = E R
v q40 = R t.
```

All seven residuals are quadratic in existing or replacement coordinates. Their unique values are

```
a = E^-1
b = E^-3
u = q E^4
v = q^2 E^11
q12 = q E^22
R = q^2 E^44
t = q E^45
q40 = q E^78.
```

Thus the eight-coordinate old subsystem, consisting of six powers and the two outputs, becomes a seven-coordinate subsystem. The existing equations Q=q^3 and R=q12^2 remain in place. There is no circular dependence: q12 is determined first using Q, then its square R determines t and q40.

## Exact forward and backward witness maps

The unchanged equations include a retained inverse for w0,

```
w0 n = (w0^2 - 2 w1^2)/2,
(E delta) B = n^2,
q delta^3 = E.
```

Since w0 is nonzero and 2 is a rational nonsquare, n is nonzero. Hence E and delta are nonzero, and then q is nonzero. The retained Q=q^3 is nonzero. These facts hold in either subsystem and do not use a replaced coordinate.

Given an old rational solution, retain all outside coordinates, including q12, q40, Q and R. Define a,b,u,v,t by the displayed Laurent values. The original chain forces q12=q E^22 and q40=q E^78. The retained R equation gives R=q^2 E^44. Consequently every new equation holds.

Conversely, given a new rational solution, successively divide by the proven nonzero E, b, and Q to obtain a=E^-1, b=E^-3, u=q E^4, v=q^2 E^11, and q12=q E^22. In particular v is nonzero. The retained R equation then gives R=q^2 E^44; dividing by q gives t=q E^45; dividing the final equation by v gives q40=q E^78. Restore the six old power coordinates as E^-1,E^-3,E^-7,E^-14,E^-29,E^-55. Every old defining equation holds with the already retained q12 and q40. All outside equations remain unchanged.

Both maps preserve the input and every outside coordinate. Summing the squares of primitive integer residuals preserves the rational zero set. The expansion has degree exactly four and a coefficient of magnitude one independent of S, proving primitive content one after specializing S=3^(2^26). The unchanged 17-coordinate constant lift would yield 533 total coordinates.

## Verification artifacts

`check_candidate.py` reads the exact 519-coordinate source and verifies its primitive residual normalization against its compiled IR. It verifies every old weight equation, both retained q-power definitions, and the retained q12-square definition coefficient by coefficient. It checks that removed power coordinates have no outside consumers. It then verifies all new equations using exact exponent vectors, checks the coordinate and residual counts, and expands the complete sum of squares.

The generated artifacts are `candidate516.json`, `polynomial516.json`, and `report.json`. `search.py` records the bounded exact search that found the seven-coordinate chain. The original 520-coordinate artifacts in the parent directory are unchanged. No shared repository or mixed-depth source file was edited.
