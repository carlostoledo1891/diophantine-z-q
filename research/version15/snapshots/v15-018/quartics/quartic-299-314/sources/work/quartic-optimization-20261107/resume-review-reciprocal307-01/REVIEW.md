# Independent review of reciprocal307

I independently accept the frozen reciprocal307 candidate as preserving the rational input projection of accepted313, subject to exactly its inherited arithmetic assumptions. The complete new algebraic interface and finite construction pass the checks below. No defect or missing hypothesis remains in this reviewed delta.

Reviewer: `/root/astra_quartic_opt01_elimination`. I did not contribute the reciprocal closure, its zero-safe ratio equations, or the new auxiliary-domain argument. I authored some earlier accepted ancestors, including the shared314 circuit; their existing independent reviews are inputs, not replaced here. The root agent, horizontal-repair agent and agent10 contributed the new closure. Agent05 authored the auxiliary-domain extension, independently reviewed by agent10 within its stated scope.

## Exact objects and result checked

Source313 IR: `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`.

Candidate307 IR: `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`.

Polynomial307: `90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106`.

Root closure proof: `9413e67fc1f54980932758304f561aaac418b037dd3406fcb0b87bbac929da0e`.

Auxiliary-domain proposal: `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`; independent conditional review: `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b`.

The checked result is 307 total rational coordinates, including the input, hence 306 witnesses; 295 residuals of degree at most two; and 6438 distinct monomials in their primitive integral sum of squares, of degree four and content one. The exact largest absolute coefficient is `186624*C^2`, where `C=3^(2^25)`. There is no additional `+64` in this candidate. These are the unweighted residual squares, not a transport of the separate weighted313 table. No ordinary-coefficient companion is covered.

## Literal equations and every affected consumer

The field is `K=Q(rho)`, `rho^2=2`, with `D=11-6rho`. My checker independently constructs each physical field equation and compares every rational coefficient with the actual IR. It imports no author implementation.

For A/T/Z respectively, the retained root square coordinates start at 1/9/13; root abscissae are `(82,2*83)`, `(2*86,2*87)`, `(88,2*89)`. The new pairs `(f,h,F,s,k)` start at `(21,23,110,112,114)`, `(29,31,126,128,130)`, `(33,35,134,136,138)`. Stored primary squares are `(255,2*256)`, `(259,2*260)`, `(261,2*262)`; alternate squares are `(190,2*191)`, `(208,2*209)`, `(220,2*221)`. The unchanged primary ratios start at 232/240/244 and alternate parameters at 164/172/176. Other pairs in this sentence have unscaled imaginary components.

Exactly 54 old rows change and 12 rows, IDs2200--2211, are added. The other 229 rows remain byte-equivalent as decoded objects. Six rational coordinates, IDs3,4,11,12,15,16, are removed. Every old use of each removed or repurposed coordinate lies in the verified changed rows. The other coordinate records are unchanged; repurposed records change only their names. No stale use of an old auxiliary square-root value remains. All three retained root-a sign actions still preserve every residual. The S-root, its orientation and the scalar subsystem remain unchanged.

In particular, the physical meanings of the retained squared leaves are now exactly `Y=f^2` and `Yalt=F^2`. Thus the unchanged downstream squaring, conjugation, normalization and shared-scale circuits receive the same values attached to actual points. No claim is made that arbitrary raw f has a square root in K.

## Oriented group law, including exceptional cases

The convention is negative reciprocal ordinate: `f=1/x(U)`, `h=-y(U)/x(U)^2`, with `(f,h)=(0,0)` representing O. The cubic `h^2=f-D*f^3` excludes T0=(0,0) but admits the other finite two-torsion points. Translation by T0 sends U to `(-D*f,-D*h)` and similarly V to `(-D*F,-D*k)`.

The checked closure is

```
s*(f-F)=h+k
s*(h-k)=1-D*(f^2+f*F+F^2)
s^2=c-D*(f+F)
yR=D*h-s*(D*f+c).
```

For `f!=F`, the first equation is the chord slope from U+T0 to -(V+T0); the last two identify the abscissa and ordinate of U-V. For `f=F`, it gives `k=-h`. If h were zero, the curve would imply `f=0` or `D*f^2=1`, whereas the second equation would require `3*D*f^2=1`. Hence h is nonzero, and `s=(1-3*D*f^2)/(2*h)` is exactly the tangent slope at U+T0. This again gives U-V, not just its abscissa.

If U=O, the equations give `-s*F=k`, `-s*k=1-D*F^2` and `F*c=1`; then `yR=k/F^2=-y(V)`. Thus the output is -V. Interchanging U and V gives the V=O case with output U. Both cannot be O. The chord argument also covers unequal finite two-torsion inputs; the impossible equal-abscissa zero-ordinate branch is excluded algebraically, not by a later valuation claim.

My separate `check_algebra.py` expands the universal root-curve identity, its orientation under swapping inputs, and the exact equal-abscissa contradiction. It uses a different sparse-polynomial representation from the root's identity checker. Thus `(c,yR)` is an actual E-point with the required orientation, even before invoking any arithmetic-domain argument.

## Restoring the old roots before using height or logarithms

The retained rows impose `a^2=c`. The literal height products are `P=cA*cS`, `2*Q=P*cT`, and `Rprod=Q*cZ`, with stored pairs `(337,2*338)`, `(339,2*340)`, `(341,2*342)`. If any c vanishes, both coordinates341 and342 vanish. Explicitly checked triangular rows then force343,344,345,391,392,393,394 to vanish, and row352 becomes -1=0. This establishes c nonzero globally, without a successful contact prime or a logarithm. Therefore a is nonzero.

Set `b=yR/a`. The universal curve identity gives `b^2=c^2-D`. Hence every A/T/Z root regains exactly its old square chart and its old actual point `(c,a*b)`. All other old uses of b were in the replaced charts. This suffices to restore the old integer root labels, squareclass conditions, oddness and height input. It does not purport to restore the auxiliary point square roots.

## Zero-safe ratios and the auxiliary-domain interface

The shared affine expression in coordinates142,143,700,701 is bound to the old physical ratio equation and is `S=-1/z(H)`. Both kinds of new equations are actually present:

```
h*L+f*S=0              (1-D*Y)*L+h*S=0
k*z-F=0                (1-D*Yalt)*z-k=0.
```

At O the regular equations force the correct L=0 or z=0. Away from O and finite two-torsion the curve gives `z=f/h=h/(1-D*Y)`, and the primary equation gives `L=z(U)/z(H)`. No division at finite two-torsion is used in this argument. The separately accepted low tests first exclude that case: its f is a unit at every consumed place. The extra raw equations are retained, so the candidate is a subset of the zero-safe interface accepted in the domain review.

For the literal old biquadratic coordinates V_old,I_old,Q_old,K_old, divide by the retained nonzero a to obtain r=V_old/a, J=I_old/a and the analogous alternate pair. Thus f=V_old^2/c, h=-I_old*V_old/c, F=Q_old^2/c and k=-K_old*Q_old/c. In particular `f=r^2`, `h=-J*r`, where `J^2+D*r^4=1`. The checked old physical ratio is I_old*L-V_old*S=0; division by a gives the normalized ratio used here. My checker verifies the two regular equations as exact linear combinations of the old ratio and conic equations, and the two raw equations as multiples of the old ratio equations. This includes r=0 with either J sign. Every old point pair has a rational chord or tangent s as above, since its difference is the nonzero retained root. Thus every old witness supplies a new witness with unchanged input and unchanged downstream values. No new real or finite approximation choice is needed.

For soundness I apply the pinned conditional domain review only after establishing its missing group-law and root-restoration inputs. Its valuation periods are valid for arbitrary E(K) points: the raw cubic gives even v(f) whether v(f) is positive or negative, and v(f)=0 is harmless; zero leaves are omitted. Consequently the unchanged squared, fourth- and eighth-power leaves have the required periods before formality. The source root-height/anchor contradiction and H/V0 exclusions remain before logarithms. Positive low tests then give formal points and make `1-D*Y` a local unit.

The enlarged auxiliary labels use `U_i=k_i*R0+T_i`, not an unjustified integer multiple of P. The valid identities are `[2m]U_i=[2k_i]H` and `[2(m-2)]V_i=[2(k_i-2n_i)]V0`; both kill the two-torsion. Their full ratios have indices k_i/2 and m/2, which are integral at consumed odd primes. The accepted integrality transfer and H bootstrap therefore deliver the same congruences to the restored integer root labels n_i. S and its scalar transfer have not been changed. The global rational-approximant nonvanishing certificates, rather than the old optional real-positivity interval, cover the enlarged auxiliary cosets. These are exactly the conditions checked by agent10's independent arithmetic review, and the actual307 equations satisfy them.

The resulting equivalence is equality of the rational input projection with the accepted313 system. It is not a bijection between all private witness fibers. No new arithmetic assumption is introduced.

## Polynomial verification and limits

`check_finite.py` clears rational denominators and primitive content separately in each actual residual, expands all ordered products, and compares every coefficient with the supplied polynomial. It verifies all307 coordinates occur, degree four, content one, and all6438 monomials. The specialization and largest-coefficient comparison use exact coefficient-polynomial dominance with coefficient bounds below 2048 bits and the stated much larger positive C; no huge decimal expansion is needed. The maximum is attained at the fourth power of coordinate89, with no lower C-power contribution there.

The author files are read-only inputs to these checks. `FINITE-CHECKS.json` and `ALGEBRA-CHECKS.json` record the independent runs. I read the final author report in full, SHA256 e665b24b174be4ddc4933293c6843a2a897c41b5982728e63a197e47b4f38d20. Its frozen manifest is 2f3a7c702bc4b01fa9f0cb8b5777b3de69c6fa4fbaa8d4ac8364ceceb49333a2. All manifest files and proof inputs are pinned in PACKET-CHECKS.json and were checked before and after replay. No author code was executed and no author file was changed. Run check_packet.py to reproduce both independent checkers and all these source bindings. This review does not authorize publication or claim the below300 milestone.
