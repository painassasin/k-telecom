#!/bin/sh
# this script is used to boot a Docker container
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 3 secs...
    sleep 3
done
flask fixtures load