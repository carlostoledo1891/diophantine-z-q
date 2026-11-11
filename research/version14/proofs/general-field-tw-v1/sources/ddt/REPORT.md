# Published DDT general Selmer-size formula

Author: /root/astra_quartic_opt05_anchor. This is an authored source-to-consumer connection for independent review, not an independent decision on its own assertions or on the complete Taylor-Wiles construction.

## Exact published source

Darmon, Diamond and Taylor, *Fermat's Last Theorem*, Current Developments in Mathematics 1995, no. 1, pp. 1-154, DOI 10.4310/CDM.1995.v1995.n1.a1. The International Press archive supplies the complete 154-page scanned article. The local file has SHA256 2b45bf258d078924f008ff178a49d78e033c83541af5f9c95fa1aeab215e235d. Its PDF page numbers and printed page numbers agree. Publisher Crossref metadata and the inspected page images are pinned in SOURCE-PINS.json.

I read the title page and the relevant definitions, statements and proof on printed pp. 54-57 directly in the rendered scan. The required result is **Theorem 2.19 on p. 57**. It explicitly quantifies over a number field F and a discrete G_F-module M of finite cardinality. Local conditions are subgroups of ordinary continuous H^1(F_v,M), unramified at almost all places. The dual conditions are their cup-product annihilators in H^1(F_v,M^D), where M^D=Hom_Z(M,mu_n) and nM=0. Both Selmer groups are finite and

    |H^1_L(F,M)| / |H^1_Lperp(F,M^D)|
      = |H^0(F,M)| / |H^0(F,M^D)|
        * product_v (|L_v| / |H^0(F_v,M)|).

The theorem imposes no odd-primary restriction and no assumption that F is unramified at 2. The odd-prime hypothesis beginning Section 2.4 below the theorem belongs to that later section. It does not restrict Theorem 2.19.

## Real places and the proof's convention

The definitions on pp. 54-55 give the contragredient action on the cyclotomic dual. The Q-case proof of Theorem 2.18 on p. 56 displays the real-place norm correction (1+c)M in the middle degree-zero term of the Poitou-Tate sequence. Its combination with the Euler characteristic gives the **ordinary H^0** groups in the final formula. The text then extends the argument to number fields and states Theorem 2.19 explicitly.

There is a convention that must not be suppressed when using these pages. A perfect degree-zero local pairing at a real place requires Tate H^0, not ordinary H^0. Thus the literal ordinary-H^0 reading of the all-place degree-zero clause of Theorem 2.17(c) is not an additional input here. The norm correction displayed in the proof of 2.18 makes the needed convention visible. Ordinary H^1 agrees with Tate H^1 and has the required perfect pairing, including for 2-primary modules at real places. The final Selmer ratio has ordinary H^0 after the Euler correction. In particular, neither H^1(R,M)=0 nor replacement of the final denominator by Tate H^0 is allowed.

The proof cites Milne I.4.10, I.4.15 and I.5.1 for duality, finiteness and Euler characteristic. These remain published mathematical inputs; reading their invocation is not a new audit of their complete proofs. The explicit general-field theorem, rather than an extrapolation from the Q-case alone, is the supplier adopted in this proposal.

## Connection to the frozen general-field construction

CONSUMERS.json binds the exact theta001 proof, SHA256 02adafa304e6b4f733c99330268bab678ab1376468f03ecc3443b9e6638b6d8e, and the raw bytes of Sections 1, 5 and 6. Only their finite Selmer-size input is under review here. Changes to the separate group-theoretic or prime-selection argument require their own successor and decision.

The proposed substitutions are M=End_k(k^2), M=k, and M=Z/2^j, with k a finite field of characteristic 2. All are finite continuous additive modules. The local condition is zero at S, full at Q, and unramified elsewhere. S contains every place above 2, every infinite place, and all module ramification; Q is disjoint from S. These are exactly admissible local conditions for Theorem 2.19. Their H^1 annihilators are full at S and zero at Q.

For the full matrix module, the pairing

    (X,Y) -> Tr_(k/F_2)(tr(XY))

is invariant under simultaneous conjugation and nondegenerate. To see nondegeneracy, a nonzero matrix entry of X is detected by a matrix unit Y, and its coefficient can be scaled so the finite-field trace is nonzero. Thus the cyclotomic additive dual agrees with the required twisted linear dual. This uses the full matrix algebra, not the trace-zero subspace, whose scalar behavior in characteristic 2 is different. The mod-2 cyclotomic character is trivial. For the constant cyclic module the dual is mu_(2^j), and that twist is retained.

At a real place in S the numerator local condition has order one and the denominator is |H^0(F_v,M)|. At a complex place ordinary H^1 is zero. No dyadic local Euler formula is needed to specialize the zero local condition itself. The auxiliary places' separate local counts, global invariant counts, Kummer classes and class-field arguments remain the responsibility of the construction's own proof and review.

For the k-vector-space instances, taking logarithms to base |k| translates the cardinality identity into dimensions. For Z/2^j it remains a cardinality identity. There is no limit to infinite coefficient modules in this connection.

## Version comparison and remaining qualifications

The current author-hosted article is dated September 9, 2007. Its Theorem 2.19 on p. 62 has the same needed statement and formula as the final 1995 scan. This is a comparison of that theorem, not an assertion that every line of the two articles agrees. The May 24, 2000 university-hosted version cited in theta001 was not authenticated as the final publication; it is unnecessary for the proposed final-source substitution. No claim is made about equality with the 1997 reprint.

NSW electronic version 2.3, Theorem 8.7.9, provides corroboration with the same real-place distinction. Its equality with a particular printed edition remains unverified and is not needed for this DDT source connection.

This packet does not resolve the original-1980-versus-IAS-retypeset qualification for Langlands *Base Change for GL(2)*. It does not approve the complete general-field auxiliary-prime construction, H, Serre modularity, or the manuscript. The next gate is independent review of this exact source connection.
