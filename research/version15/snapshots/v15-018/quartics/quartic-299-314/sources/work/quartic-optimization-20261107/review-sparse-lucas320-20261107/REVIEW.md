# Independent acceptance of the sparse Lucas recentering

I accept the exact affine coordinate change in the reviewed sparse320 packet. It gives mutually inverse maps on the full rational solution sets, fixing the input and every coordinate except249 and250. There is no additional arithmetic premise or exceptional case.

The change saves **61 quartic monomials**, from5,659 to5,598. It saves **no variables**. The count remains320 total variables,319 existential witnesses, and290 quadratic residuals. Degree four, integer content one, and maximum coefficient `16*3^(2^26)` are retained.

Reviewer: `/root/astra_bl_horizontal_repair`, November 7, 2026. Author: `/root/astra_quartic_opt10_combination`. I did not author the change. This review establishes the exact algebraic equivalence relative to its source; it does not re-prove the inherited arithmetic interpretation of the source or accept a later composition automatically. No author artifact, source packet, repository, or controller was modified.

## Exact bindings

The author directory is `work/quartic-under300-20261107/10-combination/sparse-lucas320`, and its source is the adjacent `combined320` directory.

| Artifact | SHA-256 |
|---|---|
| Author `REPORT.md` | `3b8b25f51a2058ba1f31fe2e78b67be7e4337aa59877f8d9423bde1f0da8cf63` |
| Source `combined320/candidate320-ir.json` | `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f` |
| New `candidate320-ir.json` | `2b18e4196a8366bc6cbaa6854b14d74a29997b76857da6f231eb7540cec34a02` |
| New `polynomial320.json` | `5e65508c848abf42c54cf95d25c4949f61dc419f953b5e43d9a78f75e5dac390` |
| This review's `check.py` | `b68ff9340e5784498fe10dd1b957bb46d0a5bd347edc47c8f750e79d4c14b1f0` |
| This review's `CHECKS.json` | `c236dc5215bfd1daa38417b377fd94dcfd21df78fb85bc9058714c21ba7426cf` |

I read the complete report, builder, verifier, and actual old/new equations. The independently written `check.py` imports neither the producer nor another checker. It passed under `C:/Users/glaze/.local/bin/python3.14.exe -B check.py`. It writes only this review's `CHECKS.json` and verifies that all author file hashes remain unchanged.

## Identity, physical normalization, and both maps

Use field pairs over Q(rho), rho^2=2. The actual inputs A,T,Z occupy236/237,240/241,244/245. The source private values C and V occupy249/250 and251/252 and satisfy

    C=A*Z, V=A*T.

The source output equation is

    F+1=T^2+4Z^2-4ZC+2ZV+C^2-CV.

Set S=C-2Z. Substituting C=S+2Z cancels the Z-square terms and the ZV terms exactly, giving

    S=(A-2)*Z,
    F+1=T^2+S^2-SV.

The retained physical output components are v253 and2*v254. My checker independently expands both field equations and matches every component to rows201,202,205,206. It also checks the unchanged V=A*T definition in203,204. In particular, the imaginary output factor two and the minus sign on SV are both preserved.

The forward rational map is

    new249=old249-2*old244,
    new250=old250-2*old245.

Its inverse adds the same fixed Z components. Every other coordinate is fixed. These are unipotent linear transformations over Q. Neither direction divides, chooses a square root, or needs a point to be nonzero. Their compositions are the identity even if any or all relevant field inputs vanish.

The checker substitutes the inverse into every old residual and obtains the corresponding new residual exactly. It substitutes the forward map into every new residual and obtains the old residual exactly. This check includes every unchanged row, not only the displayed four. Thus both maps preserve the entire zero set, and their projection to the distinguished input is identical.

## Complete consumer and coefficient check

The only consumers of249 and250 are precisely201,202,205,206. Exactly those residual objects change. Only the names of coordinate records249 and250 change; all other coordinate records, residuals, and non-status metadata are identical. The output F remains fixed, so every logarithm, detector, scalar, pole, and global consumer receives its original value.

I independently recomputed the primitive-integer residual sum of squares for both source and target. The source has5,659 nonzero terms and the target5,598. Every target coefficient agrees with the supplied table. All320 coordinates occur, every residual is at most quadratic, and the polynomial has exact degree four. A literal C-independent coefficient one remains. All target symbolic coefficient terms have distinct ordinary coordinate monomials, so specialization introduces no collision or hidden cancellation.

All positive-power-of-C coefficients are identical to the source. The C-squared maximum is16, C-linear coefficient multipliers are at most96, and the C-independent coefficients have fewer than2048 bits. Since C=3^(2^25), the exact maximum remains16C^2. This assertion is specific to this packet's source; it is not imported from a later anchor with a different coefficient bound.

No arithmetic or local-domain argument changes. The accepted result is an exact secondary term-count optimization on the pinned320 system. Composition with315 or any other candidate still requires checking the actual combined equations and complete coefficient table. It must not be counted as a variable reduction.
