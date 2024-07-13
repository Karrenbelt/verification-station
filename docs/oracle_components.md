# Oracle Components

Who Watches the Watchmen?

This is a meta-framework for developing oracle watcher components to be used in the Olas system. This document will outline the necessary components for interfacing with an oracle and the necessary methods that need to be implemented.

## Oracles

Oracles are not ETC TOD

## Oracle Components

Interfacing with an oracle can be done by implementing a custom component for the oracle. This component will be responsible for interfacing with the oracle and providing the data to the Olas system.

The component has 3 necessary methods:

- `get_data()`: This method will be called by the Olas system to get the data from the oracle. This method should return the data in the form of a dictionary.

- `verify_data(data: dict)`: This method will be called by the Olas system to verify the data returned by the oracle. This method should return True if the data is valid, False otherwise.

- `punish()`: This method will be called by the Olas system to punish the oracle if it provides invalid data. This method should be used to penalize the oracle for providing incorrect data.
