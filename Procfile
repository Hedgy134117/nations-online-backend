release: python nationsOnline/manage.py makemigrations --no-input
release: python nationsOnline/manage.py migrate --no-input
release: cd nationsOnline
release: python manage.py test --no-input
release: cd ../

web: gunicorn --chdir nationsOnline nationsOnline.wsgi