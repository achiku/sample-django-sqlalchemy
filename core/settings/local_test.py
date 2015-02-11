# -*- coding: utf-8 -*-
from core.settings.common import *  # NOQA


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENVIRONMENT = 'development'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

# https://docs.djangoproject.com/en/dev/topics/testing/overview/#speeding-up-the-tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

try:
    from core.settings.local import *  # NOQA
except ImportError:
    pass
