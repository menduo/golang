default:
	ls -l

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

deps:
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

build:
	python setup.py sdist bdist_wheel

publish-prod: clean deps build
	twine upload dist/*

install_local:
	pip install .[dev]


publish-test: clean
	MDVEREND=`date +%Y%m%d%H%M%S` python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
