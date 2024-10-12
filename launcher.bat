cd emphasoft\emphasoft
poetry run python clean_db.py
poetry run python manage.py makemigrations auth_app
poetry run python manage.py migrate
poetry run python manage.py fill_db
poetry run python manage.py runserver
pause