"""Fetch the pinned Lean cache with bounded transient-download retries only."""
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
COMMAND = ['lake', 'exe', 'cache', 'get']
BACKOFF = (2, 4)


def transient_download(output):
    # A compiler/build failure must never be turned into a network retry.
    if re.search(r'(?im)(?:checksum|integrity|hash[ \t]+mismatch|(?:sha1|sha256|sha512)[^\n]*(?:mismatch|invalid|failed)|\.lean:\d+(?::\d+)?:\s*error|build[ \t]+failed|failed[ \t]+to[ \t]+build|compilation[ \t]+failed|unsolved[ \t]+goals|type[ \t]+mismatch|unknown[ \t]+identifier|tactic[^\n]*failed)', output):
        return False
    # Unknown error diagnostics are not classified as safe download retries.
    for line in output.splitlines():
        if re.match(r'(?i)^curl: \(22\) The requested URL returned error: (408|429|500|502|503|504)\b', line):
            continue
        if re.search(r'(?i)(?:^|[ \t])error:', line):
            if not re.search(r'(?i)error:[ \t]*(?:could not download|failed to download|download failed|HTTP[ \t]+(?:Error|response|request))', line):
                return False
    download = re.search(r'(?i)(?:could not download|downloading|download failed|failed to download|curl:)', output)
    status = re.search(r'(?i)(?:HTTP Error\s+|HTTP response:\s*|HTTP request returned an unsuccessful status code:\s*|requested URL returned error:\s*)(408|429|500|502|503|504)\b', output)
    return bool(download and status)


def fetch(run=subprocess.run, sleep=time.sleep, emit=None):
    if emit is None:
        emit = lambda text: print(text, end='', flush=True)
    for attempt in range(len(BACKOFF) + 1):
        result = run(COMMAND, cwd=ROOT / 'lean', stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT, text=True, errors='replace')
        output = result.stdout or ''
        emit(output)
        if result.returncode == 0:
            return 0
        if attempt == len(BACKOFF) or not transient_download(output):
            return result.returncode
        emit('Transient cache-download failure; retrying in %s seconds.\n' % BACKOFF[attempt])
        sleep(BACKOFF[attempt])
    raise AssertionError('unreachable')


if __name__ == '__main__':
    sys.exit(fetch())
