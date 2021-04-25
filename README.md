MS website as Product Manager

Create virtual environment

```python 
python3 -m pip install --user virtualenv
python3 -m venv ms_site
```

Activate virtual env
```python 
source ms_site/bin/activate
```

Deactivate virtual env
```python 
deactivate
```

How to install wagtail
```python 
pip install wagtail
wagtail start my_cv
cd my_cv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```



ref: [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)