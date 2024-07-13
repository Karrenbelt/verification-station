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

"""This package contains round behaviours of SubgraphQueryAbciApp."""

from abc import ABC
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.zarathustra.skills.subgraph_query_abci.models import Params
from packages.zarathustra.skills.subgraph_query_abci.rounds import (
    SynchronizedData,
    SubgraphQueryAbciApp,
    CheckSubgraphsHealthRound,
    CollectSubgraphsDataRound,
    DataTransformationRound,
    LoadSubgraphComponentsRound,
)
from packages.zarathustra.skills.subgraph_query_abci.rounds import (
    CheckSubgraphsHealthPayload,
    CollectSubgraphsDataPayload,
    DataTransformationPayload,
    LoadSubgraphComponentsPayload,
)


class SubgraphQueryBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the subgraph_query_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class CheckSubgraphsHealthBehaviour(SubgraphQueryBaseBehaviour):
    """CheckSubgraphsHealthBehaviour"""

    matching_round: Type[AbstractRound] = CheckSubgraphsHealthRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CheckSubgraphsHealthPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CollectSubgraphsDataBehaviour(SubgraphQueryBaseBehaviour):
    """CollectSubgraphsDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectSubgraphsDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectSubgraphsDataPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class DataTransformationBehaviour(SubgraphQueryBaseBehaviour):
    """DataTransformationBehaviour"""

    matching_round: Type[AbstractRound] = DataTransformationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = DataTransformationPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class LoadSubgraphComponentsBehaviour(SubgraphQueryBaseBehaviour):
    """LoadSubgraphComponentsBehaviour"""

    matching_round: Type[AbstractRound] = LoadSubgraphComponentsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = LoadSubgraphComponentsPayload(sender=sender, content="dummy_content")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class SubgraphQueryRoundBehaviour(AbstractRoundBehaviour):
    """SubgraphQueryRoundBehaviour"""

    initial_behaviour_cls = LoadSubgraphComponentsBehaviour
    abci_app_cls = SubgraphQueryAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        CheckSubgraphsHealthBehaviour,
        CollectSubgraphsDataBehaviour,
        DataTransformationBehaviour,
        LoadSubgraphComponentsBehaviour
    ]
