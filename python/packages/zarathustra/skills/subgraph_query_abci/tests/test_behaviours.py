# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
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

"""This package contains round behaviours of SubgraphQueryAbciApp."""

from pathlib import Path
from typing import Any, Dict, Hashable, Optional, Type
from dataclasses import dataclass, field

import pytest

from packages.valory.skills.abstract_round_abci.base import AbciAppDB
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
    make_degenerate_behaviour,
)
from packages.zarathustra.skills.subgraph_query_abci.behaviours import (
    SubgraphQueryBaseBehaviour,
    SubgraphQueryRoundBehaviour,
    CheckSubgraphsHealthBehaviour,
    CollectSubgraphsDataBehaviour,
    DataTransformationBehaviour,
    LoadSubgraphComponentsBehaviour,
)
from packages.zarathustra.skills.subgraph_query_abci.rounds import (
    SynchronizedData,
    DegenerateRound,
    Event,
    SubgraphQueryAbciApp,
    CheckSubgraphsHealthRound,
    CollectSubgraphsDataRound,
    DataTransformationRound,
    FailedToSynchronizeRound,
    FinalSubgraphQueryRound,
    LoadSubgraphComponentsRound,
)

from packages.valory.skills.abstract_round_abci.test_tools.base import (
    FSMBehaviourBaseCase,
)


@dataclass
class BehaviourTestCase:
    """BehaviourTestCase"""

    name: str
    initial_data: Dict[str, Hashable]
    event: Event
    kwargs: Dict[str, Any] = field(default_factory=dict)


class BaseSubgraphQueryTest(FSMBehaviourBaseCase):
    """Base test case."""

    path_to_skill = Path(__file__).parent.parent

    behaviour: SubgraphQueryRoundBehaviour
    behaviour_class: Type[SubgraphQueryBaseBehaviour]
    next_behaviour_class: Type[SubgraphQueryBaseBehaviour]
    synchronized_data: SynchronizedData
    done_event = Event.DONE

    @property
    def current_behaviour_id(self) -> str:
        """Current RoundBehaviour's behaviour id"""

        return self.behaviour.current_behaviour.behaviour_id

    def fast_forward(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Fast-forward on initialization"""

        data = data if data is not None else {}
        self.fast_forward_to_behaviour(
            self.behaviour,
            self.behaviour_class.behaviour_id,
            SynchronizedData(AbciAppDB(setup_data=AbciAppDB.data_to_lists(data))),
        )
        assert self.current_behaviour_id == self.behaviour_class.behaviour_id

    def complete(self, event: Event) -> None:
        """Complete test"""

        self.behaviour.act_wrapper()
        self.mock_a2a_transaction()
        self._test_done_flag_set()
        self.end_round(done_event=event)
        assert self.current_behaviour_id == self.next_behaviour_class.behaviour_id


class TestCheckSubgraphsHealthBehaviour(BaseSubgraphQueryTest):
    """Tests CheckSubgraphsHealthBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CheckSubgraphsHealthBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCollectSubgraphsDataBehaviour(BaseSubgraphQueryTest):
    """Tests CollectSubgraphsDataBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CollectSubgraphsDataBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestDataTransformationBehaviour(BaseSubgraphQueryTest):
    """Tests DataTransformationBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = DataTransformationBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestLoadSubgraphComponentsBehaviour(BaseSubgraphQueryTest):
    """Tests LoadSubgraphComponentsBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = LoadSubgraphComponentsBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)

