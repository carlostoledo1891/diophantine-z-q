# BHB published-version comparison

The user supplied the purchased final publisher PDF on 7 November 2026. I inspected the journal imprint and the published Lemmas 2.1 and 4.1, their relevant definitions, and the Section 4 basis and inverse-coordinate argument. The consumed mathematical contracts match the accepted manuscript. No mathematical change to these applications is required by this comparison. The former statement that the final BHB text was unavailable is now obsolete for this bounded scope.

This is a factual source comparison by `/root/astra_v14_baseline_compiler`, not a coverage acceptance, a whole-paper reproof, or permission to redistribute the licensed PDF. The independent source reviewer must adopt the evidence and update the finding disposition. No manuscript, catalog, gate, or prior audit record was edited.

## Source identity and provenance

Final source: `C:/Users/glaze/Downloads/10.1515_forum-2020-0074.pdf`, copied unchanged to local-only `received-final/BHB-published-local-only.pdf`. SHA256 `b0f962ca0403f693f9d860260b18bd3960359406008a59db5d9a967834b2cfa0`; 812307 bytes; 19 pages. The first page visibly identifies De Gruyter, Forum Math. 2021; 33(1):147–165, the authors and title, DOI 10.1515/forum-2020-0074, receipt 25 March 2020 and revision 14 September 2020. Metadata identifies the De Gruyter LaTeX layout and creation date 17 December 2020. The source is supplied by the user after purchase, not recovered through a bypass or assumed from an author-version filename.

Accepted comparison source: `work/quartic-version5-release/sun-proof/sources/BHB-accepted.pdf`, SHA256 `1e2a4d3d3f731c0ee67599cfa50f899fe499e51d4a452455a04f2d0a35e7191c`, 405739 bytes. Its status remains accepted manuscript. Its bytes have not been relabeled as final.

`received-final/RECEIPT.json` records final source metadata. `FINAL-COMPARISON.json` pins the consumed locators. Rendered final pages 1,2,4,9,10,11,12 and accepted pages 6,13,16,17 were visually inspected. Existing accepted text for pp.14–15 and18 was also compared with final pp.155–158. The PDF extractor reported duplicate ToUnicode dictionary keys; the material formulas, subscripts and inequalities were checked in rendered pages rather than inferred from extraction alone.

## Exact contracts compared

| Contract | Accepted author pages | Published pages | Comparison |
|---|---|---|---|
| Global coordinate norm | 2 | 148, PDF2 | Vertical bars denote the supremum norm. This differs from the explicit Euclidean successive-minimum convention, as it already did in the accepted source. Fixed-dimensional norm conversion is absorbed only into dimension-dependent constants. |
| Box parameters and coefficient height | 6 | 150, PDF4 | V is the product of the B_i, B_min their minimum, and H(f) the maximum absolute coefficient. Same definitions. |
| Lemma2.1 | 6 | 150, PDF4 | Same inhomogeneous polynomial statement over Z[X_1,...,X_n], no common factor in that ring, degree at most d, heights at most H, and B_i,H,M at least2. Same bound V log(VH)/(M log M)+V log(VH)/B_min. The implicit constant depends only on d,n and is independent of r. Constant-prime common factors are excluded; coprimality merely over Q is insufficient. |
| Good primes and lattice definition | 13 | 155, PDF9 | Same requirement that p be odd and preserve the rank of R. The modulus is a product of distinct good primes. Lambda(y) consists of x in Z^m congruent to rho*y modulo q for some integer rho, with gcd(y,q)=1. It has rank m and determinant q^(m-1). |
| Lemma4.1 cover | 13 | 155, PDF9, equations4.2–4.3 | Same hypothesis rank(R) at least3 and same cover of all zeros modulo q by at most (3m)^omega(q) q^(m-2) lattices. |
| Lemma4.1 tail and norm | 13–14 | 155, PDF9, equation4.4 and next sentence | Same bound O_m((3m)^omega(q)q^(2m-3)L^(-m)) for lattices whose largest Euclidean successive minimum exceeds L, for every L>0. No coefficient-height parameter enters this bound. |
| Inclusion and dual argument | 14–15 | 155–156, PDF9–10 | Same qZ^m subset Lambda(y) subset Z^m, dual inclusion, transference inequality, short integral dual vector, hyperplane-slice estimate, and divisor sum. |
| Product of minima | 16 | 156, PDF10, equation4.6 | Same q^(m-1) <= product lambda_i <<_m q^(m-1). |
| Basis, inverse and coordinates | 16–17 | 157, PDF11, first five paragraphs | Same lambda_m<=q, basis columns e_j of size O_m(lambda_j), matrix entries O_m(q), determinant q^(m-1), inverse rows e_j^* of size O_m(lambda_j^(-1)), and w_j=e_j^* dot x=O_m(|x|/lambda_j). The direction of every inverse factor was checked visually. |
| Substitution and content | 17–18 | 157–158, PDF11–12 | Same argument for the source's homogeneous K_i after substituting (a(q),EW), nonsingular rational change of variables, exclusion of remaining constant prime factors outside a(q), and height bounded by a power of B before applying Lemma2.1. This source argument does not replace the manuscript's separate inhomogeneous fixed-coordinate and content checks. |

For the actual rank3 application, these statements give at most 9^omega(q)q lattices, determinant q², qZ³ containment, lambda_3<=q, and tail O(9^omega(q)q³T^(-3)). The two-polynomial affine bound applies to the manuscript's two- and three-variable uses with the stated integer-content condition. These specializations are unchanged from the previously reviewed accepted-source interface.

Relevant manuscript targets are `V6-AUDIT-BHB-BOX`, `V6-AUDIT-BHB-LATTICES`, `eq:v5-box-sieve`, `eq:v5-lattice-tail`, `lem:v5-large-sieve`, and the later same-position obstruction-tail use. Current preview lines16777–16800 state the imported contracts; the large-sieve lemma starts16801. This comparison supplies the missing edition check. It does not assert that every downstream application obligation is automatically satisfied.

## Notation slips and corrections evidence

The final publication retains three notation slips already present in the accepted text. They must not be silently represented as corrected publisher wording.

- Published p.155 says Q(y) in the auxiliary sentence of Lemma4.1 and an early proof sentence, although the local form is R. Equation4.2 and the concluding cover sentence explicitly concern R. The intended R-interpretation follows from the local definition and proof, not from an erratum found here.
- Published p.156 ends the tail proof with a sum over d dividing m after explicitly deriving the contribution for each divisor d of q. Summing the displayed contributions over d|q gives a factor sum d^(1-m), bounded by zeta(m-1) when m>=3, and yields the printed4.4 bound. Thus the consumed bound does not require the literal erroneous divisor set.
- Published p.157 briefly writes lambda_n when invoking4.4 in an m=n-1 dimensional lattice. The preceding and following conditions use lambda_m, the largest minimum. The same slip occurs on accepted p.17. The manuscript consumes the dimension-m largest minimum, not a nonexistent extra minimum.

The Cassels reference was renumbered from accepted [6] to final [8]. The cited work remains *An Introduction to the Geometry of Numbers*, and the relevant locators remain TheoremVI p.219, the corollary to TheoremVII p.222, and SectionsI.5/VIII.2. This comparison does not claim a separately performed final-edition Cassels audit.

The publisher/Crossref/author-record search recorded in `REPORT.md` found no linked correction or erratum for these contracts. The fresh Crossref `relation` object is empty. These observations are bounded search evidence, not proof that no correction exists. No claimed final-version change is based on absence of an erratum. The principal evidence is the actual published text now inspected.

The old access report and its manifest remain preserved. They accurately record the earlier failed requests. This report supersedes only their current unresolved-access conclusion. The locally licensed PDF and page images are excluded from any public-release authorization.
