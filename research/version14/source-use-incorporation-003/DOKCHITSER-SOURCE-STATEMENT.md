# Final Annals source statement: rational Selmer parity

This is a project-authored paraphrase for source-use indexing, not the published original or a reproduction of it. Independent comparison of this exact record remains required. The installed parity review identifies and accepts the original at the scope below.

Tim Dokchitser and Vladimir Dokchitser, “On the Birch–Swinnerton-Dyer quotient modulo squares”, Annals of Mathematics 172 (2010), 567–596. Final publisher PDF SHA-256: f13acec152f980adbe52b033f6bb20972a0e07ef995affb76c1f0bcbaaaa5306. DOI: https://doi.org/10.4007/annals.2010.172.567.

Theorem 1.4, with the definition preceding Conjecture 1.2 on printed page 568: for every elliptic curve E over Q and every prime p, the parity of the full p-infinity Selmer corank is the global root number, namely (-1)^(rk_p(E/Q)) = w(E/Q). The source's rk_p is the Mordell–Weil rank plus the number of Q_p/Z_p summands in Sha; this equals the full Selmer corank.

No finiteness of Sha, rational isogeny, ordinary reduction or semistability hypothesis is imposed by this rational-base theorem. For the current application set p=2 and use the separately supplied full corank one to obtain w(E_l/Q)=-1.

Project connecting derivation, distinct from the published theorem paraphrase: the direct-limit Kummer sequence is

    0 -> E(Q) tensor Q_p/Z_p -> Sel_(p^infinity)(E/Q) -> Sha(E/Q)[p^infinity] -> 0.

Taking Z_p-coranks gives full Selmer corank = rank E(Q) + t, where the divisible p-primary part of Sha is (Q_p/Z_p)^t. Equivalently, Pontryagin dualize and tensor with Q_p; finite summands contribute zero dimension. Thus this corank is exactly the source rk_p, with no finite-Sha premise. This is the exact argument independently checked in the installed parity review, from the predecessor REPORT.md lines 17–21. Combine it with p=2 and the separate corank-one antecedent to obtain (-1)^1=-1.

The proof at Theorem 4.19, printed page 593, attributes the p=2 case to Monsky. This source-level application does not independently reconstruct that transitive proof. The bounded correction search in the accepted parity report did not locate a correction affecting this statement; it is not a claim that no correction exists.

The source review and current incorporation review are preserved at ../evidence/source-incorporation-003/parity-review.md and ../evidence/source-incorporation-003/combined-review.md. The two manuscript consumers are separately pinned in USES.json. Earlier A022 number-field and two-isogeny records remain historical.
