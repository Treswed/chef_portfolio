# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

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

# Collect static files
RUN python manage.py collectstatic --noinput

# Switch to non-privileged user
USER appuser

EXPOSE 8000

# Start the app
CMD ["gunicorn", "chef_site.wsgi", "--bind=0.0.0.0:8000"]