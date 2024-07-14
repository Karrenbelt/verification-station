-include .env

.PHONY:	deployStatus printNetworkArgs

help:
	@echo "Usage:"
	@echo "  make deploy [ARGS=...]\n    example: make deploy ARGS=\"--network ethereumSepolia\""

FOUNDRY_NETWORK_ARGS :=		# empty by default

# Add more network options here
ifeq ($(findstring --network anvil,$(ARGS)),--network anvil)
	FOUNDRY_NETWORK_ARGS := --rpc-url $(ANVIL_RPC_URL) \
		--keystore .keystore \
		-vv
else ifeq ($(findstring --network ethereumSepolia,$(ARGS)),--network ethereumSepolia)
	FOUNDRY_NETWORK_ARGS := --rpc-url $(ETHEREUM_SEPOLIA_RPC_URL) \
		--keystore .keystore \
		-vv
endif

deployStatus:
	@forge script script/DeployStatus.s.sol:Deploy $(FOUNDRY_NETWORK_ARGS)

printNetworkArgs:
	@echo $(FOUNDRY_NETWORK_ARGS)
