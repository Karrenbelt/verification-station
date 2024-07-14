-include .env

.PHONY:	deployStatus

help:
	@echo "Usage:"
	@echo "  make deploy [ARGS=...]\n    example: make deploy ARGS=\"--network ethereumSepolia\""

FOUNDRY_NETWORK_ARGS :=		# empty by default
BROADCAST :=				# empty by default

# Add more network options here
ifeq ($(findstring --network anvil,$(ARGS)),--network anvil)
	FOUNDRY_NETWORK_ARGS := --rpc-url $(ANVIL_RPC_URL) \
		--private-key $(ANVIL_PRIVATE_KEY) \
		-vv
else ifeq ($(findstring --network ethereumSepolia,$(ARGS)),--network ethereumSepolia)
	FOUNDRY_NETWORK_ARGS := --rpc-url $(ETHEREUM_SEPOLIA_RPC_URL) \
		--keystore .keystore \
		-vv
endif

# Only send transaction if --broadcast is passed as an argument
# If --broadcast is not passed, the deploy scripts will run in dry-run mode
ifeq ($(findstring --broadcast,$(ARGS)),--broadcast)
	BROADCAST := --broadcast
endif

# deployStatus: Deploy the Status contract.
# 	Specify the address to grant the owner role to by setting the OWNER environment variable.
# 	Example: make deployStatus ARGS="..." OWNER="0x1234..."
deployStatus:
	@forge script script/DeployStatus.s.sol:Deploy $(FOUNDRY_NETWORK_ARGS)
