test_label = ""

.PHONY: clean run-dev run lint autopep8 install build build-base

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

run-dev:
	export FLASK_ENV=development && export FLASK_APP=app && flask run --host 0.0.0.0 --port 7000

run:
	gunicorn -c runtime/gunicorn.py "wsgi:app"

lint:
	flake8 .

autopep8:
	autopep8 --in-place --recursive .

shell:
	export FLASK_ENV=development && python3 command.py shell

task:
	celery worker -A tasks -P gevent --loglevel=DEBUG

install:
	python3 -m pip install --no-cache-dir -r requirements.txt -i http://mirrors.sangfor.org/pypi/web/simple --extra-index-url http://mirrors.sangfor.org/sfpypi/simple --trusted-host mirrors.sangfor.org

install-test:
	python3 -m pip install --no-cache-dir -r test-requirements.txt -i http://mirrors.sangfor.org/pypi/web/simple --trusted-host mirrors.sangfor.org

build-env-base:
	docker build -f docker/Dockerfile.env.base -t mirrors.sangfor.org/sf/sf-artifacts/server:envbase . --network host

build-base:
	docker build -f docker/Dockerfile.base -t mirrors.sangfor.org/sf/sf-artifacts/server:base . --network host

build:
	docker build -f docker/Dockerfile -t mirrors.sangfor.org/sf/sf-artifacts/server:latest .; \
	if [ -n "${tag}" ]; then \
		echo "Tag latest to ${tag}"; \
		docker tag mirrors.sangfor.org/sf/sf-artifacts/server:latest mirrors.sangfor.org/sf/sf-artifacts/server:${tag}; \
	fi

init:
	python3 command.py init-db

dbseed:
	python3 command.py dbseed

migrate:
	python3 command.py migrate

test:
	export FLASK_ENV=test && python -m pytest --tb=line -vx -m ${test_label} tests

test-api:
	export FLASK_ENV=test && python -m pytest  --tb=line -v --pyargs tests.test_api

test-debug:
	export FLASK_ENV=test && python3 -m pytest -v --lf --pdb tests
