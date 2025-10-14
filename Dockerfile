# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user
ARG UID=10001

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install dependencies
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy project files AFTER installing dependencies
COPY . ./
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
COPY db.sqlite3 /app/db.sqlite3
RUN chown appuser:appuser /app/db.sqlite3 && chmod 664 /app/db.sqlite3
# Ensure the app directory and the sqlite file are writable by the appuser
RUN chown -R appuser:appuser /app \
    && chmod 775 /app \
    && [ -f /app/db.sqlite3 ] && chown appuser:appuser /app/db.sqlite3 && chmod 664 /app/db.sqlite3 || true

# Collect static files
RUN python manage.py collectstatic --noinput

# Switch to non-privileged user
USER appuser

EXPOSE 8000

# Start the app
CMD ["gunicorn", "chef_site.wsgi", "--bind=0.0.0.0:8000"]