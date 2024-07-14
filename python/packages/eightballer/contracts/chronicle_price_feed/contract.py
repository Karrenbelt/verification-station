# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 eightballer
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the scaffold contract definition."""

from typing import Any, List, Tuple

from aea.common import JSONLike
from packages.eightballer.contracts.chronicle_price_feed import PUBLIC_ID
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi, Address


class ChroniclePriceFeed(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PUBLIC_ID

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_RAW_TRANSACTION' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_raw_message(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> bytes:
        """
        Handler method for the 'GET_RAW_MESSAGE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_state(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_STATE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def authed(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'authed' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.authed(who=who).call()
        return {
            'bool': result
        }



    @classmethod
    def authed(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'authed' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.authed().call()
        return {
            'list[address]': result
        }



    @classmethod
    def bar(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'bar' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.bar().call()
        return {
            'int': result
        }



    @classmethod
    def bud(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'bud' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.bud(who=who).call()
        return {
            'int': result
        }



    @classmethod
    def challenge_reward(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'challenge_reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.challengeReward().call()
        return {
            'int': result
        }



    @classmethod
    def construct_op_poke_message(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple,
        schnorrData: tuple
        ) -> JSONLike:
        """Handler method for the 'construct_op_poke_message' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.constructOpPokeMessage(pokeData=pokeData,
        schnorrData=schnorrData).call()
        return {
            'str': result
        }



    @classmethod
    def construct_poke_message(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple
        ) -> JSONLike:
        """Handler method for the 'construct_poke_message' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.constructPokeMessage(pokeData=pokeData).call()
        return {
            'str': result
        }



    @classmethod
    def decimals(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'decimals' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.decimals().call()
        return {
            'int': result
        }



    @classmethod
    def feed_registration_message(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'feed_registration_message' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feedRegistrationMessage().call()
        return {
            'str': result
        }



    @classmethod
    def feeds(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'feeds' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feeds(who=who).call()
        return {
            'bool': result
        }



    @classmethod
    def feeds(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        feedId: int
        ) -> JSONLike:
        """Handler method for the 'feeds' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feeds(feedId=feedId).call()
        return {
            'bool': result,
        'address': result
        }



    @classmethod
    def feeds(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'feeds' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.feeds().call()
        return {
            'list[address]': result
        }



    @classmethod
    def is_acceptable_schnorr_signature_now(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        message: str,
        schnorrData: tuple
        ) -> JSONLike:
        """Handler method for the 'is_acceptable_schnorr_signature_now' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isAcceptableSchnorrSignatureNow(message=message,
        schnorrData=schnorrData).call()
        return {
            'bool': result
        }



    @classmethod
    def latest_answer(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'latest_answer' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.latestAnswer().call()
        return {
            'int': result
        }



    @classmethod
    def latest_round_data(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'latest_round_data' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.latestRoundData().call()
        return {
            'roundId': result,
        'answer': result,
        'startedAt': result,
        'updatedAt': result,
        'answeredInRound': result
        }



    @classmethod
    def max_challenge_reward(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'max_challenge_reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.maxChallengeReward().call()
        return {
            'int': result
        }



    @classmethod
    def op_challenge_period(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'op_challenge_period' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.opChallengePeriod().call()
        return {
            'int': result
        }



    @classmethod
    def op_feed_id(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'op_feed_id' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.opFeedId().call()
        return {
            'int': result
        }



    @classmethod
    def peek(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'peek' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.peek().call()
        return {
            'int': result,
        'bool': result
        }



    @classmethod
    def peep(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'peep' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.peep().call()
        return {
            'int': result,
        'bool': result
        }



    @classmethod
    def read(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'read' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.read().call()
        return {
            'int': result
        }



    @classmethod
    def read_with_age(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'read_with_age' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.readWithAge().call()
        return {
            'int': result,
        'int': result
        }



    @classmethod
    def tolled(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'tolled' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.tolled(who=who).call()
        return {
            'bool': result
        }



    @classmethod
    def tolled(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'tolled' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.tolled().call()
        return {
            'list[address]': result
        }



    @classmethod
    def try_read(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'try_read' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.tryRead().call()
        return {
            'bool': result,
        'int': result
        }



    @classmethod
    def try_read_with_age(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'try_read_with_age' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.tryReadWithAge().call()
        return {
            'bool': result,
        'int': result,
        'int': result
        }



    @classmethod
    def wards(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'wards' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.wards(who=who).call()
        return {
            'int': result
        }



    @classmethod
    def wat(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'wat' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.wat().call()
        return {
            'str': result
        }


    @classmethod
    def deny(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'deny' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.deny(who=who)
        return tx


    @classmethod
    def diss(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'diss' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.diss(who=who)
        return tx


    @classmethod
    def drop(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        feedIds: List[int]
        ) -> JSONLike:
        """Handler method for the 'drop' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.drop(feedIds=feedIds)
        return tx


    @classmethod
    def drop(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        feedId: int
        ) -> JSONLike:
        """Handler method for the 'drop' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.drop(feedId=feedId)
        return tx


    @classmethod
    def kiss(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'kiss' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.kiss(who=who)
        return tx


    @classmethod
    def lift(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pubKey: tuple,
        ecdsaData: tuple
        ) -> JSONLike:
        """Handler method for the 'lift' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.lift(pubKey=pubKey,
        ecdsaData=ecdsaData)
        return tx


    @classmethod
    def lift(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pubKeys: Tuple,
        ecdsaDatas: Tuple
        ) -> JSONLike:
        """Handler method for the 'lift' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.lift(pubKeys=pubKeys,
        ecdsaDatas=ecdsaDatas)
        return tx


    @classmethod
    def op_challenge(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        schnorrData: tuple
        ) -> JSONLike:
        """Handler method for the 'op_challenge' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.opChallenge(schnorrData=schnorrData)
        return tx


    @classmethod
    def op_poke(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple,
        schnorrData: tuple,
        ecdsaData: tuple
        ) -> JSONLike:
        """Handler method for the 'op_poke' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.opPoke(pokeData=pokeData,
        schnorrData=schnorrData,
        ecdsaData=ecdsaData)
        return tx


    @classmethod
    def op_poke_optimized_397084999(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple,
        schnorrData: tuple,
        ecdsaData: tuple
        ) -> JSONLike:
        """Handler method for the 'op_poke_optimized_397084999' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.opPoke_optimized_397084999(pokeData=pokeData,
        schnorrData=schnorrData,
        ecdsaData=ecdsaData)
        return tx


    @classmethod
    def poke(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple,
        schnorrData: tuple
        ) -> JSONLike:
        """Handler method for the 'poke' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.poke(pokeData=pokeData,
        schnorrData=schnorrData)
        return tx


    @classmethod
    def poke_optimized_7136211(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        pokeData: tuple,
        schnorrData: tuple
        ) -> JSONLike:
        """Handler method for the 'poke_optimized_7136211' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.poke_optimized_7136211(pokeData=pokeData,
        schnorrData=schnorrData)
        return tx


    @classmethod
    def rely(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        who: Address
        ) -> JSONLike:
        """Handler method for the 'rely' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.rely(who=who)
        return tx


    @classmethod
    def set_bar(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        bar_: int
        ) -> JSONLike:
        """Handler method for the 'set_bar' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.setBar(bar_=bar_)
        return tx


    @classmethod
    def set_max_challenge_reward(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        maxChallengeReward_: int
        ) -> JSONLike:
        """Handler method for the 'set_max_challenge_reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.setMaxChallengeReward(maxChallengeReward_=maxChallengeReward_)
        return tx


    @classmethod
    def set_op_challenge_period(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        opChallengePeriod_: int
        ) -> JSONLike:
        """Handler method for the 'set_op_challenge_period' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.setOpChallengePeriod(opChallengePeriod_=opChallengePeriod_)
        return tx
