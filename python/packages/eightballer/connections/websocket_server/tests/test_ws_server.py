# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 Valory AG
#   Copyright 2018-2021 Fetch.AI Limited
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
"""This module contains the tests of the HTTP Server connection module."""
# pylint: disable=W0201
import asyncio
import logging
import os
from traceback import print_exc
from typing import Tuple, cast
from unittest.mock import MagicMock

import aiohttp
import pytest
from aea.common import Address
from aea.configurations.base import ConnectionConfig
from aea.identity.base import Identity
from aea.mail.base import Envelope, Message
from aea.protocols.dialogue.base import Dialogue as BaseDialogue
from aiohttp.client_reqrep import ClientResponse

from packages.eightballer.connections.websocket_server.connection import (
    WebSocketServerConnection,
)
from packages.eightballer.protocols.http.dialogues import HttpDialogue
from packages.eightballer.protocols.http.dialogues import (
    HttpDialogues as BaseHttpDialogues,
)
from packages.eightballer.protocols.http.message import HttpMessage
from tests.conftest import ROOT_DIR, get_host, get_unused_tcp_port

logger = logging.getLogger(__name__)


class HttpDialogues(BaseHttpDialogues):
    """The dialogues class keeps track of all http dialogues."""

    def __init__(self, self_address: Address) -> None:
        """
        Initialize dialogues.

        :return: None
        """

        def role_from_first_message(  # pylint: disable=unused-argument
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            del receiver_address
            return HttpDialogue.Role.SERVER

        BaseHttpDialogues.__init__(
            self,
            self_address=self_address,
            role_from_first_message=role_from_first_message,
        )


@pytest.mark.asyncio
class TestWebSocketServer:
    """Tests for HTTPServer connection."""

    async def request(self, method: str, path: str, **kwargs) -> ClientResponse:
        """
        Make a http request.

        :param method: HTTP method: GET, POST etc
        :param path: path to request on server. full url constructed automatically

        :return: http response
        """
        try:
            url = f"http://{self.host}:{self.port}{path}"
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, **kwargs) as resp:
                    await resp.read()
                    return resp
        except Exception:
            print_exc()
            raise

    def setup(self):
        """Initialise the test case."""
        self.identity = Identity("name", address="my_key", public_key="my_public_key")
        self.agent_address = self.identity.address
        self.host = get_host()
        self.port = get_unused_tcp_port()
        self.api_spec_path = os.path.join(
            ROOT_DIR, "tests", "data", "petstore_sim.yaml"
        )
        self.connection_id = WebSocketServerConnection.connection_id
        self.protocol_id = HttpMessage.protocol_id
        self.target_skill_id = "some_author/some_skill:0.1.0"

        self.configuration = ConnectionConfig(
            host=self.host,
            port=self.port,
            target_skill_id=self.target_skill_id,
            api_spec_path=self.api_spec_path,
            connection_id=WebSocketServerConnection.connection_id,
            restricted_to_protocols={HttpMessage.protocol_id},
        )
        self.wss_connection = WebSocketServerConnection(
            configuration=self.configuration,
            data_dir=MagicMock(),
            identity=self.identity,
        )
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.wss_connection.connect())
        self.connection_address = str(WebSocketServerConnection.connection_id)
        self._dialogues = HttpDialogues(self.target_skill_id)
        self.original_timeout = self.wss_connection.channel.timeout_window

    @pytest.mark.asyncio
    async def test_http_connection_disconnect_channel(self):
        """Test the disconnect."""
        await self.wss_connection.channel.disconnect()
        assert self.wss_connection.channel.is_stopped

    def _get_message_and_dialogue(
        self, envelope: Envelope
    ) -> Tuple[HttpMessage, HttpDialogue]:
        message = cast(HttpMessage, envelope.message)
        dialogue = cast(HttpDialogue, self._dialogues.update(message))
        assert dialogue is not None
        return message, dialogue

    @pytest.mark.asyncio
    async def test_get_200(self):
        """Test send get request w/ 200 response."""
        request_task = self.loop.create_task(self.request("get", "/pets"))
        envelope = await asyncio.wait_for(self.wss_connection.receive(), timeout=20)
        assert envelope
        incoming_message, dialogue = self._get_message_and_dialogue(envelope)
        message = dialogue.reply(
            target_message=incoming_message,
            performative=HttpMessage.Performative.RESPONSE,
            version=incoming_message.version,
            status_code=200,
            status_text="Success",
            body=b"Response body",
            headers="",
        )
        response_envelope = Envelope(
            to=envelope.sender,
            sender=envelope.to,
            context=envelope.context,
            message=message,
        )
        await self.wss_connection.send(response_envelope)

        response = await asyncio.wait_for(
            request_task,
            timeout=20,
        )

        assert (
            response.status == 200
            and response.reason == "Success"
            and await response.text() == "Response body"
        )

    def teardown(self):
        """Teardown the test case."""
        self.loop.run_until_complete(self.wss_connection.disconnect())
        self.wss_connection.channel.timeout_window = self.original_timeout
