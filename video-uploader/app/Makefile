architecture ?= x86

.PHONY: install
install:
	@pip install poetry && poetry install

.PHONY: lint
lint:
	@poetry run pre-commit

.PHONY: local-environment
local-environment:
	cd ../dockerfiles/ && docker-compose -p aws-local-enviornment up -d --build

.PHONY: build
build:
	@poetry export --without-hashes --only main > requirements.txt && poetry run sam build -t ../templates/template.local.$(architecture).yaml

.PHONY: start-api
start-api:
	@poetry run sam local start-api -t .aws-sam/build/template.yaml

.PHONY: local-run
local-run:
	@make build && make start-api
	