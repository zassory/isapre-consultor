#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt

echo "from django.contrib.auth.models import User; User.objects.create_superuser('nicolas', 'nicolas.programador@gmail.com', 'Hakxf2n5$')" | python manage.py shell

python manage.py collectstatic --no-input
python manage.py migrate