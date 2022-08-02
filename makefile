all: install test format build

install:
	poetry install

build:
	poetry build

test:
	poetry run pytest --cov-report term-missing --cov=translator_template

format:
	poetry run black translator_template

update:
	poetry update
	poetry export -f requirements.txt --output requirements.txt
