#!/bin/sh
set -e

python3 manage.py makemigrations paranuara
python3 manage.py migrate
python3 manage.py shell < loaddata.py
python3 manage.py collectstatic --noinput

exec "$@"