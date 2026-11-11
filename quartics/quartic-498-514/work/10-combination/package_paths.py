from pathlib import Path
import os
def reference_repo():
    explicit=os.environ.get('QUARTIC_REFERENCE_REPO')
    candidates=[Path(explicit)] if explicit else list(Path(__file__).resolve().parents)
    for root in candidates:
        if (root/'quartics/quartic-523-540/final523_540/verify_elimination.py').is_file():return root
    raise RuntimeError('Supply --repo PATH to the repository containing quartics/quartic-523-540.')
