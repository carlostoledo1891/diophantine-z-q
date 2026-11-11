# Dodos–Kanellopoulos source comparison

Reviewer `/root/astra_v14_baseline_gaussian`, 7 November 2026. This is a source-access and application-contract check for V6-GA-DK-INVERSE, required at current manuscript lines 18474–18488 and 18532–18564. It is not a claim to have read the unavailable final typeset theorem.

The published work is Pandelis Dodos and Vassilis Kanellopoulos, *Uniformity norms, their weaker versions, and applications*, Acta Arithmetica 203 (2022), 251–270, DOI [10.4064/aa210728-27-2](https://doi.org/10.4064/aa210728-27-2). The [publisher's article page](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/203/3/114682/uniformity-norms-their-weaker-versions-and-applications) and [issue page](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/203/3) were retrieved. They establish publication, not the theorem's exact final statement.

## Versions actually read

1. The existing `DK-v4.pdf`, SHA-256 `1d71ecfcb7a1970ce3d7a10ac426f8c94e9d1d6a88886cb378ca19a099963508`, is arXiv:1610.00487v4, dated 9 June 2022 according to the retained source record. The existing page-marked extraction at `work/quartic-version5-release/sun-proof/sources/DK-v4.txt` was read at its interval-norm and nilmanifold definitions and Theorem 5.1, pp.12–13.
2. [Dodos's research page](https://sites.google.com/view/pandelis-dodos/research) links a [public author PDF](https://drive.google.com/file/d/1lfI7jZ0cbchW7O3rtMU3F705H99CiMN3/view?usp=sharing). The downloaded file is `DK-author-linked.pdf`, 475,613 bytes, SHA-256 `fcd7bd7835106c5d2e970fcc2ac100a4ca0d3135f790034902dc525d5a39c0b5`. It is a 19-page author manuscript. Its page 1 has no Acta imprint or journal pagination. Rendered pages 12 and 13 contain the theorem and adjacent definitions. The text extraction sometimes converts the displayed weak inequalities to strict ones; visual inspection confirms s at least 2 and C at least 20. No false difference was inferred from that extraction.

## Application match in both available author versions

The theorem quantifies a fixed integer s at least 2, fixed C at least 20, and fixed positive norm threshold delta. It supplies a pseudorandomness tolerance, fixed nilmanifold with smooth metric, fixed Lipschitz bound and positive correlation threshold. N' must be prime between CN and 2CN. The majorant is nonnegative on the entire cyclic group, and its difference from one is small in U^(2s). The real function on [N] must satisfy absolute-value domination and have interval U^s norm at least delta. Its resulting test function is bounded between minus one and one, and the orbit is g^n times a base point.

The manuscript constructs a real function by a fixed positive rescaling of the centered ray-prime weight, truncated below L^(3/5). The ordinary majorant dominates it on the interval. The cyclic majorant is not zero-extended; the interval function is. The cube expansion controls the full cyclic U^(2s) norm, with at most 4^s distinct forms, before applying the theorem. The interval norm is the normalized zero-extension norm in definition (5.4). Removing the initial interval has vanishing norm and correlation cost, so the fixed threshold is reduced by a fixed factor before application.

The nilsequence estimate is uniform in the polynomial orbit and bounded Lipschitz functions at fixed complexity. A linear orbit with arbitrary base point is a polynomial orbit, and the fixed smooth metric can be compared with a fixed Mal'cev metric. Thus the output belongs to the class controlled by the centered nilsequence theorem. The inverse theorem's tolerance and nilmanifold complexity are chosen at a fixed norm threshold. The diagonal over cutoffs and thresholds applies the fixed-modulus nilsequence theorem only after each modulus is fixed.

No hypothesis mismatch or unsupported map was found in this application to either available author version. This decision does not assert that either version is byte-identical or statement-identical to the final typeset paper.

## Retrieval result and remaining obligation

The direct DOI request did not return content through the web tool. The publisher Download link points to `https://www.impan.pl/shop/en/publication/transaction/download/product/114682` and redirected to the institute home page, rather than to a PDF. The article page says PDFs are supplied to licensed institutions. Targeted title/DOI and author-page searches found the public author manuscript above, but no accessible final journal PDF. The source access obstacle is therefore concrete: the final theorem text was not returned by the legitimate primary routes available in this session.

To close the protocol-v1.3 final-version obligation, obtain the final Acta article through licensed access or a legitimate author-hosted final copy, pin its bytes, and compare Theorem 5.1 and the adjacent norm/nilmanifold definitions against the application contract above. An author manuscript's appearance on a publication list is not enough to call it the final typeset version. No payment, login, account change or correspondence was initiated.

The old historical qualification is accurate and remains open for this stronger protocol. It is not a newly discovered mathematical gap. The existing proof and source inventory should retain that qualification until the required final source is actually compared.
