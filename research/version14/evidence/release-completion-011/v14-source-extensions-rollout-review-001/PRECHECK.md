# Independent rollout precheck

Current runtime preparation003 pins controller commit268cc244786568f4a63a02ca1108ad81c2763937. The workflow requires the approved-SHA variable to equal the current main workflow SHA and checks out that same approved SHA. Local installation is not remote activation.

The first draft pin-refresh helper needed exact predecessor pin validation, ancestry/worktree checks and regenerated successor manifest. These were reported before freeze; final acceptance is pending corrected frozen files and tests. The two live context modules also require accepted coverage-gate and connections-gate dependency hashes without removing their verification.

The beta quantitative proof is not in original92 but is in added10 at hash1507355c. The proposed one-sentence correction must not rewrite a frozen supplemental reconstruction; use explicit fresh reconstruction/freeze or a separate successor path.
