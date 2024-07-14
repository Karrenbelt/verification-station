.PHONY: default
default:
	@$(MAKE) -s new_env
	@$(MAKE) -s scripts

.PHONY: new_env
new_env:
	@[ -n "$$(poetry run which python)" ] && source $$(poetry env info --path)/bin/activate && poetry env remove $$(which python) || true
	poetry install
	@[ -n "${VIRTUAL_ENV}" ] || exec poetry shell

.PHONY: test
test:
	pytest -rfE --doctest-modules tests/ --cov=verification_station --cov-report=html --cov-report=term --cov-report=term-missing

.PHONY: format
format:
	@poetry run ruff check --select I --fix .
	@poetry run ruff format .

.PHONY: lint
lint:
	@poetry run ruff check .

.PHONY: run
run:
	@poetry run ../scripts/run_agent.sh

.PHONY: hashes
hashes:
	poetry run autonomy packages lock
	poetry run autonomy push-all
	git add packages
	git commit -m 'hashes'


.PHONY: clean
clean: clean-build clean-pyc clean-test clean-docs

.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr deployments/build/
	rm -fr deployments/Dockerfiles/open_aea/packages
	rm -fr pip-wheel-metadata
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	find . -name '*.svn' -exec rm -fr {} +
	find . -name '*.db' -exec rm -fr {} +
	rm -fr .idea .history
	rm -fr venv

.PHONY: clean-docs
clean-docs:
	rm -fr site/

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.DS_Store' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -fr .tox/
	rm -f .coverage
	find . -name ".coverage*" -not -name ".coveragerc" -exec rm -fr "{}" \;
	rm -fr coverage.xml
	rm -fr htmlcov/
	rm -fr .hypothesis
	rm -fr .pytest_cache
	rm -fr .mypy_cache/
	find . -name 'log.txt' -exec rm -fr {} +
	find . -name 'log.*.txt' -exec rm -fr {} +


.PHONY: scripts
	@chmod +x scripts/*
