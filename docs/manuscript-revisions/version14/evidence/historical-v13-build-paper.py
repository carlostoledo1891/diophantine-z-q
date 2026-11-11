"""Build the manuscript with a pinned Tectonic engine and TeX bundle."""
import argparse
import hashlib
import io
import json
import os
import platform
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.17.0"
BUNDLE = "https://data1b.fullyjustified.net/tlextras-2022.0r0.tar"
BUNDLE_DIGEST = "6ffe055852f8faf66c0acbe1a7fb27f87b869a90bad1204f3bf4d9683f597c7c"
ASSETS = {
    ("Linux", "x86_64"): ("x86_64-unknown-linux-musl.tar.gz", "8533d07f9ccbd7a65824b9e0459041bca34af1eb33daba48f59215593753a3b7"),
    ("Linux", "aarch64"): ("aarch64-unknown-linux-musl.tar.gz", "b10954a95404f3ab2328d2fa59a5ebab8e657f893fab096f98be8db7c0c979b8"),
    ("Windows", "amd64"): ("x86_64-pc-windows-msvc.zip", "f61ce51f0b0ade1015b7de7ef368541c5424e9756ecbd0d7af97d6d48030845f"),
    ("Darwin", "x86_64"): ("x86_64-apple-darwin.tar.gz", "7c90ef5b6ddb1eb1937e4337add5237b79338e4b9676459fa91187d24d6cdf80"),
    ("Darwin", "arm64"): ("aarch64-apple-darwin.tar.gz", "a3f1cac7c5678f01661a92212f58480ae3b0634115d880dbc59e2953ded45667"),
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def install():
    key = (platform.system(), platform.machine().lower())
    if key not in ASSETS:
        raise RuntimeError("Unsupported platform; supply --tectonic with Tectonic " + VERSION)
    suffix, checksum = ASSETS[key]
    name = "tectonic-" + VERSION + "-" + suffix
    directory = ROOT / ".tools" / ("tectonic-" + VERSION)
    directory.mkdir(parents=True, exist_ok=True)
    archive = directory / name
    if not archive.exists():
        url = "https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%40" + VERSION + "/" + name
        request = urllib.request.Request(url, headers={"User-Agent": "diophantine-z-q-paper-build"})
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read()
        if sha(raw) != checksum:
            raise RuntimeError("Tectonic archive checksum mismatch")
        archive.write_bytes(raw)
    raw = archive.read_bytes()
    if sha(raw) != checksum:
        raise RuntimeError("Cached Tectonic archive checksum mismatch")
    executable_name = "tectonic.exe" if key[0] == "Windows" else "tectonic"
    if name.endswith(".zip"):
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            members = [n for n in z.namelist() if Path(n).name == executable_name]
            if len(members) != 1:
                raise RuntimeError("Unexpected Tectonic archive layout")
            executable_bytes = z.read(members[0])
    else:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as z:
            members = [m for m in z.getmembers() if m.isfile() and Path(m.name).name == executable_name]
            if len(members) != 1:
                raise RuntimeError("Unexpected Tectonic archive layout")
            executable_bytes = z.extractfile(members[0]).read()
    executable = directory / executable_name
    executable.write_bytes(executable_bytes)
    executable.chmod(0o755)
    return executable


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tectonic", type=Path, help="Use an installed Tectonic 0.17.0 instead of downloading it")
    parser.add_argument("--cache", type=Path, help="Reuse an existing Tectonic cache")
    parser.add_argument("--bundle", default=BUNDLE, help="Bundle URL; the pinned content fingerprint is still required")
    args = parser.parse_args()
    executable = args.tectonic.resolve() if args.tectonic else install()
    version = subprocess.check_output([str(executable), "--version"], text=True).strip()
    if version != "Tectonic " + VERSION and version != "tectonic " + VERSION:
        raise RuntimeError("Unexpected engine version: " + version)
    source = ROOT / "manuscripts" / "quartic_v13.tex"
    source_bytes = source.read_bytes()
    output = ROOT / "build" / "paper"
    output.mkdir(parents=True, exist_ok=True)
    cache = args.cache.resolve() if args.cache else ROOT / ".cache" / "tectonic"
    env = os.environ.copy()
    env["TECTONIC_CACHE_DIR"] = str(cache)
    env["SOURCE_DATE_EPOCH"] = "1794009600"
    with tempfile.TemporaryDirectory(prefix="paper-", dir=output.parent) as temporary:
        temporary = Path(temporary)
        (temporary / source.name).write_bytes(source_bytes)
        cmd = [str(executable), "--untrusted", "--bundle", args.bundle, "--keep-logs", source.name]
        with (output / "compiler.log").open("wb") as log:
            result = subprocess.run(cmd, cwd=temporary, env=env, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError("Paper build failed; see build/paper/compiler.log")
        log_path = temporary / "quartic_v13.log"
        text = log_path.read_text(errors="replace")
        if any(line.startswith("!") for line in text.splitlines()) or "undefined references" in text or "undefined citations" in text:
            raise RuntimeError("TeX errors or unresolved references; see build/paper/compiler.log")
        # Tectonic escapes ':' and '/' as their decimal character values in this
        # cache key. Check the selected URL, never another cached bundle.
        bundle_key = args.bundle.replace(":", ",58,").replace("/", ",47,")
        bundle_hash_file = cache / "bundles" / "hashes" / bundle_key
        if not bundle_hash_file.is_file() or bundle_hash_file.read_text().strip() != BUNDLE_DIGEST:
            raise RuntimeError("The selected TeX bundle fingerprint does not match the pin")
        pdf = (temporary / "quartic_v13.pdf").read_bytes()
        if not pdf.startswith(b"%PDF-"):
            raise RuntimeError("Compiler did not produce a PDF")
        (output / "quartic_v13.pdf").write_bytes(pdf)
        shutil.copyfile(log_path, output / "quartic_v13.log")
    if source.read_bytes() != source_bytes:
        raise RuntimeError("Manuscript changed during build")
    receipt = {"engine": version, "bundle_url": args.bundle, "bundle_fingerprint": BUNDLE_DIGEST,
               "manuscript_version": 13, "pdf": "quartic_v13.pdf",
               "source_sha256": sha(source_bytes), "pdf_sha256": sha(pdf), "pdf_bytes": len(pdf),
               "tex_errors": 0, "unresolved_references": False,
               "original_pdf_replaced": False, "byte_identity_to_uploaded_pdf_claimed": False}
    (output / "build-report.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
