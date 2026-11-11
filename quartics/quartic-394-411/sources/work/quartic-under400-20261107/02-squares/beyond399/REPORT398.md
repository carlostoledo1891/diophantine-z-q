# One smaller scalar anchor

The candidate removes one coordinate from the frozen399 source. It has 398 total rational coordinates, 397 witnesses, 367 quadratic residuals and 6,349 quartic monomials. The degree is four and the content one. All published and earlier frozen packets remain unchanged. Independent review is pending.

## Exact bindings

- Source `10-combination/combined399-ir.json`: `eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b`.
- Candidate `candidate398-ir.json`: `9f0b668f42878cb1bf113680052a51b466d6b00966c3bb7ef540688316f5b79b`.
- Polynomial `polynomial398.json`: `ee5ce67c075e550d61dc9901c4e34a86724a7d4cd11aa66c57c806f93169077c`.
- Inherited arithmetic source `manuscripts/quartic_v12.tex`: `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. Lemma `lem:v12-anchor-coefficient`, lines20115–20129 and its following proof, applies to every nonzero even integer scalar index. The scalar reciprocal chart identification appears at lines20385–20445.

The latest source includes the changed input label, deterministic scalar correction and H-domain relaxation. None is changed here. This packet is also disjoint from the pending scalar preparation and pole normalizations.

## Literal old and new equations

Let g=g0+g1*sqrt(2) be the retained scalar reciprocal coordinate, and let F be the irrational coefficient of f(R)=g². Let C=3^(2^25). The source rows are exactly

    F=2*g0*g1,
    F*sigma=1,
    u²+6*v²-2*w²-3*F²-4*C*w=0.

The coordinate IDs are F=505, g0=543, g1=544, sigma=549, u=55, v=56, w=57. The three anchor coordinates are private: each occurs only in the last row. F occurs only in these three rows. The inverse coordinate occurs only in the middle row.

Delete F and its definition. Repurpose sigma as tau and u,v,w as U,V,W, with new equations

    g0*tau=1,
    U²+6*V²-2*W²-12*g1²-4*C*tau*W=0.

Both rows are quadratic. Every other residual and coordinate is the literal source object. A direct substitution of F=2*g0*g1 into the old anchor would have degree four; rescaling the private anchor variables is essential.

## Forward map

Every source solution has F nonzero, hence g0 and g1 nonzero. Put

    tau=1/g0,
    U=u/g0, V=v/g0, W=w/g0.

Equivalently tau=2*g1*sigma, so no new existence assertion is required. Divide the old anchor equation by g0² and substitute F=2*g0*g1. This is exactly the new anchor equation. Forget F and retain all other coordinates.

## Reverse map and the arithmetic dependency

The new guard gives g0 nonzero, so g is a nonzero field element. The unchanged odd root S and unchanged scalar reciprocal-chart equations therefore identify R=S-P as a genuine nonidentity scalar point. Since S has an odd integer label, R=[s]P for a nonzero even integer s. This conclusion needs no anchor divisibility condition. The equal-abscissa S=-P case, if considered before the anchor is restored, still gives the nonzero even index s=-2.

The inherited lemma applies to every such s and states

    v3(f1([s]P))=2+2*v3(s).

Thus F=2*g0*g1 is nonzero. In particular g1 is nonzero; this fact is proved before restoring an inverse. The lemma is independent of the anchor condition, so its use here is not circular.

Set

    F=2*g0*g1, sigma=1/F,
    u=g0*U, v=g0*V, w=g0*W.

The old definition and inverse hold. Multiplying the new anchor by g0² and using g0*tau=1 recovers the old anchor. Every other old equation is unchanged. The maps are inverse on the full rational solution sets, with the input and all nonprivate coordinates fixed. The inherited arithmetic lemma is required for the reverse inverse coordinate; the polynomial scaling identity alone does not establish it.

## Zero and counterexample audit

- g0=0 is directly excluded in the new system and was excluded by F nonzero in the source.
- g1=0 is excluded in a full new solution by the nonzero-even scalar lemma. It is not excluded by the new anchor alone.
- In fact the isolated new anchor subsystem admits g0=1, g1=0, tau=1 and U=V=W=0. This is a counterexample to any claim of equivalence for arbitrary rational g. It is not a full candidate solution, because the unchanged scalar point interpretation and inherited lemma exclude it.
- U,V,W may individually or simultaneously be zero; no division uses them.
- No division uses the input, a detector value, the changed scalar correction, the H index or a comparison-point parameter.

## Exact finite certificate

If q_old and q_new denote the two anchor residuals above, substitute u=g0*U, v=g0*V, w=g0*W and F=2*g0*g1. The unconditional polynomial identity is

    q_old - g0²*q_new = 4*C*g0*W*(g0*tau-1).

`verify_anchor.py` checks this identity exactly, the literal old/new rows, all five private-coordinate incidences, every unchanged outside object and the complete primitive sum of squares. It also checks coordinate coverage, integer content and quadratic residual degree. It uses only the Python standard library and imports no producer. The output is `verification398.json`.

Run `python -B build_anchor.py` followed by `python -B verify_anchor.py`. Both pass. A reviewer must separately confirm the full-source scalar-domain application and the nonzero-even lemma before accepting the candidate.
