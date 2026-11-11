# One squared scalar coefficient in the parity anchor

Author: `/root/astra_quartic_opt10_combination`. This new proposal removes one variable from the independently accepted359 anchor component. It has **358 total variables**, **357 witnesses**, **328 quadratic residuals**, and **6,416 actual quartic monomials**. Its symbolic table has6,419 entries when powers of the fixed constant are listed separately. Independent mathematical review is pending.

The degree remains four and integer content remains one. The maximum coefficient changes to **186624*3^(2^26)+64**. The increase is explicit; the former16C² maximum is not retained. No released artifact or predecessor file was edited.

## Exact source and change

The source is `work/quartic-optimization-20261107/resume-elimination-20261107/abscissa359/candidate359-ir.json`, SHA `282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1`. Its non-author acceptance is `resume-review359-20261107/REVIEW.md`, SHA `6956155cc4878f0c36f5e1159330f043d473cc8fd4ba421f2ec484dc4083655c` in the same optimization tree. Those inputs retain their stated arithmetic scope.

The new IR has SHA `3f97e76e28b16174d05fc63122c85715a38090331f8b763d196c86fec7e37d5e`; its polynomial has SHA `7c4fdfe3306e068a08fd6f0c152aba5b6531d164a766a44569f58757635db249`.

Keep C=3^(2^25), g=g0+g1*rho, and the guard g0*tau=1. Let XA,XT,XZ be the actual rho coefficients of the three root abscissae, namely2*v83,2*v87,2*v89. Write

```
Qroots=12*(XA^2+XT^2)+108*XZ^2.
```

Replace the two stored values Q and B by one value T at coordinate903:

```
T=g1^2+C*Qroots.
U^2+6V^2-2W^2-4C*W-3T^2=0.
```

The new U,V,W at55/56/57 are unscaled quaternion witnesses. They have no other consumers. Delete B coordinate904 and its defining row904. Replace rows903 and504, renaming the four private coordinates to reflect their meanings. Every other object is unchanged. In particular the scalar reciprocal equations and its nonzero g0 guard remain.

The T definition is quadratic in quantified variables because C is fixed. Its physical terms are `T-g1^2-48C*v83^2-48C*v87^2-432C*v89^2`. The new quaternion parameter is

```
tnew=T/C=g1^2/C+Qroots.
```

The inherited universal criterion for the displayed quaternion form is exactly that tnew be integral at2 and3. It applies to every rational parameter, including zero. This is a changed application of that same criterion, with its new parameter checked below.

## Scalar facts before the anchor inference

The unchanged square-abscissa charts give nonzero integral labels for A,S,T,Z, without using their oddness. The unchanged scalar subtraction equations and g0*tau=1 give a nonidentity point R=S-P=[s]P with s a nonzero integer and g²=f(R). The equal-abscissa case S=-P is covered by the existing duplication identity. The case S=P would give g=0 and contradict the retained guard. No H or height inference is used here.

At3 the source good-reduction calculation says that for odd s, f([s]P) has residue2*rho. Its two square roots in F9 are plus or minus(1+rho). Consequently g0 and g1 are units in that case. For nonzero even s, the accepted source coefficient calculation gives

```
v3(f([s]P))=v3(f1([s]P))=2+2*v3(s).
```

Since the extension is unramified at3, the first equality and g²=f imply `min(v3(g0),v3(g1))=1+v3(s)`. The identity f1=2g0g1 gives the sum of those two valuations as2+2v3(s), so both equal1+v3(s). In particular g1 is nonzero. These are precisely the scalar coefficient facts already used in the independently accepted positive365 component; no new group classification is assumed.

We also need2-integrality of g1, rather than only that of f1. Here is the direct argument. At the prime over2, P has formal parameter z(P)=(232+86*rho)/357 of field valuation3/2, normalized by v(2)=1. Thus P belongs to the formal subgroup of the integral model. Integral multiplication, including negative integers, preserves that subgroup. Every nonzero[s]P is formal, so its reciprocal abscissa f([s]P) is integral by the integral expansion f=z²+O(z^6). From g²=f, g is integral. The two summands g0 and rho*g1 have respectively integral and half-integral valuations and cannot cancel. Hence v2(g0)>=0 and v2(g1)+1/2>=0. Since v2(g1) is an integer, v2(g1)>=0. Thus g1²/C and f1/C are2-integral, since C is a2-unit. This uses the formal subgroup, not good reduction at2.

## Recovering the old parameter and root parities

Suppose the new system has a rational solution. The quaternion criterion makes tnew integral at3. The three summands

```
g1^2/C, 12*(XA^2+XT^2), 108*XZ^2
```

have valuations in2Z,1+4Z,3+4Z respectively. For the first, v3(C)=2^25 is even. For the root terms, the accepted359 calculation gives each Xn valuation zero for odd labels and negative even valuation -2-2v3(n) for even labels. The binary sum has valuation twice the minimum of its two arguments' valuations because -1 is nonsquare modulo3. Thus the three classes are disjoint, and their minimum cannot cancel. Each term is3-integral.

In particular v3(g1)>=2^24. The odd-s case, where g1 is a unit, is excluded. For even s, the equal coefficient valuations proved above give v3(f1)=2v3(g1)>=2^25. Therefore f1/C is3-integral. Its2-integrality was proved independently above.

The two root terms being integral force XA,XT,XZ all to have valuation zero at3. A negative even valuation would make either1+2v3(X) or3+2v3(X) negative. The three root labels are therefore odd. The accepted3592-adic calculation then gives v2(XA)=v2(XT)=v2(XZ)=-1. Since12 and108 have valuation2, Qroots is2-integral; it is also3-integral.

It follows that the old359 parameter

```
told=f1/C+Qroots
```

is integral at2 and3. Set the old Q=Qroots and B=2g1+C*Qroots*tau. Apply the unchanged quaternion criterion to told and choose old359 private anchor witnesses, dividing the unscaled witnesses by nonzero g0 as its source equations require. These assignments restore all359 rows. All nonprivate variables, including the input, roots, H, detector, scalar and pole data, stay fixed. No half-chart sign change is needed for this map to359, whose odd charts are already removed. Only after this explicit restoration is accepted359 soundness used.

## Forward construction

For any full359 solution, its accepted pre-height parity argument supplies the odd root labels, even nonzero s, and f1/C integral at2 and3. The scalar equal-valuation statement gives g1²/C integral at3, and the formal2-adic argument gives integrality at2. Qroots is integral at both places by the odd-root coefficient calculations. Therefore tnew is integral at both places.

Set T=g1²+C*Qroots and choose the new unscaled quaternion witnesses for tnew. Forget B and the former stored Q. Every other359 coordinate remains unchanged. The forward and reverse constructions prove equality of rational input projections, conditional on independent approval of this changed application. They are existential witness maps, not a claim that the old and new private anchor coordinates agree.

No new real condition on a point, prime choice, progression, denominator support or logarithm is introduced. The universal indefinite quaternion criterion supplies the private witnesses after the old construction. Consequently the stronger H progression used in a separate detector composition would not be disturbed, but such a composition still needs its own exact check.

## Finite verification and coefficient specialization

`verify.py` imports no producer. It verifies the exact two-row change, removed-coordinate and private-variable consumers, every outside object, the physical root normalizations, the retained scalar inverse, all three root sign actions, and the full primitive SOS. It checks the valuation residue separation as a finite supplement to the universal argument above.

There are three coefficient collisions upon specializing C: the coefficients on v83^4 and v87^4 are2304C²+64, and that on v89^4 is186624C²+64. All other C-squared coefficients have smaller magnitude. C-linear coefficients have magnitude at most864, while constant coefficients have fewer than2048 bits. Since C is much larger than2^2048, the exact maximum is186624C²+64. A literal coefficient1 remains, giving integer content one. The actual monomial count is6416, not the6419 rows of the coefficient-power table.

An ordinary-coefficient circuit would need a stored Qroots to keep C*Qroots quadratic after making C a variable. The old C*tau gate would no longer be used by the anchor. No ordinary artifact or count is claimed here without that separate construction and check.

Independent review must specifically check the new g1² parameter, the formal2-adic integrality step, both existential maps, and coefficient specialization. The source359 acceptance is not an automatic acceptance of this proposal.
