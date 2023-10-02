# Project configuration
PROJECT_NAME := pypuregym
PACKAGE_NAME := pypuregym
VERSION_FILE := $(PACKAGE_NAME)/__init__.py
SHELL = /bin/zsh

TESTS_DIRECTORY := tests

# Call these functions before/after each target to maintain a coherent display
START_TARGET = @printf "[$(shell date +"%H:%M:%S")] %-40s" "$(1)"
END_TARGET := @printf "\033[32;1mOK\033[0m\n"

.PHONY: help check_pylint check

# generate command list based on the "##" comment marked with the targets
help: ## Display list of targets and their documentation
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
		'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

black:  # Run black to format code
	$(call START_TARGET,Format code with Black)
	@black --line-length 79 $(PACKAGE_NAME)
	$(call END_TARGET)

ruff:  # Run ruff
	$(call START_TARGET,Run Ruff linter)
	@ruff --fix $(PACKAGE_NAME)
	$(call END_TARGET)

check_pylint:  # Run pylint
	$(call START_TARGET,Run Pylint)
	@pylint $(PACKAGE_NAME)
	$(call END_TARGET)

check_black: ## Check if code is well formatted
	$(call START_TARGET,Checking black formatting)
	@black --line-length 79 --check $(PACKAGE_NAME)
	$(call END_TARGET)

check_ruff: ## Check if code is Python compliant
	$(call START_TARGET,Running ruff)
	@ruff check $(PACKAGE_NAME)
	$(call END_TARGET)

.env: ## Build a Python environment
	python -m venv .env
	. .env/bin/activate && \
		pip install -U setuptools wheel pip && \
		pip install -e . && \
		pip install -e '.[dev]'

check: .env  ## Run all checks in the CI environment
	. .env/bin/activate && \
		$(MAKE) check_black && \
		$(MAKE) check_ruff && \
		$(MAKE) check_pylint
