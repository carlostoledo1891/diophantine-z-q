"""Record actual local test output and tooling/source-input hashes; no approvals."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

result = subprocess.run([sys.executable, "-B", "-m", "unittest", "-q", "test_assemble_coverage"],
                        cwd=HERE, capture_output=True, text=True)
write("TEST-RESULT.json", {"command": [sys.executable, "-B", "-m", "unittest", "-q", "test_assemble_coverage"],
                           "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
                           "scope": "Synthetic tooling tests, including two assembled dossiers checked by the unmodified designated validator. No production acceptance."})
assert result.returncode == 0, result.stderr
known = ["work/quartic-v14-prep/independent-source-review/PROOF-INVENTORY-REVIEW.json",
         "work/quartic-v14-prep/independent-source-review/whole-initial-with-additional-sources.json",
         "work/protocol-v13-20261107/gate-author/adapter/COVERAGE-V1.3.md",
         "work/protocol-v13-20261107/gate-author/adapter/coverage_gate.py",
         "work/protocol-v13-20261107/gate-author/adapter/offline_manifest_gate.py"]
write("KNOWN-INPUT-PINS.json", [{"path": name, "sha256": sha((ROOT / name).read_bytes())} for name in known])
run_map = json.loads((ROOT / "work/protocol-v13-20261107/v14-run-map.json").read_bytes())
write("CANDIDATE.json", {"schema": "unsigned-tooling-candidate/v1",
                        "author_agent": "/root",
                        "author_run": run_map["/root"],
                        "original_author_agent": "/root/astra_v14_baseline_compiler",
                        "prior_candidate_sha256": "2ff4a1da27604505dd546667ba4473d7deed54f236ffa94a447561c1af619c3a",
                        "role": "Root-authored R3 tooling repair following independent review. No review decisions authored by the helper.",
                        "review_decision": None,
                        "files": [{"path": p.name, "sha256": sha(p.read_bytes()), "bytes": p.stat().st_size}
                                  for p in sorted(HERE.iterdir()) if p.is_file() and p.name != "CANDIDATE.json"]})
print(json.dumps({"candidate_sha256": sha((HERE / "CANDIDATE.json").read_bytes()),
                  "code_sha256": sha((HERE / "assemble_coverage.py").read_bytes()), "tests_exit_code": result.returncode}))
