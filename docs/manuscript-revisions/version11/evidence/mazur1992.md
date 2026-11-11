# Mazur 1992 primary-source check

Checked 7 November 2026 for the smaller source follow-up in GitHub Issue 2. This is a source verification only. No shared manuscript, release inventory, or GitHub comment was changed.

## Source acquired and inspected

Barry Mazur, *The topology of rational points*, Experimental Mathematics 1 (1992), no. 1, 35–45. DOI: [10.1080/10586458.1992.10504244](https://doi.org/10.1080/10586458.1992.10504244).

The original 11-page publisher PDF was downloaded using the visible DOWNLOAD PDF link on the [Project Euclid article](https://projecteuclid.org/euclid.em/1048709114), through normal Chrome access. The link was `https://projecteuclid.org/journalArticle/Download?urlId=em%2F1048709114`. Direct web-tool and curl requests had returned an Incapsula HTML response; those responses were not mistaken for the paper. The successful PDF is saved as `mazur1992.pdf`.

SHA256: `e2122ef31461dce5ac2f47ebf183f19670262f6c9d858997c59542f847d20162`.

PDF pages 1–3, corresponding to printed pages 35–37, were rendered to `page-01.png`, `page-02.png`, and `page-03.png` and read visually. The exact conventions and page references below were checked from those images. `mazur1992.txt` is a secondary extraction; font warnings make the rendered pages the authoritative local reading record.

## Exact locations and conventions

| Item | Printed page | Checked content |
| --- | --- | --- |
| Meaning of variety | 35, right column, immediately before Conjecture 1 | Reduced scheme of finite type over a field, usually Q. Irreducibility and projectivity are not part of this convention. |
| Conjecture 1 | 35, right column | For smooth V/Q with V(Q) Zariski dense, its closure in V(R), in the ordinary real topology, is a finite union of connected components of V(R). |
| Conjecture 2 | 36, left column, bottom | For any variety over Q, the closure of its rational points in its real locus is homeomorphic to a finite complex with a finite subcomplex removed. The preceding discussion identifies the complexes through real triangulations. |
| Finite homotopy type | 36, bottom left, continuing at top right | Mazur states this as a consequence in the paragraph following Conjecture 2. It is not a second clause inside the italicized 1992 conjecture statement. |
| Conjecture 3 | 36, right column, top | The closure of the rational points of any Q-variety has finitely many connected components. There is no smoothness, Zariski-density, irreducibility, or properness hypothesis here. |
| Diophantine setup | 36, right column | A rational polynomial whose rational solvability in auxiliary variables characterizes integer values of its distinguished rational variable. |
| Projection argument | 37, left column, first two paragraphs | Form the affine hypersurface, project to the distinguished coordinate, and use its integer image to obtain infinitely many connected components in the real closure. The argument begins with the final paragraph of page 36. |

The distinction between Conjecture 1 and Conjectures 2–3 matters. The manuscript's reduced affine hypersurface can be singular and reducible, and falls directly under Conjectures 2 and 3.

## Conjecture 2 implies Conjecture 3

The implication in the current TeX is valid and is explicitly stated in the original 1992 paper. One can verify it without any algebraic-geometric hypothesis: a finite simplicial complex minus a subcomplex is the union of the relative interiors of the finitely many simplices not removed. Each such relative interior is connected, so this union has only finitely many connected components. Alternatively, the finite homotopy-type consequence stated by Mazur gives the same result, since a homotopy equivalence induces a bijection on connected components.

There is a small presentational difference between the two cited papers. In the 1992 paper the finite homotopy-type assertion follows the displayed Conjecture 2 in prose. In the 1995 update, page 165, it appears as a clause of the displayed Conjecture 2. The current manuscript's attribution to the 1995 formulation is therefore accurate; it should not describe that entire wording as a literal quotation of the 1992 conjecture.

## Projection check against the current manuscript

Compared file: `work/github-issue-review-20261107/quartic_v10-current.tex`.

Compared file SHA256: `9559b22cc581346da1b3150fa9b8dfb62cfb048f6aac0b866448ae7ae879ff38`.

The introductory attribution at lines 111–115 and the corollary/proof at lines 6649–6680 agree with the original source. The proof correctly takes the reduced affine hypersurface. If C is its real closure and pi is the coordinate projection, continuity gives C contained in pi^{-1}(Z), because Z is closed in R. Every integer is already represented by a rational point, so pi(C)=Z. Each connected component of C maps to a connected subset of the discrete set Z, hence to a singleton. Thus there are infinitely many components. No assertion that arbitrary continuous maps commute with closure is needed.

The bibliography at lines 20032–20035 has the correct author, title, journal, volume, year, page range, and DOI. Adding issue number 1 and direct original-page citations would improve the pin but is not a correction to the mathematics or bibliographic identity.

## Inventory disposition

The version-10 source record honestly stated that the 1992 scan had not then been obtained and that the 1995 update supplied the substantive reading. That is historical evidence and should remain dated as such. This follow-up supersedes the current access status with an actual original-source check; it does not retroactively change the earlier review.

Current records requiring an additive or replacement status entry are `sources.json` for `mazur1992`; the A047 descriptions in `inventory.json` and `site-review.json`; the source-review caveat in the version-10 README; and the `V10-MAZUR-CONJECTURE2` source description if the integration elects to cite the original directly. Proposed text is provided separately in `INVENTORY_REPLACEMENT.md` and `primary-pin.json`.

No mathematical repair to the Mazur corollary was identified. The requested follow-up closes the original-source-access limitation and supplies the precise 1992 page and convention pins.
