ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
CLEAN_PATTERNS := $(shell awk '/^# Clean$$/{f=1; next} /^# End Clean$$/{f=0} f' .gitignore)

.PHONY: default
default:
	@$(MAKE) -s clean
	@$(MAKE) -s -C python
	@$(MAKE) -s scripts
	cd $$ROOT_DIR

.PHONY: clean
clean:
	@$(foreach pattern,$(CLEAN_PATTERNS), \
		find . -name "$(pattern)" -exec rm -rf {} +; \
	)

.PHONY: scripts
	@chmod +x scripts/*
