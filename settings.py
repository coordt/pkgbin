# Django settings for project project.

import calloway
import os
import sys

CALLOWAY_ROOT = os.path.abspath(os.path.dirname(calloway.__file__))
sys.path.insert(0, os.path.join(CALLOWAY_ROOT, 'apps'))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))

try:
    from local_settings import DEBUG as LOCAL_DEBUG
    DEBUG = LOCAL_DEBUG
except ImportError:
    DEBUG = False
TEMPLATE_DEBUG = DEBUG

from calloway.settings import *

ADMINS = (
    ('webmaster', 'webmaster@pkgbin.com'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL='webmaster@pkgbin.com'
SERVER_EMAIL='webmaster@pkgbin.com'

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

USE_TZ = True
LANGUAGE_CODE = 'en-us'
USE_I18N = True

try:
    from local_settings import MEDIA_URL_PREFIX
except ImportError:
    MEDIA_URL_PREFIX = "/media/"
try:
    from local_settings import MEDIA_ROOT_PREFIX
except ImportError:
    MEDIA_ROOT_PREFIX = os.path.join(PROJECT_ROOT, 'media')
try:
    from local_settings import MEDIA_ROOT
except ImportError:
    MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'uploads')
try:
    from local_settings import STATIC_ROOT
except ImportError:
    STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')


MEDIA_URL = '%suploads/' % MEDIA_URL_PREFIX
STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX
ADMIN_MEDIA_PREFIX = "%sadmin/" % STATIC_URL

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

MMEDIA_DEFAULT_STORAGE = 'media_storage.MediaStorage'
MMEDIA_IMAGE_UPLOAD_TO = 'image/%Y/%m/%d'
AUTH_PROFILE_MODULE = 'profiles.Profile'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    # 'hunger.middleware.BetaMiddleware',
    'beta_middleware.BetaMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.OpenIDBackend',
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
) + CALLOWAY_TEMPLATE_DIRS

CACHE_BACKEND = 'memcached://localhost:11211/'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'calloway',
    'userena',
    'guardian',
    'easy_thumbnails',
    'profiles',
    'userpypi',
    'userrouter',
    'bootstrapform',
    'djcelery',
    'queued_storage',
    #"kombu.transport.django",
    'hunger',
    'selectable',
    'tastypie',
    'teams',
    'robots',
)

ADMIN_TOOLS_THEMING_CSS = 'calloway/admin/css/theming.css'
ADMIN_TOOLS_MENU = 'menu.CustomMenu'

TINYMCE_JS_URL = '%scalloway/js/tiny_mce/tiny_mce.js' % STATIC_URL
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'js/tiny_mce')

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

DJANGOPYPI_SETTINGS = {
    'PROXY_MISSING': True,
    'RELEASE_FILE_STORAGE': 'media_storage.QueuedUserCloudFilesStorage',
    'RELEASE_UPLOAD_TO': lambda x,y: "%s/%s" % (x.release.package.owner.username, y)
}

#######################
# Userena settings
#######################
ANONYMOUS_USER_ID = -1

USERENA_SIGNIN_REDIRECT_URL = "/%(username)s/"
USERENA_FORBIDDEN_USERNAMES = ('signup', 'signout', 'signin', 'activate', 'me',
        'password', 'pypi', 'pkgbin', 'admin', 'admin_tools', 'username', 'user',)
USERENA_DISABLE_PROFILE_LIST = True
USERENA_HIDE_EMAIL = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#######################
# Celery settings
#######################

import djcelery
djcelery.setup_loader()

BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0
CELERYBEAT_PIDFILE = '/var/run/celerybeat.pid'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

#######################
# Hunger settings
#######################

# BETA_INVITE_CODE_LENGTH
BETA_ENABLE_BETA = True
# BETA_NEVER_ALLOW_VIEWS
BETA_ALWAYS_ALLOW_VIEWS = (
    'userena.views.signin', 
    'userena.views.direct_to_user_template', 
    'userena.views.activate',
    'userpypi.utils._wrapped',
    'tastypie.api.wrapper',
    'tastypie.resources.wrapper',
    'userpypi.views.root',
    'robots.views.rules_list',
)
# BETA_ALWAYS_ALLOW_MODULES
# BETA_ALLOW_FLATPAGES
BETA_SIGNUP_VIEWS = ('userena.views.signup',)
BETA_SIGNUP_CONFIRMATION_VIEW = 'userena.views.profile_detail'
# BETA_REDIRECT_URL
BETA_SIGNUP_URL = '/signup/'
# BETA_EMAIL_TEMPLATES_DIR
# BETA_EMAIL_MODULE
# BETA_EMAIL_CONFIRM_FUNCTION
# BETA_EMAIL_INVITE_FUNCTION

SELECTABLEWRAPPER_SETTINGS = {
    'AUTOCOMPLETESELECT_FIELDS': {
        'userpypi.maintainer.user': 'lookups.UserLookup'
    }
}


try:
    from local_settings import *
except ImportError:
    pass
