# Four odd-root reductions composed with the scalar rewrite

The frozen candidate `combined439-ir.json` has SHA256 `403c4126d532fd3403ce0d87a258790d6b78c1a46cf09716aab0df3a7e84c4df`. Its full quartic table, `combined439-polynomial.json`, has SHA256 `f81c2eaa953a508559a846fd82f4954ffc95de3df9966550dd7d6f5a73e6f171`. There are 439 total variables, 438 witnesses, 416 quadratic residuals and 6,568 quartic monomials. Content is one and the maximum coefficient remains exactly 16*3^(2^26).

The source is the independently accepted443 scalar rewrite, SHA256 `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`. Its non-author acceptance is copied to `inputs/scalar443-review.md`. The only new change is the accepted four odd-root reduction from agent02, whose source is the earlier453 system and whose target is copied to `inputs/odd449-ir.json`. The non-author mathematical and implementation review is `inputs/odd-norm-review.md`.

For each root A,S,T,Z, retain the exact h,j,x values and replace the private pair of field witnesses t,r by a field witness a and a rational witness u:

    a^2-2(x+j)a-D=0,
    Norm(a)+u^2=0.

The accepted proof reconstructs a half-point R=(a,at), where t=(a-x-j)/h, and verifies 2R=(x,hj). The inherited squareclass homomorphism and Mordell-Weil decomposition imply that Norm(a) being a negative rational square leaves exactly the classes epsilon and minus epsilon. In the second case replace a by 2(x+j)-a and t by -t. This keeps h,j,x fixed and yields a/epsilon square. Choosing its square root recovers the old private odd witness. The reverse map is existential on these private coordinates; no rational-function bijection is claimed.

This change is independent of the443 scalar elimination and the445 primary reciprocal. Its private coordinate IDs and defining rows are unchanged between the453 source and the443 source. `combine_odd439.py` checks all touched source equations and coordinate names before applying the exact delta. `verify_combination.py 439` independently reconstructs the changes, checks all surviving coordinates and rows, and verifies every coefficient of the full sum of squares. Both passed.

No root sign or point is altered. In particular the scalar S-P chart, its anchor, the common primary reciprocal and the scalar ratio all retain their exact previously accepted values. The only residuals changed are the four private odd-root augmentation blocks. Final non-author transport review is requested. The below400 publication threshold has not been reached; no manuscript or repository was changed.
