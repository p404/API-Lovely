#!/bin/sh
touch /var/log/gunicorn.log

echo Starting Gunicorn.
cd /djangoapp
exec gunicorn inventory.wsgi \
     --name lovely_api \
     --bind 0.0.0.0:8000 \
     --workers 3 \
     --log-level=info \
     --log-file=/var/log/gunicorn.log