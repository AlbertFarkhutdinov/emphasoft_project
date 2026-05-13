uv run clean_db.py
uv run manage.py makemigrations auth_app
uv run manage.py migrate
uv run manage.py fill_db
uv run manage.py runserver
pause