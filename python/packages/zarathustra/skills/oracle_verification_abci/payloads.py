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

"""This module contains the transaction payloads of the OracleVerificationAbciApp."""

from typing import Any
from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class CheckServiceDepositsPayload(BaseTxPayload):
    """Represent a transaction payload for the CheckServiceDepositsRound."""

    content = Any


@dataclass(frozen=True)
class CollectOracleDataPayload(BaseTxPayload):
    """Represent a transaction payload for the CollectOracleDataRound."""

    content = Any


@dataclass(frozen=True)
class LoadOracleComponentsPayload(BaseTxPayload):
    """Represent a transaction payload for the LoadOracleComponentsRound."""

    content = Any


@dataclass(frozen=True)
class OracleAttestationPayload(BaseTxPayload):
    """Represent a transaction payload for the OracleAttestationRound."""

    content = Any


@dataclass(frozen=True)
class PrepareMintTokenPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareMintTokenRound."""

    content = Any


@dataclass(frozen=True)
class PrepareRepayTokenPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareRepayTokenRound."""

    content = Any


@dataclass(frozen=True)
class PrepareSlashingTransactionPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareSlashingTransactionRound."""

    content = Any


@dataclass(frozen=True)
class PrepareValidTransactionPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareValidTransactionRound."""

    content = Any

