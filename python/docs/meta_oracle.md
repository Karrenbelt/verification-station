# Oracle interface

The interface defines the meta framework for the oracle.

Each custom component must implement the following methods:

- `collect_data`: Generate the params call to the Contract Api.
- `verify_data`: verify the data given the response from the Contract Api.
- `challenge_data`: Challenge the data given the response from the Contract Api in case of a dispute.
