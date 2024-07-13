
import os
from typing import cast
from pathlib import Path

from aea.skills.base import Behaviour
# we use web3 to make some calls to the Ethereum node.
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://https://rpc.ankr.com/eth_sepolia"))


def collect_data(web3=w3, address='0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603' ) -> None:
    """
    Collect data from the oracle verifier chronicle.
    """
    # get the contract ABI
    contract_abi = Path("packages/eightballer/customs/oracle_verifier_chronicle/abi.json").read_text()
    contract_address = address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    # get the data from the contract
    data = contract.functions.get_data().call()
    return data


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