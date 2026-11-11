"""Regression for a source executable becoming an ordinary release file."""
from pathlib import Path
import subprocess
import tempfile
import unittest

from mirror_plan import plan
from release_common import sha


class MirrorModeTests(unittest.TestCase):
    def test_existing_mode_change_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)

            def git(*args):
                return subprocess.check_output(
                    ['git', '-C', str(repo), *args], stderr=subprocess.STDOUT
                ).decode().strip()

            git('init')
            git('config', 'user.name', 'Synthetic release test')
            git('config', 'user.email', 'release-test@example.invalid')
            git('config', 'core.autocrlf', 'false')
            git('config', 'core.filemode', 'false')
            (repo / 'entry.txt').write_bytes(b'fixed content\n')
            git('add', 'entry.txt')
            git('update-index', '--chmod=+x', 'entry.txt')
            git('commit', '-m', 'Synthetic executable baseline')
            base = git('rev-parse', 'HEAD')
            git('update-index', '--chmod=-x', 'entry.txt')
            git('commit', '-m', 'Synthetic mode change')
            head = git('rev-parse', 'HEAD')
            with self.assertRaisesRegex(ValueError, 'changes mode or object type'):
                plan(repo, repo, base, head, base,
                     {'entry.txt': sha(b'fixed content\n')})


if __name__ == '__main__':
    unittest.main()
