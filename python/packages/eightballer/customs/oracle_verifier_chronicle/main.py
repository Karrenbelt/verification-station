
import json
import os
from typing import cast
from pathlib import Path

from aea.skills.base import Behaviour
# we use web3 to make some calls to the Ethereum node.
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth_sepolia"))

# 
if Path("vendor").exists():
    ABI_PATH = Path("vendor/eightballer/contracts/chronicle_price_feed/build/chronicle_price_feed.json")
else:
    ABI_PATH = Path("packages/eightballer/contracts/chronicle_price_feed/build/chronicle_price_feed.json")

def collect_logs(since_block_number='latest', to_block_number='latest', web3=w3, address='0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603') -> None:
    """
    Collect data from the oracle verifier chronicle.
    """
    contract_abi = Path(ABI_PATH).read_text()
    contract_address = address
    contract = web3.eth.contract(address=contract_address, abi=json.loads(contract_abi)['abi'])
    logs = contract.events.OpPoked().get_logs(fromBlock=since_block_number, toBlock=to_block_number)
    return logs

def collect_data(since_block_number='latest', to_block_number='latest', web3=w3, address='0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603') -> None:
    """
    Collect data from the oracle verifier chronicle.
    """
    contract_abi = Path(ABI_PATH).read_text()
    contract_address = address
    contract = web3.eth.contract(address=contract_address, abi=json.loads(contract_abi)['abi'])
    answer = contract.functions.latestAnswer().call()
    decimals = contract.functions.decimals().call()
    return answer * 10 ** -decimals

def verify_data(logs, web3=w3, address='0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603') -> None:
    """
    Verify data from the oracle verifier chronicle.
    """
    logs = cast(list, collect_logs())
    contract_abi = json.loads(Path(ABI_PATH).read_text())['abi']
    contract_address = address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    if not logs:
        return True # there are no logs to verify
    for log in logs:
        transaction_hash = log['transactionHash']
        tx_receipt = web3.eth.get_transaction_receipt(transaction_hash)
        rich_logs = contract.events.OpPoked().process_receipt(tx_receipt)  # type: ignore
        schnorr_data =  rich_logs[0]['args']['schnorrData']
        try:
            tx = contract.functions.opChallenge(schnorrData=schnorr_data)
            return True
        except web3.exceptions.ContractCustomError as e:
            return False
    return False

def challenge_data(schnorr_data, web3=w3, address='0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603') -> None:
    """
    Challenge data from the oracle verifier chronicle.
    """
    contract_abi = json.loads(Path(ABI_PATH).read_text())['abi']
    contract_address = '0xdd6D76262Fd7BdDe428dcfCd94386EbAe0151603'
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    tx = contract.functions.opChallenge(schnorrData=schnorr_data)
    pk = open('ethereum_private_key.txt').read()
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=pk)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash
