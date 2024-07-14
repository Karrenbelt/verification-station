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
from time import sleep
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

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
            payload = LoadOracleComponentsPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


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

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareValidTransactionPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


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
