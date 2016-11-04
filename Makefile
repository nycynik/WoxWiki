.PHONY = init migrate upgrade debug

debug:
	python3 run.py

init:
	python3 manage.py db init

migrate:
	python3 manage.py db migrate

upgrade:
	python3 manage.py db upgrade
