import sys, json
from pathlib import Path
repo = Path("C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic-v14-release/preview-repository/")
candidate = Path("C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/source-risk-review-20261107/v14-final-main-edit-batch-root-002/quartic_v14.candidate.tex")
sys.path.insert(0, str(repo / "scripts"))
import check_audit_history as history
import check_application_reviews as applications
def read(path):
    return candidate.read_bytes() if path == "manuscripts/quartic_v14.tex" else (repo / path).read_bytes()
record = json.loads(read(history.REGISTER))
history.validate(record, read)
history.self_test(record, read)
applications.check_current(read, True)
print("CANDIDATE PREFLIGHT ONLY: candidate5882 substituted for canonical main; all other files read from installed repository.")
