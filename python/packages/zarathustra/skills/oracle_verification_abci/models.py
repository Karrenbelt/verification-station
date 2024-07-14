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

"""This module contains the shared state for the abci skill of OracleVerificationAbciApp."""

from typing import Any
from packages.valory.skills.abstract_round_abci.models import ApiSpecs, BaseParams
from packages.valory.skills.abstract_round_abci.models import (
    BenchmarkTool as BaseBenchmarkTool,
)
from packages.valory.skills.abstract_round_abci.models import Requests as BaseRequests
from packages.valory.skills.abstract_round_abci.models import (
    SharedState as BaseSharedState,
)
from packages.zarathustra.skills.oracle_verification_abci.rounds import OracleVerificationAbciApp


class SharedState(BaseSharedState):
    """Keep the current shared state of the skill."""

    abci_app_cls = OracleVerificationAbciApp


class RandomnessApi(ApiSpecs):
    """A model for randomness api specifications."""


class Params(BaseParams):
    """Keep the current params of the skill."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the parameters' object."""
        # this is a mapping from a prediction market spec's attribute to the creators we want to take into account
        oracle_config = kwargs.get("oracle_config")
        self.user_interface_name = oracle_config
        super().__init__(*args, **kwargs)




Params = BaseParams
Requests = BaseRequests
BenchmarkTool = BaseBenchmarkTool
