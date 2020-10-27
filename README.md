# Django-Training

## How to Run
> python manage.py runserver

## Getting Started

1. Install django `python -m pip install Django`
2. Install rest framework `pip install djangorestframework`
3. Install postgresql driver `pip install psycopg2`
4. Install pyjwt pyjwt `pip install pyjwt`
5. Migrations :
````
    - python manage.py makemigrations ecommerce
    - python manage.py migrate
````


## Config Database

We use [**postgresql**](https://www.postgresql.org/) as our database, in your `settings.py` :
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your DB name',
        'USER': 'Your postgre username',
        'PASSWORD': 'Your postgre password',
        'HOST': 'localhost'
    }
}
````
