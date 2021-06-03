import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', 'mn-sabatino.com']

cwd = os.getcwd()

CACHES = {
    "default": {
        "BACKEND":
        "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

# django-debug-toolbar will throw an ImproperlyConfigured exception if DEBUG is
# ever turned on when run with a WSGI server
# DEBUG_TOOLBAR_PATCH_SETTINGS = False

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_NAME', ''),
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('POSTGRES_SERVICE_HOST', ''),
    }
}


# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# SECURE_BROWSER_XSS_FILTER = True


sentry_sdk.init(
    dsn="https://0a3f6f6baa244cb2af4fc5d639ade616@o739364.ingest.sentry.io/5785725",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)



try:
    from .local import *
except ImportError:
    pass
