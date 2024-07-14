"""
The test_oracle_loader module contains the tests for the oracle_loader module.
"""

from packages.eightballer.customs.oracle_verifier_chronicle import main as oracle_verifier_chronicle
from packages.eightballer.customs.oracle_verifier_pyth import main as oracle_verifier_pyth
import pytest


ORACLES = [
    oracle_verifier_pyth,
    oracle_verifier_chronicle
]


@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_collect_data(oracle):
    """
    Test the oracle_loader module.
    """
    assert oracle.collect_data() is not None

@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_verify_data_valid(oracle):
    """
    Test the oracle_loader module.
    """
    logs = oracle.collect_data(6296669, 6296671)
    assert oracle.verify_data(logs) is not None

@pytest.mark.parametrize("oracle", ORACLES)
def test_oracle_loader_challenge_data(oracle):
    """
    Test the oracle_loader module.
    """
    with pytest.raises(Exception):
        oracle.challenge_data('schnorr_data')