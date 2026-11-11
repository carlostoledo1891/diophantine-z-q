# Sparse224 presentation with198 residuals

This is a presentation of independently accepted shared-T-redundancy224-006 (manifest22cc77834fe30b475bcea750c38f424fe659929d1739fe86ad97a02abf8c6016; reviewe900dfce4c87908e6bd7f02533b219b77798730c98d18a54a4406cba7ccc55b2). It introduces no arithmetic or domain change.

Reuse the ordered sparse226 stages from shared-alternate-sparse226-002/MAPS.json, remapped through shared-T-elimination224-004/MAPS.json. Remove the substitution for deleted g component126 from its mixed constant-shift stage; no surviving expression in that stage references either deletedg component. All other coordinate and row operations are transported unchanged, with primitive row normalization recomputed. MAPS.json explicitly lists each actual stage and its inverse. build.py checks both affine compositions and reverses every row operation, recovering the exact198 raw224 residuals.

The fixed input coordinate1 and A_N parameter metadata are unchanged. The resulting unweighted sum of198 squares has224 variables,degree4,content1,2290 coordinate monomials and2291 parameter terms. All variables occur. Height is exactly A_N²+1 for N>=53; the inherited defining threshold remains ineffective. No manuscript adoption is implied.
