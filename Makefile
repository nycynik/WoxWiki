.PHONY = init migrate upgrade debug createdb
export FLASK_APP=woxwiki/__init__.py
export FLASK_DEBUG=1;

createdb:
	flask createdb

debug:
	python3 run.py

init:
	python3 manage.py db init

migrate:
	python3 manage.py db migrate

upgrade:
	python3 manage.py db upgrade
