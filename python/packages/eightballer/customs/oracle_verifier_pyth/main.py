

from aea.skills.base import Behaviour
# we use web3 to make some calls to the Ethereum node.
import requests


def collect_data(from_block_number=None, to_block_number='latest', ) -> None:
    """
    Collect data from the oracle verifier chronicle.
    """
    response = requests.get('https://hermes.pyth.network/v2/updates/price/latest?ids%5B%5D=0xff61491a931112ddf1bd8147cd1b641375f79f5825126d665480874634fd0ace')
    data = response.json()
    price_data = data['parsed'][0]['price']
    decimals = data['parsed'][0]['price']['expo']
    return int(price_data['price']) * 10 ** decimals

def verify_data(logs, )-> None:
    """
    Verify data from the oracle verifier chronicle.
    """
    return True

def challenge_data(schnorr_data, ) -> None:
    """
    Challenge data from the oracle verifier chronicle.
    """
    raise Exception('Not implemented')