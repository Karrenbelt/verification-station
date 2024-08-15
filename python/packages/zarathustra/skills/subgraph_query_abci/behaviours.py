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
import json
from typing import Generator, Set, Type, cast
import requests

from packages.valory.protocols.ledger_api.message import LedgerApiMessage
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
from packages.zarathustra.skills.subgraph_query_abci.payloads import (
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

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            ledger_block_number = 20_000_000  # TODO
            # ledger_block_number = yield from self.get_latest_block_from_ledger()
            self.context.logger.info(f"Latest ledger block: {ledger_block_number}")
            subgraph_block_number = self.get_latest_block_from_subgraph()
            self.context.logger.info(f"Latest subgraph block: {subgraph_block_number}")

            # as subgraph is often slightly behind, we use a tolerance threshold
            tolerance = 10
            subgraph_health = ledger_block_number - subgraph_block_number < tolerance
            payload = CheckSubgraphsHealthPayload(sender=sender, content=subgraph_health)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

    def get_latest_block_from_subgraph(self) -> int:
        api_key = self.params.config["subgraph_api_key"]
        subgraph_config = json.loads(self.synchronized_data.most_voted_subgraph_config)
        subgraph_url = subgraph_config["subgraph_url"]
        query = "{_meta {block {number}}}"
        url = subgraph_url.format(api_key=api_key)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json={"query": query}, headers=headers)
        subgraph_block_number = response.json()["data"]["_meta"]["block"]["number"]
        return subgraph_block_number

    def get_latest_block_from_ledger(self):
        ledger_api_response = yield from self.get_ledger_api_response(
            performative=LedgerApiMessage.Performative.GET_STATE,
            ledger_callable="get_block",
            block_identifier="latest",
        )
        self.context.logger.info(f"Ledger API response: {ledger_api_response}")
        return ledger_api_response


class CollectSubgraphsDataBehaviour(SubgraphQueryBaseBehaviour):
    """CollectSubgraphsDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectSubgraphsDataRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            data = yield from self._request_subgraph_data()
            content = json.dumps(data)
            payload = CollectSubgraphsDataPayload(sender=sender, content=content)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

    def _request_subgraph_data(self):
        """Perform a http request to the subgraph api."""
        self.context.logger.info("Requesting subgraph data.")
        api_key = self.params.config["subgraph_api_key"]
        subgraph_config = json.loads(self.synchronized_data.most_voted_subgraph_config)
        subgraph_url = subgraph_config["subgraph_url"]
        query = subgraph_config["subgraph_query"]
        headers = {"Content-Type": "application/json"}
        url = subgraph_url.format(api_key=api_key)
        content = json.dumps({"query": query}).encode("utf-8")
        response = yield from self.get_http_response(
            method="POST",
            url=url,
            content=content,
            headers=headers,
        )
        data = json.loads(response.body)["data"]
        self.context.logger.info(f"Subgraph query response: {data}")
        return data


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


class LoadSubgraphComponentsBehaviour(SubgraphQueryBaseBehaviour):
    """LoadSubgraphComponentsBehaviour"""

    matching_round: Type[AbstractRound] = LoadSubgraphComponentsRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            config = self._check_config(self.params.config)
            subgraph_url = self.params.config["subgraph_url"]
            subgraph_query = self.params.config["subgraph_query"]
            content = json.dumps({"subgraph_url": subgraph_url, "subgraph_query": subgraph_query})
            self.context.logger.info(f"subgraph config: {content}")
            payload = LoadSubgraphComponentsPayload(sender=sender, content=content)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

    def _check_config(self, config):
        required = ("subgraph_api_key", "subgraph_url", "subgraph_query")
        if not all(map(config.get, required)):
            raise ValueError(f"Ensure all required parameters are provided: {required}")


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
