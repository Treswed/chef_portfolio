#!/bin/sh
# Entry point for the web container.
# Ensures the directory for SQLITE_PATH exists and attempts to set permissions,
# then starts gunicorn.

set -e

SQLITE_PATH=${SQLITE_PATH:-/data/db.sqlite3}
SQLITE_DIR=$(dirname "$SQLITE_PATH")

echo "[entrypoint] using SQLITE_PATH=$SQLITE_PATH"
echo "[entrypoint] ensuring directory $SQLITE_DIR exists"
mkdir -p "$SQLITE_DIR" || true

echo "[entrypoint] attempting to set permissive permissions on $SQLITE_DIR"
chmod 0777 "$SQLITE_DIR" || true

echo "[entrypoint] starting gunicorn"
exec gunicorn 'chef_site.wsgi' --bind=0.0.0.0:8000
