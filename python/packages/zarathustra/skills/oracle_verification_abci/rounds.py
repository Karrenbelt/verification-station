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

"""This package contains the rounds of OracleVerificationAbciApp."""

from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.zarathustra.skills.oracle_verification_abci.payloads import (
    CheckServiceDepositsPayload,
    CollectOracleDataPayload,
    LoadOracleComponentsPayload,
    OracleAttestationPayload,
    PrepareMintTokenPayload,
    PrepareRepayTokenPayload,
    PrepareSlashingTransactionPayload,
    PrepareValidTransactionPayload,
)
from packages.valory.skills.abstract_round_abci.base import CollectionRound, VotingRound


class Event(Enum):
    """OracleVerificationAbciApp Events"""

    NEW_DEPOSIT_vsETH = "new_deposit_vseth"
    NEW_DEPOSIT_ETH = "new_deposit_eth"
    INVALID = "invalid"
    VALID = "valid"
    DONE = "done"
    NO_NEW_DEPOSIT = "no_new_deposit"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class CheckServiceDepositsRound(CollectionRound):
    """CheckServiceDepositsRound"""

    payload_class = CheckServiceDepositsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class CollectOracleDataRound(CollectionRound):
    """CollectOracleDataRound"""

    payload_class = CollectOracleDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class LoadOracleComponentsRound(CollectionRound):
    """LoadOracleComponentsRound"""

    payload_class = LoadOracleComponentsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class OracleAttestationRound(CollectionRound):
    """OracleAttestationRound"""

    payload_class = OracleAttestationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

class PrepareMintTokenRound(VotingRound):
    """PrepareMintTokenRound"""

    payload_class = PrepareMintTokenPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class PrepareRepayTokenRound(VotingRound):
    """PrepareRepayTokenRound"""

    payload_class = PrepareRepayTokenPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class PrepareSlashingTransactionRound(VotingRound):
    """PrepareSlashingTransactionRound"""

    payload_class = PrepareSlashingTransactionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class PrepareValidTransactionRound(VotingRound):
    """PrepareValidTransactionRound"""

    payload_class = PrepareValidTransactionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class FinalizedTransactionPreparationRound(DegenerateRound):
    """FinalizedTransactionPreparationRound"""


class OracleVerificationAbciApp(AbciApp[Event]):
    """OracleVerificationAbciApp"""

    initial_round_cls: AppState = CheckServiceDepositsRound
    initial_states: Set[AppState] = {CheckServiceDepositsRound}
    transition_function: AbciAppTransitionFunction = {
        CheckServiceDepositsRound: {
            Event.NEW_DEPOSIT_vsETH: PrepareRepayTokenRound,
            Event.NEW_DEPOSIT_ETH: PrepareMintTokenRound,
            Event.NO_NEW_DEPOSIT: LoadOracleComponentsRound
        },
        LoadOracleComponentsRound: {
            Event.DONE: CollectOracleDataRound
        },
        CollectOracleDataRound: {
            Event.DONE: OracleAttestationRound
        },
        OracleAttestationRound: {
            Event.VALID: PrepareValidTransactionRound,
            Event.INVALID: PrepareSlashingTransactionRound
        },
        PrepareMintTokenRound: {
            Event.DONE: FinalizedTransactionPreparationRound
        },
        PrepareRepayTokenRound: {
            Event.DONE: FinalizedTransactionPreparationRound
        },
        PrepareValidTransactionRound: {
            Event.DONE: FinalizedTransactionPreparationRound
        },
        PrepareSlashingTransactionRound: {
            Event.DONE: FinalizedTransactionPreparationRound
        },
        FinalizedTransactionPreparationRound: {}
    }
    final_states: Set[AppState] = {FinalizedTransactionPreparationRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: FrozenSet[str] = frozenset()
    db_pre_conditions: Dict[AppState, Set[str]] = {
        CheckServiceDepositsRound: {'participants'},
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        FinalizedTransactionPreparationRound: {'most_voted_tx_hash'},
    }
