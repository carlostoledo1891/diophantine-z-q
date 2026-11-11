# Independent acceptance of the squared-anchor358 reduction

I accept this exact359-to358 reduction, conditional on the inherited arithmetic inputs of accepted359. It preserves the rational input projection. I found no unresolved mathematical or implementation gap in the changed component.

The candidate has 358 total rational variables, 357 existential witnesses, and 328 quadratic residuals. Its coefficient-power table has 6,419 entries but specializes to 6,416 actual quartic monomials. The degree is four and integer content is one. Its largest coefficient is **186624*3^(2^26)+64**, not the predecessor's16C^2 bound.

Reviewer: `/root/astra_bl_horizontal_repair`, November 7, 2026. Author: `/root/astra_quartic_opt10_combination`. I did not author this reduction or359. I independently reviewed359 immediately before this audit. This acceptance checks the new parameter and exact source application; it does not re-prove all inherited global arithmetic theorems or authorize a release. No author artifact, source packet, repository file, or controller was changed.

## Exact pins and evidence

Author directory: `work/quartic-under300-20261107/10-combination/squared-anchor358`.

| Artifact | SHA-256 |
|---|---|
| Author `REPORT.md` | `8725fea19467a2576c0adde5044e08ed3e4a8d3c944113d859bbc982b6326644` |
| `candidate358-ir.json` | `3f97e76e28b16174d05fc63122c85715a38090331f8b763d196c86fec7e37d5e` |
| `polynomial358.json` | `7c4fdfe3306e068a08fd6f0c152aba5b6531d164a766a44569f58757635db249` |
| Author `verify.py` | `e32bd1d1ae304e1c036614c67f6f7e3622aff6e09f0c7747266aba402a0dac6e` |
| Accepted359 IR | `282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1` |
| Independent359 review | `6956155cc4878f0c36f5e1159330f043d473cc8fd4ba421f2ec484dc4083655c` |
| This directory's `check.py` | `50721426285c7b2c139406eccc4b5ed2190cc927a28f5d687bfbcf90539815ee` |
| This directory's `CHECKS.json` | `73b42c09e842922637fbb845e756ee117dfe37586b2809b5f47982e1d6669020` |

The source359 and its full proof are in `work/quartic-optimization-20261107/resume-elimination-20261107/abscissa359`; its independent acceptance is in sibling `resume-review359-20261107`. I read the complete new report, builder, verifier, and actual source/candidate equations. The underlying coefficient and reciprocal arguments were read from the pinned `quartic_v12.tex`, SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, during the preceding359 audit. This review uses their exact source scope rather than an informal acceptance of the analogous365 proposal.

My new checker imports no producer or other checker. It passed with `C:/Users/glaze/.local/bin/python3.14.exe -B check.py` and writes only `CHECKS.json` here. It verifies all author files have unchanged hashes afterward.

## The changed scalar coefficient

The unchanged charts and source group decomposition first give nonzero integral root labels. Independently of parity or height, the retained reciprocal equations and g0*tau=1 give

    g=g0+g1*rho, g^2=f([s]P), s!=0,
    f=1/x, rho^2=2.

The equal-abscissa S=-P case is the source's actual duplication value. S=P would give g=0 and contradict the retained guard. None of this requires the new anchor.

For odd s, the source reduction is f([s]P)=2*rho modulo3. The field is unramified quadratic at3, so g is integral with unit field valuation. Its residue is one of the two roots of2*rho, namely plus or minus(1+rho). My checker enumerates the residue field and checks exactly those roots. Both rational coefficients g0,g1 are therefore3-units.

For nonzero even s, set r=1+v3(s). The source coefficient lemma gives v3(f1)=2r and v3(f0)>=2r+1, so the field valuation of f is2r. From g^2=f, the field valuation of g isr. In the unramified basis1,rho this is min(v3(g0),v3(g1)); neither coefficient can have smaller valuation. The exact coefficient identity f1=2g0g1 makes their valuation sum2r. Hence both valuations equalr. In particular neither coefficient is zero. For all allowed s we have

    v3(g1^2)=v3(f1),

with value zero for odd s and2+2v3(s) for even s. This is an orbit-specific statement, not a general identity for arbitrary square roots in K.

At2, every integral multiple of P is in the integral formal subgroup of the given model. Its reciprocal abscissa is integral, using f=z^2+O(z^6). Therefore g^2=f makes g integral. Normalize v(2)=1 and use v(rho)=1/2. The rational components have valuations v2(g0) and v2(g1)+1/2, which cannot tie. Integrality of g forces both to be nonnegative, and the integer-valued v2(g1) is consequently nonnegative. This proves the needed2-integrality of g1 itself. It also gives2-integrality of f1=2g0g1. C=3^(2^25) is a2-unit. No good-reduction assertion at2 is used.

## New parameter, noncancellation, and restoration

The actual root rho coefficients remain XA=2*v83, XT=2*v87, XZ=2*v89. Write

    Qroots=12*(XA^2+XT^2)+108*XZ^2,
    T=g1^2+C*Qroots,
    tnew=T/C=g1^2/C+Qroots.

The new equation is exactly

    U^2+6V^2-2W^2-4C*W-3T^2=0.

Completing the square gives

    U^2+6V^2-2(W+C)^2-3T^2+2C^2=0.

Thus division by C^2 identifies the unchanged universal quaternion criterion with parameter tnew. These are unscaled anchor coordinates; no factor g0 is missing from the new row. The checker verifies the displayed identity literally.

For a new rational solution the criterion gives tnew3-integral. The three summands g1^2/C,12*(XA^2+XT^2),108*XZ^2 have valuations in2Z,1+4Z,3+4Z. The source359 abscissa result gives nonzero X values with nonpositive even valuations; anisotropy of x^2+y^2 modulo3 gives the binary sum's exact valuation. The scalar argument above gives g1!=0. Consequently all three valuations are finite, pairwise distinct, and the least cannot cancel. The entire parameter cannot vanish either. Each summand is3-integral.

The root terms force all three X values to be3-units, hence their root labels are odd. The scalar term gives v3(g1)>=2^24, excluding odd s. Since v3(f1)=2v3(g1), it gives f1/C3-integral and the full old scalar depth v3(s)>=2^24-1 before any height or detector-domain consumer. Its2-integrality was obtained separately. By the now-established root oddness and the accepted359 two-adic abscissa formula v2(X)=-1, Qroots is integral at2 as well as3.

It follows that told=f1/C+Qroots is integral at both places. Restore the old359 values Q=Qroots and B=2g1+C*Qroots*tau. The old guard g0*tau=1 has been retained and supplies g0!=0. Apply the universal criterion to told. If its standard solution is u0,v0,w0, the actual old anchor witnesses are

    Uold=C*u0/g0, Vold=C*v0/g0, Wold=C*(w0-1)/g0.

These formulas include the required C scaling and affine w translation before dividing by g0. They restore the precise old row, not a different normalized quadric. Every other source359 coordinate stays fixed. In particular no root sign choice or half-chart reconstruction is required in this map, because those charts are already absent from359. Only after restoration of a complete359 witness is its accepted soundness applied.

## Forward map and completeness

Any full359 solution has the pre-height parity and scalar conclusions proved in its accepted argument: the three roots are odd, s is even and nonzero, and f1/C is integral at2 and3. The new equality of three-adic valuations gives g1^2/C3-integral, while the separate formal-group argument gives its2-integrality. Qroots is integral at both places. Hence tnew meets exactly the inherited quaternion criterion.

Set T=g1^2+C*Qroots. A standard-form criterion solution u0,v0,w0 gives the unscaled new witnesses

    Unew=C*u0, Vnew=C*v0, Wnew=C*(w0-1).

Delete the former B and replace the former stored Q by T. Every other359 value stays fixed. This yields a complete358 witness with the same input.

The two constructions use existential choices of private anchor witnesses; they do not claim equality of old and new anchor fibers with the private values fixed. The criterion applies to every rational parameter and the real quadratic form is indefinite. There is no new real bound, local condition outside the inherited two places, prime selection, denominator-support condition, H progression, or approximation requirement. The positivity of the squared expression causes no additional constraint on the input.

## Consumers, full polynomial, and coefficient collisions

The exact finite comparison removes only coordinate and row904, changes only rows504 and903, and renames only55,56,57,903. All outside objects are unchanged. The complete old incidence of55,56,57,903,904 is confined to rows504,903,904; their new incidence is confined to504,903. Thus the reconstruction has no hidden consumer. The checker also rechecks the physical root normalizations, retained scalar inverse, and every residual under the three full root sign involutions.

The independently expanded primitive-integer sum of squares agrees coefficient by coefficient with the entire supplied table. All358 coordinates occur, every residual is at most quadratic, and the full degree is four. A C-independent coefficient is literally1, so integer content remains1 after specialization.

Specializing C produces exactly three coefficient collisions:

| Monomial | Actual coefficient |
|---|---|
| v83^4 | 2304*C^2+64 |
| v87^4 | 2304*C^2+64 |
| v89^4 | 186624*C^2+64 |

They are positive and cannot disappear. There are6,419 symbolic coefficient-power entries and6,416 actual coordinate monomials. Every other leading C-squared coefficient has absolute value less than186624, C-linear multipliers have magnitude at most864, and C-independent coefficients have fewer than2048 bits. Since C>2^2049, the gap in leading coefficients dominates all lower terms. This proves the stated exact maximum186624*C^2+64 without expanding C numerically.

No ordinary-coefficient circuit or count is accepted by this review. No composition with another reduction has been checked here. Within the stated source-relative scope, the exact358 component is accepted.
