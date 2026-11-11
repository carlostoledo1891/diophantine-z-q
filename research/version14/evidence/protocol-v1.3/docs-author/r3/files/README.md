# Z is Diophantine in Q

## Version 13

This repository contains *Z is Diophantine in Q*, Version 13, dated November 7, 2026. It gives quartics in **394 total variables** with exact symbolic coefficients and **411 total variables** with every coefficient written out in decimal. The new section proves the reductions from the retained Version 12 construction and records separate mathematical and coefficient-table reviews. The original large construction, earlier quartic proofs and Version 11 Kato index-set and limiting-class repair remain in the manuscript. The Version 9 starting reductions were contributed by Gabriel Conant with ChatGPT.

The project uses the collective agentic notes from Stefan Baranczuk, Jose Brox, Gabe Conant, Sohail Farhangi, James Freitag, Elliot Glazer, Jennifer Park, and Caroline Terry.

| To | Open |
| --- | --- |
| Read Version 13 | [Manuscript PDF](manuscripts/quartic_v13.pdf), [TeX source](manuscripts/quartic_v13.tex) |
| Reproduce the 394/411-variable quartics | [Tables, proof inventory and review scopes](docs/manuscript-revisions/version13/GUIDE.md) |
| Reproduce the 498/514-variable quartics | [Tables, proof inventory and independent reviews](docs/manuscript-revisions/version12/README.md) |
| Reproduce the 523/540-variable quartics | [Tables, source, dependency chain and checks](docs/quartic-523-540/README.md) |
| Read the fully expanded Version 4 quartic | [4,973-variable package](quartics/quartic-4973/README.md), [integer monomial table](quartics/quartic-4973/polynomial.expanded.txt) |
| Follow the current mathematical research review protocol | [Protocol v1.3](docs/research-review/PROTOCOL.md), [contributor guide](docs/research-review/README.md) |
| Inspect the Version 11 repair and repository audit integration | [Version 11 source audit](docs/manuscript-revisions/version11/README.md), [audit integration protocol](docs/audit-history/PROTOCOL.md) |
| Inspect the nine earlier review corrections | [Version 10 response and inventory](docs/manuscript-revisions/version10/README.md) |
| Inspect theorem applications and conventions | [Version 9 extension](docs/quartic-523-540/README.md), [inherited proof inventory](docs/quartic-962/README.md) |
| Build the manuscript or run the checks | [Build instructions](docs/building.md) |
| Download the current audit supplement | [Version 13 supplement and guide](research/version13/README.md), [Version 12 archive](research/version12/README.md) |
| Download the Version 7 research handoffs | [Full handoff](https://github.com/elliotglazer/diophantine-z-q/releases/download/quartic-962-version-7/z-in-q-version7-full-handoff.zip), [current-only handoff](https://github.com/elliotglazer/diophantine-z-q/releases/download/quartic-962-version-7/z-in-q-version7-current-handoff.zip), [contents and verification](handoff/README.md) |
| Read collaborator notes and the height replacement | [Research update](research/2026-11-06-collaborator-notes/README.md) |
| Read the October 11 manuscript | [Manuscript and provenance](October%2011%20Manuscript/README.md) |
| Find earlier manuscripts and research history | [Manuscript archive](manuscripts/README.md), [research guide](docs/research-guide.md) |
| Inspect the partial formalization | [Accepted Lean helpers](lean/README.md) |
| Cite the manuscript or report an issue | [BibTeX](CITATION.bib), [contribution guide](CONTRIBUTING.md) |

Version 9 integrates the odd-product argument, smaller anchor, direct targets and asymmetric formal-depth refinement. The new inventory binds every addition and preserves the existing literature-version qualifications. Version 8 remains in the [manuscript archive](manuscripts/README.md).

Version 7 incorporates four further audits of the Gaussian appendix and their repairs. See the [audit summary](docs/quartic-962/gaussian-audit-20261106.md) for the changes and review limits.

The Version 7 full handoff includes the Version 7 public snapshot, selected research notes, and the unchanged Version 6 full handoff, which preserves the Version 5 and earlier November 4 archives. The current-only handoff omits the embedded historical archive. Neither includes a conversational transcript.

## Polynomial constructions

For each polynomial, the input and all witnesses range over the rationals. The asserted defining property is

$$
q\in\mathbb Z \quad\Longleftrightarrow\quad
\exists\,\mathbf w\in\mathbb Q^{m-1},\quad P(q,\mathbf w)=0.
$$

| Construction | Total variables, including input | Degree | Nonzero monomials | Coefficient magnitude |
| --- | ---: | ---: | ---: | --- |
| Original | 292,890,231,905 | Less than $2\uparrow\uparrow7$ | Not expanded | Less than $2\uparrow\uparrow8$ |
| Version 13, decimal table | 411 | 4 | 6,388 | Less than $2^{3247}$ |
| Version 13, symbolic table | 394 | 4 | 6,338 | Maximum $16\cdot3^{2^{26}}$ |
| Version 12, decimal table | 514 | 4 | 24,716 | Maximum $3^{2048}+1005072314676622<2^{3247}$ |
| Version 12, symbolic table | 498 | 4 | 24,669 | Maximum $16\cdot3^{2^{26}}$ |
| Version 9, decimal table | 540 | 4 | 35,213 | Maximum $3^{2048}+1005072314631333<2^{3247}$ |
| Version 9, symbolic table | 523 | 4 | 35,163 | Maximum $64\cdot3^{2^{27}}$ |
| Version 4 quartic, retained | 4,973 | 4 | 72,925 | Maximum 685,783,949,153,203,534,233,890, less than $2^{80}$ |
| Version 6 quartic | 962 | 4 | 55,409 | Maximum $64\cdot3^{2^{28}}$ |

The [411-variable decimal table](quartics/quartic-411-fully-expanded.txt) contains every coefficient in decimal and occupies 214,957 bytes. The [394-variable table](quartics/quartic-394-symbolic-coefficients.json) uses the fixed integer $C=3^{2^{25}}$, not an extra variable. Both have content one. The ordinary companion adds sixteen constant-chain coordinates and one multiplication coordinate to keep its residuals quadratic. [Version 13 checks and reviews](docs/manuscript-revisions/version13/GUIDE.md) explain the construction and their separate scopes.

The [514-variable table](quartics/quartic-514-fully-expanded.txt) contains every coefficient in decimal and occupies 690,922 bytes. The [498-variable table](quartics/quartic-498-symbolic-coefficients.json) uses the fixed integer $C=3^{2^{25}}$, not an extra variable. [Version 12 checks and reviews](docs/manuscript-revisions/version12/README.md) cover the exact coefficient data and new mathematical transformations separately.

The [540-variable table](quartics/quartic-540-fully-expanded.txt) contains all coefficients in decimal and occupies 708,848 bytes. The [523-variable table](quartics/quartic-523-symbolic-coefficients.json) uses the fixed integer $S=3^{2^{26}}$, not an extra variable. [Reproduction and convention checks](docs/quartic-523-540/README.md) cover both.

The [original construction](construction/README.md) is specified by an expression tree. The [Version 4 monomial table](quartics/quartic-4973/polynomial.expanded.txt) writes every coefficient as an ordinary integer. Its SHA-256 is `094f6a7ed17e7cc8d5d17a2f809127bbaffd0fe343cb2a32d18ac97e61279876`.

The [Version 6 table](quartics/quartic-962/polynomial.json) lists every monomial and specifies its integer coefficient using the fixed constant $S=3^{2^{27}}$. It has 55,401 coefficients independent of $S$, seven linear in $S$, and one equal to $64S^2$. Its SHA-256 is `6b798de7d00ac3c7d725ca0a69d39f1eac1ddb02fee2756cb6323770b952af32`. The large coefficients are not written out digit by digit. Version 9 provides a smaller complete decimal table, while retaining this older proof baseline.

The earlier 962-variable polynomial builds on an independent reconstruction of the public [agentic improvements notes](https://github.com/JoseBrox/diophantine-z-q_improvements), followed by changes of coordinates, smaller arithmetic circuits, and 32 certified eliminations. It is not identified with the unavailable original 1,315-variable table. Its 919 quadratic residuals and their complete sum of squares are included. The manuscript also gives the notes' degree-four lower-bound argument over the rationals. Thus degree four is necessary for a single defining polynomial; the variable and monomial counts are not claimed minimal.

## Verification scope

The finite checks verify the source program, algebraic coordinate changes, projection-preserving eliminations, complete sum-of-squares expansion and coefficient statistics. Independent checks and rejection tests accompany the package. These checks do not prove the source system's arithmetic characterization of the integers.

The manuscript supplies that arithmetic argument. The [Version 13 guide](docs/manuscript-revisions/version13/GUIDE.md) separates the new component and composition reviews, the finite table checks, and the 39-application inventory. These internal reviews retain the inherited arithmetic inputs and source qualifications. The [Version 12 application inventory and reviews](docs/manuscript-revisions/version12/README.md) cover that edition's reductions while retaining the prior arithmetic inputs and their source qualifications. The [Version 9 extension](docs/quartic-523-540/README.md) connects the new arithmetic arguments to the inherited proofs. The [Version 7 inventory](docs/quartic-962/README.md) records exact theorem applications, source versions, hypotheses, conventions and translations. Version 6 proves the needed Gaussian ray-field estimate within the manuscript, following the method of Frei–Tinková without assuming their theorem. The replacement uses Mitsui's published prime-ideal estimate, Green–Tao's one-parameter results, and ordinary-prime transference.

The inventory retains source-version qualifications. In particular, the applications of Dodos–Kanellopoulos and Kollár were checked in the stated author versions of published works; their final typeset statements were not compared. This is not a claim that every cited source's final published text has been inspected.

The [Version 4 inventory](docs/quartic-4973/README.md) and the [earlier 82-record inventory](docs/theorem-application-audit/README.md) retain their own frozen scopes. Structural inventory checks detect stale or mismatched records; they are not proofs of mathematical theorems.

The Lean formalization is incomplete. The accepted snapshot contains 48 helper modules; the main bounded-polynomial declaration still contains `sorry`. AI review and successful finite checks do not constitute independent human peer review or a completed formal proof.

## Earlier work and provenance

The October 11, 2026 manuscript, *A conditional Diophantine definition of Z in Q from four arithmetic inputs*, was produced by Sohail Farhangi with ChatGPT 6. Its PDF is preserved without modification. Its provenance and conditional scope are distinct from the November manuscript.

The November manuscript was produced by Elliot Glazer with Astra 6, Sol 6.1, and Opus 5.5, with auditing from Fable 5.1. The [Version 5 manuscript](manuscripts/archive/quartic_1272.pdf), [Version 4 manuscript](manuscripts/archive/quartic_4973.pdf), [Version 3 manuscript](manuscripts/archive/quartic_9625.pdf) and [Version 2 manuscript](manuscripts/archive/quartic_12504.pdf) remain historical references, with their separate polynomial packages and inventories. Earlier research handoffs identify their own snapshots.

The project builds on OpenAI's October 6, 2026 preprint, [*Hilbert's tenth problem over the rational numbers*](https://github.com/openai/math/blob/main/preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf). The rank-one elliptic-curve and local-divisibility strategy goes back to Thanases Pheidas, as credited in the manuscript. The current construction also credits the collective agentic notes for its formulas and degree obstruction, and Zhi-Wei Sun for the prime-pattern strategy.

The manuscript author field is blank, and [CITATION.bib](CITATION.bib) intentionally omits author fields. See [archival notes](docs/archiving.md) for citation and DOI status, and [third-party notices](THIRD_PARTY_NOTICES.md) for source attribution and redistribution scope.
