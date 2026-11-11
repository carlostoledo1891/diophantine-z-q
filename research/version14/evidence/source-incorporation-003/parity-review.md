# Published rational Selmer parity substitution

Decision: accepted within the scope below. Reviewer: `/root/astra_v14_source_review`, review run `local:v14:source-first-review:20261107`. Date: 2026-11-08. I did not author this proposal. I reviewed the published statement and its definition, then the actual consumers and proposed contracts. This is a bounded successor review, not a fresh source-blind reconstruction of the manuscript.

The accepted target is `work/source-risk-review-20261107/dokchitser-parity-author/MANIFEST.json`, SHA256 `41320da6feae70129381539a365cbbecf8db45c6c3b9d9988810fde470b1a584`. The author report is `208d85a5b0357785991fa2aeac05f0f70fd1c8a364b41d650dda7a5050dfcf6b`; contract `237d54d03a98595ce7b3b3bdd91ee389a2330560f7b9acd8f3da2b357d70e17d`; assertions `edb8375819b2f36b6456a65ffcec9e8619d32bb17edca67991f75cf6ab2c0756`; proposed use successors `ea50ff68ef0c06c45d6659bce0720393df4e68299970dcd14831ea5166183be5`. The four edits in `EDITS.json`, hash `26490f0aa43d087f3ce7888a474fadaea72903077580f99f0cbe4d691a10d0bb`, take base `80b2fd21c6e33b65d8b4cc1976d5a073ac8f6ffd156ed8e3bbb4e63ce5c75d7c` to candidate `217f6927eb71fa802a8257088e04f4583521eb93d80cdc3fe94688072dd71df5`.

## Published statement and convention

I read the final Annals text, including the definition and Theorem 1.4 on printed page 568, Theorem 4.19 and its proof opening on page 593, and the full dual Selmer convention on page 594. I inspected the rendered statement and proof-opening pages. The local PDF is `local-only/annals2010-final.pdf`, SHA256 `f13acec152f980adbe52b033f6bb20972a0e07ef995affb76c1f0bcbaaaa5306`, 1,578,356 bytes. The [publisher record](https://annals.math.princeton.edu/2010/172-1/p11), independently opened during this review, identifies Dokchitser and Dokchitser, Annals of Mathematics 172 (2010), 567–596, DOI 10.4007/annals.2010.172.567, and distinguishes rational full Selmer parity from the conditional number-field rank result.

Theorem 1.4 covers every elliptic curve over Q and every prime p, including 2. Its rank is the Mordell–Weil rank plus the number of Q_p/Z_p copies in the Tate–Shafarevich group. The adjacent Theorem 1.3 has additional hypotheses; none is imported here. In particular, the selected result does not require finite Sha, semistability, ordinary reduction at 2, or a rational isogeny.

The convention map is justified by the direct-limit Kummer exact sequence

`0 -> E(Q) tensor Q_p/Z_p -> Sel_(p^infinity)(E/Q) -> Sha(E/Q)[p^infinity] -> 0`.

The finite torsion of E(Q) tensors to zero. Its free part contributes the Mordell–Weil rank. The full Selmer group is cofinitely generated over Z_p; taking Pontryagin duals and tensoring with Q_p makes ranks additive. The Sha term contributes exactly its Q_p/Z_p corank. Thus the source rank equals the full Selmer corank, including its divisible Sha contribution. This argument uses the maximal divisible summand in this cofinite setting and does not identify elementwise divisibility with a maximal divisible subgroup for arbitrary groups.

At p=2 and full corank one, the theorem yields root number -1. It still applies in the possible branch with Mordell–Weil rank zero and one divisible Sha copy. It neither removes that branch nor proves analytic rank exactly one.

The proof on page 593 expressly attributes p=2 to Monsky before proceeding with the odd-prime argument. I accept the stated published theorem as this application's external supplier. I have not independently reconstructed Monsky's proof or certified every transitive proof input. The odd-prime proof dependencies are not silently substituted for the p=2 route. The proposal's bounded correction search and the publisher record reveal no correction to this selected interface; absence of a located correction is not a proof of a universal absence of errata.

## Actual consumers and nine comparisons

The first consumer is B37-b, in the restricted-converse discussion at base lines 2045–2069. Its domain at lines 1943–1988 is the fixed rational curve `E_l: y^2=x(x-l)(x+3l)` with positive squarefree l congruent to 11 modulo 12. Its displayed discriminant is `2304*l^6`, so the curve is nonsingular. The RC antecedent is the full Z_2 Selmer corank one assumption. The rational two-isogeny mentioned nearby remains true, but the replacement theorem does not depend on it.

The second consumer is B176-parity at base lines 13911–13923. This is the same fixed E_l over Q, under the same full-corank-one assumption. The sign is determined before the BFH reference choices and the detecting/theta stages. There is no field extension or change to the CM generator curve in this application.

These observations discharge all nine proposed comparisons: the source hypotheses, constructed curve, index domain, Kummer transition, consumed-curve identity, prime and corank conventions, exceptional cases, downstream order, and local conditions. I also accept the two proposed ten-field use assertions. They remove unrelated family and height domains from the old B37-b card while preserving the actual antecedent. This decision does not adopt the historical card's old supplier locator or refresh the entire A022 history.

I checked the related prepared-filter passage at base lines 2605–2615, odd-form passage at 14244–14255, and companion passage at 15698–15715. Their subsequent signs use separate local twist formulas. They do not become new applications of rational Selmer parity over arbitrary number fields. The pole and interpreter proof sources contain no additional literal Dokchitser application requiring this replacement. Their RC, corank, and other arguments remain separately qualified. The summary row is a repetition of the selected rational application.

## Exact edits and limits

My independent checker `check_dokchitser_parity_001.py` verified all 27 manifest files, all 12 source pins, 11 current passage hashes, and the exact four replacements. Its result is `DOKCHITSER-PARITY-CHECKS-001.json`. The resulting candidate has three `ddselmer` citations and one matching bibliography item, no old `dd` citation, and no changes outside the four replacement fragments. The live base still matched 80b2 at the check time recorded there.

The four fragments are accepted for incorporation with the explicit rational A022 successor and current source bindings. If other edits are installed first, combine these fragments against their exact contexts and review the resulting binding; do not overwrite a newer manuscript with this whole candidate. I did not build the candidate PDF or edit the live source.

This resolves the selected current application's dependence on an unavailable final Crelle text by selecting a different, directly inspected published theorem. It does not establish equivalence of the Crelle author and final versions, or reapprove historical number-field/isogeny applications. It does not reapprove the supplied corank, BFH, local twist, modularity, restricted-converse, or full integer-definition arguments. No whole-proof, full transitive-dependency, or release acceptance follows from this decision. Source PDFs and their page images remain local-only.
