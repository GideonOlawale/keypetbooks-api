'''Use this for production'''

from .base import *
import dj_database_url


DEBUG = False
DATABASES = {'default': dj_database_url.config('DATABASE_URL')}
ALLOWED_HOSTS += ["*", ".herokuapp.com","https://keypetbooks.herokuapp.com"]
WSGI_APPLICATION = 'core.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CORS_ORIGIN_WHITELIST = (
    "https://keypetbooks.herokuapp.com",
)
CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.herokuapp\.com$",
]
CORS_ORIGIN_ALLOW_ALL = True
