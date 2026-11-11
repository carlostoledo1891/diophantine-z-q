# The original 156-power sharing proof has a residue gap

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. This corrects the frozen `REPORT.md`, SHA `973c42e11e86abed56a5a732757c5d79cb0251e87df174c152c7b6eeff70000b`. That report remains unchanged as a record, but its assertion that the original guarded construction is arithmetically valid is withdrawn. Its unguarded-product obstruction remains unaffected.

The problem is the P2^2 leaf in G2. This is f(U2)^4 and has valuation in8Z, because f(U2) has even valuation. Replacing its E^157 coefficient by C^-156 E changes its residue to

    -156c-alpha = 4c-alpha modulo8,

where c=v_p(C), alpha=v_p(R). The guard only proves c>23alpha/32. It does not fix the parity of c. For alpha=1,c=2 the residue is7 modulo8, which is the same residue as the unchanged P4^2 E term. The guard term itself has valuation20 and does not exclude this case.

For an explicit valuation tie, take v(f(U2))=78 and v(f(U4))=0. The two terms then both have valuation-1. These values obey the even-valuation facts used in the proof. Therefore the claimed disjoint-class and unique-minimum argument is false as stated. This is a defect in the proof and proposed guard family; it is not asserted to be a full rational witness to a counterexample quartic.

The separate `RECIPROCAL-VARIANT.md`, SHA `e233eaaa7f45f44411731719f8b9412d8f38c448e9a6ca5d7e10a2a7320874c1`, changes this coefficient to C^-160 R^3. Its valuation is-160c+3alpha, hence3alpha modulo8 for every integer c, which is the correct old P2 class. The other replacements in that variant likewise preserve their required classes, and its small-prime and real choices are separately proved there. It must nevertheless receive its own independent review; this erratum is not an acceptance of it.

Agent01 and the independent reviewer were notified before any shared-scale gain or acceptance was claimed. Candidate323 and its accepted predecessors contain no common parameter C of this kind and are unchanged.
