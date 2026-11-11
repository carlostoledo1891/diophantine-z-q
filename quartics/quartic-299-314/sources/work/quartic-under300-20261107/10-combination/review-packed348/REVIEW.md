# Review of the repaired detector and mixed packing

I accept the corrected 366-to-354 detector argument and the 354-to-348 extension on their stated, inherited arithmetic inputs. In particular I independently accept the pre-H valuation repair supplied by the earlier reviewer. No candidate or author report was changed. This is a research-candidate acceptance, not a new review of all historical arithmetic inputs or authorization to publish.

Reviewer: `/root/astra_quartic_opt10_combination`. The detector author is `/root/astra_quartic_opt06_product`; the earlier reviewer and author of the repaired sublemma is `/root/astra_bl_synthesis`. I authored the earlier 372/369 contact and guard changes, which have separate non-author acceptances. I did not author the new 354/348 packing or the repaired pre-H argument. My earlier proposed cached-power 345 extension is outside this independent decision.

## Frozen inputs

Paths here are relative to `work/quartic-under300-20261107`.

| File | SHA256 |
|---|---|
| `06-detector-next/REPORT.md` | `d6f4746d63dbf23b4be16541c2358260c87af47326e4399ca94cf7d0522fec3c` |
| `06-detector-next/candidate354-ir.json` | `cf62d9dc594e037e26d2569563f36a4d51a02197b7a3285740338441981e121a` |
| `06-detector-next/mixed348/REPORT.md` | `28f8383ea3537bcaf0b91929d082abb82e62da6b608e1b0a9322c662701cb4ed` |
| `06-detector-next/mixed348/candidate348-ir.json` | `4782ed265f5d3c2d2241ea73445af5b1465f28a7580d634b825bd9d11710f22c` |

I read the actual squared-H reconstruction, preferred 392t reconstruction, 372/369 contact and conditional-domain arguments, corrected 354 and mixed348 reports, and the prior independent reviews and checkers. The new `check.py` verifies the repair directly against the eight current H component rows. It also replays the two earlier independent full finite checkers, with their single evidence-file writes redirected here. Those are disclosed replays, not newly authored independent finite implementations. All source and checker hashes are checked before and after execution.

## The pre-H repair is valid without the disputed difference-point interpretation

Use the exact constants and normalizations in the current equations: `a=-1+7*rho/4`, `c=a^2=(57-28*rho)/8`, `b=39/8-9*rho/2`, `D=11-6*rho`, with `b^2=c^2-D`. The stored H and V0 square outputs are `U=v311+2*rho*v312` and `V=v178+2*rho*v179`. The field value `W` is stored in 140/141 without the factor two. The current equations are

```
W=v^2, U*V=W^2, Q^2=U+V+2W, t*(U+W)=Q*v,
Q=(1-D*W-2*b*v)/c.
```

In the generic branch `U*Q!=0`, the exact three polynomial identities checked in `check.py` give `f=(U+W)/Q`, `F=(V+W)/Q`, `f^2=U`, `F^2=V`, `f*F=W=v^2`, `f+F=Q`, and `f*t=v`. Thus `f!=0` and `F=f*t^2`. Define the old slope by the actual inherited substitution `S=(b+c*t+D*v)/a`.

Here is a direct check that avoids any division by `c+D*f`. Put

```
K=f*(c*(1+t^2)+D*f*t^2+2*b*t)-1.
```

The restored Kummer equation gives `K=0`. The unconditional polynomial identity is

```
f*(b+c*t+D*f*t)^2-c+c*D*f^2
  =(c+D*f)*K + f*(b^2-c^2+D).
```

Both right-hand terms vanish. Dividing only by the nonzero fixed c and the already established f gives `S^2=1/f-D*f`. Therefore `x=1/f`, `y=S/f` is a genuine point on `y^2=x*(x^2-D)` at this stage, even if `c*x+D=0`. There is no claim yet that F is the reciprocal abscissa of H-P.

At a place above p>76176 the value group is Z and D is a unit. The curve equation gives even v(x): for v(x)>0, `2v(y)=v(x)`; for v(x)<0, `2v(y)=3v(x)`; valuation zero is already even. Hence v(f) is even. When F is nonzero, `v(F)=2v(v)-v(f)` is even. If F=0, its summand is simply absent. Conjugation permutes the relevant places, so the conjugated F-squared leaf has valuation divisible by four at every place, and its square has valuation divisible by eight.

For U=0, the literal equations give v=W=0 and V=1/c^2. For Q=0, they give U=V=-v^2 and `D*v^2+2*b*v-1=0`. The two fixed v values are `(3+2*rho)/4` and `(-36+16*rho)/49`. The independent coefficient/denominator/norm calculation leaves possible bad primes only 2 and 41 for c, only 2 for the first v, and 2 and 7 for the second. Thus all exceptional V0 leaves are units at every consumed place. This uses local integrality and norm units together; it does not infer individual place valuations from the norm alone.

## Packing and one common place

The other eight leaves are fourth powers directly from the unchanged biquadratic output identities, before any H interpretation. The literal logarithm square rows express each cached Zi as the square of the conjugated V_i squared leaf. The affine expressions, including the factor two and conjugation signs, pass the full finite replay. Therefore Ui has valuation in 4Z and Zi has valuation in 8Z, with zero leaves allowed.

For `alpha=v_p(R)>0` odd, `E=1/R`. The six summands of G0 have disjoint possible valuation classes modulo eight:

```
{0}, {-alpha,4-alpha}, {-2alpha,4-2alpha},
{-3alpha}, {-4alpha}, {-7alpha}.
```

For alpha=1 these partition all eight classes. Multiplication by an odd alpha permutes the classes and fixes the subgroup `{0,4}`. G1 deletes the final singleton. Thus every such group has a unique minimum, is nonzero, and has nonpositive valuation. The old higher-order factors retain their odd-valuation proof. Zero leaves and the fixed signed exceptional leaves cause no gap.

At a required prime the whole product W is nonzero, so its norm equation forces both its rational component and z nonzero. Set `T=Tr(W^-1)=1/z` only after this step. The actual bounded input is `B=R/(T^2*(1+R)^2)`. Since `1+R` is a unit and `Lambda=max_{w|p} v_w(W)`, trace integrality gives `v_p(B)<=alpha+2*Lambda`. The pole certificate excludes negative odd valuation. This yields `Lambda>-alpha/2`.

Choose a place attaining Lambda. Every factor, and hence every summand in a packed factor, has valuation greater than `-alpha/2`. Ui and Zi therefore have positive valuation, respectively at least four and eight. Their original f tests have valuation at least two, more than the required order one. The old order-ten and order-forty tests follow at this same place. No conclusion combines successful places from different groups.

In either pre-H exceptional branch, the unit Z0 contradicts this conclusion at every prime in any contact radical. All radicals would consequently be one. The unchanged pre-H root-height and independently established scalar anchor then contradict each other. Their availability does not require H, logarithm ratios, or the scalar height upper bound. Subsequent fixed-point exclusions and the original logarithm/Lucas/height proof now receive their original inputs. A radical-free detector requires no trace inverse, including when R=-1. This is the same conditional-domain convention as accepted369.

## Completeness and construction

At each selected contact prime alpha=1, the genuine complete points have positive f valuations. The curve parity lemma improves those to at least two. Thus all nonconstant terms have positive valuation because the Ui weights 1,2 are below four and the Zi weights 3,4,7 are below eight. Each group has residue one at the designated place. At another place its inverse has residue zero or one by the same unique-minimum argument. The full inverse product has those residues as well. The trace is a unit: its residue is one or two in the split case, and two in the inert case. This proves positive odd valuation one for B at selected primes.

Away from selected primes, the existing construction gives even valuation of R. The two rational squared denominators in B preserve parity, regardless of any new factor primes. Hence B has square reduced denominator. At 2,3,17 the old fixed neighborhoods bound the finitely many leaf valuations; increased prescribed denominator divisibility makes every positive power of E tend to zero, W tend to one, and T tend to two. At both real embeddings the complete leaves are nonnegative. For large positive lambda the groups are positive and tend to one uniformly in the fixed neighborhood. Thus all three bounded B values tend to zero positively and satisfy the same preparation-zero conditions simultaneously. These are changes in private detector values, not a claimed old-fiber bijection.

The accepted ordering of finite neighborhoods, denominator divisibility, selected contact primes and final H progression is preserved. No late prime-divisor restriction on the new sums is introduced. The scalar predicate and anchor are unchanged by these two candidates.

## Finite result and limits

Both finite replays pass, including complete consumer differences, cached powers, scalar sign involution and all primitive SOS coefficients. The 354 system has 324 residuals and 5,903 monomials; the 348 system has 318 residuals and 6,065 monomials. Both have degree four, content one and maximum coefficient `16*3^(2^26)`. No giant constant was expanded. This review supplies the missing non-author acceptance of the repaired sublemma and confirms the mixed packing's arithmetic and quadratic construction. It does not approve a 345 implementation, a positive-anchor composition, or a new ordinary-coefficient companion.
