.PHONY: yapf lint clean sync lock test package test-release release

yapf:
	pipenv run yapf -vv -ir .
	pipenv run isort -y

lint:
	pipenv run flake8 .
	pipenv run pydocstyle .
	pipenv run mypy .

clean:
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

sync:
	pipenv sync --dev

lock:
	pipenv lock --dev 

test:
	pipenv run pytest tests/

package:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel

test-release: package
	pipenv run twine upload --repository-url https://test.pypi.org/legacy/dist/*

release: package
	pipenv run twine upload dist/*
