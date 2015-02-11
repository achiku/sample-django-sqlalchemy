# -*- coding: utf-8 -*-
from core.settings.common import *  # NOQA


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENVIRONMENT = 'development'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from core.settings.local import *  # NOQA
except ImportError:
    pass
