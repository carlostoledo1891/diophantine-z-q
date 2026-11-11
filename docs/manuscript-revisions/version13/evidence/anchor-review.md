# Independent review of the scalar-anchor rescaling

Accepted as the exact 399-to-398 transformation below, subject to the stated source arithmetic inputs. This is not independent acceptance of the entire 399 baseline: its final composition review was still pending when this review was written. The rescaling itself preserves the full rational solution set by inverse maps, keeping the input and all nonprivate coordinates fixed.

Reviewer: `/root/astra_quartic_opt01_elimination`. I did not author this rescaling. I read the frozen report and code, the actual source scalar equations, and the inherited scalar coefficient lemma and reciprocal-chart proof. My independent checker imports no author implementation or checker.

## Bindings and exact result

| Artifact | SHA-256 |
|---|---|
| `10-combination/combined399-ir.json` | `eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b` |
| `02-squares/beyond399/candidate398-ir.json` | `9f0b668f42878cb1bf113680052a51b466d6b00966c3bb7ef540688316f5b79b` |
| `02-squares/beyond399/polynomial398.json` | `ee5ce67c075e550d61dc9901c4e34a86724a7d4cd11aa66c57c806f93169077c` |
| Inherited `manuscripts/quartic_v12.tex` | `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9` |

The result has 398 total rational variables, 397 witnesses, 367 quadratic residuals and 6,349 quartic monomials. Its degree is four and its content one. The maximum coefficient remains exactly 16*3^(2^26).

## Source point interpretation before any anchor inference

Write the unchanged odd root as S=(x,h*j), where x=h squared and j squared=x squared-D. The source's particular-field chart and odd-root identification give S=[a]P for an odd integer a. This is a source arithmetic input, independent of the scalar anchor. The checker matches the actual S equations, including x=coordinate84+2*coordinate85*sqrt(2).

The retained scalar equation is

    d*g=a_*j-b_*h,       d=c_*x+D,

where c_*=a_* squared and b_* squared=c_* squared-D. I matched both physical component equations directly. It follows that g is the same quotient as in the source reciprocal-chart proof. Since x=h squared is nonnegative at both real embeddings and D,c_* are positive there, d is nonzero. This argument does not use either inverse guard or the anchor.

The new guard g0*tau=1 implies g0!=0, hence g!=0. The source subtraction identities, at manuscript lines 20385–20445, now identify g squared with f(S-P). Their use requires only the just-established quotient and nonzero g. They do not require the old f1 inverse. The deleted k coordinates are unnecessary for this identification: their values can be supplied by the rational formula in that source proof.

The equal-abscissa cases are essential here. If S=P, the same quotient gives g=0, contradicting the new guard. If S=-P, the source's explicit duplication calculation gives the actual point R=-2P and the same f(R)=g squared. It is unnecessary to exclude S=-P by an anchor bound at this stage. In every case R=S-P=[s]P has a nonzero even integer index s=a-1.

Thus the nonzero-even orbit hypothesis is proved before using the scalar coefficient lemma, before restoring an inverse, and before recovering any anchor divisibility or size bound. The later enlargement of H has no role: this argument concerns the unchanged S chart and fixed P only.

## The coefficient lemma has the needed unconditional scope

The inherited lemma `lem:v12-anchor-coefficient`, lines 20115 onward, explicitly applies to every nonzero even integer s, not merely indices already satisfying the anchor. It gives

    v3(f1([s]P))=2+2*v3(s),

so f1 is nonzero. I read its proof: the starting point 2P has z(2P)/3 congruent to 2+sqrt(2) modulo 3; multiplication by units and repeated multiplication by 3 preserve the asserted leading term in the integral formal group. The formal curve identity then makes the leading residue of f/3^(2+2v3(s)) equal to sqrt(2). Independence of 1 and sqrt(2) in the residue field proves the exact coefficient valuation. This proof uses no anchor equation or scalar inverse guard and includes negative s. The local checker independently verifies the displayed starting rational residue and its square.

Apply the lemma to the point just identified. Since f(R)=g squared, its irrational coefficient is F=2*g0*g1. Therefore F!=0, and in particular g1!=0. This is the required noncircular restoration of the deleted f1 guard. It is not a claim that the new anchor alone excludes g1=0.

## The inverse maps

The old subsystem is

    F=2*g0*g1,       F*sigma=1,
    u^2+6*v^2-2*w^2-3*F^2-4*C*w=0.

The new subsystem is

    g0*tau=1,
    U^2+6*V^2-2*W^2-12*g1^2-4*C*tau*W=0.

For an old solution, F!=0 implies g0!=0. Set tau=1/g0 and (U,V,W)=(u,v,w)/g0 and forget F. Dividing the old anchor by g0 squared gives the new one.

For a new full solution, the preceding point argument proves F=2*g0*g1!=0. Set sigma=1/F and (u,v,w)=g0*(U,V,W). Restore F with this value. The old definition and inverse then hold. The exact polynomial identity verified independently is

    q_old(substituted)-g0^2*q_new
       =4*C*g0*W*(g0*tau-1).

It gives the old anchor. All other equations are unchanged. The two maps are inverse because each guard uniquely determines its inverse variable. No division uses U,V,W, H, an input value, or a logarithm.

The isolated new anchor admits g0=1,g1=0,tau=1,U=V=W=0, so a purely polynomial equivalence claim for arbitrary g would be false. The accepted statement is about full systems with the stated point-domain inputs. The nonzero-even scalar lemma excludes precisely that problematic branch. Zero values of individual private anchor witnesses remain permitted and cause no difficulty.

## Complete finite audit and coefficient bound

The independent checker confirms that coordinate505 is the only deleted coordinate and residual471 is the only deleted residual. Coordinates55,56,57 are renamed for their new scaled meanings, and coordinate549 becomes the g0 inverse. The old incidence is exactly: each private anchor witness occurs only in row504; F occurs only in rows471,504,699; the old inverse occurs only in row699. Every other row and coordinate object is identical. The input and fixed parameter are preserved.

The checker matches all old and new subsystem rows, proves the scaling identity, and expands the entire primitive sum of squares. Every coefficient matches the frozen polynomial. Every retained coordinate occurs, and all residuals have degree at most two. The 6,349 symbolic terms have distinct coordinate monomials even after the fixed C is substituted, so the term count does not hide a coefficient collision.

The unique C-squared term is

    16*C^2*W^2*tau^2.

There is no constant or C-linear contribution to that same coordinate monomial. Other C-linear multipliers have magnitude at most 96, and all constant coefficients have at most 1,520 bits. Since C=3^(2^25), these are strictly smaller than 16*C squared. Thus the maximum is exactly 16*3^(2^26), now on a degree-four monomial. No enormous integer was expanded.

Run `python -B check.py` in this review directory to reproduce `CHECKS.json`. The source and author artifacts were read only. This component acceptance may be transported to a later accepted composition only after checking the same full incidence, unchanged S/g point meaning, and the complete rescaled anchor delta there.
