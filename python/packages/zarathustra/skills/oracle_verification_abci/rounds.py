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

from collections import Counter
from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Set, Tuple, cast


from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    ABCIAppException,
    AbciAppTransitionFunction,
    ABCIAppInternalError,
    AbstractRound,
    AppState,
    BaseTxPayload,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
    DeserializedCollection,
    get_name,
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
from packages.valory.skills.abstract_round_abci.base import CollectSameUntilThresholdRound, VotingRound

from packages.valory.skills.transaction_settlement_abci.payload_tools import (
    hash_payload_to_hex,
)


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

    @property
    def most_voted_tx_hash(self) -> float:
        """Get the most_voted_tx_hash."""
        return cast(float, self.db.get_strict("most_voted_tx_hash"))

    def _get_deserialized(self, key: str) -> DeserializedCollection:
        """Strictly get a collection and return it deserialized."""
        serialized = self.db.get_strict(key)
        deserialized = CollectionRound.deserialize_collection(serialized)
        return cast(DeserializedCollection, deserialized)

    @property
    def participant_to_signatures(self) -> Dict[str, Optional[str]]:
        """Get the `participant_to_signatures`."""
        participant_to_payload = self._get_deserialized("participant_to_signatures")
        return {
            agent_address: payload.signature
            for agent_address, payload in participant_to_payload.items()
        }

    @property
    def most_voted_tx_hash(self) -> float:
        """Get the most_voted_tx_hash."""
        return cast(float, self.db.get_strict("most_voted_tx_hash"))

    @property
    def signature(self) -> str:
        """Get the current agent's signature."""
        return str(self.db.get("signature", {}))

    @property
    def data_json(self) -> str:
        """Get the data json."""
        return str(self.db.get("data_json", ""))


class CheckServiceDepositsRound(CollectSameUntilThresholdRound):
    """CheckServiceDepositsRound"""

    payload_class = CheckServiceDepositsPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.NO_NEW_DEPOSIT

class CollectOracleDataRound(CollectSameUntilThresholdRound):
    """CollectOracleDataRound"""

    payload_class = CollectOracleDataPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
\        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class LoadOracleComponentsRound(CollectSameUntilThresholdRound):
    """LoadOracleComponentsRound"""

    payload_class = LoadOracleComponentsPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class OracleAttestationRound(CollectSameUntilThresholdRound):
    """OracleAttestationRound"""

    payload_class = OracleAttestationPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.VALID

class PrepareMintTokenRound(CollectSameUntilThresholdRound):
    """PrepareMintTokenRound"""

    payload_class = PrepareMintTokenPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class PrepareRepayTokenRound(CollectSameUntilThresholdRound):
    """PrepareRepayTokenRound"""

    payload_class = PrepareRepayTokenPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class PrepareSlashingTransactionRound(CollectSameUntilThresholdRound):
    """PrepareSlashingTransactionRound"""

    payload_class = PrepareSlashingTransactionPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class,
            **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE

class PrepareValidTransactionRound(CollectSameUntilThresholdRound):
    """PrepareValidTransactionRound"""

    payload_class = PrepareValidTransactionPayload
    payload_attribute = "content"
    synchronized_data_class = SynchronizedData
    collection_key = get_name(SynchronizedData.participant_to_signatures)
    selection_key = (
        get_name(SynchronizedData.signature),
        get_name(SynchronizedData.data_json),
        get_name(SynchronizedData.most_voted_tx_hash),
    )

    @property
    def payload_values_count(self) -> Counter:
        """Get count of payload values."""
        return Counter(map(lambda p: (p.values[2],), self.payloads))

    @property
    def most_voted_payload_values(
        self,
    ) -> Tuple[Any, ...]:
        """Get the most voted payload values."""
        _, max_votes = self.payload_values_count.most_common()[0]
        if max_votes < self.synchronized_data.consensus_threshold:
            raise ABCIAppInternalError("not enough votes")

        all_payload_values_count = Counter(map(lambda p: p.values, self.payloads))
        most_voted_payload_values, _ = all_payload_values_count.most_common()[0]
        return most_voted_payload_values

    def check_majority_possible(
        self,
        votes_by_participant: Dict[str, BaseTxPayload],
        nb_participants: int,
        exception_cls: Type[ABCIAppException] = ABCIAppException,
    ) -> None:
        """
        Overrides the check to only account for the tx hash which should be the same.

        The rest attributes have to be different.

        :param votes_by_participant: a mapping from a participant to its vote
        :param nb_participants: the total number of participants
        :param exception_cls: the class of the exception to raise in case the check fails
        """
        votes_by_participant = {
            participant: PrepareValidTransactionPayload(
                payload.sender, tx_hash=payload.content["tx_hash"]
            )
            for participant, payload in votes_by_participant.items()
        }
        super().check_majority_possible(
            votes_by_participant, nb_participants, exception_cls
        )

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
