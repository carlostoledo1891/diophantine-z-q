## A012: accept after replacing the uninspected book citation

The file called serre-local-cft.pdf is not Local Fields. I visually read its Chapter VI title page and pp.155-161. It contains J.-P. Serre, Local Class Field Theory, in Cassels and Frohlich, Algebraic Number Theory, Chapter VI, pp.128-161, followed by Tate's Chapter VII. Relevant exact locators are Section 4.1, pp.155-157, including Theorem 1; Section 4.2, Proposition 1, p.157; and Section 4.3, pp.158-159. The first defines the Herbrand function and states upper-numbering compatibility with quotients, including the inverse-limit extension. Theorem 1 identifies the images of unit groups under reciprocity with upper ramification groups. Proposition 1 identifies abelian conductor with last upper break plus one. Section 4.3 defines the Artin conductor through the lower ramification groups. These supply the actual external interfaces needed here. The uninspected 1979 book need not remain the cited source.

Here is a full check of the bound, including the two formulas not spelled out in that chapter. Pass from an extension of degree at most a to its normal closure, whose degree is at most a!, using the faithful action on its a embeddings. Write M/Q_p for this closure, e for its ramification index, M_0 for its maximal unramified subfield, and pi for a uniformizer. The extension M/M_0 is totally ramified, generated integrally by pi, whose polynomial f is Eisenstein of degree e. The derivative terms i b_i pi^(i-1), including e pi^(e-1), have pairwise distinct valuations modulo e. Hence the term of least valuation cannot cancel, and

    d := v_M(f'(pi)) <= e-1+e v_p(e).

For each nonidentity inertia element sigma, f'(pi)=product_sigma(pi-sigma(pi)). Its valuation equals the sum of v_M(pi-sigma(pi)). By the lower-group definition on p.155, counting those integers yields

    d = sum_(i>=0) (|G_i|-1).

Thus this equality follows directly from the derivative product, without requiring a separately cited different formula. If desired, d is the usual different exponent. With the source's Herbrand derivative du/dt=|G_t|/e, the change to upper numbering gives

    d/e = 1-1/e + integral_(u>0) (1-1/|G^u|) du.

Until the last positive break b, the nontrivial group G^u has order at least two. Therefore b<=2d/e<=2(1+log_2(a!))<=4a^2. The unramified and tame cases have no positive break and satisfy the same bound. At a=1 this is immediate; for integral a>=2 use log_2(a!)<=a log_2(a)<=a^2. The manuscript's looser 4a^2 bound is valid.

For completeness the exact subgroup indexing follows from the quoted quotient theorem. In a finite Galois tower M/F/K, write G=Gal(M/K), H=Gal(M/F), Q=G/H, and use H_t=H intersect G_t from the lower definition. The quotient theorem gives |Q^u|=|G^u|/|H intersect G^u| and |Q_0|=|G_0|/|H_0|. Differentiating psi_Q(phi_G(t)) gives |H_t|/|H_0|, exactly phi_H'(t), and both functions vanish at zero. Thus phi_H=psi_Q composed with phi_G and

    H intersect G^u = H^(psi_Q(u)).

Passing to finite Galois quotients gives the absolute formula. Here F=L_v is itself Galois over Q_p because L/Q is Galois. For the auxiliary torsion field, use its normal closure as above. No unsupported non-Galois Herbrand notation is needed. Since psi_Q' >=1, psi_Q(u)>=u for u>=0.

The semistable torsion extension has degree at most DG_0 by the separately checked torsion and Raynaud inputs. Its wild inertia is trivial on V_l(A), l different from p: semistable inertia is unipotent and a continuous pro-p group has trivial image in the resulting pro-l unipotent subgroup. Thus every absolute upper group beyond U_0=4(DG_0)^2 acts trivially on the geometric Tate representation and lies in G_L.

At odd p, beta squared is tame, so beta on wild inertia has order dividing two; the pro-p condition makes it trivial. At p=2 the local norm-reciprocity identity and the stated conductor-four character give beta^4=1 on O_F^*. For e=v_F(2), logarithm and exponential converge and are inverse on U_F^(e+1) and p_F^(e+1): all nonlinear terms have strictly larger valuations there. Multiplication by four carries p_F^(e+1) onto p_F^(3e+1), hence fourth powers carry U_F^(e+1) onto U_F^(3e+1). Beta is trivial on the latter. Serre Section 4.1 Theorem 1 and Section 4.2 Proposition 1 give relative upper break at most 3e. The subgroup formula then gives triviality on absolute groups u>max(4D^2,3e), bounded by U_0. The argument consumes the existing construction of beta and its norm compatibility, without asserting a new independent closure of A068.

Finally the Artin conductor is dim(V)-dim(V^I)+Swan(V). The first term is at most two. The Swan integral is integral_(u>0) codim(V^(G^u)) du, obtained from Section 4.3's sum by the same change of variables. It is at most 2U_0. This formula uses only the finite wild image; possible infinite tame unipotent monodromy does not enter that integral. Thus 2+2U_0<=E_0, as claimed, with no factor [L':Q].

Recommendation: close A012 when the citation and bibliography are replaced as in PATCH.diff and the direct derivative argument in this report is retained as evidence. This does not claim to have read Local Fields. Source: work/independent-height-review-20261104/conductor/primary/serre-local-cft.pdf, SHA256 e0367b25a022eb27ec220e3c15b474a94fb96d70a6bb89b77f4a02c2231950fe. Chapter VI title and page numbering were visually verified; the file also contains Chapter VII and should be catalogued as an extract rather than as the entire book.

