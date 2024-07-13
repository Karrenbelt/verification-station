"""
The test_oracle_loader module contains the tests for the oracle_loader module.
"""

from packages.eightballer.customs.oracle_verifier_chronicle import main as oracle_verifier_chronicle
import pytest


ORACLES = [
    oracle_verifier_chronicle
]


@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_collect_data(oracle):
    """
    Test the oracle_loader module.
    """
    assert oracle.collect_data() is not None

@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_verify_data(oracle):
    """
    Test the oracle_loader module.
    """
    assert oracle.verify_data() is not None

@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_challenge_data(oracle):
    """
    Test the oracle_loader module.
    """
    assert oracle.challenge_data() is not None