# Independent normalizer-degree connection review

Reviewer: `/root/astra_v14_baseline_compiler`, 2026-11-08. Author: `/root`.

I accept the bounded normalizer calculation in NORMALIZER-CONNECTION.md `4ef53848d2cd7f602d5eb1bf5889c1b97e9a54f5f04ed80766b806b06224758e`, bound by NORMALIZER-MANIFEST.json `1b52fe5eaed198786a7ef33c46f9752171962e2143f49afd4ee596a7b3e2ca94`. Acceptance is conditional on its explicitly retained geometric inputs. It neither proves nor upgrades A001, the identification of the normalizer quotient with P1_j, or the generic-fiber identification after forgetting the auxiliary marking.

I read the complete proof and current ed992 manuscript passages before the author's normalizer manifest and verification record. I did not author the proof or supply an incorporated repair. I previously independently reviewed the separate local-order connection; that receipt remains unchanged and supplies only its stated scope. Its primary-source reading included final Voight203,205–207 and the corrections described there. The present proof uses those same local-order and valuation facts; this review checks the new normalizer and degree deductions.

## Local and global normalizers

For a split local algebra, g normalizing End(L) makes gL stable under all matrix units. The diagonal projections express gL as I1 e1 plus I2 e2. Both off-diagonal units imply the two inclusions I1 subset I2 and I2 subset I1. A fractional ideal of Z_p is p^r Z_p, so gL=p^r L and p^(-r)g belongs to GL(L). The converse follows directly. This proves the precise local normalizer and keeps the actual completed maximal order from the prior connection.

For a division local algebra every conjugate of the maximal order is the same unique maximal order. The quotient by its units is measured by w=v_p(nrd)/2. Its values form (1/2)Z, since the displayed quaternion uniformizer has square a central uniformizer. Central elements have integer values. The quotient by the center and units is therefore exactly Z/2, including p=2. No rescaling error or split-algebra application is used.

The only division primes are2 and3, as retained in A001. Their two parities are independent: a local quaternion uniformizer at either prime and identities elsewhere is a finite adelic element. In the kernel, the local scalar factors are units almost everywhere, so they assemble to a finite idele; the remaining factors assemble to K0. Thus N/(A_f^* K0) has order4. This is a restricted-product argument, not an assumption of global rational strong approximation. Conjugation preserves the central ideal3 Ohat, so it preserves K3.

## Central ideles and the full curve

For a central finite idele a, the finite set of nonzero valuations defines a rational scalar r cancelling every valuation. Changing only its sign makes (ra)_3 reduce to1 in F3^*. All other components are already central units; hence ra belongs to K3. In the retained full adelic double quotient, this rational scalar may be absorbed on the left and acts identically on the symmetric domain. Scalars have positive reduced norm r^2 even when r is negative. The remaining ra is absorbed on the level side. Thus every central finite idele acts trivially on this same full curve. No component has been selected or assumed invariant under all of N.

## Index, degree, and the auxiliary marking

The map N/(A_f^* K3) -> N/(A_f^* K0) is surjective. Its kernel is a quotient of K0/K3, giving order at most 4[K0:K3]. The definition of K3 embeds K0/K3 into (O/3O)^*, so surjectivity of reduction is unnecessary. The rank-four order has 3^4 elements modulo3; using all81 rather than its unit count is a valid upper bound. Therefore the acting group has order at most324.

With the separately retained geometric normalizer-quotient identification, a geometric generic fiber is a single orbit and has at most that many points. The finite curve map is generically separable in characteristic zero. This bounds its total degree, also when all components are retained. Ineffective group elements could only decrease the bound.

The application to X35/G5 is conditional on the separate sixth-phase assertion identifying its generic fiber and j-map with this Y3 and its j-map. Under that exact identification the bound is unchanged. The degree of the temporary full-five cover is not multiplied into it. This review does not use freeness alone as a proof of the quotient or its generic-fiber identity.

## Verification and limits

The independent checker binds the author manifest, proof, previous connection/review, current source, and three exact current source passages. It checks raw excerpt hashes, uniqueness and recorded text. The normalizer span includes the closing display line760; the broader consumer span792–797 preserves the quotient and descent context. No live file was changed.

No new defect was found. Retained premises are the fixed quaternion algebra/order and positive principal polarization; the actual full adelic curve, right action and P1_j quotient; and the generic full-three identity with the same j-map. The proof of those inputs, the remaining quotient/descent constructions, genus, reduction, discriminant, height, whole B11 assembly and release status are outside this decision.
