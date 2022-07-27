all: install test format build

install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

format:
	poetry run black translator_template

update:
	poetry update
	poetry export -f requirements.txt --output requirements.txt
