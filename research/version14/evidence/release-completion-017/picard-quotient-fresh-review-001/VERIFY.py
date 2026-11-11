from pathlib import Path
import json,hashlib
out=Path(__file__).resolve().parent
root=out.parents[2]
m=json.loads((out/"MANIFEST.json").read_text(encoding="utf-8"))
sha=lambda b:hashlib.sha256(b).hexdigest()
for r in m["bindings"]: assert sha((root/r["path"]).read_bytes())==r["sha256"],r["path"]
for r in m["artifacts"]: assert sha((out/r["path"]).read_bytes())==r["sha256"],r["path"]
parts=[b"".join((root/r["path"]).read_bytes().splitlines(keepends=True)[r["first_line"]-1:r["last_line"]]) for r in m["paragraph_occurrences"]]
assert all(p==parts[0] for p in parts)
assert parts[0]==(out/"PASSAGE.tex").read_bytes()
s=(root/m["bindings"][0]["path"]).read_bytes().splitlines(keepends=True)
assert b"".join(s[2000:2005])==(out/"CONSUMER.tex").read_bytes()
print("PASS: bound files, artifacts, three raw paragraphs, consumer")
