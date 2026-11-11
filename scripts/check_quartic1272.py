"""Run the portable 1272-variable reconstruction and exact coefficient checks."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / 'quartics/quartic-1272/reproduce.py'

if __name__ == '__main__':
    raise SystemExit(subprocess.call([sys.executable, str(ENTRY), *sys.argv[1:]]))
