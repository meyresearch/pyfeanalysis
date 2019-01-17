"""
Unit and regression test for the pyfeanalysis package.
"""

# Import package, test suite, and other packages as needed
import pyfeanalysis
import pytest
import sys

def test_pyfeanalysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "pyfeanalysis" in sys.modules
