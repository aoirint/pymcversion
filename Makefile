
.PHONY: test
test: pytest mypy

.PHONY: pytest
pytest:
	pytest -s ./tests

.PHONY: mypy
mypy:
	mypy ./pymcversion
