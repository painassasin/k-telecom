#!/bin/sh

echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  echo "MySQL is unavailable - sleeping"
  sleep 0.5
done

echo "MySQL started"


python manage.py db init
python manage.py db migrate
python manage.py db upgrade

python manage.py runserver --host 0.0.0.0 --port 5000

