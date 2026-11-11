# The native genus lattice and its rational index

This note makes explicit the genus lattice used in main3286–3315 and15966–15990. It concerns the genus point only; the separate ring-class lattice is unchanged.

Fix the actual negative odd fundamental partner h* and an admissible positive fundamental D prime to h*. Let K_D=Q(sqrt(Dh*)) and F_D=Q(sqrt D,sqrt h*). The CM reciprocity action, the unaveraged genus-character sum and the same Q-defined parametrization are retained inputs. At a known simple-zero parameter the native free rank is one; the h*-twist has rank zero by the previously supplied forward theorem. These rank assertions are inputs, not consequences of the following lattice calculation.

For D>1, let tau generate Gal(F_D/K_D), and define Gamma_D={P in E(F_D):tau(P)=-P}. Put Lambda_D=Gamma_D/(its torsion subgroup). The genus index is the divisibility index of the class of the actual P_D in this rank-one lattice. Reindexing the unaveraged class-group sum under the reciprocity action proves its exact genus-character transformation law. Hence P_D belongs to Gamma_D as a point, before multiplication by4B or by L.

Choose the standard twist isomorphism iota_D:E^(D)->E over Q(sqrt D), satisfying g(iota_D)=chi_D(g)iota_D. Since chi_D(tau)=-1, iota_D identifies E^(D)(K_D) with Gamma_D. Its rational-point subgroup identifies with the rational D-character subgroup in Gamma_D.

The remaining involution sigma of K_D/Q may be represented by changing sqrt(h*) and fixing sqrt D. The rational character decomposition has D and h* parts, and the latter has rank zero. Thus sigma fixes every free class of E^(D)(K_D). For each Q in that group, Q+sigma(Q) is an actual rational point and has free class2[Q]. Therefore the rational subgroup contains2Lambda_D, so its index in the rank-one Lambda_D is at most2. No equality of the integral lattices or vanishing of torsion is asserted.

If D=1, set F_D=K_D=Q(sqrt h*) and Gamma_1=E(K_D). The genus character is trivial, so the same sum is K_D-rational. Ordinary conjugation fixes the free quotient because the h*-twist has rank zero. The same norm argument proves the index bound; there is no nonexistent nontrivial tau over K_D in this case.

The later fixed multiplier L supplies exact rational D-twist descent and kills the stated torsion uniformly. It is not used to infer this sharper index-at-most2 statement. The integral detector evaluation and the previously fixed factors in O.7 then give the native-index bound with the same C_det. No constant, field of definition, or rank hypothesis is changed.
