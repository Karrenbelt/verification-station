
import os
from typing import cast
from pathlib import Path

from aea.skills.base import Behaviour
# we use web3 to make some calls to the Ethereum node.
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://https://rpc.ankr.com/eth_sepolia")


def collect_data() -> None:
    """
    Collect data from the oracle verifier chronicle.
    """


def verify_data() -> None:
    """
    Verify data from the oracle verifier chronicle.
    """
    raise NotImplementedError("This function is not implemented yet.")

def challenge_data() -> None:
    """
    Challenge data from the oracle verifier chronicle.
    """

    raise NotImplementedError("This function is not implemented yet.")