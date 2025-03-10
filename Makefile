
extract:
	pybabel extract --input-dirs=. -o locales/messages.pot
init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
	pybabel init -i locales/messages.pot -d locales -D messages -l rus
compile:
	pybabel compile -d locales -D messages
update:
	pybabel update -d locales -D messages -i locales/messages.pot
web_command:
	uvicorn web.app:app --host localhost --port 8000

mig:
	alembic revision --autogenerate -m "Create a baseline migrations"
upgrade:
	alembic upgrade head
downgrade:
	alembic downgrade head
alembic_init:
	alembic init migrations