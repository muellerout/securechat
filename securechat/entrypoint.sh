#!/bin/ash

echo "~~> Running tests..."
pytest

echo "~~> Applying database migrations..."
python manage.py makemigrations && python manage.py migrate

echo "~~> Starting celery..."
celery -A securechat worker --detach

echo "~~> Creating superuser if absent"
python manage.py createsuperuser --noinput

echo "~~> Running django server"
python manage.py runserver 0.0.0.0:8000

exec "$@"