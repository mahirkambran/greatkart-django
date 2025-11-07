#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

## Ensure media directory exists (useful when Render mounts a persistent disk)
if [ -n "$MEDIA_ROOT" ]; then
	mkdir -p "$MEDIA_ROOT"
	chmod -R 775 "$MEDIA_ROOT" || true
fi

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate