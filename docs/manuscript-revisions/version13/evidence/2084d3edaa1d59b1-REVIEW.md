# Independent review of the Version13 release transformations

Reviewer: agent02. I accept the frozen394-to-411 release transformation, consecutive-coordinate remaps and explicit coefficient tables at the bindings below. My separate `check_release.py` imports no producer, author checker or project algebra helper. It independently recomputes the polynomials using Python's standard library. All checks pass.

This acceptance covers agent10's release transformations and table computations. I authored the preceding scalar-anchor component, so this review does not independently accept that component or the arithmetic/composition theorem. Those are separate reviews. The selected source is taken as the mathematical input to the release transformation. This report makes no claim that a manuscript has incorporated the result or that files have been published.

## Frozen scope

All reviewed originals are in `10-combination/release394`. The source is `10-combination/combined394-ir.json`, SHA256 `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5`. Its polynomial hash is `39e1f5c05a1a26be26b006703bccc2e1c23b8a15876fbd6d43749d5d464d3193`. The copies in the release folder are byte-identical to these two source files.

The release manifest `ARTIFACTS.json` has SHA256 `23078103389747c9176702d20b44e452b1a036a46c010ae4149789ececef3637`. Every one of its ten file hashes was independently checked. Important additional bindings are:

| Artifact | SHA256 |
| --- | --- |
| `candidate411-ir.json` | `b30e730bd65109a36be4f2a794222ff97dc292dcb3a4bd58de6e33f594e8c16c` |
| `compact394-ir.json` | `2f9007d746f0ae6ee9d69b2e8fc0436a482d9cfd9a6f98a4cc86781faab04a20` |
| `compact411-ir.json` | `27b280051cb06709f8bde7193b988d25570a216c003cfbb51bdcebe7590ed474` |
| `quartic-394-symbolic-coefficients.json` | `d69fb4eb5eb6f11f050f7b9a86462b2b6568ef39bf1ab578ffb2d1f77350ebbe` |
| `quartic-394-symbolic-coefficients.txt` | `652b594a94f6f7e8d5b905439fabc5c2a6f271564d4dcaeb99287451f0c58abe` |
| `quartic-411-ordinary-coefficients.json` | `40098c296c5cf7fbd07de7a4dfe9d265377c27cf0a98f7c7c5dfd615d2f6b5c2` |
| `quartic-411-ordinary-coefficients.txt` | `30d039965a0c90c2c22a7a239024ee42b53a372efee4396dcc627063a4fe24a2` |

I read the actual `prepare_release394.py` and `verify_release394.py`, but the independent checker imports neither. The older `release395` artifacts and older preparation scripts are outside this review.

## Coordinate and coefficient comparisons

Both compact maps sort the source coordinate IDs and assign consecutive physical indices starting at one. The checker compares every coordinate ID, source ID and name. Source coordinate 0 is named `input` and maps to physical x1 in both tables. It remains the same rational input; it is not added to the witness count. Every source residual is compared with its exact compact-coordinate substitution, including all metadata other than the substituted term list. No residual or variable is missing or duplicated.

I independently clear rational denominators and divide each residual by its integer coefficient gcd, then form its full ordered-product square. The sum agrees coefficient by coefficient with each source polynomial, compact polynomial and JSON coefficient table. I independently parse every noncomment text-table line as a decimal integer coefficient, nonnegative C exponent and ordered variable list. Those parsed polynomials agree with the JSON tables. Their coordinate-comment rows and input headers also agree.

Every stored coefficient in both coefficient tables is a decimal integer. In the ordinary411 table every C exponent is zero. The symbolic394 table retains C=3^(2^25) as a fixed integer parameter; it does not claim to print the enormous evaluated decimal digits of C. There are no duplicate physical monomials hidden under different C powers: the counts below are counts of actual variable monomials, not merely pairs of monomials and parameter powers.

## Ordinary lift and both-direction maps

The ordinary lift adds seventeen coordinates. Sixteen form the chain

    c0=3^1024,  c1=c0², ..., c15=c14².

They have source IDs 702 through717 and physical IDs 395 through410. The last value is exactly

    c15=3^(1024*2^15)=3^(2^25)=C.

The seventeenth coordinate has source ID 718, physical ID 411, and name `constant.C_times_tau`. Its equation is

    q=c15*tau.

Here tau is source coordinate 549, physical coordinate 305. The anchor W is source coordinate 57, physical coordinate 53. The original fixed-coefficient term -4*C*tau*W becomes -4*q*W. Both the new product equation and the altered anchor remain quadratic. Direct replacement of C by a variable without this extra gate would have created a cubic residual, so the total is411 rather than410.

I checked all sixteen chain equations and the extra product equation literally. The only changed pre-existing residual is `anchor.translatedEquation`, row 504. Substituting q=C*tau restores it exactly. Every other pre-existing row and coordinate is unchanged. No chain coordinate is consumed elsewhere unexpectedly.

For the forward map append the uniquely specified chain values and q=C*tau to any rational394 witness. Every ordinary residual then vanishes. For the reverse map the chain equations force these exact values successively, and the product equation forces q=C*tau. Forget the seventeen added coordinates to recover every symbolic394 residual. No division or nonzero hypothesis is used. The chain equations are c_j=c_(j-1)², not equations introducing a square-root sign choice. The maps therefore establish exact rational-witness equivalence and fix the input.

Each polynomial is a sum of squares of nonzero rational multiples of its displayed residuals. Over Q its vanishing is equivalent to simultaneous residual vanishing. Primitive normalization thus does not change either direction of the argument.

## Counts and maximum coefficients

| Quantity | Fixed-coefficient form | Ordinary form |
| --- | ---: | ---: |
| Total variables | 394 | 411 |
| Witnesses | 393 | 410 |
| Quadratic residuals | 364 | 381 |
| Quartic monomials | 6,338 | 6,388 |
| Total degree | 4 | 4 |
| Integer content | 1 | 1 |

The exact largest absolute coefficient of the symbolic394 polynomial is 16*C²=16*3^(2^26). Its unique C² term has source variable monomial W²*tau². Every C-linear multiplier has absolute value at most 96, and every C-free coefficient has at most 1,520 bits. The physical monomial has no other parameter-power contribution, so these bounds prove the asserted maximum after evaluating C.

The ordinary411 maximum is its constant coefficient, exactly 3^2048 plus the constant coefficient of the symbolic394 polynomial. The full explicit delta and the resulting decimal integer are recorded in `checks.json`; the delta agrees with the manifest's exact formula. This maximum has 3,247 bits and 978 decimal digits. Every other coefficient has at most 1,625 bits. These are exact computations, not numerical logarithm estimates.

## Exact byte counts

These are raw file byte counts at the reviewed hashes, including their actual line endings.

| File | Bytes |
| --- | ---: |
| `candidate394-ir.json` | 453,081 |
| `candidate411-ir.json` | 462,176 |
| `compact394-ir.json` | 408,870 |
| `compact411-ir.json` | 418,238 |
| `polynomial394.json` | 937,325 |
| `polynomial411.json` | 944,989 |
| `quartic-394-symbolic-coefficients.json` | 973,221 |
| `quartic-394-symbolic-coefficients.txt` | 212,067 |
| `quartic-411-ordinary-coefficients.json` | 982,235 |
| `quartic-411-ordinary-coefficients.txt` | 214,957 |
| `ARTIFACTS.json` | 2,573 |

The ten manifest-listed artifacts total 6,007,159 bytes. Including the manifest, these eleven files total 6,009,732 bytes. These totals do not describe the portable lineage package or any later archive, which was still being assembled separately and is outside this review.

The review found no error in the frozen release transformations or tables. Run `python -B check_release.py` in this review directory to reproduce all finite checks. Its result is `checks.json`. Originals were read only; all review outputs are in this directory.

