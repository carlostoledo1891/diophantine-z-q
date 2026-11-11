# Fixed-root V0 and shared-log search

No variable saving is established. This packet records a bounded search on the actual fixed-root V0 interface and a specific obstruction to deleting its common-log correction by sharing another alternate logarithm. The accepted320 system and the earlier general-root obstruction are unchanged.

Author: `/root/astra_quartic_opt05_anchor`, November7,2026. The numerical rank probe is finite-field reconnaissance, not an independent mathematical acceptance or a characteristic-zero impossibility proof.

## Exact source and interface

The source is `work/quartic-under300-20261107/10-combination/combined320/candidate320-ir.json`, SHA256 `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f`. Parent identified this composition as accepted. Its source report is SHA256 `ee4c2b537d9520977243a7531b20fad2890613f1c21a13f718ed75a995835aee`. The present work neither changes nor re-reviews that acceptance.

The fixed translation point uses

    a=-1+7rho/4, b=39/8-9rho/2, c=a², D=11-6rho,
    rho²=2, b²=c²-D.

The actual V0/H values available without another field pair are

    v=v700+rho*v701, t=v142+rho*v143,
    W=v140+rho*v141=v²,
    U=v311+2rho*v312=f(H)²,
    V=v178+2rho*v179=f(V0)².

Writing Q=(1-DW-2bv)/c, the retained equations are

    UV=W², Q²=U+V+2W, t(U+W)=Qv.

The high logarithm caches are w² and w⁴, with w=D*V. The first cache has the existing scaled physical coordinates180/181; the second is182/183. The approximation is186/187 and the common logarithm is188/189. Thus V0 contributes ten rational coordinates including V and its common-log output. The w⁴ output also occurs in all three detector G0 sums, so it cannot be forgotten merely by changing the logarithm evaluator. U is consumed by the strong H detector slot and the scalar norm row. The actual t,v values occur in all four primary-ratio equations and the scalar ratio equation. Removing one of these values requires transporting those consumers.

## Fixed-root probe

Unlike the preceding general-root search, the current calculation uses the literal fixed a,b,c,D. At V0=O choose a local reciprocal square-root parameter g and put

    k=sqrt(1-Dg⁴),
    r=(a*k-b*g)/(c+Dg²),
    v=r*g, t=g/r, W=v², U=r⁴, V=g⁴.

These are the actual squared-H functions on the branch with H=P at g=0. The correct local logarithm is

    ell(g)=sum[n>=0] binom(2n,n)*D^n*g^(4n+1)/(4^n*(4n+1)).

The branch denominator c is nonzero. This is only a local search parameterization, not a proposed global replacement that ignores the other squared-H branches.

`probe.py` forms all45 quadratic monomials in

    v,t,W,U,V,w²,w⁴,L

and evaluates their jets at L=ell(g), using the exact finite field with p=1000000007 and rho=940286407. The constants and their denominators are valid in that field. The ranks through g-degrees16,24,32,36,40 are17,25,33,37,37. Log-dependent null vectors exist at the lower precisions, but none remains through degree36 or40. `PROBE.json` preserves every result and the lower-order candidate vectors.

This gives no positive candidate to lift. It also does not justify a characteristic-zero lower bound by itself: a rank comparison or a complete exact kernel certificate would still be required for such a claim. I did not turn the finite-field result into a purported replacement equation or a new acceptance.

## Cache deletion and denominator changes

Deleting the w² pair while keeping w⁴ is not the same case as the earlier obstruction that kept w². In the pure-w submodel, a quadratic implicit equation in R,w,w⁴ has span

    1,w,w²,w⁴,w⁵,w⁸,R,wR,w⁴R,R².

The exact10-by10 coefficient matrix obtained by substituting the retained G series through w⁹ has rank10. Thus this submodel supplies no replacement. This calculation was a small direct rational row reduction; it is subordinate evidence, not a claim covering the extra H parameters in the fixed-root probe.

Simple changes of denominator do not otherwise remove an intermediate. For example, replacing G by `(1-w)*J` turns zG into a product involving the reciprocal square root and its slope. The source does not store those unscaled factors as independent affine values. Introducing them spends the prospective field-pair saving. Picking a positive square root is not a valid rational witness map and would lose the other sign branch.

The common-log equation can also be written `T*ell0=N0*R0`, with T affine in the H parameters and N0 a fixed multiple of t. Eliminating R0 gives a cubic relation when its rational approximation equation is cleared. Rescaling w² by N0 instead moves that cubic product into the cache equation. No cancellation reducing all these equations to quadratic was found. These observations are failed constructions, not proofs against different auxiliary functions.

## Why sharing another alternate denominator loses a needed condition

An attractive count would remove the V0 approximation and use the already computed high logarithm of V2 as the common denominator. The missing normalization cannot be inferred from the remaining cross comparisons.

To see the issue before approximation errors, let the root labels be n_i, with n_2=a_index. Let the primary indices be u_i=kappa*n_i and let H have index h, with h not required to equal kappa. The exact linear-log model gives

    primary_i=u_i/h=kappa*n_i/h,
    alternate_i=(u_i-n_i)*log(P)=(kappa-1)*n_i*log(P).

If one defines the new common value by `alternate_2/primary_2`, then it equals `(kappa-1)*h*log(P)/kappa`. Every resulting alternate quotient is therefore exactly `kappa*n_i/h`, the same as the primary quotient. All such cross comparisons vanish for any nonzero common scale kappa/h, although the intended values are n_i.

For example h=3,kappa=2,a_index=5,n_i=7 gives both compared values14/3 rather than7. This example is a counterexample to the proposed linear-log inference, not an assertion that a complete nonintegral quartic witness has been constructed. The original V0 denominator fixes this scale through its actual index h-1. Deleting it requires a new normalization argument before the existing Lucas and input-height proofs can be used.

Using V1 as denominator also requires upgrading its approximation to order40, adds its missing higher cache/evaluator coordinates, and must establish its nonzero domain before division. Merely changing which logarithm is called the common denominator supplies no net saving or missing normalization proof.

## Result and remaining scope

The established saving is zero; there is no new quartic, approximant, or witness map in this packet. All accepted coefficient sources, point domains, zero branches, order40 logarithm bounds and detector functions remain intact.

A useful future route would need an auxiliary function that simultaneously participates in the V0 cache and logarithm equations, or a coupled comparison system with a proved replacement for the lost index normalization. Neither is provided here. The local rank probe does not exclude such changes. Its script runs in under one second and does not execute candidate code or expand the anchor constant.
