# Independent review of sparse and ordinary shared314 transports

I accept the exact sparse-Lucas transport onto shared314 and the three ordinary-coefficient lifts of that transported system. The maps preserve the complete rational projection onto the original input. There is no new arithmetic assumption, new local choice, or changed completeness order. This acceptance is confined to the frozen artifacts below, relative to the accepted shared314 arithmetic and construction. It is not a publication approval.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. Transport author: `/root/astra_quartic_opt10_combination`. I authored neither transport. I previously reviewed the shared314 arithmetic; the separate construction review was by agent10. No repair to either current transport was supplied in this review.

## Exact scope

The paths in this report are relative to `work`.

| Artifact | SHA-256 |
| --- | --- |
| Shared314 source IR, `quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json` | `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5` |
| Source arithmetic review | `99630a50aac94071d7001d04afd1dcf5fa68209b34bbebff092db926720a5e33` |
| Source construction review | `5e2f0c7091bce7144e7b9659bab52451958ed9d395c9ba7dd8647b7bd3045d82` |
| `quartic-under300-20261107/10-combination/sparse-shared314/REPORT.md` | `1d5657b323e2e7135a0649a87822b519bf95698ef7fcf39435802143e0fc9abe` |
| Sparse manifest | `679b7d134e08bf9fe7e6b8f88b0aef3a37326b504bbadd2e73092c1054cd980b` |
| Sparse314 IR | `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382` |
| Sparse314 polynomial | `1fc9ba1e03e5134bd3173f22d80ecc5c29838996c1cb58839264844f6358d77e` |
| `quartic-under300-20261107/10-combination/ordinary-sparse-shared314/REPORT.md` | `c01b2ab5a0f65572d995eab9f52df92980a73160b8e4f8f69bf149d62ab89283` |
| Ordinary manifest | `3fa9242358c891bbff5f1f38ac70a48c1b55afc0469f75767410fc1ccca5cce2` |
| Ordinary331 IR | `4489f4207f1e212c5a11db0457528dc745710ee68663eb0ddafe9d60ab6a4291` |
| Ordinary330 IR | `eb4d673fcc6a1eee73e832977f634a346dd3bbe1ecf0104d6dab70c0cf739cf4` |
| Ordinary329 IR | `561f483ce198969090d83f3cb797798f5d640ae8db98a6438a177d519962e8b0` |

`SOURCE-PINS.json` records all 54 source and artifact hashes verified by the independent checker, including all ordinary polynomial JSON/text tables. Every entry of both author manifests was checked for byte length and hash. I read the actual transport reports, builders and verifiers, the earlier sparse315 and ordinary-chain review arguments, and the relevant source/current IR rows. Earlier approvals alone were not used to authorize the new compositions.

## Sparse map and exact consumed value

Let the physical field pairs be A=(v236,v237), T=(v240,v241), Z=(v244,v245), C_L=(old249,old250), V=(v251,v252), with rho squared equal to 2. The new private pair is S=C_L-2Z. Thus the forward witness map subtracts twice v244/v245 from old249/old250, and the inverse adds it back. All other coordinates remain fixed. The maps are inverse on all rational assignments, including zeros; neither map divides by a coordinate or selects a sign.

The only consumers of the changed pair in either full IR are rows201,202,205,206. The independent checker substitutes both maps through every row, not only these four, and obtains the other IR exactly. Coordinate records outside249/250 are identical; those two records differ only by name. Other semantic metadata is identical apart from status.

The separately reconstructed field equations are S=(A-2)Z, V=AT, and

    (v253,2v254)=T^2+S^2-SV=F+1.

Rows203/204 for V remain unchanged. The complete output consumer set is205,206,271,272,906,907. Rows271/272 store the square of F+1. Consequently the physical pair

    (v319-2v253+1, 4v320-4v254)

is exactly F squared. I reconstructed rows906/907 as the square of this pair, equated to gamma160 times the shared H4 pair835/836. This confirms the distinction between F and F+1 in the actual current grouping. In particular F(0,0,0)=-1, required by the accepted H bootstrap, is unaltered.

All common-scale powers, the explicit nonzero guard, promoted P1 input, grouping, root/sign-restoration equations, scalar anchor and pole equations are literally unchanged. Every downstream arithmetic input is the same field element as in shared314. Its soundness and completeness therefore transfer by the exact maps, without rerunning or changing the arithmetic argument.

## Ordinary lifts and collision checks

The only C-dependent source rows are504 and1903. Coordinate903 denotes T in the anchor; residual903 is a different object and belongs to the detector. The checker treats these namespaces separately. Detector residuals903/904 are unchanged.

Each lift adds Q in coordinate1000, with Q=48v83^2+48v87^2+432v89^2, and a chain in coordinates1001 onward. These coordinate and row IDs are disjoint from all existing IDs, including gamma1100 through1108 and the promoted input1109/1110. All old coordinate records are identical. Apart from504/1903, all old row objects are identical.

The multiplier-exponent lists are respectively nine513s followed by2 and six zeros; ten1025s followed by2 and four zeros; and2049 followed by eleven2048s and two zeros. Each equation defines its new coordinate linearly as 3^a times the preceding square, starting with a literal constant. The integer recurrence e_next=2e+a ends at33554432 in all three cases. Thus the final chain value is uniquely C=3^(2^25); no zero or sign branch is added.

The checker independently reconstructs the two lifted rows as

    u^2+6v^2-2w^2-4c_last*w-3T^2=0,
    T-2g0*g1-c_last*Q=0.

Substituting the forced Q and the symbolic final C recovers the exact old rows. Given any source solution, the unique chain and Q values extend it to a lifted solution. Conversely, forgetting those values recovers a source solution. These operations are inverse and keep the distinguished input fixed. The C chain does not constrain or substitute for the freely chosen common gamma. No completeness choice or new arithmetic application is involved.

## Full finite check

The reviewer-written `check.py` imports neither builder nor author verifier and executes no author file. It verifies both full sparse substitutions, reconstructs the field equations and all added chain/anchor equations, checks unchanged data, clears rational denominators, divides by each residual's integer content, and expands the complete sum of primitive residual squares. Every coefficient is compared with the frozen polynomial tables. It separately parses every ordinary decimal text monomial/coefficient and compares that full table too. All declared variables occur; every residual is at most quadratic; each resulting polynomial has degree four and content one.

| Candidate | Variables | Residuals | Monomials | Maximum coefficient bits |
| --- | ---: | ---: | ---: | ---: |
| Sparse shared314 | 314 | 283 | 6074 | symbolic C |
| Ordinary331 | 331 | 300 | 6122 | 1627 |
| Ordinary330 | 330 | 299 | 6119 | 3250 |
| Ordinary329 | 329 | 298 | 6116 | 6496 |

The symbolic table has6077 coefficient-power entries. The exact maximum is186624C^2+64 at v89^4. Every other C^2 leading coefficient has strictly smaller absolute value, every C-linear coefficient is at most1728 in absolute value, and every constant coefficient is below2^2048 in absolute value. Since C>2^2051, these bounds both preserve all6074 nonzero monomials after specialization and prove the claimed maximum. A literal specialized coefficient1 proves content one.

The inherited constant coefficient K has1514 bits and matches the supplied complete integer. The ordinary maxima, verified by comparing every actual coefficient, are3^1026+K,3^2050+K,3^4098+K, all at the constant monomial. Their decimal lengths are490,979,1956. Hence331 meets the3247-bit bound,330 does not, and329 meets the8193-bit bound. No expansion of the enormous C is needed.

`CHECKS.json` records the successful run. Reproduce from the workspace root with `python -B work/quartic-optimization-20261107/resume-review-transports314-20261107/check.py`. The recorded run used `C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`. All writes were confined to this review directory, leaving the author files unchanged.

No unresolved defect was found. The exploratory anchor/common-gamma coupling in a separate proposal is not part of this acceptance. The original rejected common-scale argument remains rejected; only the accepted shared314 proof is inherited here. All these candidates remain above the strict below300 publication threshold.
