"""Prepare author records in a NEW staging directory; never edit a repository.

The final contract and all 351 obligations must already be authored. This tool
does not produce a review, approval, current registry or publication decision.
"""
import argparse
import json
from pathlib import Path
import tempfile
import os
import shutil
from inventory_core import (Files, Invalid, PREFIX, canonical, digest, parse,
                            path_ok, require, text, validate)

CONTRACT_KEYS = {
    'source_hypotheses', 'constructed_objects', 'index_domain_coverage',
    'transition_maps', 'limiting_object_identity', 'coefficient_conventions',
    'local_conditions', 'exceptional_cases', 'downstream_consumption'}
HERE = Path(__file__).resolve().parent


def encoded(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False)+'\n').encode('utf-8')


def contract_check(contract, inv, files):
    require(contract['id'] == 'QUARTIC-299-COMPOSITION', 'wrong contract ID')
    require(contract['manuscript'] == inv['manuscript'], 'contract manuscript mismatch')
    authors = contract['authors']
    require(isinstance(authors, list) and authors and len(authors) == len(set(authors)),
            'missing or duplicate authors')
    for author in authors:
        text(author, 'author')
    require(set(contract['obligations']) == CONTRACT_KEYS, 'contract needs nine obligations')
    require(contract['sources'] and contract['evidence'], 'missing contract evidence')
    source_ids = [s['id'] for s in contract['sources']]
    require(len(source_ids) == len(set(source_ids)), 'duplicate source ID')
    for source in contract['sources']:
        for key in ('id', 'url', 'version', 'locator', 'sha256'):
            text(source[key], 'source ' + key)
    for pin in contract['evidence'].values():
        files.pin(pin)
    roles = set()
    for span in contract['manuscript_spans']:
        # Registry format inherits the contract's manuscript pin.
        bound = dict(inv['manuscript'], start_line=span['start_line'],
                     end_line=span['end_line'], sha256_raw_utf8_span=span['sha256'])
        files.span(bound); roles.add(span['role'])
    require({'construction', 'application', 'consumer'} <= roles, 'contract span roles')
    for value in contract['obligations'].values():
        require(value['status'] in ('checked', 'not_applicable'), 'contract obligation status')
        for key in ('required', 'constructed', 'justification'):
            text(value[key], 'contract ' + key)
        require(value['sources'] and set(value['sources']) <= set(source_ids),
                'unknown or missing contract source')
        require(value['evidence'] and set(value['evidence']) <= set(contract['evidence']),
                'unknown or missing contract evidence')
    edits = parse(files.pin(inv['edits']))
    require(isinstance(edits, list), 'edits must be the exact new-edits list')
    expected = {e['id']:digest(canonical(e)) for e in edits
                if e.get('contract_id') == contract['id']}
    require(expected and contract['reviewed_edits'] == expected, 'contract edit binding')
    text(contract['dependency_impact'], 'contract dependency impact')


def prepare(repo, records, contract, schema, extra_files=None):
    """Return checked output bytes. extra_files are explicit author evidence bytes.

    No acceptance or audit-current paths are permitted. The caller supplies the
    read-only assembled repository including the separately prepared artifacts.
    """
    output = {} if extra_files is None else dict(extra_files)
    reserved = {PREFIX+n for n in ('APPLICATIONS.json','validation-schema.json',
                                  'validate-applications.py','quartic-application.json',
                                  'GUIDE.md','inventory-install-manifest.json')}
    for name in output:
        path_ok(name)
        require(name.startswith(PREFIX+'evidence/'), 'extra files must be V14 evidence')
        require(name not in reserved and 'acceptance' not in name.lower(),
                'cannot create approval records')
    output[PREFIX+'APPLICATIONS.json'] = encoded(records)
    output[PREFIX+'validation-schema.json'] = encoded(schema)
    output[PREFIX+'validate-applications.py'] = (HERE/'inventory_core.py').read_bytes()
    output[PREFIX+'quartic-application.json'] = encoded(contract)
    output[PREFIX+'GUIDE.md'] = (HERE/'INSTALLED-GUIDE.md').read_bytes()
    files = Files(repo, output)
    result = validate(records, schema, files)
    contract_check(contract, records, files)
    # Every copied evidence object must be used by the records or the contract.
    unused = set(output) & {n for n in output if n.startswith(PREFIX+'evidence/')} - files.used
    require(not unused, 'unreferenced copied evidence: ' + str(sorted(unused)))
    manifest = {
        'schema':'v14-inventory-install-v1',
        'status':'author_records_pending_independent_review',
        'noAcceptanceCreated':True, 'noCurrentRegistryCreated':True,
        'result':result,
        'files':{name:{'sha256':digest(data),'bytes':len(data)}
                 for name,data in sorted(output.items())},
        'readOnlyDependencies':{
            name:{'sha256':digest(files.read(name)), 'bytes':len(files.read(name))}
            for name in sorted(files.used - set(output))}}
    output[PREFIX+'inventory-install-manifest.json'] = encoded(manifest)
    return output


def write_new(destination, output):
    destination = Path(destination).resolve()
    require(not destination.exists(), 'output must be a NEW directory')
    require(destination.parent.is_dir(), 'output parent must exist')
    tmp = Path(tempfile.mkdtemp(prefix='.inventory-stage-', dir=destination.parent))
    try:
        for name,data in output.items():
            path_ok(name)
            p = tmp/name; p.parent.mkdir(parents=True, exist_ok=True)
            with p.open('xb') as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
        # Windows rename rejects an existing destination. Do not replace one.
        require(not destination.exists(), 'output created concurrently')
        tmp.rename(destination)
    finally:
        if tmp.exists():
            # tmp is freshly created by this invocation inside checked parent.
            require(tmp.parent == destination.parent and tmp.name.startswith('.inventory-stage-'),
                    'unexpected temporary path')
            shutil.rmtree(tmp)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--records', type=Path, required=True)
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--schema', type=Path, default=HERE/'validation-schema.json')
    ap.add_argument('--evidence-plan', type=Path,
                    help='JSON list of {source,target,sha256}; sources relative to plan file')
    ap.add_argument('--output', type=Path, required=True)
    args=ap.parse_args()
    extra={}
    if args.evidence_plan:
        for item in parse(args.evidence_plan.read_bytes()):
            name=path_ok(item['target'])
            require(name not in extra, 'duplicate evidence target')
            source=(args.evidence_plan.parent/path_ok(item['source'])).resolve()
            require(source.is_relative_to(args.evidence_plan.parent.resolve()), 'evidence escape')
            data=source.read_bytes()
            require(digest(data)==item['sha256'], 'evidence pin mismatch')
            extra[name]=data
    output=prepare(args.repo, parse(args.records.read_bytes()),
                   parse(args.contract.read_bytes()), parse(args.schema.read_bytes()), extra)
    require(not args.output.resolve().is_relative_to(args.repo.resolve()),
            'output cannot be inside the read-only repository')
    write_new(args.output, output)
    print(json.dumps({'output':str(args.output.resolve()),'files':len(output),
                      'status':'author_records_pending_independent_review'}))


if __name__=='__main__':
    main()
