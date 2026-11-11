# Local sources for the actual beta conductor bound

## Serre source
Serre, Local Class Field Theory, Cassels–Frohlich, Algebraic Number Theory(1967), ChapterVI, §§4.1–4.3, printed155–159, supplies lower ramification groups, the Herbrand upper numbering and its quotient compatibility, units under local reciprocity, last upper break versus abelian conductor, and the Artin conductor sum. The precise subgroup psi formula and derivative-product bound are local derivations, not separately quoted statements of this chapter. This is not the1979 Local Fields book.

## Serre connection
For the actual Galois F=L_v/Q_p, pass from any auxiliary degree-a extension to its normal closure of degree<=a!. The derivative product of an Eisenstein uniformizer polynomial gives d=sum(|G_i|-1)<=e-1+e*v_p(e). Changing variables by the Herbrand derivative yields d/e=1-1/e+integral(1-1/|G^u|)du, hence last positive break<=4a². The quotient rule and H_t=H intersectG_t yield phi_H=psi_Q composedphi_G and G_Qp^u intersectG_F=G_F^(psi(u)), with psi(u)>=u. These exact derivations are in retained A012REPORT64–92 and current betaPROOF35–39. For the actual rank2 representation, finite wild image and triviality beyondU0 give Swan<=2U0 and invariant codimension<=2, irrespective of possible infinite tame unipotent monodromy.

## Torsion source
Silverberg–Zarhin, Semistable reduction and torsion subgroups of abelian varieties, Annales de l Institut Fourier45(1995),403–420, Theorem3.5 printed406: n>=3 prime to the residue characteristic and n-torsion defined over an unramified extension imply semistable reduction. Theorem3.3 printed405 supplies the semistable inertia criterion, hence unipotent inertia on the ell-adic Tate module for ell unequal to the residue characteristic. The printed inequality is >=3, not the extraction artifact >3.

## Torsion connection
For the same A/F take n=3 unlessp=3, thenn=5. Over F(A[n]) alln-torsion is rational, so the identity extension meets the unramified hypothesis. Degree overQ_p is<=D*G0 because A[n] hasrank4 and G0=|GL4(F5)| dominates|GL4(F3)|. Semistability persists to the normal closure. A stable ell-adic lattice makes the pro-p wild image finite (the congruence kernel is pro-ell); finite unipotent subgroups in characteristic0 are trivial. Together with the separate Serre break calculation this gives the geometric Tate triviality aboveU0=4(DG0)². No good reduction conclusion is inferred from this semistability theorem.

## Local norm source and corrected locator
Milne, Class Field Theory, author course notesv4.03,6August2020, ChapterIII Lemma3.2 printed107 gives the local Artin norm/inclusion diagram for a tower M/F/K with M/K finite Galois. The first diagram says rec_K(N_F/K(x)) is the image of rec_F(x) inGal(M/K)^ab. Its proof is marked To be added; the preceding Theorem3.1 and its Res/Cor compatibility are the stated cohomological basis. This is an author-notes source, not a peer-reviewed publication. ChapterV Proposition3.3 printed157 is a global ideal diagram and is not the literal local-unit supplier; preserve that old locator as history rather than equating it with the local statement.

## Local norm connection
Take K=Q_2, F=L_v and M the compositum of F with the finite cyclic character field of localchi. Since F/K is Galois, M/K is finite Galois; compose the first local diagram withchi to obtain chi|G_F(rec_F(x))=chi(rec_K(N_F/K(x))). Norms of units are units. The actual non-2 factors ofchi are unramified and its factor modulo4 has order<=2 onQ_2-units, so beta²=chi gives beta^4=1 onO_F^*. For e=v_F(2), logarithm/exponential on depthe+1 and multiplicationby4 give (U^(e+1))^4=U^(3e+1). Thus beta is trivial on that latter group. The unit/upper-group rule then gives last relative upperbreak<=3e and the separate subgroup formula transfers it to the absolute bound. No [Lprime:Q] factor enters this argument.

## Preserved scope
All three inputs concern the original beta surface, F=L_v and its original scalar cochain. The actual K,L degree and ramification bounds, beta²=chi, the restricted-character identity, all-prime Tate realization and Carayol level equality remain separate incoming constructions. This packet does not assert their recursive closure.
