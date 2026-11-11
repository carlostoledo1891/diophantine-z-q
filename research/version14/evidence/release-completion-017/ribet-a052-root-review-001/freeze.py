from pathlib import Path
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def pin(path):
    raw = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def write_new(name, value):
    path = HERE / name
    if path.exists():
        raise RuntimeError("Refusing to overwrite " + str(path))
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


checks = json.loads((HERE / "CHECKS-003.json").read_text())
assert not checks["failures"] and checks["exact_edit_replay"]
assert checks["current_manuscript_equals_reviewed_base"]
base = ROOT / "work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex"
candidate = ROOT / "work/source-risk-review-20261107/ribet-a052-gaussian-002/candidate-quartic_v14.tex"
assert pin(base)["sha256"] == "fa53dcc19ad2d9efb43aa8e44fcbd514479ea216838dcbb64a4ab39fe12a67fd"
assert pin(candidate)["sha256"] == checks["candidate_sha256"]
target = ROOT / "work/source-risk-review-20261107/ribet-a052-gaussian-003/MANIFEST.json"
assert pin(target)["sha256"] == checks["proposal_manifest_sha256"]
decision = {
    "schema": "bounded-independent-source-application-review/v1.4",
    "reviewer": "/root",
    "authors": ["/root/astra_v14_baseline_gaussian"],
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "accepted_bounded_source_applications_and_exact_candidate",
    "applications": ["A052-RIBET-GEOMETRY", "A052-RIBET-TATE", "A052-RIBET-FROBENIUS", "A052-COARSE-DESCENT"],
    "target": pin(target),
    "base": pin(base),
    "candidate": pin(candidate),
    "report": pin(HERE / "REVIEW.md"),
    "structural_checks": pin(HERE / "CHECKS-003.json"),
    "preserved_adverse_checks": pin(HERE / "CHECKS-002.json"),
    "scope": "Exact published geometric source, module/Tate and Frobenius conventions, coarse-point connection, and four edits; all stated independent CM, good-reduction and arithmetic premises retained.",
    "not_approved": ["Jetchev-Kane final-edition equivalence", "all transitive source proofs", "whole conductor-one proof", "combined004 manuscript", "final PDF", "complete source coverage", "release"],
}
write_new("DECISION.json", decision)
files = sorted(p for p in HERE.iterdir() if p.is_file() and p.name != "MANIFEST.json")
write_new("MANIFEST.json", {"schema": "independent-review-packet/v1", "reviewer": "/root", "files": [pin(p) for p in files], "external_pins": [pin(target), pin(base), pin(candidate)]})
print(json.dumps({name: pin(HERE / name)["sha256"] for name in ["REVIEW.md", "DECISION.json", "MANIFEST.json"]}))
