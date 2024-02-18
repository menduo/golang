default:
	ls -l

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

publish-prod: clean
	python setup.py sdist upload

install_local:
	pip install .[dev]


publish-test: clean
	MDVEREND=`date +%Y%m%d%H%M%S` python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*