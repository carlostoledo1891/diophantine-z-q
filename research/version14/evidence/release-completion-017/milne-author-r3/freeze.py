from pathlib import Path
import hashlib,json

here=Path(__file__).resolve().parent
root=here.parents[2]
old=here.with_name("milne-author-r2")
def sha(raw):return hashlib.sha256(raw).hexdigest()
def pin(p):
    raw=p.read_bytes()
    return {"path":p.relative_to(root).as_posix(),"sha256":sha(raw),"bytes":len(raw)}
def write(name,data):
    (here/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

parent=pin(old/"MANIFEST.json")
assert parent["sha256"]=="037a180fccf370a828c6ffb614dfae1335018db8c947acc2fcc250eaf48777ed"
for row in json.loads((old/"MANIFEST.json").read_bytes())["files"]:
    assert pin(root/row["path"])==row
assert (here/"PROPOSED-BRAUER.tex").read_bytes()==(old/"PROPOSED-BRAUER.tex").read_bytes()
bindings=json.loads((old/"SOURCE-BINDINGS.json").read_bytes())
for row in [bindings["manuscript"],bindings["book"],bindings["official_addendum"]["pin"]]:
    assert pin(root/row["path"])==row
lines=(root/bindings["manuscript"]["path"]).read_bytes().splitlines(keepends=True)
a,b=3214,3242
bindings["consumers"].append({
    "start_line":a,"end_line":b,"excerpt_sha256":sha(b"".join(lines[a-1:b])),
    "consumer":"Related finite unramified local descent, not literal citation",
    "source":"Compare corrected I.3.8 pp.46–47, addendum pp.2–3, and I.6.3 p.74"})
bindings["official_addendum"]["r3_applicability"]={
    "exercise_2_21":"Two-dimensional local field of characteristic zero with positive-characteristic first residue field. Current ordinary finite extensions of Q_p fall outside that higher-dimensional domain.",
    "i_3_8":"Corrected finite-complete-unramified-extension-first passage supplies the transitive I.6.3 input to the global Sha setting used in I.7.3. Direct finite Kummer duality does not require I.3.8.",
}
bindings["proposed_edit"]["replacement"]=pin(here/"PROPOSED-BRAUER.tex")
write("SOURCE-BINDINGS.json",bindings)
write("MANIFEST.json",{
    "schema":"bounded-source-audit-author-successor/v1",
    "author":"/root/sol_protocol_final_review","parent":parent,
    "status":"Exercise I.2.21 domain and I.3.8 source chain corrected; independent review pending",
    "files":[pin(here/n) for n in ("REPORT.md","PROPOSED-BRAUER.tex","SOURCE-BINDINGS.json","freeze.py")]})
print(pin(here/"MANIFEST.json"))
