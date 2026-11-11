"""Isolated overlay tests against the pinned deployed baseline; no deployment."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'protocol-ruleset-20261107'/'deployment-repository'
sys.path[:0]=[str(HERE/'overlay'/'adapter'),str(BASE/'adapter'),str(BASE/'controller'),str(BASE/'publisher'),str(BASE/'immutable-cache')]
names=['test_manifest_gate','test_coverage_gate','test_connections_gate','test_source_transition','test_source_bound_ci','test_runtime_coverage']
suite=unittest.defaultTestLoader.loadTestsFromNames(names)
result=unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(not result.wasSuccessful())
