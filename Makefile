# Makefile for blurtpy project

.PHONY: test-mac test-linux docs clean

test-mac:
	pipenv run pytest -v

test-linux:
	docker build -f Dockerfile.linux -t blurtpy-linux-test .
	docker run --rm blurtpy-linux-test

docs:
	cd docs && make html

clean:
	rm -rf docs/_build
	rm -rf .pytest_cache .mypy_cache 