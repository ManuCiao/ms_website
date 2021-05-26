import os
from .base import *

DEBUG = False


cwd = os.getcwd()

CACHES = {
    "default": {
        "BACKEND":
        "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}


try:
    from .local import *
except ImportError:
    pass
