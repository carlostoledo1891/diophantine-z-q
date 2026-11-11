# Independent review of H.j elimination and V0 rescaling

Reviewer: `/root/astra_bl5_models`. Decision: accepted for the frozen 439-to-437 research change. No manuscript or release approval is given.

## Exact artifacts and dependencies

- Source `combined439-ir.json`: `403c4126d532fd3403ce0d87a258790d6b78c1a46cf09716aab0df3a7e84c4df`.
- Candidate `primary437-ir.json`: `e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e`.
- Polynomial: `1a77fe61c5d77f5d83a049aaf6b8779c0b6a5bb4a2a2288c91d26123e813067d`.
- Certificate: `9d086269f8e05c0eee3d3ac2f2ff77adaabfb0c91365e7e8b3cb7a021a26650a`.
- Author report: `ae099bce5316ebb55a546d31b9be0020775fb9f98892631f4b3ac754f99223d6`.
- Reviewed verifier: `25fc481d043480f541cb492786f345f586edc5ca2351c5f1a2fd831a687d4f2f`.

The source439 composition has a separate parent review, `../00-root/REVIEW439.md`, hash `73ee0fb4eb11185c8244e75c0c580f2c8d27a530f54b353d836fe845f56dd031`. I read it and verified its hash. Its prior source443 acceptance and odd-chart acceptance remain separate dependencies. I proposed the earlier scalar-fusion identity; this report does not purport to supply an independent review of my own earlier contribution. The new H.j/V0 rescaling reviewed here was authored by the combination agent.

I read the current author report, builder, certificate and producer-free verifier. I reran the verifier with all writes intercepted and independently added complete outside-object comparisons, duplicate-term/ID checks, parameter/input preservation, and the specialized coefficient-one check. `replay437.py`, `437-replay.log`, and `437-replay-result.json` record this work. No source or repository artifact was modified.

## Whole-domain witness maps

All equations are over K=Q(sqrt(2)), represented by their two rational components. Write the retained H values as h,x,f,s, where the actual retained equations are `x=h^2`, `xf=1`, and the source also has `hs=j`. Thus x and h are nonzero in every old or new solution. In particular, the forward division by h is justified before using any elliptic interpretation.

Keep all other retained values, delete j, and replace the old reciprocal V0 coordinate g by `v=g/h`. Conversely reconstruct `j=hs` and `g=hv`. Division by h has rational component formulas with denominator `h0^2-2*h1^2`, which is nonzero for a nonzero element of K. Neither individual component h0 nor h1 is assumed nonzero. The two maps are mutually inverse on their entire solution domains and fix the input.

The new H equation is `s^2-x+D*f=0`, and the new V0 square equation is `fV*f-v^2=0` (equivalently its negative). They are precisely the old equations divided by the nonzero x. To check this without informal cancellation, put `EX=h^2-x`, `EF=xf-1`. Substituting j=hs gives

`j^2-x^2+D = x*(s^2-x+D*f)+EX*s^2-D*EF`.

Substituting g=hv gives

`fV-g^2 = x*(fV*f-v^2)-fV*EF-EX*v^2`.

The replay verifies both as exact field-polynomial identities, including both rational components and the source's affine coordinate normalizations. These identities prove the reverse direction; the same identities and x nonzero prove the forward direction.

## Reciprocal and logarithm consumers

For the fixed constants a,b,D, set `d=a^2*x+D`, `N=a*j-b*h`, and `T=-2D*h-a*b*j+2D*b*g`. After substitution,

`N=h*(a*s-b)`,

`T=h*(-2D-a*b*s+2D*b*v)=h*Tprime`.

Consequently the old reciprocal equation `d*g-N=0` is h times the new equation `d*v-(a*s-b)=0`. The old physical logarithm equation

`T*ell0+a*N*R0=0`

is h times the new equation

`Tprime*ell0+a*(a*s-b)*R0=0`.

The R0 here is the actual retained rational-approximation output, not an old G9 value or a stale semantic placeholder. Both components are explicitly matched to the physical rows in source and candidate. The new equations remain quadratic because d and Tprime are affine in available coordinates and a,b,D are constants.

No division by s, v, Tprime, ell0, R0 or fV occurs in these maps. Their possible zero values are therefore not silently excluded. The old source's nonzero or point-identification conclusions, where needed, transfer after reconstruction; they are not extra premises for this finite equivalence. In particular the old j and g values, actual H and V0 points, logarithm value ell0, primary ratios and scalar data are recovered exactly.

## Complete incidence and metadata

The full source incidence of the two removed j coordinates19/20 and two reinterpreted g coordinates700/701 is exactly these ten component rows:

- `H.chart.equation.0/1`;
- `U0.z.definition.0/1` (the hs-j equations);
- `V0.f.definition.0/1`;
- `V0.reciprocal.g.definition.0/1`;
- `logV0.definition.0/1`.

The two hs-j rows are deleted and the other eight are replaced. Every outside row object, not just its polynomial, is unchanged. The two g slots are renamed `V0.reciprocal.gOverH.0/1`; all other retained coordinate objects match the source. The earlier scalar fusion is material here: it removed the former scalar consumers of H.j. The present incidence check verifies that fact in the actual source439 rather than assuming it from a previous report.

The verifier also matches the physical retained H.x and U0.f equations that establish x=h^2 and xf=1. No required relation was taken from semantic metadata alone. All relevant equality comparisons allow only the checked nonzero rational row normalization, with the factor two in field multiplication handled explicitly.

## Quartic and conclusion

The complete primitive-integer row normalization and sum-of-squares expansion agree with the frozen polynomial. It has437 total variables,436 witnesses,414 quadratic residuals,degree4 and6503 monomials. All coordinate IDs are used; row IDs and term keys are distinct. C remains the fixed integer `3^(2^25)`, not a variable, and the input coordinate is unchanged.

After specializing C, the coefficient of x_1^4 is exactly1 and has no other C contribution. The only quadratic-C term is `16*C^2*x_57^2`, with no lower-C term on that monomial. Ordinary coefficients have bit length below2048, and coefficients linear in C have multiplier at most48. These checks prove specialized content1 and maximum absolute coefficient `16*3^(2^26)`.

Thus the new system has exactly the same rational input projection as source439, with no additional arithmetic hypothesis or exceptional branch. No defect was found in the frozen 437 change. Acceptance does not extend to subsequent modifications or replace any inherited source review.
