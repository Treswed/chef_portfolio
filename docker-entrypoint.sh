#!/bin/sh
# Entry point for the web container.
# Ensures the directory for SQLITE_PATH exists and attempts to set permissions,
# runs migrations, creates superuser, then starts gunicorn.

set -e

SQLITE_PATH=${SQLITE_PATH:-/data/db.sqlite3}
SQLITE_DIR=$(dirname "$SQLITE_PATH")

echo "[entrypoint] using SQLITE_PATH=$SQLITE_PATH"
echo "[entrypoint] ensuring directory $SQLITE_DIR exists"
mkdir -p "$SQLITE_DIR" || true

echo "[entrypoint] attempting to set permissive permissions on $SQLITE_DIR"
chmod 0777 "$SQLITE_DIR" || true

echo "[entrypoint] running Django migrations"
python manage.py migrate

echo "[entrypoint] creating Django superuser if not exists"
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'sensei'
email = 'sensei@gmail.com'
password = 'sensei1234'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
END

echo "[entrypoint] starting gunicorn"
exec gunicorn 'chef_site.wsgi' --bind=0.0.0.0:8000