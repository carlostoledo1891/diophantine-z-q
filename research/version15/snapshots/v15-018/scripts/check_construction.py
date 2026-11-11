"""Rebuild the curated polynomial and run its bounded computational checks."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


def sha(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Optional JSON result file")
    parser.add_argument("--historical-polynomial", type=Path,
                        help="Optional original ordinary-integer-definition.json from the handoff")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "construction"
    manifest = json.loads((source / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    for row in manifest["files"]:
        path = source / row["file"]
        if path.parent != source or sha(path) != row["release_sha256"]:
            raise RuntimeError("Source hash mismatch: " + row["file"])
    historical_checked = False
    if args.historical_polynomial:
        if sha(args.historical_polynomial) != manifest["original_polynomial_sha256"]:
            raise RuntimeError("Historical polynomial hash does not match the recorded source")
        historical = json.loads(args.historical_polynomial.read_text(encoding="utf-8"))
        historical["recipes"]["precision"]["sourceFile"] = "precision-natural-polynomial.json"
        historical["recipes"]["power_value"]["sourceFile"] = "precision-natural-polynomial.json#templates/0"
        historical["sourceHashes"] = {"precision-natural-polynomial.json": manifest["precision_sha256"]}
        portable = json.loads((source / "ordinary-integer-definition.json").read_text(encoding="utf-8"))
        if historical != portable:
            raise RuntimeError("Polynomial changed beyond the documented provenance fields")
        historical_checked = True
        del historical, portable
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required")
    version = subprocess.check_output([node, "--version"], text=True).strip()
    if int(version.lstrip("v").split(".")[0]) < 22:
        raise RuntimeError("Use Node.js 22 or later")
    records = []
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="zinq-construction-") as temporary:
        work = Path(temporary)
        for row in manifest["files"]:
            shutil.copyfile(source / row["file"], work / row["file"])

        def run(name, command):
            begin = time.monotonic()
            result = subprocess.run(command, cwd=work, capture_output=True, text=True,
                                    encoding="utf-8", timeout=600)
            if result.returncode:
                raise RuntimeError(name + " failed:\n" + result.stdout + result.stderr)
            parsed = json.loads(result.stdout)
            if parsed.get("passed", parsed.get("valid", True)) is not True:
                raise RuntimeError(name + " did not report success")
            record = {"check": name, "seconds": round(time.monotonic()-begin, 3),
                      "result": parsed}
            records.append(record)
            print(name + ": passed", flush=True)

        run("regenerate-polynomial", [node, "--max-old-space-size=2048",
            "ordinary-integer-polynomial.js", "precision-natural-polynomial.json",
            manifest["precision_sha256"], "regenerated-polynomial.json"])
        if sha(work / "regenerated-polynomial.json") != manifest["polynomial_sha256"]:
            raise RuntimeError("Regenerated polynomial differs from saved polynomial")
        run("syntactic-size-bounds", [sys.executable, "-B", "bound-ordinary-integer-polynomial.py"])
        expected = json.loads((source / "ordinary-integer-polynomial-size-bounds.json").read_text())
        actual = json.loads((work / "ordinary-integer-polynomial-size-bounds.json").read_text())
        if actual != expected:
            raise RuntimeError("Regenerated size bounds differ from saved bounds")
        for filename in ["verify-integer-compiler.js", "verify-division-polynomials.js",
                         "verify-finite-polynomial-expressions.js", "verify-six-contact.js"]:
            run(filename, [node, "--max-old-space-size=2048", filename])
    report = {
        "passed": True, "node": version, "python": sys.version.split()[0],
        "seconds": round(time.monotonic()-started, 3),
        "source_files_verified": len(manifest["files"]),
        "historical_provenance_normalization_checked": historical_checked,
        "polynomial_sha256": manifest["polynomial_sha256"],
        "arithmetic_theorem_proved": False,
        "scope": "Exact regeneration, structural audit, syntactic bounds, and finite arithmetic cases. See construction/README.md for exclusions.",
        "checks": records,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "checks"}, indent=2))


if __name__ == "__main__":
    main()
