import hashlib,json,pathlib
p=pathlib.Path(__file__).resolve().parent
s=json.loads((p/'SELECTION.json').read_text())
root=pathlib.Path(s['source_root'])
def sha(b):return hashlib.sha256(b).hexdigest()
dest='construction/README.md'
if not any(x['destination']==dest for x in s['recommended_distribution']):
 f=root/dest;b=f.read_bytes();s['recommended_distribution'].append({'source':str(f),'destination':dest,'sha256':sha(b),'bytes':len(b),'role':'Historical checker documentation; preserve its dated scope and links, not current V15 status'})
s['total_files']=len(s['recommended_distribution']);s['total_bytes']=sum(x['bytes'] for x in s['recommended_distribution'])
s['source_map_status']='No construction/SOURCE_MAP.json exists in selected source tree. SOURCE_MANIFEST.json preserves original paths and hashes, but is not silently substituted for a manuscript-named SOURCE_MAP.'
for x in s['recommended_distribution']:
 assert sha(pathlib.Path(x['source']).read_bytes())==x['sha256']
assert not s['manifest_mismatches']
(p/'SELECTION.json').write_text(json.dumps(s,indent=2)+'\n')
(p/'INSTRUCTIONS.md').write_text('''# Original huge-polynomial distribution proposal

Copy exactly the source/destination pairs in SELECTION.json into a fresh V15 assembly. This proposal does not copy them or change any repository. It preserves the original ordinary-integer expression and its existing supported reproduction package, distinct from the 233-variable family.

The original expression has 292,890,231,904 rational witnesses and one free rational input t. Its portable SHA256 is 4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6. It is a finite machine specification, not its expanded monomial list. Its own conditional arithmetic status and limitations remain intact.

## Reproduction

Use Python 3.11 or newer and Node.js 22 or newer on PATH. No third-party Python or npm packages are required. From the assembled repository root run:

    python scripts/check_construction.py --report build/construction-checks.json

The unchanged checker verifies every SOURCE_MANIFEST member, works in a temporary directory, regenerates the expression, compares its exact hash, computes syntactic bounds and runs four finite verification suites. It invokes Node with a 2048 MB old-space limit. Keep all manifest members: pruning them would break this supported checker. The smaller thirteen-JavaScript generator closure is recorded separately in SELECTION.json for explanation, not as a replacement for the checked distribution.

The precision-natural-polynomial.json is an exact pinned input boundary. This package reproduces the ordinary-integer expression from that input; it does not regenerate the precision input from earlier machines or prove all arithmetic dependencies. No enormous historical archives are selected.

## Provenance and integration notes

SOURCE_MANIFEST.json records original paths/hashes and the portable release hashes. Historical expression SHA a86790bbf1095d6b1cea9c66067ad8432dd35adc320254eecde21f9f98574714 differs only in three provenance path locations as documented by the existing checker. Do not claim raw historical-byte equality with the portable artifact.

The exact construction/README.md is retained because the checker refers to its scope limitations. It is historical documentation and contains older-version links; it must not be presented as a current V15 completion statement. GI should update current V15 packaging prose after installation/checking rather than rewriting this preserved source document silently.

No construction/SOURCE_MAP.json exists in this selected tree. The manuscript claim naming that companion remains a concrete integration issue: locate an authentic historical map or correct the companion filename/claim through the author. SOURCE_MANIFEST does retain historical references, but this proposal does not invent or rename a map.

Static verification here checked all selected bytes and manifest hashes and traced local CommonJS dependencies. The reproduction command has not been run by this selection task. No new mathematical acceptance, final packaging acceptance, or publication is claimed.
''')
m={'format':'v15-huge-spec-selection-proposal-v1','scope':'Read-only source selection; destination unchanged','selected_files':s['total_files'],'selected_bytes':s['total_bytes'],'files':[]}
for name in ['SELECTION.json','INSTRUCTIONS.md','inspect.py','freeze.py']:
 b=(p/name).read_bytes();m['files'].append({'path':name,'sha256':sha(b),'bytes':len(b)})
b=(json.dumps(m,indent=2)+'\n').encode();(p/'MANIFEST.json').write_bytes(b)
print(json.dumps({'manifest_sha256':sha(b),'selected_files':s['total_files'],'selected_bytes':s['total_bytes']}))
