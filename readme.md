django-admin startproject demo

cd demo

python3 manage.py startapp myapp

modify installed_apps in demo/settings.py add "myapp"

in my_app created urls.py

python3 manage.py runserver

if change in database, models.py :
    python3 manage.py makemigrations
    python3 manage.py migrate

python3 manage.py createsuperuser


