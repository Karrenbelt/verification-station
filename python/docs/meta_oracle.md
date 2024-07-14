# Oracle interface

The interface defines the meta framework for the oracle.

Each custom component must implement the following methods in a `main.py` file:

- `collect_data`: Generate the params call to the Contract Api.
- `verify_data`: verify the data given the response from the Contract Api.
- `challenge_data`: Challenge the data given the response from the Contract Api in case of a dispute.

it must also contain a directory `tests` with the following files:

- `test_main.py`: Test the main methods of the component.

