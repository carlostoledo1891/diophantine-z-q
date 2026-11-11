# A single-coefficient anchor gives 522 variables

The 523-variable system admits a 522-variable replacement. The change removes
the coordinate named `anchor.physicalA.quadratic` and its defining residual.
It replaces the anchor equation by one quadratic equation in the same three
private witnesses and the existing coordinate `Sscalar.f.1`.

The argument below proves equivalence of projections onto all coordinates
outside the anchor, using the arithmetic inputs already stated in Version 11.
It does not provide a fresh verification of the manuscript's inherited global
arithmetic results. This proposal has not received independent review and has
not been incorporated into the repository.

## Exact candidate

Let rho^2=2, C=3^(2^25), and S0=C^2=3^(2^26). Preserve every residual and
coordinate of the pinned 523-variable candidate except the following changes.

1. Delete coordinate 539, `anchor.physicalA.quadratic`.
2. Delete residual 507, `anchor.physicalA.definition`.
3. Replace residual 508 by

   u^2 + 6v^2 - 2w^2 - 3f1^2 + 2S0 = 0.

Here u,v,w are the three existing private coordinates 55,56,57, and f1 is the
existing coordinate 509. It is exactly the rho-coefficient of f(R)=1/x(R),
where R=S-P=[a-1]P. No coefficient rescaling is hidden in this identification.
Each remaining rational residual is multiplied by its positive rational
normalization factor to become primitive with integer coefficients. Define
P522 to be the sum of the squares of these 491 normalized residuals.

This is an explicit integer polynomial in 522 variables, including input 0.
`candidate522-ir.json` contains the complete defining residual system and
`polynomial522-symbolic.json` contains its complete collected symbolic
expansion. The latter has 35,138 coordinate monomials and 35,140 terms when
different powers of S0 at one monomial are listed separately. Its degree is
four and its content is one. A coefficient equal to one remains present.
Its largest coefficient magnitude is

    4 S0^2 + 1005072314631333.

All S0-dependent coefficients have degree at most two in S0; only the constant
coefficient has degree two. The fixed coefficients have at most 1,520 bits,
so the displayed leading coefficient dominates without expanding S0.

## The local observation

Use the exact curve and point from the manuscript's
`subsec:o8-anchor-subgroup`, with valuation v3(3)=1 at the unramified
quadratic prime above 3:

    E: y^2 = x^3 - (11-6rho)x,
    P = (57/8 - (7/2)rho, -165/8 + (417/32)rho),
    z = -x/y, f = 1/x.

The manuscript gives, and exact rational arithmetic in the checker confirms,

    z(2P) = (3396356159088 - 4135204317756rho)/3287811625151.

After division by 3 and reduction modulo 3 this is 2+rho. Its square in
F9=F3[rho]/(rho^2-2) is rho.

Write a nonzero even integer n as n=2*3^k*u, where k>=0 and u is an integer
not divisible by 3, possibly negative. For the integral odd formal group
used in the manuscript,

    [u]z = uz + O(z^3),
    [3]z = 3z + O(z^3).

The coefficients in both remainders are integral. If v3(z)=r>=1, division
of the first identity by 3^r shows that multiplication by u multiplies the
leading residue by its nonzero F3 residue. Division of the second identity
by 3^(r+1) shows that multiplication by 3 preserves the leading residue:
the remainder has valuation at least 3r-(r+1)=2r-1>=1. Induction therefore
gives

    z(nP)/3^(k+1) = u(2+rho) modulo 3.

The exact curve identity is

    f = z^2(1-(11-6rho)f^2).

On the formal branch the second factor is 1 modulo 3. Since u^2=1 in F3,

    f(nP)/3^(2k+2) = rho modulo 3.

Write f(nP)=f0+f1*rho. The basis 1,rho remains a basis of the residue field
over F3. Thus the stronger, coefficient-specific version of the existing
depth formula is

    v3(f1) = 2+2v3(n),
    v3(f0) >= 3+2v3(n),

where the second statement permits f0=0. In particular, f1 cannot vanish.
This proof covers every nonzero even n, not merely the finite examples run
by the checker.

## Equivalence of anchors and input projections

The four odd-coset charts in Version 9, retained in Version 11, force the root
index a to be odd. The retained subtraction guard excludes a=1. Consequently
R=[a-1]P has a nonzero even index. The local observation applies to every
solution of the unchanged equations outside the anchor.

At the prime above 2, the original anchor-subgroup proof already establishes
that both rational coefficients f0 and f1 are 2-integral for every integral
multiple of P. Since C is a 2-unit, both f0/C and f1/C are 2-integral.
At 3, the coefficient-specific valuation formula implies

    f1/C in Z_(3) iff both f0/C and f1/C are in Z_(3).

Hence the old two-coefficient condition is equivalent to just

    f1/C in Z_(2) intersect Z_(3).

The three-witness lemma `lem:v5-three-witness-anchor` proves for each rational
t, including t=0,

    t in Z_(2) intersect Z_(3)
    iff there exist U,V,W in Q with U^2+6V^2-2W^2-3t^2+2=0.

Apply it with t=f1/C and multiply by C^2. Renaming CU,CV,CW as u,v,w gives
exactly the new quadratic anchor. This uses the identical quaternion
criterion from the source lemma. Its argument does not require that t be
the anisotropic quadratic expression used in the older anchor.

For an old solution, retain all coordinates outside 55,56,57,539. Its old
anchor implies the semilocal condition, so the three-witness lemma supplies
u,v,w solving the replacement. Conversely, a solution of the replacement
has the same semilocal condition on both coefficients. Apply the old anchor
lemma to obtain its private witnesses and set coordinate 539 to
f0^2+f0*f1-f1^2. Finally apply the old invertible affine witness translation
recorded in the baseline IR. This extends the solution to every old residual.
No other equation contains the three private coordinates or coordinate 539.

These two constructions prove equality of the projections, without asserting
an unnecessary one-to-one correspondence between anchor witnesses. In
particular the input projection remains Z, on precisely the same inherited
arithmetic assumptions as P523.

The exact allowed index subgroup remains

    a-1 in 2*3^(2^24-1) Z, a-1 != 0.

Thus all height margins, scalar conditions, prime choices, arbitrary further
divisibility and completeness choices remain unchanged.

## A smaller fixed coefficient and 538-variable ordinary version

Substitute w_old=w_new+C in the new equation. The constant cancels, giving

    u^2 + 6v^2 - 2w_new^2 - 4C*w_new - 3f1^2 = 0,
    C=3^(2^25).

`candidate522-smallcoeff-ir.json` gives this affinely equivalent 522-variable
version. The largest coefficient now has magnitude 16*C^2, at w_new^2
in the expanded anchor square. All other coefficient terms are at most
linear in C or have the previously bounded fixed size. This affine change
does not use a new number-theoretic input.

To eliminate the fixed huge coefficient while retaining the original
3,247-bit coefficient bound, introduce just sixteen coordinates:

    c0 = 3^1024,
    c(j+1) = cj^2 for 0<=j<15,
    C = c15.

Replace the term -4C*w_new by -4c15*w_new. Each residual stays quadratic and
the chain has exactly one rational lift. `candidate538-ir.json` contains the
resulting system of 507 residuals in 538 variables, including the input.
The integer sum of squares is explicit without any expansion of C.
The constant coefficient is 3^2048+1005072314631333, as in the earlier
540-variable construction; this dominates every other coefficient.

## Reproduction and source bindings

Run `build_check.py` using Python 3.10 or newer. It reads the pinned baseline,
constructs the systems above, checks private-coordinate incidence, verifies
counts and degrees, expands the 522-variable sum of squares with S0 symbolic,
checks coefficient content, compares three finite-field evaluations of the
expanded polynomial with direct residual evaluation, and checks the local
starting point and even indices 2,4,6,10,12,18 by exact rational arithmetic.
It uses only the standard library and never evaluates 3^(2^25) or 3^(2^26).

The baseline is
`quartics/quartic-523-540/final523_540/symbolic523/candidate-ir.json`, SHA-256
`48a8b8f9263a97d3a1c59f3f0f3553eae628b7aba342d44003e8da840ae84928`.

The reviewed manuscript is `manuscripts/quartic_v11.tex`, SHA-256
`1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`.
Relevant passages are the exact local anchor calculation at lines 8132-8220,
the three-witness criterion at lines 10972-11024, and the Version 9 bridge at
lines 19268-19323. The odd-coset construction and shifted scalar point are
also stated in `docs/quartic-523-540/addition.tex`.

The source requirements match this application: the field, coefficient
basis, point, and valuation normalization are unchanged; R is a nonzero
even multiple of P; the quaternion lemma accepts every rational t; and its
output is exactly the semilocal condition needed by the original anchor.
The construction covers negative as well as positive indices. It does not
change any global theorem application or any local condition outside 2,3.

A search of the current manuscript and available anchor notes found the
older simultaneous two-coefficient predicates and the required formal-group
inputs. No earlier occurrence of this coefficient-specific argument was
identified. Its broader historical priority is unresolved. The manuscript
has not been edited, and its prior acceptance records do not independently
approve this proposal. The repository's source review and independent
acceptance requirements still apply before integration or release.

No additional reduction of the three quaternion witnesses is claimed. A
binary norm equation would generally introduce conditions at further primes,
so replacing this ternary representation without a new proof would be invalid.
Reducing the repeated-squaring exponent 32 to 16 would also lose the existing
scalar bound with exponent 19/32<1. Neither shortcut is used here.
