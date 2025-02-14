# MS website as Product Manager

## Create virtual environment

```py
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

## How to install wagtail

```python
pip install wagtail
wagtail start manuciaocv
cd manuciaocv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Use SCSS/SASS in my django project

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

## To run NVM

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

## Update the Website Style LOCALLY

If you want to update the stylesheet of the website remember to update the relative SCSS files and run:

before running npm v.8.11.4 update the bashrc as it has been referred above.

```sh
npm run build
python manage.py collectstatic --no-input
```

## Migrate Wagtail Application Database from SQLite to PostgreSQL

### Step 1: Dump existing data to a file

Dump data from SQLite3 to a json file as shown below, where datadump.json is the file:
python3 manage.py dumpdata > datadump.json

### Step 2: Configure Settings to point to postgresql database

Assuming you have created an empty postgresql database, edit base.py and change database settings to :

```sh
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
```

### Step 3: Install Psycopg2

```sh
sudo apt-get install libpq-dev python-psycopg2pip install psycopg2
```

### Step 4: Migrate database tables

Ensure you can connect to your postgresql database then migrate:

```sh
python3 manage.py migrate --run-syncdb
```

## Dump Postgres database

```sh
pg_dump --host localhost --dbname msdb --file msdb.dump --format=custom --username postgres
```

## Restore Postgres database

```sh
pg_restore --verbose --clean --no-acl --no-owner --host localhost --dbname  msdb -U postgres msdb.dump
```

## Squash migrations

```py
./manage.py squashmigrations home 0003 0025
./manage.py squashmigrations flex 0003 0009
```

## How to migrate by app

```py
python manage.py migrate home
python manage.py migrate flex
python manage.py migrate site_settings
python manage.py migrate
```

## Create new app within the project

```py
python manage.py startapp <name>
```

Add the new app to the `manuciaocv/settings/base.py`

Clean up the app by removing files that you don't need for the wagtail project, leave only:

- the migrations folder
- apps
- models

## Debug toolbar

Most popular debug toolbars `django debug toolbar` and `pudb`

```py
pip install django-debug-toolbar

pip install pudb
## add on the code that you wish to debug
import pudb; pu.db()
```

## How to Black your python files

Black can reformat your entire file in place according to the Black code style. It helps your brain focus on the problem you want to solve and code solutions, rather than getting distracted by code structure and minor stylistic differences.

Black can be installed by running `pip install black`

## Change Number of Characters per Line

Note that Black defaults to 88 characters for its line length, but you can change that using the “-l” or “- -line-length” option.

For example, to change to 60 characters: `black -l 60 python_file.py`

## Install all the required libraries for dev environment

Install all the base requirements and the extra dev requirements

```sh
pip install -r dev.txt
```

## Where to get wagtail icons

[A List of Wagtail StreamField Icons](https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html)

## Use .env to hide your secret keys:

[How To Harden the Security of Your Production Django Project](https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project)

## If .gitignore does not remove files/folder

The `.gitignore` file ensures that files not tracked by Git remain untracked.

Just adding folders/files to a `.gitignore` file will not untrack them -- they will remain tracked by Git.

To untrack files, it is necessary to remove from the repository the tracked files listed in `.gitignore` file. Then re-add them and commit your changes.

The easiest, most thorough way to do this is to remove and cache all files in the repository, then add them all back. All folders/files listed in `.gitignore` file will not be tracked. From the top folder in the repository run the following commands:

```sh
git rm -r --cached .
```

## Deploy on Digital Ocean

- Buy a Google Domain
- Get an ubuntu server on Digital Ocean (so called Droplet)
- Add SSH key
- Update the google domain DNS with the Digital Ocean DNS [Registrar: Google Domains](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Check Digital Ocean [DNS Lookup](https://www.digitalocean.com/community/tools/dns)

- Root into the ubuntu server by typing on the terminal

```sh
ssh root@mn-sabatino.com
```

- Create new user on the ubuntu server and make it sudo user

```sh
adduser manuciao
usermod -aG sudo manuciao
```

- Allow OpenSSH to work on the ubuntu server

```sh
ufw app list
ufw allow OpenSSH
ufw enable -y
ufw status
```

- copy over the SSH

```sh
rsync --archive --chown=manuciao:manuciao ~/.ssh /home/manuciao
```

- Access the ubuntu server with the new user

```sh
ssh manuciao@mn-sabatino.com
```

- Update Ubuntu

```sh
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl 
```

- Log into a postgres session and create db (postgres 13.2)

```sh
sudo -u postgres psql

# Create a new database
create database msdb;
CREATE USER manuciao WITH PASSWORD 'your_postgres_password';
ALTER ROLE manuciao SET client_encoding TO 'utf8';
ALTER ROLE manuciao SET default_transaction_isolation TO 'read committed';
ALTER ROLE manuciao SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE msdb TO manuciao;
```

- Upgrade pip and install virtualenv

```sh
sudo -H pip3 install --upgrade pip && sudo -H pip3 install virtualenv
```

- Create a new project directory

```sh
mkdir ~/ms_website && cd ~/ms_website
```

- Clone your project from github into this directory (Add the "." at the ed it will add all the files in that folder)

```sh
git clone https://github.com/ManuCiao/ms_website.git .
git config pull.ff only
```

- Run the following commands:

```sh
sudo apt install python3.9-venv
python3 -m venv wbmanu
source wbmanu/bin/activate
pip freeze
pip install gunicorn psycopg2-binary
pip install -r requirements.txt
python manage.py collectstatic --settings=manuciaocv.settings.production
sudo apt install npm
npm install
npm run build

export DJANGO_SETTINGS_MODULE='manuciaocv.settings.production'
echo $DJANGO_SETTINGS_MODULE
python manage.py runserver 0.0.0.0:8000
python manage.py migrate home
python manage.py migrate flex
python manage.py migrate
python manage.py createsuperuser
sudo ufw allow 8000
sudo ufw status
python manage.py runserver 0.0.0.0:8000

# go to your browser using your IP address from Digital Ocean:
http://mn-sabatino.com:8000/

# to transfer the db dump from your local machine to remote machine
rsync /path/to/local/file username@PCB:/path/to/remote/destination
rsync '/home/dev01/Downloads/Personal/website/theme_portfolio_cv/ms_website/msdb.dump' manuciao@mn-sabatino.com:/home/manuciao/ms_website
rsync '/home/dev01/Downloads/Personal/website/theme_portfolio_cv/ms_website/.env' manuciao@mn-sabatino.com:/home/manuciao/ms_website
rsync -a '/home/dev01/Downloads/Personal/website/theme_portfolio_cv/ms_website/media' manuciao@mn-sabatino.com:/home/manuciao/ms_website

rsync '/home/dev01/Downloads/Personal/website/theme_portfolio_cv/ms_website/manuciaocv/settings/local.py' manuciao@mn-sabatino.com:/home/manuciao/ms_website/manuciaocv/settings/

# restore db from pg_dump
pg_restore --verbose --clean --no-acl --no-owner --host localhost --dbname  msdb -U manuciao msdb.dump


# Run gunicorn on port 8000
gunicorn --bind 0.0.0.0:8000 manuciaocv.wsgi 
deactivate
sudo nano /etc/systemd/system/gunicorn.socket

# Add this to the file `/etc/systemd/system/gunicorn.socket`:
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

# Create a systemd file for gunicorn with sudo privileges
sudo nano /etc/systemd/system/gunicorn.service
# And add this into it:

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=manuciao
Group=www-data
WorkingDirectory=/home/manuciao/ms_website
ExecStart=/home/manuciao/ms_website/wbmanu/bin/gunicorn \
        --access-logfile - \
        --workers 3 \
        --bind unix:/run/gunicorn.sock \
        manuciaocv.wsgi:application

[Install]
WantedBy=multi-user.target

#  Start and enable the gunicorn
sudo systemctl start gunicorn.socket && sudo systemctl enable gunicorn.socket 
sudo systemctl status gunicorn.socket

# Check the existence of the new socket file
file /run/gunicorn.sock 

# Check the gunicorn status with
sudo systemctl status gunicorn # You should see INACTIVE DEAD
# Test the socket activation with a curl command
curl --unix-socket /run/gunicorn.sock localhost
# Reload gunicorn
sudo systemctl daemon-reload && sudo systemctl restart gunicorn

# Create a new server block in nginx
sudo nano /etc/nginx/sites-available/ms_website 
# And add this:

server {
    listen      80;
    listen      [::]:80;
    server_name mn-sabatino.com;
    charset     UTF-8;

    error_log   /home/manuciao/ms_website/nginx-error.log;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/manuciao/ms_website/static/;
    }

    location /media/ {
        alias /home/manuciao/ms_website/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}


# Create a file by linking it to the sites-enabled directory
sudo ln -s /etc/nginx/sites-available/ms_website /etc/nginx/sites-enabled
# Test nginx with:
sudo nginx -t
# If there were no errors, restart nginx
sudo systemctl restart nginx 
sudo systemctl status nginx  #to see that it is running

# Open the firewall to normal traffic with Nginx, and delete port 8000
sudo ufw delete allow 8000 && sudo ufw allow 'Nginx Full'
sudo ufw status
# If NGINX shows the welcome to nginx page, double check your server_name ip in your nginx config file (the one we created earlier). Add your IP to your domain DNS. When launching your website update your nginx settings
sudo nano /etc/nginx/sites-available/manuciao
# Replace 167.172.xxx.xx with yourwebsite.com
# Test nginx settings with
sudo nginx -t
# Restart nginx with
sudo systemctl restart nginx 
sudo systemctl restart gunicorn
sudo systemctl restart postgresql

# kill all postgres connection if it is stuck
SELECT
	pg_terminate_backend(pg_stat_activity.pid)
FROM
	pg_stat_activity
WHERE
	pg_stat_activity.datname = 'msdb'
	AND pid <> pg_backend_pid();

sudo tail -F /home/manuciao/ms_website/nginx-error.log


# report error permission denied for nginx
sudo nano /etc/nginx/nginx.conf 
# By default `nginx.conf` user is `www-data`.

user www-data;
worker_processes auto;
pid /run/nginx.pid;

# Then I replaced with my sudo user and solved my problem. 😀
user manuciao;
worker_processes auto;
pid /run/nginx.pid;

# Then I restart nginx, gunicorn and postgresql
sudo systemctl restart nginx 
sudo systemctl restart gunicorn
sudo systemctl restart postgresql

# Add 167.172.xxx.xx to your domain DNS settings and wait for it to propogate. View your new website at yourwebsite.com
# Update the wagtail site settings
# Go to http://yourwebsite.com/admin/sites/2/ and: change localhost to yourwebsite.com 

# Add www.yourwebsite.com and SSL
sudo nano /etc/nginx/sites-available/ms_website

server {
    listen      80;
    listen      [::]:80;
    server_name mn-sabatino.com www.mn-sabatino.com;
    charset     UTF-8;

# To avoid a possible hash bucket memory problem that can arise from adding additional server names
sudo nano /etc/nginx/nginx.conf

http {
    ...
    server_names_hash_bucket_size 64;
    ...
}


sudo nginx -t
sudo systemctl restart nginx

# Add SSL to your website with let's encrypt
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d mn-sabatino.com -d www.mn-sabatino.com
sudo systemctl status certbot.timer
sudo certbot renew --dry-run
#Since Let’s Encrypt certificates expire every 90 days, Nginx recommends setting up and automatic renewal cron job.
#1. First, open the crontab configuration file for the current user:
crontab -e
#2. Add a cron job that runs the certbot command, which renews the certificate if it detects the certificate will expire within 30 days. Schedule it to run daily at a specified time (in this example, it does so at 05:00 a.m.):
0 5 * * * /usr/bin/certbot renew --quiet
 #You can now go to [ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/analyze.html?d=mn%2dsabatino.com&latest) and run an SSL test on your domain.


## TO UPDATE THE SERVER
Pull all the .env and .local files from local machine `rsync <local path> <remote path>`
Pull github repo `git pull`
Restart nginx and gunicorn `sudo systemctl restart nginx` `sudo systemctl restart gunicorn`
Update `.local` file with the .env details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_NAME', ''),
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('POSTGRES_SERVICE_HOST', ''),
    }
}

```

- Follow this [tutorial](https://learnwagtail.com/launch-your-wagtail-website-digital-ocean-ubuntu-18/)
- Follow this [Digital ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)
- Follow this [Nginx server block](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04#step-5-%E2%80%93-setting-up-server-blocks-(recommended))
- Follow this [Let's Encrypt](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)

-----------------------------------------------------------------------

## TODO list

- Add Redis as Cache server
- Improve Contact form
- Split CSS style into SASS files per block
- Ansible script to deploy app
- Dockerise
- Create personal logo
- Add more projects

-----------------------------------------------------------------------
## Reference

- [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [https://github.com/AccordBox/django-heroku-docker](https://github.com/AccordBox/django-heroku-docker)
- [https://www.accordbox.com/blog/how-use-scsssass-your-django-project-npm-way/](https://www.accordbox.com/blog/how-use-scsssass-your-django-project-npm-way/)
- [https://medium.com/@ochieng.grace/migrate-wagtail-application-database-from-sqlite-to-postgresql-32f705f2f5f4](https://medium.com/@ochieng.grace/migrate-wagtail-application-database-from-sqlite-to-postgresql-32f705f2f5f4)
- [https://project-awesome.org/springload/awesome-wagtail](https://project-awesome.org/springload/awesome-wagtail)
-[https://docs.wagtail.io/en/stable/](https://docs.wagtail.io/en/stable/)

-----------------------------------------------------------------------
