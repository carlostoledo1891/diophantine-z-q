# Final-publication checks: Browning–Loughran and Browning–Heath-Brown

Reviewer: `/root/astra_v14_baseline_compiler`, non-author model reviewer. Local date: 2026-11-07; retrieval timestamps are UTC on 2026-11-08. This supplement preserves all earlier baseline records.

## Decision

**Browning–Loughran: the final-publication comparison is complete for the consumed Theorem 4.1 interface.** A genuine AMS final typeset PDF was retrieved, its journal imprint inspected, and the statement, definitions and uniformity convention on printed pages 5772–5773 compared visually with the retained accepted manuscript. No mathematical difference affecting this application was found. This removes the specific “final typeset text not accessible” qualification for this bounded BL application, not any unrelated proof obligation.

**Browning–Heath-Brown: the final-publication comparison remains open.** The publisher's accessible record confirms the article but says the full content is unavailable. Ordinary requests to its HTML and PDF endpoints returned HTTP 405 human-verification HTML, not a PDF. The lawful Oxford repository explicitly identifies its copy as an accepted manuscript. The author's publication list links arXiv. No final BHB text was obtained, and no access control or verification challenge was bypassed. The accepted/arXiv qualification must remain.

## BL provenance and comparison

The retrieved publication is T. Browning and D. Loughran, *Sieving rational points on varieties*, Transactions of the American Mathematical Society 371 (2019), 5757–5785, DOI [10.1090/tran/7514](https://doi.org/10.1090/tran/7514). The [direct AMS PDF](https://www.ams.org/journals/tran/2019-371-08/S0002-9947-2018-07514-6/S0002-9947-2018-07514-6.pdf) returned HTTP 200 and a PDF signature. It is saved as `bl-final.pdf`: 405,106 bytes, SHA-256 `51bafd17097d8bf227a63c885973586a9645546fadb7eea6b5e5ebefe2a361c3`.

The first page has the AMS journal imprint, volume 371, number 8, the article page range and DOI; the PDF has 29 pages. Rendered pages `bl-page-1.png`, `bl-page-16.png` and `bl-page-17.png` were directly inspected. The latter two are printed pages 5772 and 5773. They were compared with accepted-manuscript PDF pages 17–18 (author pages 16–17), rendered here as `bl-accepted-page-17.png` and `bl-accepted-page-18.png`. Text extraction was used for navigation only; font-encoding warnings make the page images the controlling evidence.

The following interface is unchanged between the accepted and final versions:

- An isotropic integral quadratic form F with nonzero discriminant, in n ≥ 5 variables.
- A smooth nonnegative compactly supported weight with gradient of F bounded away from zero on its support.
- Modulus M coprime to twice the discriminant; each prime-power allowed set is a nonempty subset of the local zeros consisting of vectors nonzero modulo that prime.
- The count is over **all** integral zeros satisfying the specified local conditions, with weight w(x/B). Its leading factors are the real density, unrestricted p-adic densities away from M, and `|Omega_(p^a)| / p^(a(n−1))` at primes dividing M.
- The error is `O_(epsilon,F,w)(B^(n/2+epsilon) M^(n/2+epsilon))`. The subsequent paragraph explicitly excludes dependence on M. No cardinality-dependent loss for the allowed subsets is inserted.

This is a comparison of the statement and conventions actually consumed; it is not a fresh reproof of the circle method in the remainder of Section 4, nor a claim that the entire accepted and final PDFs are identical.

## BL application to the fixed manuscript

The consumer is `lem:v5-primitive-count`, fixed v13 lines 16650–16694, especially the BL call at 16665. The fixed manuscript hash is `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. The relevant independent Gaussian contracts are GAU-003 and its downstream medium-prime consumers.

The source form is specialized to `Q_kappa = a²+b²−c²−d²−kappa w²`, with kappa nonzero. The displayed rational zero `(1,0,1,0,0)` proves isotropy; nonsingularity follows from the diagonal matrix, and every discriminant prime lies among those dividing 2 kappa. Consequently the manuscript's squarefree m, coprime to 2 kappa, is an admissible M. A compact support avoiding the origin gives the required gradient lower bound for this nonsingular form. Empty allowed sets are handled separately, as the source's formulation requires nonempty sets.

The source count is not itself primitive. The manuscript applies Möbius inversion to the common coordinate divisor h. Terms with `(h,m)>1` vanish because the allowed vectors are nonzero modulo each prime dividing m; otherwise multiplication by `h^(-1)` transports each allowed set bijectively, preserving its cardinality. Replacing B by B/h makes the error sum convergent. Thus the final source supplies exactly the same uniform unprimitive input needed by that argument.

The factors `ell^4−1`, positivity of the final constant, the tail from extending the Möbius sum, and the later sieve estimates remain the manuscript's stated internal deductions and local-density calculations. They are not substituted into the published theorem by assertion. In particular, the source's generic weight notation does not remove the need to choose a weight meeting the real cone when a positive real density is wanted.

The bounded final-version comparison introduces no source-strengthening, no new hypothesis, and no replacement of the independently audited Gaussian proof.

## BHB remaining requirement

The target is T. D. Browning and D. R. Heath-Brown, *The geometric sieve for quadrics*, Forum Mathematicum 33 (2021), no. 1, 147–165, DOI [10.1515/forum-2020-0074](https://doi.org/10.1515/forum-2020-0074), Lemmas 2.1 and 4.1 and the lattice-basis argument used later in Section 4.

The [publisher record](https://www.degruyterbrill.com/document/doi/10.1515/forum-2020-0074/html) was readable through web retrieval, including metadata and references, but not these theorem statements. The local attempted PDF is deliberately saved as `bhb-final.html`; it is not a PDF and is not source evidence for a theorem. The [Oxford record](https://ora.ox.ac.uk/objects/uuid:029537a5-f3a1-4ec7-a96f-07533accd494) labels its linked file “Accepted manuscript” and expressly distinguishes the final publisher version. [Browning's publications page](https://tdbrowning.github.io/pubs.html) links the arXiv version. These facts do not establish final-version identity.

The remaining comparison must check the exact hypotheses and uniform constants for the inhomogeneous coprime-polynomial box bound, including exclusion of common constant prime factors; rank-preserving odd primes and squarefree q in the lattice covering lemma; the determinant and containment of q Z^m; Euclidean successive minima and their largest-minimum tail; and the later bounded-basis/inverse estimates consumed by the manuscript. The existing accepted-text audit supplies those interfaces, but it cannot establish their equality with an unread final edition.

## Integration instructions

No main TeX or repository record was changed. If this check is accepted for integration, the BL bibliography note at fixed v13 lines 21675–21677 may be replaced by a bounded statement that Theorem 4.1 and its adjacent conventions were compared with the final published text, pp. 5772–5773, using this pinned PDF. The BHB note at 21683–21685 should remain qualified. This supplement is separate from and does not rewrite the earlier Gaussian review, which correctly described the evidence available to it.

`RETRIEVAL.json` preserves the initial sandbox-network failures; `RETRIEVAL-network.json` records the subsequent ordinary authorized network requests, status codes, resolved URLs, byte counts and hashes. `COMPARISON.json` contains machine-readable decisions and source/consumer pins. `MANIFEST.json` binds the artifacts. No purchase, login, correspondence, publication or remote mutation was performed.
