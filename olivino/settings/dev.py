from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%0)^irzangk6&kq_)23y#ge#8@$)9&*%q-#&@41!8*p_-!@@b'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': u'olivinostg',
        'HOST': u'rds2.dyna-code.com',
        'USER': u'olivino',
        'PASSWORD': u'76eldorado',
        'PORT': 3306}
}

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass

# debug_toolbar settings
#def show_always(request):
#    return True

INTERNAL_IPS = ('127.0.0.1',)

#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)

#INSTALLED_APPS += (
#    'debug_toolbar',
#)

#DEBUG_TOOLBAR_PANELS = [
#    'debug_toolbar.panels.versions.VersionsPanel',
#    'debug_toolbar.panels.timer.TimerPanel',
#    'debug_toolbar.panels.settings.SettingsPanel',
#    'debug_toolbar.panels.headers.HeadersPanel',
#    'debug_toolbar.panels.request.RequestPanel',
#    'debug_toolbar.panels.sql.SQLPanel',
#    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#    'debug_toolbar.panels.templates.TemplatesPanel',
#    'debug_toolbar.panels.cache.CachePanel',
#    'debug_toolbar.panels.signals.SignalsPanel',
#    'debug_toolbar.panels.logging.LoggingPanel',
#    'debug_toolbar.panels.redirects.RedirectsPanel',
#]

#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#    'SHOW_TOOLBAR_CALLBACK': show_always,
#}

#DEBUG_TOOLBAR_PATCH_SETTINGS = False
