default:
	ls -l


publish-prod:
	python setup.py sdist upload

install_local:
	pip install .[dev]

