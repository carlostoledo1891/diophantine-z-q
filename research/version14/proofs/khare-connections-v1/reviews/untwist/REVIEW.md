# Arbitrary-weight cyclotomic untwist: independent bounded review

Target: residual-cyclotomic-twist-author-001, manifest 9b5a46dba82e3e672c444f14f749556391e18f8771216c8beb21440303f5cc24, proof 310c2b412c56e57af4b4a9e95f89a629b929fd94de9bd6ea85d5bd629b6fb27b. The seven application cards and seven internal connections are accepted in their stated scopes, relative to the named published inputs. No mathematical repair was requested after the freeze.

## Independence and source-first domain

Root proposed a Gauss-translate strategy; Arithmetic authored the proof. I did not author this arbitrary-weight construction. I previously supplied weight-two BG05 source suggestions and authored its high-level interface, and I have read related character and Hecke calculations. That exposure is disclosed. I do not extend Shimura's weight-two paragraph or use my old BG05 argument as independent authority for arbitrary weight. Here I read the new complete proof, all seven cards and connections, final Li's actual pages 285, 287 and 294, and final Ghate–Vatsal pages 2143–2144. I also read the actual normalization18 proof before comparing the new records. The earlier O5 source representation of the Serre trace inputs was my work; its existing independent source decision is retained, and the new application to this fixed pair of representations is checked here.

The opening draft's arbitrary exponent wording was noted before freeze. The author had independently already submitted the clarification that e=0 modulo P−1 is the identity case. The final proof separates that case before the nontrivial Gauss construction. This is not a new reviewer-authored proof segment or an extension of the actual caller domain.

The exact consumer is normalization18 proof fc43c584c820286d69248f6544bf27352b70d2731c016338e01b9120124d8f49. It needs modularity of r from modularity of r tensor omega^e, only in a nonordinary branch whose lower weight is already in the preceding modularity range. It does not need optimal residual level or weight, an ordinary characteristic-zero lift, or a compatible system from this particular input.

## Construction and selected sources

The fixed complex and P-adic embeddings distinguish the algebraic character from its realizations. The unique prime-to-P roots of unity lifting a^(-e) define eta; for nonzero e modulo P−1 it is a nontrivial character of conductor P. Its Galois realization is explicitly defined by the action on P-th roots of unity. Arithmetic Frobenius therefore has value eta(ell), with reduction omega^(-e); no inverse reciprocity convention is hidden. The trivial exponent case requires no translation.

The finite Fourier calculation proves the Gauss scalar is nonzero without claiming it is a P-adic unit. The normalized first coefficient of f makes the translated F nonzero. The displayed conjugation matrix is integral even if P divides N, because NP^2 divides its lower-left input. Its lower-right entry has the required residue modulo N. Reindexing the character weights gives epsilon eta^2 for every weight w in the source slash convention. At each rational cusp the rational translate factors through an integral cusp representative and an upper triangular positive-determinant map. The zero constant term and positive rescaling give cuspidality and holomorphy. These arguments establish the actual arbitrary-weight cusp form, not merely its formal Fourier series.

Li's printed page 285 defines the weight-k slash and lower-right-entry nebentype convention for fixed positive integer k. Printed page 287 explicitly gives the Hecke Fourier expansion for an arbitrary form in C_epsilon(M,N); with the second level parameter one it is exactly the operator used here. Thus the eigenform calculation does not assume that F is already new or an eigenvector. For ell outside NP the eta^2 diamond term gives the required eta(ell) eigenvalue. The terms with P dividing n vanish; the nonintegral n/ell term is zero by the source convention.

Li's printed page 294 provides the invariant old/new spaces, simultaneous eigenforms, nonzero first coefficient for a newform, and primitive extraction from an old common eigenform. Applying these to the nonzero F preserves w and the inflated character at good primes. A nonzero new projection is already a common eigenvector; an old projection has a primitive source at divisor level. No uniqueness theorem or least-conductor assertion is required.

The final Ghate–Vatsal statement on 2143 and the first paragraph of 2144 gives the chosen-prime attachment and its good trace/determinant for a normalized cusp eigenform of every integral weight at least two. The ordinary condition begins only afterward. Neither that condition, equation (1.1), the splitting theorem nor its Wiles/Mazur–Wiles proof inputs is consumed. I additionally visually checked printed page 2153 solely to confirm the paper's convention: it denotes the P-adic cyclotomic character by nu and identifies the classical determinant as chi nu^(k−1). Together with the good-prime formula this matches the arithmetic-Frobenius convention selected here. No Hida-family result from that page is added as an existence input.

## Representation and lattice check

Both representations are placed in one finite P-adic coefficient field. Their good traces agree because eta_G(Frob_ell)=eta(ell), and their good determinants also match epsilon eta^2 ell^(w−1). The proof needs only the trace identity for Chebotarev and the standalone characteristic-zero trace algebra lemma. The selected Serre density/trace input is the reviewed I.2.2 and standalone I.2.3 statement, not the surrounding Q-rational compatible-system theorem.

Residual absolute irreducibility of the actual T_f implies absolute irreducibility in characteristic zero. A hypothetical invariant line after finite scalar extension meets the extended lattice in a saturated rank-one module, whose reduction would be a proper invariant line. Brauer–Nesbitt first identifies semisimplifications; since one is absolutely irreducible and two-dimensional, the other has composition length one. Thus the proof gets an actual representation isomorphism. The intertwiner and all coefficients lie in a finite extension; no infinite coefficient field is needed for lattice transport.

Twisting the given lattice by the unit-valued finite character and transporting it through that isomorphism produces an actual stable lattice in rho_H. Its reduction is r tensor omega^e tensor omega^(-e), hence the original r over the extended residue field. If the original modularity assertion used semisimplification, the irreducible residual module already has length one, so that convention introduces no hidden extension. The Gauss scalar is never used to assert integrality of this lattice.

## Seven scoped decisions

| Card | Accepted connection and boundary |
| --- | --- |
| TW-TRANSLATE | Actual nonzero arbitrary-weight cusp form at NP^2 with epsilon eta^2; no U_P or primitive conclusion yet. |
| TW-HECKE | Good-prime common eigenpacket from the arbitrary-form formula, including the diamond factor and zero coefficient cases. |
| TW-PRIMITIVE | A primitive form of the same weight and some divisor level with the same good packet; no optimal residual level or weight. |
| TW-ATTACHMENT | Final general-weight attachment before the source's ordinary hypothesis; no ramified local compatibility or splitting assertion. |
| TW-TRACE-ISOMORPHISM | Density and the characteristic-zero algebra lemma, plus actual absolute irreducibility, give an isomorphism after finite scalar extension. |
| TW-LATTICE-UNTWIST | The specified stable lattice reduces to the original r, not only an unspecified equality of residual trace functions. |
| TW-NORMALIZATION18 | Applies only when the nonordinary lower-weight twist has already been proved modular. The ordinary/endpoint branches and their lift constructions remain separate. |

All thirteen finite rows match normalization18. The eight possible uses are (P,k)=(11,10), (19,14),(19,16),(19,18), and (29,22),(29,24),(29,26),(29,28). The five endpoint rows have no twist use. In the general domain, odd B and even k>=B+2 imply k>=B+3; hence w=P+3−k<=P−B<B, while k<=P−1 gives w>=4. Also e=w−2 is nonzero even and at most P−7. This is a symbolic domain check, not an inference from a finite numerical test. Existence of P and the prior modularity range remain incoming hypotheses.

## Verification and limits

Independent checks passed all 13 manifest members, 14 exact input pins, ten raw source/consumer spans, seven application and seven connection identities, and the thirteen finite rows. The actual selected Li/Ghate–Vatsal page images were read; their complete papers and every proof ancestor were not re-proved. The source originals/renders remain local-only.

This decision supplies the stated global untwist under its explicit published inputs and residual modularity premise. It does not approve optimal-level/weight refinements, the ordinary lift, prime selection, all FIRST/RETURN constructions, the full Serre theorem, current ordinary-inventory adoption, manuscript edits, or release. No author, historic packet or live source was modified.
