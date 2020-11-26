#!/bin/env bash
>&2 echo "Waiting for MySQL..."
while ! nc -z db 3306; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done
>&2 echo "MySQL started"

#https://github.com/KartikShrikantHegde/Docker-Flask-MySQL/blob/master/docker-entrypoint.sh
#https://github.com/peter-evans/docker-compose-healthcheck/blob/master/docker-compose.yml
#https://stavshamir.github.io/python/dockerizing-a-flask-mysql-app-with-docker-compose/