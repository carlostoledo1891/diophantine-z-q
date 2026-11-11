# Independent composition acceptance: candidate369

Accepted for the exact frozen composition below, on the inherited arithmetic inputs. The candidate has the same rational input projection as accepted372 and therefore defines the integers over Q. It has 369 total variables, 368 witnesses, 339 quadratic residuals and 6,568 quartic monomials. Degree, integer content and maximum coefficient are four, one and 16*3^(2^26).

Reviewer: `/root/astra_quartic_opt01_elimination`. I authored neither the new contact-polynomial detector nor this composition. This is a fresh review of the changed domain on the actual372 interface. It does not infer composition correctness merely from the older387 guard review. No full-witness bijection, ordinary companion or manuscript release is asserted. Version13 remains unchanged.

## Frozen scope

Paths are relative to `work/quartic-under300-20261107`.

| Artifact | SHA-256 |
|---|---|
| Source `10-combination/unweighted372/candidate372-ir.json` | `ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce` |
| Source acceptance `01-elimination/review372/REVIEW.md` | `3e5a5fe8a14025979b27bbb45c55f35d55c0237082f4fd7a299babc9b3e9d997` |
| Proposal `10-combination/REPORT369.md` | `60913ea2024a0d2e20d206b99ce05fdb1a81a0f0b04704b85df9b3b230a548e0` |
| Candidate `10-combination/candidate369-ir.json` | `b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095` |
| Polynomial `10-combination/polynomial369.json` | `906179089ce38d574ae8ff64398078db63d4a035d3e3b15d537a963972c20267` |
| Author verifier `10-combination/verify369.py` | `7cbf64a602bc7dca67e3cd32a229448b0df89637e82805c07df889c39c5b3be4` |

I read the frozen composition argument and inspected the current E, norm and B equations directly. The actual contact identities, current toric product identities, positive-contact scope, signed390 exceptions and ordered372 completeness construction are as checked in the pinned source review. The underlying manuscript remains `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, with the current depth24/order10 and point-domain amendments.

## Independent finite check

The local checker imports no producer or other checker. Exactly coordinates 382,430,478 and rows 334,384,434 disappear. Each deleted coordinate occurs only in its deleted inverse row, which is exactly 1-w0*inverse=0. Every retained residual, coordinate object and metadata object is identical to372, apart from the descriptive status. In particular all three ER=1 equations, all toric weights and hybrid products, and all point/anchor/scalar rows are preserved.

The checker independently extracts R as the affine coefficient of E in each actual ER-1 row. It verifies that the corresponding norm and B rows are precisely

    w0²-2w1²=2w0*z,
    B*(R+E+2)=z².

The full primitive SOS was independently expanded and compared coefficient by coefficient. Every coordinate occurs, all residuals have degree at most two and the output has exact degree four and content one. Distinct symbolic terms have distinct ordinary coordinate monomials. The unique C² term is 16*C²*v57²*v549²; C-linear coefficients are at most96 and C-independent coefficients have fewer than2048 bits. The maximum is therefore unchanged without expanding C.

The frozen author verifier was also replayed with its sole output write redirected to this directory. It agrees. Hashes confirm that no pre-existing author file changed. Reproduction: run `python -B check.py` and `python -B replay.py` here; their local outputs are `CHECKS.json`, `AUTHOR-REPLAY.json` and `REPLAY-PINS.json`.

## Fresh domain argument for the new R

Here R is F5(A*lambda), not either earlier delta-normalized parameter. ER=1 holds globally, so E and R are always nonzero and all five contact values are excluded. The toric chain therefore decodes globally to weights E, E^19 and E^79. There is no E=0 branch and no division by t-1. This step does not need the deleted guards.

Before H is interpreted, product factors have the necessary square or signed-square meanings only on the two classified exceptional branches. After those branches are excluded, they have their ordinary square meanings. The conditional proof below is applied in those respective settings, not to arbitrary nonsquare leaves.

Fix a prime in one detector's required odd-contact radical. The unchanged contact identity gives an odd positive alpha=v_p(R). A nonzero nonconstant term in a factor

    1+epsilon*R*(D/R^m)²

has odd valuation 2v(D)-(2m-1)*alpha. It cannot have valuation zero, so the factor cannot vanish. If D=0 the factor equals1. Thus the actual W is nonzero. This conclusion precedes any trace or B interpretation.

If w0=0, the retained norm equation forces w1=0 over Q, contradicting W nonzero. Therefore w0 is nonzero, its field norm is nonzero, and z=Norm(W)/(2w0) is nonzero. Thus T=Tr(W^-1)=1/z is defined and nonzero. Also 1+R is a unit at this prime, hence is globally nonzero. The B equation now gives exactly

    B=R/(T²*(1+R)²)!=0.

The unchanged normalized and factored pole rows reconstruct the preparation-zero obstruction on this B. Their soundness conversion permits arbitrary signs of B and zero private conic factors; it requires no deleted inverse beyond the nonzero input just proved.

Let lambda_p be the largest valuation of W over places above the prime. All factor valuations are nonpositive, and trace integrality gives v_p(T)>=-lambda_p. Since 1+R is a unit,

    v_p(B)<=alpha+2lambda_p.

The left side is odd and the pole excludes negative odd values. Therefore lambda_p>-alpha/2. At a place attaining lambda_p, each factor has valuation at least lambda_p. This yields v(D)>(m-3/4)*alpha>=m-3/4, and unramified integrality gives v(D)>=m. The signs epsilon=+1 or -1 do not change any step. This recovers the exact local conclusion needed, on the actual new R and B formulas.

For a detector with radical1, no such trace conclusion is asserted or needed. In particular, the potential R=-1 branch cannot contain a required prime, since every valuation of -1 is zero whereas such a prime would give positive valuation of R. The B equation then forces z=0 and the norm equation forces W=0; it need not reconstruct an old inverse. These possible extra auxiliary solutions are harmless only because the global proof consumes no local tests from a radical equal to1. The argument does not claim that this branch has rational t solutions or that all new witnesses lift to372.

## Signed H exclusions and whole soundness

On U=0 the unchanged squared-H equations give the low conjugate-V leaf as the square of the fixed unit 1/conjugate(c). On Q_H=0 they give U=V=-v² with v one of the two classified fixed units. Every other leaf is a square independently of H. The conditional result above therefore applies at any prime in any radical, with the negative signs only where justified. It would force a fixed unit to have positive valuation, a contradiction. Thus all three radicals must equal1 on either branch.

The unchanged root-product height theorem then gives Bmax²-6<7*Hcal. Independently, the unchanged scalar reciprocal guard identifies a nonzero even scalar point, its unconditional coefficient lemma restores the old anchor inverse, and the rescaled anchor gives Bmax>=|a|>(40*Hcal)^10. This is a contradiction. No scalar height upper bound, H logarithm or trace at a radical-free detector is used. H is reconstructed only after these exclusions.

The subsequent finite H/V0 exclusions have the same structure: the fixed unit leaf contradicts every possible required prime, and all radicals1 contradict the pre-ratio anchor-height bounds. Therefore the current enlarged point domains, nonzero logarithms and half-index identities remain valid. At genuine points the conditional local result supplies the same simultaneous comparison orders at every prime in every radical. It gives the same order40 radical divisibility for the Lucas residual and order10 divisibility for the input-error numerator. A radical of1 contributes a vacuous divisibility statement.

The root-scale height theorem, scalar depth24 bound, anchor margins, Lucas contradiction and current parity-sensitive input bridge depend only on those premises. They still force n=51*(2X+1)²+2504 with n odd and X integral. This is a rerun of soundness through the current local interface, not an invocation of full372 soundness after a nonexistent lift of all guards.

For completeness, take the complete372 witness supplied by its independently accepted ordered construction and forget the three private inverses. Every remaining equation holds literally. No new finite, real, prime or CRT choice is required.

The two inclusions establish equality of input projections. The exact369 composition is accepted; no defect or unresolved condition remains within the stated inherited arithmetic scope. The below300 publication threshold is still unmet.
