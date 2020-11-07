from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','128.199.28.172','snehahouseholds.in','www.snehahouseholds.in']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS



DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return False


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_51HgdA5Jrj3iHiajpXCGHk3IEN19uK47W57iTE9Ku1vK1dDLt4v7jJkIrzFVyAJQ6N2kcakCVMjPG3akVTrpuNrmX00DR50eQPO'
STRIPE_SECRET_KEY = 'sk_test_51HgdA5Jrj3iHiajpXCjB6MKqWvJtC21RK4XmXXhC07hnHgiC0NYjnYX2tJkDnr4m2EIJpXSpuQNXLzjpx99qD0Gb007dDY9Eid'
