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
	@poetry run sam build -t ../templates/template.local.$(architecture).yaml

.PHONY: invoke
invoke:
	@poetry run sam local invoke -t .aws-sam/build/template.yaml -e ../events/event.json --env-vars ../environments/env.json --force-image-build

.PHONY: local-run
local-run:
	@make build && make invoke
