.PHONY: manage
manage:
	poetry run python -m django_template.manage

.PHONY: setup-devenv
setup-devenv:
	python -m venv .venv; \
	./venv/bin/activate; \
	poetry install; \
	poetry run pre-commit install;
