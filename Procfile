release: python nationsOnline/manage.py makemigrations --no-input
release: python nationsOnline/manage.py migrate --no-input
release: python nationsOnline/manage.py test --no-input

web: gunicorn --chdir nationsOnline nationsOnline.wsgi