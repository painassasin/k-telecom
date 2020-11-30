#!/bin/sh

echo "Waiting for MySQL..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "MySQL started"

python manage.py create_tables
python manage.py create_seed

exec "$@"
