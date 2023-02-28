PORT ?= 5000
TAG ?= auto_labelling_api
WORKERS ?= 4
TIMEOUT ?= 600
LOGLEVEL ?= INFO

start:
	@make stop
	@make build
	@make run

run:
	docker run -it -e LOGLEVEL=$(LOGLEVEL) -e TIMEOUT=$(TIMEOUT) -e WORKERS=$(WORKERS) -e DEEPL_API_KEY="$(DEEPL_API_KEY)" -e PORT=$(PORT) -p $(PORT):$(PORT) --name $(TAG) --rm $(TAG)

build:
	docker build . --compress --tag $(TAG)

bash:
	docker run -it -e DEEPL_API_KEY="$(DEEPL_API_KEY)" --rm $(TAG) /bin/bash

stop:
	docker stop $(TAG) > /dev/null 2>&1 || true
