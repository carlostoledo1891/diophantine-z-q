from pathlib import Path
from runpy import run_path
import re

OUT=Path(__file__).resolve().parent
OLD=OUT.with_name("combined005-forward-hodge-author-sol-003")
EXPECTED="4b6d68cd68e0702339f31604ac7efc09a10a9dc55040ed65429a075d59fdcecf"
m=run_path(str(OLD/"prepare.py"))
read,sha,pin,ROOT=(m[k] for k in ("read","sha","pin","ROOT"))
canonical=m["canonical"]

def write(name,obj):
    import json
    with (OUT/f"{name}.json").open("x",encoding="utf-8") as f:
        json.dump(obj,f,indent=2,ensure_ascii=False)
        f.write("\n")

def prepare():
    assert list(OUT.iterdir())==[Path(__file__).resolve()]
    assert sha((OLD/"MANIFEST.json").read_bytes())==EXPECTED
    manifest=read(OLD/"MANIFEST.json")
    for row in manifest["files"]:
        assert pin(ROOT/row["path"])==row
    apps=read(OLD/"APPLICATIONS.json")
    conns=read(OLD/"CONNECTIONS.json")
    uses=read(OLD/"USES.json")
    field=next(a for a in apps if a["id"]=="CURRENT-MILNE-CAV-HODGE")["obligations"]["downstream_consumption"]
    deltas=[]
    for name,pattern,replacement in [
        ("required",r"883\s*[-–]+\s*886","combined005 lines 1427–1430 (ed992 predecessor lines 883–886)"),
        ("constructed",r"887\s*[-–]+\s*896","combined005 lines 1431–1440 (ed992 predecessor lines 887–896)")
    ]:
        old=field[name]
        new,n=re.subn(pattern,replacement,old)
        assert n==1,(name,old)
        field[name]=new
        deltas.append(dict(application="CURRENT-MILNE-CAV-HODGE",obligation="downstream_consumption",
                           field=name,before=old,after=new))
    uid="FR-PICARD-DIVISOR"
    c=next(c for c in conns if c["use_id"]==uid)
    u=next(u for u in uses if u["id"]==uid)
    old="Pushforward of divisors preserves degree and principal divisor classes under the stated finite curve morphism, and the elliptic identity identifies its degree-zero Picard variety with the elliptic curve."
    new=u["supplier"]["statement"]
    assert "divisor-class group" in new and c["available_assertion"]["statement"]==new
    for key in ("required_capabilities","available_capabilities"):
        assert c[key].count(old)==1
        before=list(c[key])
        c[key]=[new if s==old else s for s in c[key]]
        deltas.append(dict(use_id=uid,field=key,before=before,after=c[key]))
    assert c["use_sha256"]==canonical(u)
    assert set(c["required_capabilities"])<=set(c["available_capabilities"])|set(c["derived_capabilities"])
    for row in manifest["files"]:
        rel=(ROOT/row["path"]).relative_to(OLD)
        if rel.as_posix() in ("prepare.py","APPLICATIONS.json","CONNECTIONS.json"):
            continue
        path=OUT/rel
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("xb") as f:
            f.write((OLD/rel).read_bytes())
    write("APPLICATIONS",apps)
    write("CONNECTIONS",conns)
    write("FINAL-PROJECTION-DELTA",dict(predecessor_sha256=EXPECTED,changes=deltas,
        scope="Two inherited line references and exact propagation of the narrowed source statement into its capabilities. No new mathematical assertion or manuscript change."))
    write("MANIFEST",dict(status=manifest["status"],target_sha256=manifest["target_sha256"],
        predecessor_sha256=EXPECTED,counts=manifest["counts"],
        files=[pin(p) for p in sorted(OUT.rglob("*")) if p.is_file()]))
    print(pin(OUT/"MANIFEST.json"))

if __name__=="__main__":
    prepare()

