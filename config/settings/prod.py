import os
import environ
import dj_database_url
from .base import *


ADMINS = (("Eyong Kevin", "tonyparkerkenz@gmail.com"),)
env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1", "0.0.0.0"]
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://127.0.0.1",
    "https://0.0.0.0",
    "https://gd-team-app.herokuapp.com",
]

MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"] + MIDDLEWARE

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),  # database name
        "USER": env.str("DB_USER"),  # database user
        "PASSWORD": env.str("DB_PWD"),  # database password
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

import django_on_heroku

django_on_heroku.settings(locals())
