from .base import *
from typing import Optional
import os
from typing import Optional
import environ

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")


ALLOWED_HOSTS: Optional[list] = []


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


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_ADDRESS = "enowblog@gmail.com"
