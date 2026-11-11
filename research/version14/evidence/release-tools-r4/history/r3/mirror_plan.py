"""Build a read-only exact mirror plan and payload from actual Git commits."""
import argparse
import json
from pathlib import Path

from release_common import commit, git, json_bytes, output_dir, pinned, put, safe, sha


def tree(repo, oid):
    result = {}
    for row in git(repo, 'ls-tree', '-rz', '--full-tree', oid).split(b'\0'):
        if row:
            metadata, raw_name = row.split(b'\t', 1)
            mode, kind, blob_id = metadata.decode().split()
            name = raw_name.decode('utf-8')
            safe(name)
            result[name] = (mode, kind, blob_id)
    return result


def plan(public, private, public_base, public_head, private_base, allow):
    commits = [commit(repo, oid) for repo, oid in ((public, public_base), (public, public_head), (private, private_base))]
    if git(public, 'merge-base', public_base, public_head).decode().strip() != public_base:
        raise ValueError('Public head must descend from the reviewed base')
    history = git(public, 'rev-list', '--parents', public_base + '..' + public_head).decode().splitlines()
    if not history or any(len(row.split()) != 2 for row in history):
        raise ValueError('Release history must be a nonempty linear chain without merge commits')
    before, after, mirror = (tree(repo, oid) for repo, oid in zip((public, public, private), commits))
    changed = {name for name in set(before) | set(after) if before.get(name) != after.get(name)}
    if not changed or changed != set(allow):
        raise ValueError('Changed path set differs from the exact reviewed allowlist')
    files = {}
    for name in sorted(changed):
        if name not in after or after[name][:2] != ('100644', 'blob'):
            raise ValueError('Deletion or nonregular release target: ' + name)
        if name in before and before[name][:2] != after[name][:2]:
            raise ValueError('Existing release path changes mode or object type: ' + name)
        if before.get(name) != mirror.get(name):
            raise ValueError('Private preimage differs from public base: ' + name)
        raw = git(public, 'cat-file', 'blob', after[name][2])
        files[name] = pinned(raw, allow[name], name)
    return files


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--public', required=True, type=Path)
    p.add_argument('--private', required=True, type=Path)
    for key in ('public-base', 'public-head', 'private-base', 'allowlist-sha256'):
        p.add_argument('--' + key, required=True)
    p.add_argument('--allowlist', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    allow = json.loads(pinned(args.allowlist.read_bytes(), args.allowlist_sha256, 'reviewed change allowlist'))
    files = plan(args.public, args.private, args.public_base, args.public_head, args.private_base, allow)
    output = output_dir(args.output)
    for name, raw in files.items():
        put(output / 'payload', name, raw)
    put(output, 'MIRROR.json', json_bytes({'public_base': args.public_base, 'public_head': args.public_head,
        'private_base': args.private_base, 'allowlist_sha256': args.allowlist_sha256,
        'files': {name: {'sha256': sha(raw), 'bytes': len(raw)} for name, raw in files.items()},
        'status': 'read-only payload; private worktree/index untouched'}))


if __name__ == '__main__':
    main()
