CODE = .
# Add source dir to pythonpath
PYTHONPATH = PYTHONPATH=./:$(CODE)
# Params
DOWNGRADE_DEFAULT = -1

.PHONY: migrations db_upgrade db_downgrade lint format test test-failed test-cov validate

# Actions

lint:
	pylint --jobs 4 --rcfile=setup.cfg $(PACKAGES)
	black --line-length=100 --skip-string-normalization --check $(CODE)
	mypy $(PACKAGES)

format:
	isort --apply --recursive $(CODE)
	black --line-length=100 --skip-string-normalization $(CODE)
	unify --in-place --recursive $(CODE)

validate: lint test
