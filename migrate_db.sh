#!/bin/bash
cd /var/app/current
source /var/app/venv/*/bin/activate
export SECRET_KEY='django-insecure-your-secret-key-here'
export DEBUG=False
export EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
export EMAIL_HOST='localhost'
export EMAIL_PORT=587
export EMAIL_HOST_USER=''
export EMAIL_HOST_PASSWORD=''
export EMAIL_USE_TLS=True
export DEFAULT_FROM_EMAIL='noreply@greatkart.com'
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
echo "Migrations completed successfully!"

