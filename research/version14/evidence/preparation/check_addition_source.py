"""Read-only structural checks and source pins for the frozen author addition."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXPECTED = "6feff3f223c8363847da846706db313e1b7ca0fe2ddd6cbed1307fb944f7d87f"

def pin(relative):
    path = ROOT / relative
    data = path.read_bytes()
    return {"path": relative, "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data)}

addition = pin("work/quartic-v14-prep/addition.tex")
assert addition["sha256"] == EXPECTED
text = (OUT / "addition.tex").read_text(encoding="utf-8")
labels = re.findall(r"\\label\{([^}]+)\}", text)
refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text)
assert len(labels) == len(set(labels))
external = {"subsec:v12-inputs", "sec:v13"}
assert set(refs) <= set(labels) | external
stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
    action, env = match.groups()
    if action == "begin":
        stack.append(env)
    else:
        assert stack and stack.pop() == env, match.group()
assert not stack
depth = 0
for ch in re.sub(r"\\[{}]", "", text):
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        assert depth >= 0
assert depth == 0

paths = [
 "work/quartic-version6-release/repository/manuscripts/quartic_v13.tex",
 "work/quartic-version6-release/repository/docs/manuscript-revisions/version13/addition.tex",
 "work/quartic-optimization-20261107/resume-release-inventory-20261107-r5/PROOF-INTEGRATION-OUTLINE.tex",
 "work/quartic-optimization-20261107/resume-release-inventory-20261107-r6/FROZEN-MANIFEST.json",
 "work/quartic-optimization-20261107/resume-release-inventory-20261107-r6/NEW-PROOF-TEXT.tex",
 "work/quartic-optimization-20261107/resume-release-inventory-20261107-r6/APPLICATION-DELTA.json",
 "work/quartic-optimization-20261107/resume-release-inventory-20261107-r6/RETAINED-SOURCES.json",
 "work/quartic-under300-20261107/10-combination/unweighted372/REPORT.md",
 "work/quartic-under300-20261107/10-combination/report369.md",
 "work/quartic-under300-20261107/01-elimination/s-odd366/REPORT.md",
 "work/quartic-optimization-20261107/resume-elimination-20261107/abscissa359/REPORT.md",
 "work/quartic-optimization-20261107/resume-elimination-20261107/exact319/REPORT.md",
 "work/quartic-optimization-20261107/resume-depth-20261107/shared314/PROOF.md",
 "work/quartic-optimization-20261107/resume-review-shared314-20261107/REVIEW.md",
 "work/quartic-optimization-20261107/resume-depth-20261107/anchor313/PROOF.md",
 "work/quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/REPORT.md",
 "work/quartic-under300-20261107/10-combination/review-anchor-gamma313/REVIEW.md",
 "work/quartic-optimization-20261107/root-reciprocal307/PROOF.md",
 "work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md",
 "work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md",
 "work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md",
 "work/quartic-optimization-20261107/resume-review-reciprocal307-01/REVIEW.md",
 "work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal301/REPORT.md",
 "work/quartic-under300-20261107/10-combination/review-reciprocal301/REVIEW.md",
 "work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/REPORT.md",
 "work/quartic-under300-20261107/10-combination/review-reciprocal299/REVIEW.md",
 "work/quartic-under300-20261107/10-combination/ordinary-reciprocal299/REPORT.md",
 "work/quartic-optimization-20261107/resume-depth-20261107/review-ordinary299/REVIEW.md",
 "work/quartic-v14-prep/quartic-299-314/candidate299-ir.json",
 "work/quartic-v14-prep/quartic-299-314/candidate314-ir.json",
 "work/quartic-v14-prep/quartic-299-314/coordinate-map299.json",
 "work/quartic-v14-prep/quartic-299-314/coordinate-map314.json",
 "work/quartic-v14-prep/quartic-299-314/quartic-299-symbolic-coefficients.txt",
 "work/quartic-v14-prep/quartic-299-314/quartic-314-ordinary-coefficients.txt",
 "work/quartic-v14-prep/quartic-299-314/quartic-314-source-id-coefficients.txt",
]
sources = [pin(p) for p in paths]
result = {
 "status": "Author-frozen TeX; mathematical and assembled acceptance are separate reviews.",
 "addition": addition,
 "lineCount": len(text.splitlines()),
 "checks": {"distinctLabels": True, "referencesBound": True,
            "environmentsBalanced": True, "bracesBalanced": True},
 "compile": {"status": "Not executed by TeX engine",
             "reason": "MiKTeX startup failed before source loading: uninitialized roaming configuration directory."},
 "labels": labels,
 "externalLabels": sorted(external),
 "sources": sources,
}
(OUT / "ADDITION-SOURCES.json").write_text(json.dumps(result, indent=2) + "\n",
                                         encoding="utf-8")
print(json.dumps({"addition": addition, "lines": len(text.splitlines()),
                  "sourcePins": len(sources), "structuralChecks": "pass"}))
