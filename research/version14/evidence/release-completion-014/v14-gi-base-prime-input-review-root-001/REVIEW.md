# Independent Bertrand application review

Reviewer: /root. Reviewed at 2026-11-09T08:29:00.185Z. Decision: accepted for ACTIVE-GI-EXT-BASE-BERTRAND only.

I independently extracted and read the original 1932 published PDF, printed pages 194, 197 and 198, then read the actual BASE source lines 210–263. Page 197 section 5 states the interval theorem for every integer n>1. Page 198 supplies the finite prime-chain step; the source does not leave small positive lengths to an asymptotic exception. Its Latin-letter convention on page 194 is natural numbers.

The application first fixes an integer C>16 and takes a positive integer N. Thus m=CN is an integer greater than 1, and the theorem supplies CN<P<2CN. If an intermediate source bound is written P<=2m, the endpoint is excluded because 2m is composite for m>1. Consequently 1/(2C)<N/P<1/C uniformly in every positive N. This matches BASE233–239 and its explicit all-positive-N assertion at257–258. C is fixed before N; no prime in an arithmetic progression, limiting exchange, or omitted small-N case is needed.

This review accepts prime existence and the stated endpoint/parameter transfer. It does not independently accept the Gowers norm comparison, the forward bracket theorem, the polynomial model, or the full inverse theorem; those retain their own source and review obligations. The proposed source declaration is a project paraphrase of the published result, not the primary source itself.

The author manifest is 7ef17d0da61712abe1285016c3869468d2be1b83bb16f3866c09ab75b507df5f. CHECKS.json records exact member and source-location checks, the primary PDF identity and the use digest. Their success is binding evidence, not the mathematical argument.
