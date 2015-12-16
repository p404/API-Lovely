#!/bin/sh
echo Running migrations.
cd /djangoapp && python3 manage.py migrate
echo Generating static files.
python3 manage.py collectstatic --noinput