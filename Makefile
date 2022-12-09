.DEFAULT_GOAL := install

install:
	python3 setup.py install

clean:
	rm -rf .pytest_cache
	rm -rf aoc.egg-info
	rm -rf build
	rm -rf dist