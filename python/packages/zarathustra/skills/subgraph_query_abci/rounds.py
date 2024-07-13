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

"""This package contains the rounds of SubgraphQueryAbciApp."""

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

from packages.zarathustra.skills.subgraph_query_abci.payloads import (
    CheckSubgraphsHealthPayload,
    CollectSubgraphsDataPayload,
    DataTransformationPayload,
    LoadSubgraphComponentsPayload,
)
from packages.valory.skills.abstract_round_abci.base import CollectionRound


class Event(Enum):
    """SubgraphQueryAbciApp Events"""

    MAX_RETRIES = "max_retries"
    SYNCHRONIZED = "synchronized"
    DONE = "done"
    RETRY = "retry"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class CheckSubgraphsHealthRound(CollectionRound):
    """CheckSubgraphsHealthRound"""

    payload_class = CheckSubgraphsHealthPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.SYNCHRONIZED


class CollectSubgraphsDataRound(CollectionRound):
    """CollectSubgraphsDataRound"""

    payload_class = CollectSubgraphsDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class DataTransformationRound(CollectionRound):
    """DataTransformationRound"""

    payload_class = DataTransformationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE



class LoadSubgraphComponentsRound(CollectionRound):
    """LoadSubgraphComponentsRound"""

    payload_class = LoadSubgraphComponentsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE


class FailedToSynchronizeRound(DegenerateRound):
    """FailedToSynchronizeRound"""


class FinalSubgraphQueryRound(DegenerateRound):
    """FinalSubgraphQueryRound"""


class SubgraphQueryAbciApp(AbciApp[Event]):
    """SubgraphQueryAbciApp"""

    initial_round_cls: AppState = LoadSubgraphComponentsRound
    initial_states: Set[AppState] = {LoadSubgraphComponentsRound}
    transition_function: AbciAppTransitionFunction = {
        LoadSubgraphComponentsRound: {
            Event.DONE: CheckSubgraphsHealthRound
        },
        CheckSubgraphsHealthRound: {
            Event.SYNCHRONIZED: CollectSubgraphsDataRound,
            Event.RETRY: CheckSubgraphsHealthRound,
            Event.MAX_RETRIES: FailedToSynchronizeRound
        },
        CollectSubgraphsDataRound: {
            Event.DONE: DataTransformationRound
        },
        DataTransformationRound: {
            Event.DONE: FinalSubgraphQueryRound
        },
        FailedToSynchronizeRound: {},
        FinalSubgraphQueryRound: {}
    }
    final_states: Set[AppState] = {FinalSubgraphQueryRound, FailedToSynchronizeRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: FrozenSet[str] = frozenset()
    db_pre_conditions: Dict[AppState, Set[str]] = {
        LoadSubgraphComponentsRound: {'participants'},
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        FinalSubgraphQueryRound: {'most_voted_tx_hash'},
    	FailedToSynchronizeRound: [],
    }
