"""
The test_oracle_loader module contains the tests for the oracle_loader module.
"""

from packages.eightballer.customs.oracle_verifier_chronicle import main as oracle_verifier_chronicle


ORACLES = [
    oracle_verifier_chronicle
]

import pytest




@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader(oracle):
    """
    Test the oracle_loader module.
    """

    assert oracle.collect_data() is not None


