'''Use this for development'''

from .base import *


ALLOWED_HOSTS += ['127.0.0.1:8000','localhost:3000']
DEBUG = True

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.keypet'),
    }
}
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://127.0.0.1:8000"
)
CORS_ORIGIN_ALLOW_ALL = True
