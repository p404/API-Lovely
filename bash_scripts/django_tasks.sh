#!/bin/sh
echo Running migrations.
cd /djangoapp && python3 manage.py migrate
