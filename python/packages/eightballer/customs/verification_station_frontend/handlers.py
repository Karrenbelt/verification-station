"""
Simple handler funtions for the Ui ABCI loader.
"""
import datetime

got_message = datetime.datetime.now().isoformat()

from aea.skills.base import Handler


class PingPongHandler(Handler):
    def setup(self):
        """Set up the handler."""

    def handle(self, msg):
        """Handle the data."""

        breakpoint()
        response = f"Pong @ {got_message}: {msg.data}"
        return response

    def teardown(self):
        """Implement the handler teardown.
        """
