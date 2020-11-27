.PHONY: dist

install:
	python setup.py install

test:
	pipenv run pytest test.py

style:
	pipenv run pycodestyle docassemble_textstat/
	pipenv run pycodestyle test.py

clean:
	rm -rf build/ dist/ docassemble_textstat.egg-info/ __pycache__/ */__pycache__/
	rm -f *.pyc */*.pyc

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

