"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG = (bool, False)
)

environ.Env.read_env(BASE_DIR / '.env')
DEBUG = env('DEBUG')
if DEBUG:
    SECRET_KEY = env('SECRET_KEY')
    DATABASES = {'default': env.db()}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from ._apps import INSTALLED_APPS, MIDDLEWARE

ROOT_URLCONF = 'config.urls'

from ._media import TEMPLATES

WSGI_APPLICATION = 'config.wsgi.application'

from ._auth import AUTH_PASSWORD_VALIDATORS

from ._formats import *

from ._media import *
