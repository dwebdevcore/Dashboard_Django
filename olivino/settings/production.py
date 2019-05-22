from .base import *
from django.core.exceptions import ImproperlyConfigured
from os import environ
import logging

DEBUG = False


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

ALLOWED_HOSTS = ['.olivino.com', '.olivino.com.']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%0)^irzangk6&kq_)23y#ge#8@$)9&*%q-#&@41!8*p_-!@@b'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': u'olivino',
        'HOST': u'rds2.dyna-code.com',
        'USER': u'olivino',
        'PASSWORD': u'76eldorado',
        'PORT': 3306}
}

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'olivino'
    }
}


INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES += (
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
)

RAVEN_CONFIG = {
    'dsn': 'https://81c20024b1094bafad0cec7c85f5661b:3856b6fd3b3242a59588c95049d4fdbf@sentry.io/115733',
}

# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': 'olivino',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/olivino/olivino.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'console',
        },
        'sentry': {
            'level': 'WARNING', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/olivino/django_request.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'console',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False
        },
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

SENTRY_CELERY_LOGLEVEL = logging.INFO
