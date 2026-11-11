# Source attachment and proposed insertion

Author: v14_sign_conductor. Independent acceptance pending. This successor preserves the former mixed packet and reconciles its source qualification. Carayol was read through the web tool; local PDF pins and renders remain pending.

## Sign input

J. S. Milne, Abelian Varieties, Arithmetic Geometry, Springer, 1986, Chapter V, pp. 103–150, Theorem 8.2. The actual published pages 115–116 were visually read locally. Page 115 defines degree by finite-kernel order or direct-image rank, states multiplicativity, and gives degree n^(2g) for positive multiplication n. Page 116 contains the proof. Negative n follows by the degree-one automorphism [-1]; conjugation preserves the rank of a finite locally free map.

The exact images are in ../h5-sign-normalization-theta-001/local-only/. File milne-pdf-13.png, printed p.115, has SHA-256 3069785d91b2f55096816a74f6208ca995936a67f34a0457ff5741c55a5e6d1a. File milne-pdf-14.png, printed p.116, has SHA-256 053952a3e7084ff0a0be81ab8ca95c9c4a1cf7cd7d54f95d075e98846995220b. These published pages supply the input. The 2022 corrected rendition is not the selected source. Original scan URL: https://wstein.org/edu/Fall2003/252/references/milne-abvar/Milne-Abelian_Varieties.pdf .
The rational clearing-denominator proof in PROOF.md is the new connecting argument. The current manuscript already specifies algebraic coefficient extensions and trivial Galois action on those coefficients. That convention is retained. Root located the consuming passage at lines 1279–1300 of classical-local-tex-integration-root-002/PROPOSED.tex, SHA-256 99d35bfe017ffdea59f134520a05a5ae15ccfa41c9d0004da02bee4f67431cee. This location is root-supplied, not yet independently read by this author.

Proposed insertion replacing the compressed degree assertion:

```tex
Here degree extends to rational quasi-isogenies by
\(D(u)=\deg([m]u)/m^4\), for any positive integer \(m\)
clearing denominators. This is independent of \(m\): comparison
after multiplication by a second denominator uses
\(\deg[n]=n^4\) and multiplicativity. It is multiplicative and
invariant under field conjugation. Writing \(c=r/s\in\mathbf Q^\times\)
with \(s>0\), the equality \([s](cu)=[r]u\) gives
\(D(cu)=c^4D(u)\). Thus
\[
 D(\mu_\sigma)D(\mu_\tau)
 =c(\sigma,\tau)^4D(\mu_{\sigma\tau}),\qquad
 \frac{a_\sigma a_\tau}{a_{\sigma\tau}}
 =\frac1{|c(\sigma,\tau)|}.
\]
The positive fourth-root convention therefore gives
\(\epsilon(\sigma,\tau)=c(\sigma,\tau)/|c(\sigma,\tau)|\).
```

Attach Milne 1986, Theorem 8.2, p.115, to the multiplication-degree input. Finite cochain splitting is a separate subsequent argument.

## CL1 and CL2 conductor provider

Henri Carayol, Formes modulaires et représentations l-adiques, Astérisque 147–148, 1987, pp. 33–47, https://www.numdam.org/item/AST_1987__147-148__33_0.pdf . Section 2.1, p. 36, uses normalized newforms, weight at least two, and an embedding of their coefficient number field. Section 2.4, p. 37, asks whether the Artin conductor exponent equals v_p(N), for p different from ell, also at divisors of N. The next paragraph, p. 38, and the conclusion after Theorem 4 in section 4.1, p. 42, answer affirmatively. This covers general coefficient fields.

The full local theorem is also stated in Carayol, Sur les représentations l-adiques associées aux formes modulaires de Hilbert, Annales scientifiques de l'ENS 19, 1986, pp. 409–468, https://numdam.org/item/10.24033/asens.1512.pdf , sections 0.3–0.7, Theorem A, pp. 409–411. It identifies the local representations at every finite prime away from the coefficient characteristic. For F=Q the even-degree restriction in section 0.3 is inapplicable. Section 0.5 specifies normalization. The theorem retains the Weil–Deligne monodromy; it is not merely semisimplified inertia comparison. Section 0.8's elliptic-curve corollary is not the general coefficient-field supplier.

For each of the beta-family and b-family, use the separately established isomorphism of its actual two-dimensional representation with the representation of its own primitive newform. Fix p and choose ell different from p, using the same coefficient embedding as in that isomorphism. Restriction gives equality of the full local representations. Their inertia-invariant dimensions and Swan terms agree, hence their Artin conductor exponents agree. The 1987 theorem then gives v_p(N_f). This supplies the level comparison independently from C6. It does not prove either family's geometric construction, all-prime compatibility, or any higher-dimensional multiplicity formula. Those remain inputs owned by the arithmetic packets. The auxiliary prime is allowed to depend on p, so p=3 is covered without using a 3-adic conductor formula there.

Proposed concluding sentence for each family-specific all-prime comparison paragraph:

```tex
For each rational prime \(p\), choose an auxiliary prime \(\ell\ne p\).
The preceding isomorphism restricts to an isomorphism of the full
local Galois representations at \(p\), so their Artin conductor
exponents agree. Carayol's conductor theorem for primitive newforms
(\emph{Formes modulaires et repr\'esentations \(\ell\)-adiques},
\S\S2.1, 2.4, 4.1) identifies this exponent with \(v_p(N_f)\).
```

The final manuscript should replace the descriptive citation by its bibliography key and bind this insertion to both exact family-specific sites. No canonical manuscript edit or full-release acceptance is asserted here.

