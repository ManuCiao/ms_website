import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '603=*(mg4tlpifji+b8s^dnnpy#@ad9l0rd2gw&2l-4i0jz-ur'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Django <no_reply@example.com>'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


## Disable the cache if on develop it slows down the updates, enable it only on production
# cwd = os.getcwd()

# CACHES = {
#     "default": {
#         "BACKEND":
#         "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": f"{cwd}/.cache"
#     }
# }

try:
    from .local import *
except ImportError:
    pass
