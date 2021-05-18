MS website as Product Manager
------------------------------

### Create virtual environment

```python
python3 -m pip install --user virtualenv
python3 -m venv wbmanu
```

Activate virtual env

```python
source wbmanu/bin/activate
```

Deactivate virtual env

```python
deactivate
```

### How to install wagtail

```python
pip install wagtail
wagtail start manuciaocv
cd manuciaocv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Use SCSS/SASS in my django project

```js
nvm install 0.35.3
npm init
```

To create package.json

```js
npm init
```

Then, please install node-sass package using npm, node-sass is a tool which can help us combine SCSS to CSS

```js
npm install node-sass
npm install bootstrap
```

### To run NVM

run in one terminal these commands:

```js
npm install    (it will install the node modules locally)
npm run build  (it will update the frontend locally)
npm run watch-sass (to watch the changes to the sass files)
```

and in another one:

```sh
source wbmanu/bin/activate
python manage.py runserver
```

### Update the Website Style LOCALLY

If you want to update the stylesheet of the website remember to update the relative SCSS files and run:

before running npm v.8.11.4 update the bashrc as it has been referred above.

```sh
npm run build
python manage.py collectstatic --no-input
```

### Migrate Wagtail Application Database from SQLite to PostgreSQL

*Step 1: Dump existing data to a file*

Dump data from SQLite3 to a json file as shown below, where datadump.json is the file:
python3 manage.py dumpdata > datadump.json

*Step 2: Configure Settings to point to postgresql database*

Assuming you have created an empty postgresql database, edit base.py and change database settings to :

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<database_name>',
            'USER': '<database_user>',
            'PASSWORD': '<password>',
            'HOST': '<host>',
            'PORT': <port>,
        }
    }

*Step 3: Install Psycopg2*

    sudo apt-get install libpq-dev python-psycopg2pip install psycopg2

*Step 4: Migrate database tables*

Ensure you can connect to your postgresql database then migrate:

    python3 manage.py migrate --run-syncdb

ref:

- [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [https://github.com/AccordBox/django-heroku-docker](https://github.com/AccordBox/django-heroku-docker)
- [https://www.accordbox.com/blog/how-use-scsssass-your-django-project-npm-way/](https://www.accordbox.com/blog/how-use-scsssass-your-django-project-npm-way/)
- [https://medium.com/@ochieng.grace/migrate-wagtail-application-database-from-sqlite-to-postgresql-32f705f2f5f4](https://medium.com/@ochieng.grace/migrate-wagtail-application-database-from-sqlite-to-postgresql-32f705f2f5f4)
