
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

"""This module contains the shared state for the composite CompositeAbciApp skill."""

from packages.valory.skills.abstract_round_abci.models import BaseParams
from packages.valory.skills.abstract_round_abci.models import (
    BenchmarkTool as BaseBenchmarkTool,
)
from packages.valory.skills.abstract_round_abci.models import Requests as BaseRequests
from packages.valory.skills.abstract_round_abci.models import (
    SharedState as BaseSharedState,
)
from packages.zarathustra.skills.oracle_verification_abci.models import RandomnessApi as BaseRandomnessApi
from packages.zarathustra.skills.oracle_verification.composition import CompositeAbciApp

from packages.valory.skills.registration_abci.models import Params as RegistrationParams
from packages.valory.skills.transaction_settlement_abci.models import TransactionParams as TransactionSettlementParams
from packages.valory.skills.reset_pause_abci.models import Params as ResetAndPauseParams
from packages.eightballer.skills.ui_loader_abci.models import UserInterfaceLoaderParams as UILoaderParams 
from packages.eightballer.skills.ui_loader_abci.models import UserInterfaceClientStrategy
from packages.zarathustra.skills.subgraph_query_abci.models import Params as SubgraphQueryParams
from packages.zarathustra.skills.oracle_verification_abci.models import Params as OracleVerificationParams

class SharedState(BaseSharedState):
    """Keep the current shared state of the skill."""

    abci_app_cls = CompositeAbciApp


class Params(
    # RegistrationParams,
    # TransactionSettlementParams,
    # ResetAndPauseParams,
    UILoaderParams,
    # SubgraphQueryParams,
    # OracleVerificationParams,
):
    """Oracle Verification Params"""

Requests = BaseRequests
BenchmarkTool = BaseBenchmarkTool
RandomnessApi = BaseRandomnessApi
UiClientStrategy = UserInterfaceClientStrategy
