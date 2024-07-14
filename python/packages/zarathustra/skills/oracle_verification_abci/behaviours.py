# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 zarathustra
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

"""This package contains round behaviours of OracleVerificationAbciApp."""

from abc import ABC
import copy
import hashlib
import json
from decimal import Decimal
from time import sleep
from typing import Dict, Generator, Optional, Set, Tuple, Type, cast

from packages.valory.contracts.gnosis_safe.contract import GnosisSafeContract

# TODO
# from packages.eightballer.contracts.oracle_attestation.contract import (
#     AttestationContract,
# )
from packages.valory.protocols.contract_api.message import ContractApiMessage
from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.valory.skills.transaction_settlement_abci.payload_tools import hash_payload_to_hex
from packages.zarathustra.skills.oracle_verification_abci.models import Params
from packages.zarathustra.skills.oracle_verification_abci.rounds import (
    SynchronizedData,
    OracleVerificationAbciApp,
    CheckServiceDepositsRound,
    CollectOracleDataRound,
    LoadOracleComponentsRound,
    OracleAttestationRound,
    PrepareMintTokenRound,
    PrepareRepayTokenRound,
    PrepareSlashingTransactionRound,
    PrepareValidTransactionRound,
)
from packages.zarathustra.skills.oracle_verification_abci.rounds import (
    CheckServiceDepositsPayload,
    CollectOracleDataPayload,
    LoadOracleComponentsPayload,
    OracleAttestationPayload,
    PrepareMintTokenPayload,
    PrepareRepayTokenPayload,
    PrepareSlashingTransactionPayload,
    PrepareValidTransactionPayload,
)


def to_int(most_voted_estimate: float, decimals: int) -> int:
    """Convert to int."""
    most_voted_estimate_ = str(most_voted_estimate)
    decimal_places = most_voted_estimate_[::-1].find(".")
    if decimal_places > decimals:
        most_voted_estimate_ = most_voted_estimate_[: -(decimal_places - decimals)]
    most_voted_estimate_decimal = Decimal(most_voted_estimate_)
    int_value = int(most_voted_estimate_decimal * (10**decimals))
    return int_value



class OracleVerificationBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the oracle_verification_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class CheckServiceDepositsBehaviour(OracleVerificationBaseBehaviour):
    """CheckServiceDepositsBehaviour"""

    matching_round: Type[AbstractRound] = CheckServiceDepositsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CheckServiceDepositsPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CollectOracleDataBehaviour(OracleVerificationBaseBehaviour):
    """CollectOracleDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectOracleDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectOracleDataPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class LoadOracleComponentsBehaviour(OracleVerificationBaseBehaviour):
    """LoadOracleComponentsBehaviour"""

    matching_round: Type[AbstractRound] = LoadOracleComponentsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            yield from self._load_oracle_components()
            payload = LoadOracleComponentsPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


    def _load_oracle_components(self) -> None: # type: ignore
        """Load oracle components."""
        self.context.logger.info("Loading oracle components...")
        self.context.shared_state['oracles'] = self.params.oracle_config
        yield 


class OracleAttestationBehaviour(OracleVerificationBaseBehaviour):
    """OracleAttestationBehaviour"""

    matching_round: Type[AbstractRound] = OracleAttestationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = OracleAttestationPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareMintTokenBehaviour(OracleVerificationBaseBehaviour):
    """PrepareMintTokenBehaviour"""

    matching_round: Type[AbstractRound] = PrepareMintTokenRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareMintTokenPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareRepayTokenBehaviour(OracleVerificationBaseBehaviour):
    """PrepareRepayTokenBehaviour"""

    matching_round: Type[AbstractRound] = PrepareRepayTokenRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareRepayTokenPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareSlashingTransactionBehaviour(OracleVerificationBaseBehaviour):
    """PrepareSlashingTransactionBehaviour"""

    matching_round: Type[AbstractRound] = PrepareSlashingTransactionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareSlashingTransactionPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareValidTransactionBehaviour(OracleVerificationBaseBehaviour):
    """PrepareValidTransactionBehaviour"""

    matching_round: Type[AbstractRound] = PrepareValidTransactionRound

    def async_act(self) -> Generator:
        """
        Do the action.

        Steps:
        - Request the transaction hash for the safe transaction. This is the
          hash that needs to be signed by a threshold of agents.
        - Send the transaction hash as a transaction and wait for it to be mined.
        - Wait until ABCI application transitions to the next round.
        - Go to the next behaviour (set done event).
        """

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            signature = data_json = None
            payload_string = yield from self._get_safe_tx_hash()
            service_data = self.get_service_data()
            if payload_string is not None:
                signature, data_json = yield from self.get_data_signature(service_data)
            payload = PrepareValidTransactionPayload(
                address=self.context.agent_address,
                signature=signature,
                data_json=data_json,
                payload_string=payload_string,
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def get_service_data(self) -> Dict:
        """Get service data to expose."""
        period_count = self.synchronized_data.period_count
        self.context.logger.info("Attempting broadcast")

        prev_tx_hash = ""
        if period_count != 0:
            # grab tx_hash from previous cycle
            prev_period_count = period_count - 1
            previous_data = self.synchronized_data.db.get_latest_from_reset_index(
                prev_period_count
            )

            prev_tx_hash = previous_data.get("final_tx_hash", "")

        # select relevant data
        payloads = self.synchronized_data.db.get_strict("participant_to_observations")
        attestation = self.synchronized_data.db.get_strict("content")

        observations = {
            address: payload.content for address, payload in payloads.items()
        }

        # adding timestamp on server side when received
        # period and agent_address are used as `primary key`
        return {
            "period_count": period_count,
            "agent_address": self.context.agent_address,
            "attestation": attestation,
            "prev_tx_hash": prev_tx_hash,
            "observations": observations,
            # "data_source": price_api.api_id,
            # "unit": f"{price_api.currency_id}:{price_api.convert_id}",
        }

    def get_data_signature(self, data: Dict) -> Generator[None, None, Tuple[str, str]]:
        """Get signature for the data."""
        data = copy.deepcopy(data)

        data.pop("agent_address", None)  # agent address is unique, need to remove it
        data.pop("data_source", None)  # data_source can be unique, need to remove it

        data_json = json.dumps(data, sort_keys=True)
        data_bytes = data_json.encode("ascii")
        hash_bytes = hashlib.sha256(data_bytes).digest()

        signature_hex = yield from self.get_signature(
            hash_bytes, is_deprecated_mode=True
        )
        # remove the leading '0x'
        signature_hex = signature_hex[2:]
        self.context.logger.info(f"Data signature: {signature_hex}")
        return signature_hex, data_json

    def _get_safe_tx_hash(self) -> Generator[None, None, Optional[str]]:
        """Get the transaction hash of the Safe tx."""
        contract_id = AttestationContract.contract_id
        contract_api_msg = yield from self.get_contract_api_response(
            performative=ContractApiMessage.Performative.GET_RAW_TRANSACTION,  # type: ignore
            contract_address=self.synchronized_data.oracle_contract_address,
            contract_id=str(contract_id),
            contract_callable="get_latest_transmission_details",
        )
        if (
            contract_api_msg.performative
            != ContractApiMessage.Performative.RAW_TRANSACTION
        ):  # pragma: nocover
            self.context.logger.warning("get_latest_transmission_details unsuccessful!")
            return None
        epoch_ = cast(int, contract_api_msg.raw_transaction.body["epoch_"]) + 1
        round_ = cast(int, contract_api_msg.raw_transaction.body["round_"])
        decimals = self.params.oracle_params["decimals"]
        amount = self.synchronized_data.most_voted_estimate
        amount_ = to_int(amount, decimals)
        contract_api_msg = yield from self.get_contract_api_response(
            performative=ContractApiMessage.Performative.GET_RAW_TRANSACTION,  # type: ignore
            contract_address=self.synchronized_data.target_contract_address,
            contract_id=str(OffchainAggregatorContract.contract_id),  # TODO
            contract_callable="get_transmit_data",
            epoch_=epoch_,
            round_=round_,
            amount_=amount_,
        )
        if (
            contract_api_msg.performative
            != ContractApiMessage.Performative.RAW_TRANSACTION
        ):  # pragma: nocover
            self.context.logger.warning("get_transmit_data unsuccessful!")
            return None
        data = cast(bytes, contract_api_msg.raw_transaction.body["data"])
        to_address = self.synchronized_data.target_contract_address
        ether_value = ETHER_VALUE
        safe_tx_gas = SAFE_TX_GAS
        contract_api_msg = yield from self.get_contract_api_response(
            performative=ContractApiMessage.Performative.GET_RAW_TRANSACTION,  # type: ignore
            contract_address=self.synchronized_data.safe_contract_address,
            contract_id=str(GnosisSafeContract.contract_id),
            contract_callable="get_raw_safe_transaction_hash",
            to_address=to_address,
            value=ether_value,
            data=data,
            safe_tx_gas=safe_tx_gas,
        )
        if (
            contract_api_msg.performative
            != ContractApiMessage.Performative.RAW_TRANSACTION
        ):  # pragma: nocover
            self.context.logger.warning("get_raw_safe_transaction_hash unsuccessful!")
            return None
        safe_tx_hash = cast(str, contract_api_msg.raw_transaction.body["tx_hash"])
        safe_tx_hash = safe_tx_hash[2:]
        self.context.logger.info(f"Hash of the Safe transaction: {safe_tx_hash}")
        # temp hack:
        payload_string = hash_payload_to_hex(
            safe_tx_hash, ether_value, safe_tx_gas, to_address, data
        )
        return payload_string


class OracleVerificationRoundBehaviour(AbstractRoundBehaviour):
    """OracleVerificationRoundBehaviour"""

    initial_behaviour_cls = CheckServiceDepositsBehaviour
    abci_app_cls = OracleVerificationAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        CheckServiceDepositsBehaviour,
        CollectOracleDataBehaviour,
        LoadOracleComponentsBehaviour,
        OracleAttestationBehaviour,
        PrepareMintTokenBehaviour,
        PrepareRepayTokenBehaviour,
        PrepareSlashingTransactionBehaviour,
        PrepareValidTransactionBehaviour
    ]
