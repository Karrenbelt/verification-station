#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)

# Navigate to the 'python' directory within the repository
cd "$REPO_ROOT/python"

# Remove the agent folder if it exists
TARGET_FOLDER="$REPO_ROOT/python/oracle_verifier"
[ -d "$TARGET_FOLDER" ] && rm -rf "$TARGET_FOLDER"

# Fetch the agent from the local packages directory
aea fetch zarathustra/oracle_verifier --local

# Navigate to the project directory
cd oracle_verifier

# Install agent dependencies
aea install

# Create a key for the agent
aea generate-key ethereum && aea add-key ethereum

# Issue certificates for the Libp2p connection
aea issue-certificates

# and run the agent
aea run
